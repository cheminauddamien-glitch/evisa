"""
1. Fix Guides nav link (use nav-specific check)
2. destination.html: 4 columns (col-md-3) instead of 3 (col-md-4), reduce margins
3. Create SVG favicon + add to all pages
"""
import os, re, glob

WWW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www')

# ── 1. CREATE SVG FAVICON ──────────────────────────────────────────────────────
svg_favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#e74c3c"/>
  <text x="32" y="46" font-family="Arial,sans-serif" font-size="36" font-weight="bold"
        text-anchor="middle" fill="#fff">eV</text>
</svg>'''

svg_path = os.path.join(WWW, 'favicon.svg')
with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg_favicon)
print(f'Created favicon.svg')

# ── 2. FIX destination.html: col-md-4 → col-md-3 + reduce padding ─────────────
dest_path = os.path.join(WWW, 'destination.html')
with open(dest_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change country card columns from 3-col to 4-col grid
html = re.sub(r'class="col-md-4 ftco-animate"', 'class="col-md-3 col-sm-6 ftco-animate"', html)

# Reduce pb-5 on main content area (too much bottom padding)
html = html.replace('col-md-9 ftco-animate pb-5 text-center"', 'col-md-9 ftco-animate pb-3 text-center"')

# Add tighter margin CSS if not already present
if 'dest-grid-fix' not in html:
    css_fix = '''<style>
/* dest-grid-fix */
.project-wrap { margin-bottom: 12px; }
.project-wrap .img { height: 180px; }
.ftco-section { padding-top: 3rem !important; padding-bottom: 3rem !important; }
</style>'''
    html = html.replace('</head>', css_fix + '\n</head>', 1)

with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Fixed destination.html: 4-column grid')

# ── 3. FIX ALL PAGES: Guides nav + favicon link ───────────────────────────────
fixed_nav = 0
fixed_fav = 0

for fpath in glob.glob(os.path.join(WWW, '**', '*.html'), recursive=True):
    rel = os.path.relpath(fpath, WWW).replace('\\','/')
    parts = rel.split('/')
    page_depth = len(parts) - 1  # 0 = root, 1 = en/ fr/ etc.
    current_lang = parts[0] if page_depth == 1 and parts[0] in ['en','fr','es','pt'] else 'en'
    prefix = '../' if page_depth == 1 else ''

    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        original = html

        # ── Fix Guides nav link (check specifically for nav-link containing Guides) ──
        if 'langDropdown' in html and 'href=' in html:
            has_guides_nav = bool(re.search(r'nav-link[^>]*>[^<]*Guides', html))
            if not has_guides_nav:
                if current_lang == 'en':
                    guides_href = f'{prefix}retirement-visa-guide.html'
                else:
                    guides_href = f'{prefix}en/retirement-visa-guide.html'

                guides_item = f'\n                    <li class="nav-item"><a class="nav-link" href="{guides_href}">Guides</a></li>'

                # Insert after Blog nav item or before lang switcher
                if re.search(r'nav-link[^>]*>[^<]*Blog', html):
                    html = re.sub(
                        r'(<li class="nav-item"><a class="nav-link"[^>]*>Blog</a></li>)',
                        r'\1' + guides_item,
                        html, count=1
                    )
                else:
                    html = re.sub(
                        r'(<li class="nav-item dropdown ml-2">)',
                        guides_item + r'\n                    \1',
                        html, count=1
                    )
                if html != original:
                    fixed_nav += 1

        # ── Add SVG favicon link if not already present ──
        favicon_tag = '<link rel="icon" type="image/svg+xml" href="/favicon.svg"/>'
        if 'favicon.svg' not in html and '</head>' in html:
            html = html.replace('</head>', favicon_tag + '\n</head>', 1)
            fixed_fav += 1

        if html != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)

    except Exception as e:
        print(f'Error {rel}: {e}')

print(f'Guides nav added to: {fixed_nav} pages')
print(f'SVG favicon added to: {fixed_fav} pages')
