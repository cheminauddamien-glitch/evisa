#!/usr/bin/env python3
"""Fix navigation links across all pages in www/ and fix blog.html language switcher.

Ensures consistent nav: Home | Destinations | Blog | Guides | About | [Lang]
With correct links per language directory.
"""
import os, re, glob

WWW = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "www")

LANGS = ["en", "fr", "es", "pt", "ar", "ja", "ko", "ru", "th", "zh"]

# Nav labels per language
NAV = {
    "en":  {"home": "Home",     "dest": "Destinations", "blog": "Blog",     "guides": "Guides",    "about": "About"},
    "fr":  {"home": "Accueil",  "dest": "Destinations", "blog": "Blog",     "guides": "Guides",    "about": "\u00c0 propos"},
    "es":  {"home": "Inicio",   "dest": "Destinos",     "blog": "Blog",     "guides": "Gu\u00edas","about": "Acerca de"},
    "pt":  {"home": "In\u00edcio","dest": "Destinos",   "blog": "Blog",     "guides": "Guias",     "about": "Sobre"},
    "ar":  {"home": "\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629","dest": "\u0627\u0644\u0648\u062c\u0647\u0627\u062a","blog": "\u0627\u0644\u0645\u062f\u0648\u0646\u0629","guides": "\u0623\u062f\u0644\u0629","about": "\u0639\u0646 \u0627\u0644\u0645\u0648\u0642\u0639"},
    "ja":  {"home": "\u30db\u30fc\u30e0","dest": "\u76ee\u7684\u5730","blog": "\u30d6\u30ed\u30b0","guides": "\u30ac\u30a4\u30c9","about": "\u6982\u8981"},
    "ko":  {"home": "\ud648",   "dest": "\ubaa9\uc801\uc9c0","blog": "\ube14\ub85c\uadf8","guides": "\uac00\uc774\ub4dc","about": "\uc18c\uac1c"},
    "ru":  {"home": "\u0413\u043b\u0430\u0432\u043d\u0430\u044f","dest": "\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f","blog": "\u0411\u043b\u043e\u0433","guides": "\u0413\u0438\u0434\u044b","about": "\u041e \u043d\u0430\u0441"},
    "th":  {"home": "\u0e2b\u0e19\u0e49\u0e32\u0e41\u0e23\u0e01","dest": "\u0e08\u0e38\u0e14\u0e2b\u0e21\u0e32\u0e22","blog": "\u0e1a\u0e25\u0e47\u0e2d\u0e01","guides": "\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d","about": "\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a"},
    "zh":  {"home": "\u9996\u9875","dest": "\u76ee\u7684\u5730","blog": "\u535a\u5ba2","guides": "\u6307\u5357","about": "\u5173\u4e8e"},
}

# Language flag emojis
FLAGS = {
    "en": "\U0001f1ec\U0001f1e7", "fr": "\U0001f1eb\U0001f1f7", "es": "\U0001f1ea\U0001f1f8",
    "pt": "\U0001f1e7\U0001f1f7", "ar": "\U0001f1f8\U0001f1e6", "ja": "\U0001f1ef\U0001f1f5",
    "ko": "\U0001f1f0\U0001f1f7", "ru": "\U0001f1f7\U0001f1fa", "th": "\U0001f1f9\U0001f1ed",
    "zh": "\U0001f1e8\U0001f1f3"
}

LANG_NAMES = {
    "en": "English", "fr": "Fran\u00e7ais", "es": "Espa\u00f1ol", "pt": "Portugu\u00eas",
    "ar": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629", "ja": "\u65e5\u672c\u8a9e",
    "ko": "\ud55c\uad6d\uc5b4", "ru": "\u0420\u0443\u0441\u0441\u043a\u0438\u0439",
    "th": "\u0e44\u0e17\u0e22", "zh": "\u4e2d\u6587"
}


def get_lang_for_file(filepath):
    """Determine language from file path."""
    rel = os.path.relpath(filepath, WWW).replace("\\", "/")
    parts = rel.split("/")
    if len(parts) >= 2 and parts[0] in LANGS:
        return parts[0]
    return "en"  # root-level pages default to EN


def build_nav_html(lang, is_subdir):
    """Build the correct nav <ul> content for a given language."""
    prefix = f"/{lang}" if is_subdir else ""

    # Home link
    if is_subdir:
        home_href = f"/{lang}/index.html" if lang != "en" else "/index.html"
    else:
        home_href = "/index.html"

    # Destinations link
    if is_subdir and lang != "en":
        dest_href = f"/{lang}/destination.html"
    else:
        dest_href = "/destination.html"

    # Blog link (blog.html is at root, no translated versions yet)
    blog_href = "/blog.html"

    # Guides link
    guides_href = f"/{lang}/expat-guides.html"

    # About link
    about_href = f"/{lang}/about-our-experts.html" if is_subdir else "/en/about-our-experts.html"

    n = NAV.get(lang, NAV["en"])

    nav_items = f'''                    <li class="nav-item"><a class="nav-link" href="{home_href}">{n["home"]}</a></li>
                    <li class="nav-item"><a class="nav-link" href="{dest_href}">{n["dest"]}</a></li>
                    <li class="nav-item"><a class="nav-link" href="{blog_href}">{n["blog"]}</a></li>
                    <li class="nav-item"><a class="nav-link" href="{guides_href}">{n["guides"]}</a></li>
                    <li class="nav-item"><a class="nav-link" href="{about_href}">{n["about"]}</a></li>'''

    return nav_items


def build_lang_dropdown(lang, filename):
    """Build language dropdown for a page."""
    flag = FLAGS.get(lang, FLAGS["en"])
    name = LANG_NAMES.get(lang, "English")

    items = []
    for l in LANGS:
        l_flag = FLAGS[l]
        l_name = LANG_NAMES[l]
        active = ' active' if l == lang else ''

        # Determine href for this language version
        if l == "en" and filename in ("index.html", "destination.html", "blog.html", "contact.html", "about.html", "404.html"):
            href = f"/{filename}"
        elif filename in ("index.html", "destination.html"):
            href = f"/{l}/{filename}"
        elif filename == "blog.html":
            href = f"/blog.html"  # no translated blog yet
        else:
            href = f"/{l}/{filename}"

        items.append(f'          <a class="dropdown-item{active}" href="{href}">{l_flag} {l_name}</a>')

    dropdown = f'''                <li class="nav-item dropdown ml-3">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">{flag} {name}</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
{chr(10).join(items)}
                    </div>
                </li>'''

    return dropdown


def replace_nav(content, lang, filename, is_subdir):
    """Replace the entire nav <ul> block with correct links."""
    # Find the navbar-nav block (handles both ml-auto and align-items-center variants)
    pattern = r'(<ul\s+class="navbar-nav[^"]*">)\s*\n(.*?)(</ul>)'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return content, False

    nav_items = build_nav_html(lang, is_subdir)
    lang_dropdown = build_lang_dropdown(lang, filename)

    # Preserve original ul class attribute
    original_ul = match.group(1)
    new_nav = f'''{original_ul}
{nav_items}
{lang_dropdown}
          </ul>'''

    content = content[:match.start()] + new_nav + content[match.end():]
    return content, True


def process_file(filepath):
    """Process a single HTML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if '<ul class="navbar-nav' not in content:
        return False

    lang = get_lang_for_file(filepath)
    filename = os.path.basename(filepath)
    rel = os.path.relpath(filepath, WWW).replace("\\", "/")
    is_subdir = "/" in rel and rel.split("/")[0] in LANGS

    new_content, changed = replace_nav(content, lang, filename, is_subdir)

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def main():
    count = 0
    errors = 0

    # Process root-level HTML files
    for fname in os.listdir(WWW):
        if not fname.endswith(".html"):
            continue
        filepath = os.path.join(WWW, fname)
        if os.path.isfile(filepath):
            try:
                if process_file(filepath):
                    count += 1
            except Exception as e:
                print(f"  ERROR {filepath}: {e}")
                errors += 1

    # Process language directories
    for lang in LANGS:
        lang_dir = os.path.join(WWW, lang)
        if not os.path.isdir(lang_dir):
            continue
        for fname in os.listdir(lang_dir):
            if not fname.endswith(".html"):
                continue
            filepath = os.path.join(lang_dir, fname)
            try:
                if process_file(filepath):
                    count += 1
            except Exception as e:
                print(f"  ERROR {filepath}: {e}")
                errors += 1

    print(f"\nDone: {count} pages updated, {errors} errors")


if __name__ == "__main__":
    main()
