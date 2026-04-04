#!/usr/bin/env python3
"""
normalize_priority_pages.py
Normalise CSS + JS only on PRIORITY pages (guide pages, index pages, guide articles).
Skips the ~12 000 individual visa pages.
"""
import os, re, glob

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
LANGS = ["en","fr","es","pt","zh","th","ru","ar","ja","ko"]

STD_CSS = """    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&amp;display=swap" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/owl.carousel.min.css" rel="stylesheet"/>
    <link href="../css/owl.theme.default.min.css" rel="stylesheet"/>
    <link href="../css/magnific-popup.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>"""

STD_JS_BLOCK = """<script src="../js/jquery.min.js"></script>
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

# Patterns to REMOVE from <head> (will be replaced by STD_CSS)
REMOVE_PATTERNS = [
    r'[ \t]*<link[^>]*fonts\.googleapis\.com[^>]*(Poppins)[^>]*>\n?',
    r'[ \t]*<link[^>]*fonts\.googleapis\.com[^>]*(Arizonia)[^>]*>\n?',
    r'[ \t]*<link[^>]*font-awesome[^>]*>\n?',
    r'[ \t]*<link[^>]*flag-icons[^>]*>\n?',
    r'[ \t]*<link[^>]*animate\.css[^>]*>\n?',
    r'[ \t]*<link[^>]*owl\.carousel\.min\.css[^>]*>\n?',
    r'[ \t]*<link[^>]*owl\.theme\.default\.min\.css[^>]*>\n?',
    r'[ \t]*<link[^>]*magnific-popup\.css[^>]*>\n?',
    r'[ \t]*<link[^>]*["\']\.\.\/css\/bootstrap\.min\.css["\'][^>]*>\n?',
    r'[ \t]*<link[^>]*["\']bootstrap\.min\.css["\'][^>]*>\n?',
    r'[ \t]*<link[^>]*style\.css[^>]*>\n?',
    r'[ \t]*<link[^>]*bootstrap-datepicker\.css[^>]*>\n?',
    r'[ \t]*<link[^>]*jquery\.timepicker\.css[^>]*>\n?',
    r'[ \t]*<link[^>]*flaticon\.css[^>]*>\n?',
]

CJK_PATTERN = re.compile(
    r'[ \t]*<link[^>]*fonts\.googleapis\.com[^>]*(?:Noto|Sarabun|IBM.Plex|Tajawal|Nanum)[^>]*>\n?',
    re.IGNORECASE
)

def collect_priority_files():
    """Return list of (filepath) for priority pages only."""
    files = []
    for lang in LANGS:
        d = os.path.join(BASE, lang)
        if not os.path.isdir(d):
            continue
        for fname in os.listdir(d):
            if not fname.endswith(".html"):
                continue
            # Only process guide/index pages, not individual visa pages
            if any([
                fname.startswith("expat-guide"),
                fname.startswith("best-countries"),
                fname.startswith("digital-nomad"),
                fname.startswith("schengen"),
                fname.startswith("retirement"),
                fname.startswith("cheapest"),
                fname == "expat-guides.html",
                fname == "index.html",
                fname == "destination.html",
                fname == "about.html",
                fname == "blog.html",
            ]):
                files.append(os.path.join(d, fname))
    return files

def normalize_file(filepath):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()
    original = html

    # Extract CJK/special fonts to preserve
    cjk_fonts = CJK_PATTERN.findall(html)

    # Remove existing CSS links
    for pat in REMOVE_PATTERNS:
        html = re.sub(pat, '', html, flags=re.IGNORECASE)

    # Clean up multiple blank lines
    html = re.sub(r'\n{3,}', '\n\n', html)

    # Insert STD_CSS before </head> if not already normalised
    if 'owl.carousel.min.css' not in html:
        extra = ''
        if cjk_fonts:
            extra = '\n    ' + '\n    '.join([f.strip() for f in cjk_fonts])
        html = html.replace('</head>', STD_CSS + extra + '\n</head>', 1)

    # Replace JS block at end of file
    # Remove existing script src lines just before </body></html>
    html = re.sub(
        r'(\s*<script src="[^"]*"></script>)+\s*</body>\s*</html>\s*$',
        '\n' + STD_JS_BLOCK,
        html.rstrip(),
        flags=re.IGNORECASE
    )

    if html != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    files = collect_priority_files()
    print(f"Priority files to process: {len(files)}")
    updated = 0
    for fp in files:
        if normalize_file(fp):
            updated += 1
            rel = os.path.relpath(fp, BASE)
            print(f"  OK {rel}")
    print(f"\nDone: {updated}/{len(files)} files updated.")

if __name__ == "__main__":
    main()
