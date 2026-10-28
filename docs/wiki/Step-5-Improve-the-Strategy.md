**English** · [Dansk](Step-5-Improve-the-Strategy-da) · [Bahasa Malaysia](Step-5-Improve-the-Strategy-ms)

# Lecture step 5: tweak the algorithm

![The game after the best run, checking every 10 seconds](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-5.png)

## What the assignment asks

Try another check interval (every second, every 10 seconds) or buy all affordable upgrades, and see whether the cookies per second go up.

## What we built

- `--interval SECONDS` sets the time between upgrade checks. It must be greater than 0; the default stays 5 seconds.
- `--buy-all` buys every upgrade that still fits in the cookies you have, the most expensive first (`choose_affordable_upgrades`). Without it the bot buys one upgrade, the most expensive affordable one (`choose_most_expensive_affordable`).
- Both rules are pure functions in the domain package, so they are unit tested without a browser. The strategy is a value (`BuyStrategy`), not a flag spread through the code.

```bash
cookie-clicker-bot --interval 10
cookie-clicker-bot --interval 1 --buy-all
```

## What we measured

Each row is a full 300 second run in a Docker container. Five containers ran at the same time on one computer, in two batches, so the numbers are good for comparing the rows with each other but a run alone is faster (our solo baseline of lecture step 4 was 18.9).

| Check every | Strategy | Batch 1 | Batch 2 |
| --- | --- | --- | --- |
| 1 second | buy one | 13.5 | 13.5 |
| 1 second | buy all | 13.5 | 13.5 |
| 5 seconds (assignment) | buy one | 15.5 | 15.5 |
| 5 seconds | buy all | crashed, see below | 14.5 |
| 10 seconds | buy one | **18.2** | **18.2** |

The best result is the 10 second interval with buy one. Why:

- Checking more often is not better. Every check reads the page and takes time away from clicking, and the most expensive affordable product is usually only a little better than the cheaper one you could have bought a moment before.
- Buy all makes no difference early in the game: only Cursor and Grandma are affordable, and the bot buys them anyway. It would matter later, when the cookie count holds several products at once.

## A smarter rule: best value

`--best-value` does not look at the price alone. The game tells how many cookies per second one unit of each product makes, and the bot buys the affordable product with the lowest price per cookie per second (`choose_best_value`). Cursor costs 15 and makes 0.1 (150 cookies for each cookie per second), Grandma costs 100 and makes 1 (100 for each), so Grandma is the better deal even though it costs more.

```bash
cookie-clicker-bot --best-value
```

Each row is a full 300 second run alone in a Docker container, one after the other, check every 5 seconds:

| Run | Strategy | cookies/second | Bought |
| --- | --- | --- | --- |
| 1 | most expensive affordable | 18 | 30 Cursor, 15 Grandma |
| 2 | best value | 17.9 | 29 Cursor, 15 Grandma |
| 3 | most expensive affordable | 18.8 | 28 Cursor, 16 Grandma |
| 4 | best value | 18.8 | 28 Cursor, 16 Grandma |

The smarter rule is **not better**: the two rules differ by less than the difference between two runs of the same rule (18 and 18.8). The reason is the same as for buy all. In 5 seconds the bot clicks about 125 cookies, so only Cursor and Grandma are ever affordable, and both rules buy nearly the same. A rule that looks at value would matter once several products are affordable at once, for example with a longer check interval or after the first minutes of luck.

## What we gained in this step

- **Small, pure rules are easy to compare.** Because the choice of upgrade does not touch Selenium, a new strategy is a new function plus a test.
- **Measure, do not guess.** The result we expected (more checks, more cookies) was the opposite of what the runs showed.
- **A second real bug.** The first batch crashed in one container: the game rewrites the counter every frame, and a computer under load made our single retry fail. The read now retries five times with a short pause. A test with a fake driver that goes stale four times shows it.
- **Fair comparisons need the same conditions.** We ran the rows at the same time and report two batches, because one run can be lucky.
- **A better idea still has to be measured.** The best value rule is correct on paper and made no difference in the runs, because the bot never has enough cookies to choose between more than two products.
