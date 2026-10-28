"""@file test_game_loop.py
@brief Tests of the game loop with a fake game and a fake clock.
"""

from pathlib import Path

from cookie_clicker_bot.application.game_loop import (
    PlayResult,
    buy_most_expensive_upgrade,
    click_and_buy,
    click_cookie,
)
from cookie_clicker_bot.domain.upgrades import Upgrade

CURSOR = Upgrade("product0", "Cursor", 15)
GRANDMA = Upgrade("product1", "Grandma", 100)


class FakeClock:
    """A clock that only moves when the fake game is clicked."""

    def __init__(self) -> None:
        self.now = 0.0

    def __call__(self) -> float:
        return self.now


class FakeGame:
    """A game with a cookie count and upgrades; each click takes one second."""

    def __init__(
        self,
        cookies: int = 0,
        upgrades: list[Upgrade] | None = None,
        clock: FakeClock | None = None,
        buy_succeeds: bool = True,
    ) -> None:
        self.buy_succeeds = buy_succeeds
        self.clicks = 0
        self.cookies = cookies
        self.available = upgrades or []
        self.bought: list[Upgrade] = []
        self.buy_times: list[float] = []
        self._clock = clock

    def open_game(self) -> None:
        pass

    def dismiss_language(self) -> None:
        pass

    def click_cookie(self) -> None:
        self.clicks += 1
        if self._clock is not None:
            self._clock.now += 1.0

    def cookie_count(self) -> int:
        return self.cookies

    def cookies_per_second(self) -> float:
        return 0.0

    def upgrades(self) -> list[Upgrade]:
        return self.available

    def buy(self, upgrade: Upgrade) -> bool:
        self.bought.append(upgrade)
        if self._clock is not None:
            self.buy_times.append(self._clock.now)
        return self.buy_succeeds

    def save_screenshot(self, path: Path) -> None:
        pass

    def close(self) -> None:
        pass


def test_click_cookie_delegates_to_the_game() -> None:
    game = FakeGame()

    click_cookie(game)

    assert game.clicks == 1


def test_buy_most_expensive_upgrade_buys_the_best_affordable() -> None:
    game = FakeGame(cookies=105, upgrades=[CURSOR, GRANDMA])

    bought = buy_most_expensive_upgrade(game)

    assert bought == GRANDMA
    assert game.bought == [GRANDMA]


def test_buy_most_expensive_upgrade_buys_nothing_when_too_poor() -> None:
    game = FakeGame(cookies=10, upgrades=[CURSOR, GRANDMA])

    assert buy_most_expensive_upgrade(game) is None
    assert game.bought == []


def test_click_and_buy_checks_the_upgrades_every_interval() -> None:
    clock = FakeClock()
    game = FakeGame(cookies=105, upgrades=[CURSOR, GRANDMA], clock=clock)

    result = click_and_buy(game, 12, 5, clock)

    assert result == PlayResult(
        clicks=12, purchases=("Grandma", "Grandma"), elapsed_seconds=12.0
    )
    # The checks fall in the iterations that start at 5 s and 10 s; each click then
    # moves the fake clock on by one second.
    assert game.buy_times == [6.0, 11.0]


def test_click_and_buy_does_not_check_before_the_first_interval() -> None:
    clock = FakeClock()
    game = FakeGame(cookies=105, upgrades=[GRANDMA], clock=clock)

    result = click_and_buy(game, 4, 5, clock)

    assert result == PlayResult(clicks=4, purchases=(), elapsed_seconds=4.0)
    assert game.bought == []


def test_click_and_buy_records_only_real_purchases() -> None:
    clock = FakeClock()
    game = FakeGame(cookies=10, upgrades=[CURSOR, GRANDMA], clock=clock)

    result = click_and_buy(game, 11, 5, clock)

    assert result.clicks == 11
    assert result.purchases == ()


def test_buy_most_expensive_upgrade_returns_none_when_the_click_fails() -> None:
    game = FakeGame(cookies=105, upgrades=[CURSOR, GRANDMA], buy_succeeds=False)

    assert buy_most_expensive_upgrade(game) is None
    assert game.bought == [GRANDMA]


def test_click_and_buy_does_not_record_a_purchase_when_the_click_fails() -> None:
    clock = FakeClock()
    game = FakeGame(cookies=105, upgrades=[GRANDMA], clock=clock, buy_succeeds=False)

    result = click_and_buy(game, 12, 5, clock)

    assert game.buy_times == [6.0, 11.0]
    assert result.purchases == ()


def test_click_and_buy_does_not_click_when_duration_is_zero() -> None:
    clock = FakeClock()
    game = FakeGame(clock=clock)

    assert click_and_buy(game, 0, 5, clock) == PlayResult(
        clicks=0, purchases=(), elapsed_seconds=0.0
    )


def test_click_and_buy_stops_at_the_deadline_and_reports_elapsed_time() -> None:
    clock = FakeClock()
    game = FakeGame(clock=clock)

    result = click_and_buy(game, 300, 5, clock)

    assert result.clicks == 300
    assert result.elapsed_seconds == 300.0
