"""
Fix all pages in www/:
1. Language switcher 404 — fallback to /destination.html for pages without FR/ES/PT version
2. Add Destinations + Guides + Blog to navbar
3. Copyright 2025 → 2026
"""
import os, re, glob

WWW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www')

# Pages that have FR/ES/PT counterparts
def has_translation(slug):
    """True if fr/slug.html and es/slug.html and pt/slug.html all exist"""
    for lang in ['fr','es','pt']:
        if not os.path.exists(os.path.join(WWW, lang, slug + '.html')):
            return False
    return True

def fix_lang_switcher(html, slug, current_lang, page_depth):
    """Fix language switcher links — fallback to /destination.html if no translation exists"""
    langs = {
        'en': ('/en/' + slug + '.html', 'fi-gb', 'English'),
        'fr': ('/fr/' + slug + '.html', 'fi-fr', 'Français'),
        'es': ('/es/' + slug + '.html', 'fi-es', 'Español'),
        'pt': ('/pt/' + slug + '.html', 'fi-br', 'Português'),
    }
    fallback = '/destination.html'

    # Build new dropdown items
    items = []
    for lang, (href, flag, label) in langs.items():
        # Check if target page exists
        target_path = os.path.join(WWW, href.lstrip('/').replace('/', os.sep))
        if lang == current_lang:
            active = ' active'
            real_href = href
        elif os.path.exists(target_path):
            active = ''
            real_href = href
        else:
            active = ''
            real_href = fallback

        items.append(
            f'<a class="dropdown-item{active}" href="{real_href}">'
            f'<span class="fi {flag}"></span> {label}</a>'
        )

    new_dropdown = '\n          '.join(items)

    # Replace the dropdown-menu contents
    html = re.sub(
        r'(<div class="dropdown-menu[^>]*>)(.*?)(</div>)',
        lambda m: m.group(1) + '\n          ' + new_dropdown + '\n        ' + m.group(3),
        html,
        count=1,
        flags=re.DOTALL
    )

    # Fix the button label to show correct current language
    flag_map = {'en':'fi-gb','fr':'fi-fr','es':'fi-es','pt':'fi-br'}
    label_map = {'en':'English','fr':'Français','es':'Español','pt':'Português'}
    html = re.sub(
        r'(<a[^>]*id="langDropdown"[^>]*>).*?(<span class="fi fi-[a-z]+"></span>[^<]*</a>)',
        lambda m: m.group(1).rstrip() +
            f'\n              <span class="fi {flag_map[current_lang]}"></span> {label_map[current_lang]}</a>',
        html,
        count=1,
        flags=re.DOTALL
    )
    return html


def fix_navbar(html, current_lang, page_depth):
    """Add Destinations, Guides, Blog links to navbar if missing"""
    # Determine path prefix based on depth
    prefix = '../' if page_depth == 1 else ''  # depth 1 = en/ fr/ es/ pt/

    # Links to add
    dest_href   = f'{prefix}destination.html'
    guides_href = f'{prefix}en/retirement-visa-guide.html' if current_lang != 'en' else f'{prefix}retirement-visa-guide.html'
    blog_href   = f'{prefix}blog.html'

    # Only add if not already present
    new_items = ''
    if 'Destinations' not in html and 'destination.html' not in html:
        new_items += f'\n                    <li class="nav-item"><a class="nav-link" href="{dest_href}">Destinations</a></li>'
    if 'Guides' not in html:
        new_items += f'\n                    <li class="nav-item"><a class="nav-link" href="{guides_href}">Guides</a></li>'
    if '>Blog<' not in html:
        new_items += f'\n                    <li class="nav-item"><a class="nav-link" href="{blog_href}">Blog</a></li>'

    if new_items:
        # Insert before the lang switcher dropdown
        html = re.sub(
            r'(<li class="nav-item dropdown ml-2">)',
            new_items + r'\n                    \1',
            html,
            count=1
        )
    return html


def fix_copyright(html):
    """Update © 2025 to © 2026"""
    html = re.sub(r'©\s*2025', '© 2026', html)
    html = html.replace('copyright 2025', 'copyright 2026')
    html = html.replace('Copyright 2025', 'Copyright 2026')
    return html


# Process all pages
fixed = 0
errors = []

for fpath in glob.glob(os.path.join(WWW, '**', '*.html'), recursive=True):
    rel = os.path.relpath(fpath, WWW).replace('\\','/')
    parts = rel.split('/')

    # Determine language and depth
    if len(parts) == 1:
        current_lang = 'en'
        page_depth = 0
        slug = parts[0].replace('.html','')
    elif len(parts) == 2:
        lang_dir = parts[0]
        current_lang = lang_dir if lang_dir in ['en','fr','es','pt'] else 'en'
        page_depth = 1
        slug = parts[1].replace('.html','')
    else:
        continue

    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()

        original = html

        # Only fix lang switcher for pages in en/ or fr/ es/ pt/ subdirs
        if page_depth == 1 and 'langDropdown' in html:
            html = fix_lang_switcher(html, slug, current_lang, page_depth)

        # Add navbar links to all pages
        if 'langDropdown' in html:
            html = fix_navbar(html, current_lang, page_depth)

        # Fix copyright
        html = fix_copyright(html)

        if html != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            fixed += 1

    except Exception as e:
        errors.append(f'{rel}: {e}')

print(f'Fixed: {fixed} pages')
if errors:
    print(f'Errors ({len(errors)}):')
    for e in errors[:10]: print(' ', e)
else:
    print('No errors')
