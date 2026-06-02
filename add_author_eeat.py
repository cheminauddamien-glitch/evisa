"""Add the named editorial reviewer (Damien Cheminaud) to the E-E-A-T block of
every page, in a language-appropriate "Reviewed by" form. Idempotent.

PROD ONLY: edits C:\\Users\\chemi\\Documents\\evisa\\pacific-main\\www
"""
import re, glob, os

WWW = r'C:\Users\chemi\Documents\evisa\pacific-main\www'
AUTHOR = 'Damien Cheminaud'

REVIEWED = {
    'en': 'Reviewed by', 'fr': 'Révisé par', 'es': 'Revisado por',
    'pt': 'Revisado por', 'zh': '审核：', 'th': 'ตรวจสอบโดย',
    'ru': 'Проверено:', 'ar': 'مراجعة:', 'ja': '監修：', 'ko': '검토:',
}

ANCHOR = 'eVisa-Card.com</a></strong>'

n = 0
for f in glob.glob(os.path.join(WWW, '*', '*.html')):
    lang = f.replace('\\', '/').split('/')[-2]
    if lang not in REVIEWED:
        continue
    h = open(f, encoding='utf-8', errors='replace').read()
    if ANCHOR not in h or AUTHOR in h:
        continue
    label = REVIEWED[lang]
    repl = f'eVisa-Card.com</a> &middot; <span class="author">{label} {AUTHOR}</span></strong>'
    h2 = h.replace(ANCHOR, repl, 1)
    if h2 != h:
        open(f, 'w', encoding='utf-8').write(h2)
        n += 1

print('pages updated:', n)
