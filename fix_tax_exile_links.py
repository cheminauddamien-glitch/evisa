"""Point all tax-exile links to the French simulator on taxes-crypto.eu.

Current links use /en/fiscal-exile-simulator[/country]. Switch to
/fr/simulateur-exil-fiscal[/country]. Countries that have no French
per-country page (greece, spain -> 404) fall back to the FR base URL so no
link points to a 404.

PROD ONLY: C:\\Users\\chemi\\Documents\\evisa\\pacific-main\\www
"""
import glob, os

WWW = r'C:\Users\chemi\Documents\evisa\pacific-main\www'
BASE_EN = 'https://taxes-crypto.eu/en/fiscal-exile-simulator'
BASE_FR = 'https://taxes-crypto.eu/fr/simulateur-exil-fiscal'

# countries with NO French per-country page -> send to FR base
NO_FR_COUNTRY = ('greece', 'spain')

n_files = n_repl = 0
for f in glob.glob(os.path.join(WWW, '*', '*.html')):
    h = open(f, encoding='utf-8', errors='replace').read()
    if BASE_EN not in h:
        continue
    orig = h
    # 1) 404 per-country -> FR base
    for c in NO_FR_COUNTRY:
        h = h.replace(f'{BASE_EN}/{c}', BASE_FR)
    # 2) valid per-country prefix -> FR per-country
    h = h.replace(f'{BASE_EN}/', f'{BASE_FR}/')
    # 3) bare base -> FR base
    h = h.replace(BASE_EN, BASE_FR)
    if h != orig:
        open(f, 'w', encoding='utf-8').write(h)
        n_files += 1
        n_repl += orig.count(BASE_EN)

print(f'files updated: {n_files}, links replaced: {n_repl}')
