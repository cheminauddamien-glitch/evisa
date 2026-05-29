"""Strip .html from internal page links so crawlers hit clean URLs directly
(no 301 hop). This is the root-cause fix for the GSC "Page avec redirection"
report: ~360k internal links currently point to .html URLs that redirect.

Safe rules:
- Only touches href="..." values.
- Only strips .html from INTERNAL page links (no scheme, not an asset).
- Preserves #fragment and ?query.
- index.html / ../index.html / /xx/index.html -> homepage-relative clean form.
- NEVER touches .css/.js/.png/.jpg/.svg/.ico/.xml/.json/.woff or external URLs.
"""
import os, re, glob, sys

ROOT = r'C:\Users\chemi\Documents\evisa\pacific-main'
LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']

# href="VALUE" where VALUE ends in .html (optionally + #frag / ?query),
# VALUE has no scheme (no "://") and is therefore internal.
LINK_RE = re.compile(r'href="(?!https?://|//|mailto:|tel:)([^"]+?)\.html((?:#|\?)[^"]*)?"')


def transform(m):
    path = m.group(1)
    suffix = m.group(2) or ''
    # Homepage special case: .../index -> directory root
    base = path.rsplit('/', 1)[-1]
    if base == 'index':
        parent = path[:-len('index')]  # keep trailing slash/prefix
        new = parent if parent else '/'
        return f'href="{new}{suffix}"'
    return f'href="{path}{suffix}"'


def process(path):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    new = LINK_RE.sub(transform, html)
    if new != html:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new)
        return LINK_RE.subn(transform, html)[1]  # count (on original)
    return 0


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    files = []
    if only and only.endswith('.html'):
        files = [only]
    else:
        for lang in LANGS:
            files += glob.glob(os.path.join(ROOT, 'www', lang, '*.html'))
        files += glob.glob(os.path.join(ROOT, 'www', '*.html'))
    total_files = changed_files = total_links = 0
    for f in files:
        total_files += 1
        n = process(f)
        if n:
            changed_files += 1
            total_links += n
    print(f'files scanned={total_files} changed={changed_files} links_stripped={total_links}')


if __name__ == '__main__':
    main()
