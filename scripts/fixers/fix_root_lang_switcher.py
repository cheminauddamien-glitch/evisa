"""
Fix lang switcher on ROOT pages (depth 0: destination.html, index.html, blog.html etc.)
These pages don't have FR/ES/PT counterparts, so all lang links should fallback to /destination.html
Also add a stronger 4-column CSS override to style.css
"""
import os, re, glob

WWW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www')
fixed = 0
errors = []

# Root HTML pages
root_pages = glob.glob(os.path.join(WWW, '*.html'))

for fpath in root_pages:
    rel = os.path.basename(fpath)
    slug = rel.replace('.html', '')

    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()

        if 'langDropdown' not in html:
            continue

        original = html

        # Build correct lang switcher for root pages
        # EN stays on current page, FR/ES/PT → /destination.html (fallback)
        en_href = f'/{slug}.html' if slug != 'index' else '/'
        fr_href = f'/fr/{slug}.html' if os.path.exists(os.path.join(WWW, 'fr', rel)) else '/destination.html'
        es_href = f'/es/{slug}.html' if os.path.exists(os.path.join(WWW, 'es', rel)) else '/destination.html'
        pt_href = f'/pt/{slug}.html' if os.path.exists(os.path.join(WWW, 'pt', rel)) else '/destination.html'

        new_items = (
            f'<a class="dropdown-item active" href="{en_href}"><span class="fi fi-gb"></span> English</a>\n'
            f'          <a class="dropdown-item" href="{fr_href}"><span class="fi fi-fr"></span> Fran&#231;ais</a>\n'
            f'          <a class="dropdown-item" href="{es_href}"><span class="fi fi-es"></span> Espa&#241;ol</a>\n'
            f'          <a class="dropdown-item" href="{pt_href}"><span class="fi fi-br"></span> Portugu&#234;s</a>'
        )

        # Replace dropdown menu contents
        html = re.sub(
            r'(<div class="dropdown-menu[^"]*"[^>]*>)(.*?)(</div>)',
            lambda m: m.group(1) + '\n          ' + new_items + '\n        ' + m.group(3),
            html,
            count=1,
            flags=re.DOTALL
        )

        # Fix the button to show "English" flag
        html = re.sub(
            r'(<a[^>]*id="langDropdown"[^>]*>).*?(</a>)',
            r'\1\n              <span class="fi fi-gb"></span> English</a>',
            html,
            count=1,
            flags=re.DOTALL
        )

        if html != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            fixed += 1
            print(f'  Fixed: {rel}')

    except Exception as e:
        errors.append(f'{rel}: {e}')

print(f'\nRoot pages fixed: {fixed}')
if errors:
    for e in errors: print(f'  ERROR: {e}')
else:
    print('No errors')

# ─── ALSO FIX EN/FR/ES/PT pages with broken é/ñ encoding in lang labels ───────
# The fix_navbar_lang.py wrote UTF-8 chars that got corrupted.
# Replace Fran? / Espa? / Portugu? with HTML entities in ALL pages

print('\nFixing encoding in lang labels across all pages...')
enc_fixed = 0

all_pages = glob.glob(os.path.join(WWW, '**', '*.html'), recursive=True)
for fpath in all_pages:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        original = html

        # Fix corrupted French/Spanish/Portuguese label text in dropdown items
        html = re.sub(r'Fran[^\w<"]*ais', 'Fran&#231;ais', html)
        html = re.sub(r'Espa[^\w<"]*ol', 'Espa&#241;ol', html)
        html = re.sub(r'Portugu[^\w<"]*s', 'Portugu&#234;s', html)
        # Also fix correct UTF-8 versions to entities (for consistency in HTML)
        html = html.replace('Français', 'Fran&#231;ais')
        html = html.replace('Español', 'Espa&#241;ol')
        html = html.replace('Português', 'Portugu&#234;s')

        if html != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            enc_fixed += 1

    except Exception as e:
        pass

print(f'Encoding fixed on: {enc_fixed} pages')

# ─── ADD STRONGER CSS GRID OVERRIDE ───────────────────────────────────────────
css_path = os.path.join(WWW, 'css', 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

extra_css = """
/* ===== FORCE 4-COLUMN GRID ON DESTINATION PAGE ===== */
@media (min-width: 768px) {
  .destination-grid .col-md-3,
  #asia .col-md-3,
  #europe .col-md-3,
  #americas .col-md-3,
  #middleeast .col-md-3,
  #oceania .col-md-3 {
    flex: 0 0 25% !important;
    max-width: 25% !important;
  }
}
"""

if 'FORCE 4-COLUMN GRID' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(extra_css)
    print('Added stronger 4-column CSS override')
else:
    print('4-column CSS already present')
