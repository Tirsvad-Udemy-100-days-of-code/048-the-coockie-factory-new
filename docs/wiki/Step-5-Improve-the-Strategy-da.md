[English](Step-5-Improve-the-Strategy) · **Dansk** · [Bahasa Malaysia](Step-5-Improve-the-Strategy-ms)

# Lektionens trin 5: justér algoritmen

![Spillet efter den bedste kørsel, med tjek hvert 10. sekund](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-5.png)

## Hvad opgaven går ud på

Prøv et andet tjekinterval (hvert sekund, hvert 10. sekund) eller køb alle opgraderinger, der er råd til, og se, om cookies pr. sekund stiger.

## Hvad vi byggede

- `--interval SECONDS` sætter tiden mellem tjek af opgraderinger. Den skal være større end 0; standarden forbliver 5 sekunder.
- `--buy-all` køber alle opgraderinger, der stadig kan være inden for de cookies, du har, den dyreste først (`choose_affordable_upgrades`). Uden den køber botten én opgradering, den dyreste, der er råd til (`choose_most_expensive_affordable`).
- Begge regler er rene funktioner i domænepakken, så de enhedstestes uden en browser. Strategien er en værdi (`BuyStrategy`), ikke et flag spredt rundt i koden.

```bash
cookie-clicker-bot --interval 10
cookie-clicker-bot --interval 1 --buy-all
```

## Hvad vi målte

Hver række er en fuld kørsel på 300 sekunder i en Docker-container. Fem containere kørte samtidig på én computer, i to hold, så tallene er gode til at sammenligne rækkerne med hinanden, men en kørsel alene er hurtigere (vores solo-udgangspunkt fra lektionens trin 4 var 18,9).

| Tjek hvert | Strategi | Hold 1 | Hold 2 |
| --- | --- | --- | --- |
| 1 sekund | køb én | 13.5 | 13.5 |
| 1 sekund | køb alle | 13.5 | 13.5 |
| 5 sekunder (opgaven) | køb én | 15.5 | 15.5 |
| 5 sekunder | køb alle | styrtede ned, se nedenfor | 14.5 |
| 10 sekunder | køb én | **18.2** | **18.2** |

Det bedste resultat er intervallet på 10 sekunder med køb én. Hvorfor:

- At tjekke oftere er ikke bedre. Hvert tjek læser siden og tager tid fra klikningen, og det dyreste produkt, der er råd til, er som regel kun lidt bedre end det billigere, man kunne have købt et øjeblik før.
- Køb alle gør ingen forskel tidligt i spillet: der er kun råd til Cursor og Grandma, og det køber botten alligevel. Det ville få betydning senere, når antallet af cookies rummer flere produkter på én gang.

## En smartere regel: bedste værdi

`--best-value` ser ikke kun på prisen. Spillet fortæller, hvor mange cookies pr. sekund én enhed af hvert produkt giver, og botten køber det produkt, der er råd til, med den laveste pris pr. cookie pr. sekund (`choose_best_value`). Cursor koster 15 og giver 0,1 (150 cookies for hver cookie pr. sekund), Grandma koster 100 og giver 1 (100 for hver), så Grandma er det bedste køb, selv om den koster mere.

```bash
cookie-clicker-bot --best-value
```

Hver række er en fuld kørsel på 300 sekunder alene i en Docker-container, den ene efter den anden, tjek hvert 5. sekund:

| Kørsel | Strategi | cookies/sekund | Købt |
| --- | --- | --- | --- |
| 1 | dyreste, der er råd til | 18 | 30 Cursor, 15 Grandma |
| 2 | bedste værdi | 17.9 | 29 Cursor, 15 Grandma |
| 3 | dyreste, der er råd til | 18.8 | 28 Cursor, 16 Grandma |
| 4 | bedste værdi | 18.8 | 28 Cursor, 16 Grandma |

Den smartere regel er **ikke bedre**: de to regler adskiller sig mindre end to kørsler af den samme regel (18 og 18,8). Årsagen er den samme som for køb alle. På 5 sekunder klikker botten omkring 125 cookies, så der er kun råd til Cursor og Grandma, og begge regler køber næsten det samme. En regel, der ser på værdi, ville få betydning, når der er råd til flere produkter på én gang, for eksempel med et længere tjekinterval.

## Hvad vi fik ud af dette trin

- **Små, rene regler er nemme at sammenligne.** Fordi valget af opgradering ikke rører Selenium, er en ny strategi en ny funktion plus en test.
- **Mål, gæt ikke.** Det resultat, vi forventede (flere tjek, flere cookies), var det modsatte af, hvad kørslerne viste.
- **En anden rigtig fejl.** Det første hold styrtede ned i én container: spillet omskriver tælleren i hvert billede, og en computer under belastning fik vores ene genforsøg til at fejle. Læsningen forsøger nu fem gange med en kort pause. En test med en falsk driver, der bliver forældet fire gange, viser det.
- **Retfærdige sammenligninger kræver de samme forhold.** Vi kørte rækkerne samtidig og rapporterer to hold, fordi en enkelt kørsel kan være heldig.
- **En bedre idé skal stadig måles.** Reglen om bedste værdi er rigtig på papiret og gjorde ingen forskel i kørslerne, fordi botten aldrig har cookies nok til at vælge mellem mere end to produkter.
