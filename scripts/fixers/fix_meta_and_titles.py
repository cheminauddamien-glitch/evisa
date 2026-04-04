#!/usr/bin/env python3
"""
Fix 1: Add meta descriptions to legal pages (disclaimer, legal-notice) in all langs
Fix 2: Shorten long titles in FR/ES/PT visa pages
"""
import os, re

BASE = r"C:/Users/chemi/Documents/evisa/pacific-main/www"
LANGS = ["en","fr","es","pt","zh","th","ru","ar","ja","ko"]

# ── 1. Legal pages meta descriptions ──────────────────────────────────────────
LEGAL_META = {
    "disclaimer.html": "eVisa-Card.com disclaimer: visa information is provided for reference purposes only. Always verify requirements at official government sources before travel.",
    "legal-notice.html": "Legal notice for eVisa-Card.com — publisher information, intellectual property, limitations of liability and applicable law.",
    "aviso-legal.html": "Aviso legal de eVisa-Card.com — información del editor, propiedad intelectual y limitaciones de responsabilidad.",
    "mentions-legales.html": "Mentions légales d'eVisa-Card.com — informations sur l'éditeur, propriété intellectuelle et limitations de responsabilité.",
}

fixed_meta = 0
for lang in LANGS:
    lang_dir = os.path.join(BASE, lang)
    if not os.path.isdir(lang_dir):
        continue
    for fname, meta_desc in LEGAL_META.items():
        path = os.path.join(lang_dir, fname)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        if 'name="description"' in html or "name='description'" in html:
            continue  # already has meta description
        # Insert meta description after charset
        new_meta = f'    <meta name="description" content="{meta_desc}"/>\n'
        html = re.sub(
            r'(<meta charset="utf-8"[^>]*/?>)',
            r'\1\n' + new_meta,
            html, count=1
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Meta added: {lang}/{fname}")
        fixed_meta += 1

# Also fix blog-single.html
for bdir in [BASE, os.path.join(BASE, "en")]:
    bpath = os.path.join(bdir, "blog-single.html")
    if not os.path.exists(bpath):
        bpath = os.path.join(BASE, "blog-single.html")
    if os.path.exists(bpath):
        with open(bpath, "r", encoding="utf-8") as f:
            html = f.read()
        if 'name="description"' not in html:
            html = re.sub(
                r'(<meta charset="utf-8"[^>]*/?>)',
                r'\1\n    <meta name="description" content="eVisa-Card.com travel blog — visa guides, travel tips and immigration news for international travelers."/>\n',
                html, count=1
            )
            with open(bpath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  Meta added: blog-single.html")
            fixed_meta += 1

print(f"\nMeta descriptions fixed: {fixed_meta}")

# ── 2. Fix long titles (>60 chars) in multilang visa pages ────────────────────
# Map of EN title patterns to shorter versions
# These are the pages the audit flagged
TITLE_FIXES = {
    # FR pages
    "fr/visa-costa-rica.html": "Visa Costa Rica 2026 — Conditions &amp; Entrée",
    "fr/visa-colombia.html": "Visa Colombie 2026 — Conditions &amp; Formalités",
    "fr/visa-turkey.html": "Visa Turquie 2026 — eVisa, Frais &amp; Demande",
    "fr/visa-argentina.html": "Visa Argentine 2026 — Conditions &amp; Entrée",
    "fr/visa-qatar.html": "Visa Qatar 2026 — eVisa, Frais &amp; Conditions",
    "fr/visa-brazil.html": "Visa Brésil 2026 — eVisa, Conditions &amp; Guide",
    "fr/visa-india.html": "Visa Inde 2026 — e-Tourist Visa, Frais &amp; Demande",
    "fr/visa-mexico.html": "Visa Mexique 2026 — FMM, Conditions &amp; Entrée",
    "fr/visa-usa.html": "Visa USA 2026 — ESTA, B1/B2 &amp; Conditions",
    "fr/visa-china.html": "Visa Chine 2026 — eVisa, Transit &amp; Conditions",
    "fr/retirement-visa-guide.html": "Guide Visa Retraite 2026 — Meilleures Destinations",
    # ES pages
    "es/visa-croatia.html": "Visa Croacia 2026 — Condiciones &amp; Entrada",
    "es/visa-united-kingdom.html": "Visa Reino Unido 2026 — ETA &amp; Condiciones",
    "es/visa-philippines.html": "Visa Filipinas 2026 — eVisa &amp; Condiciones",
    "es/visa-sri-lanka.html": "Visa Sri Lanka 2026 — ETA, Tasas &amp; Entrada",
    "es/visa-thailand.html": "Visa Tailandia 2026 — eVisa, Tasas &amp; Condiciones",
    "es/visa-hong-kong.html": "Visa Hong Kong 2026 — Condiciones &amp; Entrada",
    "es/visa-taiwan.html": "Visa Taiwán 2026 — eVisa, Golden Card &amp; Entrada",
    "es/visa-vietnam.html": "Visa Vietnam 2026 — eVisa USD 25 &amp; Condiciones",
    "es/visa-norway.html": "Visa Noruega 2026 — Schengen &amp; Condiciones",
    "es/visa-hungary.html": "Visa Hungría 2026 — Schengen eVisa &amp; Solicitud",
    "es/visa-new-zealand.html": "Visa Nueva Zelanda 2026 — NZeTA &amp; Solicitud",
    "es/visa-nepal.html": "Visa Nepal 2026 — eVisa, Permisos &amp; Tasas",
    "es/visa-singapore.html": "Visa Singapur 2026 — ONE Pass &amp; Condiciones",
    "es/visa-maldives.html": "Visa Maldivas 2026 — Entrada Gratuita &amp; Guía",
    "es/visa-denmark.html": "Visa Dinamarca 2026 — Schengen &amp; Condiciones",
    "es/visa-ireland.html": "Visa Irlanda 2026 — Tourist Visa &amp; Condiciones",
    "es/visa-sweden.html": "Visa Suecia 2026 — Schengen &amp; Condiciones",
    "es/visa-poland.html": "Visa Polonia 2026 — Schengen eVisa &amp; Solicitud",
    "es/visa-cambodia.html": "Visa Camboya 2026 — eVisa USD 30 &amp; Entrada",
    "es/visa-australia.html": "Visa Australia 2026 — ETA, eVisitor &amp; Solicitud",
    "es/visa-jordan.html": "Visa Jordania 2026 — Jordan Pass &amp; Condiciones",
    "es/visa-norway.html": "Visa Noruega 2026 — Schengen &amp; Condiciones",
    "es/visa-uae.html": "Visa EAU 2026 — eVisa, Dubai &amp; Golden Visa",
    "es/visa-qatar.html": "Visa Catar 2026 — eVisa, Frais &amp; Condiciones",
    "es/visa-czech-republic.html": "Visa República Checa 2026 — Schengen &amp; Guía",
    "es/retirement-visa-guide.html": "Guía Visa Jubilación 2026 — Mejores Destinos",
    # PT pages
    "pt/visa-thailand.html": "Visto Tailândia 2026 — eVisa, Taxas &amp; Regras",
    "pt/visa-malaysia.html": "Visto Malásia 2026 — Condições &amp; Entrada",
    "pt/visa-uae.html": "Visto EAU 2026 — eVisa, Dubai &amp; Condições",
    "pt/visa-australia.html": "Visto Austrália 2026 — ETA, eVisitor &amp; Guia",
    "pt/visa-costa-rica.html": "Visto Costa Rica 2026 — Condições &amp; Entrada",
    "pt/visa-jordan.html": "Visto Jordânia 2026 — Jordan Pass &amp; Condições",
    "pt/visa-usa.html": "Visto EUA 2026 — ESTA, B1/B2 &amp; Condições",
    "pt/visa-mexico.html": "Visto México 2026 — FMM, Condições &amp; Entrada",
    "pt/visa-singapore.html": "Visto Singapura 2026 — ONE Pass &amp; Condições",
    "pt/visa-hungary.html": "Visto Hungria 2026 — Schengen eVisa &amp; Guia",
    "pt/visa-united-kingdom.html": "Visto Reino Unido 2026 — ETA &amp; Condições",
    "pt/visa-brazil.html": "Visto Brasil 2026 — eVisa, Condições &amp; Guia",
    "pt/visa-philippines.html": "Visto Filipinas 2026 — eVisa &amp; Condições",
    "pt/visa-turkey.html": "Visto Turquia 2026 — eVisa USD 60 &amp; Guia",
    "pt/visa-taiwan.html": "Visto Taiwan 2026 — eVisa, Gold Card &amp; Entrada",
    "pt/visa-new-zealand.html": "Visto Nova Zelândia 2026 — NZeTA &amp; Solicitud",
    "pt/visa-nepal.html": "Visto Nepal 2026 — eVisa, Permisos &amp; Taxas",
    "pt/visa-romania.html": "Visto Roménia 2026 — Schengen &amp; Guia",
    "pt/visa-colombia.html": "Visto Colômbia 2026 — Nômade Digital &amp; Entrada",
    "pt/visa-belgium.html": "Visto Bélgica 2026 — Schengen eVisa &amp; Guia",
    "pt/visa-canada.html": "Visto Canadá 2026 — eTA, Condições &amp; Guia",
    "pt/visa-china.html": "Visto China 2026 — eVisa, Trânsito &amp; Condições",
    "pt/visa-indonesia.html": "Visto Indonésia 2026 — eVOA, Bali &amp; Condições",
    "pt/visa-ireland.html": "Visto Irlanda 2026 — Tourist Visa &amp; Condições",
    "pt/visa-maldives.html": "Visto Maldivas 2026 — Entrada Gratuita &amp; Guia",
    "pt/visa-qatar.html": "Visto Qatar 2026 — eVisa, Taxas &amp; Condições",
    "pt/visa-croatia.html": "Visto Croácia 2026 — Schengen &amp; Condições",
    "pt/visa-greece.html": "Visto Grécia 2026 — Schengen eVisa &amp; Guia",
    "pt/visa-argentina.html": "Visto Argentina 2026 — Condições &amp; Entrada",
    "pt/visa-colombia.html": "Visto Colômbia 2026 — Nômade Digital &amp; Guia",
    "pt/retirement-visa-guide.html": "Guia Visto Reforma 2026 — Melhores Destinos",
    # EN pages flagged
    "en/visa-spain.html": "Spain Visa Requirements 2026 — Schengen &amp; Steps",
    "en/visa-ireland.html": "Ireland Visa Requirements 2026 — Tourist Visa &amp; Fees",
    "en/visa-germany.html": "Germany Visa Requirements 2026 — Schengen &amp; Fees",
    "en/visa-switzerland.html": "Switzerland Visa Requirements 2026 — Schengen &amp; ETA",
    "en/retirement-visa-guide.html": "Retirement Visa Guide 2026 — Best Countries",
    # RU pages
    "ru/visa-ireland.html": "Виза в Ирландию 2026 — Условия и документы",
    "ru/visa-france.html": "Виза во Францию 2026 — Шенген, сборы и заявка",
    "ru/visa-germany.html": "Виза в Германию 2026 — Шенген, сборы и заявка",
    "ru/visa-switzerland.html": "Виза в Швейцарию 2026 — Шенген и условия",
    "ru/visa-italy.html": "Виза в Италию 2026 — Шенген, сборы и заявка",
    "ru/visa-spain.html": "Виза в Испанию 2026 — Шенген и условия",
    "ru/visa-greece.html": "Виза в Грецию 2026 — Шенген и условия",
    # AR pages
    "ar/visa-germany.html": "تأشيرة ألمانيا 2026 — شنغن والمتطلبات",
}

fixed_titles = 0
for rel_path, new_title in TITLE_FIXES.items():
    path = os.path.join(BASE, rel_path.replace("/", os.sep))
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    # Replace title tag
    new_html = re.sub(r'<title>[^<]+</title>', f'<title>{new_title}</title>', html, count=1)
    # Also replace og:title if it matches the old title
    if new_html != html:
        old_title_match = re.search(r'<title>([^<]+)</title>', html)
        if old_title_match:
            old_title = old_title_match.group(1)
            new_html = new_html.replace(
                f'property="og:title" content="{old_title}"',
                f'property="og:title" content="{new_title}"'
            )
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"  Title fixed: {rel_path}")
        fixed_titles += 1

print(f"\nTitles fixed: {fixed_titles}")
print("DONE")
