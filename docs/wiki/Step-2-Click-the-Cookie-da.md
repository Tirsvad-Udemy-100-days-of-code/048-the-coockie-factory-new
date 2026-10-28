[English](Step-2-Click-the-Cookie) · **Dansk** · [Bahasa Malaysia](Step-2-Click-the-Cookie-ms)

# Lektionens trin 2: klik på cookien så hurtigt som muligt

![Spillet efter 15 sekunders klikning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-2.png)

## Hvad opgaven går ud på

Lav en bot med Selenium og Python, der klikker på cookien så hurtigt som muligt. Den skal selv lukke sprogvalget, før den går i gang.

## Hvad vi byggede

- `open_game` indlæser siden.
- `dismiss_language` venter, til den engelske knap er synlig, klikker på den og venter derefter, til den store cookie er synlig. Spillet skal bruge nogle sekunder på at starte, efter sproget er valgt, så botten poller (hvert 0,2 sekund, højst 20 sekunder) i stedet for at sove i fast tid.
- `click_cookie` klikker én gang på `#bigCookie`. Hvis et banner eller en gentegning blokerer klikket et øjeblik, prøver botten igen i næste runde.
- En løkke kalder `click_cookie`, indtil tiden er gået. I en kørsel på 15 sekunder i containeren klikkede botten 344 gange, og skærmbilledet ovenfor viser 342 cookies.

```bash
cookie-clicker-bot --headless --duration 15 --screenshot step-2.png
```

## Hvad vi fik ud af dette trin

- **Vent på en betingelse, ikke på et tidsrum.** En fast `sleep` er enten for kort (botten fejler) eller for lang (botten spilder tid). At polle efter "cookien er synlig" er både hurtigere og sikrere.
- **Hold browseren bag en port.** Løkken kender kun `GamePort` (`open_game`, `dismiss_language`, `click_cookie`, ...). Selenium-koden bor i én adapter, så løkken testes med et falsk spil på få millisekunder.
- **Tidsstyr en løkke med et ur, du kan udskifte.** `click_and_buy` tager uret som parameter; testene giver den et falsk ur og kontrollerer antallet af klik helt præcist.
