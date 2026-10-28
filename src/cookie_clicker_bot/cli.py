"""@file cli.py
@brief Command-line entry point (the composition root of the bot).
"""

import argparse
import logging
from collections.abc import Callable, Sequence
from pathlib import Path

from cookie_clicker_bot import constants
from cookie_clicker_bot.application.game_loop import click_cookie_for
from cookie_clicker_bot.application.ports import GamePort
from cookie_clicker_bot.infrastructure.browser import create_driver
from cookie_clicker_bot.infrastructure.selenium_game import SeleniumGame

logger = logging.getLogger(__name__)


def create_game(headless: bool) -> GamePort:
    """@brief Build the Selenium game.

    @param headless True to run Chromium without a window.
    @return The game, ready to open.
    """
    return SeleniumGame(create_driver(headless))


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """@brief Read the command line.

    @param argv Arguments without the program name; None reads `sys.argv`.
    @return The parsed options.
    """
    parser = argparse.ArgumentParser(
        prog="cookie-clicker-bot",
        description="Plays Cookie Clicker: clicks the big cookie as fast as it can.",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=constants.RUN_DURATION_SECONDS,
        help="seconds to play (default: %(default)s)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="run Chromium without a window (the Docker image does this)",
    )
    parser.add_argument(
        "--screenshot-start",
        type=Path,
        help="write a screenshot of the game before the first click",
    )
    parser.add_argument(
        "--screenshot",
        type=Path,
        help="write a screenshot of the game when the run ends",
    )
    return parser.parse_args(argv)


def main(
    argv: Sequence[str] | None = None,
    game_factory: Callable[[bool], GamePort] = create_game,
) -> int:
    """@brief Start the bot.

    @param argv Arguments without the program name; None reads `sys.argv`.
    @param game_factory Builds the game; a test passes a fake.
    @return Process exit code, 0 when the run finished.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = parse_args(argv)
    game = game_factory(args.headless)
    try:
        game.open_game()
        game.dismiss_language()
        if args.screenshot_start is not None:
            game.save_screenshot(args.screenshot_start)
        clicks = click_cookie_for(game, args.duration)
        logger.info("clicked the cookie %d times in %s seconds", clicks, args.duration)
        if args.screenshot is not None:
            game.save_screenshot(args.screenshot)
    finally:
        game.close()
    return 0
