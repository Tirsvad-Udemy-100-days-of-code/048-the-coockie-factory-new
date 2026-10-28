"""@file test_constants.py
@brief Smoke test: the assignment's timings are the ones in constants.py.
"""

from cookie_clicker_bot import constants


def test_run_lasts_five_minutes() -> None:
    assert constants.RUN_DURATION_SECONDS == 5 * 60


def test_upgrades_are_checked_every_five_seconds() -> None:
    assert constants.UPGRADE_CHECK_INTERVAL_SECONDS == 5


def test_game_address_is_https() -> None:
    assert constants.GAME_URL.startswith("https://")
