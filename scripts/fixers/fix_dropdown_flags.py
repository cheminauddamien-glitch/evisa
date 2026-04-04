#!/usr/bin/env python3
"""
fix_dropdown_flags.py
Fix the language dropdown flags/labels on zh/th/ru/ar/ja/ko pages.
The EN dropdown item wrongly shows the current lang's flag+label instead of fi-gb English.
"""
import os, re, glob

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
LANGS_TO_FIX = ["zh", "th", "ru", "ar", "ja", "ko"]

# Expected flag+label for each language link in the dropdown
EXPECTED = {
    "en": ("fi-gb", "English"),
    "fr": ("fi-fr", "Fran"),  # Match partial to catch Francais/Français
    "es": ("fi-es", "Espa"),  # Espanol/Español
    "pt": ("fi-br", "Portugu"),
    "zh": ("fi-cn", ""),
    "th": ("fi-th", ""),
    "ru": ("fi-ru", ""),
    "ar": ("fi-sa", ""),
    "ja": ("fi-jp", ""),
    "ko": ("fi-kr", ""),
}


def fix_file(filepath, current_lang):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    original = html
    filename = os.path.basename(filepath)

    # Fix the EN dropdown item: it should show fi-gb English
    # Current bug: shows current lang's flag+label with /en/ link
    # Pattern: href="/en/{filename}"><span class="fi fi-{WRONG}"></span> {WRONG_LABEL}</a>

    # Fix EN link in dropdown
    html = re.sub(
        r'(href="/en/' + re.escape(filename) + r'"[^>]*>)\s*<span class="fi fi-[a-z]+"></span>\s*[^<]*</a>',
        r'\1<span class="fi fi-gb"></span> English</a>',
        html
    )

    # Also fix any other language links that might have wrong flags
    for lang, (flag, _) in EXPECTED.items():
        if lang == current_lang:
            continue
        # Fix: href="/{lang}/{filename}" should have the correct flag
        pattern = r'(href="/' + lang + r'/' + re.escape(filename) + r'"[^>]*>)\s*<span class="fi fi-[a-z]+"></span>'
        replacement = r'\1<span class="fi ' + flag + r'"></span>'
        html = re.sub(pattern, replacement, html)

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
