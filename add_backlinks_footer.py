#!/usr/bin/env python3
"""
Add backlinks to taxes-crypto.eu simulator + popular keywords to footer
All pages: New footer with keywords
Tax exile pages: Body section before footer
"""

import re
from pathlib import Path

# Tax exile simulator URLs by language
TAX_URLS = {
    'en': 'https://taxes-crypto.eu/en/simulateur-exil-fiscal',
    'fr': 'https://taxes-crypto.eu/fr/simulateur-exil-fiscal',
    'es': 'https://taxes-crypto.eu/es/simulador-exilio-fiscal',
    'pt': 'https://taxes-crypto.eu/pt/simulador-exilio-fiscal',
    'zh': 'https://taxes-crypto.eu/fr/simulateur-exil-fiscal',
    'ja': 'https://taxes-crypto.eu/en/simulateur-exil-fiscal',
    'ko': 'https://taxes-crypto.eu/en/simulateur-exil-fiscal',
    'ru': 'https://taxes-crypto.eu/en/simulateur-exil-fiscal',
    'ar': 'https://taxes-crypto.eu/en/simulateur-exil-fiscal',
    'th': 'https://taxes-crypto.eu/en/simulateur-exil-fiscal',
}

# Popular keywords by language
KEYWORDS = {
    'en': [
        ('cappadocia-visa-requirements', 'Cappadocia visa'),
        ('machu-picchu-visa-requirements', 'Machu Picchu'),
        ('taipei-visa-requirements', 'Taipei visa'),
        ('patagonia-visa-requirements', 'Patagonia'),
    ],
    'fr': [
        ('cappadocia-visa-requirements', 'Visa Cappadocia'),
        ('machu-picchu-visa-requirements', 'Machu Picchu'),
        ('taipei-visa-requirements', 'Visa Taipei'),
        ('patagonia-visa-requirements', 'Patagonie'),
    ],
    'es': [
        ('cappadocia-visa-requirements', 'Visa Capadocia'),
        ('machu-picchu-visa-requirements', 'Machu Picchu'),
        ('taipei-visa-requirements', 'Visa Taipei'),
        ('patagonia-visa-requirements', 'Patagonia'),
    ],
    'pt': [
        ('cappadocia-visa-requirements', 'Visto Capadócia'),
        ('machu-picchu-visa-requirements', 'Machu Picchu'),
        ('taipei-visa-requirements', 'Visto Taipei'),
        ('patagonia-visa-requirements', 'Patagônia'),
    ],
    'zh': [
        ('cappadocia-visa-requirements', '卡帕多奇亚签证'),
        ('machu-picchu-visa-requirements', '马丘比丘'),
        ('taipei-visa-requirements', '台北签证'),
        ('patagonia-visa-requirements', '巴塔哥尼亚'),
    ],
}

# Keywords section HTML
def get_keywords_section(lang):
    """Generate popular keywords section for footer"""
    keywords = KEYWORDS.get(lang, KEYWORDS['en'])
    links = '\n                    '.join([
        f'<a href="/{lang}/{slug}" style="color:#000000;text-decoration:none;">{name}</a>'
        for slug, name in keywords
    ])

    return f'''<div class="row mb-5 justify-content-center">
                <div class="col-md-10 text-center">
                    <p style="font-size:12px;color:#000000;margin-bottom:8px;">Popular searches:</p>
                    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px;font-size:13px;">
                        {links}
                    </div>
                </div>
            </div>'''

# Tax simulator section for body
def get_tax_body_section(lang):
    """Generate tax simulator section for body (tax exile pages only)"""
    tax_url = TAX_URLS.get(lang, TAX_URLS['en'])
    labels = {
        'en': 'Tax Exile Simulator',
        'fr': "Simulateur d'exil fiscal",
        'es': 'Simulador de exilio fiscal',
        'pt': 'Simulador de exílio fiscal',
        'zh': '税务流亡模拟器',
        'ja': '税務亡命ガイド',
        'ko': '세금 망명 가이드',
        'ru': 'Симулятор налогового изгнания',
        'ar': 'محاكي النفي الضريبي',
        'th': 'เครื่องจำลองการเนรเทศทางภาษี',
    }
    cta_texts = {
        'en': 'Access the simulator →',
        'fr': 'Accédez au simulateur →',
        'es': 'Acceder al simulador →',
        'pt': 'Acesse o simulador →',
        'zh': '访问模拟器 →',
        'ja': 'シミュレーターにアクセス →',
        'ko': '시뮬레이터 액세스 →',
        'ru': 'Доступ к симулятору →',
        'ar': 'الوصول إلى المحاكي →',
        'th': 'เข้าถึงเครื่องจำลอง →',
    }

    label = labels.get(lang, labels['en'])
    cta = cta_texts.get(lang, cta_texts['en'])

    return f'''<section style="background:#f0f0f0;padding:20px;margin:30px auto;max-width:960px;border-radius:8px;">
    <h3 style="color:#000000;margin-bottom:12px;font-size:16px;">📊 {label}</h3>
    <p style="color:#333;font-size:14px;margin:0;">Optimize your tax situation:
    <a href="{tax_url}" style="color:#0066cc;font-weight:bold;text-decoration:none;">
    {cta}
    </a></p>
</section>'''

# New footer HTML
def get_new_footer(lang, is_tax_page=False):
    """Generate new footer with keywords and optional tax simulator link"""
    tax_url = TAX_URLS.get(lang, TAX_URLS['en'])

    # Most requested visas
    visas = {
        'en': [('thailand', 'Thailand'), ('vietnam', 'Vietnam'), ('india', 'India'), ('turkey', 'Turkey'),
                ('japan', 'Japan'), ('china', 'China'), ('indonesia', 'Indonesia'), ('malaysia', 'Malaysia'),
                ('taiwan', 'Taiwan'), ('uae', 'UAE'), ('maldives', 'Maldives'), ('sri-lanka', 'Sri Lanka'),
                ('colombia', 'Colombia'), ('egypt', 'Egypt'), ('jordan', 'Jordan'), ('usa', 'USA'),
                ('canada', 'Canada'), ('australia', 'Australia'), ('schengen-visa-guide-2026', 'Schengen Visa')],
    }

    visa_links = '\n                        '.join([
        f'<a href="/{lang}/visa-{slug}" style="color:#000000;text-decoration:none;font-size:14px;transition:color .2s;">{name}</a>'
        for slug, name in visas['en']
    ])

    keywords_section = get_keywords_section(lang)

    tax_section = f'''<div class="row mb-5 justify-content-center">
                <div class="col-md-10 text-center">
                    <p style="font-size:13px;color:#000000;margin:0;">
                        💰 <a href="{tax_url}" style="color:#000000;text-decoration:none;font-weight:bold;">
                        Tax Exile Simulator
                        </a>
                    </p>
                </div>
            </div>''' if is_tax_page else ''

    footer = f'''<!-- ======== FOOTER (SEO-optimized with backlinks) ======== -->
    <footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(['../'] * {lang != 'en'})images/bg_3.jpg);">
        <div class="container">
            <!-- Most Requested Visas Section -->
            <div class="row mb-5 justify-content-center">
                <div class="col-md-10 text-center">
                    <h2 style="font-size:18px;color:#000000;margin-bottom:16px;font-weight:600;letter-spacing:.5px;">Most Requested Visas</h2>
                    <nav style="line-height:2;display:flex;flex-wrap:wrap;justify-content:center;gap:8px;">
                        {visa_links}
                    </nav>
                </div>
            </div>
            <!-- Tax Exile Simulator Section -->
            {tax_section}
            <!-- Popular Keywords Section -->
            {keywords_section}
            <!-- Copyright & Legal Section -->
            <div class="row mb-5 justify-content-center border-top" style="border-top:1px solid #ccc;padding-top:24px;">
                <div class="col-md-10 text-center">
                    <p style="color:#000000;font-size:14px;margin-bottom:8px;">© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform</p>
                    <p style="font-size:12px;color:#000000;margin:0;">
                        <a href="/{lang}/legal-notice" style="color:#000000;text-decoration:none;transition:color .2s;">Legal Notice</a>
                        <span style="margin:0 6px;">|</span>
                        <a href="/{lang}/disclaimer" style="color:#000000;text-decoration:none;transition:color .2s;">Disclaimer</a>
                    </p>
                </div>
            </div>
        </div>
    </footer>'''

    return footer

# Detect tax exile pages
def is_tax_page(filepath, content):
    """Detect if page is about tax exile"""
    keywords = ['retire', 'retirement', 'retire', 'retiré', 'pension', 'exil', 'tax haven', 'expatriate',
                'expat', 'residency', 'long-stay', 'nos-residents', 'ltr visa', 'nlr', 'nhr']
    content_lower = content.lower()
    return any(kw in content_lower for kw in keywords)

# Process files
def process_files():
    www_path = Path('C:/Users/chemi/Documents/evisa/pacific-main/www')

    languages = {
        None: 'en',  # root
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

    updated = 0
    tax_pages = 0

    for lang_dir, lang_code in languages.items():
        target_dir = www_path / lang_dir if lang_dir else www_path

        for html_file in sorted(target_dir.glob('*.html')):
            if 'flaticon' in str(html_file):
                continue

            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Check if tax page
            is_tax = is_tax_page(html_file, content)
            if is_tax:
                tax_pages += 1

            # Remove old footer
            footer_pattern = r'<!--\s*=+\s*FOOTER.*?-->.*?</footer>'
            match = re.search(footer_pattern, content, re.DOTALL | re.IGNORECASE)
            if not match:
                footer_pattern = r'<footer\s+class="ftco-footer[^>]*>.*?</footer>'
                match = re.search(footer_pattern, content, re.DOTALL | re.IGNORECASE)

            if match:
                new_footer = get_new_footer(lang_code, is_tax)
                new_content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL | re.IGNORECASE)

                # Add tax body section if tax page
                if is_tax:
                    tax_body = get_tax_body_section(lang_code)
                    # Insert before footer
                    new_content = new_content.replace(new_footer, tax_body + '\n' + new_footer)

                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                updated += 1
                if updated % 100 == 0:
                    print(f"[OK] {updated} files updated")

    print(f"\n[COMPLETE] Updated {updated} files ({tax_pages} tax pages detected)")

if __name__ == '__main__':
    process_files()
