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

    def __init__(self, fail_on_open: bool = False, buy_succeeds: bool = True) -> None:
        self._buy_succeeds = buy_succeeds
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
        return 1000

    def cookies_per_second(self) -> float:
        return 8.5

    def upgrades(self) -> list[Upgrade]:
        return [Upgrade("product0", "Cursor", 15)]

    def buy(self, upgrade: Upgrade) -> bool:
        self.calls.append("buy")
        return self._buy_succeeds

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


def test_main_prints_exactly_one_result_line_on_stdout(
    capsys: pytest.CaptureFixture[str], caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level("INFO")

    main(["--duration", "0"], lambda _headless: RecordingGame())

    out = capsys.readouterr().out
    assert out == "cookies/second: 8.5" + chr(10)
    assert "clicked the cookie" not in out
    assert "clicked the cookie" in caplog.text


def test_main_logs_bought_only_for_real_purchases(
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level("INFO")

    main(["--duration", "0.05", "--interval", "0.001"], lambda _h: RecordingGame())
    assert "bought Cursor" in caplog.text

    caplog.clear()
    game = RecordingGame(buy_succeeds=False)
    main(["--duration", "0.05", "--interval", "0.001"], lambda _h: game)
    assert "buy" in game.calls
    assert "bought Cursor" not in caplog.text
    assert "bought 0 upgrades" in caplog.text


def test_main_prints_nothing_on_stdout_when_the_run_fails(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(RuntimeError, match="boom"):
        main(["--duration", "0"], lambda _headless: RecordingGame(fail_on_open=True))

    assert capsys.readouterr().out == ""


def test_parse_args_buys_one_upgrade_unless_buy_all_is_given() -> None:
    assert parse_args([]).buy_all is False
    assert parse_args(["--buy-all"]).buy_all is True


def test_parse_args_best_value_is_off_by_default() -> None:
    assert parse_args([]).best_value is False
    assert parse_args(["--best-value"]).best_value is True


def test_parse_args_rejects_buy_all_together_with_best_value(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as exit_info:
        parse_args(["--buy-all", "--best-value"])

    assert exit_info.value.code == 2
    assert "not allowed with" in capsys.readouterr().err


def test_main_logs_the_best_value_strategy(
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level("INFO")

    main(["--duration", "0", "--best-value"], lambda _h: RecordingGame())

    assert "strategy best-value" in caplog.text


@pytest.mark.parametrize("value", ["0", "-1", "abc", "nan"])
def test_parse_args_rejects_an_interval_that_is_not_positive(
    value: str, capsys: pytest.CaptureFixture[str]
) -> None:
    with pytest.raises(SystemExit) as exit_info:
        parse_args(["--interval", value])

    assert exit_info.value.code == 2
    assert "greater than 0" in capsys.readouterr().err


def test_main_logs_the_interval_and_the_strategy(
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level("INFO")

    main(["--duration", "0"], lambda _h: RecordingGame())
    assert "every 5 seconds, strategy buy-one" in caplog.text

    caplog.clear()
    main(
        ["--duration", "0", "--interval", "2", "--buy-all"], lambda _h: RecordingGame()
    )
    assert "every 2.0 seconds, strategy buy-all" in caplog.text


def test_main_buy_all_buys_every_affordable_upgrade_per_check(
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level("INFO")
    game = RecordingGame()

    main(["--duration", "0.05", "--interval", "0.001", "--buy-all"], lambda _h: game)

    assert "bought Cursor" in caplog.text
