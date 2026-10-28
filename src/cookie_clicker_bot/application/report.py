"""@file report.py
@brief The text the program prints when a run ends.
"""

from cookie_clicker_bot import constants


def format_result(cookies_per_second: float) -> str:
    """@brief Build the result line, for example `cookies/second: 8.5`.

    @param cookies_per_second The cookies per second at the end of the run.
    @return The line, without a trailing newline.
    """
    return constants.RESULT_MESSAGE_TEMPLATE.format(
        cookies_per_second=cookies_per_second
    )
