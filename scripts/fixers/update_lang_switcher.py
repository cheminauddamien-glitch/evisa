#!/usr/bin/env python3
"""
update_lang_switcher.py
Updates the language switcher dropdown on ALL existing pages (en/fr/es/pt + root)
to include zh / th / ru / ar / ja / ko.
"""
import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

# New items to append inside the existing dropdown
NEW_LANG_ITEMS = """                        <a class="dropdown-item" href="/zh/destination.html"><span class="fi fi-cn"></span> 中文</a>
                        <a class="dropdown-item" href="/th/destination.html"><span class="fi fi-th"></span> ไทย</a>
                        <a class="dropdown-item" href="/ru/destination.html"><span class="fi fi-ru"></span> Русский</a>
                        <a class="dropdown-item" href="/ar/destination.html"><span class="fi fi-sa"></span> العربية</a>
                        <a class="dropdown-item" href="/ja/destination.html"><span class="fi fi-jp"></span> 日本語</a>
                        <a class="dropdown-item" href="/ko/destination.html"><span class="fi fi-kr"></span> 한국어</a>"""

# Closing tag of the dropdown menu — we insert before it
CLOSING = '                    </div>'

def already_updated(html):
    return 'fi-cn' in html or '中文' in html

fixed = 0
errors = 0
skipped = 0

all_pages = (
    glob.glob(os.path.join(WWW, "*.html")) +
    glob.glob(os.path.join(WWW, "en", "*.html")) +
    glob.glob(os.path.join(WWW, "fr", "*.html")) +
    glob.glob(os.path.join(WWW, "es", "*.html")) +
    glob.glob(os.path.join(WWW, "pt", "*.html"))
)

for fpath in all_pages:
    try:
        html = open(fpath, encoding="utf-8").read()
        if already_updated(html):
            skipped += 1
            continue
        # Find the first dropdown-menu closing div that follows langDropdown
        # Strategy: find the dropdown-menu-right div and insert before its closing tag
        pattern = r'(<div class="dropdown-menu dropdown-menu-right"[^>]*>)(.*?)(</div>)'
        m = re.search(pattern, html, re.S)
        if not m:
            skipped += 1
            continue
        old_block = m.group(0)
        new_block  = m.group(1) + m.group(2) + "\n" + NEW_LANG_ITEMS + "\n" + m.group(3)
        new_html   = html.replace(old_block, new_block, 1)
        if new_html != html:
            open(fpath, "w", encoding="utf-8").write(new_html)
            fixed += 1
    except Exception as e:
        print(f"ERR {fpath}: {e}")
        errors += 1

print(f"Updated: {fixed} | Skipped (already done or no dropdown): {skipped} | Errors: {errors}")
print("DONE")
