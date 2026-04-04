#!/usr/bin/env python3
"""Add visa-result pages to sitemap and update lastmod dates."""
import re

SITEMAP = r"C:\Users\chemi\Documents\evisa\pacific-main\www\sitemap.xml"
LANGS = ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]
NEW_DATE = "2026-03-27"

# New entries to add
NEW_ENTRIES = ""
for lang in LANGS:
    NEW_ENTRIES += f"""  <url>
    <loc>https://www.evisa-card.com/{lang}/visa-result</loc>
    <lastmod>{NEW_DATE}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
"""

with open(SITEMAP, encoding="utf-8") as f:
    content = f.read()

# Check if visa-result is already there
if "visa-result" in content:
    print("visa-result already in sitemap")
else:
    # Insert before </urlset>
    content = content.replace("</urlset>", NEW_ENTRIES + "</urlset>")
    print(f"Added {len(LANGS)} visa-result entries")

# Update lastmod for expat-guide entries (they may still have old date)
old_dates = re.findall(r"<lastmod>(2026-03-\d+)</lastmod>", content)
unique_dates = set(old_dates)
print(f"Dates found in sitemap: {unique_dates}")

with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(content)

print("Sitemap updated.")
