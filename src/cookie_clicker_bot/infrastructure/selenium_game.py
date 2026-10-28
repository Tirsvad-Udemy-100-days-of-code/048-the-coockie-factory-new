"""@file selenium_game.py
@brief Selenium adapter that implements the game port.
"""

import time
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Any, Protocol, TypeVar

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    JavascriptException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.by import By

from cookie_clicker_bot import constants
from cookie_clicker_bot.domain.parsing import (
    parse_amount,
    parse_cookie_count,
    parse_cookies_per_second,
)
from cookie_clicker_bot.domain.upgrades import Upgrade

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

    def get_attribute(self, name: str) -> str | None:
        """@brief Read an attribute of the element."""
        ...

    def find_element(self, by: str, value: str) -> "ElementLike":
        """@brief Find one element inside this element."""
        ...


class DriverLike(Protocol):
    """@brief The part of a Selenium driver that the adapter uses."""

    def get(self, url: str) -> None:
        """@brief Load a page."""

    def find_element(self, by: str, value: str) -> ElementLike:
        """@brief Find one element."""
        ...

    def find_elements(self, by: str, value: str) -> Sequence[ElementLike]:
        """@brief Find every element that matches."""
        ...

    def save_screenshot(self, filename: str) -> bool:
        """@brief Write a PNG screenshot."""
        ...

    def execute_script(self, script: str, *args: Any) -> Any:  # noqa: ANN401
        """@brief Run JavaScript in the page; the arguments are `arguments[n]`."""
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

    def cookie_count(self) -> int:
        """@brief Read how many cookies the player has.

        @return The cookie count.
        """
        return self._read_again_if_stale(
            lambda: parse_cookie_count(
                self._driver.find_element(By.ID, constants.COOKIE_COUNT_ID).text
            )
        )

    def cookies_per_second(self) -> float:
        """@brief Read how many cookies the player makes each second.

        @return The cookies per second.
        """
        return self._read_again_if_stale(
            lambda: parse_cookies_per_second(
                self._driver.find_element(By.ID, constants.COOKIES_PER_SECOND_ID).text
            )
        )

    def upgrades(self) -> list[Upgrade]:
        """@brief Read the upgrades the player can see in the right-hand pane.

        @return The visible upgrades, affordable or not, in store order.
        """
        return self._read_again_if_stale(self._read_upgrades)

    def _read_upgrades(self) -> list[Upgrade]:
        """@brief Find the visible products and read each one."""
        products = self._driver.find_elements(
            By.CSS_SELECTOR, constants.VISIBLE_PRODUCT_SELECTOR
        )
        production = self._read_production()
        return [self._read_upgrade(product, production) for product in products]

    def _read_production(self) -> list[float]:
        """@brief Read the cookies per second of one unit of every product.

        @return The numbers by product index; empty when the page does not tell.
        """
        try:
            production = self._driver.execute_script(constants.JS_PRODUCTION_SCRIPT)
        except JavascriptException:
            return []
        return production if isinstance(production, list) else []

    def _read_again_if_stale(self, read: Callable[[], T]) -> T:
        """@brief Run a read; repeat it while the page re-renders under it.

        @throws StaleElementReferenceException When every attempt went stale.
        """
        for _ in range(constants.STALE_READ_ATTEMPTS - 1):
            try:
                return read()
            except StaleElementReferenceException:
                self._sleep(constants.POLL_INTERVAL_SECONDS)
        return read()

    def buy(self, upgrade: Upgrade) -> bool:
        """@brief Buy an upgrade by clicking its product.

        @param upgrade The upgrade to buy.
        @return True only when a click really reached the product.
        """
        try:
            element = self._driver.find_element(By.ID, upgrade.key)
            try:
                element.click()
            except ElementClickInterceptedException:
                # The cookie-consent banner covers the lower products. Click from
                # inside the page instead; the banner itself is never clicked.
                self._driver.execute_script(constants.JS_CLICK_SCRIPT, element)
        except StaleElementReferenceException:
            # The pane re-rendered under us; the next check retries.
            return False
        return True

    def save_screenshot(self, path: Path) -> None:
        """@brief Write a screenshot of the game to a PNG file.

        @param path Target file; its folder is created when missing.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        self._driver.save_screenshot(str(path))

    def close(self) -> None:
        """@brief Close the browser."""
        self._driver.quit()

    @staticmethod
    def _read_upgrade(product: ElementLike, production: Sequence[float]) -> Upgrade:
        """@brief Read the id, name, price and production of one product element."""
        name = product.find_element(By.CSS_SELECTOR, constants.PRODUCT_NAME_SELECTOR)
        price = product.find_element(By.CSS_SELECTOR, constants.PRODUCT_PRICE_SELECTOR)
        key = product.get_attribute(constants.ID_ATTRIBUTE) or ""
        return Upgrade(
            key=key,
            name=name.text.strip(),
            price=parse_amount(price.text),
            cookies_per_second=SeleniumGame._production_of(key, production),
        )

    @staticmethod
    def _production_of(key: str, production: Sequence[float]) -> float | None:
        """@brief Look up the production of the product with this element id."""
        index = key.removeprefix(constants.PRODUCT_ID_PREFIX)
        if not index.isdigit() or int(index) >= len(production):
            return None
        value = production[int(index)]
        return float(value) if isinstance(value, int | float) else None

    def _visible(self, element_id: str) -> ElementLike | None:
        """@brief Return the element with this id when it exists and is displayed."""
        try:
            element = self._driver.find_element(By.ID, element_id)
            return element if element.is_displayed() else None
        except (NoSuchElementException, StaleElementReferenceException):
            # Not there yet, or the page re-rendered under us: poll again.
            return None

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
