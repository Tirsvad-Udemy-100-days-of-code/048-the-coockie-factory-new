"""@file test_parsing.py
@brief Tests of the parsing of prices and cookie counts.
"""

import pytest

from cookie_clicker_bot.domain.parsing import parse_amount, parse_cookie_count


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("15", 15),
        ("0", 0),
        ("1,100", 1100),
        ("130,000", 130000),
        (" 100 ", 100),
        ("1.4 million", 1_400_000),
        ("20 million", 20_000_000),
        ("1.235 million", 1_235_000),
        ("3.5 Billion", 3_500_000_000),
        ("2 thousand", 2000),
        ("1 decillion", 10**33),
    ],
)
def test_parse_amount_reads_prices(text: str, expected: int) -> None:
    assert parse_amount(text) == expected


@pytest.mark.parametrize(
    "text", ["", "   ", "abc", "1.4 gazillion", "1 2 3", "-5", "nan", "million"]
)
def test_parse_amount_rejects_garbage(text: str) -> None:
    with pytest.raises(ValueError, match="not an amount of cookies"):
        parse_amount(text)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("120 cookies\nper second: 0", 120),
        ("5,000 cookies\nper second: 0", 5000),
        ("1 cookie\nper second: 0", 1),
        ("0 cookies\nper second: 0", 0),
        ("1.235\nmillion cookies\nper second: 0", 1_235_000),
        ("3.500\nbillion cookies\nper second: 12.5", 3_500_000_000),
        ("120 cookies", 120),
    ],
)
def test_parse_cookie_count_reads_the_count_element(text: str, expected: int) -> None:
    assert parse_cookie_count(text) == expected


def test_parse_cookie_count_rejects_text_without_a_count() -> None:
    with pytest.raises(ValueError, match="not an amount of cookies"):
        parse_cookie_count("per second: 0")
