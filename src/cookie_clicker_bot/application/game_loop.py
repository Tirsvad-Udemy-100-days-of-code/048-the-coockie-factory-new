"""@file game_loop.py
@brief The game loop of the bot, written against the game port.
"""

import time
from collections.abc import Callable
from dataclasses import dataclass

from cookie_clicker_bot.application.ports import GamePort
from cookie_clicker_bot.domain.buy_strategy import BuyStrategy
from cookie_clicker_bot.domain.upgrades import (
    Upgrade,
    choose_affordable_upgrades,
    choose_best_value,
    choose_most_expensive_affordable,
)


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


def buy_best_value_upgrade(game: GamePort) -> Upgrade | None:
    """@brief Buy the affordable upgrade with the lowest price per cookie per second.

    @param game The game to play.
    @return The upgrade that was bought, or None when nothing was affordable or
        the click did not reach the product.
    """
    chosen = choose_best_value(game.upgrades(), game.cookie_count())
    if chosen is not None and game.buy(chosen):
        return chosen
    return None


def buy_upgrades(game: GamePort, strategy: BuyStrategy) -> list[Upgrade]:
    """@brief Do one purchase round with the given strategy (lecture step 5).

    @param game The game to play.
    @param strategy BUY_ONE buys the most expensive affordable upgrade, BUY_ALL buys
        every upgrade the cookies pay for, BEST_VALUE buys the one with the lowest
        price per cookie per second.
    @return The upgrades really bought, in order; a click that missed is left out.
    """
    if strategy is not BuyStrategy.BUY_ALL:
        buy_one = (
            buy_best_value_upgrade
            if strategy is BuyStrategy.BEST_VALUE
            else buy_most_expensive_upgrade
        )
        bought = buy_one(game)
        return [] if bought is None else [bought]
    plan = choose_affordable_upgrades(game.upgrades(), game.cookie_count())
    return [upgrade for upgrade in plan if game.buy(upgrade)]


def click_and_buy(
    game: GamePort,
    duration_seconds: float,
    check_interval_seconds: float,
    clock: Callable[[], float] = time.monotonic,
    strategy: BuyStrategy = BuyStrategy.BUY_ONE,
) -> PlayResult:
    """@brief Click the cookie nonstop and check the upgrades at every interval.

    @param game The game to play.
    @param duration_seconds How long to play.
    @param check_interval_seconds Time between two upgrade checks; the first check
        comes one interval after the start.
    @param clock Monotonic clock in seconds; a test passes a fake one.
    @param strategy What to buy at each check.
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
            purchases.extend(upgrade.name for upgrade in buy_upgrades(game, strategy))
    return PlayResult(
        clicks=clicks, purchases=tuple(purchases), elapsed_seconds=clock() - start
    )
