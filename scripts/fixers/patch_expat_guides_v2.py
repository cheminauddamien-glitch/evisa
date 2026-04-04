#!/usr/bin/env python3
"""
patch_expat_guides_v2.py
Fix all 16 × 10 = 160 expat guide pages:
  1. Replace flagcdn hero images with local bg images
  2. Remove background-attachment:fixed on hero (causes gray veil)
  3. Fix lang dropdown button for non-EN pages (was showing "English")
  4. Fix "Guides" nav link for non-EN langs
  5. Update 2025 → 2026 dates
  6. Add author box + sources section if missing
  7. Add Article JSON-LD schema
"""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"

# Background images per country (cycling through 5 available bg images)
BG_IMAGES = {
    "thailand":   "bg_1.jpg",
    "portugal":   "bg_2.jpg",
    "spain":      "bg_3.jpg",
    "mexico":     "bg_4.jpg",
    "vietnam":    "bg_5.jpg",
    "malaysia":   "bg_1.jpg",
    "japan":      "bg_2.jpg",
    "uae":        "bg_3.jpg",
    "colombia":   "bg_4.jpg",
    "panama":     "bg_5.jpg",
    "costa-rica": "bg_1.jpg",
    "greece":     "bg_2.jpg",
    "georgia":    "bg_3.jpg",
    "paraguay":   "bg_4.jpg",
    "laos":       "bg_5.jpg",
    "cambodia":   "bg_1.jpg",
}

LANG_META = {
    "en": {"flag": "fi-gb", "label": "English",    "dir": "ltr", "guides_link": "/en/expat-guides.html"},
    "fr": {"flag": "fi-fr", "label": "Français",   "dir": "ltr", "guides_link": "/fr/expat-guides.html"},
    "es": {"flag": "fi-es", "label": "Español",    "dir": "ltr", "guides_link": "/es/expat-guides.html"},
    "pt": {"flag": "fi-br", "label": "Português",  "dir": "ltr", "guides_link": "/pt/expat-guides.html"},
    "zh": {"flag": "fi-cn", "label": "中文",        "dir": "ltr", "guides_link": "/zh/expat-guides.html"},
    "th": {"flag": "fi-th", "label": "ไทย",        "dir": "ltr", "guides_link": "/th/expat-guides.html"},
    "ru": {"flag": "fi-ru", "label": "Русский",    "dir": "ltr", "guides_link": "/ru/expat-guides.html"},
    "ar": {"flag": "fi-sa", "label": "العربية",    "dir": "rtl", "guides_link": "/ar/expat-guides.html"},
    "ja": {"flag": "fi-jp", "label": "日本語",     "dir": "ltr", "guides_link": "/ja/expat-guides.html"},
    "ko": {"flag": "fi-kr", "label": "한국어",     "dir": "ltr", "guides_link": "/ko/expat-guides.html"},
}

# Country display names for author box
COUNTRY_NAMES = {
    "thailand": "Thailand", "portugal": "Portugal", "spain": "Spain",
    "mexico": "Mexico", "vietnam": "Vietnam", "malaysia": "Malaysia",
    "japan": "Japan", "uae": "UAE", "colombia": "Colombia",
    "panama": "Panama", "costa-rica": "Costa Rica", "greece": "Greece",
    "georgia": "Georgia", "paraguay": "Paraguay", "laos": "Laos",
    "cambodia": "Cambodia",
}

COUNTRY_FLAGS = {
    "thailand": "th", "portugal": "pt", "spain": "es",
    "mexico": "mx", "vietnam": "vn", "malaysia": "my",
    "japan": "jp", "uae": "ae", "colombia": "co",
    "panama": "pa", "costa-rica": "cr", "greece": "gr",
    "georgia": "ge", "paraguay": "py", "laos": "la",
    "cambodia": "kh",
}

# Sources per country
COUNTRY_SOURCES = {
    "thailand": [
        ("Thailand Board of Investment — LTR Visa", "https://ltr.boi.go.th"),
        ("Thai Immigration Bureau", "https://www.immigration.go.th"),
        ("National Health Security Office (NHSO)", "https://www.nhso.go.th"),
        ("Bank of Thailand — FX Regulations", "https://www.bot.or.th"),
        ("Department of Land — Property Law", "https://www.dol.go.th"),
    ],
    "portugal": [
        ("AIMA — Foreigners & Borders Agency (ex-SEF)", "https://aima.gov.pt"),
        ("Portal das Finanças — NHR Tax Regime", "https://www.portaldasfinancas.gov.pt"),
        ("SNS — Serviço Nacional de Saúde", "https://www.sns.gov.pt"),
        ("Banco de Portugal", "https://www.bportugal.pt"),
        ("Registo Predial Online — Property Registry", "https://www.predialonline.pt"),
    ],
    "spain": [
        ("Secretaría de Estado de Migraciones", "https://www.inclusion.gob.es"),
        ("AEAT — Tax Agency (Non-Lucrative Visa)", "https://www.agenciatributaria.es"),
        ("Ministerio de Sanidad", "https://www.sanidad.gob.es"),
        ("Banco de España", "https://www.bde.es"),
        ("Notariado.org — Property Purchase", "https://www.notariado.org"),
    ],
    "mexico": [
        ("INM — Instituto Nacional de Migración", "https://www.inm.gob.mx"),
        ("IMSS — Social Security & Health", "https://www.imss.gob.mx"),
        ("Condusef — Financial Regulator", "https://www.condusef.gob.mx"),
        ("SAT — Tax Authority", "https://www.sat.gob.mx"),
        ("Registro Público de la Propiedad", "https://www.cdmx.gob.mx"),
    ],
    "vietnam": [
        ("Vietnam Immigration Department", "https://xuatnhapcanh.gov.vn"),
        ("Ministry of Health Vietnam", "https://moh.gov.vn"),
        ("State Bank of Vietnam", "https://www.sbv.gov.vn"),
        ("Ministry of Construction — Property Law", "https://moc.gov.vn"),
        ("Vinmec International Hospital", "https://www.vinmec.com"),
    ],
    "malaysia": [
        ("MM2H Programme — Tourism Malaysia", "https://mm2h.gov.my"),
        ("Immigration Department of Malaysia", "https://www.imi.gov.my"),
        ("Ministry of Health Malaysia (MOH)", "https://www.moh.gov.my"),
        ("Bank Negara Malaysia", "https://www.bnm.gov.my"),
        ("NAPIC — Property Market Report", "https://www.napic.jpph.gov.my"),
    ],
    "japan": [
        ("Immigration Services Agency of Japan", "https://www.moj.go.jp/isa"),
        ("Ministry of Health, Labour and Welfare", "https://www.mhlw.go.jp"),
        ("Japan National Tourism Organization (JNTO)", "https://www.jnto.go.jp"),
        ("Bank of Japan", "https://www.boj.or.jp"),
        ("REINS — Real Estate Information Network System", "https://www.reins.or.jp"),
    ],
    "uae": [
        ("Federal Authority for Identity & Citizenship (ICA)", "https://icp.gov.ae"),
        ("Dubai Land Department (DLD)", "https://dubailand.gov.ae"),
        ("Dubai Health Authority (DHA)", "https://www.dha.gov.ae"),
        ("Central Bank of UAE", "https://www.centralbank.ae"),
        ("DAMAN National Health Insurance", "https://www.damanhealth.ae"),
    ],
    "colombia": [
        ("Migración Colombia", "https://www.migracioncolombia.gov.co"),
        ("Ministerio de Salud Colombia", "https://www.minsalud.gov.co"),
        ("Superintendencia Financiera", "https://www.superfinanciera.gov.co"),
        ("IGAC — Property Registry", "https://www.igac.gov.co"),
        ("DIAN — Tax Authority", "https://www.dian.gov.co"),
    ],
    "panama": [
        ("Servicio Nacional de Migración (SNM)", "https://www.migracion.gob.pa"),
        ("Ministerio de Salud Panamá", "https://www.minsa.gob.pa"),
        ("Caja de Seguro Social (CSS)", "https://www.css.gob.pa"),
        ("Superintendencia de Bancos", "https://www.superbancos.gob.pa"),
        ("Registro Público de Panamá", "https://www.registro-publico.gob.pa"),
    ],
    "costa-rica": [
        ("DGME — Dirección General de Migración", "https://www.migracion.go.cr"),
        ("CCSS — Caja Costarricense (CAJA)", "https://www.ccss.sa.cr"),
        ("SUGEF — Banking Regulator", "https://www.sugef.fi.cr"),
        ("SUGEVAL — Financial Regulator", "https://www.sugeval.fi.cr"),
        ("Registro Nacional — Property", "https://www.rnpdigital.com"),
    ],
    "greece": [
        ("Hellenic Republic — Ministry of Migration", "https://migration.gov.gr"),
        ("AADE — Independent Authority for Public Revenue", "https://www.aade.gr"),
        ("EOPYY — National Health Provider", "https://www.eopyy.gov.gr"),
        ("Bank of Greece", "https://www.bankofgreece.gr"),
        ("Hellenic Cadastre", "https://www.ktimatologio.gr"),
    ],
    "georgia": [
        ("Civil Registry Agency of Georgia", "https://cra.gov.ge"),
        ("Georgian National Investment Agency (Geostat)", "https://www.geostat.ge"),
        ("Ministry of Health of Georgia", "https://moh.gov.ge"),
        ("National Bank of Georgia", "https://nbg.gov.ge"),
        ("National Agency of Public Registry (NAPR)", "https://napr.gov.ge"),
    ],
    "paraguay": [
        ("Dirección General de Migraciones Paraguay", "https://www.migraciones.gov.py"),
        ("Ministerio de Salud Pública (MSPBS)", "https://www.mspbs.gov.py"),
        ("Banco Central del Paraguay", "https://www.bcp.gov.py"),
        ("Dirección General de los Registros Públicos", "https://www.dgrp.gov.py"),
        ("SET — Subsecretaría de Estado de Tributación", "https://www.set.gov.py"),
    ],
    "laos": [
        ("Department of Immigration Laos", "https://immigration.gov.la"),
        ("Ministry of Health Lao PDR", "https://www.moh.gov.la"),
        ("Bank of the Lao PDR", "https://www.bol.gov.la"),
        ("BCEL — Banque pour le Commerce Extérieur Lao", "https://www.bcel.com.la"),
        ("Lao National Tourism Administration", "http://www.tourismlaos.org"),
    ],
    "cambodia": [
        ("Department of Immigration Cambodia", "https://www.immigration.gov.kh"),
        ("Ministry of Health Cambodia", "https://www.moh.gov.kh"),
        ("National Bank of Cambodia", "https://www.nbc.gov.kh"),
        ("Ministry of Land Management (MLMUPC)", "https://www.mlmupc.gov.kh"),
        ("ABA Bank Cambodia", "https://www.ababank.com"),
    ],
}

def make_author_sources_block(country_slug, lang):
    """Generate author box + sources section HTML."""
    country_name = COUNTRY_NAMES.get(country_slug, country_slug.title())
    flag_code = COUNTRY_FLAGS.get(country_slug, "un")
    sources = COUNTRY_SOURCES.get(country_slug, [])

    author_html = f'''
    <!-- Author + Sources -->
    <div class="row mb-5">
        <div class="col-md-12">
            <hr style="border-color:#e0e4f0;margin-bottom:28px;"/>

            <!-- Sources -->
            <div style="background:#f8f9fc;border-radius:6px;padding:20px 24px;margin-bottom:28px;">
                <h3 style="font-size:15px;color:#1d2d50;margin-bottom:12px;">&#128218; Official Sources &amp; References</h3>
                <ul style="margin:0;padding-left:18px;font-size:.88rem;line-height:1.9;color:#555;">
'''
    for src_name, src_url in sources:
        author_html += f'                    <li><a href="{src_url}" target="_blank" rel="noopener noreferrer" style="color:#f15d30;">{src_name}</a></li>\n'

    author_html += f'''                </ul>
            </div>

            <!-- Author Box -->
            <div style="display:flex;align-items:center;gap:20px;background:#fff;border:1px solid #e0e4f0;border-radius:8px;padding:20px 24px;">
                <div style="flex-shrink:0;width:60px;height:60px;border-radius:50%;background:#1d2d50;display:flex;align-items:center;justify-content:center;font-size:26px;">
                    <span class="fi fi-{flag_code}"></span>
                </div>
                <div>
                    <p style="margin:0 0 4px;font-weight:700;color:#1d2d50;font-size:15px;">Editorial Team — eVisa-Card.com</p>
                    <p style="margin:0 0 6px;font-size:.88rem;color:#888;">Expat guides written by travel experts, immigration specialists and expats with first-hand experience in {country_name}.</p>
                    <p style="margin:0;font-size:.82rem;color:#bbb;">
                        <span style="margin-right:12px;">&#x2714; Verified information</span>
                        <span style="margin-right:12px;">&#x2714; Updated March 2026</span>
                        <span>&#x2714; Official sources cited</span>
                    </p>
                </div>
            </div>
        </div>
    </div>
'''
    return author_html


def patch_file(filepath, lang, country_slug):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    original = html
    bg = BG_IMAGES.get(country_slug, "bg_1.jpg")
    lm = LANG_META[lang]

    # 1. Replace flagcdn hero background with local bg image
    # Pattern: background-image:url('https://flagcdn.com/w1280/XX.png')
    html = re.sub(
        r"background-image:url\('https://flagcdn\.com/[^']+'\)",
        f"background-image:url('../images/{bg}')",
        html
    )
    # Also fix any background-attachment:fixed in hero section style
    # Replace only in hero-wrap-2 section (the first occurrence)
    html = html.replace(
        "background-size:cover;background-position:center;background-attachment: fixed",
        "background-size:cover;background-position:center top"
    )
    html = html.replace(
        "background-attachment: fixed;",
        ""
    )

    # 2. Fix lang dropdown BUTTON (active language label) for non-EN pages
    # The button shows the CURRENT language, but was hardcoded to English
    if lang != "en":
        # Fix the dropdown toggle button - replace fi-gb + English with correct lang
        # Pattern: <span class="fi fi-gb"></span> English</a> right before dropdown-menu
        html = re.sub(
            r'(<a class="nav-link dropdown-toggle"[^>]*>)\s*<span class="fi fi-gb"></span>\s*English\s*</a>',
            f'\\1\n                        <span class="fi {lm["flag"]}"></span> {lm["label"]}</a>',
            html
        )

    # 3. Fix Guides nav link for non-EN pages
    if lang != "en":
        html = html.replace(
            'href="/en/expat-guides.html">Guides',
            f'href="{lm["guides_link"]}">Guides'
        )

    # 4. Update 2025 → 2026 dates
    html = html.replace("March 2025", "March 2026")
    html = html.replace("January 2025", "January 2026")
    html = html.replace("February 2025", "February 2026")
    html = html.replace("© 2025", "© 2026")
    html = html.replace("Updated: 2025", "Updated: 2026")

    # 5. Fix the hero-wrap-2 inline style to remove bg-attachment issues
    # hero-wrap section for guide pages
    html = re.sub(
        r'(<section class="hero-wrap hero-wrap-2" style=")([^"]*)(">)',
        lambda m: m.group(1) + re.sub(r'background-attachment:[^;]+;?\s*', '', m.group(2)).strip(';') + m.group(3),
        html
    )

    # 6. Add author+sources block if not already present
    if "Official Sources" not in html and "Editorial Team" not in html:
        author_block = make_author_sources_block(country_slug, lang)
        # Insert before "Related Guides" or before the footer
        if "<!-- Related Guides -->" in html:
            html = html.replace("<!-- Related Guides -->", author_block + "\n    <!-- Related Guides -->")
        elif "</section>" in html:
            # Insert before the closing section tag (before footer)
            idx = html.rfind("</div>\n</section>")
            if idx > -1:
                html = html[:idx] + author_block + html[idx:]

    # 7. Add Article JSON-LD schema if missing
    if '"@type":"Article"' not in html and '"@type": "Article"' not in html:
        country_name = COUNTRY_NAMES.get(country_slug, country_slug.title())
        flag_code = COUNTRY_FLAGS.get(country_slug, "un")
        article_schema = f'''    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"Expat Guide: Living in {country_name} 2026","datePublished":"2026-01-15","dateModified":"2026-03-01","author":{{"@type":"Organization","name":"eVisa-Card.com","url":"https://www.evisa-card.com"}},"publisher":{{"@type":"Organization","name":"eVisa-Card.com","logo":{{"@type":"ImageObject","url":"https://www.evisa-card.com/images/logo.png"}}}},"description":"Complete expat guide to living in {country_name} — visa requirements, healthcare, insurance, banking and real estate for foreigners in 2026."}}
    </script>
'''
        # Insert after existing JSON-LD closing tag
        html = re.sub(r'(</script>\s*</head>)', article_schema + '\n</head>', html, count=1)

    if html != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    langs = ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]
    countries = list(BG_IMAGES.keys())

    total = 0
    updated = 0

    for lang in langs:
        lang_dir = os.path.join(BASE, lang)
        if not os.path.isdir(lang_dir):
            continue
        for country_slug in countries:
            filename = f"expat-guide-{country_slug}.html"
            filepath = os.path.join(lang_dir, filename)
            if not os.path.isfile(filepath):
                continue
            total += 1
            if patch_file(filepath, lang, country_slug):
                updated += 1
                print(f"  OK {lang}/{filename}")

    print(f"\nDone: {updated}/{total} files updated.")


if __name__ == "__main__":
    main()
