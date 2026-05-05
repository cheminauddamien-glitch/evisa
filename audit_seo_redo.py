import re, glob, os

def has_meta(h):
    return bool(re.search(r'<meta[^>]*name=["\']description["\']', h, re.I))
def has_canon(h):
    return bool(re.search(r'<link[^>]*rel=["\']canonical["\']', h, re.I))
def has_h1(h):
    return bool(re.search(r'<h1[^>]*>', h, re.I))

EXCLUDE = ('for-', '-visa-', 'requirement', 'extension', 'fee', 'processing')

for lang in ['en','es','fr','pt']:
    print(f'--- {lang} ---')
    for pattern, label in [
        ('visa-*.html','hub_country'),
        ('*-visa-requirements.html','requirements'),
        ('*-visa-fees.html','fees'),
        ('*-visa-processing-time.html','processing-time'),
        ('*-visa-extension.html','extension'),
    ]:
        files = glob.glob(f'www/{lang}/{pattern}')
        if pattern == 'visa-*.html':
            files = [f for f in files if not any(s in os.path.basename(f) for s in EXCLUDE)]
        nm=nc=nh=0
        for f in files:
            with open(f, encoding='utf-8', errors='replace') as fh:
                h = fh.read()
            if not has_meta(h): nm += 1
            if not has_canon(h): nc += 1
            if not has_h1(h): nh += 1
        print(f'  {label}: {len(files)} | no-meta={nm} | no-canon={nc} | no-h1={nh}')
