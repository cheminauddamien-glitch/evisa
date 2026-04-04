#!/usr/bin/env python
"""
enrich_visa_pages.py
--------------------
Enriches ALL visa-{country}.html pages in www/en/ by:
  1. Injecting a colour-coded alert block right after the <h1> title
  2. Adding Capital / Currency / Main Airports rows to the Key Facts table

Idempotent: safe to run multiple times without duplicating content.
"""

import os, re, glob

# ── directory setup ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(BASE_DIR, "www", "en")

# ── files to skip (not country pages) ────────────────────────────────────────
SKIP_FILES = {
    "visa-uk.html",              # redirect to visa-united-kingdom.html
    "visa-documents-checklist.html",
    "visa-photo-requirements.html",
    "visa-processing-times.html",
    "visa-rejection-reasons.html",
}
SKIP_PREFIXES = ("visa-free-countries-",)

# ── alert type configuration ────────────────────────────────────────────────
ALERT_CONFIG = {
    "evisa_mandatory": {
        "bg": "#fff3e0", "border": "#ff9800",
        "emoji": "\u26a0\ufe0f",
        "title_prefix": "eVisa Required",
        "link_color": "#e65100",
    },
    "evisa_available": {
        "bg": "#e3f2fd", "border": "#2196f3",
        "emoji": "\u2139\ufe0f",
        "title_prefix": "eVisa Available",
        "link_color": "#0d47a1",
    },
    "visa_free": {
        "bg": "#e8f5e9", "border": "#4caf50",
        "emoji": "\u2705",
        "title_prefix": "Visa-Free Entry",
        "link_color": "#1b5e20",
    },
    "embassy_required": {
        "bg": "#fce4ec", "border": "#f44336",
        "emoji": "\U0001f534",
        "title_prefix": "Visa Required",
        "link_color": "#b71c1c",
    },
    "eta_required": {
        "bg": "#fff3e0", "border": "#ff9800",
        "emoji": "\u26a0\ufe0f",
        "title_prefix": "Electronic Travel Authorization Required",
        "link_color": "#e65100",
    },
    "esta_required": {
        "bg": "#fff3e0", "border": "#ff9800",
        "emoji": "\u26a0\ufe0f",
        "title_prefix": "ESTA Required for VWP Countries",
        "link_color": "#e65100",
    },
}

# ── country data ─────────────────────────────────────────────────────────────
COUNTRIES = {
    "andorra": {
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "currency": "Euro (EUR)",
        "airports": "No airport (nearest: BCN Barcelona, TLS Toulouse)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Andorra without a visa. Andorra is not in the EU or Schengen Area but has no border controls; access is via France or Spain.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "angola": {
        "name": "Angola",
        "capital": "Luanda",
        "currency": "Angolan Kwanza (AOA)",
        "airports": "LAD (Luanda)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Angola requires a visa for most nationalities. An eVisa or pre-arrival visa can be obtained online for eligible travelers.",
        "evisa_url": "https://www.smevisa.gov.ao",
        "evisa_name": "Angola eVisa",
    },
    "argentina": {
        "name": "Argentina",
        "capital": "Buenos Aires",
        "currency": "Argentine Peso (ARS)",
        "airports": "EZE (Buenos Aires Ezeiza), AEP (Buenos Aires Aeroparque)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Argentina visa-free for up to 90 days. Some nationalities must pay a reciprocity fee online before travel.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "australia": {
        "name": "Australia",
        "capital": "Canberra",
        "currency": "Australian Dollar (AUD)",
        "airports": "SYD (Sydney), MEL (Melbourne), BNE (Brisbane), PER (Perth)",
        "alert_type": "eta_required",
        "alert_text": "Most visitors need an Electronic Travel Authority (ETA) or visa before arrival. ETA is available for eligible passport holders.",
        "evisa_url": "https://www.eta.homeaffairs.gov.au",
        "evisa_name": "Australia ETA",
    },
    "austria": {
        "name": "Austria",
        "capital": "Vienna",
        "currency": "Euro (EUR)",
        "airports": "VIE (Vienna Schwechat)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Austria allows visa-free entry for many nationalities for up to 90 days in any 180-day period. ETIAS will be required for visa-exempt nationals from 2025-2026.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "bahamas": {
        "name": "Bahamas",
        "capital": "Nassau",
        "currency": "Bahamian Dollar (BSD)",
        "airports": "NAS (Nassau), FPO (Freeport)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter the Bahamas visa-free for up to 90 days.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "bahrain": {
        "name": "Bahrain",
        "capital": "Manama",
        "currency": "Bahraini Dinar (BHD)",
        "airports": "BAH (Bahrain International)",
        "alert_type": "evisa_available",
        "alert_text": "Bahrain offers eVisa and visa-on-arrival for many nationalities. GCC citizens enter freely. Others may apply online.",
        "evisa_url": "https://www.evisa.gov.bh",
        "evisa_name": "Bahrain eVisa",
    },
    "belgium": {
        "name": "Belgium",
        "capital": "Brussels",
        "currency": "Euro (EUR)",
        "airports": "BRU (Brussels), CRL (Brussels-Charleroi)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Belgium allows visa-free entry for many nationalities for up to 90 days in any 180-day period. ETIAS will be required for visa-exempt nationals from 2025-2026.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "belize": {
        "name": "Belize",
        "capital": "Belmopan",
        "currency": "Belize Dollar (BZD)",
        "airports": "BZE (Philip S. W. Goldson International)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Belize visa-free for up to 30 days.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "bermuda": {
        "name": "Bermuda",
        "capital": "Hamilton",
        "currency": "Bermudian Dollar (BMD)",
        "airports": "BDA (L.F. Wade International)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Bermuda visa-free for up to 90 days. Bermuda is a British Overseas Territory.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "bhutan": {
        "name": "Bhutan",
        "capital": "Thimphu",
        "currency": "Bhutanese Ngultrum (BTN)",
        "airports": "PBH (Paro International)",
        "alert_type": "evisa_mandatory",
        "alert_text": "All visitors (except Indian, Bangladeshi, and Maldivian citizens) must obtain a visa through a licensed tour operator or apply online. A Sustainable Development Fee applies.",
        "evisa_url": "https://www.bhutan.travel",
        "evisa_name": "Bhutan Visa",
    },
    "brazil": {
        "name": "Brazil",
        "capital": "Brasilia",
        "currency": "Brazilian Real (BRL)",
        "airports": "GRU (Sao Paulo Guarulhos), GIG (Rio de Janeiro Galeao), BSB (Brasilia)",
        "alert_type": "evisa_available",
        "alert_text": "Brazil offers visa-free entry for many nationalities (up to 90 days). US, Canada, Australia, and Japan citizens need an eVisa.",
        "evisa_url": "https://www.gov.br/mre/pt-br/assuntos/portal-consular/vistos/e-visa",
        "evisa_name": "Brazil eVisa",
    },
    "brunei": {
        "name": "Brunei",
        "capital": "Bandar Seri Begawan",
        "currency": "Brunei Dollar (BND)",
        "airports": "BWN (Brunei International)",
        "alert_type": "visa_free",
        "alert_text": "Many nationalities can enter Brunei visa-free for 14-90 days depending on nationality.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "bulgaria": {
        "name": "Bulgaria",
        "capital": "Sofia",
        "currency": "Bulgarian Lev (BGN)",
        "airports": "SOF (Sofia), BOJ (Burgas), VAR (Varna)",
        "alert_type": "visa_free",
        "alert_text": "Bulgaria is an EU member joining the Schengen Area. Many nationalities can enter visa-free for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "cambodia": {
        "name": "Cambodia",
        "capital": "Phnom Penh",
        "currency": "Cambodian Riel (KHR) / US Dollar (USD)",
        "airports": "PNH (Phnom Penh), REP (Siem Reap), SHV (Sihanoukville)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Most visitors need a visa for Cambodia. An eVisa is available online for tourism (30 days, single entry). Visa on arrival is also available at major ports.",
        "evisa_url": "https://www.evisa.gov.kh",
        "evisa_name": "Cambodia eVisa",
    },
    "canada": {
        "name": "Canada",
        "capital": "Ottawa",
        "currency": "Canadian Dollar (CAD)",
        "airports": "YYZ (Toronto Pearson), YVR (Vancouver), YUL (Montreal), YOW (Ottawa)",
        "alert_type": "eta_required",
        "alert_text": "Visa-exempt travelers (except US citizens) must obtain an Electronic Travel Authorization (eTA) before flying to Canada. Other nationalities need a visitor visa.",
        "evisa_url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/eta.html",
        "evisa_name": "Canada eTA",
    },
    "cape-verde": {
        "name": "Cape Verde",
        "capital": "Praia",
        "currency": "Cape Verdean Escudo (CVE)",
        "airports": "SID (Sal), RAI (Praia)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Most visitors need a visa for Cape Verde. An eVisa can be obtained online before travel.",
        "evisa_url": "https://www.ease.gov.cv",
        "evisa_name": "Cape Verde eVisa",
    },
    "chile": {
        "name": "Chile",
        "capital": "Santiago",
        "currency": "Chilean Peso (CLP)",
        "airports": "SCL (Santiago Arturo Merino Benitez)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Chile visa-free for up to 90 days.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "china": {
        "name": "China",
        "capital": "Beijing",
        "currency": "Chinese Yuan Renminbi (CNY)",
        "airports": "PEK (Beijing Capital), PKX (Beijing Daxing), PVG (Shanghai Pudong), CAN (Guangzhou)",
        "alert_type": "embassy_required",
        "alert_text": "Most nationalities require a visa from the nearest Chinese embassy or consulate before travel. Transit visa-free options (72/144 hours) are available at select cities. China has expanded visa-free access for some nationalities.",
        "evisa_url": "https://www.visaforchina.cn",
        "evisa_name": "China Visa Application",
    },
    "colombia": {
        "name": "Colombia",
        "capital": "Bogota",
        "currency": "Colombian Peso (COP)",
        "airports": "BOG (Bogota El Dorado), MDE (Medellin), CTG (Cartagena)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Colombia visa-free for up to 90 days (extendable to 180 days per year).",
        "evisa_url": "",
        "evisa_name": "",
    },
    "cook-islands": {
        "name": "Cook Islands",
        "capital": "Avarua",
        "currency": "New Zealand Dollar (NZD)",
        "airports": "RAR (Rarotonga International)",
        "alert_type": "visa_free",
        "alert_text": "All nationalities can visit the Cook Islands visa-free for up to 31 days.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "costa-rica": {
        "name": "Costa Rica",
        "capital": "San Jose",
        "currency": "Costa Rican Colon (CRC)",
        "airports": "SJO (San Jose Juan Santamaria), LIR (Liberia)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Costa Rica visa-free for up to 90 days.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "croatia": {
        "name": "Croatia",
        "capital": "Zagreb",
        "currency": "Euro (EUR)",
        "airports": "ZAG (Zagreb), DBV (Dubrovnik), SPU (Split)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Croatia allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "cyprus": {
        "name": "Cyprus",
        "capital": "Nicosia",
        "currency": "Euro (EUR)",
        "airports": "LCA (Larnaca), PFO (Paphos)",
        "alert_type": "visa_free",
        "alert_text": "Cyprus is an EU member. Many nationalities can enter visa-free for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "czech-republic": {
        "name": "Czech Republic",
        "capital": "Prague",
        "currency": "Czech Koruna (CZK)",
        "airports": "PRG (Prague Vaclav Havel)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, the Czech Republic allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "denmark": {
        "name": "Denmark",
        "capital": "Copenhagen",
        "currency": "Danish Krone (DKK)",
        "airports": "CPH (Copenhagen Kastrup), BLL (Billund)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Denmark allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "ecuador": {
        "name": "Ecuador",
        "capital": "Quito",
        "currency": "US Dollar (USD)",
        "airports": "UIO (Quito Mariscal Sucre), GYE (Guayaquil)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Ecuador visa-free for up to 90 days.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "egypt": {
        "name": "Egypt",
        "capital": "Cairo",
        "currency": "Egyptian Pound (EGP)",
        "airports": "CAI (Cairo), HRG (Hurghada), SSH (Sharm El Sheikh), LXR (Luxor)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Most visitors need a visa for Egypt. An eVisa is available online for eligible nationalities. Visa on arrival is also available for some passport holders.",
        "evisa_url": "https://www.visa2egypt.gov.eg",
        "evisa_name": "Egypt eVisa",
    },
    "fiji": {
        "name": "Fiji",
        "capital": "Suva",
        "currency": "Fijian Dollar (FJD)",
        "airports": "NAN (Nadi International), SUV (Suva Nausori)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Fiji visa-free for up to 4 months. A visa extension can be obtained locally.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "finland": {
        "name": "Finland",
        "capital": "Helsinki",
        "currency": "Euro (EUR)",
        "airports": "HEL (Helsinki-Vantaa)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Finland allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "france": {
        "name": "France",
        "capital": "Paris",
        "currency": "Euro (EUR)",
        "airports": "CDG (Paris Charles de Gaulle), ORY (Paris Orly), LYS (Lyon), NCE (Nice)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, France allows visa-free entry for many nationalities for up to 90 days in any 180-day period. ETIAS will be required for visa-exempt nationals from 2025-2026.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "georgia": {
        "name": "Georgia",
        "capital": "Tbilisi",
        "currency": "Georgian Lari (GEL)",
        "airports": "TBS (Tbilisi), KUT (Kutaisi), BUS (Batumi)",
        "alert_type": "visa_free",
        "alert_text": "Citizens of 95+ countries can enter Georgia visa-free for up to 1 year. An eVisa is available for nationalities not on the visa-free list.",
        "evisa_url": "https://www.evisa.gov.ge",
        "evisa_name": "Georgia eVisa",
    },
    "germany": {
        "name": "Germany",
        "capital": "Berlin",
        "currency": "Euro (EUR)",
        "airports": "FRA (Frankfurt), MUC (Munich), BER (Berlin Brandenburg), DUS (Dusseldorf)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Germany allows visa-free entry for many nationalities for up to 90 days in any 180-day period. ETIAS will be required for visa-exempt nationals from 2025-2026.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "greece": {
        "name": "Greece",
        "capital": "Athens",
        "currency": "Euro (EUR)",
        "airports": "ATH (Athens), SKG (Thessaloniki), HER (Heraklion), RHO (Rhodes)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Greece allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "guatemala": {
        "name": "Guatemala",
        "capital": "Guatemala City",
        "currency": "Guatemalan Quetzal (GTQ)",
        "airports": "GUA (La Aurora International)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Guatemala visa-free for up to 90 days (part of the CA-4 agreement with Honduras, El Salvador, and Nicaragua).",
        "evisa_url": "",
        "evisa_name": "",
    },
    "hong-kong": {
        "name": "Hong Kong",
        "capital": "Hong Kong (SAR)",
        "currency": "Hong Kong Dollar (HKD)",
        "airports": "HKG (Hong Kong International)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Hong Kong visa-free for 7 to 180 days depending on nationality.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "hungary": {
        "name": "Hungary",
        "capital": "Budapest",
        "currency": "Hungarian Forint (HUF)",
        "airports": "BUD (Budapest Ferenc Liszt)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Hungary allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "iceland": {
        "name": "Iceland",
        "capital": "Reykjavik",
        "currency": "Icelandic Krona (ISK)",
        "airports": "KEF (Keflavik International)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Iceland allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "india": {
        "name": "India",
        "capital": "New Delhi",
        "currency": "Indian Rupee (INR)",
        "airports": "DEL (Delhi Indira Gandhi), BOM (Mumbai), BLR (Bengaluru), MAA (Chennai), CCU (Kolkata)",
        "alert_type": "evisa_mandatory",
        "alert_text": "An eVisa (e-Tourist, e-Business, e-Medical) is required for most nationalities. Apply online before travel. Some nationalities need a regular visa from the embassy.",
        "evisa_url": "https://indianvisaonline.gov.in",
        "evisa_name": "India eVisa",
    },
    "indonesia": {
        "name": "Indonesia",
        "capital": "Jakarta",
        "currency": "Indonesian Rupiah (IDR)",
        "airports": "CGK (Jakarta Soekarno-Hatta), DPS (Bali Ngurah Rai), SUB (Surabaya), JOG (Yogyakarta)",
        "alert_type": "evisa_available",
        "alert_text": "Indonesia offers visa-free entry for some nationalities (30 days, not extendable). Others can obtain a Visa on Arrival (30 days, extendable). An eVisa is also available.",
        "evisa_url": "https://molina.imigrasi.go.id",
        "evisa_name": "Indonesia eVisa (Molina)",
    },
    "iran": {
        "name": "Iran",
        "capital": "Tehran",
        "currency": "Iranian Rial (IRR)",
        "airports": "IKA (Tehran Imam Khomeini), THR (Tehran Mehrabad), SYZ (Shiraz), ISF (Isfahan)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Most visitors require a visa for Iran. An eVisa can be applied for online. Some nationalities may also obtain a visa on arrival at major airports.",
        "evisa_url": "https://e_visa.mfa.ir",
        "evisa_name": "Iran eVisa",
    },
    "iraq": {
        "name": "Iraq",
        "capital": "Baghdad",
        "currency": "Iraqi Dinar (IQD)",
        "airports": "BGW (Baghdad), EBL (Erbil), BSR (Basra)",
        "alert_type": "embassy_required",
        "alert_text": "Most nationalities require a visa obtained from an Iraqi embassy before travel. Visa on arrival may be available at Erbil and Sulaymaniyah airports for some nationalities visiting the Kurdistan Region.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "ireland": {
        "name": "Ireland",
        "capital": "Dublin",
        "currency": "Euro (EUR)",
        "airports": "DUB (Dublin), ORK (Cork), SNN (Shannon)",
        "alert_type": "visa_free",
        "alert_text": "Many nationalities can enter Ireland visa-free for up to 90 days. Ireland is not part of the Schengen Area but has its own visa-free arrangements.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "israel": {
        "name": "Israel",
        "capital": "Jerusalem (disputed) / Tel Aviv (diplomatic)",
        "currency": "Israeli New Shekel (ILS)",
        "airports": "TLV (Ben Gurion, Tel Aviv), VDA (Ramon, Eilat)",
        "alert_type": "evisa_available",
        "alert_text": "Many nationalities can enter Israel visa-free for up to 90 days. An ETA-IL electronic authorization is being introduced for some travelers.",
        "evisa_url": "https://www.gov.il/en/departments/general/visa-to-israel",
        "evisa_name": "Israel Visa Information",
    },
    "italy": {
        "name": "Italy",
        "capital": "Rome",
        "currency": "Euro (EUR)",
        "airports": "FCO (Rome Fiumicino), MXP (Milan Malpensa), VCE (Venice), NAP (Naples)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Italy allows visa-free entry for many nationalities for up to 90 days in any 180-day period. ETIAS will be required for visa-exempt nationals from 2025-2026.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "japan": {
        "name": "Japan",
        "capital": "Tokyo",
        "currency": "Japanese Yen (JPY)",
        "airports": "NRT (Tokyo Narita), HND (Tokyo Haneda), KIX (Osaka Kansai), NGO (Nagoya Chubu)",
        "alert_type": "visa_free",
        "alert_text": "Citizens of 71 countries can enter Japan visa-free for 15-90 days depending on nationality. Japan introduced Visit Japan Web for pre-registration.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "jordan": {
        "name": "Jordan",
        "capital": "Amman",
        "currency": "Jordanian Dinar (JOD)",
        "airports": "AMM (Queen Alia International), AQJ (Aqaba King Hussein)",
        "alert_type": "evisa_available",
        "alert_text": "Jordan offers visa on arrival for many nationalities (single entry, 40 JOD). The Jordan Pass includes visa fee waiver and access to attractions.",
        "evisa_url": "https://www.jordanpass.jo",
        "evisa_name": "Jordan Pass / eVisa",
    },
    "kuwait": {
        "name": "Kuwait",
        "capital": "Kuwait City",
        "currency": "Kuwaiti Dinar (KWD)",
        "airports": "KWI (Kuwait International)",
        "alert_type": "evisa_available",
        "alert_text": "Kuwait offers eVisa for eligible nationalities. GCC citizens enter freely. Others may need a visa sponsored by a Kuwaiti resident.",
        "evisa_url": "https://evisa.moi.gov.kw",
        "evisa_name": "Kuwait eVisa",
    },
    "laos": {
        "name": "Laos",
        "capital": "Vientiane",
        "currency": "Lao Kip (LAK)",
        "airports": "VTE (Vientiane Wattay), LPQ (Luang Prabang)",
        "alert_type": "evisa_available",
        "alert_text": "Laos offers visa on arrival at major border crossings for most nationalities (30 days, ~USD 30-42). An eVisa is also available.",
        "evisa_url": "https://laoevisa.gov.la",
        "evisa_name": "Laos eVisa",
    },
    "liechtenstein": {
        "name": "Liechtenstein",
        "capital": "Vaduz",
        "currency": "Swiss Franc (CHF)",
        "airports": "No airport (nearest: ZRH Zurich, FDH Friedrichshafen)",
        "alert_type": "visa_free",
        "alert_text": "As part of the Schengen Area (via Switzerland), Liechtenstein allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "luxembourg": {
        "name": "Luxembourg",
        "capital": "Luxembourg City",
        "currency": "Euro (EUR)",
        "airports": "LUX (Luxembourg Findel)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Luxembourg allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "macau": {
        "name": "Macau",
        "capital": "Macau (SAR)",
        "currency": "Macanese Pataca (MOP)",
        "airports": "MFM (Macau International)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Macau visa-free for 30-90 days depending on nationality.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "malaysia": {
        "name": "Malaysia",
        "capital": "Kuala Lumpur",
        "currency": "Malaysian Ringgit (MYR)",
        "airports": "KUL (Kuala Lumpur KLIA), PEN (Penang), BKI (Kota Kinabalu), KCH (Kuching)",
        "alert_type": "evisa_available",
        "alert_text": "Many nationalities can enter Malaysia visa-free for 14-90 days. For those requiring a visa, an eVisa or eNTRI can be obtained online.",
        "evisa_url": "https://www.windowmalaysia.my",
        "evisa_name": "Malaysia eVisa",
    },
    "maldives": {
        "name": "Maldives",
        "capital": "Male",
        "currency": "Maldivian Rufiyaa (MVR)",
        "airports": "MLE (Velana International, Male)",
        "alert_type": "visa_free",
        "alert_text": "All nationalities receive a free 30-day visa on arrival in the Maldives. An online Traveller Declaration must be completed before travel.",
        "evisa_url": "https://imuga.immigration.gov.mv",
        "evisa_name": "Maldives IMUGA Declaration",
    },
    "mexico": {
        "name": "Mexico",
        "capital": "Mexico City",
        "currency": "Mexican Peso (MXN)",
        "airports": "MEX (Mexico City), CUN (Cancun), GDL (Guadalajara), SJD (San Jose del Cabo)",
        "alert_type": "visa_free",
        "alert_text": "Many nationalities can enter Mexico visa-free for up to 180 days. An SAE electronic authorization is available for some nationalities.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "moldova": {
        "name": "Moldova",
        "capital": "Chisinau",
        "currency": "Moldovan Leu (MDL)",
        "airports": "KIV (Chisinau International)",
        "alert_type": "visa_free",
        "alert_text": "Citizens of many countries can enter Moldova visa-free for up to 90 days in any 180-day period. An eVisa is available for nationalities not on the visa-free list.",
        "evisa_url": "https://www.evisa.gov.md",
        "evisa_name": "Moldova eVisa",
    },
    "myanmar": {
        "name": "Myanmar",
        "capital": "Naypyidaw",
        "currency": "Myanmar Kyat (MMK)",
        "airports": "RGN (Yangon), MDL (Mandalay), NYT (Naypyidaw)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Most visitors require a visa for Myanmar. An eVisa is available for tourism and business (28 days).",
        "evisa_url": "https://evisa.moip.gov.mm",
        "evisa_name": "Myanmar eVisa",
    },
    "nepal": {
        "name": "Nepal",
        "capital": "Kathmandu",
        "currency": "Nepalese Rupee (NPR)",
        "airports": "KTM (Tribhuvan International, Kathmandu)",
        "alert_type": "evisa_available",
        "alert_text": "Most nationalities can obtain a visa on arrival at Kathmandu airport. An online visa application can be pre-filled before arrival to speed up the process.",
        "evisa_url": "https://nepaliport.immigration.gov.np",
        "evisa_name": "Nepal Online Visa",
    },
    "netherlands": {
        "name": "Netherlands",
        "capital": "Amsterdam",
        "currency": "Euro (EUR)",
        "airports": "AMS (Amsterdam Schiphol), EIN (Eindhoven), RTM (Rotterdam The Hague)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, the Netherlands allows visa-free entry for many nationalities for up to 90 days in any 180-day period. ETIAS will be required for visa-exempt nationals from 2025-2026.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "new-zealand": {
        "name": "New Zealand",
        "capital": "Wellington",
        "currency": "New Zealand Dollar (NZD)",
        "airports": "AKL (Auckland), WLG (Wellington), CHC (Christchurch), ZQN (Queenstown)",
        "alert_type": "eta_required",
        "alert_text": "Most visitors need a New Zealand Electronic Travel Authority (NZeTA) before travel. Some nationalities require a visitor visa from the embassy.",
        "evisa_url": "https://www.immigration.govt.nz/new-zealand-visas/visas/visa/nzeta",
        "evisa_name": "NZeTA",
    },
    "nicaragua": {
        "name": "Nicaragua",
        "capital": "Managua",
        "currency": "Nicaraguan Cordoba (NIO)",
        "airports": "MGA (Managua Augusto Cesar Sandino)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Nicaragua visa-free for up to 90 days (part of the CA-4 agreement).",
        "evisa_url": "",
        "evisa_name": "",
    },
    "norway": {
        "name": "Norway",
        "capital": "Oslo",
        "currency": "Norwegian Krone (NOK)",
        "airports": "OSL (Oslo Gardermoen), BGO (Bergen), TRD (Trondheim)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Norway allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "oman": {
        "name": "Oman",
        "capital": "Muscat",
        "currency": "Omani Rial (OMR)",
        "airports": "MCT (Muscat International), SLL (Salalah)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Most visitors require a visa for Oman. An eVisa can be obtained online. GCC citizens enter freely.",
        "evisa_url": "https://evisa.rop.gov.om",
        "evisa_name": "Oman eVisa",
    },
    "panama": {
        "name": "Panama",
        "capital": "Panama City",
        "currency": "Panamanian Balboa (PAB) / US Dollar (USD)",
        "airports": "PTY (Tocumen International, Panama City)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Panama visa-free for up to 90-180 days depending on nationality.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "peru": {
        "name": "Peru",
        "capital": "Lima",
        "currency": "Peruvian Sol (PEN)",
        "airports": "LIM (Lima Jorge Chavez), CUZ (Cusco)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Peru visa-free for up to 90-183 days.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "philippines": {
        "name": "Philippines",
        "capital": "Manila",
        "currency": "Philippine Peso (PHP)",
        "airports": "MNL (Manila Ninoy Aquino), CEB (Cebu-Mactan), CRK (Clark)",
        "alert_type": "visa_free",
        "alert_text": "Many nationalities can enter the Philippines visa-free for 30 days (extendable). An eTravel registration is required before arrival.",
        "evisa_url": "https://etravel.gov.ph",
        "evisa_name": "Philippines eTravel",
    },
    "poland": {
        "name": "Poland",
        "capital": "Warsaw",
        "currency": "Polish Zloty (PLN)",
        "airports": "WAW (Warsaw Chopin), KRK (Krakow), GDN (Gdansk), WRO (Wroclaw)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Poland allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "portugal": {
        "name": "Portugal",
        "capital": "Lisbon",
        "currency": "Euro (EUR)",
        "airports": "LIS (Lisbon), OPO (Porto), FAO (Faro)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Portugal allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "qatar": {
        "name": "Qatar",
        "capital": "Doha",
        "currency": "Qatari Riyal (QAR)",
        "airports": "DOH (Hamad International)",
        "alert_type": "evisa_available",
        "alert_text": "Qatar offers visa-free entry for 95+ nationalities. Others can obtain a visa on arrival or eVisa.",
        "evisa_url": "https://www.visitqatar.com/intl-en/visa",
        "evisa_name": "Qatar Visa Portal",
    },
    "romania": {
        "name": "Romania",
        "capital": "Bucharest",
        "currency": "Romanian Leu (RON)",
        "airports": "OTP (Bucharest Henri Coanda), CLJ (Cluj-Napoca), TGM (Tirgu Mures)",
        "alert_type": "visa_free",
        "alert_text": "Romania is an EU member joining the Schengen Area. Many nationalities can enter visa-free for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "samoa": {
        "name": "Samoa",
        "capital": "Apia",
        "currency": "Samoan Tala (WST)",
        "airports": "APW (Faleolo International)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Samoa visa-free for up to 60 days. An Entry Permit is issued on arrival.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "saudi-arabia": {
        "name": "Saudi Arabia",
        "capital": "Riyadh",
        "currency": "Saudi Riyal (SAR)",
        "airports": "RUH (Riyadh King Khalid), JED (Jeddah King Abdulaziz), DMM (Dammam)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Saudi Arabia requires a visa for most visitors. An eVisa for tourism is available for 49+ nationalities. Umrah and Hajj pilgrims have separate visa procedures.",
        "evisa_url": "https://visa.visitsaudi.com",
        "evisa_name": "Saudi Arabia eVisa",
    },
    "singapore": {
        "name": "Singapore",
        "capital": "Singapore",
        "currency": "Singapore Dollar (SGD)",
        "airports": "SIN (Changi International)",
        "alert_type": "evisa_available",
        "alert_text": "Most nationalities can enter Singapore visa-free for 30-90 days. Singapore requires all travelers to complete an SG Arrival Card online before arrival.",
        "evisa_url": "https://eservices.ica.gov.sg/sgarrivalcard",
        "evisa_name": "SG Arrival Card",
    },
    "slovakia": {
        "name": "Slovakia",
        "capital": "Bratislava",
        "currency": "Euro (EUR)",
        "airports": "BTS (Bratislava M. R. Stefanik)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Slovakia allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "slovenia": {
        "name": "Slovenia",
        "capital": "Ljubljana",
        "currency": "Euro (EUR)",
        "airports": "LJU (Ljubljana Joze Pucnik)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Slovenia allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "south-korea": {
        "name": "South Korea",
        "capital": "Seoul",
        "currency": "South Korean Won (KRW)",
        "airports": "ICN (Seoul Incheon), GMP (Seoul Gimpo), PUS (Busan Gimhae), CJU (Jeju)",
        "alert_type": "visa_free",
        "alert_text": "Citizens of 112 countries can enter South Korea visa-free for 30-90 days. The K-ETA requirement is currently suspended for most visa-free nationalities.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "spain": {
        "name": "Spain",
        "capital": "Madrid",
        "currency": "Euro (EUR)",
        "airports": "MAD (Madrid Barajas), BCN (Barcelona El Prat), AGP (Malaga), PMI (Palma de Mallorca)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Spain allows visa-free entry for many nationalities for up to 90 days in any 180-day period. ETIAS will be required for visa-exempt nationals from 2025-2026.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "sri-lanka": {
        "name": "Sri Lanka",
        "capital": "Sri Jayawardenepura Kotte (legislative) / Colombo (commercial)",
        "currency": "Sri Lankan Rupee (LKR)",
        "airports": "CMB (Colombo Bandaranaike), HRI (Mattala Rajapaksa)",
        "alert_type": "eta_required",
        "alert_text": "All visitors (except certain exemptions) must obtain an Electronic Travel Authorization (ETA) before arrival. Apply online.",
        "evisa_url": "https://www.srilankaevisa.lk",
        "evisa_name": "Sri Lanka ETA",
    },
    "sweden": {
        "name": "Sweden",
        "capital": "Stockholm",
        "currency": "Swedish Krona (SEK)",
        "airports": "ARN (Stockholm Arlanda), GOT (Gothenburg Landvetter), MMX (Malmo)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Sweden allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "switzerland": {
        "name": "Switzerland",
        "capital": "Bern",
        "currency": "Swiss Franc (CHF)",
        "airports": "ZRH (Zurich), GVA (Geneva), BSL (Basel EuroAirport)",
        "alert_type": "visa_free",
        "alert_text": "As a Schengen Area member, Switzerland allows visa-free entry for many nationalities for up to 90 days in any 180-day period.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "taiwan": {
        "name": "Taiwan",
        "capital": "Taipei",
        "currency": "New Taiwan Dollar (TWD)",
        "airports": "TPE (Taipei Taoyuan), TSA (Taipei Songshan), RMQ (Taichung), KHH (Kaohsiung)",
        "alert_type": "visa_free",
        "alert_text": "Many nationalities can enter Taiwan visa-free for 30-90 days. Others can apply for a travel authorization online.",
        "evisa_url": "https://visawebapp.boca.gov.tw",
        "evisa_name": "Taiwan Travel Authorization",
    },
    "thailand": {
        "name": "Thailand",
        "capital": "Bangkok",
        "currency": "Thai Baht (THB)",
        "airports": "BKK (Suvarnabhumi), DMK (Don Mueang), HKT (Phuket), CNX (Chiang Mai)",
        "alert_type": "evisa_available",
        "alert_text": "Thailand offers visa-free entry for 93 countries (60 days). For other nationalities, an eVisa must be obtained before travel.",
        "evisa_url": "https://www.thaievisa.go.th",
        "evisa_name": "Thailand eVisa",
    },
    "tonga": {
        "name": "Tonga",
        "capital": "Nukualofa",
        "currency": "Tongan Paanga (TOP)",
        "airports": "TBU (Fua'amotu International)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Tonga visa-free for up to 31 days. Visa extensions are available locally.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "turkey": {
        "name": "Turkey",
        "capital": "Ankara",
        "currency": "Turkish Lira (TRY)",
        "airports": "IST (Istanbul), SAW (Istanbul Sabiha Gokcen), ESB (Ankara Esenboga), ADB (Izmir), AYT (Antalya)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Many nationalities must obtain an eVisa online before travel. Some nationalities are visa-exempt for short stays (up to 90 days).",
        "evisa_url": "https://www.evisa.gov.tr",
        "evisa_name": "Turkey eVisa",
    },
    "uae": {
        "name": "United Arab Emirates",
        "capital": "Abu Dhabi",
        "currency": "UAE Dirham (AED)",
        "airports": "DXB (Dubai International), AUH (Abu Dhabi), SHJ (Sharjah)",
        "alert_type": "evisa_available",
        "alert_text": "Many nationalities receive visa-free entry or visa on arrival for 30-90 days. Others can apply for an eVisa before travel.",
        "evisa_url": "https://smartservices.icp.gov.ae",
        "evisa_name": "UAE eVisa",
    },
    "ukraine": {
        "name": "Ukraine",
        "capital": "Kyiv",
        "currency": "Ukrainian Hryvnia (UAH)",
        "airports": "KBP (Kyiv Boryspil), IEV (Kyiv Zhuliany), LWO (Lviv), ODS (Odesa)",
        "alert_type": "evisa_available",
        "alert_text": "Many nationalities can enter Ukraine visa-free for up to 90 days. An eVisa is available for nationalities not on the visa-free list. Note: check current travel advisories due to the ongoing conflict.",
        "evisa_url": "https://evisa.mfa.gov.ua",
        "evisa_name": "Ukraine eVisa",
    },
    "united-kingdom": {
        "name": "United Kingdom",
        "capital": "London",
        "currency": "British Pound Sterling (GBP)",
        "airports": "LHR (London Heathrow), LGW (London Gatwick), MAN (Manchester), EDI (Edinburgh)",
        "alert_type": "eta_required",
        "alert_text": "The UK Electronic Travel Authorisation (ETA) is required for non-visa nationals from 2025. Others must obtain a visa before travel.",
        "evisa_url": "https://www.gov.uk/electronic-travel-authorisation",
        "evisa_name": "UK ETA",
    },
    "uruguay": {
        "name": "Uruguay",
        "capital": "Montevideo",
        "currency": "Uruguayan Peso (UYU)",
        "airports": "MVD (Carrasco International, Montevideo)",
        "alert_type": "visa_free",
        "alert_text": "Most nationalities can enter Uruguay visa-free for up to 90 days.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "usa": {
        "name": "United States",
        "capital": "Washington, D.C.",
        "currency": "US Dollar (USD)",
        "airports": "JFK (New York), LAX (Los Angeles), ORD (Chicago), MIA (Miami), SFO (San Francisco)",
        "alert_type": "esta_required",
        "alert_text": "Citizens of 42 Visa Waiver Program (VWP) countries must apply for ESTA before travel. All other nationalities need a B-1/B-2 visa from a US embassy.",
        "evisa_url": "https://esta.cbp.dhs.gov",
        "evisa_name": "ESTA (Electronic System for Travel Authorization)",
    },
    "venezuela": {
        "name": "Venezuela",
        "capital": "Caracas",
        "currency": "Venezuelan Bolivar (VES)",
        "airports": "CCS (Simon Bolivar International, Caracas)",
        "alert_type": "visa_free",
        "alert_text": "Many nationalities can enter Venezuela visa-free for up to 90 days. Check current travel advisories before planning travel.",
        "evisa_url": "",
        "evisa_name": "",
    },
    "vietnam": {
        "name": "Vietnam",
        "capital": "Hanoi",
        "currency": "Vietnamese Dong (VND)",
        "airports": "SGN (Ho Chi Minh City Tan Son Nhat), HAN (Hanoi Noi Bai), DAD (Da Nang), CXR (Nha Trang Cam Ranh)",
        "alert_type": "evisa_available",
        "alert_text": "Vietnam offers visa-free entry for citizens of 25 countries (15-45 days). An eVisa is available for 80+ nationalities (single entry, 30 days). Visa on arrival is also possible with a pre-approved letter.",
        "evisa_url": "https://evisa.xuatnhapcanh.gov.vn",
        "evisa_name": "Vietnam eVisa",
    },
    # ── Ethiopia, Kenya, Azerbaijan, etc. ──────────────
    "ethiopia": {
        "name": "Ethiopia",
        "capital": "Addis Ababa",
        "currency": "Ethiopian Birr (ETB)",
        "airports": "ADD (Addis Ababa Bole International)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Most visitors require a visa for Ethiopia. An eVisa can be obtained online for tourism and business travel.",
        "evisa_url": "https://www.evisa.gov.et",
        "evisa_name": "Ethiopia eVisa",
    },
    "kenya": {
        "name": "Kenya",
        "capital": "Nairobi",
        "currency": "Kenyan Shilling (KES)",
        "airports": "NBO (Jomo Kenyatta International, Nairobi), MBA (Moi International, Mombasa)",
        "alert_type": "eta_required",
        "alert_text": "Kenya requires an Electronic Travel Authorization (eTA) for all visitors. Apply online before travel.",
        "evisa_url": "https://www.etakenya.go.ke",
        "evisa_name": "Kenya eTA",
    },
    "azerbaijan": {
        "name": "Azerbaijan",
        "capital": "Baku",
        "currency": "Azerbaijani Manat (AZN)",
        "airports": "GYD (Heydar Aliyev International, Baku)",
        "alert_type": "evisa_mandatory",
        "alert_text": "Most visitors require a visa for Azerbaijan. An ASAN eVisa can be obtained online (single entry, 30 days).",
        "evisa_url": "https://evisa.gov.az",
        "evisa_name": "Azerbaijan ASAN eVisa",
    },
    "russia": {
        "name": "Russia",
        "capital": "Moscow",
        "currency": "Russian Ruble (RUB)",
        "airports": "SVO (Moscow Sheremetyevo), DME (Moscow Domodedovo), LED (St. Petersburg Pulkovo)",
        "alert_type": "embassy_required",
        "alert_text": "Most nationalities require a visa from a Russian embassy or consulate before travel. An eVisa is available for some nationalities for visits to certain regions.",
        "evisa_url": "https://electronic-visa.kdmid.ru",
        "evisa_name": "Russia eVisa (limited)",
    },
    "north-korea": {
        "name": "North Korea",
        "capital": "Pyongyang",
        "currency": "North Korean Won (KPW)",
        "airports": "FNJ (Pyongyang Sunan)",
        "alert_type": "embassy_required",
        "alert_text": "A visa must be obtained through a licensed tour operator and the embassy. Independent travel is not permitted. US citizens are generally prohibited from traveling to North Korea.",
        "evisa_url": "",
        "evisa_name": "",
    },
}


def build_alert_html(country_data):
    """Build the alert block HTML for a given country."""
    atype = country_data["alert_type"]
    cfg = ALERT_CONFIG[atype]

    title = cfg["title_prefix"]
    text = country_data["alert_text"]
    url = country_data.get("evisa_url", "")
    url_label = country_data.get("evisa_name", "")

    link_html = ""
    if url:
        link_html = (
            f'\n            <a href="{url}" target="_blank" rel="noopener" '
            f'style="display:inline-block;margin-top:6px;color:{cfg["link_color"]};'
            f'font-weight:600;text-decoration:underline;font-size:14px;">'
            f'{url_label} \u2192</a>'
        )

    html = (
        f'\n<div class="visa-alert visa-alert-{atype}" style="'
        f'background:{cfg["bg"]};border-left:4px solid {cfg["border"]};'
        f'padding:16px 20px;border-radius:8px;margin:16px 0 20px;">'
        f'\n    <div style="display:flex;align-items:center;gap:12px;">'
        f'\n        <span style="font-size:28px;">{cfg["emoji"]}</span>'
        f'\n        <div>'
        f'\n            <strong style="font-size:16px;">{title}</strong>'
        f'\n            <p style="margin:4px 0 0;font-size:14px;">{text}</p>'
        f'{link_html}'
        f'\n        </div>'
        f'\n    </div>'
        f'\n</div>\n'
    )
    return html


def add_table_rows(html, country_data):
    """Add Capital, Currency, Main Airports rows to the Key Facts table if missing."""
    rows_to_add = []
    if "Capital" not in html or country_data["capital"] == "":
        pass  # will check more carefully below

    capital = country_data["capital"]
    currency = country_data["currency"]
    airports = country_data["airports"]

    # Check each row individually using a case-insensitive search within the table area
    # Find the first table (Key Facts)
    table_match = re.search(r'<table[^>]*>.*?</table>', html, re.DOTALL | re.IGNORECASE)
    if not table_match:
        return html

    table_html = table_match.group(0)
    table_start = table_match.start()
    table_end = table_match.end()

    new_rows = ""

    # Check for Capital row
    if not re.search(r'>Capital<', table_html, re.IGNORECASE):
        new_rows += f'<tr><th>Capital</th><td>{capital}</td></tr>\n'

    # Check for Currency row
    if not re.search(r'>Currency<', table_html, re.IGNORECASE):
        new_rows += f'<tr><th>Currency</th><td>{currency}</td></tr>\n'

    # Check for Main Airports row
    if not re.search(r'>Main Airports?<', table_html, re.IGNORECASE):
        new_rows += f'<tr><th>Main Airports</th><td>{airports}</td></tr>\n'

    if not new_rows:
        return html

    # Insert new rows before </tbody> in the first table
    tbody_end = table_html.rfind('</tbody>')
    if tbody_end == -1:
        # fallback: insert before </table>
        insert_pos = table_html.rfind('</table>')
    else:
        insert_pos = tbody_end

    new_table = table_html[:insert_pos] + new_rows + table_html[insert_pos:]
    html = html[:table_start] + new_table + html[table_end:]

    return html


def process_file(filepath, country_data):
    """Process a single visa-{country}.html file."""
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    modified = False

    # 1. Inject alert block after <h1>...</h1> if not already present
    if "visa-alert" not in html:
        # Find the h1 closing tag
        h1_match = re.search(r'</h1>', html, re.IGNORECASE)
        if h1_match:
            alert_html = build_alert_html(country_data)
            insert_pos = h1_match.end()
            html = html[:insert_pos] + alert_html + html[insert_pos:]
            modified = True

    # 2. Enrich Key Facts table
    original = html
    html = add_table_rows(html, country_data)
    if html != original:
        modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

    return modified


def main():
    # Scan directory for visa-*.html files
    pattern = os.path.join(EN_DIR, "visa-*.html")
    files = sorted(glob.glob(pattern))

    modified_count = 0
    skipped_no_data = []
    skipped_non_country = []

    for filepath in files:
        filename = os.path.basename(filepath)

        # Skip non-country pages
        if filename in SKIP_FILES:
            skipped_non_country.append(filename)
            continue

        skip = False
        for prefix in SKIP_PREFIXES:
            if filename.startswith(prefix):
                skip = True
                break
        if skip:
            skipped_non_country.append(filename)
            continue

        # Extract country slug
        slug = filename.replace("visa-", "").replace(".html", "")

        if slug not in COUNTRIES:
            skipped_no_data.append(slug)
            continue

        country_data = COUNTRIES[slug]
        was_modified = process_file(filepath, country_data)

        if was_modified:
            modified_count += 1
            print(f"  [MODIFIED] {filename}")
        else:
            print(f"  [NO CHANGE] {filename}")

    print(f"\n{'='*60}")
    print(f"  Total files scanned:  {len(files)}")
    print(f"  Files modified:       {modified_count}")
    print(f"  Skipped (non-country):{len(skipped_non_country)}")
    if skipped_no_data:
        print(f"  Skipped (no data):    {len(skipped_no_data)} -> {skipped_no_data}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
