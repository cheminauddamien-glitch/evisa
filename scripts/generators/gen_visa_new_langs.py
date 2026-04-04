#!/usr/bin/env python3
"""
gen_visa_new_langs.py
Generates visa-{country}.html for zh/th/ru/ar/ja/ko from EN pages.
Uses text substitution for UI elements + country name translation.
"""
import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

LANGS = {
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

# UI label translations
UI_SUBS = {
    "zh": [
        ('">Home</a>', '">首页</a>'),
        ('">Destinations</a>', '">目的地</a>'),
        ('">About</a>', '">关于我们</a>'),
        ('">Blog</a>', '">博客</a>'),
        ('">Guides</a>', '">指南</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-cn"></span> 中文</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
         '© 2026 eVisa-Card.com — 全球eVisa和旅行信息平台'),
        ('Legal Notice', '法律声明'),
        ('Disclaimer', '免责声明'),
        ('Last updated: <strong>March 2026</strong>.', '最后更新：<strong>2026年3月</strong>。'),
        ('Editorial Team', '编辑团队'),
        ('Related Guides', '相关指南'),
        ('All Destinations', '所有目的地'),
        ('Visa Requirements', '签证要求'),
        ('How to Apply', '如何申请'),
        ('Processing Time', '处理时间'),
        ('Official Links', '官方链接'),
    ],
    "th": [
        ('">Home</a>', '">หน้าหลัก</a>'),
        ('">Destinations</a>', '">จุดหมายปลายทาง</a>'),
        ('">About</a>', '">เกี่ยวกับ</a>'),
        ('">Blog</a>', '">บล็อก</a>'),
        ('">Guides</a>', '">คู่มือ</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-th"></span> ไทย</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
         '© 2026 eVisa-Card.com — แพลตฟอร์มข้อมูล eVisa และการเดินทางระดับโลก'),
        ('Legal Notice', 'ข้อกำหนดทางกฎหมาย'),
        ('Disclaimer', 'ข้อจำกัดความรับผิดชอบ'),
        ('Last updated: <strong>March 2026</strong>.', 'อัปเดตล่าสุด: <strong>มีนาคม 2026</strong>'),
        ('Editorial Team', 'ทีมบรรณาธิการ'),
        ('Related Guides', 'คู่มือที่เกี่ยวข้อง'),
        ('All Destinations', 'จุดหมายทั้งหมด'),
        ('Visa Requirements', 'ข้อกำหนดวีซ่า'),
        ('How to Apply', 'วิธีสมัคร'),
        ('Processing Time', 'เวลาดำเนินการ'),
    ],
    "ru": [
        ('">Home</a>', '">Главная</a>'),
        ('">Destinations</a>', '">Направления</a>'),
        ('">About</a>', '">О нас</a>'),
        ('">Blog</a>', '">Блог</a>'),
        ('">Guides</a>', '">Руководства</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-ru"></span> Русский</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
         '© 2026 eVisa-Card.com — Глобальная платформа информации об eVisa и путешествиях'),
        ('Legal Notice', 'Правовая информация'),
        ('Disclaimer', 'Отказ от ответственности'),
        ('Last updated: <strong>March 2026</strong>.', 'Последнее обновление: <strong>март 2026</strong>.'),
        ('Editorial Team', 'Редакционная команда'),
        ('Related Guides', 'Похожие руководства'),
        ('All Destinations', 'Все направления'),
        ('Visa Requirements', 'Требования к визе'),
        ('How to Apply', 'Как подать заявку'),
        ('Processing Time', 'Время обработки'),
    ],
    "ar": [
        ('">Home</a>', '">الرئيسية</a>'),
        ('">Destinations</a>', '">الوجهات</a>'),
        ('">About</a>', '">عن الموقع</a>'),
        ('">Blog</a>', '">مدونة</a>'),
        ('">Guides</a>', '">أدلة</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-sa"></span> العربية</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
         '© 2026 eVisa-Card.com — منصة معلومات eVisa والسفر العالمية'),
        ('Legal Notice', 'إشعار قانوني'),
        ('Disclaimer', 'إخلاء المسؤولية'),
        ('Last updated: <strong>March 2026</strong>.', 'آخر تحديث: <strong>مارس 2026</strong>.'),
        ('Editorial Team', 'الفريق التحريري'),
        ('Related Guides', 'أدلة ذات صلة'),
        ('All Destinations', 'جميع الوجهات'),
        ('Visa Requirements', 'متطلبات التأشيرة'),
        ('How to Apply', 'كيفية التقديم'),
        ('Processing Time', 'وقت المعالجة'),
    ],
    "ja": [
        ('">Home</a>', '">ホーム</a>'),
        ('">Destinations</a>', '">目的地</a>'),
        ('">About</a>', '">会社概要</a>'),
        ('">Blog</a>', '">ブログ</a>'),
        ('">Guides</a>', '">ガイド</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-jp"></span> 日本語</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
         '© 2026 eVisa-Card.com — グローバルeVisaおよび旅行情報プラットフォーム'),
        ('Legal Notice', '法的通知'),
        ('Disclaimer', '免責事項'),
        ('Last updated: <strong>March 2026</strong>.', '最終更新：<strong>2026年3月</strong>。'),
        ('Editorial Team', '編集チーム'),
        ('Related Guides', '関連ガイド'),
        ('All Destinations', 'すべての目的地'),
        ('Visa Requirements', 'ビザ要件'),
        ('How to Apply', '申請方法'),
        ('Processing Time', '処理時間'),
    ],
    "ko": [
        ('">Home</a>', '">홈</a>'),
        ('">Destinations</a>', '">목적지</a>'),
        ('">About</a>', '">소개</a>'),
        ('">Blog</a>', '">블로그</a>'),
        ('">Guides</a>', '">가이드</a>'),
        ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-kr"></span> 한국어</a>'),
        ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
         '© 2026 eVisa-Card.com — 글로벌 eVisa 및 여행 정보 플랫폼'),
        ('Legal Notice', '법적 고지'),
        ('Disclaimer', '면책 조항'),
        ('Last updated: <strong>March 2026</strong>.', '마지막 업데이트: <strong>2026년 3월</strong>.'),
        ('Editorial Team', '편집팀'),
        ('Related Guides', '관련 가이드'),
        ('All Destinations', '모든 목적지'),
        ('Visa Requirements', '비자 요건'),
        ('How to Apply', '신청 방법'),
        ('Processing Time', '처리 시간'),
    ],
}

# New language dropdown items (all 10 langs)
NEW_DROPDOWN = {
    "zh": '<span class="fi fi-cn"></span> 中文',
    "th": '<span class="fi fi-th"></span> ไทย',
    "ru": '<span class="fi fi-ru"></span> Русский',
    "ar": '<span class="fi fi-sa"></span> العربية',
    "ja": '<span class="fi fi-jp"></span> 日本語',
    "ko": '<span class="fi fi-kr"></span> 한국어',
}

def fix_page(html, lang, fname, slug):
    lm = LANGS[lang]

    # 1. html lang attribute
    html = re.sub(r'<html lang="[^"]*"', f'<html lang="{lm["html_lang"]}"', html)

    # 2. Add dir=rtl for Arabic
    if lm["dir"]:
        html = html.replace(f'<html lang="{lm["html_lang"]}"',
                            f'<html lang="{lm["html_lang"]}" {lm["dir"]}')

    # 3. Add font if needed
    if lm["font"] and lm["font"] not in html:
        html = html.replace('</head>', f'  {lm["font"]}\n</head>')

    # 4. Canonical + hreflang
    html = re.sub(
        r'<link rel="canonical" href="https://www\.evisa-card\.com/en/[^"]*"',
        f'<link rel="canonical" href="https://www.evisa-card.com/{lang}/{slug}"',
        html
    )

    # 5. UI text substitutions
    for old, new in UI_SUBS[lang]:
        html = html.replace(old, new)

    # 6. Fix navbar active lang label
    html = re.sub(
        r'<span class="fi fi-[a-z]+-?[a-z]*"></span> (?:English|Français|Español|Português)</a>\s*</a>',
        f'<span class="fi {lm["flag"]}"></span> {lm["label"]}</a>',
        html
    )
    # Simpler: replace the active dropdown toggle label
    html = re.sub(
        r'(<a class="nav-link dropdown-toggle"[^>]*>\s*<span class="fi fi-[^"]*"></span> )(?:English|Français|Español|Português)',
        rf'\g<1>{lm["label"]}',
        html
    )
    # And update the flag icon in the toggle
    html = re.sub(
        r'(<a class="nav-link dropdown-toggle"[^>]*>\s*<span class="fi )fi-(?:gb|fr|es|br)(")',
        rf'\g<1>{lm["flag"]}\g<2>',
        html
    )

    # 7. Update footer legal links
    html = re.sub(r'/en/legal-notice\.html', f'/{lang}/legal-notice.html', html)
    html = re.sub(r'/en/disclaimer\.html', f'/{lang}/disclaimer.html', html)

    # 8. Update destination link in navbar
    html = re.sub(r'href="/(?:en|fr|es|pt)/destination\.html"', f'href="/{lang}/destination.html"', html)
    html = re.sub(r'href="/(?:en|fr|es|pt)/expat-guides\.html"', f'href="/{lang}/expat-guides.html"', html)

    # 9. Add new lang items to dropdown if not present
    if 'fi-cn' not in html:
        flag_map = {"zh":"cn","th":"th","ru":"ru","ar":"sa","ja":"jp","ko":"kr"}
        new_items = "\n".join([
            f'                        <a class="dropdown-item" href="/{lc}/{slug}.html"><span class="fi fi-{flag_map[lc]}"></span> {lb}</a>'
            for lc, lb in [("zh","中文"),("th","ไทย"),("ru","Русский"),("ar","العربية"),("ja","日本語"),("ko","한국어")]
        ])
        html = re.sub(
            r'(</div>\s*</li>\s*</ul>)',
            new_items + r'\n\1',
            html, count=1
        )

    # 10. Update active dropdown item
    html = re.sub(
        r'<a class="dropdown-item active" href="/(?:en|fr|es|pt)/[^"]*">',
        f'<a class="dropdown-item" href="/en/{slug}.html">',
        html
    )
    html = html.replace(
        f'<a class="dropdown-item" href="/{lang}/{slug}.html">',
        f'<a class="dropdown-item active" href="/{lang}/{slug}.html">'
    )

    return html


# ── Main ────────────────────────────────────────────────────────────────────
en_visa_pages = glob.glob(os.path.join(WWW, "en", "visa-*.html"))
created = {l: 0 for l in LANGS}
errors  = 0

for en_path in en_visa_pages:
    fname = os.path.basename(en_path)
    slug  = fname.replace(".html", "")

    try:
        html_en = open(en_path, encoding="utf-8").read()
    except Exception as e:
        print(f"ERR reading {fname}: {e}")
        errors += 1
        continue

    for lang in LANGS:
        out_path = os.path.join(WWW, lang, fname)
        try:
            new_html = fix_page(html_en, lang, fname, slug)
            open(out_path, "w", encoding="utf-8").write(new_html)
            created[lang] += 1
        except Exception as e:
            print(f"ERR {lang}/{fname}: {e}")
            errors += 1

for lang, count in created.items():
    print(f"{lang}: {count} pages")
print(f"Errors: {errors}")
print("DONE")
