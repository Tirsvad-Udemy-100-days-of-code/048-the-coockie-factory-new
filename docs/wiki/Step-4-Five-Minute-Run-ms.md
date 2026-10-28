[English](Step-4-Five-Minute-Run) · [Dansk](Step-4-Five-Minute-Run-da) · **Bahasa Malaysia**

# Langkah kuliah 4: berhenti selepas lima minit dan cetak kuki sesaat

![Permainan selepas larian lima minit](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-4.png)

## Apa yang diminta oleh tugasan

Selepas 5 minit bot berhenti dan mencetak `cookies/second`.

## Apa yang kami bina

- `click_and_buy` berjalan sehingga tarikh akhir yang diukur dengan jam monotonik (`time.monotonic`), jadi larian berlangsung tepat `RUN_DURATION_SECONDS` (300) dan tidak tersasar jika sesuatu klik perlahan.
- `SeleniumGame.cookies_per_second` membaca angka permainan itu sendiri daripada `#cookiesPerSecond` (contohnya `per second: 18.9`), dan `parse_cookies_per_second` menukarnya kepada nombor, termasuk nilai seperti `1.2 million`.
- `format_result` membina baris `cookies/second: 18.9`. Program mencetak tepat satu baris ini pada output standard; log (klik, pembelian, masa berlalu) pergi ke ralat standard, jadi `cookie-clicker-bot > result.txt` hanya menyimpan keputusan.

## Keputusan pertama kami

Larian penuh dalam bekas Docker dengan peraturan tugasan (semak setiap 5 saat, beli produk termahal yang mampu dibeli):

| Ukuran | Nilai |
| --- | --- |
| Tempoh | 300.0 saat |
| Klik | 7,666 |
| Produk dibeli | 45 (29 Cursor, 16 Grandma) |
| Keputusan | `cookies/second: 18.9` |

## Apa yang kita peroleh dalam langkah ini

- **Gelung bermasa yang tidak tersasar.** Jam monotonik dan tarikh akhir lebih boleh dipercayai daripada mengira tidur.
- **Output berasingan untuk manusia dan untuk program.** Pencatatan log pergi ke ralat standard dan keputusan ke output standard.
- **Dua pepijat sebenar ditemui oleh larian sebenar.** Permainan memaparkan semula selepas bahasa dipilih, jadi sesuatu elemen boleh menjadi basi antara ketika ia ditemui dan ketika ia digunakan; pembetulannya ialah mencari semula. Sepanduk kuki menutup sebahagian kedai, jadi klik pada produk boleh dipintas; bot kemudian mengklik dengan JavaScript dan hanya mengira pembelian apabila klik itu berjaya. Ujian unit dengan pemacu palsu tidak menunjukkan sebarang masalah ini, itulah sebabnya setiap langkah mempunyai larian bekas dan tangkapan skrin.
- **Garis dasar.** 18.9 kuki sesaat ialah nombor yang cuba dikalahkan oleh langkah 5.
