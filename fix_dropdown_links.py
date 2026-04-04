"""
Fix language dropdown links across all HTML files.

Problem: Many pages have dropdown-item links pointing to /{lang}/destination.html
instead of /{lang}/{current_filename}.

Fix: Replace href="/{lang}/destination.html" with href="/{lang}/{current_filename}"
but only for dropdown-item links, only if the target file exists, and skip
destination.html files themselves (their links are correct by definition).
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WWW_DIR = os.path.join(BASE_DIR, "www")

LANG_DIRS = ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]

# Regex to match dropdown-item links pointing to /{lang}/destination.html
# Captures: (1) everything before href, (2) the lang code, (3) everything after the href value
PATTERN = re.compile(
    r'(<a\s+class="dropdown-item[^"]*"\s+href=")/(' +
    '|'.join(LANG_DIRS) +
    r')/destination\.html(")'
)


def fix_file(filepath, filename, lang_dir):
    """Fix dropdown links in a single HTML file.

    Returns (num_replacements, num_skipped) tuple.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    replacements = 0
    skipped = 0

    def replace_match(match):
        nonlocal replacements, skipped
        prefix = match.group(1)     # '<a class="dropdown-item..." href="'
        target_lang = match.group(2) # e.g., 'zh'
        suffix = match.group(3)      # '"'

        # Check if the target file exists in the target language directory
        target_path = os.path.join(WWW_DIR, target_lang, filename)
        if os.path.exists(target_path):
            replacements += 1
            return f'{prefix}/{target_lang}/{filename}{suffix}'
        else:
            skipped += 1
            return match.group(0)  # Leave unchanged

    new_content = PATTERN.sub(replace_match, content)

    if replacements > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return replacements, skipped


def main():
    total_files_processed = 0
    total_files_modified = 0
    total_replacements = 0
    total_skipped = 0

    print("=" * 70)
    print("Fixing language dropdown links")
    print("=" * 70)
    print()

    for lang in LANG_DIRS:
        lang_path = os.path.join(WWW_DIR, lang)
        if not os.path.isdir(lang_path):
            print(f"[SKIP] Directory not found: {lang_path}")
            continue

        lang_files_processed = 0
        lang_files_modified = 0
        lang_replacements = 0
        lang_skipped = 0

        html_files = [f for f in os.listdir(lang_path) if f.endswith(".html")]

        for filename in html_files:
            # Skip destination.html - its links are correct by definition
            if filename == "destination.html":
                continue

            filepath = os.path.join(lang_path, filename)
            if not os.path.isfile(filepath):
                continue

            lang_files_processed += 1
            replacements, skipped = fix_file(filepath, filename, lang)

            if replacements > 0:
                lang_files_modified += 1

            lang_replacements += replacements
            lang_skipped += skipped

        print(f"[{lang.upper()}] Processed: {lang_files_processed:>5} files | "
              f"Modified: {lang_files_modified:>5} | "
              f"Links fixed: {lang_replacements:>6} | "
              f"Skipped (target missing): {lang_skipped:>4}")

        total_files_processed += lang_files_processed
        total_files_modified += lang_files_modified
        total_replacements += lang_replacements
        total_skipped += lang_skipped

    print()
    print("=" * 70)
    print(f"TOTAL: Processed {total_files_processed} files, "
          f"modified {total_files_modified}, "
          f"fixed {total_replacements} links, "
          f"skipped {total_skipped} (target file missing)")
    print("=" * 70)


if __name__ == "__main__":
    main()
