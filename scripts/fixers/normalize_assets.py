#!/usr/bin/env python3
"""
normalize_assets.py
Standardise CSS + JS on every HTML page under language subdirs (en/fr/es/pt/zh/th/ru/ar/ja/ko).
Goal: every page gets the same CSS/JS stack as the home page (minus CookieConsent / GTM).
"""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
LANGS = ["en","fr","es","pt","zh","th","ru","ar","ja","ko"]

# ── Standard CSS block (inserted after last <meta> / before </head>) ─────────
# Uses relative ../css/ paths for sub-directory pages.
STD_CSS = """\
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&amp;display=swap" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/owl.carousel.min.css" rel="stylesheet"/>
    <link href="../css/owl.theme.default.min.css" rel="stylesheet"/>
    <link href="../css/magnific-popup.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>"""

# ── Standard JS block (replaces all <script src> before </body>) ─────────────
STD_JS = """\
<script src="../js/jquery.min.js"></script>
<script src="../js/jquery-migrate-3.0.1.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/jquery.easing.1.3.js"></script>
<script src="../js/jquery.waypoints.min.js"></script>
<script src="../js/jquery.stellar.min.js"></script>
<script src="../js/owl.carousel.min.js"></script>
<script src="../js/jquery.magnific-popup.min.js"></script>
<script src="../js/scrollax.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""

# CSS tags that should be REMOVED (replaced by STD_CSS)
CSS_TO_REMOVE = [
    r'<link[^>]*fonts\.googleapis\.com[^>]*Poppins[^>]*>',
    r'<link[^>]*fonts\.googleapis\.com[^>]*Arizonia[^>]*>',
    r'<link[^>]*font-awesome[^>]*>',
    r'<link[^>]*flag-icons[^>]*>',
    r'<link[^>]*animate\.css[^>]*>',
    r'<link[^>]*owl\.carousel\.min\.css[^>]*>',
    r'<link[^>]*owl\.theme\.default\.min\.css[^>]*>',
    r'<link[^>]*magnific-popup\.css[^>]*>',
    r'<link[^>]*bootstrap\.min\.css[^>]*>',   # remove separate bootstrap.min.css (it's in style.css)
    r'<link[^>]*style\.css[^>]*>',
    r'<link[^>]*bootstrap-datepicker\.css[^>]*>',
    r'<link[^>]*jquery\.timepicker\.css[^>]*>',
    r'<link[^>]*flaticon\.css[^>]*>',
    r'<link[^>]*Noto\+Sans[^>]*>',   # CJK fonts — keep them? We'll preserve them separately
]

# CJK/Arabic fonts patterns to preserve (we'll re-add them after STD_CSS if present)
CJK_FONT_PATTERN = re.compile(
    r'<link[^>]*fonts\.googleapis\.com[^>]*(?:Noto|Sarabun|IBM\+Plex|Tajawal|Nanum|Noto\+Sans)[^>]*>',
    re.IGNORECASE
)

def normalize_file(filepath):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    original = html

    # 1. Extract CJK/special fonts to re-insert after standard CSS
    cjk_fonts = CJK_FONT_PATTERN.findall(html)

    # 2. Remove all existing CSS link tags (we'll replace with STD_CSS)
    for pat in CSS_TO_REMOVE:
        html = re.sub(pat, '', html, flags=re.IGNORECASE)

    # 3. Remove leftover blank lines from removed tags
    html = re.sub(r'\n\s*\n\s*\n', '\n\n', html)

    # 4. Insert STD_CSS before </head>
    if STD_CSS not in html:
        replacement = STD_CSS
        if cjk_fonts:
            replacement += '\n    ' + '\n    '.join(cjk_fonts)
        html = html.replace('</head>', replacement + '\n</head>', 1)

    # 5. Replace the JS block at end of body
    # Remove all existing <script src=...> before </body></html>
    html = re.sub(
        r'(\s*<script src="[^"]*"><\/script>)+(\s*<\/body>\s*<\/html>)',
        '\n' + STD_JS,
        html,
        flags=re.IGNORECASE
    )

    if html != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    total = updated = 0
    for lang in LANGS:
        lang_dir = os.path.join(BASE, lang)
        if not os.path.isdir(lang_dir):
            continue
        for fname in sorted(os.listdir(lang_dir)):
            if not fname.endswith(".html"):
                continue
            fpath = os.path.join(lang_dir, fname)
            total += 1
            if normalize_file(fpath):
                updated += 1

    print(f"Done: {updated}/{total} files normalised.")


if __name__ == "__main__":
    main()
