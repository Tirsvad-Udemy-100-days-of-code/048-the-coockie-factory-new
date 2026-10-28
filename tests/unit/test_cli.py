"""@file test_cli.py
@brief Tests of the command line and the run sequence with a fake game.
"""

from pathlib import Path

import pytest

from cookie_clicker_bot import constants
from cookie_clicker_bot.application.ports import GamePort
from cookie_clicker_bot.cli import main, parse_args
from cookie_clicker_bot.domain.upgrades import Upgrade


class RecordingGame:
    """A game that records every call in order."""

    def __init__(self, fail_on_open: bool = False) -> None:
        self.calls: list[str] = []
        self.screenshots: list[Path] = []
        self._fail_on_open = fail_on_open

    def open_game(self) -> None:
        self.calls.append("open_game")
        if self._fail_on_open:
            message = "boom"
            raise RuntimeError(message)

    def dismiss_language(self) -> None:
        self.calls.append("dismiss_language")

    def click_cookie(self) -> None:
        self.calls.append("click_cookie")

    def cookie_count(self) -> int:
        return 0

    def upgrades(self) -> list[Upgrade]:
        return []

    def buy(self, upgrade: Upgrade) -> None:
        self.calls.append("buy")

    def save_screenshot(self, path: Path) -> None:
        self.calls.append("save_screenshot")
        self.screenshots.append(path)

    def close(self) -> None:
        self.calls.append("close")


def test_parse_args_uses_defaults() -> None:
    args = parse_args([])

    assert args.duration == constants.RUN_DURATION_SECONDS == 300
    assert args.interval == constants.UPGRADE_CHECK_INTERVAL_SECONDS == 5
    assert args.headless is False
    assert args.screenshot_start is None
    assert args.screenshot is None


def test_parse_args_reads_every_option() -> None:
    args = parse_args(
        [
            "--headless",
            "--duration",
            "10",
            "--interval",
            "2.5",
            "--screenshot-start",
            "a.png",
            "--screenshot",
            "b.png",
        ]
    )

    assert args.headless is True
    assert args.duration == 10
    assert args.interval == 2.5
    assert args.screenshot_start == Path("a.png")
    assert args.screenshot == Path("b.png")


def test_main_opens_dismisses_and_closes() -> None:
    game = RecordingGame()

    code = main(["--duration", "0"], lambda _headless: game)

    assert code == 0
    assert game.calls == ["open_game", "dismiss_language", "close"]


def test_main_passes_headless_to_the_factory() -> None:
    seen: list[bool] = []

    def factory(headless: bool) -> GamePort:
        seen.append(headless)
        return RecordingGame()

    main(["--headless", "--duration", "0"], factory)

    assert seen == [True]


def test_main_takes_both_screenshots_when_asked() -> None:
    game = RecordingGame()

    main(
        ["--duration", "0", "--screenshot-start", "s.png", "--screenshot", "e.png"],
        lambda _headless: game,
    )

    assert game.screenshots == [Path("s.png"), Path("e.png")]
    assert game.calls[-1] == "close"


def test_main_takes_no_screenshot_by_default() -> None:
    game = RecordingGame()

    main(["--duration", "0"], lambda _headless: game)

    assert game.screenshots == []


def test_main_closes_the_game_when_an_error_is_raised() -> None:
    game = RecordingGame(fail_on_open=True)

    with pytest.raises(RuntimeError, match="boom"):
        main(["--duration", "0"], lambda _headless: game)

    assert game.calls == ["open_game", "close"]
