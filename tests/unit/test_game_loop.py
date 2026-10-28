"""@file test_game_loop.py
@brief Tests of the game loop with a fake game and a fake clock.
"""

from pathlib import Path

from cookie_clicker_bot.application.game_loop import click_cookie, click_cookie_for


class FakeGame:
    """A game that only counts clicks."""

    def __init__(self) -> None:
        self.clicks = 0

    def open_game(self) -> None:
        pass

    def dismiss_language(self) -> None:
        pass

    def click_cookie(self) -> None:
        self.clicks += 1

    def save_screenshot(self, path: Path) -> None:
        pass

    def close(self) -> None:
        pass


class FakeClock:
    """A clock that moves forward one second each time it is read."""

    def __init__(self) -> None:
        self.now = 0.0

    def __call__(self) -> float:
        value = self.now
        self.now += 1.0
        return value


def test_click_cookie_delegates_to_the_game() -> None:
    game = FakeGame()

    click_cookie(game)

    assert game.clicks == 1


def test_click_cookie_for_clicks_until_the_deadline() -> None:
    game = FakeGame()

    # Reads: deadline = 0 + 5; the loop reads 1, 2, 3, 4 (clicks) and 5 (stops).
    clicks = click_cookie_for(game, 5, FakeClock())

    assert clicks == 4
    assert game.clicks == 4


def test_click_cookie_for_does_not_click_when_duration_is_zero() -> None:
    game = FakeGame()

    assert click_cookie_for(game, 0, FakeClock()) == 0
    assert game.clicks == 0
