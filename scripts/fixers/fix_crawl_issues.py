#!/usr/bin/env python3
"""
fix_crawl_issues.py
Fix all issues found by the full crawl audit:
1. Fix canonical URLs on non-EN pages (must point to own language, not /en/)
2. Fix legal/disclaimer links (fr->mentions-legales, es/pt->aviso-legal)
3. Fix visa-dubai -> visa-uae links
"""
import os, re, glob

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
LANGS = ["fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]

# Legal page mappings
LEGAL_LINKS = {
    "fr": {"legal": "mentions-legales.html", "disclaimer": "mentions-legales.html"},
    "es": {"legal": "aviso-legal.html", "disclaimer": "aviso-legal.html"},
    "pt": {"legal": "aviso-legal.html", "disclaimer": "aviso-legal.html"},
}


def fix_canonical(html, lang, filename):
    """Fix canonical URL to point to correct language."""
    # Replace canonical pointing to /en/ with correct lang
    html = re.sub(
        r'(rel="canonical"\s+href="https://www\.evisa-card\.com)/en/([^"]*")',
        rf'\1/{lang}/\2',
        html
    )
    html = re.sub(
        r'(href="https://www\.evisa-card\.com)/en/([^"]*"\s+rel="canonical")',
        rf'\1/{lang}/\2',
        html
    )
    return html


def fix_legal_links(html, lang):
    """Fix legal notice and disclaimer links for non-EN languages."""
    # Fix /fr/legal-notice.html -> /fr/mentions-legales.html etc.
    if lang == "fr":
        html = html.replace(f'/{lang}/legal-notice.html', f'/{lang}/mentions-legales.html')
        html = html.replace(f'/{lang}/disclaimer.html', f'/{lang}/mentions-legales.html')
        html = html.replace(f'/{lang}/avertissement.html', f'/{lang}/mentions-legales.html')
    elif lang in ("es", "pt"):
        html = html.replace(f'/{lang}/legal-notice.html', f'/{lang}/aviso-legal.html')
        html = html.replace(f'/{lang}/disclaimer.html', f'/{lang}/aviso-legal.html')
        html = html.replace(f'/{lang}/aviso.html', f'/{lang}/aviso-legal.html')
    return html


def fix_dubai_link(html):
    """Fix visa-dubai.html -> visa-uae.html."""
    html = html.replace('visa-dubai.html', 'visa-uae.html')
    return html


def process_file(filepath, lang):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    original = html
    filename = os.path.basename(filepath)

    # 1. Fix canonical
    html = fix_canonical(html, lang, filename)

    # 2. Fix legal links
    html = fix_legal_links(html, lang)

    # 3. Fix dubai links
    html = fix_dubai_link(html)

    if html != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    total = 0
    updated = 0

    for lang in LANGS:
        lang_dir = os.path.join(BASE, lang)
        if not os.path.isdir(lang_dir):
            continue

        html_files = glob.glob(os.path.join(lang_dir, "*.html"))
        lang_updated = 0
        for filepath in html_files:
            total += 1
            if process_file(filepath, lang):
                lang_updated += 1
                updated += 1

        print(f"  {lang}: {lang_updated}/{len(html_files)} files fixed")

    # Also fix EN pages for dubai link
    en_dir = os.path.join(BASE, "en")
    en_files = glob.glob(os.path.join(en_dir, "*.html"))
    en_updated = 0
    for filepath in en_files:
        total += 1
        with open(filepath, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        original = html
        html = fix_dubai_link(html)
        if html != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            en_updated += 1
            updated += 1
    print(f"  en: {en_updated}/{len(en_files)} files fixed (dubai only)")

    print(f"\nDone: {updated}/{total} files fixed.")


if __name__ == "__main__":
    main()
