[English](Step-4-Five-Minute-Run) · **Dansk** · [Bahasa Malaysia](Step-4-Five-Minute-Run-ms)

# Lektionens trin 4: stop efter fem minutter og udskriv cookies pr. sekund

![Spillet efter kørslen på fem minutter](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-4.png)

## Hvad opgaven går ud på

Efter 5 minutter stopper botten og udskriver `cookies/second`.

## Hvad vi byggede

- `click_and_buy` kører til en deadline målt med et monotont ur (`time.monotonic`), så kørslen varer præcis `RUN_DURATION_SECONDS` (300) og driver ikke, hvis et klik er langsomt.
- `SeleniumGame.cookies_per_second` læser spillets eget tal fra `#cookiesPerSecond` (for eksempel `per second: 18.9`), og `parse_cookies_per_second` omdanner det til et tal, også værdier som `1.2 million`.
- `format_result` bygger linjen `cookies/second: 18.9`. Programmet udskriver præcis denne ene linje på standard output; loggen (klik, køb, forløbet tid) går til standard error, så `cookie-clicker-bot > result.txt` kun beholder resultatet.

## Vores første resultat

En fuld kørsel i Docker-containeren med opgavens regler (tjek hvert 5. sekund, køb det dyreste produkt, der er råd til):

| Mål | Værdi |
| --- | --- |
| Varighed | 300,0 sekunder |
| Klik | 7.666 |
| Købte produkter | 45 (29 Cursor, 16 Grandma) |
| Resultat | `cookies/second: 18.9` |

## Hvad vi fik ud af dette trin

- **En tidsstyret løkke, der ikke driver.** Et monotont ur og en deadline er mere pålidelige end at tælle sleeps.
- **Adskilt output til mennesker og til programmer.** Logning går til standard error og resultatet til standard output.
- **To rigtige fejl fundet ved en rigtig kørsel.** Spillet gentegner siden, efter sproget er valgt, så et element kan blive forældet mellem det øjeblik, man finder det, og det øjeblik, man bruger det; løsningen er at slå det op igen. Et cookie-banner dækker en del af butikken, så et klik på et produkt kan blive opfanget; botten klikker så med JavaScript og tæller kun et køb, når klikket gik igennem. Enhedstests med en falsk driver afslørede ingen af problemerne, og derfor har hvert trin en containerkørsel og et skærmbillede.
- **Et udgangspunkt.** 18,9 cookies pr. sekund er det tal, trin 5 forsøger at slå.
