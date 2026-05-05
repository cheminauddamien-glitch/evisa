"""Rebuild www/sitemap.xml from filesystem — covers all 13K+ HTML pages.

The deployed sitemap is www/sitemap.xml (served at evisa-card.com/sitemap.xml).
URLs are written WITHOUT the .html extension to match the .htaccess clean-URL rewrites.

Priority strategy:
- 1.0 root index
- 0.9 destination/about/contact + lang index pages
- 0.85 hub country (visa-{country})
- 0.8 EN -visa-requirements / fees / processing / extension
- 0.75 FR/ES/PT same
- 0.7 EN nationality pages
- 0.65 FR/ES/PT nationality pages
- 0.6 other languages (zh/th/ru/ar/ja/ko)
- 0.4 utility pages (legal-notice, disclaimer, search-result, etc.)
"""
import os, glob, datetime

LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']
LASTMOD = datetime.date.today().isoformat()
BASE = 'https://www.evisa-card.com'

UTILITY = {'legal-notice','disclaimer','privacy','contact','about','search','search-result',
           'visa-result','visa-search','expat-guides','blog','blog-single',
           'how-to-apply-evisa','visa-documents-checklist','visa-processing-times',
           'visa-photo-requirements','visa-payment-methods','visa-rejection-reasons'}


def page_priority(filepath):
    bn = os.path.basename(filepath)
    name = bn.replace('.html','')
    parts = filepath.replace('\\','/').split('/')
    lang = parts[1] if len(parts) > 1 else 'en'
    is_latin = lang in ('en','fr','es','pt')

    if name in UTILITY: return ('0.4','monthly')
    if 'visa-for-' in name and 'citizens' in name:
        return (('0.7' if is_latin else '0.6'), 'monthly')
    if name.endswith('-visa-requirements') or name.endswith('-visa-fees') \
            or name.endswith('-visa-processing-time') or name.endswith('-visa-extension'):
        return (('0.8' if lang == 'en' else ('0.75' if is_latin else '0.6')), 'monthly')
    if name.startswith('visa-') and name.count('-') == 1:
        return (('0.85' if is_latin else '0.7'), 'monthly')
    return (('0.6' if is_latin else '0.5'), 'monthly')


def root_pages():
    """The 4 root pages (no lang dir)."""
    return [
        (f'{BASE}/', '1.0', 'weekly'),
        (f'{BASE}/destination', '0.9', 'weekly'),
        (f'{BASE}/about', '0.6', 'monthly'),
        (f'{BASE}/contact', '0.6', 'monthly'),
    ]


def main():
    urls = []
    seen = set()

    for u, prio, freq in root_pages():
        urls.append((u, prio, freq))
        seen.add(u)

    for lang in LANGS:
        files = sorted(glob.glob(f'www/{lang}/*.html'))
        for f in files:
            bn = os.path.basename(f).replace('.html', '')
            url = f'{BASE}/{lang}/{bn}'
            if url in seen: continue
            seen.add(url)
            prio, freq = page_priority(f)
            urls.append((url, prio, freq))

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, prio, freq in urls:
        out.append('  <url>')
        out.append(f'    <loc>{url}</loc>')
        out.append(f'    <lastmod>{LASTMOD}</lastmod>')
        out.append(f'    <changefreq>{freq}</changefreq>')
        out.append(f'    <priority>{prio}</priority>')
        out.append('  </url>')
    out.append('</urlset>')

    # Write to BOTH locations: root (legacy) and www/ (the one actually deployed)
    for path in ('sitemap.xml', 'www/sitemap.xml'):
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(out) + '\n')
        print(f'Wrote {path}: {len(urls)} URLs')


if __name__ == '__main__':
    main()
