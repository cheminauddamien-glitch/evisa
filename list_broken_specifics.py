"""List exact pages that fail any check."""
import os, glob
from html.parser import HTMLParser

LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']

class A(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_meta = self.has_canon = self.has_h1 = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta' and a.get('name','').lower() == 'description': self.has_meta = True
        if tag == 'link' and a.get('rel','').lower() == 'canonical': self.has_canon = True
        if tag == 'h1': self.has_h1 = True


def categorize(filename):
    bn = os.path.basename(filename)
    if 'visa-for-' in bn and 'citizens' in bn: return 'nationality'
    if bn.endswith('-visa-requirements.html'): return 'requirements'
    if bn.endswith('-visa-extension.html'): return 'extension'
    if bn.endswith('-visa-fees.html'): return 'fees'
    if bn.endswith('-visa-processing-time.html'): return 'processing'
    if bn.startswith('visa-') and bn.count('-') == 1: return 'hub_country'
    return 'other'


issues = {'no_meta': [], 'no_canon': [], 'no_h1': []}
for lang in LANGS:
    for f in glob.glob(f'www/{lang}/*.html'):
        with open(f, encoding='utf-8', errors='replace') as fh: html = fh.read()
        p = A()
        try: p.feed(html)
        except: pass
        cat = categorize(f)
        if cat == 'hub_country':
            if not p.has_meta: issues['no_meta'].append(f)
            if not p.has_h1: issues['no_h1'].append(f)
        if cat == 'other':
            if not p.has_canon: issues['no_canon'].append(f)

print('=== HUB COUNTRY: no meta description ===')
for f in issues['no_meta']: print(' ', f)
print(f'  TOTAL: {len(issues["no_meta"])}')
print('\n=== HUB COUNTRY: no H1 ===')
for f in issues['no_h1']: print(' ', f)
print(f'  TOTAL: {len(issues["no_h1"])}')
print('\n=== OTHER: no canonical ===')
for f in issues['no_canon']: print(' ', f)
print(f'  TOTAL: {len(issues["no_canon"])}')
