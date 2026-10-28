"""@file cli.py
@brief Command-line entry point (the composition root of the bot).
"""

import argparse
import logging
from collections.abc import Callable, Sequence
from pathlib import Path

from cookie_clicker_bot import constants
from cookie_clicker_bot.application.game_loop import click_and_buy
from cookie_clicker_bot.application.ports import GamePort
from cookie_clicker_bot.application.report import format_result
from cookie_clicker_bot.domain.buy_strategy import BuyStrategy
from cookie_clicker_bot.infrastructure.browser import create_driver
from cookie_clicker_bot.infrastructure.selenium_game import SeleniumGame

logger = logging.getLogger(__name__)


def create_game(headless: bool) -> GamePort:
    """@brief Build the Selenium game.

    @param headless True to run Chromium without a window.
    @return The game, ready to open.
    """
    return SeleniumGame(create_driver(headless))


def positive_float(text: str) -> float:
    """@brief Read a number greater than zero from the command line.

    @param text The argument text.
    @return The number.
    @throws argparse.ArgumentTypeError When the text is not a number above zero.
    """
    message = constants.POSITIVE_NUMBER_ERROR_TEMPLATE.format(value=text)
    try:
        value = float(text)
    except ValueError:
        raise argparse.ArgumentTypeError(message) from None
    if not value > 0:
        raise argparse.ArgumentTypeError(message)
    return value


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """@brief Read the command line.

    @param argv Arguments without the program name; None reads `sys.argv`.
    @return The parsed options.
    """
    parser = argparse.ArgumentParser(
        prog="cookie-clicker-bot",
        description=(
            "Plays Cookie Clicker: clicks the big cookie as fast as it can "
            "and buys upgrades."
        ),
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=constants.RUN_DURATION_SECONDS,
        help="seconds to play (default: %(default)s)",
    )
    parser.add_argument(
        "--interval",
        type=positive_float,
        default=constants.UPGRADE_CHECK_INTERVAL_SECONDS,
        help="seconds between upgrade checks, greater than 0 (default: %(default)s)",
    )
    choice = parser.add_mutually_exclusive_group()
    choice.add_argument(
        "--buy-all",
        action="store_true",
        help=(
            "at each check buy every affordable upgrade, most expensive first "
            "(default: buy only the most expensive affordable one)"
        ),
    )
    choice.add_argument(
        "--best-value",
        action="store_true",
        help=(
            "at each check buy the affordable upgrade with the lowest price per "
            "cookie per second"
        ),
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


def choose_strategy(args: argparse.Namespace) -> BuyStrategy:
    """@brief Turn the purchase options into a strategy.

    @param args The parsed options.
    @return BUY_ALL, BEST_VALUE or, by default, BUY_ONE.
    """
    if args.buy_all:
        return BuyStrategy.BUY_ALL
    if args.best_value:
        return BuyStrategy.BEST_VALUE
    return BuyStrategy.BUY_ONE


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
        strategy = choose_strategy(args)
        logger.info(
            "checking upgrades every %s seconds, strategy %s",
            args.interval,
            strategy.value,
        )
        result = click_and_buy(game, args.duration, args.interval, strategy=strategy)
        for name in result.purchases:
            logger.info("bought %s", name)
        logger.info(
            "clicked the cookie %d times and bought %d upgrades in %.1f seconds",
            result.clicks,
            len(result.purchases),
            result.elapsed_seconds,
        )
        cookies_per_second = game.cookies_per_second()
        logger.info("%s", format_result(cookies_per_second))
        if args.screenshot is not None:
            game.save_screenshot(args.screenshot)
    finally:
        game.close()
    # The program's required result: the only line written to stdout (logs use stderr).
    print(format_result(cookies_per_second))
    return 0
