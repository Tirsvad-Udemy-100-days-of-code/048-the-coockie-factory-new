"""@file parsing.py
@brief Turn the texts of the game page into whole numbers of cookies.
"""

from decimal import Decimal, InvalidOperation

from cookie_clicker_bot import constants


def parse_amount(text: str) -> int:
    """@brief Read an amount such as `1,100`, `15` or `1.4 million`.

    @param text The text of a price or a count, with optional thousands commas
        and an optional magnitude word.
    @return The amount as a whole number.
    @throws ValueError When the text is not an amount.
    """
    return int(_read_amount(text))


def parse_cookies_per_second(text: str) -> float:
    """@brief Read the text of `#cookiesPerSecond`, such as `per second: 1,234.5`.

    @param text The visible text of the element, with its `per second:` label.
    @return The cookies per second.
    @throws ValueError When the text holds no amount.
    """
    amount = text.lower().replace(constants.PER_SECOND_MARKER, "", 1).strip()
    return float(_read_amount(amount.removeprefix(":")))


def parse_cookie_count(text: str) -> int:
    """@brief Read the cookie count from the whole text of the `#cookies` element.

    The text looks like `5,000 cookies` then a line `per second: 0`; a big count
    puts the magnitude word on the second line: `1.235`, `million cookies`.

    @param text The visible text of the element.
    @return The number of cookies.
    @throws ValueError When the text holds no count.
    """
    count = text.lower().split(constants.PER_SECOND_MARKER)[0]
    for word in constants.COOKIE_WORDS:
        count = count.replace(word, "")
    return parse_amount(" ".join(count.split()))


def _read_amount(text: str) -> Decimal:
    """@brief Read an amount with optional commas and magnitude word, exactly."""
    words = text.strip().lower().replace(",", "").split()
    if not 1 <= len(words) <= 2:
        raise ValueError(_message(text))
    multiplier = 1
    if len(words) == 2:
        multiplier = constants.MAGNITUDE_MULTIPLIERS.get(words[1], 0)
        if multiplier == 0:
            raise ValueError(_message(text))
    try:
        number = Decimal(words[0])
    except InvalidOperation:
        raise ValueError(_message(text)) from None
    if not number.is_finite() or number < 0:
        raise ValueError(_message(text))
    return number * multiplier


def _message(text: str) -> str:
    """@brief Build the error message for a text that is not an amount."""
    return f"not an amount of cookies: {text!r}"
