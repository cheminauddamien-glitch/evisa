"""Comprehensive SEO audit: on-page, technical, AI visibility, broken links."""
import os, re, glob, json
from html.parser import HTMLParser
from collections import defaultdict, Counter

LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']

class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.has_meta_desc = False
        self.meta_desc = ''
        self.has_canonical = False
        self.canonical = ''
        self.has_h1 = False
        self.h1_count = 0
        self.has_h2 = False
        self.h2_count = 0
        self.has_robots = False
        self.html_lang = ''
        self.html_dir = ''
        self.hreflangs = []
        self.json_ld_count = 0
        self.og_title = False
        self.og_desc = False
        self.og_image = False
        self.internal_links = []
        self._in_title = False
        self._in_h1 = False
        self._in_jsonld = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.html_lang = a.get('lang','')
            self.html_dir = a.get('dir','')
        elif tag == 'title':
            self._in_title = True
        elif tag == 'meta':
            n = a.get('name','').lower()
            p = a.get('property','').lower()
            if n == 'description':
                self.has_meta_desc = True
                self.meta_desc = a.get('content','')
            if n == 'robots':
                self.has_robots = True
            if p == 'og:title': self.og_title = True
            if p == 'og:description': self.og_desc = True
            if p == 'og:image': self.og_image = True
        elif tag == 'link':
            rel = a.get('rel','').lower()
            if rel == 'canonical':
                self.has_canonical = True
                self.canonical = a.get('href','')
            if rel == 'alternate' and a.get('hreflang'):
                self.hreflangs.append(a.get('hreflang'))
        elif tag == 'h1':
            self.has_h1 = True
            self.h1_count += 1
            self._in_h1 = True
        elif tag == 'h2':
            self.has_h2 = True
            self.h2_count += 1
        elif tag == 'script':
            if a.get('type','').lower() == 'application/ld+json':
                self._in_jsonld = True
                self.json_ld_count += 1
        elif tag == 'a':
            href = a.get('href','')
            if href and not href.startswith(('http://','https://','mailto:','tel:','javascript:','#')):
                self.internal_links.append(href)
    def handle_endtag(self, tag):
        if tag == 'title': self._in_title = False
        if tag == 'h1': self._in_h1 = False
        if tag == 'script': self._in_jsonld = False
    def handle_data(self, data):
        if self._in_title: self.title += data


def categorize(filename):
    bn = os.path.basename(filename)
    if 'visa-for-' in bn and 'citizens' in bn: return 'nationality'
    if bn.endswith('-visa-requirements.html'): return 'requirements'
    if bn.endswith('-visa-extension.html'): return 'extension'
    if bn.endswith('-visa-fees.html'): return 'fees'
    if bn.endswith('-visa-processing-time.html'): return 'processing'
    if bn.startswith('visa-') and bn.count('-') == 1: return 'hub_country'
    return 'other'


def main():
    print('='*70)
    print('FULL SEO AUDIT — eVisa-Card.com')
    print('='*70)

    # 1. Inventory
    inventory = {lang: glob.glob(f'www/{lang}/*.html') for lang in LANGS}
    total_pages = sum(len(v) for v in inventory.values())
    print(f'\n## 1. INVENTORY')
    print(f'Total HTML pages: {total_pages}')
    for lang, files in inventory.items():
        cats = Counter(categorize(f) for f in files)
        print(f'  {lang}: {len(files)} | ' + ' '.join(f'{k}={v}' for k,v in sorted(cats.items())))

    # 2. On-page audit (sample 1 page per category per lang)
    print(f'\n## 2. ON-PAGE SEO AUDIT (full scan)')
    issues = defaultdict(list)
    stats = defaultdict(lambda: defaultdict(int))
    for lang, files in inventory.items():
        for f in files:
            with open(f, encoding='utf-8', errors='replace') as fh: html = fh.read()
            p = PageAudit()
            try: p.feed(html)
            except: pass
            cat = categorize(f)
            stats[cat]['total'] += 1
            if not p.title.strip(): stats[cat]['no_title'] += 1
            if not p.has_meta_desc: stats[cat]['no_meta'] += 1
            if not p.has_canonical: stats[cat]['no_canonical'] += 1
            if not p.has_h1: stats[cat]['no_h1'] += 1
            if p.h1_count > 1: stats[cat]['multi_h1'] += 1
            if not p.has_h2: stats[cat]['no_h2'] += 1
            if p.json_ld_count == 0: stats[cat]['no_jsonld'] += 1
            if not p.og_title or not p.og_desc: stats[cat]['no_og'] += 1
            if p.title and len(p.title) > 70: stats[cat]['title_too_long'] += 1
            if p.title and len(p.title) < 30: stats[cat]['title_too_short'] += 1
            if p.meta_desc and len(p.meta_desc) > 165: stats[cat]['meta_too_long'] += 1
            if p.meta_desc and len(p.meta_desc) < 80: stats[cat]['meta_too_short'] += 1
            if p.has_canonical and lang not in p.canonical:
                if f'/{lang}/' not in p.canonical: stats[cat]['canonical_lang_mismatch'] += 1
            if not p.html_lang: stats[cat]['no_html_lang'] += 1
            if lang == 'ar' and p.html_dir != 'rtl': stats[cat]['ar_no_rtl'] += 1
            # hreflang completeness
            if len(p.hreflangs) < 4: stats[cat]['hreflang_incomplete'] += 1

    print(f'{"Category":<14} {"Total":>6} {"NoMeta":>7} {"NoCanon":>8} {"NoH1":>5} {"MultiH1":>8} {"NoSchema":>9} {"NoOG":>5} {"HrefIncompl":>12}')
    for cat in ['hub_country','requirements','fees','processing','extension','nationality','other']:
        s = stats[cat]
        if s['total']:
            print(f'{cat:<14} {s["total"]:>6} {s["no_meta"]:>7} {s["no_canonical"]:>8} {s["no_h1"]:>5} {s["multi_h1"]:>8} {s["no_jsonld"]:>9} {s["no_og"]:>5} {s["hreflang_incomplete"]:>12}')

    # 3. Technical SEO
    print(f'\n## 3. TECHNICAL SEO')
    print('robots.txt:')
    with open('robots.txt') as f: print('  ' + f.read().replace('\n','\n  '))
    sitemap_size = sum(1 for _ in re.finditer(r'<loc>', open('sitemap.xml',encoding='utf-8').read()))
    print(f'sitemap.xml URLs: {sitemap_size}')
    print(f'sitemap coverage: {sitemap_size}/{total_pages} = {100*sitemap_size/total_pages:.1f}%')

    # 4. AI Visibility (schema.org coverage by type)
    print(f'\n## 4. AI VISIBILITY')
    schema_types = Counter()
    semantic_html = defaultdict(int)
    for f in inventory['en'][:200]:  # sample
        with open(f, encoding='utf-8', errors='replace') as fh: html = fh.read()
        for m in re.finditer(r'"@type"\s*:\s*"([^"]+)"', html):
            schema_types[m.group(1)] += 1
        if '<article' in html: semantic_html['article'] += 1
        if '<section' in html: semantic_html['section'] += 1
        if '<nav' in html: semantic_html['nav'] += 1
        if '<main' in html: semantic_html['main'] += 1
        if '<header' in html: semantic_html['header'] += 1
        if '<footer' in html: semantic_html['footer'] += 1
    print(f'Schema.org types (top 15) on EN sample of 200 pages:')
    for t, c in schema_types.most_common(15):
        print(f'  {t}: {c}')
    print(f'Semantic HTML5 elements:')
    for tag, count in semantic_html.items():
        print(f'  <{tag}>: {count}/200 pages')

    # 5. Broken links (sample EN — check internal links exist)
    print(f'\n## 5. BROKEN INTERNAL LINKS (sampling 50 EN pages)')
    sample = inventory['en'][:50]
    broken = defaultdict(list)
    seen = set()
    for f in sample:
        with open(f, encoding='utf-8', errors='replace') as fh: html = fh.read()
        p = PageAudit()
        try: p.feed(html)
        except: pass
        for href in p.internal_links:
            href_clean = href.split('#')[0].split('?')[0]
            if not href_clean: continue
            if href_clean in seen: continue
            seen.add(href_clean)
            # Resolve to filesystem path
            if href_clean.startswith('/'):
                fp = 'www' + href_clean
            else:
                base = os.path.dirname(f)
                fp = os.path.normpath(os.path.join(base, href_clean))
            if not fp.endswith('.html') and not fp.endswith('/'):
                # Try adding .html
                if not os.path.exists(fp) and os.path.exists(fp + '.html'):
                    continue
            if not os.path.exists(fp) and not os.path.exists(fp.rstrip('/')+'/index.html'):
                broken[href].append(os.path.basename(f))
    print(f'Unique internal hrefs sampled: {len(seen)}')
    print(f'Broken (404 in filesystem): {len(broken)}')
    for href, srcs in list(broken.items())[:30]:
        print(f'  -> {href}  (in {srcs[0]} +{len(srcs)-1})')


if __name__ == '__main__':
    main()
