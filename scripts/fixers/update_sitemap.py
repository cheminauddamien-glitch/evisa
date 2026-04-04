#!/usr/bin/env python3
"""
update_sitemap.py
Rebuilds sitemap.xml from all HTML files in www/
"""
import os, glob, sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')

WWW  = "C:/Users/chemi/Documents/evisa/pacific-main/www"
BASE = "https://www.evisa-card.com"
TODAY = date.today().isoformat()

# Priority rules
def get_priority(url):
    if url == BASE + "/":       return "1.0"
    if url.endswith("/en/") or url.endswith("/fr/") or url.endswith("/es/") or url.endswith("/pt/"): return "0.9"
    parts = url.rstrip("/").split("/")
    slug  = parts[-1] if parts else ""
    # Main country pages
    if re.search(r'^visa-[a-z]', slug): return "0.9"
    # Nationality pages
    if "visa-for-" in slug and "citizens" in slug: return "0.7"
    # Requirements / processing / fees
    if any(s in slug for s in ("requirements","processing-time","fees","visa-free")): return "0.8"
    # Guides
    if any(s in slug for s in ("guide","expat","nomad","retire")): return "0.7"
    return "0.6"

import re

def get_changefreq(url):
    slug = url.rstrip("/").split("/")[-1]
    if any(s in slug for s in ("visa-for-","requirements","processing")): return "monthly"
    return "weekly"

def is_noindex(filepath):
    try:
        with open(filepath, encoding="utf-8", errors="ignore") as fh:
            chunk = fh.read(4096)
        return "noindex" in chunk
    except Exception:
        return False

urls = []

# Root HTML pages
for f in glob.glob(os.path.join(WWW, "*.html")):
    if is_noindex(f):
        continue
    name = os.path.basename(f)
    slug = name.replace(".html","")
    url  = f"{BASE}/{slug}" if slug != "index" else BASE + "/"
    urls.append(url)

# en / fr / es / pt
for lang in ("en","fr","es","pt","zh","th","ru","ar","ja","ko"):
    for f in glob.glob(os.path.join(WWW, lang, "*.html")):
        if is_noindex(f):
            continue
        name = os.path.basename(f)
        slug = name.replace(".html","")
        url  = f"{BASE}/{lang}/{slug}"
        urls.append(url)

urls = sorted(set(urls))

# Build XML
lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
         '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']

for url in urls:
    prio   = get_priority(url)
    freq   = get_changefreq(url)
    lines += [
        "  <url>",
        f"    <loc>{url}</loc>",
        f"    <lastmod>{TODAY}</lastmod>",
        f"    <changefreq>{freq}</changefreq>",
        f"    <priority>{prio}</priority>",
        "  </url>",
    ]

lines.append("</urlset>")

out_path = os.path.join(WWW, "sitemap.xml")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Sitemap written: {len(urls)} URLs → {out_path}")
print("DONE")
