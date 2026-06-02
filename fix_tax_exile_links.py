"""Point each page's tax-exile links to the matching-language simulator on
taxes-crypto.eu. The FR URL was only an example — links must be language-aware.

taxes-crypto.eu languages: en, fr, es, pt (also de/it/nl/tr, unused here).
evisa-card languages without a matching simulator language (zh, th, ru, ar,
ja, ko) fall back to the English simulator.

Per-country pages exist only for: georgia, malaysia, panama, paraguay,
portugal, thailand, uae. Any other country (e.g. greece, spain — 404 in every
language) links to the language base URL instead, so no link 404s.

PROD ONLY: C:\\Users\\chemi\\Documents\\evisa\\pacific-main\\www
"""
import glob, os, re

WWW = r'C:\Users\chemi\Documents\evisa\pacific-main\www'

BASE = {
    'en': 'https://taxes-crypto.eu/en/fiscal-exile-simulator',
    'fr': 'https://taxes-crypto.eu/fr/simulateur-exil-fiscal',
    'es': 'https://taxes-crypto.eu/es/simulador-exilio-fiscal',
    'pt': 'https://taxes-crypto.eu/pt/simulador-exilio-fiscal',
}
FALLBACK = 'en'  # for zh, th, ru, ar, ja, ko

VALID_COUNTRIES = {'georgia', 'malaysia', 'panama', 'paraguay',
                   'portugal', 'thailand', 'uae'}

# Match any existing taxes-crypto simulator link, capture optional country.
LINK = re.compile(
    r'https://taxes-crypto\.eu/[a-z]{2}/[a-z-]*(?:simul[a-z-]*|exil[a-z-]*)'
    r'(?:/([a-z-]+))?'
)

n_files = n_links = 0
for f in glob.glob(os.path.join(WWW, '*', '*.html')):
    lang = f.replace('\\', '/').split('/')[-2]
    base = BASE.get(lang, BASE[FALLBACK])
    h = open(f, encoding='utf-8', errors='replace').read()
    if 'taxes-crypto.eu' not in h:
        continue

    def repl(m):
        country = m.group(1)
        if country and country in VALID_COUNTRIES:
            return f'{base}/{country}'
        return base

    new = LINK.sub(repl, h)
    if new != h:
        n_links += len(LINK.findall(h))
        open(f, 'w', encoding='utf-8').write(new)
        n_files += 1

print(f'files updated: {n_files}, links rewritten: {n_links}')
