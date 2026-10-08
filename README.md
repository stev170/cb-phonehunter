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

### Android / Termux

```bash
pkg update && pkg upgrade
pkg install python git
python -m pip install --upgrade pip
pip install -r requirements.txt
python cb_phone_hunter.py
```

### Linux / macOS / Windows (Git Bash)

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

---

## 🔧 Persyaratan Sistem

- **Python:** 3.8 atau lebih baru
- **Perpustakaan Python:**
  - `requests` ≥ 2.31.0
  - `colorama` ≥ 0.4.6
  - `phonenumbers` ≥ 8.13.0
  - `dnspython` (untuk DNS lookup)
- **Koneksi Internet:** Diperlukan untuk verifikasi online
- **Sistem Operasi:** Linux, macOS, Windows, Termux

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

---

## 🛡️ Ciberbrigada OSINT Suite

- 📧 **CB-EmailHunter** — Email OSINT → [lihat repo](https://github.com/ciberbrigada/cb-emailhunter)
- 👤 **CB-UserHunter** — Username OSINT → [lihat repo](https://github.com/ciberbrigada/cb-userhunter)
- 📱 **CB-PhoneHunter** — Phone OSINT *(repositori ini)*
- 🌐 **CB-DomainHunter** — OSINT domain & IP *(segera hadir)*
- 📸 **CB-InstaHunter** — Instagram OSINT *(segera hadir)*

---

## 📝 Lisensi

Program ini dilisensikan di bawah **MIT License**.

Lihat file [LICENSE_phonehunter](./LICENSE_phonehunter) untuk detail lengkap.

---

<p align="center">
  <b>Dibuat dengan ❤️ oleh Ciberbrigada</b>
  <br/>
  <sub>Untuk tujuan keamanan, penelitian, dan pendidikan</sub>
</p>
