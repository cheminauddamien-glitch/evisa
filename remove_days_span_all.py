#!/usr/bin/env python3
"""
Remove all <span class="days">...</span> tags from all HTML files
"""

import re
from pathlib import Path

def main():
    www_path = Path('C:/Users/chemi/Documents/evisa/pacific-main/www')

    removed_count = 0
    total_files = 0

    for html_file in sorted(www_path.rglob('*.html')):
        if 'flaticon' in str(html_file):
            continue

        total_files += 1

        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Count matches before
        matches_before = len(re.findall(r'<span class="days">[^<]*</span>', content))

        if matches_before > 0:
            # Remove all occurrences
            new_content = re.sub(r'<span class="days">[^<]*</span>\s*\n?', '', content)

            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)

            removed_count += matches_before
            print(f"[REMOVED] {html_file.name}: {matches_before} span(s)")

    print(f"\n[COMPLETE] Total: {removed_count} <span class=\"days\"> tags removed from {total_files} files")

if __name__ == '__main__':
    main()
