[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Cookie Clicker Bot

En Selenium-bot, der spiller [Cookie Clicker](https://ozh.github.io/cookieclicker/) for dig: den klikker på den store cookie, køber den dyreste opgradering, den har råd til, hvert 5. sekund og udskriver cookies pr. sekund efter 5 minutter. Det er dag 48 i Udemys *100 Days of Code: The Complete Python Pro Bootcamp*.

## De fem trin i lektionen

| Trin | Hvad botten lærer | Side |
| --- | --- | --- |
| 1 | Lær spillet og dets side at kende | [Step 1](Step-1-Get-to-Know-the-Game-da) |
| 2 | Luk sprogvalget og klik på cookien | [Step 2](Step-2-Click-the-Cookie-da) |
| 3 | Køb den dyreste opgradering, der er råd til, hvert 5. sekund | [Step 3](Step-3-Buy-Upgrades-da) |
| 4 | Stop efter 5 minutter og udskriv cookies pr. sekund | [Step 4](Step-4-Five-Minute-Run-da) |
| 5 | Justér strategien og sammenlign kørsler | [Step 5](Step-5-Improve-the-Strategy-da) |

Hver side viser et skærmbillede af spillet på det pågældende trin og forklarer, hvad vi fik ud af det.

## Kør den

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
cookie-clicker-bot
```

For at holde dit skrivebord frit kan du køre den i Docker (headless Chromium): `docker build -t cookie-clicker-bot .` og `docker run --rm cookie-clicker-bot`. Repositoriets README har den fulde vejledning til Windows, Linux og macOS samt til testene.

## Resultater

| Kørsel | cookies/second |
| --- | --- |
| Lektionens trin 4: tjek hvert 5. sekund, køb én (alene på computeren) | 18.9 |
| Lektionens trin 5: tjek hvert 10. sekund, køb én (bedste i sammenligningen) | 18.2 |
| Reglen bedste værdi, tjek hvert 5. sekund (alene på computeren, to kørsler) | 17.9 og 18.8 |

Reglen bedste værdi (`cookie-clicker-bot --best-value`) køber den opgradering, der er råd til, med den laveste pris pr. cookie pr. sekund. Den var ikke bedre end opgavens regel (18 og 18.8 under de samme forhold). Rækkerne stammer fra forskellige forhold; [Step 5](Step-5-Improve-the-Strategy-da) forklarer, hvordan de blev målt.

## Sådan er koden organiseret

- `domain/`: reglerne (fortolkning af sidens tekst, valg af opgradering) uden Selenium.
- `application/`: spillets løkke, som taler med spillet gennem en port.
- `infrastructure/`: Selenium-adapteren og Chromium-fabrikken.
- `constants.py`: alle konstanter.

Testene bruger en falsk driver, så de kører på et sekund og kræver ingen browser.
