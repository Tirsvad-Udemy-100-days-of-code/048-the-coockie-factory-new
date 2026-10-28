**English** · [Dansk](Step-4-Five-Minute-Run-da) · [Bahasa Malaysia](Step-4-Five-Minute-Run-ms)

# Lecture step 4: stop after five minutes and print cookies per second

![The game after the five minute run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-4.png)

## What the assignment asks

After 5 minutes the bot stops and prints `cookies/second`.

## What we built

- `click_and_buy` runs until a deadline measured with a monotonic clock (`time.monotonic`), so the run lasts exactly `RUN_DURATION_SECONDS` (300) and does not drift if a click is slow.
- `SeleniumGame.cookies_per_second` reads the game's own figure from `#cookiesPerSecond` (for example `per second: 18.9`), and `parse_cookies_per_second` turns it into a number, including values such as `1.2 million`.
- `format_result` builds the line `cookies/second: 18.9`. The program prints exactly this one line on standard output; the log (clicks, purchases, elapsed time) goes to standard error, so `cookie-clicker-bot > result.txt` keeps only the result.

## Our first result

A full run in the Docker container with the assignment's rules (check every 5 seconds, buy the most expensive affordable product):

| Measure | Value |
| --- | --- |
| Duration | 300.0 seconds |
| Clicks | 7,666 |
| Products bought | 45 (29 Cursor, 16 Grandma) |
| Result | `cookies/second: 18.9` |

## What we gained in this step

- **A timed loop that does not drift.** A monotonic clock and a deadline are more reliable than counting sleeps.
- **Separate output for people and for programs.** Logging goes to standard error and the result to standard output.
- **Two real bugs found by a real run.** The game re-renders after the language is chosen, so an element can go stale between finding it and using it; the fix is to look again. A cookie banner covers part of the store, so a click on a product can be intercepted; the bot then clicks with JavaScript and counts a purchase only when the click went through. Unit tests with a fake driver did not show either problem, which is why every step has a container run and a screenshot.
- **A baseline.** 18.9 cookies per second is the number step 5 tries to beat.
