[English](Step-2-Click-the-Cookie) · [Dansk](Step-2-Click-the-Cookie-da) · **Bahasa Malaysia**

# Langkah kuliah 2: klik kuki secepat mungkin

![Permainan selepas 15 saat mengklik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/raw/branch/main/docs/images/step-2.png)

## Apa yang diminta oleh tugasan

Cipta bot dengan Selenium dan Python yang mengklik kuki secepat mungkin. Ia mesti menutup pemilihan bahasa sendiri sebelum bermula.

## Apa yang kami bina

- `open_game` memuatkan halaman.
- `dismiss_language` menunggu sehingga butang bahasa Inggeris kelihatan, mengkliknya, kemudian menunggu sehingga kuki besar kelihatan. Permainan memerlukan beberapa saat untuk bermula selepas bahasa dipilih, jadi bot membuat pengundian (setiap 0.2 saat, paling lama 20 saat) dan bukannya tidur untuk masa yang tetap.
- `click_cookie` mengklik `#bigCookie` sekali. Jika sepanduk atau pemaparan semula menghalang klik seketika, bot mencuba lagi pada pusingan seterusnya.
- Satu gelung memanggil `click_cookie` sehingga masa tamat. Dalam larian 15 saat di dalam bekas, bot mengklik sebanyak 344 kali, dan tangkapan skrin di atas menunjukkan 342 kuki.

```bash
cookie-clicker-bot --headless --duration 15 --screenshot step-2.png
```

## Apa yang kita peroleh dalam langkah ini

- **Tunggu sesuatu keadaan, bukan sesuatu masa.** `sleep` yang tetap sama ada terlalu pendek (bot gagal) atau terlalu lama (bot membazir masa). Mengundi untuk "kuki kelihatan" adalah lebih pantas dan lebih selamat.
- **Letakkan pelayar di belakang port.** Gelung hanya mengenali `GamePort` (`open_game`, `dismiss_language`, `click_cookie`, ...). Kod Selenium berada dalam satu penyesuai, jadi gelung diuji dengan permainan palsu dalam beberapa milisaat.
- **Catat masa gelung dengan jam yang boleh digantikan.** `click_and_buy` menerima jam sebagai parameter; ujian memberikannya jam palsu dan menyemak bilangan klik dengan tepat.
