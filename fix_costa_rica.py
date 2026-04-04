#!/usr/bin/env python3
"""Fix Costa Rica translation bug in all non-EN language expat guide files."""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
LANGS = ["ja", "ko", "ru", "ar", "th"]

for lang in LANGS:
    lang_dir = os.path.join(BASE, lang)
    for fname in sorted(os.listdir(lang_dir)):
        if not fname.startswith("expat-guide-") or not fname.endswith(".html"):
            continue
        fpath = os.path.join(lang_dir, fname)
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()

        original = html
        # Fix any non-ASCII + "a Rica" pattern → "Costa Rica"
        html = re.sub(r'[\u0080-\uFFFF]+a Rica', 'Costa Rica', html)

        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Fixed {lang}/{fname}")

print("Done.")
