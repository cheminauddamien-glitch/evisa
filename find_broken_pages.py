import re, glob, os

def has_meta(h):
    return bool(re.search(r'<meta[^>]*name=["\']description["\']', h, re.I))
def has_canon(h):
    return bool(re.search(r'<link[^>]*rel=["\']canonical["\']', h, re.I))
def has_h1(h):
    return bool(re.search(r'<h1[^>]*>', h, re.I))

EXCLUDE = ('for-', '-visa-', 'requirement', 'extension', 'fee', 'processing')

print('=== Pages MISSING meta description or H1 ===\n')
for lang in ['en','es','fr','pt']:
    for pattern in ['visa-*.html', '*-visa-requirements.html', '*-visa-fees.html',
                    '*-visa-processing-time.html', '*-visa-extension.html']:
        files = glob.glob(f'www/{lang}/{pattern}')
        if pattern == 'visa-*.html':
            files = [f for f in files if not any(s in os.path.basename(f) for s in EXCLUDE)]
        for f in files:
            with open(f, encoding='utf-8', errors='replace') as fh:
                h = fh.read()
            issues = []
            if not has_meta(h): issues.append('no-meta')
            if not has_canon(h): issues.append('no-canon')
            if not has_h1(h): issues.append('no-h1')
            if issues:
                print(f'  {f}  --> {",".join(issues)}')
