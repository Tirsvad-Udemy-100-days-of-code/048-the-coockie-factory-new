[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Cookie Clicker Bot

Bot Selenium yang bermain [Cookie Clicker](https://ozh.github.io/cookieclicker/) untuk anda: ia mengklik kuki besar, membeli naik taraf termahal yang mampu dibeli setiap 5 saat dan mencetak kuki sesaat selepas 5 minit. Ini ialah hari ke-48 kursus Udemy *100 Days of Code: The Complete Python Pro Bootcamp*.

## Lima langkah kuliah

| Langkah | Apa yang dipelajari bot | Halaman |
| --- | --- | --- |
| 1 | Mengenali permainan dan halamannya | [Langkah 1](Step-1-Get-to-Know-the-Game-ms) |
| 2 | Menutup pemilihan bahasa dan mengklik kuki | [Langkah 2](Step-2-Click-the-Cookie-ms) |
| 3 | Setiap 5 saat, beli naik taraf termahal yang mampu dibeli | [Langkah 3](Step-3-Buy-Upgrades-ms) |
| 4 | Berhenti selepas 5 minit dan cetak kuki sesaat | [Langkah 4](Step-4-Five-Minute-Run-ms) |
| 5 | Ubah suai strategi dan bandingkan larian | [Langkah 5](Step-5-Improve-the-Strategy-ms) |

Setiap halaman menunjukkan tangkapan skrin permainan pada langkah tersebut dan menerangkan apa yang kita peroleh di dalamnya.

## Jalankannya

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
cookie-clicker-bot
```

Untuk memastikan desktop anda bebas, jalankannya dalam Docker (Chromium tanpa kepala): `docker build -t cookie-clicker-bot .` dan `docker run --rm cookie-clicker-bot`. README repositori mengandungi arahan lengkap untuk Windows, Linux dan macOS, serta untuk ujian.

## Keputusan

| Larian | cookies/second |
| --- | --- |
| Langkah kuliah 4: semak setiap 5 saat, beli satu (bersendirian pada komputer) | 18.9 |
| Langkah kuliah 5: semak setiap 10 saat, beli satu (terbaik dalam perbandingan) | 18.2 |
| Peraturan nilai terbaik, semak setiap 5 saat (bersendirian pada komputer, dua larian) | 17.9 dan 18.8 |

Peraturan nilai terbaik (`cookie-clicker-bot --best-value`) membeli naik taraf yang mampu dibeli dengan harga terendah bagi setiap kuki sesaat. Ia tidak lebih baik daripada peraturan tugasan (18 dan 18.8 dalam keadaan yang sama). Baris-baris ini datang daripada keadaan yang berbeza; [Langkah 5](Step-5-Improve-the-Strategy-ms) menerangkan cara ia diukur.

## Cara kod disusun

- `domain/`: peraturan (menghurai teks halaman, memilih naik taraf), tanpa Selenium.
- `application/`: gelung permainan, yang berhubung dengan permainan melalui port.
- `infrastructure/`: penyesuai Selenium dan kilang Chromium.
- `constants.py`: semua pemalar.

Ujian menggunakan pemacu palsu, jadi ia berjalan dalam sesaat dan tidak memerlukan pelayar.
