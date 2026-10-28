"""@file constants.py
@brief Every constant of the bot: the game address, selectors, timings and messages.

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

## Id of the button that picks English on the language selection page.
LANGUAGE_ENGLISH_ID: Final[str] = "langSelect-EN"

## Id of the big cookie in the left-hand pane.
BIG_COOKIE_ID: Final[str] = "bigCookie"

## Id of the element that shows the cookie count and the cookies per second.
COOKIE_COUNT_ID: Final[str] = "cookies"

## Seconds between two polls while waiting for an element.
POLL_INTERVAL_SECONDS: Final[float] = 0.2

## Environment variable that names the Chromium binary (set in the Docker image).
CHROME_BIN_ENV: Final[str] = "CHROME_BIN"

## Environment variable that names the Chromium driver (set in the Docker image).
CHROMEDRIVER_PATH_ENV: Final[str] = "CHROMEDRIVER_PATH"

## Size of the browser window in pixels, so the screenshots look the same every time.
WINDOW_SIZE: Final[str] = "1366,768"

## Chromium arguments needed to run headless inside a container.
HEADLESS_BROWSER_ARGUMENTS: Final[tuple[str, ...]] = (
    "--headless=new",
    "--no-sandbox",
    "--disable-dev-shm-usage",
)
