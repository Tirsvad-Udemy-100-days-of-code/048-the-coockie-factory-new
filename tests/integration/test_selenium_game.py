"""@file test_selenium_game.py
@brief Tests of the Selenium adapter against a fake driver (no browser).
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
)

from cookie_clicker_bot import constants
from cookie_clicker_bot.domain.upgrades import Upgrade
from cookie_clicker_bot.infrastructure.selenium_game import SeleniumGame


class FakeElement:
    """An element that records clicks and may raise on click."""

    def __init__(
        self,
        displayed: Callable[[], bool] = lambda: True,
        click_error: Exception | None = None,
        text: str = "",
        attributes: dict[str, str] | None = None,
        children: dict[str, "FakeElement"] | None = None,
    ) -> None:
        self.text = text
        self.clicks = 0
        self._displayed = displayed
        self._click_error = click_error
        self._attributes = attributes or {}
        self._children = children or {}

    def get_attribute(self, name: str) -> str | None:
        return self._attributes.get(name)

    def find_element(self, by: str, value: str) -> "FakeElement":
        if by != "css selector" or value not in self._children:
            raise NoSuchElementException(value)
        return self._children[value]

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
        self.groups: dict[str, list[FakeElement]] = {}
        self.loaded: list[str] = []
        self.screenshots: list[str] = []
        self.quit_called = False
        self.scripts: list[tuple[str, FakeElement]] = []

    def execute_script(self, script: str, *args: Any) -> None:  # noqa: ANN401
        self.scripts.append((script, args[0]))

    def get(self, url: str) -> None:
        self.loaded.append(url)

    def find_element(self, by: str, value: str) -> FakeElement:
        if by != "id" or value not in self.elements:
            raise NoSuchElementException(value)
        return self.elements[value]

    def find_elements(self, by: str, value: str) -> list[FakeElement]:
        if by != "css selector":
            return []
        return self.groups.get(value, [])

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


def stale_once() -> Callable[[], bool]:
    """Return an `is_displayed` that goes stale on the first call only."""
    calls: list[int] = []

    def displayed() -> bool:
        calls.append(1)
        if len(calls) == 1:
            raise StaleElementReferenceException
        return True

    return displayed


def test_dismiss_language_survives_a_cookie_that_goes_stale_once() -> None:
    driver = ready_driver()
    driver.elements[constants.BIG_COOKIE_ID] = FakeElement(displayed=stale_once())

    make_game(driver).dismiss_language()

    assert driver.elements[constants.LANGUAGE_ENGLISH_ID].clicks == 1


def test_dismiss_language_survives_a_button_that_goes_stale_once() -> None:
    driver = ready_driver()
    driver.elements[constants.LANGUAGE_ENGLISH_ID] = FakeElement(displayed=stale_once())

    make_game(driver).dismiss_language()

    assert driver.elements[constants.LANGUAGE_ENGLISH_ID].clicks == 1


def test_dismiss_language_survives_a_lookup_that_goes_stale_once() -> None:
    driver = ready_driver()
    real_find = driver.find_element
    calls: list[int] = []

    def find_element(by: str, value: str) -> FakeElement:
        calls.append(1)
        if len(calls) == 1:
            raise StaleElementReferenceException
        return real_find(by, value)

    driver.find_element = find_element  # type: ignore[method-assign]

    make_game(driver).dismiss_language()

    assert driver.elements[constants.LANGUAGE_ENGLISH_ID].clicks == 1


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


def make_product(key: str, name: str, price: str) -> FakeElement:
    return FakeElement(
        attributes={"id": key},
        children={
            constants.PRODUCT_NAME_SELECTOR: FakeElement(text=name),
            constants.PRODUCT_PRICE_SELECTOR: FakeElement(text=price),
        },
    )


def test_cookie_count_reads_the_cookie_counter() -> None:
    driver = FakeDriver(
        {
            constants.COOKIE_COUNT_ID: FakeElement(
                text="1.235\nmillion cookies\nper second: 0"
            )
        }
    )

    assert make_game(driver).cookie_count() == 1_235_000


def test_cookies_per_second_reads_its_element() -> None:
    driver = FakeDriver(
        {constants.COOKIES_PER_SECOND_ID: FakeElement(text="per second: 1,234.5")}
    )

    assert make_game(driver).cookies_per_second() == 1234.5


def test_upgrades_reads_the_visible_products() -> None:
    driver = FakeDriver()
    driver.groups[constants.VISIBLE_PRODUCT_SELECTOR] = [
        make_product("product0", "Cursor", "15"),
        make_product("product2", "Farm", "1,100"),
    ]

    assert make_game(driver).upgrades() == [
        Upgrade("product0", "Cursor", 15),
        Upgrade("product2", "Farm", 1100),
    ]


class StaleOnceText(FakeElement):
    """An element whose text goes stale on the first read."""

    def __init__(self, text: str) -> None:
        super().__init__()
        self._text = text
        self._reads = 0

    @property
    def text(self) -> str:
        self._reads += 1
        if self._reads == 1:
            raise StaleElementReferenceException
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value


def test_cookie_count_retries_once_when_the_counter_goes_stale() -> None:
    driver = FakeDriver({constants.COOKIE_COUNT_ID: StaleOnceText("42 cookies")})

    assert make_game(driver).cookie_count() == 42


def test_cookies_per_second_retries_once_when_the_element_goes_stale() -> None:
    driver = FakeDriver(
        {constants.COOKIES_PER_SECOND_ID: StaleOnceText("per second: 3.5")}
    )

    assert make_game(driver).cookies_per_second() == 3.5


def test_upgrades_retries_once_when_a_product_goes_stale() -> None:
    product = make_product("product0", "Cursor", "15")
    product.get_attribute = _stale_once_then(product.get_attribute)  # type: ignore[assignment]
    driver = FakeDriver()
    driver.groups[constants.VISIBLE_PRODUCT_SELECTOR] = [product]

    assert make_game(driver).upgrades() == [Upgrade("product0", "Cursor", 15)]


def test_cookie_count_gives_up_when_the_counter_stays_stale() -> None:
    driver = FakeDriver()
    driver.find_element = _always_stale  # type: ignore[method-assign]

    with pytest.raises(StaleElementReferenceException):
        make_game(driver).cookie_count()


def _always_stale(by: str, value: str) -> FakeElement:
    raise StaleElementReferenceException


def _stale_once_then(
    original: Callable[[str], str | None],
) -> Callable[[str], str | None]:
    calls: list[int] = []

    def get_attribute(name: str) -> str | None:
        calls.append(1)
        if len(calls) == 1:
            raise StaleElementReferenceException
        return original(name)

    return get_attribute


def test_upgrades_is_empty_when_no_product_is_visible() -> None:
    assert make_game(FakeDriver()).upgrades() == []


def test_buy_clicks_the_product_with_the_upgrade_key() -> None:
    driver = FakeDriver({"product1": FakeElement()})

    bought = make_game(driver).buy(Upgrade("product1", "Grandma", 100))

    assert bought is True
    assert driver.elements["product1"].clicks == 1
    assert driver.scripts == []


def test_buy_clicks_through_javascript_when_a_banner_covers_the_product() -> None:
    element = FakeElement(click_error=ElementClickInterceptedException())
    driver = FakeDriver({"product1": element})

    bought = make_game(driver).buy(Upgrade("product1", "Grandma", 100))

    assert bought is True
    assert driver.scripts == [(constants.JS_CLICK_SCRIPT, element)]


def test_buy_returns_false_for_a_stale_product() -> None:
    driver = FakeDriver(
        {"product1": FakeElement(click_error=StaleElementReferenceException())}
    )

    assert make_game(driver).buy(Upgrade("product1", "Grandma", 100)) is False
    assert driver.scripts == []


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
