"""@file game_loop.py
@brief The game loop of the bot, written against the game port.
"""

import time
from collections.abc import Callable

from cookie_clicker_bot.application.ports import GamePort


def click_cookie(game: GamePort) -> None:
    """@brief Click the big cookie once (lecture step 2).

    @param game The game to play.
    """
    game.click_cookie()


def click_cookie_for(
    game: GamePort,
    duration_seconds: float,
    clock: Callable[[], float] = time.monotonic,
) -> int:
    """@brief Click the cookie as fast as possible until the time is up.

    @param game The game to play.
    @param duration_seconds How long to keep clicking.
    @param clock Monotonic clock in seconds; a test passes a fake one.
    @return The number of clicks made.
    """
    deadline = clock() + duration_seconds
    clicks = 0
    while clock() < deadline:
        click_cookie(game)
        clicks += 1
    return clicks
