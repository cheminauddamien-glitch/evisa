"""Insert 80 new Phase 2 URLs (8 destinations x 10 languages) into sitemap.xml."""
import re

SLUGS = [
    'patagonia-visa-requirements',
    'laos-visa-requirements',
    'taipei-visa-requirements',
    'machu-picchu-visa-requirements',
    'bermuda-visa-requirements',
    'macau-visa-requirements',
    'amsterdam-visa-requirements',
    'cappadocia-visa-requirements',
]
LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']
LASTMOD = '2026-05-05'

with open('sitemap.xml', encoding='utf-8') as f:
    sm = f.read()

new_blocks = []
for slug in SLUGS:
    for lang in LANGS:
        # priority: 0.8 for en, 0.7 for fr/es/pt, 0.6 for others
        prio = '0.8' if lang == 'en' else ('0.7' if lang in ('fr','es','pt') else '0.6')
        new_blocks.append(f"""  <url>
    <loc>https://www.evisa-card.com/{lang}/{slug}.html</loc>
    <lastmod>{LASTMOD}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{prio}</priority>
  </url>""")

new_xml = '\n'.join(new_blocks) + '\n'
updated = sm.replace('</urlset>', new_xml + '</urlset>')

# Skip if already inserted
if 'patagonia-visa-requirements' in sm:
    print('Already in sitemap, skipping')
else:
    with open('sitemap.xml', 'w', encoding='utf-8', newline='\n') as f:
        f.write(updated)
    print(f'Added {len(new_blocks)} URLs to sitemap.xml')
