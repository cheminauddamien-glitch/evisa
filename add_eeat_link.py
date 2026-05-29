"""B) E-E-A-T: make the editorial-team attribution verifiable by linking it to
the per-language about-our-experts page. Turns the static
"<strong>… — eVisa-Card.com</strong>" inside .eeat-section into a link to the
expertise page (the key authorship signal core updates reward).

Universal anchor: the brand "eVisa-Card.com</strong>" inside the editorial
<strong>, present identically across all 10 languages.
"""
import re, glob, os, sys

ROOT = r'C:\Users\chemi\Documents\evisa\pacific-main'

# Match the editorial <strong>…(em-dash) eVisa-Card.com</strong>, capture the
# prefix up to and including the dash, so we only wrap the brand word.
PAT = re.compile(r'(<strong>[^<]*?(?:&#8212;|&mdash;|—)\s*)eVisa-Card\.com(</strong>)')


def process(path):
    p = path.replace('\\', '/').split('/')
    lang = p[-2]
    if lang not in ('en','fr','es','pt','zh','th','ru','ar','ja','ko'):
        return 0
    h = open(path, encoding='utf-8', errors='replace').read()
    if 'about-our-experts' in h and 'eeat-section' in h and PAT.search(h) is None:
        return 0
    if PAT.search(h) is None:
        return 0
    link = f'/{lang}/about-our-experts'
    new = PAT.sub(rf'\1<a href="{link}">eVisa-Card.com</a>\2', h, count=1)
    if new != h:
        open(path, 'w', encoding='utf-8').write(new)
        return 1
    return 0


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    files = [only] if only else glob.glob(os.path.join(ROOT, 'www', '*', '*.html'))
    n = sum(process(f) for f in files)
    print(f'eeat links added: {n}')


if __name__ == '__main__':
    main()
