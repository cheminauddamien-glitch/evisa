"""Count pages by canonical format: with .html vs without .html."""
import re, glob, os
from collections import defaultdict

LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']
stats = defaultdict(lambda: {'html': 0, 'clean': 0, 'missing': 0})

for lang in LANGS:
    for f in glob.glob(f'www/{lang}/*.html'):
        with open(f, encoding='utf-8', errors='replace') as fh: h = fh.read()
        m = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)', h, re.I)
        if not m:
            m = re.search(r'<link[^>]*href=["\']([^"\']*)["\'][^>]*rel=["\']canonical["\']', h, re.I)
        if not m:
            stats[lang]['missing'] += 1
        elif m.group(1).endswith('.html'):
            stats[lang]['html'] += 1
        else:
            stats[lang]['clean'] += 1

print(f'{"Lang":<6} {"Total":>6} {"Canon=.html":>12} {"Canon=clean":>12} {"Missing":>8}')
total_html = total_clean = total_missing = 0
for lang in LANGS:
    s = stats[lang]
    t = s['html'] + s['clean'] + s['missing']
    total_html += s['html']; total_clean += s['clean']; total_missing += s['missing']
    print(f'{lang:<6} {t:>6} {s["html"]:>12} {s["clean"]:>12} {s["missing"]:>8}')
print(f'{"TOTAL":<6} {total_html+total_clean+total_missing:>6} {total_html:>12} {total_clean:>12} {total_missing:>8}')
