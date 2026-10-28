"""@file ports.py
@brief The port through which the game loop talks to the game.
"""

from pathlib import Path
from typing import Protocol


class GamePort(Protocol):
    """@brief What the bot needs from the game, whatever drives the browser."""

    def open_game(self) -> None:
        """@brief Load the game page."""

    def dismiss_language(self) -> None:
        """@brief Pick English on the language selection and wait for the game."""

    def click_cookie(self) -> None:
        """@brief Click the big cookie once."""

    def save_screenshot(self, path: Path) -> None:
        """@brief Write a screenshot of the game to a PNG file.

        @param path Target file; its folder is created when missing.
        """

    def close(self) -> None:
        """@brief Close the browser."""
