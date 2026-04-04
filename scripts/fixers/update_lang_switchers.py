#!/usr/bin/env python3
"""
Update language switcher dropdowns to add 6 new languages (zh/th/ru/ar/ja/ko)
to HTML files that still have only 4 languages (en/fr/es/pt).
"""
import os
import re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"

# Files confirmed to be missing the new 6 language options
TARGET_FILES = [
    r"destination.html",
    r"fr\destination.html",
    r"fr\china-visa-processing-time.html",
    r"fr\china-visa-requirements.html",
    r"fr\visa-free-countries-japan-passport.html",
    r"fr\visa-free-countries-uae-passport.html",
    r"es\destination.html",
    r"es\china-visa-processing-time.html",
    r"es\china-visa-requirements.html",
    r"es\visa-free-countries-japan-passport.html",
    r"es\visa-free-countries-uae-passport.html",
    r"pt\destination.html",
    r"pt\china-visa-processing-time.html",
    r"pt\china-visa-requirements.html",
    r"pt\visa-free-countries-japan-passport.html",
    r"pt\visa-free-countries-uae-passport.html",
]

NEW_LANG_ITEMS = """                        <a class="dropdown-item" href="/zh/destination.html"><span class="fi fi-cn"></span> 中文</a>
                        <a class="dropdown-item" href="/th/destination.html"><span class="fi fi-th"></span> ไทย</a>
                        <a class="dropdown-item" href="/ru/destination.html"><span class="fi fi-ru"></span> Русский</a>
                        <a class="dropdown-item" href="/ar/destination.html"><span class="fi fi-sa"></span> العربية</a>
                        <a class="dropdown-item" href="/ja/destination.html"><span class="fi fi-jp"></span> 日本語</a>
                        <a class="dropdown-item" href="/ko/destination.html"><span class="fi fi-kr"></span> 한국어</a>"""

# Match the Português dropdown-item line (href varies), capturing it
PT_PATTERN = re.compile(
    r'(<a class="dropdown-item[^"]*"[^>]*href="[^"]*"[^>]*><span class="fi fi-br"></span> Portugu[^<]+</a>)',
    re.DOTALL
)

updated = 0
skipped = 0

for rel_path in TARGET_FILES:
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        print(f"  MISSING: {rel_path}")
        skipped += 1
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already updated
    if "中文" in content:
        print(f"  ALREADY OK: {rel_path}")
        skipped += 1
        continue

    # Find the Português item and insert new languages after it
    match = PT_PATTERN.search(content)
    if not match:
        print(f"  NO MATCH (Português item not found): {rel_path}")
        skipped += 1
        continue

    pt_item = match.group(1)
    replacement = pt_item + "\n" + NEW_LANG_ITEMS
    new_content = content.replace(pt_item, replacement, 1)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  UPDATED: {rel_path}")
    updated += 1

print(f"\nDone. Updated: {updated}, Skipped/already-done: {skipped}")
