"""Add self-canonical to disclaimer.html and legal-notice.html in zh/th/ru/ar/ja/ko."""
import re

LANGS = ['zh','th','ru','ar','ja','ko']
PAGES = ['disclaimer.html','legal-notice.html']

for lang in LANGS:
    for page in PAGES:
        path = f'www/{lang}/{page}'
        try:
            with open(path, encoding='utf-8') as f:
                html = f.read()
        except FileNotFoundError:
            print(f'MISSING {path}')
            continue
        if re.search(r'<link[^>]*rel=["\']canonical["\']', html, re.I):
            print(f'SKIP {path} (canonical present)')
            continue
        canonical = f'<link rel="canonical" href="https://www.evisa-card.com/{lang}/{page}"/>\n    '
        # Insert right before the first hreflang alternate
        new = re.sub(
            r'(\n    )(<link rel="alternate" hreflang="en")',
            r'\n    ' + canonical + r'\2',
            html, count=1
        )
        if new == html:
            print(f'NO MATCH {path}')
            continue
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f'OK {path}')
