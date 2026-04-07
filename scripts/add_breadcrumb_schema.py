#!/usr/bin/env python3
"""Add BreadcrumbList JSON-LD schema to all pages in www/."""
import os, re, json, html

SITE = "https://www.evisa-card.com"
WWW = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "www")

LANGS = {
    "en": "English", "fr": "Français", "es": "Español", "pt": "Português",
    "ar": "العربية", "ja": "日本語", "ko": "한국어", "ru": "Русский",
    "th": "ไทย", "zh": "中文"
}

LANG_HOME = {
    "en": "Home", "fr": "Accueil", "es": "Inicio", "pt": "Início",
    "ar": "الرئيسية", "ja": "ホーム", "ko": "홈", "ru": "Главная",
    "th": "หน้าแรก", "zh": "首页"
}

LANG_DEST = {
    "en": "Destinations", "fr": "Destinations", "es": "Destinos", "pt": "Destinos",
    "ar": "الوجهات", "ja": "目的地", "ko": "목적지", "ru": "Направления",
    "th": "จุดหมาย", "zh": "目的地"
}

LANG_GUIDES = {
    "en": "Expat Guides", "fr": "Guides Expatriés", "es": "Guías para Expatriados",
    "pt": "Guias para Expatriados", "ar": "أدلة المغتربين", "ja": "駐在ガイド",
    "ko": "주재원 가이드", "ru": "Гиды для экспатов", "th": "คู่มือชาวต่างชาติ",
    "zh": "外派指南"
}

LANG_BLOG = {
    "en": "Blog", "fr": "Blog", "es": "Blog", "pt": "Blog",
    "ar": "المدونة", "ja": "ブログ", "ko": "블로그", "ru": "Блог",
    "th": "บล็อก", "zh": "博客"
}

COUNTRY_NAMES = {
    "argentina": "Argentina", "australia": "Australia", "austria": "Austria",
    "belgium": "Belgium", "brazil": "Brazil", "cambodia": "Cambodia",
    "canada": "Canada", "china": "China", "colombia": "Colombia",
    "costa-rica": "Costa Rica", "croatia": "Croatia", "czech-republic": "Czech Republic",
    "denmark": "Denmark", "france": "France", "germany": "Germany",
    "greece": "Greece", "hong-kong": "Hong Kong", "hungary": "Hungary",
    "india": "India", "indonesia": "Indonesia", "ireland": "Ireland",
    "italy": "Italy", "japan": "Japan", "jordan": "Jordan",
    "malaysia": "Malaysia", "maldives": "Maldives", "mexico": "Mexico",
    "nepal": "Nepal", "netherlands": "Netherlands", "new-zealand": "New Zealand",
    "norway": "Norway", "philippines": "Philippines", "poland": "Poland",
    "portugal": "Portugal", "qatar": "Qatar", "romania": "Romania",
    "singapore": "Singapore", "spain": "Spain", "sri-lanka": "Sri Lanka",
    "sweden": "Sweden", "switzerland": "Switzerland", "taiwan": "Taiwan",
    "thailand": "Thailand", "turkey": "Turkey", "uae": "UAE",
    "united-kingdom": "United Kingdom", "usa": "USA", "vietnam": "Vietnam",
    "georgia": "Georgia", "laos": "Laos", "panama": "Panama", "paraguay": "Paraguay"
}


def make_breadcrumb_jsonld(items):
    """Generate BreadcrumbList JSON-LD from list of (name, url) tuples."""
    elements = []
    for i, (name, url) in enumerate(items, 1):
        elements.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": url
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements
    }
    return json.dumps(schema, ensure_ascii=False)


def get_country_from_filename(fname):
    """Extract country slug from filename like visa-argentina.html or argentina-visa-fees.html."""
    fname = fname.replace(".html", "")
    # visa-{country}.html
    m = re.match(r"visa-(.+)$", fname)
    if m:
        return m.group(1)
    # {country}-visa-*.html
    for slug in sorted(COUNTRY_NAMES.keys(), key=len, reverse=True):
        if fname.startswith(slug + "-visa-") or fname.startswith(slug + "-evisa") or fname.startswith(slug + "-eta") or fname.startswith(slug + "-evoa"):
            return slug
    # expat-guide-{country}.html
    m = re.match(r"expat-guide-(.+)$", fname)
    if m:
        return m.group(1)
    return None


def classify_page(fname):
    """Return (page_type, country_slug) for a filename."""
    if fname == "index.html":
        return ("home", None)
    if fname == "destination.html":
        return ("destination", None)
    if fname == "expat-guides.html":
        return ("expat-hub", None)
    if fname.startswith("expat-guide-"):
        country = fname.replace("expat-guide-", "").replace(".html", "")
        return ("expat-guide", country)
    if re.match(r"visa-[a-z]", fname) and "-for-" not in fname:
        country = fname.replace("visa-", "").replace(".html", "")
        return ("visa-country", country)
    if "-visa-for-" in fname:
        country = get_country_from_filename(fname)
        return ("visa-nationality", country)
    if "-visa-fees" in fname:
        country = get_country_from_filename(fname)
        return ("visa-fees", country)
    if "-visa-processing-time" in fname:
        country = get_country_from_filename(fname)
        return ("visa-processing", country)
    if "-visa-extension" in fname:
        country = get_country_from_filename(fname)
        return ("visa-extension", country)
    if "-visa-requirements" in fname:
        country = get_country_from_filename(fname)
        return ("visa-requirements", country)
    if "-evisa" in fname or "-eta" in fname or "-evoa" in fname:
        country = get_country_from_filename(fname)
        return ("visa-evisa", country)
    if fname.startswith("visa-free-countries-"):
        return ("visa-free", None)
    if fname.startswith("blog"):
        return ("blog", None)
    # editorial pages
    if fname in ("how-to-apply-evisa.html", "visa-documents-checklist.html",
                  "visa-photo-requirements.html", "visa-processing-times.html",
                  "visa-rejection-reasons.html", "travel-insurance-for-visa-applications.html",
                  "digital-nomad-visas-guide.html", "best-countries-digital-nomads-2026.html",
                  "cheapest-countries-to-retire-abroad-2026.html", "visa-result.html"):
        return ("editorial", None)
    if fname in ("about-our-experts.html", "editorial-policy.html", "our-methodology.html",
                  "disclaimer.html", "legal-notice.html"):
        return ("trust", None)
    return ("other", None)


def build_breadcrumbs(fname, lang):
    """Build breadcrumb trail for a page."""
    page_type, country = classify_page(fname)
    home_name = LANG_HOME.get(lang, "Home")
    home_url = f"{SITE}/{lang}/" if lang != "root" else f"{SITE}/"
    dest_name = LANG_DEST.get(lang, "Destinations")
    dest_url = f"{SITE}/destination.html" if lang == "root" else f"{SITE}/{lang}/destination.html" if os.path.exists(os.path.join(WWW, lang, "destination.html")) else f"{SITE}/destination.html"
    country_name = COUNTRY_NAMES.get(country, country.replace("-", " ").title() if country else "")

    crumbs = [(home_name, home_url)]

    if page_type == "home":
        return None  # no breadcrumb on homepage
    elif page_type == "destination":
        crumbs.append((dest_name, f"{SITE}/destination.html"))
    elif page_type in ("visa-country", "visa-nationality", "visa-fees", "visa-processing",
                        "visa-extension", "visa-requirements", "visa-evisa"):
        crumbs.append((dest_name, dest_url))
        if country_name:
            lang_prefix = f"/{lang}" if lang != "root" else ""
            visa_page_url = f"{SITE}{lang_prefix}/visa-{country}.html"
            if page_type == "visa-country":
                crumbs.append((country_name, visa_page_url))
            else:
                crumbs.append((country_name, visa_page_url))
                # sub-page name
                subpage_names = {
                    "visa-nationality": "Visa by Nationality",
                    "visa-fees": "Visa Fees",
                    "visa-processing": "Processing Time",
                    "visa-extension": "Visa Extension",
                    "visa-requirements": "Visa Requirements",
                    "visa-evisa": "eVisa"
                }
                sub_name = subpage_names.get(page_type, fname.replace(".html", "").replace("-", " ").title())
                crumbs.append((sub_name, f"{SITE}/{lang}/{fname}" if lang != "root" else f"{SITE}/{fname}"))
    elif page_type == "expat-hub":
        guides_name = LANG_GUIDES.get(lang, "Expat Guides")
        crumbs.append((guides_name, f"{SITE}/{lang}/expat-guides.html" if lang != "root" else f"{SITE}/expat-guides.html"))
    elif page_type == "expat-guide":
        guides_name = LANG_GUIDES.get(lang, "Expat Guides")
        crumbs.append((guides_name, f"{SITE}/{lang}/expat-guides.html" if lang != "root" else f"{SITE}/expat-guides.html"))
        crumbs.append((country_name, f"{SITE}/{lang}/{fname}" if lang != "root" else f"{SITE}/{fname}"))
    elif page_type == "blog":
        blog_name = LANG_BLOG.get(lang, "Blog")
        crumbs.append((blog_name, f"{SITE}/blog.html"))
    elif page_type in ("editorial", "visa-free"):
        # Extract title from filename
        nice_name = fname.replace(".html", "").replace("-", " ").title()
        crumbs.append((nice_name, f"{SITE}/{lang}/{fname}" if lang != "root" else f"{SITE}/{fname}"))
    elif page_type == "trust":
        nice_name = fname.replace(".html", "").replace("-", " ").title()
        crumbs.append((nice_name, f"{SITE}/{lang}/{fname}" if lang != "root" else f"{SITE}/{fname}"))
    else:
        nice_name = fname.replace(".html", "").replace("-", " ").title()
        crumbs.append((nice_name, f"{SITE}/{lang}/{fname}" if lang != "root" else f"{SITE}/{fname}"))

    return crumbs


def inject_breadcrumb(filepath, lang):
    """Inject BreadcrumbList schema into a page if not already present."""
    fname = os.path.basename(filepath)
    crumbs = build_breadcrumbs(fname, lang)
    if crumbs is None:
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "BreadcrumbList" in content:
        return False

    jsonld = make_breadcrumb_jsonld(crumbs)
    tag = f'\n    <script type="application/ld+json">{jsonld}</script>'

    # Insert before </head>
    if "</head>" in content:
        content = content.replace("</head>", tag + "\n</head>", 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    count = 0
    errors = 0

    # Process root-level pages
    for fname in os.listdir(os.path.join(WWW)):
        if not fname.endswith(".html"):
            continue
        filepath = os.path.join(WWW, fname)
        if os.path.isfile(filepath):
            try:
                if inject_breadcrumb(filepath, "root"):
                    count += 1
            except Exception as e:
                print(f"  ERROR {filepath}: {e}")
                errors += 1

    # Process language directories
    for lang in LANGS:
        lang_dir = os.path.join(WWW, lang)
        if not os.path.isdir(lang_dir):
            continue
        files = [f for f in os.listdir(lang_dir) if f.endswith(".html")]
        for fname in files:
            filepath = os.path.join(lang_dir, fname)
            try:
                if inject_breadcrumb(filepath, lang):
                    count += 1
            except Exception as e:
                print(f"  ERROR {filepath}: {e}")
                errors += 1

    print(f"\nDone: {count} pages updated, {errors} errors")


if __name__ == "__main__":
    main()
