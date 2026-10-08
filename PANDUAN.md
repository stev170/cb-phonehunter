# 📖 Panduan Lengkap CB-PhoneHunter

## 📚 Daftar Isi
1. [Pengenalan](#pengenalan)
2. [Instalasi Lengkap](#instalasi-lengkap)
3. [Panduan Penggunaan](#panduan-penggunaan)
4. [Penjelasan Modul](#penjelasan-modul)
5. [Troubleshooting](#troubleshooting)
6. [FAQ](#faq)

---

## Pengenalan

**CB-PhoneHunter** adalah alat OSINT (Open Source Intelligence) untuk menganalisis nomor telepon. Alat ini mengumpulkan informasi dari berbagai sumber publik dan API gratis.

### Fitur Utama:
- ✅ Analisis nomor telepon internasional
- ✅ Validasi & format otomatis
- ✅ Identifikasi operator & lokasi
- ✅ Verifikasi WhatsApp & Telegram
- ✅ Pencarian DNS & ENUM
- ✅ Profil Gravatar terkait

### Keamanan:
- **Offline:** Modul 1 berfungsi tanpa internet
- **Privat:** Tidak menyimpan data lokal
- **Gratis:** Tidak ada biaya atau langganan
- **Transparan:** Kode sumber terbuka

---

## Instalasi Lengkap

### 1. Prasyarat Sistem

#### Windows
```
- Windows 7 atau lebih baru
- Python 3.8+
- Git (opsional, untuk clone)
```

#### Linux / macOS
```
- Ubuntu 18.04+ / Debian 10+ / macOS 10.14+
- Python 3.8+
- pip3
- Git
```

### 2. Install Python

**Windows:**
1. Download dari https://www.python.org/downloads/
2. Jalankan installer
3. ✅ Centang "Add Python to PATH"
4. Klik "Install Now"

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip git
```

**macOS:**
```bash
# Dengan Homebrew
brew install python3 git

# Atau download dari https://www.python.org/downloads/
```

### 3. Clone Repository

```bash
# Menggunakan HTTPS
git clone https://github.com/stev170/cb-phonehunter.git
cd cb-phonehunter

# Atau menggunakan SSH
git clone git@github.com:stev170/cb-phonehunter.git
cd cb-phonehunter
```

### 4. Install Dependensi

```bash
# Windows
pip install -r requirements.txt

# Linux / macOS
pip3 install -r requirements.txt
```

**Jika ada error**, instalasi manual:
```bash
pip install requests colorama phonenumbers dnspython
```

### 5. Jalankan Program

```bash
# Windows
python cb_phone_hunter.py

# Linux / macOS
python3 cb_phone_hunter.py
```

✅ Program siap digunakan!

---

## Panduan Penggunaan

### Startup Awal

```
$ python3 cb_phone_hunter.py

              ...::::...               
              ..:::+: ....             
        .:...:::::::.  ..:....... ..   

  Ciberbrigada OSINT Suite  ─────────────────────
  ╔══════════════════════════════════════════╗
  ║  📱  CB-PHONEHUNTER  v2.0               ║
  ║  Phone OSINT — Data nyata di terminal   ║
  ╚══════════════════════════════════════════╝
  [ ciberbrigada.com ]  [ OSINT Suite ]
  ⚠  Hanya untuk penggunaan yang sah, etis, dan edukatif  ⚠

  Masukkan nomor dengan kode negara:
  Contoh: +62 812 3456-7890 | +1 555 123 4567 | +34 612 345 678

  ▸ Nomor: 
```

### Input Nomor

Masukkan nomor dengan kode negara internasional:

```
▸ Nomor: +62 812 3456-7890
```

**Format yang diterima:**
```
✅ +62 812 3456-7890     (dengan spasi)
✅ +628123456789         (tanpa spasi)
✅ +62-812-3456-7890     (dengan dash)
✅ +62812 3456 7890      (campuran)
```

### Output Analisis Modul 1

```
── ANALISIS NOMOR ──
  ▸ Nomor internasional: +62 812 3456-7890
  ▸ Format E164:         +628123456789
  ▸ Format nasional:     0812 3456-7890
  ▸ Valid:               ✓ YA
  ▸ Mungkin:             ✓ YA
  ▸ Negara:              Indonesia
  ▸ Kode wilayah:        ID
  ▸ Kode negara:         +62
  ▸ Operator:            Telkomsel
  ▸ Zona waktu:          Asia/Jakarta
  ▸ Tipe line:           📱 SELULER
  ▸ Nomor nasional:      8123456789
  ▸ Kode area:           812
```

### Pemilihan Modul

```
── PILIH MODUL ──
  [2] Veriphone        — Operator, tipe & negara (API gratis)
  [3] NumVerify        — Validasi & operator
  [4] DNS / ENUM       — Protokol E.164 & infrastruktur
  [5] WhatsApp         — Apakah punya akun aktif?
  [6] Telegram         — Apakah punya akun aktif?
  [7] Gravatar         — Profil terkait nomor
  [0] SEMUA MODUL

  ▸ Pilihan (contoh: 0 atau 2,5,6):
```

**Opsi Input:**
- `0` - Jalankan semua modul
- `2` - Hanya Veriphone
- `2,5,6` - Veriphone, WhatsApp, Telegram (tanpa spasi)
- `5,7` - WhatsApp & Gravatar

### Output Veriphone

```
── VERIPHONE — Validasi & Operator ──
  [✓] Data berhasil diambil dari Veriphone
  ▸ Nomor:          +62812 345 6789
  ▸ Internasional:  +62 812 345 6789
  ▸ Lokal:          812 345 6789
  ▸ Negara:         Indonesia
  ▸ Kode negara:    62
  ▸ Prefiks:        +62
  ▸ Operator:       Telkomsel
  ▸ Tipe line:      MOBILE
  ▸ Valid:          ✓ YA
  ▸ Wilayah:        ID
```

### Output WhatsApp

```
── WHATSAPP — Verifikasi akun ──
  [✓] ✓ Nomor AKTIF di WhatsApp
  ▸ Nomor:         +62 812 3456-7890
  ▸ Tautan chat:   https://wa.me/628123456789
  ▸ Tautan langsung: https://api.whatsapp.com/send?phone=628123456789
```

Atau:

```
  [✗] Nomor TIDAK terdaftar di WhatsApp
```

### Output Telegram

```
── TELEGRAM — Verifikasi akun ──
  [✓] Nomor ditemukan di Telegram
  ▸ Tautan langsung: https://t.me/+628123456789
```

---

## Penjelasan Modul

### Modul 1: Analisis Lokal (Offline)

**Apa:** Analisis dasar nomor menggunakan perpustakaan `phonenumbers`

**Informasi yang Diberikan:**
- Format internasional & nasional
- Validasi nomor
- Negara & kode wilayah
- Operator (dari basis lokal)
- Zona waktu
- Tipe line (seluler, tetap, VoIP, dll)

**Keuntungan:**
- ✅ Bekerja offline
- ✅ Cepat & akurat
- ✅ Tidak ada batasan permintaan

**Keterbatasan:**
- ❌ Operator mungkin tidak lengkap
- ❌ Data berdasarkan format saja

---

### Modul 2: Veriphone

**Apa:** Validasi nomor via API Veriphone

**Informasi yang Diberikan:**
- Validasi nomor real
- Nama operator aktual
- Tipe line sebenarnya
- Format internasional & lokal
- Wilayah geografis

**Keuntungan:**
- ✅ Data real-time dari provider
- ✅ Akurat untuk operator seluler
- ✅ Gratis tanpa API key

**Keterbatasan:**
- ❌ Memerlukan internet
- ❌ Ada rate limit (~100 permintaan/hari)
- ❌ Mungkin tidak tersedia untuk nomor statis

**Pesan Error:**
```
  [!] Rate limit di Veriphone — coba beberapa menit lagi
```
→ Tunggu 5-10 menit sebelum mencoba lagi

---

### Modul 3: NumVerify

**Apa:** Verifikasi tambahan via API NumVerify

**Informasi yang Diberikan:**
- Validasi terpisah dari Veriphone
- Lokasi geografis lebih detail
- Format berbagai tipe
- Operator alternatif

**Keuntungan:**
- ✅ Sumber data independen
- ✅ Verifikasi cross-check
- ✅ Format lokal lengkap

**Keterbatasan:**
- ❌ Terkadang kurang akurat untuk negara tertentu
- ❌ API tier gratis terbatas

---

### Modul 4: DNS & ENUM

**Apa:** Pencarian infrastruktur telepon via DNS

**Protokol:**
- **ENUM (E.164 User ARPA DNS)** — RFC 3761
- **NAPTR (Naming Authority Pointer Records)**
- **Reverse DNS (PTR)**

**Contoh Pencarian:**
```
Nomor: +628123456789
Konversi ENUM: 9.8.7.6.5.4.3.2.1.8.2.6.e164.arpa
Query: NAPTR records
```

**Informasi yang Diberikan:**
- NAPTR records (jika ada)
- PTR records (jika ada)
- Operator yang dikenal di negara tersebut

**Keuntungan:**
- ✅ Data infrastruktur teknis
- ✅ Tidak ada rate limit
- ✅ Sumber resmi (DNS)

**Keterbatasan:**
- ❌ Banyak nomor tidak punya ENUM records
- ❌ Memerlukan pengetahuan teknis untuk interpretasi

**Pesan Umum:**
```
  [i] Tidak ada rekaman ENUM (umum untuk nomor seluler)
```
→ Normal untuk nomor seluler modern

---

### Modul 5: WhatsApp

**Apa:** Verifikasi keaktifan akun WhatsApp

**Metode:**
1. Akses `https://wa.me/{nomor}`
2. Analisis response & HTML
3. Verifikasi API WhatsApp (opsional)

**Hasil Positif:**
```
  [✓] ✓ Nomor AKTIF di WhatsApp
```
→ Nomor terdaftar & akun aktif

**Hasil Negatif:**
```
  [✗] Nomor TIDAK terdaftar di WhatsApp
```
→ Nomor tidak pernah membuat akun WhatsApp

**Hasil Tidak Pasti:**
```
  [!] Tidak dapat memastikan akun WhatsApp
```
→ Status tidak jelas (privasi tinggi, API error, dll)

**Keuntungan:**
- ✅ Verifikasi langsung dari WhatsApp
- ✅ Link chat siap digunakan
- ✅ Akurat untuk user aktif

**Keterbatasan:**
- ❌ Tidak bisa diferensiasi antara user aktif vs inactive
- ❌ WhatsApp bisa memblokir/rate limit

---

### Modul 6: Telegram

**Apa:** Pencarian nomor di Telegram & TGStat

**Metode:**
1. Cek `https://t.me/+{nomor}`
2. Pencarian di TGStat.com
3. Analisis hasil

**Hasil Positif:**
```
  [✓] Nomor ditemukan di Telegram
  ▸ Tautan langsung: https://t.me/+628123456789
```
→ Nomor terhubung dengan profil/channel Telegram

**Hasil Negatif:**
```
  [!] Tidak ditemukan akun Telegram untuk nomor ini
```
→ Nomor tidak terhubung di Telegram

**Keuntungan:**
- ✅ Telegram lebih public-friendly
- ✅ Bisa menemukan channel/bot terkait
- ✅ Tautan langsung ke profil

**Keterbatasan:**
- ❌ Hanya untuk nomor yang link ke Telegram
- ❌ TGStat mungkin tidak selalu akurat

---

### Modul 7: Gravatar

**Apa:** Profil Gravatar terkait hash nomor

**Metode:**
1. Hash nomor dengan MD5
2. Query API Gravatar
3. Extract profil & social links

**Hasil Positif:**
```
  [✓] Profil Gravatar ditemukan untuk nomor ini
  ▸ Nama tampilan:   Budi Santoso
  ▸ Username:        budisantoso
  ▸ Avatar:          https://www.gravatar.com/avatar/...
  ▸ URL profil:      https://gravatar.com/budisantoso
  ▸ Akun [Twitter]:  https://twitter.com/budisantoso
  ▸ Akun [GitHub]:   https://github.com/budisantoso
  ▸ Bio:             Software Engineer based in Jakarta
```

**Hasil Negatif:**
```
  [!] Tidak ada profil Gravatar terkait dengan nomor ini
```
→ Email terkait nomor tidak punya profil Gravatar

**Keuntungan:**
- ✅ Linked social profiles
- ✅ Bio & informasi publik
- ✅ Email verification indirectly

**Keterbatasan:**
- ❌ Hanya untuk email yang pernah register Gravatar
- ❌ Tidak semua Gravatar lengkap

---

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'requests'"

**Penyebab:** Dependensi belum terinstall

**Solusi:**
```bash
pip install -r requirements.txt

# Atau manual
pip install requests colorama phonenumbers dnspython
```

---

### Error: "No module named 'phonenumbers'"

**Penyebab:** Library phonenumbers tidak terinstall

**Solusi:**
```bash
pip install phonenumbers
```

---

### Error: "Connection timeout"

**Penyebab:** 
- Internet lambat/terputus
- API server down
- Rate limit tercapai

**Solusi:**
1. Cek koneksi internet: `ping google.com`
2. Tunggu beberapa menit
3. Coba nomor berbeda
4. Jalankan ulang program

---

### Error: "Invalid phone number"

**Penyebab:** Format nomor tidak valid

**Solusi:**
- Selalu include kode negara: `+62...`
- Gunakan format internasional: `+[country][area][number]`
- Contoh benar: `+62 812 3456-7890`

```bash
# Salah
▸ Nomor: 0812 3456-7890

# Benar
▸ Nomor: +62 812 3456-7890
```

---

### Error: "Rate limit"

**Penyebab:** Terlalu banyak permintaan dalam waktu singkat

**Pesan:**
```
[!] Rate limit di Veriphone — coba beberapa menit lagi
```

**Solusi:**
1. Tunggu 5-10 menit
2. Gunakan modul 1 (offline) saja
3. Coba API lain (NumVerify, dll)
4. Jalankan ulang nanti

---

### Output kosong atau "—"

**Penyebab:** API tidak punya data untuk nomor tersebut

**Contoh:**
```
  ▸ Operator:         —
  ▸ Lokasi:           —
```

**Solusi:**
- Nomor mungkin tidak valid
- Operator mungkin tidak terdaftar di database
- Coba API/modul lain
- Verifikasi format nomor

---

### Program crash/hang

**Penyebab:**
- Internet putus saat request
- API timeout
- Bug dalam parsing

**Solusi:**
1. Tekan `Ctrl+C` untuk stop
2. Pastikan internet stabil
3. Update program: `git pull`
4. Reinstall dependencies

---

## FAQ

### P: Apa yang dimaksud dengan "E164 format"?
**J:** Format standar internasional: `+[kode_negara][area][nomor]`
```
Contoh: +628123456789
- + = simbol internasional
- 62 = kode negara Indonesia
- 812 = kode area
- 3456789 = nomor
```

---

### P: Berapa lama analisis untuk satu nomor?
**J:** 
- Modul 1: < 1 detik (offline)
- Per modul online: 2-5 detik
- Semua modul: 15-30 detik

---

### P: Bisa batch processing (banyak nomor)?
**J:** Belum di implementasi dalam versi ini. Workaround:
```bash
# Jalankan dalam loop manual
for nomor in +62812xxx +62821xxx +62822xxx; do
  echo "$nomor" | python3 cb_phone_hunter.py
done
```

---

### P: Output bisa disimpan ke file?
**J:** Ya, dengan redirect:
```bash
# Linux/macOS
python3 cb_phone_hunter.py > hasil.txt 2>&1

# Windows PowerShell
python cb_phone_hunter.py | Out-File hasil.txt
```

---

### P: Apakah aman untuk privasi?
**J:** 
- ✅ Data tidak disimpan lokal
- ✅ Hanya API publik yang digunakan
- ✅ HTTPS untuk koneksi
- ⚠️ Data dikirim ke API eksternal (baca privacy policy mereka)

---

### P: Bisa offline 100%?
**J:** Hanya Modul 1 (Analisis Lokal) yang 100% offline. Modul lain memerlukan internet.

---

### P: Kemana data saya dikirim?
**J:** 
- Veriphone: https://veriphone.io
- NumVerify: https://apilayer.net
- DNS: Ke DNS server lokal Anda
- WhatsApp: Ke server WhatsApp
- Telegram: Ke server Telegram
- Gravatar: Ke gravatar.com

---

### P: Bisa digunakan di Android/iPhone?
**J:** Belum. Alternatif:
- Install Python di Android (Termux)
- Cloud terminal (replit.com, etc)
- Web wrapper (development in progress)

---

### P: Gimana cara kontribusi?
**J:** 
1. Fork repository
2. Buat branch: `git checkout -b fitur/x`
3. Commit: `git commit -m "Tambah x"`
4. Push: `git push origin fitur/x`
5. Pull Request ke main

---

<p align="center">
  <b>Butuh bantuan lebih?</b>
  <br/>
  Buka issue di: https://github.com/stev170/cb-phonehunter/issues
</p>
