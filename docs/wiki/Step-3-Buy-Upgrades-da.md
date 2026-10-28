[English](Step-3-Buy-Upgrades) · **Dansk** · [Bahasa Malaysia](Step-3-Buy-Upgrades-ms)

# Lektionens trin 3: køb den dyreste opgradering, der er råd til

![Spillet efter 45 sekunders klikning og køb](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-3.png)

## Hvad opgaven går ud på

Hvert 5. sekund skal botten se på ruden til højre, finde de opgraderinger, der er råd til, og købe den dyreste. Med 105 cookies er der for eksempel råd til både Cursor (15) og Grandma (100), så botten køber Grandma. Hintene peger på `split`, `strip` og `replace` til at omdanne sidens tekst til tal.

## Hvad vi byggede

- `parse_amount` og `parse_cookie_count` omdanner sidens tekst til tal. De fjerner ordet `cookies`, dropper alt efter `per second`, fjerner tusindtalskommaerne med `replace` og forstår ord som `1.4 million`. Eksempler: `5,000 cookies` giver 5000; `1.235` og `million cookies` på to linjer giver 1.235.000.
- `SeleniumGame.upgrades` læser hvert synligt produkt: dets id, navn og pris.
- `choose_most_expensive_affordable(upgrades, cookies)` er en ren funktion: blandt de opgraderinger, hvis pris ikke overstiger antallet af cookies, returnerer den den dyreste eller ingenting. Den er testet med eksemplet ovenfor (105 cookies giver Grandma).
- `click_and_buy` bliver ved med at klikke, og når `check_interval_seconds` (som standard 5) er gået, læser den antallet, vælger og køber.
- I en kørsel på 45 sekunder i containeren købte botten 8 opgraderinger, og skærmbilledet viser de Cursors og Grandmas, den ejer.

## Hvad vi fik ud af dette trin

- **Det svære er teksten, ikke klikket.** Det samme tal optræder som `120`, `5,000`, `1.4 million` og på to linjer. Fortolkningen er en lille ren funktion med mange testcases, så den er sikker at ændre.
- **Hold reglen væk fra browseren.** "Køb den dyreste opgradering, der er råd til" er én funktion, der intet ved om Selenium. Derfor kunne trin 5 tilføje en anden regel uden at røre browserkoden.
- **Tæl ikke et køb, du ikke har foretaget.** Den første version loggede et køb, hver gang den klikkede. En rigtig kørsel viste, at klikket ikke altid nåede produktet, så `buy` melder nu, om det gjorde, og kun rigtige køb tælles (se [Step 4](Step-4-Five-Minute-Run-da)).
