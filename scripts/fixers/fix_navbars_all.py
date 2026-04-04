#!/usr/bin/env python3
"""
Standardise toutes les navbars sur EN / FR / ES / PT.
Structure cible : Home | Destinations | About | Blog | Guides | [lang switcher]
"""
import os, re, glob

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

LABELS = {
    "en": {"home": "Home",       "dest": "Destinations", "about": "About",          "blog": "Blog", "guides": "Guides"},
    "fr": {"home": "Accueil",    "dest": "Destinations", "about": "À propos",        "blog": "Blog", "guides": "Guides"},
    "es": {"home": "Inicio",     "dest": "Destinos",     "about": "Sobre Nosotros",  "blog": "Blog", "guides": "Guías"},
    "pt": {"home": "Início",     "dest": "Destinos",     "about": "Sobre Nós",       "blog": "Blog", "guides": "Guias"},
}

FLAG = {"en": "fi-gb", "fr": "fi-fr", "es": "fi-es", "pt": "fi-br"}
LANG_LABEL = {"en": "English", "fr": "Français", "es": "Español", "pt": "Português"}

def make_navbar(lang, page_slug, lang_links):
    """
    lang        : 'en'|'fr'|'es'|'pt'
    page_slug   : e.g. 'visa-thailand' (basename without .html)
    lang_links  : dict {lang: url} for the switcher
    """
    L = LABELS[lang]

    # Nav items
    items = f'''
                <li class="nav-item"><a class="nav-link" href="../index.html">{L["home"]}</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">{L["dest"]}</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">{L["about"]}</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">{L["blog"]}</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/retirement-visa-guide.html">{L["guides"]}</a></li>'''

    # Language switcher dropdown items
    switcher_items = ""
    for tl in ["en", "fr", "es", "pt"]:
        active = ' active' if tl == lang else ''
        url = lang_links.get(tl, "/destination.html")
        switcher_items += f'\n          <a class="dropdown-item{active}" href="{url}"><span class="fi {FLAG[tl]}"></span> {LANG_LABEL[tl]}</a>'

    navbar = f'''<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#ftco-nav" data-toggle="collapse" type="button">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">{items}
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi {FLAG[lang]}"></span> {LANG_LABEL[lang]}</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">{switcher_items}
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>'''
    return navbar


def get_lang_links(page_slug, lang):
    """Determine switcher URLs: if counterpart exists, use it; else fallback /destination.html"""
    links = {}
    for tl in ["en", "fr", "es", "pt"]:
        path = os.path.join(WWW, tl, page_slug + ".html")
        if os.path.exists(path):
            links[tl] = f"/{tl}/{page_slug}.html"
        else:
            links[tl] = "/destination.html"
    return links


fixed = 0
errors = 0

for lang in ["en", "fr", "es", "pt"]:
    pages = glob.glob(os.path.join(WWW, lang, "*.html"))
    for fpath in pages:
        page_slug = os.path.basename(fpath).replace(".html", "")
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                html = f.read()

            # Find existing <nav...> ... </nav>
            m = re.search(r'<nav\s[^>]*ftco_navbar[^>]*>.*?</nav>', html, re.DOTALL)
            if not m:
                continue

            lang_links = get_lang_links(page_slug, lang)
            new_nav = make_navbar(lang, page_slug, lang_links)
            html_new = html[:m.start()] + new_nav + html[m.end():]

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html_new)
            fixed += 1

        except Exception as e:
            print(f"ERROR {fpath}: {e}")
            errors += 1

print(f"Fixed: {fixed} pages | Errors: {errors}")
