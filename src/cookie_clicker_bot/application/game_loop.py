"""@file game_loop.py
@brief The game loop of the bot, written against the game port.
"""

import time
from collections.abc import Callable
from dataclasses import dataclass

from cookie_clicker_bot.application.ports import GamePort
from cookie_clicker_bot.domain.upgrades import Upgrade, choose_most_expensive_affordable


@dataclass(frozen=True, slots=True)
class PlayResult:
    """@brief What a run did."""

    ## Number of clicks on the big cookie.
    clicks: int
    ## Names of the upgrades bought, in the order they were bought.
    purchases: tuple[str, ...]
    ## Seconds the run lasted, measured with the clock given to `click_and_buy`.
    elapsed_seconds: float


def click_cookie(game: GamePort) -> None:
    """@brief Click the big cookie once (lecture step 2).

    @param game The game to play.
    """
    game.click_cookie()


def buy_most_expensive_upgrade(game: GamePort) -> Upgrade | None:
    """@brief Buy the most expensive upgrade the player can afford (lecture step 3).

    @param game The game to play.
    @return The upgrade that was bought, or None when nothing was affordable or
        the click did not reach the product.
    """
    chosen = choose_most_expensive_affordable(game.upgrades(), game.cookie_count())
    if chosen is not None and game.buy(chosen):
        return chosen
    return None


def click_and_buy(
    game: GamePort,
    duration_seconds: float,
    check_interval_seconds: float,
    clock: Callable[[], float] = time.monotonic,
) -> PlayResult:
    """@brief Click the cookie nonstop and check the upgrades at every interval.

    @param game The game to play.
    @param duration_seconds How long to play.
    @param check_interval_seconds Time between two upgrade checks; the first check
        comes one interval after the start.
    @param clock Monotonic clock in seconds; a test passes a fake one.
    @return The clicks, the names of the upgrades bought in order, and the time spent.
    """
    start = clock()
    deadline = start + duration_seconds
    next_check = start + check_interval_seconds
    clicks = 0
    purchases: list[str] = []
    while (now := clock()) < deadline:
        click_cookie(game)
        clicks += 1
        if now >= next_check:
            next_check = now + check_interval_seconds
            bought = buy_most_expensive_upgrade(game)
            if bought is not None:
                purchases.append(bought.name)
    return PlayResult(
        clicks=clicks, purchases=tuple(purchases), elapsed_seconds=clock() - start
    )
