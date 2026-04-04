import os, glob
from datetime import date

WWW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www')
BASE = 'https://www.evisa-card.com'
today = date.today().isoformat()

urls = []

def norm(path):
    return path.replace('\\', '/')

# Root pages
for fpath in glob.glob(os.path.join(WWW, '*.html')):
    rel = norm(os.path.relpath(fpath, WWW))
    slug = rel.replace('.html', '')
    if slug == 'index':
        loc = BASE + '/'
        priority = '1.0'
        freq = 'daily'
    elif slug in ['destination', 'blog', 'contact', 'about']:
        loc = BASE + '/' + slug
        priority = '0.8'
        freq = 'weekly'
    else:
        loc = BASE + '/' + slug
        priority = '0.6'
        freq = 'monthly'
    urls.append((loc, freq, priority))

# EN pages
for fpath in sorted(glob.glob(os.path.join(WWW, 'en', '*.html'))):
    rel = norm(os.path.relpath(fpath, WWW))
    slug = rel.replace('.html', '')
    loc = BASE + '/' + slug
    name = os.path.basename(fpath).replace('.html', '')
    if name.startswith('visa-') and not any(x in name for x in ['-for-', '-requirements', '-fees', '-processing', '-extension']):
        priority = '0.9'
        freq = 'weekly'
    elif '-for-' in name or '-requirements' in name or '-fees' in name or '-processing' in name or '-extension' in name:
        priority = '0.7'
        freq = 'monthly'
    else:
        priority = '0.6'
        freq = 'monthly'
    urls.append((loc, freq, priority))

# FR ES PT pages
for lang in ['fr', 'es', 'pt']:
    for fpath in sorted(glob.glob(os.path.join(WWW, lang, '*.html'))):
        rel = norm(os.path.relpath(fpath, WWW))
        slug = rel.replace('.html', '')
        loc = BASE + '/' + slug
        urls.append((loc, 'monthly', '0.7'))

print(f'Total URLs: {len(urls)}')

# Write sitemap
xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
xml_lines.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')

for loc, freq, priority in urls:
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{loc}</loc>')
    xml_lines.append(f'    <lastmod>{today}</lastmod>')
    xml_lines.append(f'    <changefreq>{freq}</changefreq>')
    xml_lines.append(f'    <priority>{priority}</priority>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

sitemap_path = os.path.join(WWW, 'sitemap.xml')
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml_lines))

print(f'Sitemap written to: {sitemap_path}')
