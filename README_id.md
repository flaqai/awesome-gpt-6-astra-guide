# Panduan Praktis GPT-6 Astra

Panduan GPT-6 Astra terbaru yang disusun oleh **tim [flaq.ai](https://flaq.ai/)**: dasar model, langkah awal, kode yang bisa dijalankan, alur kreatif, dan tangkapan layar nyata.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · **Bahasa Indonesia** · [العربية](README_ar.md)
<!-- languages:end -->

Terakhir diperiksa: 2026-09-08. Ini panduan independen dari tim, bukan dokumentasi resmi OpenAI. README tersedia dalam 12 bahasa; tutorial mendalam dan pesan diagnostik saat ini menggunakan bahasa Mandarin sederhana.

[Langkah awal](docs/quickstart.md) · [12 kasus](docs/cases.md) · [6 alur kerja](docs/workflows.md) · [Contoh kode](examples/README.md)

## Apa itu Astra

Astra adalah model OpenAI untuk penalaran kompleks, pemrograman, riset, dan tugas bertahap. Model menerima teks dan gambar lalu menghasilkan teks. Penjelajahan web, eksekusi perangkat lunak, dan pembuatan video memerlukan alat di aplikasi yang digunakan.

| Model | `gpt-6-astra` |
| --- | --- |
| Konteks | 1,050,000 tokens |
| Keluaran maksimum | 128,000 tokens |
| Tingkat penalaran | `low` · `medium` · `high` · `xhigh` · `max` |

[Dokumentasi resmi](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Parameter dan fitur lanjutan](https://developers.openai.com/api/docs/guides/latest-model)

## Mulai tanpa menulis kode

Pilih Astra dalam produk yang dapat Anda akses, berikan materi, dan minta hasil kecil terlebih dahulu. Contohnya:

```text
Rencanakan acara dua hari untuk kedai kopi. Anggaran 2.000 yuan dengan dua staf. Buat aturan, jadwal, rincian anggaran, dan tiga pesan promosi. Periksa jumlah biaya dan jelaskan asumsi yang dipakai.
```

## Jalankan contoh pertama

Gunakan Python 3.10+ atau Node.js 20+ dari direktori utama repositori. Skrip memakai pustaka bawaan tanpa perlu memasang paket. Pratinjau permintaan secara gratis terlebih dahulu:

```bash
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

Untuk panggilan nyata, atur `OPENAI_API_KEY` di terminal memakai kunci proyek OpenAI yang memiliki akses Astra. Lihat [pengaturan](docs/quickstart.md#用-api-开始). Jangan masukkan kunci ke kode atau tangkapan layar. `--dry-run` tidak terhubung ke jaringan; permintaan nyata dikenai biaya. Contoh memanggil OpenAI API secara langsung. Periksa ketersediaan model di Flaq.ai secara terpisah.

```bash
python3 examples/astra.py text --prompt 'Rencanakan acara dua hari untuk kedai kopi. Anggaran 2.000 yuan dengan dua staf. Buat aturan, jadwal, rincian anggaran, dan tiga pesan promosi. Periksa jumlah biaya dan jelaskan asumsi yang dipakai.'
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[Contoh kode](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## Proyek dan tangkapan layar nyata

Gambar berikut diambil langsung dari browser. Hak karya tetap milik pembuatnya; proyek tidak direproduksi secara menyeluruh.

![Kereta uap Tom Krcha: halaman yang menampilkan pratinjau pembuatnya.](assets/screenshots/steam-train-reference.png)

Kereta uap Tom Krcha: halaman yang menampilkan pratinjau pembuatnya. [Postingan asli](https://x.com/tomkrcha/status/2095756085890310311)

![iPhone Archive oleh bluedev: halaman publik yang dibuka di browser.](assets/screenshots/iphone-archive.png)

iPhone Archive oleh bluedev: halaman publik yang dibuka di browser. [Postingan asli](https://x.com/blueemi99/status/2096917792737911131) · [Proyek langsung](https://iphone-archive.vercel.app/)

![Seoul 3D Atlas oleh synabreu: perpindahan City dan Sunset telah diperiksa.](assets/screenshots/seoul-atlas.png)

Seoul 3D Atlas oleh synabreu: perpindahan City dan Sunset telah diperiksa. [Postingan asli](https://x.com/synabreu/status/2096557555086725159) · [Proyek langsung](https://seoul-3d-atlas.synabreu.chatgpt.site/)

[Sumber tangkapan layar](assets/screenshots/README.md) · [12 kasus](docs/cases.md)

## Alur kerja praktis

Buat versi terkecil yang berfungsi, lalu perbaiki berdasarkan tangkapan layar, galat, dan kriteria penerimaan. Minta berkas yang dapat diedit, cara menjalankan, dan tangkapan layar hasil sebenarnya.

[6 alur kerja](docs/workflows.md)

## Verifikasi dan kontribusi

Contoh lulus 17 pengujian offline. Tidak ada panggilan API berbayar atau reproduksi proyek secara menyeluruh. [Verifikasi](docs/verification.md) · [Sumber](docs/sources.md) · [Kontribusi](CONTRIBUTING.md). Konten dan kode asli memakai [MIT](LICENSE); materi pihak ketiga mempertahankan hak masing-masing.

## Tentang flaq.ai

[flaq.ai](https://flaq.ai/) menyediakan akses API terpadu ke model gambar, video, musik, dan bahasa untuk agen AI serta aplikasi produksi. Tim kami membagikan metode praktis melalui panduan ini. Alur kerja sumber terbuka: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Afiliasi dan dukungan mitra

Kreator, developer, dan pengajar dapat mengikuti [Program Afiliasi Flaq.ai](https://flaq.ai/affiliate-program/) serta membagikan tutorial, ulasan, dan panduan integrasi menggunakan tautan rujukan sendiri.

**20%** untuk pesanan berbayar valid pertama pengguna rujukan, lalu **10%** untuk pesanan berikutnya. Pesanan yang memenuhi syarat berada dalam **60 hari setelah pengguna rujukan mendaftar**.

Masuk dan lengkapi profil untuk mengelola tautan, melacak rujukan, dan menyiapkan pembayaran. Ungkapkan hubungan afiliasi dengan jelas. Kelayakan, peninjauan, dan pembayaran mengikuti [perjanjian yang berlaku](https://flaq.ai/affiliate-agreement/); penghasilan tidak dijamin.
