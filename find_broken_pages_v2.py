import glob, os
from html.parser import HTMLParser

EXCLUDE = ('for-', '-visa-', 'requirement', 'extension', 'fee', 'processing')

class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_meta = False
        self.has_canon = False
        self.has_h1 = False
        self.meta_content = ''
        self.h1_content = ''
        self._in_h1 = False
        self.unescaped_gt = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta' and a.get('name','').lower() == 'description':
            self.has_meta = True
            self.meta_content = a.get('content','')
            if '>' in self.meta_content:
                self.unescaped_gt = True
        if tag == 'link' and a.get('rel','').lower() == 'canonical':
            self.has_canon = True
        if tag == 'h1':
            self.has_h1 = True
            self._in_h1 = True
    def handle_endtag(self, tag):
        if tag == 'h1':
            self._in_h1 = False
    def handle_data(self, data):
        if self._in_h1:
            self.h1_content += data

issues = []
for lang in ['en','es','fr','pt']:
    for pattern in ['visa-*.html','*-visa-requirements.html','*-visa-fees.html',
                    '*-visa-processing-time.html','*-visa-extension.html']:
        files = glob.glob(f'www/{lang}/{pattern}')
        if pattern == 'visa-*.html':
            files = [f for f in files if not any(s in os.path.basename(f) for s in EXCLUDE)]
        for f in files:
            try:
                with open(f, encoding='utf-8', errors='replace') as fh:
                    h = fh.read()
            except Exception:
                continue
            p = Audit()
            try: p.feed(h)
            except Exception: pass
            probs = []
            if not p.has_meta: probs.append('NO_META')
            if not p.has_canon: probs.append('NO_CANON')
            if not p.has_h1: probs.append('NO_H1')
            if p.unescaped_gt: probs.append('UNESCAPED_GT_IN_META')
            if probs:
                issues.append((f, probs, p.meta_content[:120]))

print(f'TOTAL ISSUES: {len(issues)}\n')
for f, probs, meta in issues:
    print(f'{f}')
    print(f'  -> {", ".join(probs)}')
    if meta: print(f'  meta: {meta}')
    print()
