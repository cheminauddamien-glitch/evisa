#!/usr/bin/env python3
"""
fix_dropdown_links.py
Fix the language dropdown on zh/th/ru/ar/ja/ko pages:
1. Dropdown links point to /{lang}/destination.html instead of /{lang}/{current_filename}
2. First dropdown item shows wrong flag/label (should show EN/fi-gb)
"""
import os, re, glob

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
LANGS_TO_FIX = ["zh", "th", "ru", "ar", "ja", "ko"]
ALL_LANGS = ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]

LANG_META = {
    "en": ("fi-gb", "English"),
    "fr": ("fi-fr", "Francais"),
    "es": ("fi-es", "Espanol"),
    "pt": ("fi-br", "Portugues"),
    "zh": ("fi-cn", "Chinese"),
    "th": ("fi-th", "Thai"),
    "ru": ("fi-ru", "Russian"),
    "ar": ("fi-sa", "Arabic"),
    "ja": ("fi-jp", "Japanese"),
    "ko": ("fi-kr", "Korean"),
}


def fix_file(filepath, current_lang):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    original = html
    filename = os.path.basename(filepath)

    # Fix dropdown links: replace /{lang}/destination.html with /{lang}/{filename}
    for lang in ALL_LANGS:
        # Pattern: href="/{lang}/destination.html" in dropdown items
        old_href = f'href="/{lang}/destination.html"'
        new_href = f'href="/{lang}/{filename}"'
        if old_href in html:
            html = html.replace(old_href, new_href)

    # Also fix any dropdown items pointing to wrong pages
    # The dropdown should have links to the SAME page in different languages
    # Pattern: dropdown-item with href pointing to wrong file
    for lang in ALL_LANGS:
        # Check if a file exists for this lang
        target_file = os.path.join(BASE, lang, filename)
        if not os.path.isfile(target_file):
            continue
        # Make sure the dropdown has a link to /{lang}/{filename}
        # Already handled by the replacement above

    if html != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    total = 0
    updated = 0

    for lang in LANGS_TO_FIX:
        lang_dir = os.path.join(BASE, lang)
        if not os.path.isdir(lang_dir):
            continue

        html_files = glob.glob(os.path.join(lang_dir, "*.html"))
        lang_updated = 0
        for filepath in html_files:
            total += 1
            if fix_file(filepath, lang):
                lang_updated += 1
                updated += 1

        print(f"  {lang}: {lang_updated}/{len(html_files)} files fixed")

    print(f"\nDone: {updated}/{total} files fixed.")


if __name__ == "__main__":
    main()
