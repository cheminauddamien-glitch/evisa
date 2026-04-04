#!/usr/bin/env python3
"""Fix canonical URLs: each page must self-reference its own language."""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
DOMAIN = "https://www.evisa-card.com"

fixed = 0
for lang in ["fr","es","pt","zh","th","ru","ar","ja","ko"]:
    lang_dir = os.path.join(BASE, lang)
    if not os.path.isdir(lang_dir):
        continue
    for fn in os.listdir(lang_dir):
        if not fn.endswith(".html"):
            continue
        fp = os.path.join(lang_dir, fn)
        with open(fp, encoding="utf-8", errors="ignore") as f:
            html = f.read()

        # Expected canonical
        correct_canon = f'{DOMAIN}/{lang}/{fn}'

        # Check if canonical points to wrong language
        # Pattern: <link rel="canonical" href="https://www.evisa-card.com/XX/filename.html"/>
        m = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', html)
        if not m:
            continue
        current = m.group(1)

        # Fix if canonical doesn't point to this lang
        if f"/{lang}/{fn}" not in current:
            html = html.replace(
                f'href="{current}"',
                f'href="{correct_canon}"',
                1  # only replace the canonical, not all hrefs with this URL
            )
            # Be more precise - replace only the canonical link
            html = re.sub(
                r'(<link\s+rel="canonical"\s+href=")[^"]*(")',
                f'\\g<1>{correct_canon}\\2',
                html, count=1
            )
            with open(fp, "w", encoding="utf-8") as f:
                f.write(html)
            fixed += 1

print(f"Fixed {fixed} canonical URLs")
