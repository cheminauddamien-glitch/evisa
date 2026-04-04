#!/usr/bin/env python3
"""
Add zh/th/ru/ar/ja/ko hreflang to all pages that have matching files in those dirs.
Also fix lang switcher on visa-*.html pages in EN to point to actual visa pages.
"""
import os, re

BASE = r"C:/Users/chemi/Documents/evisa/pacific-main/www"
ALL_LANGS = ["en","fr","es","pt","zh","th","ru","ar","ja","ko"]
NEW_LANGS = ["zh","th","ru","ar","ja","ko"]

def get_existing_langs(slug, filename):
    """Return list of langs where this file exists."""
    langs = []
    for lang in ALL_LANGS:
        path = os.path.join(BASE, lang, filename)
        if os.path.exists(path):
            langs.append(lang)
    return langs

def build_hreflang_block(filename, existing_langs):
    """Build hreflang link tags."""
    lines = []
    for lang in existing_langs:
        url = f"https://www.evisa-card.com/{lang}/{filename}"
        lines.append(f'    <link rel="alternate" hreflang="{lang}" href="{url}"/>')
    # x-default → en
    if "en" in existing_langs:
        lines.append(f'    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{filename}"/>')
    return "\n".join(lines)

def update_hreflang(html, filename, existing_langs):
    """Remove old hreflang tags and insert new complete block."""
    # Remove all existing hreflang tags
    html = re.sub(r'[ \t]*<link[^>]+hreflang[^>]+/?>\n?', '', html)
    # Build new block
    new_block = build_hreflang_block(filename, existing_langs)
    if not new_block:
        return html
    # Insert before </head>
    html = html.replace('</head>', new_block + '\n</head>', 1)
    return html

def fix_lang_switcher_visa(html, slug, lang):
    """
    Fix language switcher links: for visa-*.html pages in new langs,
    point to actual visa page instead of destination.html.
    """
    for nl in NEW_LANGS:
        # Replace /nl/destination.html with /nl/visa-{slug}.html
        old = f'href="/{nl}/destination.html"'
        new = f'href="/{nl}/visa-{slug}.html"'
        html = html.replace(old, new)
    return html

updated = 0
skipped = 0

# Process en/ visa-*.html: update hreflang + fix lang switcher for new langs
en_dir = os.path.join(BASE, "en")
for fname in os.listdir(en_dir):
    if not fname.endswith(".html"):
        continue
    path = os.path.join(en_dir, fname)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    existing_langs = get_existing_langs(fname, fname)
    if len(existing_langs) <= 1:
        skipped += 1
        continue

    # Check if all langs already present
    current_hreflang = re.findall(r'hreflang="([^"]+)"', html)
    new_langs_needed = [l for l in existing_langs if l not in current_hreflang and l != "x-default"]
    if not new_langs_needed and all(l in current_hreflang for l in existing_langs):
        skipped += 1
        continue

    new_html = update_hreflang(html, fname, existing_langs)

    # Fix visa-*.html lang switcher for new langs
    if fname.startswith("visa-") and not any(x in fname for x in ["visa-free","visa-photo","visa-processing","visa-documents","visa-rejection"]):
        slug = fname.replace("visa-","").replace(".html","")
        new_html = fix_lang_switcher_visa(new_html, slug, "en")

    if new_html != html:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        updated += 1

print(f"EN dir: {updated} updated, {skipped} skipped")

# Process all other language dirs
for lang in ["fr","es","pt","zh","th","ru","ar","ja","ko"]:
    lang_dir = os.path.join(BASE, lang)
    if not os.path.isdir(lang_dir):
        continue
    lang_updated = 0
    for fname in os.listdir(lang_dir):
        if not fname.endswith(".html"):
            continue
        path = os.path.join(lang_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()

        existing_langs = get_existing_langs(fname, fname)
        if len(existing_langs) <= 1:
            continue

        current_hreflang = re.findall(r'hreflang="([^"]+)"', html)
        if all(l in current_hreflang for l in existing_langs):
            continue  # already has all langs

        new_html = update_hreflang(html, fname, existing_langs)

        if new_html != html:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_html)
            lang_updated += 1

    print(f"  {lang}/: {lang_updated} updated")
    updated += lang_updated

print(f"\nDONE — Total {updated} pages updated with hreflang")
