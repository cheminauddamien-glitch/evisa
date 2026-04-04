#!/usr/bin/env python3
"""
Generate missing guide pages for all languages.
- zh/th/ru/ar/ja/ko: all individual guide pages from EN source
- fr/es/pt: 4 missing guide pages (digital-nomad, best-nomad, cheapest-retire, schengen)
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

# All EN guide pages (excluding expat-guides.html which already exists in all langs)
EN_GUIDES = [
    "best-countries-digital-nomads-2026.html",
    "cheapest-countries-to-retire-abroad-2026.html",
    "digital-nomad-visas-guide.html",
    "expat-guide-colombia.html",
    "expat-guide-japan.html",
    "expat-guide-malaysia.html",
    "expat-guide-mexico.html",
    "expat-guide-portugal.html",
    "expat-guide-spain.html",
    "expat-guide-thailand.html",
    "expat-guide-uae.html",
    "expat-guide-vietnam.html",
    "retirement-visa-guide.html",
    "schengen-visa-guide-2026.html",
]

# Pages missing in FR/ES/PT (the others already exist)
FR_ES_PT_MISSING = [
    "best-countries-digital-nomads-2026.html",
    "cheapest-countries-to-retire-abroad-2026.html",
    "digital-nomad-visas-guide.html",
    "schengen-visa-guide-2026.html",
]

LANGS_NEW = {
    "zh": {"html_lang":"zh","flag":"fi-cn","label":"中文","dir":"",
           "font":'<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'},
    "th": {"html_lang":"th","flag":"fi-th","label":"ไทย","dir":"",
           "font":'<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'},
    "ru": {"html_lang":"ru","flag":"fi-ru","label":"Русский","dir":"","font":""},
    "ar": {"html_lang":"ar","flag":"fi-sa","label":"العربية","dir":'dir="rtl"',
           "font":'<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'},
    "ja": {"html_lang":"ja","flag":"fi-jp","label":"日本語","dir":"",
           "font":'<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'},
    "ko": {"html_lang":"ko","flag":"fi-kr","label":"한국어","dir":"",
           "font":'<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'},
}

LANGS_EUR = {
    "fr": {"html_lang":"fr","flag":"fi-fr","label":"Français","dir":"","font":"",
           "nav":{"Home":"Accueil","Destinations":"Destinations","About":"À propos","Blog":"Blog","Guides":"Guides"},
           "legal":{"Legal Notice":"Mentions légales","Disclaimer":"Avertissement"},
           "footer":'© 2026 eVisa-Card.com — Plateforme mondiale d\'information eVisa et voyage'},
    "es": {"html_lang":"es","flag":"fi-es","label":"Español","dir":"","font":"",
           "nav":{"Home":"Inicio","Destinations":"Destinos","About":"Acerca de","Blog":"Blog","Guides":"Guías"},
           "legal":{"Legal Notice":"Aviso legal","Disclaimer":"Aviso legal"},
           "footer":'© 2026 eVisa-Card.com — Plataforma global de información sobre eVisa y viajes'},
    "pt": {"html_lang":"pt","flag":"fi-br","label":"Português","dir":"","font":"",
           "nav":{"Home":"Início","Destinations":"Destinos","About":"Sobre nós","Blog":"Blog","Guides":"Guias"},
           "legal":{"Legal Notice":"Aviso legal","Disclaimer":"Aviso legal"},
           "footer":'© 2026 eVisa-Card.com — Plataforma global de informações sobre eVisa e viagens'},
}

UI_SUBS = {
    "zh": [
        ('">Home</a>', '">首页</a>'),('">Destinations</a>', '">目的地</a>'),
        ('">About</a>', '">关于我们</a>'),('">Blog</a>', '">博客</a>'),
        ('">Guides</a>', '">指南</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-cn"></span> 中文</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — 全球eVisa和旅行信息平台'),
        ('Legal Notice','法律声明'),('Disclaimer','免责声明'),
        ('Last updated: <strong>March 2026</strong>.','最后更新：<strong>2026年3月</strong>。'),
        ('Editorial Team','编辑团队'),('Related Visa Guides','相关签证指南'),
    ],
    "th": [
        ('">Home</a>', '">หน้าหลัก</a>'),('">Destinations</a>', '">จุดหมายปลายทาง</a>'),
        ('">About</a>', '">เกี่ยวกับ</a>'),('">Blog</a>', '">บล็อก</a>'),
        ('">Guides</a>', '">คู่มือ</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-th"></span> ไทย</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — แพลตฟอร์มข้อมูล eVisa และการเดินทางระดับโลก'),
        ('Legal Notice','ข้อกำหนดทางกฎหมาย'),('Disclaimer','ข้อจำกัดความรับผิดชอบ'),
        ('Last updated: <strong>March 2026</strong>.','อัปเดตล่าสุด: <strong>มีนาคม 2026</strong>'),
        ('Editorial Team','ทีมบรรณาธิการ'),('Related Visa Guides','คู่มือวีซ่าที่เกี่ยวข้อง'),
    ],
    "ru": [
        ('">Home</a>', '">Главная</a>'),('">Destinations</a>', '">Направления</a>'),
        ('">About</a>', '">О нас</a>'),('">Blog</a>', '">Блог</a>'),
        ('">Guides</a>', '">Гиды</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-ru"></span> Русский</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — Глобальная платформа информации об eVisa и путешествиях'),
        ('Legal Notice','Правовое уведомление'),('Disclaimer','Отказ от ответственности'),
        ('Last updated: <strong>March 2026</strong>.','Последнее обновление: <strong>март 2026</strong>.'),
        ('Editorial Team','Редакционная команда'),('Related Visa Guides','Связанные визовые руководства'),
    ],
    "ar": [
        ('">Home</a>', '">الرئيسية</a>'),('">Destinations</a>', '">الوجهات</a>'),
        ('">About</a>', '">من نحن</a>'),('">Blog</a>', '">المدونة</a>'),
        ('">Guides</a>', '">الأدلة</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-sa"></span> العربية</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — منصة معلومات التأشيرة الإلكترونية والسفر العالمية'),
        ('Legal Notice','إشعار قانوني'),('Disclaimer','إخلاء المسؤولية'),
        ('Last updated: <strong>March 2026</strong>.','آخر تحديث: <strong>مارس 2026</strong>.'),
        ('Editorial Team','الفريق التحريري'),('Related Visa Guides','أدلة التأشيرة ذات الصلة'),
    ],
    "ja": [
        ('">Home</a>', '">ホーム</a>'),('">Destinations</a>', '">目的地</a>'),
        ('">About</a>', '">私たちについて</a>'),('">Blog</a>', '">ブログ</a>'),
        ('">Guides</a>', '">ガイド</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-jp"></span> 日本語</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — グローバルeVisa・旅行情報プラットフォーム'),
        ('Legal Notice','法的通知'),('Disclaimer','免責事項'),
        ('Last updated: <strong>March 2026</strong>.','最終更新: <strong>2026年3月</strong>。'),
        ('Editorial Team','編集チーム'),('Related Visa Guides','関連するビザガイド'),
    ],
    "ko": [
        ('">Home</a>', '">홈</a>'),('">Destinations</a>', '">목적지</a>'),
        ('">About</a>', '">소개</a>'),('">Blog</a>', '">블로그</a>'),
        ('">Guides</a>', '">가이드</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-kr"></span> 한국어</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — 글로벌 eVisa 및 여행 정보 플랫폼'),
        ('Legal Notice','법적 고지'),('Disclaimer','면책 조항'),
        ('Last updated: <strong>March 2026</strong>.','최종 업데이트: <strong>2026년 3월</strong>.'),
        ('Editorial Team','편집팀'),('Related Visa Guides','관련 비자 가이드'),
    ],
}

def fix_new_lang(html, lang, filename):
    """Fix a page for zh/th/ru/ar/ja/ko."""
    cfg = LANGS_NEW[lang]
    slug = filename.replace(".html","")
    BASE = "https://www.evisa-card.com"

    # 1. html lang + dir
    html = re.sub(r'<html\s+lang="[^"]*"[^>]*>', f'<html lang="{cfg["html_lang"]}" {cfg["dir"]}>'.strip(), html)

    # 2. canonical
    html = re.sub(r'<link rel="canonical"[^/]*/>', f'<link rel="canonical" href="{BASE}/{lang}/{filename}"/>', html)

    # 3. hreflang — replace existing block with all 10 langs
    hreflang_block = "\n".join([
        f'    <link rel="alternate" hreflang="en" href="{BASE}/en/{filename}"/>',
        f'    <link rel="alternate" hreflang="fr" href="{BASE}/fr/{filename}"/>',
        f'    <link rel="alternate" hreflang="es" href="{BASE}/es/{filename}"/>',
        f'    <link rel="alternate" hreflang="pt" href="{BASE}/pt/{filename}"/>',
        f'    <link rel="alternate" hreflang="zh" href="{BASE}/zh/{filename}"/>',
        f'    <link rel="alternate" hreflang="th" href="{BASE}/th/{filename}"/>',
        f'    <link rel="alternate" hreflang="ru" href="{BASE}/ru/{filename}"/>',
        f'    <link rel="alternate" hreflang="ar" href="{BASE}/ar/{filename}"/>',
        f'    <link rel="alternate" hreflang="ja" href="{BASE}/ja/{filename}"/>',
        f'    <link rel="alternate" hreflang="ko" href="{BASE}/ko/{filename}"/>',
        f'    <link rel="alternate" hreflang="x-default" href="{BASE}/en/{filename}"/>',
    ])
    html = re.sub(r'<link rel="alternate" hreflang[^>]*/>\n?', '', html)
    html = html.replace('<link rel="canonical"', hreflang_block + '\n    <link rel="canonical"', 1)

    # 4. Add font if needed
    if cfg["font"] and 'Noto Sans' not in html:
        html = html.replace(
            '<link href="https://fonts.googleapis.com/css?family=Poppins',
            cfg["font"] + '\n    <link href="https://fonts.googleapis.com/css?family=Poppins'
        )

    # 5. Fix lang dropdown — active language + links for zh/th/ru/ar/ja/ko
    # Remove old active class on en/fr/es/pt items
    html = re.sub(r'(<a class="dropdown-item) active(")', r'\1\2', html)
    # Set new langs in dropdown (replace /en/filename or /zh/destination with /{lang}/filename)
    html = re.sub(
        r'href="/(zh|th|ru|ar|ja|ko)/[^"]*"(<span class="fi fi-(cn|th|ru|sa|jp|kr)"></span>)',
        lambda m: f'href="/{m.group(1)}/{filename}"' + m.group(2),
        html
    )
    # Fix active item for this lang
    lang_labels = {
        "zh":("fi-cn","中文"), "th":("fi-th","ไทย"), "ru":("fi-ru","Русский"),
        "ar":("fi-sa","العربية"), "ja":("fi-jp","日本語"), "ko":("fi-kr","한국어")
    }
    flag, label = lang_labels[lang]
    # Mark correct dropdown item as active
    html = re.sub(
        rf'(href="/{lang}/{re.escape(filename)}")(>)(<span class="fi {flag}"></span> {re.escape(label)}</a>)',
        rf'\1\2<span class="fi {flag}"></span> {label}</a>',
        html
    )
    html = re.sub(
        rf'(<a class="dropdown-item")(.*?href="/{lang}/{re.escape(filename)}")',
        r'<a class="dropdown-item active"\2',
        html
    )

    # Fix the toggler label (show current lang)
    html = re.sub(
        r'(<span class="fi fi-gb"></span> English</a>)',
        f'<span class="fi {flag}"></span> {label}</a>',
        html
    )

    # 6. Fix nav: Guides link + legal links
    html = html.replace(f'/en/expat-guides.html">', f'/{lang}/expat-guides.html">')
    html = html.replace('/en/legal-notice.html', f'/{lang}/legal-notice.html')
    html = html.replace('/en/disclaimer.html', f'/{lang}/disclaimer.html')

    # 7. UI text substitutions
    for old, new in UI_SUBS[lang]:
        html = html.replace(old, new)

    # 8. og:url
    html = re.sub(r'(<meta property="og:url"[^>]*content=")[^"]*(")', f'\\1{BASE}/{lang}/{filename}\\2', html)

    return html


def fix_eur_lang(html, lang, filename):
    """Fix a page for fr/es/pt — use existing FR page as reference for nav labels."""
    cfg = LANGS_EUR[lang]
    slug = filename.replace(".html","")
    BASE = "https://www.evisa-card.com"

    # 1. html lang
    html = re.sub(r'<html\s+lang="[^"]*"[^>]*>', f'<html lang="{cfg["html_lang"]}">', html)

    # 2. canonical
    html = re.sub(r'<link rel="canonical"[^/]*/>', f'<link rel="canonical" href="{BASE}/{lang}/{filename}"/>', html)

    # 3. hreflang
    hreflang_block = "\n".join([
        f'    <link rel="alternate" hreflang="en" href="{BASE}/en/{filename}"/>',
        f'    <link rel="alternate" hreflang="fr" href="{BASE}/fr/{filename}"/>',
        f'    <link rel="alternate" hreflang="es" href="{BASE}/es/{filename}"/>',
        f'    <link rel="alternate" hreflang="pt" href="{BASE}/pt/{filename}"/>',
        f'    <link rel="alternate" hreflang="x-default" href="{BASE}/en/{filename}"/>',
    ])
    html = re.sub(r'<link rel="alternate" hreflang[^>]*/>\n?', '', html)
    html = html.replace('<link rel="canonical"', hreflang_block + '\n    <link rel="canonical"', 1)

    # 4. Set active lang in dropdown
    html = re.sub(r'(<a class="dropdown-item) active(")', r'\1\2', html)
    lang_info = {
        "fr": ("fi-fr","Français"), "es": ("fi-es","Español"), "pt": ("fi-br","Português")
    }
    flag, label = lang_info[lang]
    html = re.sub(
        rf'(<a class="dropdown-item")(.*?href="/{lang}/{re.escape(filename)}")',
        r'<a class="dropdown-item active"\2',
        html
    )

    # 5. Fix toggler label
    for old_flag, old_label in [("fi-gb","English"),("fi-fr","Français"),("fi-es","Español"),("fi-br","Português")]:
        html = html.replace(
            f'<span class="fi {old_flag}"></span> {old_label}</a>',
            f'<span class="fi {flag}"></span> {label}</a>',
            1  # only first occurrence (the toggler button)
        )

    # 6. Fix nav labels
    nav = cfg["nav"]
    for en_label, tr_label in nav.items():
        html = html.replace(f'">{en_label}</a>', f'">{tr_label}</a>')

    # 7. Guides nav link
    html = html.replace('/en/expat-guides.html">', f'/{lang}/expat-guides.html">')

    # 8. Legal links
    html = html.replace('/en/legal-notice.html', f'/{lang}/legal-notice.html')
    html = html.replace('/en/disclaimer.html', f'/{lang}/disclaimer.html')

    # 9. Footer
    if cfg["footer"]:
        html = html.replace(
            '© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
            cfg["footer"]
        )

    # 10. Legal link labels
    for en_l, tr_l in cfg["legal"].items():
        html = html.replace(f'>{en_l}<', f'>{tr_l}<')

    # 11. og:url
    html = re.sub(r'(<meta property="og:url"[^>]*content=")[^"]*(")', f'\\1{BASE}/{lang}/{filename}\\2', html)

    return html


created = 0

# Generate for zh/th/ru/ar/ja/ko — all EN_GUIDES
for filename in EN_GUIDES:
    en_path = os.path.join(WWW, "en", filename)
    if not os.path.exists(en_path):
        print(f"  SKIP (no EN source): {filename}")
        continue
    en_html = open(en_path, encoding="utf-8").read()

    for lang in LANGS_NEW:
        out_path = os.path.join(WWW, lang, filename)
        if os.path.exists(out_path):
            continue  # already exists
        fixed = fix_new_lang(en_html, lang, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"  CREATED: {lang}/{filename}")
        created += 1

# Generate for fr/es/pt — only missing pages
for filename in FR_ES_PT_MISSING:
    en_path = os.path.join(WWW, "en", filename)
    if not os.path.exists(en_path):
        print(f"  SKIP (no EN source): {filename}")
        continue
    en_html = open(en_path, encoding="utf-8").read()

    for lang in LANGS_EUR:
        out_path = os.path.join(WWW, lang, filename)
        if os.path.exists(out_path):
            continue
        fixed = fix_eur_lang(en_html, lang, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"  CREATED: {lang}/{filename}")
        created += 1

print(f"\nDONE — {created} pages created")
