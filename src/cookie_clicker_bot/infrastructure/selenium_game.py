"""@file selenium_game.py
@brief Selenium adapter that implements the game port.
"""

import time
from collections.abc import Callable
from pathlib import Path
from typing import Protocol, TypeVar

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.by import By

from cookie_clicker_bot import constants

T = TypeVar("T")


class ElementLike(Protocol):
    """@brief The part of a Selenium element that the adapter uses."""

    @property
    def text(self) -> str:
        """@brief Visible text of the element."""
        ...

    def click(self) -> None:
        """@brief Click the element."""

    def is_displayed(self) -> bool:
        """@brief True when the element is visible."""
        ...


class DriverLike(Protocol):
    """@brief The part of a Selenium driver that the adapter uses."""

    def get(self, url: str) -> None:
        """@brief Load a page."""

    def find_element(self, by: str, value: str) -> ElementLike:
        """@brief Find one element."""
        ...

    def save_screenshot(self, filename: str) -> bool:
        """@brief Write a PNG screenshot."""
        ...

    def quit(self) -> None:
        """@brief Close the browser."""


class SeleniumGame:
    """@brief Plays the game page through a Selenium driver."""

    def __init__(
        self,
        driver: DriverLike,
        timeout_seconds: float = constants.WAIT_TIMEOUT_SECONDS,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        """@brief Wrap a driver.

        @param driver The Selenium driver (or a fake in tests).
        @param timeout_seconds Longest wait for an element.
        @param clock Monotonic clock in seconds.
        @param sleep Pause function used between polls.
        """
        self._driver = driver
        self._timeout = timeout_seconds
        self._clock = clock
        self._sleep = sleep

    def open_game(self) -> None:
        """@brief Load the game page."""
        self._driver.get(constants.GAME_URL)

    def dismiss_language(self) -> None:
        """@brief Pick English, then wait until the big cookie can be clicked."""
        english = self._wait_for(lambda: self._visible(constants.LANGUAGE_ENGLISH_ID))
        english.click()
        self._wait_for(lambda: self._visible(constants.BIG_COOKIE_ID))

    def click_cookie(self) -> None:
        """@brief Click the big cookie once."""
        try:
            self._driver.find_element(By.ID, constants.BIG_COOKIE_ID).click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            # A banner or a re-render covered the cookie for a moment; try again.
            return

    def save_screenshot(self, path: Path) -> None:
        """@brief Write a screenshot of the game to a PNG file.

        @param path Target file; its folder is created when missing.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        self._driver.save_screenshot(str(path))

    def close(self) -> None:
        """@brief Close the browser."""
        self._driver.quit()

    def _visible(self, element_id: str) -> ElementLike | None:
        """@brief Return the element with this id when it exists and is displayed."""
        try:
            element = self._driver.find_element(By.ID, element_id)
        except NoSuchElementException:
            return None
        return element if element.is_displayed() else None

    def _wait_for(self, locate: Callable[[], T | None]) -> T:
        """@brief Poll until `locate` returns a value.

        @param locate Function that returns the value, or None while not ready.
        @return The value.
        @throws TimeoutError When the value is not there within the timeout.
        """
        deadline = self._clock() + self._timeout
        while True:
            found = locate()
            if found is not None:
                return found
            if self._clock() >= deadline:
                message = f"the game page was not ready within {self._timeout} s"
                raise TimeoutError(message)
            self._sleep(constants.POLL_INTERVAL_SECONDS)
