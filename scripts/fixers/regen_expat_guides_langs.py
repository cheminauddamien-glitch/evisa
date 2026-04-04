"""
Fix EN expat guide pages (hero + ftco-animate) and force-regenerate FR/ES/PT from new detailed EN.
"""
import os, re, glob

WWW = "www"

# ── Language configs ──────────────────────────────────────────────────────────
EUR = {
    "fr": {
        "html_lang": "fr",
        "flag": "fi-fr", "label": "Français",
        "nav": {"Home":"Accueil","Destinations":"Destinations","About":"À propos","Blog":"Blog","Guides":"Guides"},
        "read_guide": "Lire le Guide →",
        "last_updated": "Dernière mise à jour :",
        "editorial": "Équipe éditoriale, eVisa-Card.com",
        "legal_notice": "Mentions légales",
        "disclaimer": "Avertissement",
        "legal_files": ("mentions-legales.html", "avertissement.html"),
        "expat_guides_label": "Guides Expat",
        "breadcrumb_home": "Accueil",
    },
    "es": {
        "html_lang": "es",
        "flag": "fi-es", "label": "Español",
        "nav": {"Home":"Inicio","Destinations":"Destinos","About":"Acerca de","Blog":"Blog","Guides":"Guías"},
        "read_guide": "Leer la Guía →",
        "last_updated": "Última actualización :",
        "editorial": "Equipo editorial, eVisa-Card.com",
        "legal_notice": "Aviso Legal",
        "disclaimer": "Aviso",
        "legal_files": ("aviso-legal.html", "aviso.html"),
        "expat_guides_label": "Guías Expat",
        "breadcrumb_home": "Inicio",
    },
    "pt": {
        "html_lang": "pt",
        "flag": "fi-br", "label": "Português",
        "nav": {"Home":"Início","Destinations":"Destinos","About":"Sobre","Blog":"Blog","Guides":"Guias"},
        "read_guide": "Ler o Guia →",
        "last_updated": "Última atualização :",
        "editorial": "Equipe editorial, eVisa-Card.com",
        "legal_notice": "Aviso Legal",
        "disclaimer": "Aviso",
        "legal_files": ("aviso-legal.html", "aviso.html"),
        "expat_guides_label": "Guias Expat",
        "breadcrumb_home": "Início",
    },
}

def fix_hero(html):
    """Remove stellar dependency and ftco-animate from hero so it always shows."""
    # Remove data-stellar-background-ratio attribute
    html = re.sub(r'\s*data-stellar-background-ratio="[^"]*"', '', html)
    # Remove ftco-animate from col-md-9 div inside hero
    html = re.sub(r'(<div class="col-md-9[^"]*) ftco-animate(")', r'\1\2', html)
    return html

def transform_eur(html, lang, filename):
    cfg = EUR[lang]
    # 1. html lang
    html = re.sub(r'<html lang="[^"]*">', f'<html lang="{cfg["html_lang"]}">', html)
    # 2. canonical
    html = re.sub(
        r'<link rel="canonical" href="https://www\.evisa-card\.com/en/',
        f'<link rel="canonical" href="https://www.evisa-card.com/{lang}/', html
    )
    # 3. og:url
    html = re.sub(
        r'(<meta property="og:url" content="https://www\.evisa-card\.com/)en/',
        rf'\g<1>{lang}/', html
    )
    # 4. Nav labels
    for en_label, loc_label in cfg["nav"].items():
        html = re.sub(
            rf'(<a class="nav-link[^"]*" href="[^"]*">){en_label}(</a>)',
            rf'\g<1>{loc_label}\2', html
        )
    # 5. Active lang dropdown item
    html = re.sub(
        r'<a class="dropdown-item active" href="/en/' + re.escape(filename) + r'">(<span class="fi fi-gb"></span>) English</a>',
        f'<a class="dropdown-item" href="/en/{filename}">\\1 English</a>', html
    )
    html = re.sub(
        r'<a class="dropdown-item" href="/{lang}/' + re.escape(filename) + r'">(<span class="fi fi-{flag}"></span>) {label}</a>'.format(
            lang=lang, flag=cfg["flag"].replace("fi-",""), label=cfg["label"]
        ),
        f'<a class="dropdown-item active" href="/{lang}/{filename}"><span class="fi {cfg["flag"]}"></span> {cfg["label"]}</a>', html
    )
    # 6. Legal links in footer
    html = re.sub(
        r'href="/en/legal-notice\.html"[^>]*>Legal Notice',
        f'href="/{lang}/{cfg["legal_files"][0]}">{cfg["legal_notice"]}', html
    )
    html = re.sub(
        r'href="/en/disclaimer\.html"[^>]*>Disclaimer',
        f'href="/{lang}/{cfg["legal_files"][1]}">{cfg["disclaimer"]}', html
    )
    # 7. Expat Guides breadcrumb link
    html = html.replace(
        'href="/en/expat-guides.html">Expat Guides',
        f'href="/{lang}/expat-guides.html">{cfg["expat_guides_label"]}'
    )
    # 8. Breadcrumb Home
    html = re.sub(
        r'href="\.\./index\.html">Home ',
        f'href="../index.html">{cfg["breadcrumb_home"]} ', html
    )
    # 9. Last updated / editorial
    html = html.replace('Last updated:', cfg["last_updated"])
    html = html.replace('Editorial Team, eVisa-Card.com', cfg["editorial"])
    # 10. Read the Guide button
    html = html.replace('Read the Guide →', cfg["read_guide"])
    return html

# ── Step 1: Fix all EN expat guide pages (hero + ftco-animate) ────────────────
en_guides = glob.glob(f"{WWW}/en/expat-guide-*.html")
fixed_en = 0
for fp in en_guides:
    with open(fp, encoding="utf-8") as f:
        html = f.read()
    new = fix_hero(html)
    if new != html:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new)
        fixed_en += 1

print(f"Fixed hero on {fixed_en} EN guide pages")

# ── Step 2: Force-regenerate FR/ES/PT from new detailed EN ───────────────────
regen = 0
for en_fp in en_guides:
    filename = os.path.basename(en_fp)
    with open(en_fp, encoding="utf-8") as f:
        en_html = f.read()

    for lang in EUR:
        out_fp = f"{WWW}/{lang}/{filename}"
        new_html = transform_eur(en_html, lang, filename)
        with open(out_fp, "w", encoding="utf-8") as f:
            f.write(new_html)
        regen += 1

print(f"Regenerated {regen} FR/ES/PT guide pages from new detailed EN")
print("DONE")
