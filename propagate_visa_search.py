#!/usr/bin/env python3
"""
propagate_visa_search.py
Add the visa search form container + script tag to all language homepage/destination pages.
"""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"

# Files to update per language
LANG_FILES = {
    "fr": ["fr/index.html", "fr/destination.html"],
    "es": ["es/index.html", "es/destination.html"],
    "pt": ["pt/index.html", "pt/destination.html"],
    "zh": ["zh/destination.html"],
    "th": ["th/destination.html"],
    "ru": ["ru/destination.html"],
    "ar": ["ar/destination.html"],
    "ja": ["ja/destination.html"],
    "ko": ["ko/destination.html"],
}

def add_form_to_page(filepath):
    """Add visa search container and script to a page."""
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    if "visa-search-container" in html:
        return False  # Already has it

    modified = False

    # 1. Add container div in hero section (after <p class="lead"> or after <h1>)
    # Look for the hero section pattern
    # Try to insert after the lead paragraph
    lead_pattern = r'(<p class="lead[^"]*">[^<]*</p>)'
    match = re.search(lead_pattern, html)
    if match:
        insert_pos = match.end()
        html = html[:insert_pos] + '\n                    <!-- Visa Search Form -->\n                    <div id="visa-search-container" class="mb-4"></div>' + html[insert_pos:]
        modified = True
    else:
        # Try after h1
        h1_pattern = r'(</h1>)'
        match = re.search(h1_pattern, html)
        if match:
            insert_pos = match.end()
            html = html[:insert_pos] + '\n                    <!-- Visa Search Form -->\n                    <div id="visa-search-container" class="mb-4"></div>' + html[insert_pos:]
            modified = True

    # 2. Add visa-search.js script tag before </body> or after main.js
    if "visa-search.js" not in html:
        # Try after main.js
        if '../js/main.js">' in html:
            html = html.replace(
                '../js/main.js"></script>',
                '../js/main.js"></script>\n<script src="../js/visa-search.js"></script>'
            )
            modified = True
        elif 'js/main.js">' in html:
            html = html.replace(
                'js/main.js"></script>',
                'js/main.js"></script>\n<script src="../js/visa-search.js"></script>'
            )
            modified = True
        elif '</body>' in html:
            html = html.replace(
                '</body>',
                '<script src="../js/visa-search.js"></script>\n</body>'
            )
            modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    total = 0
    updated = 0

    for lang, files in LANG_FILES.items():
        for rel_path in files:
            filepath = os.path.join(BASE, rel_path)
            if not os.path.isfile(filepath):
                continue
            total += 1
            if add_form_to_page(filepath):
                updated += 1
                print(f"  OK {rel_path}")

    print(f"\nDone: {updated}/{total} language pages updated with visa search form.")


if __name__ == "__main__":
    main()
