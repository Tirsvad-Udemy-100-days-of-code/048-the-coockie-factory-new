"""@file test_upgrades.py
@brief Tests of the rule that picks the upgrade to buy.
"""

from cookie_clicker_bot.domain.upgrades import (
    Upgrade,
    choose_affordable_upgrades,
    choose_best_value,
    choose_most_expensive_affordable,
)

CURSOR = Upgrade("product0", "Cursor", 15)
GRANDMA = Upgrade("product1", "Grandma", 100)
FARM = Upgrade("product2", "Farm", 1100)


def test_choose_picks_the_most_expensive_affordable() -> None:
    assert choose_most_expensive_affordable([CURSOR, GRANDMA, FARM], 105) == GRANDMA


def test_choose_returns_none_when_nothing_is_affordable() -> None:
    assert choose_most_expensive_affordable([CURSOR, GRANDMA], 10) is None


def test_choose_returns_none_without_upgrades() -> None:
    assert choose_most_expensive_affordable([], 1000) is None


def test_choose_accepts_a_price_equal_to_the_cookies() -> None:
    assert choose_most_expensive_affordable([CURSOR, GRANDMA], 100) == GRANDMA


def test_choose_takes_the_first_on_a_tie() -> None:
    twin = Upgrade("product9", "Twin", 100)

    assert choose_most_expensive_affordable([GRANDMA, twin], 500) == GRANDMA


def test_choose_ignores_the_order_of_the_list() -> None:
    assert choose_most_expensive_affordable([GRANDMA, CURSOR], 105) == GRANDMA


def test_plan_skips_an_upgrade_the_remaining_cookies_cannot_pay() -> None:
    assert choose_affordable_upgrades([CURSOR, GRANDMA, FARM], 105) == [GRANDMA]


def test_plan_buys_several_upgrades_most_expensive_first() -> None:
    assert choose_affordable_upgrades([CURSOR, GRANDMA, FARM], 120) == [GRANDMA, CURSOR]


def test_plan_is_empty_when_nothing_is_affordable() -> None:
    assert choose_affordable_upgrades([CURSOR, GRANDMA], 10) == []


def test_plan_is_empty_without_upgrades() -> None:
    assert choose_affordable_upgrades([], 1000) == []


def test_plan_spends_the_whole_budget_on_equal_prices() -> None:
    twin = Upgrade("product9", "Twin", 100)

    assert choose_affordable_upgrades([GRANDMA, twin], 250) == [GRANDMA, twin]
    assert choose_affordable_upgrades([twin, GRANDMA], 150) == [twin]


def test_plan_does_not_change_the_given_list() -> None:
    upgrades = [CURSOR, GRANDMA]

    choose_affordable_upgrades(upgrades, 1000)

    assert upgrades == [CURSOR, GRANDMA]


VALUE_CURSOR = Upgrade("product0", "Cursor", 15, 0.1)
VALUE_GRANDMA = Upgrade("product1", "Grandma", 100, 1.0)
VALUE_FARM = Upgrade("product2", "Farm", 1100, 8.0)


def test_best_value_picks_the_lowest_price_per_cookie_per_second() -> None:
    upgrades = [VALUE_CURSOR, VALUE_GRANDMA, VALUE_FARM]

    assert choose_best_value(upgrades, 2000) == VALUE_GRANDMA


def test_best_value_ignores_what_the_cookies_cannot_pay() -> None:
    upgrades = [VALUE_CURSOR, VALUE_GRANDMA, VALUE_FARM]

    assert choose_best_value(upgrades, 50) == VALUE_CURSOR


def test_best_value_returns_none_when_nothing_is_affordable() -> None:
    assert choose_best_value([VALUE_CURSOR, VALUE_GRANDMA], 10) is None


def test_best_value_returns_none_without_upgrades() -> None:
    assert choose_best_value([], 1000) is None


def test_best_value_takes_the_first_on_a_tie() -> None:
    twin = Upgrade("product9", "Twin", 100, 1.0)

    assert choose_best_value([VALUE_GRANDMA, twin], 500) == VALUE_GRANDMA


def test_best_value_skips_an_upgrade_with_zero_production() -> None:
    idle = Upgrade("product9", "Idle", 10, 0.0)

    assert choose_best_value([idle, VALUE_GRANDMA], 500) == VALUE_GRANDMA


def test_best_value_falls_back_to_the_most_expensive_when_production_is_unknown() -> (
    None
):
    assert choose_best_value([CURSOR, GRANDMA, FARM], 1200) == FARM
