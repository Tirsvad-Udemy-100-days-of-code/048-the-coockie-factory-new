[English](Step-3-Buy-Upgrades) · [Dansk](Step-3-Buy-Upgrades-da) · **Bahasa Malaysia**

# Langkah kuliah 3: beli naik taraf termahal yang mampu dibeli

![Permainan selepas 45 saat mengklik dan membeli](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-3.png)

## Apa yang diminta oleh tugasan

Setiap 5 saat, lihat anak tetingkap sebelah kanan, cari naik taraf yang mampu dibeli, dan beli yang paling mahal. Contohnya, dengan 105 kuki, Cursor (15) dan Grandma (100) kedua-duanya mampu dibeli, jadi bot membeli Grandma. Petunjuk menyebut `split`, `strip` dan `replace` untuk menukar teks halaman kepada nombor.

## Apa yang kami bina

- `parse_amount` dan `parse_cookie_count` menukar teks halaman kepada nombor. Ia membuang perkataan `cookies`, menggugurkan segala-galanya selepas `per second`, membuang koma ribuan dengan `replace`, dan memahami perkataan seperti `1.4 million`. Contoh: `5,000 cookies` menghasilkan 5000; `1.235` dan `million cookies` pada dua baris menghasilkan 1,235,000.
- `SeleniumGame.upgrades` membaca setiap produk yang kelihatan: id, nama dan harganya.
- `choose_most_expensive_affordable(upgrades, cookies)` ialah fungsi tulen: antara naik taraf yang harganya tidak melebihi bilangan kuki, pulangkan yang paling mahal, atau tiada apa-apa. Ia diuji dengan contoh di atas (105 kuki menghasilkan Grandma).
- `click_and_buy` terus mengklik, dan apabila `check_interval_seconds` (5 secara lalai) telah berlalu, ia membaca bilangan kuki, memilih, dan membeli.
- Dalam larian bekas selama 45 saat, bot membeli 8 naik taraf, dan tangkapan skrin menunjukkan Cursor dan Grandma yang dimilikinya.

## Apa yang kita peroleh dalam langkah ini

- **Bahagian yang sukar ialah teks, bukan kliknya.** Nombor yang sama muncul sebagai `120`, `5,000`, `1.4 million` dan pada dua baris. Penghuraian ialah fungsi tulen kecil dengan banyak kes ujian, jadi selamat untuk diubah.
- **Jauhkan peraturan daripada pelayar.** "Beli naik taraf termahal yang mampu dibeli" ialah satu fungsi yang tidak tahu apa-apa tentang Selenium. Itulah sebabnya langkah 5 boleh menambah peraturan kedua tanpa menyentuh kod pelayar.
- **Jangan kira pembelian yang tidak anda buat.** Versi pertama mencatat pembelian setiap kali ia mengklik. Larian sebenar menunjukkan klik itu tidak selalu sampai ke produk, jadi `buy` kini memberitahu sama ada ia berjaya, dan hanya pembelian sebenar dikira (lihat [Langkah 4](Step-4-Five-Minute-Run-ms)).
