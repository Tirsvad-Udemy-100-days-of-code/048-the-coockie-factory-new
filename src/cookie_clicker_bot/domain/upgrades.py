"""@file upgrades.py
@brief The rule for which upgrade to buy.
"""

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Upgrade:
    """@brief A product of the right-hand pane that can be bought."""

    ## Id of the product element on the page (product0 .. product19).
    key: str
    ## Name shown in the store, for example Cursor.
    name: str
    ## Price in cookies.
    price: int
    ## Cookies per second one unit makes; None when the page did not tell.
    cookies_per_second: float | None = None


def choose_affordable_upgrades(
    upgrades: Sequence[Upgrade], cookies: int
) -> list[Upgrade]:
    """@brief Plan a buy-all round: as many upgrades as the cookies pay for.

    Walks the upgrades from most expensive to cheapest (the list order on a tie) and
    takes each one whose price still fits in the cookies left.

    @param upgrades The visible upgrades, in store order.
    @param cookies The cookies the player has.
    @return The upgrades to buy, most expensive first; empty when none is affordable.
    """
    plan: list[Upgrade] = []
    remaining = cookies
    for upgrade in sorted(upgrades, key=lambda candidate: -candidate.price):
        if upgrade.price <= remaining:
            plan.append(upgrade)
            remaining -= upgrade.price
    return plan


def choose_best_value(upgrades: Sequence[Upgrade], cookies: int) -> Upgrade | None:
    """@brief Pick the affordable upgrade that pays for itself fastest.

    The value of an upgrade is its price divided by the cookies per second it makes,
    so the lowest ratio wins. Upgrades with unknown or zero production are skipped;
    when none of the affordable ones has a known production the rule falls back to
    the most expensive affordable upgrade.

    @param upgrades The visible upgrades, in store order.
    @param cookies The cookies the player has.
    @return The chosen upgrade (the first on a tie), or None when none is affordable.
    """
    producing = [
        upgrade
        for upgrade in upgrades
        if upgrade.price <= cookies
        and upgrade.cookies_per_second is not None
        and upgrade.cookies_per_second > 0
    ]
    if not producing:
        return choose_most_expensive_affordable(upgrades, cookies)
    return min(
        producing,
        key=lambda upgrade: upgrade.price / (upgrade.cookies_per_second or 1.0),
    )


def choose_most_expensive_affordable(
    upgrades: Sequence[Upgrade], cookies: int
) -> Upgrade | None:
    """@brief Pick the most expensive upgrade the player can pay for.

    @param upgrades The visible upgrades, in store order.
    @param cookies The cookies the player has.
    @return The chosen upgrade (the first on a tie), or None when none is affordable.
    """
    plan = choose_affordable_upgrades(upgrades, cookies)
    return plan[0] if plan else None
