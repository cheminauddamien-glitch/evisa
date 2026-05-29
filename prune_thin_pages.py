"""A) Pruning: noindex nationality pages that are BOTH thin (<300 words in
<article>) AND absent from GSC traffic (top-1000 Pages report). Concentrates
crawl budget and cuts the scaled-content footprint that core updates penalise.

Keeps indexed: pages with traffic, and longer (>=300w) nationality pages.
Never touches hub/requirements/fees/extension/processing pages.
"""
import pandas as pd, glob, re, os, sys

ROOT = r'C:\Users\chemi\Documents\evisa\pacific-main'
PERF = r'C:\Users\chemi\Downloads\evisa-card.com-Performance-on-Search-2026-05-29.xlsx'

pages = pd.read_excel(PERF, sheet_name='Pages')
pages.columns = ['URL', 'Clicks', 'Impr', 'CTR', 'Pos']
traffic = set(u.replace('https://www.evisa-card.com', '').replace('.html', '').strip('/')
              for u in pages.URL)

flipped = skipped_traffic = skipped_long = 0
for f in glob.glob(os.path.join(ROOT, 'www', '*', '*-visa-for-*-citizens.html')):
    p = f.replace('\\', '/').split('/')
    lang, bn = p[-2], p[-1].replace('.html', '')
    path = f'{lang}/{bn}'
    if path in traffic:
        skipped_traffic += 1
        continue
    h = open(f, encoding='utf-8', errors='replace').read()
    b = re.search(r'<article[^>]*>(.*?)</article>', h, re.S)
    wc = len(re.sub(r'<[^>]+>', ' ', b.group(1)).split()) if b else 0
    if wc >= 300:
        skipped_long += 1
        continue
    # flip index -> noindex
    new = re.sub(r'(name=["\']robots["\'][^>]*content=["\'])index',
                 r'\1noindex', h, count=1, flags=re.I)
    if new == h:
        new = re.sub(r'(content=["\'])index(\s*,?\s*follow["\'][^>]*name=["\']robots["\'])',
                     r'\1noindex\2', h, count=1, flags=re.I)
    if new == h:
        # no robots meta -> inject
        new = h.replace('<head>', '<head>\n    <meta name="robots" content="noindex, follow"/>', 1)
    if new != h:
        open(f, 'w', encoding='utf-8').write(new)
        flipped += 1

print(f'noindexed (thin + no-traffic): {flipped}')
print(f'kept (has traffic): {skipped_traffic}')
print(f'kept (>=300 words): {skipped_long}')
