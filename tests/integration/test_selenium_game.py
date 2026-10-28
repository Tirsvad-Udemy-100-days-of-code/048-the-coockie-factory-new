"""@file test_selenium_game.py
@brief Tests of the Selenium adapter against a fake driver (no browser).
"""

from collections.abc import Callable
from pathlib import Path

import pytest
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
)

from cookie_clicker_bot import constants
from cookie_clicker_bot.infrastructure.selenium_game import SeleniumGame


class FakeElement:
    """An element that records clicks and may raise on click."""

    def __init__(
        self,
        displayed: Callable[[], bool] = lambda: True,
        click_error: Exception | None = None,
    ) -> None:
        self.text = ""
        self.clicks = 0
        self._displayed = displayed
        self._click_error = click_error

    def click(self) -> None:
        if self._click_error is not None:
            raise self._click_error
        self.clicks += 1

    def is_displayed(self) -> bool:
        return self._displayed()


class FakeDriver:
    """A driver with elements by id."""

    def __init__(self, elements: dict[str, FakeElement] | None = None) -> None:
        self.elements = elements or {}
        self.loaded: list[str] = []
        self.screenshots: list[str] = []
        self.quit_called = False

    def get(self, url: str) -> None:
        self.loaded.append(url)

    def find_element(self, by: str, value: str) -> FakeElement:
        if by != "id" or value not in self.elements:
            raise NoSuchElementException(value)
        return self.elements[value]

    def save_screenshot(self, filename: str) -> bool:
        self.screenshots.append(filename)
        return True

    def quit(self) -> None:
        self.quit_called = True


class FakeTime:
    """A clock that only moves when the fake sleep is called."""

    def __init__(self) -> None:
        self.now = 0.0
        self.sleeps: list[float] = []

    def clock(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


def make_game(driver: FakeDriver, fake_time: FakeTime | None = None) -> SeleniumGame:
    fake_time = fake_time or FakeTime()
    return SeleniumGame(
        driver, timeout_seconds=1.0, clock=fake_time.clock, sleep=fake_time.sleep
    )


def ready_driver() -> FakeDriver:
    return FakeDriver(
        {
            constants.LANGUAGE_ENGLISH_ID: FakeElement(),
            constants.BIG_COOKIE_ID: FakeElement(),
        }
    )


def test_open_game_loads_the_game_address() -> None:
    driver = FakeDriver()

    make_game(driver).open_game()

    assert driver.loaded == [constants.GAME_URL]


def test_dismiss_language_clicks_english_and_waits_for_the_cookie() -> None:
    driver = ready_driver()

    make_game(driver).dismiss_language()

    assert driver.elements[constants.LANGUAGE_ENGLISH_ID].clicks == 1


def test_dismiss_language_polls_until_the_button_is_visible() -> None:
    fake_time = FakeTime()
    driver = ready_driver()
    driver.elements[constants.LANGUAGE_ENGLISH_ID] = FakeElement(
        displayed=lambda: fake_time.now >= 0.4
    )

    make_game(driver, fake_time).dismiss_language()

    assert driver.elements[constants.LANGUAGE_ENGLISH_ID].clicks == 1
    assert fake_time.sleeps == [constants.POLL_INTERVAL_SECONDS] * 2


def test_dismiss_language_times_out_when_the_button_never_shows() -> None:
    fake_time = FakeTime()

    with pytest.raises(TimeoutError):
        make_game(FakeDriver(), fake_time).dismiss_language()

    assert fake_time.now >= 1.0


def test_dismiss_language_times_out_when_the_cookie_never_shows() -> None:
    driver = FakeDriver({constants.LANGUAGE_ENGLISH_ID: FakeElement()})

    with pytest.raises(TimeoutError):
        make_game(driver).dismiss_language()


def test_click_cookie_clicks_the_big_cookie() -> None:
    driver = ready_driver()

    make_game(driver).click_cookie()

    assert driver.elements[constants.BIG_COOKIE_ID].clicks == 1


@pytest.mark.parametrize(
    "error",
    [ElementClickInterceptedException(), StaleElementReferenceException()],
)
def test_click_cookie_ignores_a_covered_or_stale_cookie(error: Exception) -> None:
    driver = FakeDriver({constants.BIG_COOKIE_ID: FakeElement(click_error=error)})

    make_game(driver).click_cookie()


def test_save_screenshot_creates_the_folder_and_calls_the_driver(
    tmp_path: Path,
) -> None:
    driver = FakeDriver()
    target = tmp_path / "images" / "shot.png"

    make_game(driver).save_screenshot(target)

    assert target.parent.is_dir()
    assert driver.screenshots == [str(target)]


def test_close_quits_the_driver() -> None:
    driver = FakeDriver()

    make_game(driver).close()

    assert driver.quit_called
