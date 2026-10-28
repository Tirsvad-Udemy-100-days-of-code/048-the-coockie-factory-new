"""@file buy_strategy.py
@brief How many upgrades the bot buys at each check.
"""

from enum import Enum


class BuyStrategy(Enum):
    """@brief The purchase strategy of one upgrade check (lecture step 5)."""

    ## Buy only the most expensive affordable upgrade (the assignment).
    BUY_ONE = "buy-one"
    ## Buy every upgrade the cookies pay for, most expensive first.
    BUY_ALL = "buy-all"
