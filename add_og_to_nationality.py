"""Add Open Graph tags to all nationality pages (visa-for-{nat}-citizens.html)
that don't already have them. Inserts OG block right after the canonical link.
"""
import os, re, glob, html as htmllib

LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']
TOTAL = 0
ADDED = 0
SKIPPED = 0
ERRORS = 0


def has_og(html):
    return bool(re.search(r'<meta[^>]*property=["\']og:title["\']', html, re.I))


def extract(html):
    title_m = re.search(r'<title>([^<]*)</title>', html, re.I)
    title = title_m.group(1).strip() if title_m else ''

    # Meta description (handle both attribute orders)
    desc = ''
    for pat in [
        r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']',
        r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']',
    ]:
        m = re.search(pat, html, re.I)
        if m:
            desc = m.group(1)
            break

    canon = ''
    for pat in [
        r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']',
        r'<link[^>]*href=["\']([^"\']*)["\'][^>]*rel=["\']canonical["\']',
    ]:
        m = re.search(pat, html, re.I)
        if m:
            canon = m.group(1)
            break

    return title, desc, canon


def og_block(title, desc, canon):
    # Escape for HTML attribute
    def esc(s):
        return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

    return (f'    <meta property="og:title" content="{esc(title)}"/>\n'
            f'    <meta property="og:description" content="{esc(desc)}"/>\n'
            f'    <meta property="og:type" content="website"/>\n'
            f'    <meta property="og:url" content="{esc(canon)}"/>\n'
            f'    <meta property="og:image" content="https://www.evisa-card.com/images/og-image.jpg"/>\n')


def process_file(path):
    global TOTAL, ADDED, SKIPPED, ERRORS
    TOTAL += 1
    try:
        with open(path, encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        ERRORS += 1
        return
    if has_og(html):
        SKIPPED += 1
        return
    title, desc, canon = extract(html)
    if not title or not canon:
        # Cannot insert OG without these
        ERRORS += 1
        return
    # If meta desc missing, fall back to title
    if not desc:
        desc = title
    og = og_block(title, desc, canon)

    # Insert right after the canonical line
    new = re.sub(
        r'(<link[^>]*rel=["\']canonical["\'][^>]*/>\s*\n)',
        r'\1' + og,
        html, count=1
    )
    if new == html:
        # Try the reversed pattern
        new = re.sub(
            r'(<link[^>]*href=["\'][^"\']+["\'][^>]*rel=["\']canonical["\'][^>]*/>\s*\n)',
            r'\1' + og,
            html, count=1
        )
    if new == html:
        ERRORS += 1
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)
    ADDED += 1


def main():
    for lang in LANGS:
        files = glob.glob(f'www/{lang}/*-visa-for-*-citizens.html')
        for f in files:
            process_file(f)
        print(f'  {lang}: processed {len(files)} (added so far: {ADDED}, skipped: {SKIPPED}, errors: {ERRORS})')
    print(f'\nFINAL: total={TOTAL}, added={ADDED}, skipped={SKIPPED}, errors={ERRORS}')


if __name__ == '__main__':
    main()
