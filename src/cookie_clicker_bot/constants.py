"""@file constants.py
@brief Every constant of the bot: the game address, timings and messages.

Selectors of the game page are added here by the milestone that first uses them.
"""

from typing import Final

## Address of the new version of Cookie Clicker on GitHub Pages (ozh/cookieclicker).
GAME_URL: Final[str] = "https://ozh.github.io/cookieclicker/"

## Total playing time of one run, in seconds (lecture step 4: five minutes).
RUN_DURATION_SECONDS: Final[int] = 300

## Seconds between two checks for an affordable upgrade (lecture step 3).
UPGRADE_CHECK_INTERVAL_SECONDS: Final[int] = 5

## Longest time to wait for an element of the page, in seconds.
WAIT_TIMEOUT_SECONDS: Final[int] = 20

## Folder where screenshots of a container run are written.
SCREENSHOT_DIR: Final[str] = "docs/images"
