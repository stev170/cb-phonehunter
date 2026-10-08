#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════[...]
#   CB-PHONEHUNTER v2.0 — Ciberbrigada OSINT Suite
#   Pengenalan OSINT nomor telepon — Data nyata di terminal
#   Hanya untuk tujuan yang sah, etis, dan edukatif
# ══════════════════════════════════════════════════════════════════[...]

import sys
import os

# Deteksi Termux/Android
IS_TERMUX = (
    os.environ.get("PREFIX", "").startswith("/data/data/com.termux")
    or os.path.exists("/data/data/com.termux/files/usr/bin/pkg")
    or os.environ.get("ANDROID_ROOT") is not None
)

# Install dependencies
try:
    import requests
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone as pn_timezone
    import dns.resolver
    from colorama import init, Fore, Style
except ImportError:
    print("[*] Menginstal dependensi yang diperlukan...")
    if IS_TERMUX:
        os.system("python -m pip install requests colorama phonenumbers dnspython -q 2>/dev/null")
    else:
        os.system("pip install requests colorama phonenumbers dnspython --break-system-packages -q 2>/dev/null")

    try:
        import requests
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone as pn_timezone
        import dns.resolver
        from colorama import init, Fore, Style
        print("[✓] Dependensi berhasil diinstal\n")
    except ImportError as e:
        print(f"[✗] Gagal menginstal: {e}")
        print("\nCoba install manual:")
        if IS_TERMUX:
            print("  python -m pip install requests colorama phonenumbers dnspython")
        else:
            print("  pip install requests colorama phonenumbers dnspython")
        sys.exit(1)

init(autoreset=True)

import re
import json
import socket
import urllib.parse
import hashlib

# ── Warna ─────────────────────────────────────────────────────────────[.[...]
C = Fore.CYAN
Y = Fore.YELLOW
G = Fore.GREEN
R = Fore.RED
W = Fore.WHITE
D = Fore.WHITE + Style.DIM
B = Style.BRIGHT
RS = Style.RESET_ALL

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "id-ID,id;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

HEADERS_JSON = {**HEADERS, "Accept": "application/json, text/plain, */*"}

COUNTRY_NAMES = {
    "AR": "Argentina", "US": "Amerika Serikat", "MX": "Meksiko",
    "BR": "Brasil", "CO": "Kolombia", "CL": "Chili", "PE": "Peru",
    "VE": "Venezuela", "EC": "Ekuador", "BO": "Bolivia", "PY": "Paraguay",
    "UY": "Uruguay", "ES": "Spanyol", "DE": "Jerman", "FR": "Prancis",
    "IT": "Italia", "GB": "Britania Raya", "PT": "Portugal", "RU": "Rusia",
    "CN": "China", "JP": "Jepang", "IN": "India", "AU": "Australia",
    "CA": "Kanada", "ZA": "Afrika Selatan", "NG": "Nigeria", "EG": "Mesir",
    "TR": "Turki", "SA": "Arab Saudi", "AE": "Uni Emirat Arab",
    "IL": "Israel", "KR": "Korea Selatan", "TH": "Thailand",
    "PH": "Filipina", "ID": "Indonesia", "PK": "Pakistan",
    "NL": "Belanda", "BE": "Belgia", "SE": "Swedia",
    "NO": "Norwegia", "DK": "Denmark", "FI": "Finlandia",
    "PL": "Polandia", "UA": "Ukraina", "RO": "Rumania",
    "HU": "Hungaria", "CZ": "Republik Ceko",
}

TIPOS_LINEA = {
    0: "📞 FIXED",
    1: "📱 SELULER",
    2: "📞📱 FIXED ATAU SELULER",
    3: "🆓 GRATIS (0800)",
    4: "💰 PREMIUM",
    5: "🔀 BIAYA BERSAMA",
    6: "🌐 VoIP",
    7: "📟 PAGER",
    8: "🔧 UAN",
    27: "❓ TIDAK DIKETAHUI",
}

# ---------- helpers ----------
def sep(titulo=""):
    if titulo:
        pad = (56 - len(titulo)) // 2
        print(f"\n{C}{'─'*pad} {B}{titulo}{RS}{C} {'─'*pad}{RS}")
    else:
        print(f"{D}{'─'*60}{RS}")


def ok(msg):
    print(f"  {G}{B}[✓]{RS} {W}{msg}{RS}")


def warn(msg):
    print(f"  {Y}[!]{RS} {Y}{msg}{RS}")


def fail(msg):
    print(f"  {R}[✗]{RS} {D}{msg}{RS}")


def info(msg):
    print(f"  {C}[i]{RS} {W}{msg}{RS}")


def dato(k, v):
    print(f"  {C}  ▸ {D}{k}:{RS} {W}{B}{v}{RS}")


def safe_request(url, timeout=10):
    try:
        return requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
    except Exception:
        return None


def banner():
    os.system("cls" if os.name == "nt" else "clear")
    CYAN = '\033[96m'; ORAN = '\033[38;5;208m'
    DIM = '\033[2m\033[37m'; BOLD = '\033[1m'
    YEL = '\033[33m'; RST = '\033[0m'
    logo = [
        "              ...::::...               ",
        "              ..:::+: ....             ",
        "        .:...:::::::.  ..:....... ..   ",
        "       :+  .:::::::    ::::::::::.     ",
        "      .+. .::::::::    +::::::::++::   ",
        "    . ::.:+:.          :::       ::+:  ",
        "   .: :::+.            +:+       .+++  ",
        "   .+ .+::             +:+.    .:+++.  ",
        "    +: :+.             ++++++++++++:   ",
        "     +:.:+             +++:......:+++: ",
        "   :. :++++.           +++         ++%:",
        "    ::  .::+++:::::    +++        .++%:",
        "     .:::....::++++   .+++:.....::+++: ",
        "   ... ..:+::+::+++:. ::++++++++++:.   ",
        "     :+:. :+.:+:.:++::......  ...      ",
        "       :+: :+..++...::::.......         ",
        "         .. :+:..:+:.........           ",
    ]
    print()
    for line in logo:
        mid = len(line) // 2
        print(f"       {CYAN}{BOLD}{line[:mid]}{ORAN}{line[mid:]}{RST}")
    print(f"                          {DIM}by: Fgunther{RST}")
    print()
    print(f"  {CYAN}{BOLD}Ciber{ORAN}brigada{RST} {CYAN}OSINT Suite{RST}  {DIM}─────────────────────{RST}")
    print(f"  {BOLD}╔══════════════════════════════════════════╗{RST}")
    print(f"  {BOLD}║  📱  CB-PHONEHUNTER  v2.0               ║{RST}")
    print(f"  {BOLD}║  Phone OSINT — Data nyata di terminal ║{RST}")
    print(f"  {BOLD}╚══════════════════════════════════════════╝{RST}")
    print(f"  {DIM}[ ciberbrigada.com ]  [ OSINT Suite ]{RST}")
    print(f"  {YEL}⚠  Hanya untuk penggunaan yang sah, etis, dan edukatif  ⚠{RST}")
    print()


# ---------- modul 1 ----------
def modulo_analisis(phone_raw):
    sep("ANALISIS NOMOR")
    try:
        try:
            parsed = phonenumbers.parse(phone_raw)
        except Exception:
            parsed = phonenumbers.parse(phone_raw, "AR")

        es_valido = phonenumbers.is_valid_number(parsed)
        es_posible = phonenumbers.is_possible_number(parsed)

        fmt_intl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        fmt_e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        fmt_nac = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)

        dato("Nomor internasional", fmt_intl)
        dato("Format E164", fmt_e164)
        dato("Format nasional", fmt_nac)
        dato("Valid", f"{'✓ YA' if es_valido else '✗ TIDAK'}")
        dato("Mungkin", f"{'✓ YA' if es_posible else '✗ TIDAK'}")

        region = phonenumbers.region_code_for_number(parsed)
        pais_nombre = COUNTRY_NAMES.get(region, geocoder.description_for_number(parsed, "id") or "Tidak diketahui")
        dato("Negara", pais_nombre)
        dato("Kode wilayah", region or "—")
        dato("Kode negara", f"+{parsed.country_code}")

        pais_geo = geocoder.description_for_number(parsed, "id")
        if pais_geo and pais_geo != pais_nombre:
            dato("Zona geografis", pais_geo)

        op = carrier.name_for_number(parsed, "id")
        dato("Operator", op if op else "Tidak tersedia di basis lokal")

        zonas = list(pn_timezone.time_zones_for_number(parsed))
        dato("Zona waktu", ", ".join(zonas) if zonas else "Tidak tersedia")

        tipo = phonenumbers.number_type(parsed)
        dato("Tipe line", TIPOS_LINEA.get(tipo, "❓ Tidak diketahui"))

        dato("Nomor nasional", str(parsed.national_number))
        dato("Kode area", str(parsed.national_number)[:3])

        if not es_valido:
            warn("Nomor ini tampaknya tidak valid untuk wilayah yang terdeteksi")

        return fmt_e164, fmt_intl, parsed, region
    except Exception as e:
        fail(f"Error saat menganalisis: {e}")
        warn("Masukkan kode negara. Contoh: +62 812 3456-7890")
        return None, None, None, None


# ---------- modul 2 ----------
def modulo_veriphone(fmt_e164):
    sep("VERIPHONE — Validasi & Operator")
    try:
        r = requests.get(
            f"https://api.veriphone.io/v2/verify?phone={urllib.parse.quote(fmt_e164)}&key=demo",
            headers=HEADERS_JSON, timeout=12
        )
        if r.status_code == 200:
            d = r.json()
            if d.get("status") == "success" or d.get("phone_valid"):
                ok("Data berhasil diambil dari Veriphone")
                dato("Nomor", d.get("phone", "—"))
                dato("Internasional", d.get("international_number", "—"))
                dato("Lokal", d.get("local_number", "—"))
                dato("Negara", d.get("country", "—"))
                dato("Kode negara", d.get("country_code", "—"))
                dato("Prefiks", d.get("country_prefix", "—"))
                dato("Operator", d.get("carrier", "—"))
                dato("Tipe line", d.get("phone_type", "—").upper())
                dato("Valid", "✓ YA" if d.get("phone_valid") else "✗ TIDAK")
                dato("Wilayah", d.get("phone_region", "—"))
            else:
                warn("Veriphone tidak mengembalikan data untuk nomor ini")
        elif r.status_code == 429:
            warn("Rate limit di Veriphone — coba beberapa menit lagi")
        else:
            warn(f"Veriphone merespons {r.status_code}")
    except Exception as e:
        warn(f"Veriphone tidak tersedia: {type(e).__name__}")


# ---------- modul 3 ----------
def modulo_numverify(fmt_e164, region):
    sep("NUMVERIFY — Operator & Line")
    phone_clean = fmt_e164.replace("+", "")
    try:
        r = requests.get(
            f"http://apilayer.net/api/validate?number={phone_clean}&format=1",
            headers=HEADERS_JSON, timeout=10
        )
        if r.status_code == 200:
            d = r.json()
            if d.get("valid"):
                ok("Nomor divalidasi oleh NumVerify")
                dato("Nomor", d.get("number", "—"))
                dato("Format lokal", d.get("local_format", "—"))
                dato("Internasional", d.get("international_format", "—"))
                dato("Negara", d.get("country_name", "—"))
                dato("Kode negara", d.get("country_code", "—"))
                dato("Prefiks", d.get("country_prefix", "—"))
                dato("Operator", d.get("carrier", "—"))
                dato("Tipe line", d.get("line_type", "—").upper() if d.get("line_type") else "—")
                dato("Lokasi", d.get("location", "—"))
            else:
                warn("NumVerify: nomor tidak valid atau tidak ada data")
        else:
            warn(f"NumVerify merespons {r.status_code}")
    except Exception as e:
        warn(f"NumVerify tidak tersedia: {type(e).__name__}")


# ---------- modul 4 ----------
def modulo_dns(fmt_e164, region):
    sep("DNS & INFRASTRUKTUR")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "")
    try:
        digits = phone_clean[::-1]
        enum_domain = ".".join(list(digits)) + ".e164.arpa"
        dato("Domain ENUM", enum_domain)
        try:
            naptr = dns.resolver.resolve(enum_domain, 'NAPTR')
            ok("Rekaman NAPTR ditemukan (ENUM)")
            for record in naptr:
                dato("  NAPTR", str(record))
        except Exception:
            info("Tidak ada rekaman ENUM (umum untuk nomor seluler)")

        try:
            reversed_ip = dns.resolver.resolve(f"{phone_clean[::-1]}.e164.arpa", 'PTR')
            for r in reversed_ip:
                dato("  PTR", str(r))
        except Exception:
            pass
    except Exception as e:
        warn(f"DNS lookup gagal: {type(e).__name__}")

    country_carriers = {
        "AR": ["Personal (Telecom)", "Claro (AMX Argentina)", "Movistar (Telefónica)", "Tuenti"],
        "MX": ["Telcel", "Movistar Meksiko", "AT&T Meksiko", "Unefon"],
        "CO": ["Claro Kolombia", "Movistar Kolombia", "Tigo", "WOM"],
        "CL": ["Entel", "Movistar Chili", "Claro Chili", "WOM Chili"],
        "BR": ["Vivo", "TIM", "Claro Brasil", "Oi"],
        "PE": ["Claro Peru", "Movistar Peru", "Entel Peru", "Bitel"],
        "US": ["AT&T", "Verizon", "T-Mobile", "Sprint"],
        "ES": ["Movistar Spanyol", "Vodafone Spanyol", "Orange Spanyol", "Yoigo"],
        "ID": ["Telkomsel", "Indosat", "XL Axiata", "Tri"],
    }

    if region and region in country_carriers:
        info(f"Operator yang dikenal di {COUNTRY_NAMES.get(region, region)}:")
        for op in country_carriers[region]:
            print(f"    {D}• {op}{RS}")


# ---------- modul 5 ----------
def modulo_whatsapp(fmt_e164):
    sep("WHATSAPP — Verifikasi akun")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "")
    try:
        r = requests.get(f"https://wa.me/{phone_clean}", headers=HEADERS, timeout=10, allow_redirects=True)
        body = r.text.lower()

        if r.status_code == 200:
            if any(x in body for x in ["send message", "open whatsapp", "use whatsapp web", "whatsapp"]):
                ok("✓ Nomor AKTIF di WhatsApp")
                dato("Nomor", fmt_e164)
                dato("Tautan chat", f"https://wa.me/{phone_clean}")
                dato("Tautan langsung", f"https://api.whatsapp.com/send?phone={phone_clean}")
            else:
                warn("Tidak dapat memastikan akun WhatsApp")
        elif r.status_code == 404:
            fail("Nomor TIDAK terdaftar di WhatsApp")
        else:
            warn(f"WhatsApp merespons {r.status_code}")

        try:
            r2 = requests.get(f"https://api.whatsapp.com/send?phone={phone_clean}", headers=HEADERS, timeout=8, allow_redirects=True)
            if r2.status_code == 200 and "phone" in r2.text.lower():
                dato("Verifikasi API", "Nomor ditemukan di sistem WhatsApp")
        except Exception:
            pass
    except Exception as e:
        warn(f"Tidak dapat memverifikasi WhatsApp: {type(e).__name__}")


# ---------- modul 6 ----------
def modulo_telegram(fmt_e164):
    sep("TELEGRAM — Verifikasi akun")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "")
    try:
        r = requests.get(f"https://t.me/+{phone_clean}", headers=HEADERS, timeout=10, allow_redirects=True)
        body = r.text.lower()

        if r.status_code == 200:
            if "tgme_page_title" in body or "telegram" in body:
                if "join" in body or "preview" in body:
                    ok("Nomor ditemukan di Telegram")
                    dato("Tautan langsung", f"https://t.me/+{phone_clean}")
                else:
                    warn("Telegram merespons tapi tanpa profil yang jelas")
            else:
                warn("Tidak ditemukan akun Telegram untuk nomor ini")
        else:
            warn(f"Telegram merespons {r.status_code}")

        try:
            r2 = requests.get(f"https://tgstat.com/search?q={urllib.parse.quote(fmt_e164)}", headers=HEADERS, timeout=8)
            if r2.status_code == 200 and phone_clean in r2.text:
                ok("Nomor disebutkan di TGStat")
                dato("TGStat", f"https://tgstat.com/search?q={urllib.parse.quote(fmt_e164)}")
        except Exception:
            pass
    except Exception as e:
        warn(f"Tidak dapat memverifikasi Telegram: {type(e).__name__}")


# ---------- modul 7 ----------
def modulo_gravatar(fmt_e164):
    sep("GRAVATAR — Profil terkait")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").strip()
    md5_hash = hashlib.md5(phone_clean.encode()).hexdigest()
    try:
        r = requests.get(f"https://www.gravatar.com/{md5_hash}.json", headers=HEADERS_JSON, timeout=8)
        if r.status_code == 200:
            d = r.json()
            entry = d.get("entry", [{}])[0]
            ok("Profil Gravatar ditemukan untuk nomor ini")
            dato("Nama tampilan", entry.get("displayName", "—"))
            dato("Username", entry.get("preferredUsername", "—"))
            dato("Avatar", f"https://www.gravatar.com/avatar/{md5_hash}?s=200")
            dato("URL profil", f"https://gravatar.com/{entry.get('preferredUsername','')}")
            for acc in entry.get("accounts", []):
                dato(f"Akun [{acc.get('shortname','?')}]", acc.get("url", "—"))
            about = entry.get("aboutMe", "")
            if about:
                dato("Bio", about[:100])
        elif r.status_code == 404:
            warn("Tidak ada profil Gravatar terkait dengan nomor ini")
        else:
            warn(f"Gravatar merespons {r.status_code}")
    except Exception as e:
        warn(f"Gravatar tidak tersedia: {type(e).__name__}")


# ---------- generic social link helpers ----------
def print_valid_search_links(title, urls, note=""):
    sep(title)
    if note:
        info(note)
    for idx, url in enumerate(urls, start=1):
        dato(f"{idx}. URL", url)


def domain_url_ok(urls, timeout=10):
    for url in urls:
        r = safe_request(url, timeout)
        if r is not None and r.status_code == 200:
            return True, url, r.status_code
    return False, urls[0] if urls else "", 0


# ---------- social modules ----------
def modulo_twitter(fmt_e164):
    sep("TWITTER/X — Pencarian & hasil valid")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://x.com/search?q={urllib.parse.quote(fmt_e164)}&src=typed_query",
        f"https://x.com/search?q={urllib.parse.quote(phone_clean)}&src=typed_query",
        f"https://x.com/search?q={urllib.parse.quote(f'"{fmt_e164}"')}&src=typed_query",
    ]
    ok, url, status = domain_url_ok(urls)
    if ok:
        ok("Pencarian Twitter/X dibuat dengan URL yang valid")
        dato("Nomor", fmt_e164)
        dato("URL pencarian", url)
        info("Hasil real hanya terlihat di halaman Twitter/X; situs bisa membatasi index pencarian")
    else:
        warn("Tidak dapat mengakses Twitter/X dari terminal")
        for u in urls:
            print(f"    {D}• {u}{RS}")


def modulo_facebook(fmt_e164):
    sep("FACEBOOK — Pencarian profil")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://www.facebook.com/search/top/?q={urllib.parse.quote(fmt_e164)}",
        f"https://www.facebook.com/search/people/?q={urllib.parse.quote(fmt_e164)}",
        f"https://www.facebook.com/search/top/?q={urllib.parse.quote(phone_clean)}",
    ]
    ok, url, status = domain_url_ok(urls)
    if ok:
        ok("Pencarian Facebook dibuat dengan URL yang valid")
        dato("Nomor", fmt_e164)
        dato("URL pencarian", url)
        info("Facebook sering membatasi pencarian kontak publik, hasil bisa terbatas")
    else:
        warn("Tidak dapat membuka pencarian Facebook dari terminal")
        for u in urls:
            print(f"    {D}• {u}{RS}")


def modulo_tiktok(fmt_e164):
    sep("TIKTOK — Pencarian akun")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://www.tiktok.com/search?q={urllib.parse.quote(fmt_e164)}",
        f"https://www.tiktok.com/search?q={urllib.parse.quote(phone_clean)}",
        f"https://www.tiktok.com/search?q={urllib.parse.quote(f'"{fmt_e164}"')}",
    ]
    ok, url, status = domain_url_ok(urls)
    if ok:
        ok("Pencarian TikTok dibuat dengan URL yang valid")
        dato("Nomor", fmt_e164)
        dato("URL pencarian", url)
        info("TikTok tidak selalu menampilkan nomor telepon sebagai hasil publik")
    else:
        warn("Tidak dapat membuka pencarian TikTok dari terminal")
        for u in urls:
            print(f"    {D}• {u}{RS}")


def modulo_instagram(fmt_e164):
    sep("INSTAGRAM — Pencarian akun")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://www.instagram.com/explore/search/keyword/?q={urllib.parse.quote(fmt_e164)}",
        f"https://www.instagram.com/explore/search/keyword/?q={urllib.parse.quote(phone_clean)}",
        f"https://www.instagram.com/explore/search/keyword/?q={urllib.parse.quote(f'"{fmt_e164}"')}",
    ]
    ok, url, status = domain_url_ok(urls)
    if ok:
        ok("Pencarian Instagram dibuat dengan URL yang valid")
        dato("Nomor", fmt_e164)
        dato("URL pencarian", url)
        info("Instagram tidak menyediakan hasil nomor telepon yang andal secara publik")
    else:
        warn("Tidak dapat membuka pencarian Instagram dari terminal")
        for u in urls:
            print(f"    {D}• {u}{RS}")


def modulo_linkedin(fmt_e164):
    sep("LINKEDIN — Pencarian profil profesional")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://www.linkedin.com/search/results/people/?keywords={urllib.parse.quote(fmt_e164)}",
        f"https://www.linkedin.com/search/results/people/?keywords={urllib.parse.quote(phone_clean)}",
        f"https://www.linkedin.com/search/results/all/?keywords={urllib.parse.quote(f'phone:{phone_clean}')}",
    ]
    ok, url, status = domain_url_ok(urls)
    if ok:
        ok("Pencarian LinkedIn dibuat dengan URL yang valid")
        dato("Nomor", fmt_e164)
        dato("URL pencarian", url)
        info("LinkedIn membatasi hasil publik, tapi tautan pencarian tetap valid")
    else:
        warn("Tidak dapat membuka pencarian LinkedIn secara langsung")
        for u in urls:
            print(f"    {D}• {u}{RS}")


def modulo_getcontact(fmt_e164):
    sep("GETCONTACT — Database kontak global")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://www.getcontact.com/search?q={urllib.parse.quote(fmt_e164)}",
        f"https://www.getcontact.com/phone/{phone_clean}",
    ]
    info("GetContact sering membatasi lookup nomor telepon publik karena privasi")
    status, url, code = domain_url_ok(urls)
    if status:
        ok("GetContact URL valid dan dapat dibuka")
        dato("Nomor", fmt_e164)
        dato("URL", url)
    else:
        warn("GetContact tidak membuka hasil atau mengembalikan 404")
        for u in urls:
            print(f"    {D}• {u}{RS}")
    print()
    info("Alternatif tools untuk reverse phone lookup:")
    print(f"    {D}• TrueCaller: https://www.truecaller.com/search/{urllib.parse.quote(phone_clean)}{RS}")
    print(f"    {D}• WhitePages: https://www.whitepages.com/phone/{phone_clean}{RS}")
    print(f"    {D}• Reverse Phone Lookup: https://www.reversephonelookup.com/phone/{phone_clean}{RS}")


def modulo_truecaller(fmt_e164):
    sep("TRUECALLER — Reverse lookup")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://www.truecaller.com/search/{urllib.parse.quote(phone_clean)}",
        f"https://www.truecaller.com/search/{urllib.parse.quote(fmt_e164)}",
    ]
    ok, url, status = domain_url_ok(urls)
    if ok:
        ok("TrueCaller URL valid")
        dato("Nomor", fmt_e164)
        dato("URL", url)
        info("TrueCaller sering membatasi hasil publik, tapi URL pencarian tetap valid")
    else:
        warn("Tidak dapat membuka TrueCaller dari terminal")
        for u in urls:
            print(f"    {D}• {u}{RS}")


def modulo_whitepages(fmt_e164):
    sep("WHITEPAGES — Reverse lookup")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://www.whitepages.com/phone/{phone_clean}",
        f"https://www.whitepages.com/phone/{urllib.parse.quote(fmt_e164)}",
    ]
    ok, url, status = domain_url_ok(urls)
    if ok:
        ok("WhitePages URL valid")
        dato("Nomor", fmt_e164)
        dato("URL", url)
    else:
        warn("WhitePages tidak dapat diakses dari terminal")
        for u in urls:
            print(f"    {D}• {u}{RS}")


def modulo_reverse_phone_lookup(fmt_e164):
    sep("REVERSE PHONE LOOKUP — Search")
    phone_clean = fmt_e164.replace("+", "").replace(" ", "").replace("-", "")
    urls = [
        f"https://www.reversephonelookup.com/phone/{phone_clean}",
        f"https://www.reversephonelookup.com/search?number={urllib.parse.quote(phone_clean)}",
    ]
    ok, url, status = domain_url_ok(urls)
    if ok:
        ok("Reverse Phone Lookup URL valid")
        dato("Nomor", fmt_e164)
        dato("URL", url)
    else:
        warn("Reverse Phone Lookup tidak dapat diakses dari terminal")
        for u in urls:
            print(f"    {D}• {u}{RS}")


def modulo_social_all(fmt_e164):
    sep("SEMUA MODUL SOSIAL")
    info("Menjalankan pencarian secara bertahap untuk semua platform sosial dan reverse lookup")
    modulo_twitter(fmt_e164)
    modulo_facebook(fmt_e164)
    modulo_tiktok(fmt_e164)
    modulo_instagram(fmt_e164)
    modulo_linkedin(fmt_e164)
    modulo_getcontact(fmt_e164)
    modulo_truecaller(fmt_e164)
    modulo_whitepages(fmt_e164)
    modulo_reverse_phone_lookup(fmt_e164)


# ---------- summary ----------
def modulo_resumen(phone_raw, fmt_e164, fmt_intl, region, parsed):
    sep("RINGKASAN INTELIGENSI")
    print(f"\n  {C}{B}Target:{RS}        {W}{B}{phone_raw}{RS}")
    print(f"  {C}{B}E164:{RS}          {W}{fmt_e164}{RS}")
    print(f"  {C}{B}Internasional:{RS} {W}{fmt_intl}{RS}")
    print(f"  {C}{B}Negara:{RS}          {W}{COUNTRY_NAMES.get(region, region) if region else '—'}{RS}")

    if parsed:
        op = carrier.name_for_number(parsed, "id")
        tipo = phonenumbers.number_type(parsed)
        print(f"  {C}{B}Operator:{RS}     {W}{op if op else 'Lihat modul Veriphone'}{RS}")
        print(f"  {C}{B}Tipe line:{RS}    {W}{TIPOS_LINEA.get(tipo, 'Tidak diketahui')}{RS}")

    print(f"\n  {D}Analisis selesai — Ciberbrigada OSINT Suite v2.0{RS}\n")


# ---------- main ----------
def main():
    banner()
    print(f"  {W}Masukkan nomor dengan kode negara:{RS}")
    print(f"  {D}Contoh: +62 812 3456-7890 | +1 555 123 4567 | +34 612 345 678{RS}\n")

    while True:
        try:
            phone_raw = input(f"  {C}▸ Nomor:{RS} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n  {Y}Keluar... Sampai jumpa.{RS}\n")
            sys.exit(0)

        if phone_raw.lower() in ("keluar", "exit", "quit", "q"):
            print(f"\n  {Y}Keluar... Sampai jumpa.{RS}\n")
            sys.exit(0)

        if not phone_raw:
            warn("Masukkan nomor telepon")
            continue

        fmt_e164, fmt_intl, parsed, region = modulo_analisis(phone_raw)
        if not fmt_e164:
            continue

        sep("PILIH MODUL")
        modulos = [
            ("2", "Veriphone        — Operator, tipe & negara (API gratis)"),
            ("3", "NumVerify        — Validasi & operator"),
            ("4", "DNS / ENUM       — Protokol E.164 & infrastruktur"),
            ("5", "WhatsApp         — Apakah punya akun aktif?"),
            ("6", "Telegram         — Apakah punya akun aktif?"),
            ("7", "Gravatar         — Profil terkait nomor"),
            ("8", "Twitter/X        — Pencarian & verifikasi"),
            ("9", "Facebook         — Pencarian profil"),
            ("10", "TikTok          — Pencarian & verifikasi"),
            ("11", "Instagram       — Pencarian pengguna"),
            ("12", "LinkedIn        — Pencarian profil profesional"),
            ("13", "GetContact      — Database kontak global"),
            ("14", "TrueCaller      — Reverse lookup"),
            ("15", "WhitePages      — Reverse phone lookup"),
            ("16", "ReverseLookup   — Search by phone"),
            ("0", "SEMUA MODUL"),
        ]
        for num, desc in modulos:
            color = C if num != "0" else Y
            print(f"  {color}[{num}]{RS} {W}{desc}{RS}")

        print()
        try:
            sel = input(f"  {C}▸ Pilihan (contoh: 0 atau 2,5,6,8,13,14):{RS} ").strip()
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)

        selected = ["2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"] if sel == "0" else [s.strip() for s in sel.split(",")]
        print()

        if "2" in selected: modulo_veriphone(fmt_e164)
        if "3" in selected: modulo_numverify(fmt_e164, region)
        if "4" in selected: modulo_dns(fmt_e164, region)
        if "5" in selected: modulo_whatsapp(fmt_e164)
        if "6" in selected: modulo_telegram(fmt_e164)
        if "7" in selected: modulo_gravatar(fmt_e164)
        if "8" in selected: modulo_twitter(fmt_e164)
        if "9" in selected: modulo_facebook(fmt_e164)
        if "10" in selected: modulo_tiktok(fmt_e164)
        if "11" in selected: modulo_instagram(fmt_e164)
        if "12" in selected: modulo_linkedin(fmt_e164)
        if "13" in selected: modulo_getcontact(fmt_e164)
        if "14" in selected: modulo_truecaller(fmt_e164)
        if "15" in selected: modulo_whitepages(fmt_e164)
        if "16" in selected: modulo_reverse_phone_lookup(fmt_e164)

        modulo_resumen(phone_raw, fmt_e164, fmt_intl, region, parsed)

        sep()
        print(f"\n  {D}Analisis nomor lain? (Enter / 'keluar'){RS}")
        try:
            again = input(f"  {C}▸{RS} ").strip().lower()
            if again in ("keluar", "exit", "quit", "q"):
                print(f"\n  {Y}Keluar... Sampai jumpa.{RS}\n")
                sys.exit(0)
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)

        banner()


if __name__ == "__main__":
    main()
