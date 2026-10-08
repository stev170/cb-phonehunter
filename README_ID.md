# 📱 CB-PhoneHunter

Alat OSINT untuk pengumpulan dan analisis informasi nomor telepon.

## ¿Qué hace?

CB-PhoneHunter adalah tool yang dirancang untuk membantu investigator dan security researcher dalam mengumpulkan informasi terkait nomor telepon melalui berbagai modul OSINT.

## Instalasi

### Kali Linux / Parrot OS / Ubuntu

```bash
git clone https://github.com/stev170/cb-phonehunter.git
cd cb-phonehunter
pip install -r requirements.txt
python3 cb-phonehunter.py
```

### Windows

1. Download Python dari [python.org](https://www.python.org)
2. Clone repository
3. Buka Command Prompt dan jalankan:

```bash
pip install -r requirements.txt
python cb-phonehunter.py
```

## 🔄 Memperbarui

Untuk mendapatkan versi terbaru:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Penggunaan

```bash
python3 cb-phonehunter.py -n +1234567890
```

## Modul

- **Validasi Nomor**: Verifikasi format dan validitas nomor telepon
- **Lookup Operator**: Identifikasi operator penyedia layanan
- **OSINT Modules**: Pencarian informasi di berbagai sumber publik

## Format Input

Nomor telepon harus dalam format internasional:
- `+[Kode Negara][Nomor]`
- Contoh: `+62812345678`

## Persyaratan

- Python 3.8+
- requests >= 2.31.0
- colorama >= 0.4.6
- phonenumbers >= 8.13.0
- dnspython >= 2.3.0

## ⚠️ Pemberitahuan Hukum

Tool ini hanya untuk tujuan pendidikan dan legal. Pengguna bertanggung jawab atas penggunaan dan mematuhi hukum setempat.

## 🛡️ Ciberbrigada OSINT Suite

Bagian dari rangkaian tool OSINT Ciberbrigada untuk security research dan intelligence gathering yang legal dan etis.
