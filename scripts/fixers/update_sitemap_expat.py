#!/usr/bin/env python3
"""Add expat guide pages + hub pages to sitemap.xml"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"
SITEMAP = os.path.join(WWW, "sitemap.xml")
BASE = "https://www.evisa-card.com"

EXPAT_SLUGS = [
    "expat-guide-thailand",
    "expat-guide-portugal",
    "expat-guide-spain",
    "expat-guide-mexico",
    "expat-guide-vietnam",
    "expat-guide-malaysia",
    "expat-guide-japan",
    "expat-guide-uae",
    "expat-guide-colombia",
    "expat-guides",
]

LANGS = ["en","fr","es","pt"]

with open(SITEMAP, "r", encoding="utf-8") as f:
    content = f.read()

# Build new URLs block
new_urls = ""
for slug in EXPAT_SLUGS:
    for lang in LANGS:
        url = f"{BASE}/{lang}/{slug}.html"
        if url not in content:
            new_urls += f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-03-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""

if new_urls:
    # Insert before </urlset>
    content = content.replace("</urlset>", new_urls + "</urlset>")
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(content)
    count = new_urls.count("<url>")
    print(f"Added {count} URLs to sitemap")
else:
    print("All URLs already in sitemap")

# Final count
import re
total = len(re.findall(r'<loc>', content))
print(f"Total URLs in sitemap: {total}")
