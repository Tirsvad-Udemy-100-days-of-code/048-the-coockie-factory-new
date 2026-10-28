**English** · [Dansk](Step-3-Buy-Upgrades-da) · [Bahasa Malaysia](Step-3-Buy-Upgrades-ms)

# Lecture step 3: buy the most expensive affordable upgrade

![The game after 45 seconds of clicking and buying](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-3.png)

## What the assignment asks

Every 5 seconds, look at the right-hand pane, find the upgrades you can afford, and buy the most expensive one. For example, with 105 cookies both Cursor (15) and Grandma (100) are affordable, so the bot buys Grandma. The hints point to `split`, `strip` and `replace` for turning the page text into numbers.

## What we built

- `parse_amount` and `parse_cookie_count` turn page text into numbers. They remove the word `cookies`, drop everything after `per second`, take away the thousands commas with `replace`, and understand words such as `1.4 million`. Examples: `5,000 cookies` gives 5000; `1.235` and `million cookies` on two lines gives 1,235,000.
- `SeleniumGame.upgrades` reads every visible product: its id, its name and its price.
- `choose_most_expensive_affordable(upgrades, cookies)` is a pure function: of the upgrades whose price is not above the cookies, return the most expensive one, or nothing. It is tested with the example above (105 cookies gives Grandma).
- `click_and_buy` keeps clicking, and when `check_interval_seconds` (5 by default) have passed it reads the count, chooses, and buys.
- In a 45 second container run the bot bought 8 upgrades, and the screenshot shows the Cursors and Grandmas it owns.

## What we gained in this step

- **The hard part is the text, not the click.** The same number appears as `120`, `5,000`, `1.4 million` and on two lines. Parsing is a small pure function with many test cases, so it is safe to change.
- **Keep the rule away from the browser.** "Buy the most expensive affordable upgrade" is one function that knows nothing about Selenium. That is why step 5 could add a second rule without touching the browser code.
- **Do not count a purchase you did not make.** The first version logged a purchase whenever it clicked. A real run showed the click did not always reach the product, so `buy` now says whether it did, and only real purchases are counted (see [Step 4](Step-4-Five-Minute-Run)).
