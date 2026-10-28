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
