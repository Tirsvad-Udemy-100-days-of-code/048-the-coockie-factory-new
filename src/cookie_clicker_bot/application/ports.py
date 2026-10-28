"""@file ports.py
@brief The port through which the game loop talks to the game.
"""

from pathlib import Path
from typing import Protocol

from cookie_clicker_bot.domain.upgrades import Upgrade


class GamePort(Protocol):
    """@brief What the bot needs from the game, whatever drives the browser."""

    def open_game(self) -> None:
        """@brief Load the game page."""

    def dismiss_language(self) -> None:
        """@brief Pick English on the language selection and wait for the game."""

    def click_cookie(self) -> None:
        """@brief Click the big cookie once."""

    def cookie_count(self) -> int:
        """@brief Read how many cookies the player has.

        @return The cookie count.
        """
        ...

    def upgrades(self) -> list[Upgrade]:
        """@brief Read the upgrades the player can see in the right-hand pane.

        @return The visible upgrades, affordable or not, in store order.
        """
        ...

    def buy(self, upgrade: Upgrade) -> None:
        """@brief Buy an upgrade by clicking it.

        @param upgrade The upgrade to buy.
        """

    def save_screenshot(self, path: Path) -> None:
        """@brief Write a screenshot of the game to a PNG file.

        @param path Target file; its folder is created when missing.
        """

    def close(self) -> None:
        """@brief Close the browser."""
