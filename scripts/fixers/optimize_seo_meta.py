#!/usr/bin/env python3
"""
optimize_seo_meta.py
Step 1 of SEO plan: Optimize existing pages for better Google rankings.

1. Nationality pages: enrich title with "- Cost, Requirements & How to Apply"
2. ALL pages in en/: add missing hreflang tags (zh/th/ru/ar/ja/ko)
3. Propagate hreflang fixes to all 9 language dirs
"""
import os, re, glob

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"

ALL_LANGS = ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]

HREFLANG_TEMPLATE = '    <link rel="alternate" hreflang="{lang}" href="https://www.evisa-card.com/{lang}/{filename}"/>'
XDEFAULT_TEMPLATE = '    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{filename}"/>'


def get_filename_from_path(filepath):
    return os.path.basename(filepath)


def fix_title_nationality(html, filepath):
    """Enrich short nationality page titles."""
    fname = os.path.basename(filepath)
    # Only apply to nationality pages
    if '-visa-for-' not in fname or '-citizens' not in fname:
        return html

    # Check if title already has a dash suffix (already enriched)
    title_match = re.search(r'<title>([^<]+)</title>', html)
    if not title_match:
        return html

    title = title_match.group(1)

    # Skip if already has " - " or " — " suffix with keywords
    if ' — ' in title or ' - ' in title:
        return html

    # Add keyword suffix
    new_title = title + " — Requirements, Cost & How to Apply"
    html = html.replace(f'<title>{title}</title>', f'<title>{new_title}</title>')

    return html


def fix_hreflang(html, filepath, lang):
    """Add missing hreflang tags for all 10 languages."""
    filename = get_filename_from_path(filepath)

    # Check which hreflang tags already exist
    existing_langs = set(re.findall(r'hreflang="([a-z\-]+)"', html))

    # Remove x-default from the set for comparison
    existing_langs.discard("x-default")

    # If all 10 languages are already present, skip
    if all(l in existing_langs for l in ALL_LANGS):
        return html

    # Check if the file exists in each language dir
    available_langs = []
    for l in ALL_LANGS:
        lang_file = os.path.join(BASE, l, filename)
        if os.path.isfile(lang_file):
            available_langs.append(l)

    # If no new languages to add, skip
    new_langs = [l for l in available_langs if l not in existing_langs]
    if not new_langs:
        return html

    # Build the new hreflang block
    new_hreflang_lines = []
    for nl in new_langs:
        new_hreflang_lines.append(HREFLANG_TEMPLATE.format(lang=nl, filename=filename))

    # Find where to insert - after the last existing hreflang tag
    # Find the x-default line or the last hreflang line
    lines = html.split('\n')
    insert_idx = None

    for i, line in enumerate(lines):
        if 'hreflang="x-default"' in line:
            insert_idx = i  # Insert before x-default
            break
        if 'hreflang=' in line:
            insert_idx = i + 1  # After last hreflang

    if insert_idx is None:
        # No hreflang found - insert before </head>
        for i, line in enumerate(lines):
            if '</head>' in line:
                insert_idx = i
                break

    if insert_idx is not None:
        # Insert new hreflang lines
        for j, new_line in enumerate(new_hreflang_lines):
            lines.insert(insert_idx + j, new_line)
        html = '\n'.join(lines)

    return html


def process_file(filepath, lang):
    """Process a single HTML file."""
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    original = html

    # 1. Fix nationality page titles (EN only - other langs keep translated titles)
    if lang == "en":
        html = fix_title_nationality(html, filepath)

    # 2. Add missing hreflang tags
    html = fix_hreflang(html, filepath, lang)

    if html != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    total = 0
    updated = 0

    for lang in ALL_LANGS:
        lang_dir = os.path.join(BASE, lang)
        if not os.path.isdir(lang_dir):
            continue

        html_files = glob.glob(os.path.join(lang_dir, "*.html"))
        for filepath in html_files:
            filename = os.path.basename(filepath)
            # Skip non-indexable pages
            if filename in ("index.html",) and lang not in ("en",):
                # Skip redirect index pages
                with open(filepath, encoding="utf-8", errors="ignore") as f:
                    chunk = f.read(2048)
                if "noindex" in chunk:
                    continue

            total += 1
            if process_file(filepath, lang):
                updated += 1

        print(f"  {lang}: processed {len(html_files)} files")

    print(f"\nDone: {updated}/{total} files updated.")


if __name__ == "__main__":
    main()
