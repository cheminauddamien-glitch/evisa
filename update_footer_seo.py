#!/usr/bin/env python3
"""
Update footer across all HTML pages with SEO-optimized, consistent format.
"""

import os
import re
from pathlib import Path

# Footer translations
FOOTER_LABELS = {
    'en': {
        'title': 'Most Requested Visas',
        'copyright': '© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
        'legal': 'Legal Notice',
        'disclaimer': 'Disclaimer',
    },
    'fr': {
        'title': 'Visas les plus demandés',
        'copyright': '© 2026 eVisa-Card.com — Plateforme mondiale d\'information sur les eVisa &amp; voyages',
        'legal': 'Mentions légales',
        'disclaimer': 'Avertissement',
    },
    'es': {
        'title': 'Visas Más Solicitadas',
        'copyright': '© 2026 eVisa-Card.com — Plataforma Global de Información de eVisa y Viajes',
        'legal': 'Aviso Legal',
        'disclaimer': 'Descargo de Responsabilidad',
    },
    'pt': {
        'title': 'Vistos Mais Solicitados',
        'copyright': '© 2026 eVisa-Card.com — Plataforma Global de Informações de eVisa &amp; Viagens',
        'legal': 'Aviso Legal',
        'disclaimer': 'Isenção de Responsabilidade',
    },
    'zh': {
        'title': '最受欢迎的签证',
        'copyright': '© 2026 eVisa-Card.com — 全球电子签证和旅行信息平台',
        'legal': '法律声明',
        'disclaimer': '免责声明',
    },
    'ja': {
        'title': '人気のビザ',
        'copyright': '© 2026 eVisa-Card.com — グローバルeVisa＆旅行情報プラットフォーム',
        'legal': '法的通知',
        'disclaimer': '免責事項',
    },
    'ko': {
        'title': '인기있는 비자',
        'copyright': '© 2026 eVisa-Card.com — 글로벌 eVisa &amp; 여행 정보 플랫폼',
        'legal': '법적 고지',
        'disclaimer': '면책조항',
    },
    'ru': {
        'title': 'Наиболее запрашиваемые визы',
        'copyright': '© 2026 eVisa-Card.com — Глобальная платформа информации об электронных визах и путешествиях',
        'legal': 'Правовая информация',
        'disclaimer': 'Отказ от ответственности',
    },
    'ar': {
        'title': 'التأشيرات الأكثر طلباً',
        'copyright': '© 2026 eVisa-Card.com — منصة المعلومات العالمية للتأشيرات الإلكترونية والسفر',
        'legal': 'الإشعار القانوني',
        'disclaimer': 'إخلاء المسؤولية',
    },
    'th': {
        'title': 'วีซ่าที่ได้รับความนิยมมากที่สุด',
        'copyright': '© 2026 eVisa-Card.com — แพลตฟอร์มข้อมูลวีซ่าดิจิตัลและท่องเที่ยวทั่วโลก',
        'legal': 'หมายเหตุทางกฎหมาย',
        'disclaimer': 'ข้อความปฏิเสธความรับผิดชอบ',
    }
}

# Most requested visas list (name, slug without 'visa-' prefix, special_path if needed)
VISA_COUNTRIES = [
    ('Thailand', 'thailand', None),
    ('Vietnam', 'vietnam', None),
    ('India', 'india', None),
    ('Turkey', 'turkey', None),
    ('Japan', 'japan', None),
    ('China', 'china', None),
    ('Indonesia', 'indonesia', None),
    ('Malaysia', 'malaysia', None),
    ('Taiwan', 'taiwan', None),
    ('UAE', 'uae', None),
    ('Maldives', 'maldives', None),
    ('Sri Lanka', 'sri-lanka', None),
    ('Colombia', 'colombia', None),
    ('Egypt', 'egypt', None),
    ('Jordan', 'jordan', None),
    ('USA', 'usa', None),
    ('Canada', 'canada', None),
    ('Australia', 'australia', None),
    ('Schengen Visa', 'schengen', 'schengen-visa-guide-2026'),
]

def generate_footer_html(lang, is_root=False):
    """Generate SEO-optimized footer HTML for given language."""
    labels = FOOTER_LABELS.get(lang, FOOTER_LABELS['en'])
    base_path = '' if is_root else '../'
    img_path = f'{base_path}images/bg_3.jpg'

    # Build visa links
    visa_links = '\n                        '.join([
        f'<a href="/{lang}/{special_path or f"visa-{slug}"}" style="color:#cfd8e3;text-decoration:none;font-size:14px;transition:color .2s;">{name}</a>'
        for name, slug, special_path in VISA_COUNTRIES
    ])

    # Build footer
    footer = f'''<!-- ======== FOOTER (SEO-optimized with most requested visas) ======== -->
    <footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url({img_path});">
        <div class="container">
            <!-- Most Requested Visas Section -->
            <div class="row mb-5 justify-content-center">
                <div class="col-md-10 text-center">
                    <h2 style="font-size:18px;color:#ffffff;margin-bottom:16px;font-weight:600;letter-spacing:.5px;">{labels['title']}</h2>
                    <nav style="line-height:2;display:flex;flex-wrap:wrap;justify-content:center;gap:8px;">
                        {visa_links}
                    </nav>
                </div>
            </div>
            <!-- Copyright & Legal Section -->
            <div class="row mb-5 justify-content-center border-top" style="border-top:1px solid rgba(255,255,255,.1);padding-top:24px;">
                <div class="col-md-10 text-center">
                    <p style="color:#ffffff;font-size:14px;margin-bottom:8px;">{labels['copyright']}</p>
                    <p style="font-size:12px;color:#b0bcc6;margin:0;">
                        <a href="/{lang}/legal-notice" style="color:#b0bcc6;text-decoration:none;transition:color .2s;">{labels['legal']}</a>
                        <span style="margin:0 6px;">|</span>
                        <a href="/{lang}/disclaimer" style="color:#b0bcc6;text-decoration:none;transition:color .2s;">{labels['disclaimer']}</a>
                    </p>
                </div>
            </div>
        </div>
    </footer>'''

    return footer

def replace_footer_in_file(filepath, lang, is_root=False):
    """Replace footer in a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern 1: Match footer with HTML comment (<!-- ======== FOOTER ... --> ... </footer>)
    footer_pattern_1 = r'<!--\s*=+\s*FOOTER.*?-->.*?</footer>'
    # Pattern 2: Match footer without comment (<footer ... > ... </footer>)
    footer_pattern_2 = r'<footer\s+class="ftco-footer[^>]*>.*?</footer>'

    # Try pattern 1 first
    match = re.search(footer_pattern_1, content, re.DOTALL | re.IGNORECASE)
    if match:
        footer_pattern = footer_pattern_1
    else:
        # Try pattern 2
        match = re.search(footer_pattern_2, content, re.DOTALL | re.IGNORECASE)
        if match:
            footer_pattern = footer_pattern_2
        else:
            print(f"  [WARN] No footer pattern found in {filepath}")
            return False

    new_footer = generate_footer_html(lang, is_root)
    new_content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL | re.IGNORECASE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    www_path = Path('C:/Users/chemi/Documents/evisa/pacific-main/www')

    if not www_path.exists():
        print(f"[ERROR] {www_path} not found")
        return

    # Languages and their directories
    languages = {
        'en': None,  # Root level
        'fr': 'fr',
        'es': 'es',
        'pt': 'pt',
        'zh': 'zh',
        'ja': 'ja',
        'ko': 'ko',
        'ru': 'ru',
        'ar': 'ar',
        'th': 'th',
    }

    total_updated = 0

    for lang, lang_dir in languages.items():
        if lang_dir:
            target_dir = www_path / lang_dir
            print(f"\n[{lang.upper()}] Updating pages in {lang_dir}/")
        else:
            target_dir = www_path
            print(f"\n[EN] Updating English pages in root")

        if not target_dir.exists():
            print(f"  [ERROR] Directory not found: {target_dir}")
            continue

        html_files = sorted(target_dir.glob('*.html'))

        if not html_files:
            print(f"  [INFO] No HTML files found")
            continue

        for html_file in html_files:
            # Skip system files
            if html_file.name in ['flaticon.html']:
                continue

            is_root = (lang == 'en' and lang_dir is None)
            if replace_footer_in_file(str(html_file), lang, is_root):
                print(f"  [OK] {html_file.name}")
                total_updated += 1
            else:
                print(f"  [FAIL] {html_file.name}")

    print(f"\n[DONE] Footer updated in {total_updated} HTML files")

if __name__ == '__main__':
    main()
