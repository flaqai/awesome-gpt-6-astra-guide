# Panduan Praktis GPT-6 Astra

Panduan GPT-6 Astra terbaru yang disusun oleh **tim [flaq.ai](https://flaq.ai/)**: dasar model, langkah awal, kode yang bisa dijalankan, alur kreatif, dan tangkapan layar nyata.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · **Bahasa Indonesia** · [العربية](README_ar.md)
<!-- languages:end -->

## Ide tambahan dari X

2026-09-22: delapan latihan dari tujuh unggahan yang dibaca langsung: takarir, warna, migrasi mesin, aset modular, seni piksel spreadsheet, antarmuka gudang, pemeriksaan sejarah, dan kriteria selesai. Sumber serta batas verifikasi dicantumkan; hasil belum direproduksi. Ringkasan dalam bahasa Inggris, prompt terperinci dalam Mandarin.

[Panduan kasus X](docs/x-playbook.md) · [Catatan sumber X](docs/research/x-sources-2026-09-22.json)

Terakhir diperiksa: 2026-09-08. Ini panduan independen dari tim, bukan dokumentasi resmi OpenAI. README tersedia dalam 12 bahasa; tutorial mendalam dan pesan diagnostik saat ini menggunakan bahasa Mandarin sederhana.

[Langkah awal](docs/quickstart.md) · [12 kasus](docs/cases.md) · [6 alur kerja](docs/workflows.md) · [Contoh kode](examples/README.md)

## Apa itu Astra

Astra adalah model OpenAI untuk penalaran kompleks, pemrograman, riset, dan tugas bertahap. Model menerima teks dan gambar lalu menghasilkan teks. Penjelajahan web, eksekusi perangkat lunak, dan pembuatan video memerlukan alat di aplikasi yang digunakan.


[Dokumentasi resmi](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Parameter dan fitur lanjutan](https://developers.openai.com/api/docs/guides/latest-model)

## Mulai tanpa menulis kode

Pilih Astra dalam produk yang dapat Anda akses, berikan materi, dan minta hasil kecil terlebih dahulu. Contohnya:

```text
Rencanakan acara dua hari untuk kedai kopi. Anggaran 2.000 yuan dengan dua staf. Buat aturan, jadwal, rincian anggaran, dan tiga pesan promosi. Periksa jumlah biaya dan jelaskan asumsi yang dipakai.
```

## Gunakan langsung melalui klien

Masuk dengan akun ChatGPT tanpa menyiapkan kunci API terlebih dahulu. Akses Astra dan batas penggunaan bergantung pada akun serta ruang kerja.

### ChatGPT

Masuk ke ChatGPT dan pilih Work untuk membuat hasil akhir. Pilih Astra pada model/Power; periksa Advanced jika tersedia. Lampirkan gambar anggaran dan minta perbandingan 24 dengan 32 peserta.

### Codex

Masuk ke klien Codex; pada aplikasi desktop terpadu, beralih ke Codex. Buka folder proyek lokal, buat tugas dengan Astra, lalu minta menjalankan latihan dan menyerahkan berkas beserta pemeriksaan nyata.

### Codex CLI

[Instal CLI](https://learn.chatgpt.com/docs/cli). Instal CLI dari halaman resmi dan jalankan di folder proyek. Pertama kali pilih Sign in with ChatGPT. Dalam sesi, gunakan /model untuk memastikan Astra dan /status untuk melihat pengaturan, lalu jelaskan tugas Anda.

```bash
codex -m gpt-6-astra
```

[Langkah terperinci (Mandarin)](docs/quickstart.md) · [English](README.md) · [Models](https://learn.chatgpt.com/docs/models)

<details>
<summary>API opsional untuk integrasi aplikasi sendiri</summary>

[API](docs/api.md) · [Python / JavaScript](examples/README.md)

</details>

## Jalankan latihan orisinal kami

Tiga latihan yang dibuat khusus untuk panduan ini memakai satu contoh studio fiktif. Gambar adalah tangkapan peramban asli dari laporan SVG yang dibuat secara lokal, bukan karya pihak ketiga atau hasil pengukuran API Astra.

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![Anggaran: pengeluaran 2.168 CNY, cadangan 432 CNY.](assets/screenshots/workshop-budget.png)

Anggaran: pengeluaran 2.168 CNY, cadangan 432 CNY.

![Storyboard: 20 detik pada 30 fps, dengan 600 bingkai berurutan.](assets/screenshots/craft-storyboard.png)

Storyboard: 20 detik pada 30 fps, dengan 600 bingkai berurutan.

![Tinjauan rilis: 3 dari 5 pemeriksaan fiktif lolos; 2 perlu diperbaiki.](assets/screenshots/release-review.png)

Tinjauan rilis: 3 dari 5 pemeriksaan fiktif lolos; 2 perlu diperbaiki.

[Kode, langkah reproduksi, dan latihan](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

## Alur kerja praktis

Buat versi terkecil yang berfungsi, lalu perbaiki berdasarkan tangkapan layar, galat, dan kriteria penerimaan. Minta berkas yang dapat diedit, cara menjalankan, dan tangkapan layar hasil sebenarnya.

[6 alur kerja](docs/workflows.md)

## Verifikasi dan kontribusi

Contoh lulus 28 pengujian offline. Tidak ada panggilan API berbayar atau reproduksi proyek secara menyeluruh. [Verifikasi](docs/verification.md) · [Sumber](docs/sources.md) · [Kontribusi](CONTRIBUTING.md). Konten dan kode asli memakai [MIT](LICENSE); materi pihak ketiga mempertahankan hak masing-masing.

## 3D seru: robot yang merakit dirinya

Enam latihan orisinal: robot meja, animasi perakitan, sudut baca, film sirkuit kertas, maskot jamur, dan pemeriksaan adegan. Panduan Inggris/Mandarin memuat prompt, pengaturan, dan skrip orisinal. Hanya sintaks Python yang diperiksa; skrip belum diuji di Blender.

[Panduan praktik Blender](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

## Tentang flaq.ai

[flaq.ai](https://flaq.ai/) menyediakan akses API terpadu ke model gambar, video, musik, dan bahasa untuk agen AI serta aplikasi produksi. Tim kami membagikan metode praktis melalui panduan ini. Alur kerja sumber terbuka: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Afiliasi dan dukungan mitra

Kreator, developer, dan pengajar dapat mengikuti [Program Afiliasi Flaq.ai](https://flaq.ai/affiliate-program/) serta membagikan tutorial, ulasan, dan panduan integrasi menggunakan tautan rujukan sendiri.

**20%** untuk pesanan berbayar valid pertama pengguna rujukan, lalu **10%** untuk pesanan berikutnya. Pesanan yang memenuhi syarat berada dalam **60 hari setelah pengguna rujukan mendaftar**.

Masuk dan lengkapi profil untuk mengelola tautan, melacak rujukan, dan menyiapkan pembayaran. Ungkapkan hubungan afiliasi dengan jelas. Kelayakan, peninjauan, dan pembayaran mengikuti [perjanjian yang berlaku](https://flaq.ai/affiliate-agreement/); penghasilan tidak dijamin.

## Referensi dan inspirasi

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

Diterbitkan oleh 数字生命卡兹克; penulis: 卡兹克、可达; 2026-09-08. Inspirasi alur kerja; gambar dan prompt panjang artikel tidak disalin.

[Catatan sumber X · 2026-09-22](docs/x-playbook.md) · [JSON](docs/research/x-sources-2026-09-22.json)
