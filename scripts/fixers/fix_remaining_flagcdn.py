#!/usr/bin/env python3
"""Fix remaining flagcdn hero images on guide pages."""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"

BG = {
    "thailand":"bg_1.jpg","portugal":"bg_2.jpg","spain":"bg_3.jpg",
    "mexico":"bg_4.jpg","vietnam":"bg_5.jpg","malaysia":"bg_1.jpg",
    "japan":"bg_2.jpg","uae":"bg_3.jpg","colombia":"bg_4.jpg",
    "panama":"bg_5.jpg","costa-rica":"bg_1.jpg","greece":"bg_2.jpg",
    "georgia":"bg_3.jpg","paraguay":"bg_4.jpg","laos":"bg_5.jpg",
    "cambodia":"bg_1.jpg"
}

fixed = 0
for lang in ["en","fr","es","pt","zh","th","ru","ar","ja","ko"]:
    for slug, bg in BG.items():
        fp = os.path.join(BASE, lang, f"expat-guide-{slug}.html")
        if not os.path.isfile(fp):
            continue
        with open(fp, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        if "flagcdn" not in html:
            continue
        # Replace all flagcdn URL variants
        html2 = re.sub(
            r"background-image:\s*url\(['\"]?https://flagcdn\.com/[^)'\")]*['\"]?\)",
            f"background-image: url('../images/{bg}')",
            html
        )
        if html2 != html:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(html2)
            fixed += 1
            print(f"  OK {lang}/expat-guide-{slug}.html")

print(f"\nFixed {fixed} hero images")
