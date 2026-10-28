[English](Step-1-Get-to-Know-the-Game) · **Dansk** · [Bahasa Malaysia](Step-1-Get-to-Know-the-Game-ms)

# Lektionens trin 1: lær spillet at kende

![Spillet lige efter sproget er valgt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-1.png)

## Hvad opgaven går ud på

Åbn den nye version af Cookie Clicker (ozh.github.io/cookieclicker) og lær, hvordan den fungerer, før du skriver kode.

## Hvad vi fandt

Vi åbnede siden i en headless Chromium i en Docker-container og kiggede på dens HTML. Det, botten har brug for:

| Hvad | Hvor på siden |
| --- | --- |
| Engelsk i sprogvalget | `#langSelect-EN` |
| Den store cookie | `#bigCookie` |
| Antal cookies og cookies pr. sekund | `#cookies` (og `#cookiesPerSecond` inde i den) |
| Butikken | `#products`, med `#product0` (Cursor), `#product1` (Grandma), `#product2` (Farm) osv. |
| Et produkts navn og pris | `.productName` og `.price` inde i produktet |
| Har jeg råd? | produktet har klassen `unlocked enabled` (et produkt, du endnu ikke har råd til, er `unlocked disabled`; et skjult er `locked disabled`) |

Godt at vide:

- Spillet beder om et sprog, første gang siden indlæses. Botten skal vælge et af sig selv.
- Antallet er skrevet som tekst: `3 cookies`, `5,000 cookies`, og for store tal på to linjer, `1.235` og `million cookies`.
- Et cookie-banner ("Got it!") sidder nederst på siden. Botten klikker aldrig på det, fordi det er et samtykkebanner, der tilhører den, der spiller; botten arbejder uden om det (se [Step 4](Step-4-Five-Minute-Run-da)).

Alle disse id'er og selektorer står ét sted, i `constants.py`.

## Hvad vi fik ud af dette trin

- **Læs siden, før du koder.** Et kort kig på den rigtige HTML sparede timers gætværk; hver eneste selektor i botten stammer fra dette trin.
- **Hav selektorerne ét sted.** Hvis spillet ændrer et id, er rettelsen én linje i `constants.py`.
- **Kør browseren i en container.** Det samme Docker-image, der kører botten, tager skærmbillederne, så der åbner intet på dit eget skrivebord, og hver kørsel starter fra den samme rene browser.
