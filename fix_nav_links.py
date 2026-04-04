"""
Fix navigation links in all HTML files under language subdirectories.

Rules:
1. navbar-brand logo link: ../index.html -> /{lang}/destination.html
2. Home/Accueil nav-item link: ../index.html -> /{lang}/destination.html
3. Destinations nav-item link: ../destination.html -> /{lang}/destination.html
4. About nav-item link: keep ../about.html (no translated page)
5. Blog nav-item link: keep ../blog.html (no translated page)

Only modifies links inside <nav> blocks, not elsewhere in the page.
"""

import os
import re

LANGUAGES = ["fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www")


def fix_nav_links_in_file(filepath, lang):
    """Fix nav links in a single HTML file. Returns True if the file was modified."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # We need to only replace links inside <nav>...</nav> blocks.
    # Strategy: find all <nav ...>...</nav> sections and do replacements within them.

    def fix_nav_block(match):
        nav_html = match.group(0)

        # 1. Fix navbar-brand logo link: href="../index.html" -> href="/{lang}/destination.html"
        #    Pattern: <a class="navbar-brand" href="../index.html"
        nav_html = re.sub(
            r'(<a\s+class="navbar-brand"\s+href=")\.\.\/index\.html(")',
            rf'\g<1>/{lang}/destination.html\2',
            nav_html
        )

        # 2. Fix Home/Accueil nav-link: href="../index.html" inside nav-item
        #    Pattern: <li class="nav-item"><a class="nav-link" href="../index.html">
        #    Also handle variations with "active" class: class="nav-link active"
        nav_html = re.sub(
            r'(<li\s+class="nav-item">\s*<a\s+class="nav-link(?:\s+active)?"?\s+href=")\.\.\/index\.html(")',
            rf'\g<1>/{lang}/destination.html\2',
            nav_html
        )

        # 3. Fix Destinations nav-link: href="../destination.html" inside nav-item
        #    Pattern: <li class="nav-item"><a class="nav-link" href="../destination.html">
        #    Also handle "active" class variant
        nav_html = re.sub(
            r'(<li\s+class="nav-item">\s*<a\s+class="nav-link(?:\s+active)?"?\s+href=")\.\.\/destination\.html(")',
            rf'\g<1>/{lang}/destination.html\2',
            nav_html
        )

        # About (../about.html) and Blog (../blog.html) are kept as-is.
        return nav_html

    # Replace within all <nav ...>...</nav> blocks (non-greedy, DOTALL)
    content = re.sub(
        r'<nav\b[^>]*>.*?</nav>',
        fix_nav_block,
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    total_updated = 0
    total_scanned = 0
    per_lang_counts = {}

    for lang in LANGUAGES:
        lang_dir = os.path.join(BASE_DIR, lang)
        if not os.path.isdir(lang_dir):
            print(f"WARNING: Directory not found: {lang_dir}")
            continue

        lang_updated = 0
        for filename in os.listdir(lang_dir):
            if not filename.endswith(".html"):
                continue
            filepath = os.path.join(lang_dir, filename)
            total_scanned += 1
            if fix_nav_links_in_file(filepath, lang):
                lang_updated += 1

        per_lang_counts[lang] = lang_updated
        total_updated += lang_updated
        print(f"  {lang}: {lang_updated} files updated")

    print(f"\nTotal files scanned: {total_scanned}")
    print(f"Total files updated: {total_updated}")


if __name__ == "__main__":
    main()
