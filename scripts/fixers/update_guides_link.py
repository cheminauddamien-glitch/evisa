#!/usr/bin/env python3
"""Update Guides navbar link on all pages to point to expat-guides.html hub"""
import os, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

fixed = errors = 0

for lang in ["en","fr","es","pt"]:
    for fpath in glob.glob(os.path.join(WWW, lang, "*.html")):
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                html = f.read()
            new_html = html.replace(
                'href="/en/retirement-visa-guide.html"',
                f'href="/{lang}/expat-guides.html"'
            )
            if new_html != html:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_html)
                fixed += 1
        except Exception as e:
            print(f"ERR {fpath}: {e}")
            errors += 1

print(f"Guides link updated: {fixed} pages | Errors: {errors}")
