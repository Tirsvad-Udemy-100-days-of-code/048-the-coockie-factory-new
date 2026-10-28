[English](Step-5-Improve-the-Strategy) · [Dansk](Step-5-Improve-the-Strategy-da) · **Bahasa Malaysia**

# Langkah kuliah 5: ubah suai algoritma

![Permainan selepas larian terbaik, menyemak setiap 10 saat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-5.png)

## Apa yang diminta oleh tugasan

Cuba selang semakan lain (setiap saat, setiap 10 saat) atau beli semua naik taraf yang mampu dibeli, dan lihat sama ada kuki sesaat meningkat.

## Apa yang kami bina

- `--interval SECONDS` menetapkan masa antara semakan naik taraf. Ia mesti lebih besar daripada 0; nilai lalai kekal 5 saat.
- `--buy-all` membeli setiap naik taraf yang masih muat dalam kuki yang anda ada, yang paling mahal dahulu (`choose_affordable_upgrades`). Tanpanya bot membeli satu naik taraf, iaitu yang termahal yang mampu dibeli (`choose_most_expensive_affordable`).
- Kedua-dua peraturan ialah fungsi tulen dalam pakej domain, jadi ia diuji unit tanpa pelayar. Strategi ialah satu nilai (`BuyStrategy`), bukan bendera yang tersebar di seluruh kod.

```bash
cookie-clicker-bot --interval 10
cookie-clicker-bot --interval 1 --buy-all
```

## Apa yang kami ukur

Setiap baris ialah larian penuh 300 saat dalam bekas Docker. Lima bekas berjalan serentak pada satu komputer, dalam dua kelompok, jadi nombor ini sesuai untuk membandingkan baris antara satu sama lain tetapi larian bersendirian adalah lebih pantas (garis dasar solo kami pada langkah kuliah 4 ialah 18.9).

| Semak setiap | Strategi | Kelompok 1 | Kelompok 2 |
| --- | --- | --- | --- |
| 1 saat | beli satu | 13.5 | 13.5 |
| 1 saat | beli semua | 13.5 | 13.5 |
| 5 saat (tugasan) | beli satu | 15.5 | 15.5 |
| 5 saat | beli semua | ranap, lihat di bawah | 14.5 |
| 10 saat | beli satu | **18.2** | **18.2** |

Keputusan terbaik ialah selang 10 saat dengan beli satu. Sebabnya:

- Menyemak lebih kerap tidak lebih baik. Setiap semakan membaca halaman dan mengambil masa daripada mengklik, dan produk termahal yang mampu dibeli biasanya hanya sedikit lebih baik daripada yang lebih murah yang boleh anda beli seketika sebelumnya.
- Beli semua tidak membuat perbezaan pada awal permainan: hanya Cursor dan Grandma yang mampu dibeli, dan bot membelinya juga. Ia akan penting kemudian, apabila bilangan kuki cukup untuk beberapa produk sekali gus.

## Peraturan yang lebih bijak: nilai terbaik

`--best-value` tidak melihat harga sahaja. Permainan memberitahu berapa kuki sesaat yang dihasilkan oleh satu unit setiap produk, dan bot membeli produk yang mampu dibeli dengan harga terendah bagi setiap kuki sesaat (`choose_best_value`). Cursor berharga 15 dan menghasilkan 0.1 (150 kuki bagi setiap kuki sesaat), Grandma berharga 100 dan menghasilkan 1 (100 bagi setiap satu), jadi Grandma ialah belian yang lebih baik walaupun lebih mahal.

```bash
cookie-clicker-bot --best-value
```

Setiap baris ialah larian penuh 300 saat bersendirian dalam bekas Docker, satu demi satu, semak setiap 5 saat:

| Larian | Strategi | kuki/saat | Dibeli |
| --- | --- | --- | --- |
| 1 | termahal yang mampu dibeli | 18 | 30 Cursor, 15 Grandma |
| 2 | nilai terbaik | 17.9 | 29 Cursor, 15 Grandma |
| 3 | termahal yang mampu dibeli | 18.8 | 28 Cursor, 16 Grandma |
| 4 | nilai terbaik | 18.8 | 28 Cursor, 16 Grandma |

Peraturan yang lebih bijak ini **tidak lebih baik**: perbezaan antara kedua-dua peraturan lebih kecil daripada perbezaan antara dua larian peraturan yang sama (18 dan 18.8). Sebabnya sama seperti beli semua. Dalam 5 saat bot mengklik kira-kira 125 kuki, jadi hanya Cursor dan Grandma yang mampu dibeli, dan kedua-dua peraturan membeli hampir perkara yang sama. Peraturan yang melihat nilai akan penting apabila beberapa produk mampu dibeli sekali gus, misalnya dengan selang semakan yang lebih panjang.

## Apa yang kita peroleh dalam langkah ini

- **Peraturan kecil yang tulen mudah dibandingkan.** Oleh kerana pemilihan naik taraf tidak menyentuh Selenium, strategi baharu hanyalah fungsi baharu serta satu ujian.
- **Ukur, jangan meneka.** Keputusan yang kami jangkakan (lebih banyak semakan, lebih banyak kuki) bertentangan dengan apa yang ditunjukkan oleh larian.
- **Pepijat sebenar kedua.** Kelompok pertama ranap dalam satu bekas: permainan menulis semula pembilang pada setiap bingkai, dan komputer yang terbeban menyebabkan satu percubaan semula kami gagal. Bacaan kini mencuba semula lima kali dengan jeda singkat. Ujian dengan pemacu palsu yang menjadi basi empat kali menunjukkannya.
- **Perbandingan yang adil memerlukan keadaan yang sama.** Kami menjalankan baris-baris itu serentak dan melaporkan dua kelompok, kerana satu larian boleh bernasib baik.
- **Idea yang lebih baik masih perlu diukur.** Peraturan nilai terbaik betul di atas kertas dan tidak membuat perbezaan dalam larian, kerana bot tidak pernah mempunyai kuki yang cukup untuk memilih antara lebih daripada dua produk.
