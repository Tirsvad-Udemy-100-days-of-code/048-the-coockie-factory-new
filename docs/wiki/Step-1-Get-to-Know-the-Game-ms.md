[English](Step-1-Get-to-Know-the-Game) · [Dansk](Step-1-Get-to-Know-the-Game-da) · **Bahasa Malaysia**

# Langkah kuliah 1: mengenali permainan

![Permainan sebaik sahaja bahasa dipilih](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-1.png)

## Apa yang diminta oleh tugasan

Buka versi baharu Cookie Clicker (ozh.github.io/cookieclicker) dan fahami cara ia berfungsi sebelum menulis sebarang kod.

## Apa yang kami temui

Kami membuka halaman itu dalam Chromium tanpa kepala di dalam bekas Docker dan melihat HTML-nya. Bahagian yang diperlukan oleh bot:

| Apa | Di mana pada halaman |
| --- | --- |
| Bahasa Inggeris pada pemilihan bahasa | `#langSelect-EN` |
| Kuki besar | `#bigCookie` |
| Bilangan kuki dan kuki sesaat | `#cookies` (dan `#cookiesPerSecond` di dalamnya) |
| Kedai | `#products`, dengan `#product0` (Cursor), `#product1` (Grandma), `#product2` (Farm) dan seterusnya |
| Nama dan harga produk | `.productName` dan `.price` di dalam produk |
| Mampukah saya membelinya? | produk itu mempunyai kelas `unlocked enabled` (produk yang belum mampu dibeli ialah `unlocked disabled`; yang tersembunyi ialah `locked disabled`) |

Juga baik untuk diketahui:

- Permainan meminta bahasa apabila halaman dimuatkan buat kali pertama. Bot mesti memilih satu sendiri.
- Bilangan ditulis sebagai teks: `3 cookies`, `5,000 cookies`, dan untuk nombor besar pada dua baris, `1.235` dan `million cookies`.
- Sepanduk kuki ("Got it!") berada di bahagian bawah halaman. Bot tidak pernah mengkliknya, kerana ia ialah sepanduk persetujuan yang menjadi hak orang yang bermain; bot mengatasinya dengan cara lain (lihat [Langkah 4](Step-4-Five-Minute-Run-ms)).

Semua id dan pemilih ini ditulis sekali sahaja, dalam `constants.py`.

## Apa yang kita peroleh dalam langkah ini

- **Baca halaman sebelum menulis kod.** Meninjau sebentar HTML sebenar menjimatkan berjam-jam meneka; setiap pemilih dalam bot datang daripada langkah ini.
- **Simpan pemilih di satu tempat.** Jika permainan menukar sesuatu id, satu baris dalam `constants.py` ialah pembetulannya.
- **Jalankan pelayar dalam bekas.** Imej Docker yang sama yang menjalankan bot mengambil tangkapan skrin, jadi tiada apa yang terbuka pada desktop anda sendiri dan setiap larian bermula daripada pelayar bersih yang sama.
