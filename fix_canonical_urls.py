"""Strip .html from all canonical, og:url, and hreflang href values
across the entire site to match the deployed clean-URL convention.

This fixes 'duplicate canonical' issues reported by GSC where the
canonical pointed to a .html version that Google saw as a separate URL.
"""
import re, glob, os
from collections import Counter

LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']

# Match an evisa-card.com URL ending in .html  (capture base without .html)
URL_RE = re.compile(r'(https://(?:www\.)?evisa-card\.com/[a-z]{2}/[A-Za-z0-9_\-]+)\.html\b')

stats = Counter()


def strip_html(html):
    """Replace every evisa-card.com/{lang}/...html with the clean URL form
    inside link[canonical], link[hreflang], and meta[og:url|og:title not allowed]
    Tags processed:
      - <link rel="canonical" href="X.html"> → href="X"
      - <link rel="alternate" hreflang="X" href="Y.html"> → href="Y"
      - <meta property="og:url" content="X.html"> → content="X"
    """
    # Replace ALL evisa-card.com/.../.html occurrences. Safe because we only
    # touch absolute eVisa-Card URLs. Internal page-content references stay.
    new, n = URL_RE.subn(r'\1', html)
    return new, n


def process(path):
    try:
        with open(path, encoding='utf-8') as f:
            html = f.read()
    except Exception:
        stats['errors'] += 1
        return
    new, n = strip_html(html)
    if n == 0:
        stats['no_change'] += 1
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)
    stats['changed'] += 1
    stats['urls_stripped'] += n


def main():
    for lang in LANGS:
        files = glob.glob(f'www/{lang}/*.html')
        for f in files:
            process(f)
        print(f'  {lang}: processed {len(files)} | changed so far: {stats["changed"]} | URLs stripped: {stats["urls_stripped"]}')
    print(f'\nFINAL: changed={stats["changed"]}, no_change={stats["no_change"]}, '
          f'urls_stripped={stats["urls_stripped"]}, errors={stats["errors"]}')


if __name__ == '__main__':
    main()
