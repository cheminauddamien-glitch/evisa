#!/usr/bin/env python3
"""
Generate zh/th/ru/ar/ja/ko versions of newly created EN pages that are still missing.
Reuses the same logic as gen_visa_new_langs.py.
"""
import os, re, sys
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
        ('All Destinations','所有目的地'),('Visa Requirements','签证要求'),
        ('How to Apply','如何申请'),('Processing Time','处理时间'),('Official Links','官方链接'),
        ('This guide is maintained by our visa research team.','本指南由我们的签证研究团队维护。'),
        ('Always verify current requirements at','请始终在以下官方网站验证当前要求：'),
        ('before travel. This page is for informational purposes only.','出行前请核实。本页面仅供参考。'),
        ('Important:','重要提示：'),('Visa rules change frequently.','签证规则经常变化。'),
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
        ('All Destinations','ทุกจุดหมายปลายทาง'),('Visa Requirements','ข้อกำหนดวีซ่า'),
        ('How to Apply','วิธีการสมัคร'),('Processing Time','ระยะเวลาดำเนินการ'),('Official Links','ลิงก์ทางการ'),
        ('This guide is maintained by our visa research team.','คู่มือนี้ดูแลโดยทีมวิจัยวีซ่าของเรา'),
        ('Always verify current requirements at','กรุณาตรวจสอบข้อกำหนดปัจจุบันที่'),
        ('before travel. This page is for informational purposes only.','ก่อนเดินทาง หน้านี้มีไว้เพื่อข้อมูลเท่านั้น'),
        ('Important:','สำคัญ:'),('Visa rules change frequently.','กฎวีซ่าเปลี่ยนแปลงบ่อยครั้ง'),
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
        ('All Destinations','Все направления'),('Visa Requirements','Требования для визы'),
        ('How to Apply','Как подать заявку'),('Processing Time','Время обработки'),('Official Links','Официальные ссылки'),
        ('This guide is maintained by our visa research team.','Это руководство поддерживается нашей командой по исследованию виз.'),
        ('Always verify current requirements at','Всегда проверяйте актуальные требования на'),
        ('before travel. This page is for informational purposes only.','перед поездкой. Эта страница предназначена только для информации.'),
        ('Important:','Важно:'),('Visa rules change frequently.','Правила выдачи виз часто меняются.'),
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
        ('All Destinations','جميع الوجهات'),('Visa Requirements','متطلبات التأشيرة'),
        ('How to Apply','كيفية التقديم'),('Processing Time','وقت المعالجة'),('Official Links','الروابط الرسمية'),
        ('This guide is maintained by our visa research team.','يتم صيانة هذا الدليل من قبل فريق أبحاث التأشيرة لدينا.'),
        ('Always verify current requirements at','تحقق دائماً من المتطلبات الحالية على'),
        ('before travel. This page is for informational purposes only.','قبل السفر. هذه الصفحة للأغراض المعلوماتية فقط.'),
        ('Important:','هام:'),('Visa rules change frequently.','قواعد التأشيرة تتغير بشكل متكرر.'),
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
        ('All Destinations','すべての目的地'),('Visa Requirements','ビザ要件'),
        ('How to Apply','申請方法'),('Processing Time','処理時間'),('Official Links','公式リンク'),
        ('This guide is maintained by our visa research team.','このガイドはビザ調査チームによって管理されています。'),
        ('Always verify current requirements at','渡航前に必ず最新の要件を以下で確認してください：'),
        ('before travel. This page is for informational purposes only.','出発前にご確認ください。このページは情報提供のみを目的としています。'),
        ('Important:','重要：'),('Visa rules change frequently.','ビザのルールは頻繁に変更されます。'),
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
        ('All Destinations','모든 목적지'),('Visa Requirements','비자 요건'),
        ('How to Apply','신청 방법'),('Processing Time','처리 시간'),('Official Links','공식 링크'),
        ('This guide is maintained by our visa research team.','이 가이드는 비자 리서치팀이 관리합니다.'),
        ('Always verify current requirements at','여행 전에 항상 공식 사이트에서 최신 요건을 확인하세요:'),
        ('before travel. This page is for informational purposes only.','이 페이지는 정보 제공 목적으로만 작성되었습니다.'),
        ('Important:','중요:'),('Visa rules change frequently.','비자 규정은 자주 변경됩니다.'),
    ],
}

flag_map = {"zh":"cn","th":"th","ru":"ru","ar":"sa","ja":"jp","ko":"kr"}

# Only process these 6 slugs that are still missing
TARGET_SLUGS = ["south-korea","saudi-arabia","oman","bahrain","israel","peru"]

def fix_page(html, lang, slug):
    cfg = LANGS[lang]
    # html lang + dir
    html = re.sub(r'<html lang="en"[^>]*>', f'<html lang="{cfg["html_lang"]}" {cfg["dir"]}>', html)
    # Add font
    if cfg["font"]:
        html = html.replace('</head>', cfg["font"] + '\n</head>', 1)
    # canonical + og:url
    html = html.replace(
        f'https://www.evisa-card.com/en/visa-{slug}.html',
        f'https://www.evisa-card.com/{lang}/visa-{slug}.html'
    )
    # hreflang — remove old and add new
    html = re.sub(r'[ \t]*<link[^>]+hreflang[^>]+/?>\n?', '', html)
    hreflang = f'''    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/visa-{slug}.html"/>
    <link rel="alternate" hreflang="zh" href="https://www.evisa-card.com/zh/visa-{slug}.html"/>
    <link rel="alternate" hreflang="th" href="https://www.evisa-card.com/th/visa-{slug}.html"/>
    <link rel="alternate" hreflang="ru" href="https://www.evisa-card.com/ru/visa-{slug}.html"/>
    <link rel="alternate" hreflang="ar" href="https://www.evisa-card.com/ar/visa-{slug}.html"/>
    <link rel="alternate" hreflang="ja" href="https://www.evisa-card.com/ja/visa-{slug}.html"/>
    <link rel="alternate" hreflang="ko" href="https://www.evisa-card.com/ko/visa-{slug}.html"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/visa-{slug}.html"/>'''
    html = html.replace('</head>', hreflang + '\n</head>', 1)
    # navbar brand JS paths use ../ so fine
    # Active language in dropdown — switch active from EN to this lang
    fl = flag_map[lang]
    ln = cfg["label"]
    # Deactivate EN
    html = html.replace(
        f'<a class="dropdown-item active" href="/en/visa-{slug}.html"><span class="fi fi-gb"></span> English</a>',
        f'<a class="dropdown-item" href="/en/visa-{slug}.html"><span class="fi fi-gb"></span> English</a>'
    )
    # Activate current lang
    html = html.replace(
        f'href="/{lang}/destination.html"><span class="fi fi-{fl}"></span> {ln}</a>',
        f'href="/{lang}/visa-{slug}.html" class="dropdown-item active"><span class="fi fi-{fl}"></span> {ln}</a>'
    )
    # Fix legal/expat links
    html = html.replace('href="/en/legal-notice.html"', f'href="/{lang}/legal-notice.html"')
    html = html.replace('href="/en/disclaimer.html"', f'href="/{lang}/disclaimer.html"')
    html = html.replace('href="/en/expat-guides.html"', f'href="/{lang}/expat-guides.html"')
    # Apply UI substitutions
    for old, new in UI_SUBS[lang]:
        html = html.replace(old, new)
    return html

created = 0
en_dir = os.path.join(WWW, "en")

for slug in TARGET_SLUGS:
    en_path = os.path.join(en_dir, f"visa-{slug}.html")
    if not os.path.exists(en_path):
        print(f"  SKIP (no EN source): visa-{slug}.html")
        continue
    with open(en_path, "r", encoding="utf-8") as f:
        en_html = f.read()
    for lang in LANGS:
        out_dir = os.path.join(WWW, lang)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"visa-{slug}.html")
        if os.path.exists(out_path):
            print(f"  SKIP (exists): {lang}/visa-{slug}.html")
            continue
        new_html = fix_page(en_html, lang, slug)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"  Created: {lang}/visa-{slug}.html")
        created += 1

print(f"\nDONE — {created} new-lang pages created")
