# 📱 CB-PhoneHunter

<p align="center">
  <img src="https://img.shields.io/badge/versi-2.0-cyan?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OSINT-Telepon-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/lisensi-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/gratis-tanpa%20API%20key-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  <b>Pengenalan OSINT nomor telepon di sumber terbuka</b><br/>
  Bagian dari <a href="https://ciberbrigada.com">Ciberbrigada OSINT Suite</a>
</p>

---

## 🎯 Apa yang dilakukan?

CB-PhoneHunter menganalisis nomor telepon di berbagai sumber terbuka dan gratis:

- ✅ Validasi dan format nomor (E164, internasional, nasional)
- ✅ Negara, wilayah, operator, dan zona waktu
- ✅ Tipe line (seluler, tetap, VoIP, dll.)
- ✅ Verifikasi di Veriphone (data operator nyata)
- ✅ Verifikasi di NumVerify (validasi & operator)
- ✅ Pencarian DNS & ENUM (infrastruktur telepon)
- ✅ Verifikasi WhatsApp (apakah akun aktif?)
- ✅ Verifikasi Telegram (tautan & pencarian)
- ✅ Profil Gravatar (data terkait nomor)
- ✅ Geolokasi berdasarkan negara & operator

**100% Gratis · Tanpa API Key · Tanpa Registrasi · Tanpa Login**

---

## 📥 Instalasi

### Prasyarat
- Python 3.8 atau lebih baru
- pip (Python Package Manager)
- Koneksi internet

### Langkah-langkah

#### Linux / macOS / Windows (Git Bash)

```bash
# 1. Kloning repositori
git clone https://github.com/stev170/cb-phonehunter
cd cb-phonehunter

# 2. Instalasi dependensi
pip install -r requirements.txt

# 3. Jalankan program
python3 cb_phone_hunter.py
```

#### Kali Linux / Parrot OS / Ubuntu

```bash
git clone https://github.com/stev170/cb-phonehunter
cd cb-phonehunter
pip3 install -r requirements.txt
python3 cb_phone_hunter.py
```

#### Windows (Command Prompt)

```cmd
git clone https://github.com/stev170/cb-phonehunter
cd cb-phonehunter
pip install -r requirements.txt
python cb_phone_hunter.py
```

---

## 🔄 Memperbarui ke Versi Terbaru

```bash
cd cb-phonehunter
git pull origin main
```

---

## 🚀 Cara Menggunakan

```bash
python3 cb_phone_hunter.py
```

### Contoh Interaksi:

```
▸ Nomor: +62 812 3456-7890

── ANALISIS NOMOR ──
  ▸ Nomor internasional: +62 812 3456-7890
  ▸ Format E164:         +628123456789
  ▸ Format nasional:     0812 3456-7890
  ▸ Valid:               ✓ YA
  ▸ Negara:              Indonesia
  ▸ Operator:            Telkomsel
  ▸ Tipe line:           📱 SELULER
  ▸ Zona waktu:          Asia/Jakarta

── PILIH MODUL ──
[2] Veriphone        — Operator, tipe & negara (API gratis)
[3] NumVerify        — Validasi & operator
[4] DNS / ENUM       — Protokol E.164 & infrastruktur
[5] WhatsApp         — Apakah punya akun aktif?
[6] Telegram         — Apakah punya akun aktif?
[7] Gravatar         — Profil terkait nomor
[0] SEMUA MODUL

▸ Pilihan (contoh: 0 atau 2,5,6): 0
```

---

## 📊 Modul Analisis

| # | Modul | Deskripsi |
|---|-------|-----------|
| 1 | Analisis Lokal | Format, negara, operator, zona waktu, tipe line (offline) |
| 2 | Veriphone | Validasi nomor, nama operator, tipe line via API gratis |
| 3 | NumVerify | Validasi tambahan, lokasi geografis, operator |
| 4 | DNS & ENUM | Pencarian infrastruktur telepon via DNS, ENUM protocol |
| 5 | WhatsApp | Verifikasi apakah nomor terdaftar & aktif di WhatsApp |
| 6 | Telegram | Cek kehadiran nomor di Telegram & pencarian TGStat |
| 7 | Gravatar | Profil & akun media sosial terkait hash nomor |

---

## 📱 Format Nomor Input

CB-PhoneHunter mendukung berbagai format input. Selalu sertakan **kode negara** dengan simbol `+`:

### Indonesia
```
+62 812 3456-7890    (Seluler umum)
+62 21 1234-5678     (Tetap Jakarta)
+62812-3456-7890     (Format alternatif)
```

### Negara Lain
```
+1 555 123 4567      (Amerika Serikat)
+44 20 1234 5678     (Britania Raya)
+33 1 2345 6789      (Prancis)
+55 11 91234-5678    (Brasil)
+34 612 345 678      (Spanyol)
+81 90 1234 5678     (Jepang)
```

### Perintah Khusus
```
keluar               (Keluar dari program)
exit                 (Keluar dari program)
quit                 (Keluar dari program)
q                    (Keluar dari program)
```

---

## 🔧 Persyaratan Sistem

- **Python:** 3.8 atau lebih baru
- **Perpustakaan Python:**
  - `requests` ≥ 2.31.0
  - `colorama` ≥ 0.4.6
  - `phonenumbers` ≥ 8.13.0
  - `dnspython` (untuk DNS lookup)
- **Koneksi Internet:** Diperlukan untuk verifikasi online
- **Sistem Operasi:** Linux, macOS, Windows

---

## 📋 Dependensi

Lihat file `requirements.txt`:

```
requests>=2.31.0
colorama>=0.4.6
phonenumbers>=8.13.0
dnspython>=2.3.0
```

Instalasi otomatis saat pertama kali menjalankan program jika belum terinstal.

---

## 💡 Tips & Trik

### 1. Analisis Cepat
Gunakan `0` untuk menjalankan semua modul sekaligus:
```
▸ Pilihan: 0
```

### 2. Modul Spesifik
Pilih modul tertentu dengan nomor:
```
▸ Pilihan: 2,5,6
```
(Menjalankan Veriphone, WhatsApp, dan Telegram)

### 3. Batch Analysis
Program berjalan dalam loop interaktif, masukkan nomor baru tanpa perlu restart:
```
▸ Nomor: +62812...
[analisis...]
▸ Analisis nomor lain? +62821...
```

### 4. Format Fleksibel
Semua format di bawah valid:
- `+62 812 3456-7890`
- `+628123456789`
- `+62-812-3456-7890`
- `62812 3456 7890` (tanpa +, system auto-detect)

---

## ⚠️ Pernyataan Legal & Etika

### Penggunaan yang Sah
Alat ini dirancang **HANYA** untuk:
- ✅ Penelitian keamanan yang sah
- ✅ Tujuan pendidikan dan pembelajaran
- ✅ Verifikasi nomor pribadi Anda sendiri
- ✅ Investigasi dengan persetujuan pemilik nomor
- ✅ Keperluan hukum dan penegakan

### Penggunaan Terlarang
**JANGAN** gunakan untuk:
- ❌ Penipuan, spamming, atau harassment
- ❌ Pelacakan tanpa persetujuan
- ❌ Akses tidak sah atau aktivitas ilegal
- ❌ Mengumpulkan data pribadi untuk dijual
- ❌ Mengganggu privasi orang lain

### Tanggung Jawab Pengguna
Pengguna sepenuhnya bertanggung jawab atas penggunaan alat ini. Ciberbrigada dan pengembang **TIDAK BERTANGGUNG JAWAB** atas:
- Penyalahgunaan alat ini
- Kerusakan atau kerugian yang timbul
- Pelanggaran hukum atau regulasi
- Pelanggaran privasi atau hak cipta

---

## 🛡️ Ciberbrigada OSINT Suite

Koleksi lengkap alat OSINT:

- 📧 **CB-EmailHunter** — Email OSINT → [lihat repo](https://github.com/ciberbrigada/cb-emailhunter)
- 👤 **CB-UserHunter** — Username OSINT → [lihat repo](https://github.com/ciberbrigada/cb-userhunter)
- 📱 **CB-PhoneHunter** — Phone OSINT *(repositori ini)*
- 🌐 **CB-DomainHunter** — OSINT domain & IP *(segera hadir)*
- 📸 **CB-InstaHunter** — Instagram OSINT *(segera hadir)*

---

## 🐛 Pelaporan Bug & Saran

Jika Anda menemukan bug atau memiliki saran perbaikan:

1. Periksa **Issues** yang sudah ada untuk menghindari duplikasi
2. Buka **Issue baru** dengan:
   - Deskripsi masalah yang jelas
   - Langkah reproduksi
   - Screenshot jika relevan
   - Versi Python & sistem operasi

---

## 📝 Lisensi

Program ini dilisensikan di bawah **MIT License**.

Lihat file [LICENSE_phonehunter](./LICENSE_phonehunter) untuk detail lengkap.

---

## 👨‍💻 Kontribusi

Kontribusi dari komunitas sangat diterima! Cara berkontribusi:

1. Fork repositori
2. Buat branch fitur (`git checkout -b fitur/FiturBaru`)
3. Commit perubahan (`git commit -m 'Tambah fitur baru'`)
4. Push ke branch (`git push origin fitur/FiturBaru`)
5. Buka Pull Request

---

## ❓ Pertanyaan Umum (FAQ)

### P: Apakah gratis?
**J:** Ya, 100% gratis selamanya.

### P: Apakah perlu API key?
**J:** Tidak. Alat ini menggunakan API gratis dan endpoint publik.

### P: Bagaimana jika mendapat error "Rate limit"?
**J:** Tunggu beberapa menit lalu coba lagi. Beberapa API memiliki batasan permintaan.

### P: Bisa offline?
**J:** Modul 1 (Analisis Lokal) bisa offline. Modul lain memerlukan internet.

### P: Nomor mana yang bisa dianalisis?
**J:** Nomor valid dari seluruh dunia dengan kode negara internasional.

### P: Apakah privat atau kirim data kemana-mana?
**J:** Data hanya dikirim ke API publik yang ditentukan. Program tidak menyimpan log atau data Anda.

---

## 🔗 Link Penting

- 🌐 **Website:** https://ciberbrigada.com
- 📘 **GitHub:** https://github.com/ciberbrigada
- 💼 **LinkedIn:** https://www.linkedin.com/company/ciberbrigada
- 📧 **Email:** contact@ciberbrigada.com

---

## 🙏 Ucapan Terima Kasih

- **Fgunther** — Developer & Creator
- **Ciberbrigada Team** — OSINT Suite Development
- **Komunitas** — Feedback & Saran

---

<p align="center">
  <b>Dibuat dengan ❤️ oleh Ciberbrigada</b>
  <br/>
  <sub>Untuk tujuan keamanan, penelitian, dan pendidikan</sub>
  <br/><br/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Maintained-Yes-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Language-Python-blue?style=flat-square"/>
</p>
