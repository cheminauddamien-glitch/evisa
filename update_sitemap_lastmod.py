#!/usr/bin/env python3
"""
Update lastmod date in sitemap.xml to today's date
"""
import re
from pathlib import Path

sitemap_path = Path('C:/Users/chemi/Documents/evisa/pacific-main/www/sitemap.xml')

with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all lastmod dates with today
new_date = '2026-06-05'
new_content = re.sub(r'<lastmod>\d{4}-\d{2}-\d{2}</lastmod>', f'<lastmod>{new_date}</lastmod>', content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Count
count = len(re.findall(r'<lastmod>', new_content))
print(f"[OK] Updated {count} lastmod entries to {new_date}")
