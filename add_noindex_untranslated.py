"""Add noindex to all non-English pages (untranslated — content is still English).
Temporary measure to stop the GSC 'duplicate, Google chose different canonical' error.
noindex is removed per-language as translation completes.

EN pages are untouched. Pages already noindex stay noindex.
"""
import os, re, glob

LANGS = ['fr','es','pt','zh','th','ru','ar','ja','ko']
ROOT = r'C:\Users\chemi\Documents\evisa\pacific-main'

NOINDEX_META = '    <meta name="robots" content="noindex, follow"/>\n'

changed = already = added = errors = 0

for lang in LANGS:
    files = glob.glob(os.path.join(ROOT, 'www', lang, '*.html'))
    for f in files:
        try:
            with open(f, encoding='utf-8') as fh:
                html = fh.read()
        except Exception:
            errors += 1
            continue

        m = re.search(r'<meta[^>]*name=["\']robots["\'][^>]*>', html, re.I)
        if m:
            tag = m.group(0)
            if 'noindex' in tag.lower():
                already += 1
                continue
            # Replace index -> noindex inside the existing tag
            new_tag = re.sub(r'index', 'noindex', tag, count=1, flags=re.I)
            # Guard: don't double-prefix (e.g. 'noindex' already)
            new_tag = new_tag.replace('nonoindex', 'noindex')
            new_html = html.replace(tag, new_tag, 1)
            changed += 1
        else:
            # No robots meta — insert one after <head> or before </head>
            if '<head>' in html:
                new_html = html.replace('<head>', '<head>\n' + NOINDEX_META, 1)
            else:
                new_html = html.replace('</head>', NOINDEX_META + '</head>', 1)
            added += 1

        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_html)

    print(f'  {lang}: {len(files)} files processed')

print(f'\nFINAL: changed index->noindex={changed}, added new meta={added}, '
      f'already noindex={already}, errors={errors}')
print(f'TOTAL noindexed: {changed + added}')
