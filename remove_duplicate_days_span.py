#!/usr/bin/env python3
"""
Remove duplicate <span class="days">...</span> tags from all pages
Keep <span class="price">...</span> tags on image overlays
"""

import re
from pathlib import Path

def remove_days_span(filepath):
    """Remove <span class="days">...</span> from file"""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Pattern to match <span class="days">...</span>
    pattern = r'<span class="days">[^<]*</span>\s*'

    if re.search(pattern, content):
        new_content = re.sub(pattern, '', content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True

    return False

def main():
    www_path = Path('C:/Users/chemi/Documents/evisa/pacific-main/www')

    removed = 0
    checked = 0

    for html_file in sorted(www_path.rglob('*.html')):
        if 'flaticon' in str(html_file):
            continue

        checked += 1
        if remove_days_span(html_file):
            removed += 1
            if removed % 100 == 0:
                print(f"[OK] {removed} files processed...")

    print(f"\n[COMPLETE] Removed <span class=\"days\"> from {removed}/{checked} files")

if __name__ == '__main__':
    main()
