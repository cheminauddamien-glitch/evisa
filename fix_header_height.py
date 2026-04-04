#!/usr/bin/env python3
"""Reduce header height: logo 120px -> 60px, tighten navbar padding."""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
count = 0

for root, dirs, files in os.walk(BASE):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        fp = os.path.join(root, fn)
        with open(fp, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        if "height:120px" not in html and "height: 120px" not in html:
            continue
        # Replace logo height 120px -> 60px
        html = html.replace("height:120px", "height:60px")
        html = html.replace("height: 120px", "height:60px")
        with open(fp, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1

print(f"Done: {count} files updated (logo 120px -> 60px)")
