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


def choose_most_expensive_affordable(
    upgrades: Sequence[Upgrade], cookies: int
) -> Upgrade | None:
    """@brief Pick the most expensive upgrade the player can pay for.

    @param upgrades The visible upgrades, in store order.
    @param cookies The cookies the player has.
    @return The chosen upgrade (the first on a tie), or None when none is affordable.
    """
    affordable = [upgrade for upgrade in upgrades if upgrade.price <= cookies]
    if not affordable:
        return None
    return max(affordable, key=lambda upgrade: upgrade.price)
