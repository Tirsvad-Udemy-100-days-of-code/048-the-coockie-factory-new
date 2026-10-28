"""@file test_report.py
@brief Tests of the result line.
"""

import pytest

from cookie_clicker_bot.application.report import format_result


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (8.5, "cookies/second: 8.5"),
        (0.0, "cookies/second: 0"),
        (1234.5, "cookies/second: 1234.5"),
        (1_200_000.0, "cookies/second: 1200000"),
    ],
)
def test_format_result_writes_the_summary_line(value: float, expected: str) -> None:
    assert format_result(value) == expected
