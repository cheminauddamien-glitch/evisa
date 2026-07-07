#!/usr/bin/env python3
"""
Fix duplicate meta descriptions that hurt CTR.
Keep the longer/better description, remove the weaker one.
"""

import re
from pathlib import Path

def fix_duplicate_descriptions(filepath):
    """Remove duplicate meta descriptions, keep the better one."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find both types of description meta tags
    pattern1 = re.compile(r'<meta name="description" content="([^"]*)"', re.IGNORECASE)
    pattern2 = re.compile(r'<meta content="([^"]*)" name="description"', re.IGNORECASE)

    match1 = pattern1.search(content)
    match2 = pattern2.search(content)

    if not (match1 and match2):
        return False  # No duplicate found

    desc1, desc2 = match1.group(1), match2.group(1)

    # Score descriptions: prefer ones with specific details (USD, visa fees, numbers, days)
    def score_description(desc):
        score = 0
        if any(word in desc.lower() for word in ['usd', 'fee', 'cost', 'price', 'day', 'hours']):
            score += 50
        if any(char.isdigit() for char in desc):
            score += 30
        if 'requirements' in desc.lower():
            score += 20
        score += len(desc) * 0.1  # Prefer longer descriptions
        return score

    score1, score2 = score_description(desc1), score_description(desc2)

    # Remove the lower-scoring description
    if score1 >= score2:
        remove = match2.group(0)
    else:
        remove = match1.group(0)

    # Remove the duplicate
    new_content = content.replace(remove, '', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    www_path = Path('C:/Users/chemi/Documents/evisa/pacific-main/www')

    fixed = 0
    checked = 0

    for html_file in sorted(www_path.rglob('*.html')):
        if 'flaticon' in str(html_file):
            continue

        checked += 1
        if fix_duplicate_descriptions(html_file):
            fixed += 1
            print(f"[FIXED] {html_file.relative_to(www_path)}")

    print(f"\n[SUMMARY] Checked {checked} files, fixed {fixed} files with duplicate descriptions")

if __name__ == '__main__':
    main()
