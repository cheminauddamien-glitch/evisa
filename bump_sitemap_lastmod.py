#!/usr/bin/env python3
"""
bump_sitemap_lastmod.py — Update <lastmod> to 2026-05-20 for the 3240 files
that received the visa 2026 update banner (identified via the
'<!-- visa-2026-update -->' marker we injected).

Leaves every other URL's lastmod untouched.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
WWW = ROOT / "www"
SITEMAP = WWW / "sitemap.xml"
NEW_LASTMOD = "2026-05-20"
MARKER = "<!-- visa-2026-update -->"

# Build set of URL paths (without https://www.evisa-card.com prefix and .html suffix)
# for every HTML file that contains the marker.
print("Scanning files for marker...")
updated_urls = set()
for html_file in WWW.rglob("*.html"):
    try:
        if MARKER in html_file.read_text(encoding="utf-8", errors="replace"):
            rel = html_file.relative_to(WWW).as_posix()  # e.g. en/expat-guide-thailand.html
            no_ext = rel[:-5]  # strip .html
            updated_urls.add(f"https://www.evisa-card.com/{no_ext}")
    except Exception as e:
        print(f"  skip {html_file}: {e}")

print(f"Marker found in {len(updated_urls)} files")

# Also update expat-guide files (they don't have the same marker but have the new banner)
# We can detect them by their distinctive new banner string in any language.
EXPAT_MARKERS = [
    "Updated: 20 May 2026",
    "Mis à jour: 20 mai 2026",
    "Actualizado: 20 de mayo de 2026",
    "Atualizado: 20 de maio de 2026",
    "更新: 2026年5月20日",
    "อัปเดต: 20 พฤษภาคม 2026",
    "Обновлено: 20 мая 2026",
    "تم التحديث: 20 مايو 2026",
    "業데이트: 2026년 5월 20일",  # ja/ko handled below too
    "업데이트: 2026년 5월 20일",
]
for html_file in WWW.rglob("expat-guide-*.html"):
    try:
        txt = html_file.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    if any(m in txt for m in EXPAT_MARKERS):
        rel = html_file.relative_to(WWW).as_posix()
        no_ext = rel[:-5]
        updated_urls.add(f"https://www.evisa-card.com/{no_ext}")

print(f"Total updated URLs (incl. expat-guides): {len(updated_urls)}")

# Read sitemap, bump lastmod for matching URLs only
text = SITEMAP.read_text(encoding="utf-8")

# Each <url> block has <loc>...</loc> and <lastmod>...</lastmod>
# We rewrite block-by-block.
url_block_re = re.compile(
    r"(<url>\s*<loc>([^<]+)</loc>\s*<lastmod>)([^<]+)(</lastmod>)",
    re.MULTILINE,
)

bumped = 0
def repl(m):
    global bumped
    loc = m.group(2).strip()
    if loc in updated_urls:
        bumped += 1
        return m.group(1) + NEW_LASTMOD + m.group(4)
    return m.group(0)

new_text = url_block_re.sub(repl, text)

if bumped == 0:
    print("WARNING: no URLs matched — sitemap unchanged. URL format mismatch?")
else:
    SITEMAP.write_text(new_text, encoding="utf-8")
    print(f"Sitemap updated: {bumped} <lastmod> bumped to {NEW_LASTMOD}")
    print(f"({len(updated_urls) - bumped} updated URLs had no sitemap entry)")
