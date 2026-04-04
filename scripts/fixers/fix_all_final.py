#!/usr/bin/env python3
"""
Fix final complet :
1. index.html : col-md-4 → col-md-3 (4 colonnes)
2. Créer fr/destination.html, es/destination.html, pt/destination.html
3. Mettre à jour switcher langue sur pages racines → pointe vers la bonne langue
4. Header + footer IDENTIQUES sur toutes les pages (par langue)
"""
import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

# ─── 1. Fix index.html : col-md-4 → col-md-3 ────────────────────────────────
with open(os.path.join(WWW, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('col-md-4 ftco-animate', 'col-md-3 col-sm-6 ftco-animate')
html = html.replace('"col-md-4"', '"col-md-3 col-sm-6"')

with open(os.path.join(WWW, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print(f"index.html: col-md-4→col-md-3, count={html.count('col-md-3')}")


# ─── Helper: standard navbar per lang ───────────────────────────────────────
LABELS = {
    "en": ("Home","Destinations","About","Blog","Guides","English","fi-gb"),
    "fr": ("Accueil","Destinations","À propos","Blog","Guides","Français","fi-fr"),
    "es": ("Inicio","Destinos","Sobre Nosotros","Blog","Guías","Español","fi-es"),
    "pt": ("Início","Destinos","Sobre Nós","Blog","Guias","Português","fi-br"),
}
LANG_FLAGS = {"en":"fi-gb","fr":"fi-fr","es":"fi-es","pt":"fi-br"}
LANG_NAMES = {"en":"English","fr":"Français","es":"Español","pt":"Português"}

# For root pages use absolute paths; for lang subpages use ../
def make_navbar(lang, is_root=False, page_slug=None):
    home, dest, about, blog, guides, cur_label, flag = LABELS[lang]
    prefix = "/" if is_root else "../"

    # Determine switcher links
    if is_root:
        switcher = {
            "en": "/",
            "fr": "/fr/destination.html",
            "es": "/es/destination.html",
            "pt": "/pt/destination.html",
        }
    else:
        # For subpages, link to same slug in other lang if exists, else /XX/destination.html
        switcher = {}
        for tl in ["en","fr","es","pt"]:
            if page_slug:
                p = os.path.join(WWW, tl, page_slug + ".html")
                switcher[tl] = f"/{tl}/{page_slug}.html" if os.path.exists(p) else f"/{tl}/destination.html" if tl != "en" else "/destination.html"
            else:
                switcher[tl] = f"/{tl}/destination.html" if tl != "en" else "/destination.html"

    items_html = f"""
                <li class="nav-item"><a class="nav-link" href="{prefix}index.html">{home}</a></li>
                <li class="nav-item"><a class="nav-link" href="{prefix}destination.html">{dest}</a></li>
                <li class="nav-item"><a class="nav-link" href="{prefix}about.html">{about}</a></li>
                <li class="nav-item"><a class="nav-link" href="{prefix}blog.html">{blog}</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/retirement-visa-guide.html">{guides}</a></li>"""

    sw_items = ""
    for tl in ["en","fr","es","pt"]:
        active = ' active' if tl == lang else ''
        sw_items += f'\n                        <a class="dropdown-item{active}" href="{switcher[tl]}"><span class="fi {LANG_FLAGS[tl]}"></span> {LANG_NAMES[tl]}</a>'

    return f"""<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="{prefix}index.html">eVisa-Card<span>.com</span></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">{items_html}
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi {flag}"></span> {cur_label}</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">{sw_items}
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""


# ─── Helper: standard footer per lang ───────────────────────────────────────
FOOTER_DATA = {
    "en": ("© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform",
           '/en/legal-notice.html','Legal Notice','/en/disclaimer.html','Disclaimer','../images/bg_3.jpg'),
    "fr": ("© 2026 eVisa-Card.com — Plateforme mondiale d'information eVisa",
           '/fr/mentions-legales.html','Mentions légales','/fr/disclaimer.html','Disclaimer','../images/bg_3.jpg'),
    "es": ("© 2026 eVisa-Card.com — Plataforma global de información eVisa",
           '/es/aviso-legal.html','Aviso Legal','/es/disclaimer.html','Disclaimer','../images/bg_3.jpg'),
    "pt": ("© 2026 eVisa-Card.com — Plataforma global de informações eVisa",
           '/pt/aviso-legal.html','Aviso Legal','/pt/disclaimer.html','Disclaimer','../images/bg_3.jpg'),
    "root": ("© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform",
             '/en/legal-notice.html','Legal Notice','/en/disclaimer.html','Disclaimer','images/bg_3.jpg'),
}

def make_footer(lang):
    copy, u1, l1, u2, l2, img = FOOTER_DATA.get(lang, FOOTER_DATA["root"])
    return f"""<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url({img});">
        <div class="container">
            <div class="row mb-5 justify-content-center">
                <div class="col-md-6 text-center">
                    <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                    <ul class="ftco-footer-social list-unstyled float-md-center mt-3">
                        <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                        <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                        <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                    </ul>
                    <p class="mt-4">{copy}</p>
                    <p class="mt-2" style="font-size:13px;">
                        <a href="{u1}" style="color:rgba(255,255,255,0.7);text-decoration:none;">{l1}</a>
                        &nbsp;|&nbsp;
                        <a href="{u2}" style="color:rgba(255,255,255,0.7);text-decoration:none;">{l2}</a>
                    </p>
                </div>
            </div>
        </div>
    </footer>"""


# ─── 2. Apply uniform header+footer on ALL pages ─────────────────────────────
fixed = errors = 0

# Root pages
for fpath in glob.glob(os.path.join(WWW, "*.html")):
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        # Navbar
        m = re.search(r'<nav\s[^>]*ftco_navbar[^>]*>.*?</nav>', html, re.DOTALL)
        if m:
            html = html[:m.start()] + make_navbar("en", is_root=True) + html[m.end():]
        # Footer
        m2 = re.search(r'<footer[^>]*>.*?</footer>', html, re.DOTALL)
        if m2:
            html = html[:m2.start()] + make_footer("root") + html[m2.end():]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        fixed += 1
    except Exception as e:
        print(f"ERR root {os.path.basename(fpath)}: {e}")
        errors += 1

# Lang subpages
for lang in ["en","fr","es","pt"]:
    for fpath in glob.glob(os.path.join(WWW, lang, "*.html")):
        try:
            slug = os.path.basename(fpath).replace(".html","")
            with open(fpath, "r", encoding="utf-8") as f:
                html = f.read()
            m = re.search(r'<nav\s[^>]*ftco_navbar[^>]*>.*?</nav>', html, re.DOTALL)
            if m:
                html = html[:m.start()] + make_navbar(lang, is_root=False, page_slug=slug) + html[m.end():]
            m2 = re.search(r'<footer[^>]*>.*?</footer>', html, re.DOTALL)
            if m2:
                html = html[:m2.start()] + make_footer(lang) + html[m2.end():]
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            fixed += 1
        except Exception as e:
            print(f"ERR {lang}/{os.path.basename(fpath)}: {e}")
            errors += 1

print(f"Header+footer fixed: {fixed} pages | Errors: {errors}")


# ─── 3. Create fr/destination.html, es/destination.html, pt/destination.html ─
with open(os.path.join(WWW, "destination.html"), "r", encoding="utf-8") as f:
    dest_en = f.read()

DEST_LABELS = {
    "fr": {"title":"Destinations eVisa — Guide Visa Mondial | eVisa-Card.com",
           "h1":"Guide Visa Mondial — 48 Pays",
           "breadcrumb":"Toutes les Destinations",
           "desc":"Explorez les exigences de visa pour 48 pays. Informations sur les eVisas, visas à l'arrivée et exemptions de visa."},
    "es": {"title":"Destinos eVisa — Guía de Visas Mundial | eVisa-Card.com",
           "h1":"Guía de Visas Mundial — 48 Países",
           "breadcrumb":"Todos los Destinos",
           "desc":"Explora los requisitos de visa para 48 países. Información sobre eVisas, visas a la llegada y exenciones de visa."},
    "pt": {"title":"Destinos eVisa — Guia de Vistos Mundial | eVisa-Card.com",
           "h1":"Guia de Vistos Mundial — 48 Países",
           "breadcrumb":"Todos os Destinos",
           "desc":"Explore os requisitos de visto para 48 países. Informações sobre eVisas, vistos na chegada e isenções de visto."},
}

for lang, labels in DEST_LABELS.items():
    html = dest_en

    # Fix title
    html = re.sub(r'<title>.*?</title>', f'<title>{labels["title"]}</title>', html)

    # Fix html lang
    html = re.sub(r'<html lang="[^"]*">', f'<html lang="{lang}">', html)

    # Fix h1 breadcrumb
    html = re.sub(r'<h1 class="mb-0 bread">.*?</h1>', f'<h1 class="mb-0 bread">{labels["h1"]}</h1>', html)
    html = re.sub(r'<span>All Destinations.*?</span>', f'<span>{labels["breadcrumb"]} <i class="fa fa-chevron-right"></i></span>', html)

    # Fix canonical + hreflang
    html = re.sub(r'<link[^>]*rel="canonical"[^>]*>', f'<link rel="canonical" href="https://www.evisa-card.com/{lang}/destination.html"/>', html)

    # Apply lang navbar + footer
    m = re.search(r'<nav\s[^>]*ftco_navbar[^>]*>.*?</nav>', html, re.DOTALL)
    if m:
        html = html[:m.start()] + make_navbar(lang, is_root=False, page_slug="destination") + html[m.end():]
    m2 = re.search(r'<footer[^>]*>.*?</footer>', html, re.DOTALL)
    if m2:
        html = html[:m2.start()] + make_footer(lang) + html[m2.end():]

    # Fix all card links: /en/visa-X.html → /lang/visa-X.html
    html = re.sub(r'/en/(visa-[a-z0-9-]+\.html)', f'/{lang}/\\1', html)

    # Fix image paths (root uses images/, subdir uses ../images/)
    html = html.replace('url(images/', 'url(../images/')
    html = html.replace('src="images/', 'src="../images/')

    out_path = os.path.join(WWW, lang, "destination.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {lang}/destination.html")

print("DONE")
