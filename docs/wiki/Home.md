**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Cookie Clicker Bot

A Selenium bot that plays [Cookie Clicker](https://ozh.github.io/cookieclicker/) for you: it clicks the big cookie, buys the most expensive upgrade it can afford every 5 seconds and prints the cookies per second after 5 minutes. It is day 48 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*.

## The five lecture steps

| Step | What the bot learns | Page |
| --- | --- | --- |
| 1 | Get to know the game and its page | [Step 1](Step-1-Get-to-Know-the-Game) |
| 2 | Dismiss the language selection and click the cookie | [Step 2](Step-2-Click-the-Cookie) |
| 3 | Every 5 seconds buy the most expensive affordable upgrade | [Step 3](Step-3-Buy-Upgrades) |
| 4 | Stop after 5 minutes and print the cookies per second | [Step 4](Step-4-Five-Minute-Run) |
| 5 | Tweak the strategy and compare runs | [Step 5](Step-5-Improve-the-Strategy) |

Each page shows a screenshot of the game at that step and explains what we gained in it.

## Run it

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
cookie-clicker-bot
```

To keep your desktop free, run it in Docker (headless Chromium): `docker build -t cookie-clicker-bot .` and `docker run --rm cookie-clicker-bot`. The README of the repository has the full instructions for Windows, Linux and macOS, and for the tests.

## Results

| Run | cookies/second |
| --- | --- |
| Lecture step 4: check every 5 seconds, buy one (alone on the computer) | 18.9 |
| Lecture step 5: check every 10 seconds, buy one (best of the comparison) | 18.2 |
| Best value rule, check every 5 seconds (alone on the computer, two runs) | 17.9 and 18.8 |

The best value rule (`cookie-clicker-bot --best-value`) buys the affordable upgrade with the lowest price per cookie per second. It was not better than the assignment's rule (18 and 18.8 in the same conditions). The rows come from different conditions; [Step 5](Step-5-Improve-the-Strategy) explains how they were measured.

## How the code is organised

- `domain/`: the rules (parsing the page text, choosing the upgrade), with no Selenium.
- `application/`: the game loop, which talks to the game through a port.
- `infrastructure/`: the Selenium adapter and the Chromium factory.
- `constants.py`: every constant.

The tests use a fake driver, so they run in a second and need no browser.
