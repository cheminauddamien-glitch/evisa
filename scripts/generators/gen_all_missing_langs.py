#!/usr/bin/env python3
"""
Generate ALL missing language versions of EN pages.
- FR/ES/PT: ~101 missing each
- ZH/TH/RU/AR/JA/KO: ~1195 missing each
Strategy: take EN source, apply UI + metadata transformations per language.
"""
import os, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"
BASE = "https://www.evisa-card.com"

# ─── Language configs ────────────────────────────────────────────────────────

EUR = {
    "fr": {
        "html_lang":"fr", "flag":"fi-fr", "label":"Français",
        "nav": {"Home":"Accueil","Destinations":"Destinations","About":"À propos","Blog":"Blog","Guides":"Guides"},
        "footer": "© 2026 eVisa-Card.com — Plateforme mondiale d'information eVisa et voyage",
        "legal_label": {"Legal Notice":"Mentions légales","Disclaimer":"Avertissement"},
        "font": "",
    },
    "es": {
        "html_lang":"es", "flag":"fi-es", "label":"Español",
        "nav": {"Home":"Inicio","Destinations":"Destinos","About":"Acerca de","Blog":"Blog","Guides":"Guías"},
        "footer": "© 2026 eVisa-Card.com — Plataforma global de información sobre eVisa y viajes",
        "legal_label": {"Legal Notice":"Aviso legal","Disclaimer":"Aviso legal"},
        "font": "",
    },
    "pt": {
        "html_lang":"pt", "flag":"fi-br", "label":"Português",
        "nav": {"Home":"Início","Destinations":"Destinos","About":"Sobre nós","Blog":"Blog","Guides":"Guias"},
        "footer": "© 2026 eVisa-Card.com — Plataforma global de informações sobre eVisa e viagens",
        "legal_label": {"Legal Notice":"Aviso legal","Disclaimer":"Aviso legal"},
        "font": "",
    },
}

NEW = {
    "zh": {
        "html_lang":"zh", "flag":"fi-cn", "label":"中文", "dir":"",
        "font": '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>',
        "ui": [
            ('">Home</a>','">首页</a>'),('">Destinations</a>','">目的地</a>'),
            ('">About</a>','">关于我们</a>'),('">Blog</a>','">博客</a>'),
            ('">Guides</a>','">指南</a>'),
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — 全球eVisa和旅行信息平台'),
            ('>Legal Notice<','>法律声明<'),('>Disclaimer<','>免责声明<'),
            ('Last updated: <strong>March 2026</strong>.','最后更新：<strong>2026年3月</strong>。'),
            ('Editorial Team','编辑团队'),('Related Visa Guides','相关签证指南'),
        ],
    },
    "th": {
        "html_lang":"th", "flag":"fi-th", "label":"ไทย", "dir":"",
        "font": '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>',
        "ui": [
            ('">Home</a>','">หน้าหลัก</a>'),('">Destinations</a>','">จุดหมายปลายทาง</a>'),
            ('">About</a>','">เกี่ยวกับ</a>'),('">Blog</a>','">บล็อก</a>'),
            ('">Guides</a>','">คู่มือ</a>'),
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — แพลตฟอร์มข้อมูล eVisa และการเดินทางระดับโลก'),
            ('>Legal Notice<','>ข้อกำหนดทางกฎหมาย<'),('>Disclaimer<','>ข้อจำกัดความรับผิดชอบ<'),
            ('Last updated: <strong>March 2026</strong>.','อัปเดตล่าสุด: <strong>มีนาคม 2026</strong>'),
            ('Editorial Team','ทีมบรรณาธิการ'),('Related Visa Guides','คู่มือวีซ่าที่เกี่ยวข้อง'),
        ],
    },
    "ru": {
        "html_lang":"ru", "flag":"fi-ru", "label":"Русский", "dir":"",
        "font": "",
        "ui": [
            ('">Home</a>','">Главная</a>'),('">Destinations</a>','">Направления</a>'),
            ('">About</a>','">О нас</a>'),('">Blog</a>','">Блог</a>'),
            ('">Guides</a>','">Гиды</a>'),
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — Глобальная платформа информации об eVisa и путешествиях'),
            ('>Legal Notice<','>Правовое уведомление<'),('>Disclaimer<','>Отказ от ответственности<'),
            ('Last updated: <strong>March 2026</strong>.','Последнее обновление: <strong>март 2026</strong>.'),
            ('Editorial Team','Редакционная команда'),('Related Visa Guides','Связанные визовые руководства'),
        ],
    },
    "ar": {
        "html_lang":"ar", "flag":"fi-sa", "label":"العربية", "dir":'dir="rtl"',
        "font": '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>',
        "ui": [
            ('">Home</a>','">الرئيسية</a>'),('">Destinations</a>','">الوجهات</a>'),
            ('">About</a>','">من نحن</a>'),('">Blog</a>','">المدونة</a>'),
            ('">Guides</a>','">الأدلة</a>'),
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — منصة معلومات التأشيرة الإلكترونية والسفر العالمية'),
            ('>Legal Notice<','>إشعار قانوني<'),('>Disclaimer<','>إخلاء المسؤولية<'),
            ('Last updated: <strong>March 2026</strong>.','آخر تحديث: <strong>مارس 2026</strong>.'),
            ('Editorial Team','الفريق التحريري'),('Related Visa Guides','أدلة التأشيرة ذات الصلة'),
        ],
    },
    "ja": {
        "html_lang":"ja", "flag":"fi-jp", "label":"日本語", "dir":"",
        "font": '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>',
        "ui": [
            ('">Home</a>','">ホーム</a>'),('">Destinations</a>','">目的地</a>'),
            ('">About</a>','">私たちについて</a>'),('">Blog</a>','">ブログ</a>'),
            ('">Guides</a>','">ガイド</a>'),
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — グローバルeVisa・旅行情報プラットフォーム'),
            ('>Legal Notice<','>法的通知<'),('>Disclaimer<','>免責事項<'),
            ('Last updated: <strong>March 2026</strong>.','最終更新: <strong>2026年3月</strong>。'),
            ('Editorial Team','編集チーム'),('Related Visa Guides','関連するビザガイド'),
        ],
    },
    "ko": {
        "html_lang":"ko", "flag":"fi-kr", "label":"한국어", "dir":"",
        "font": '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>',
        "ui": [
            ('">Home</a>','">홈</a>'),('">Destinations</a>','">목적지</a>'),
            ('">About</a>','">소개</a>'),('">Blog</a>','">블로그</a>'),
            ('">Guides</a>','">가이드</a>'),
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform','© 2026 eVisa-Card.com — 글로벌 eVisa 및 여행 정보 플랫폼'),
            ('>Legal Notice<','>법적 고지<'),('>Disclaimer<','>면책 조항<'),
            ('Last updated: <strong>March 2026</strong>.','최종 업데이트: <strong>2026년 3월</strong>.'),
            ('Editorial Team','편집팀'),('Related Visa Guides','관련 비자 가이드'),
        ],
    },
}

NEW_LANG_INFO = {
    "zh":("fi-cn","中文"), "th":("fi-th","ไทย"), "ru":("fi-ru","Русский"),
    "ar":("fi-sa","العربية"), "ja":("fi-jp","日本語"), "ko":("fi-kr","한국어"),
}
EUR_LANG_INFO = {
    "fr":("fi-fr","Français"), "es":("fi-es","Español"), "pt":("fi-br","Português"),
}

ALL_LANGS_FOR_HREFLANG = ["en","fr","es","pt","zh","th","ru","ar","ja","ko"]

# ─── Helper functions ────────────────────────────────────────────────────────

def is_noindex(html):
    return "noindex" in html[:2000]

def rebuild_hreflang(filename, existing_langs):
    """Build a complete hreflang block for languages that actually have the file."""
    lines = []
    for l in ALL_LANGS_FOR_HREFLANG:
        if l in existing_langs:
            lines.append(f'    <link rel="alternate" hreflang="{l}" href="{BASE}/{l}/{filename}"/>')
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE}/en/{filename}"/>')
    return "\n".join(lines)

def fix_canonical(html, lang, filename):
    return re.sub(r'<link rel="canonical"[^/]*/>', f'<link rel="canonical" href="{BASE}/{lang}/{filename}"/>', html)

def fix_hreflang_block(html, filename, existing_langs):
    """Remove old hreflang tags, insert new block before canonical."""
    html = re.sub(r'    <link rel="alternate" hreflang[^>]*/>\n?', '', html)
    block = rebuild_hreflang(filename, existing_langs)
    html = html.replace('<link rel="canonical"', block + '\n    <link rel="canonical"', 1)
    return html

def fix_ogurl(html, lang, filename):
    return re.sub(r'(<meta property="og:url"[^>]*content=")[^"]*(")', f'\\1{BASE}/{lang}/{filename}\\2', html)

def fix_legal_links(html, lang):
    """Fix /en/legal*.html and /en/disclaimer*.html to /{lang}/"""
    html = re.sub(r'href="/en/(legal-notice\.html)"', f'href="/{lang}/legal-notice.html"', html)
    html = re.sub(r'href="/en/(disclaimer\.html)"', f'href="/{lang}/disclaimer.html"', html)
    html = re.sub(r'href="/en/(mentions-legales\.html)"', f'href="/{lang}/legal-notice.html"', html)
    html = re.sub(r'href="/en/(aviso-legal\.html)"', f'href="/{lang}/legal-notice.html"', html)
    return html

def fix_guides_link(html, lang):
    return html.replace('/en/expat-guides.html">', f'/{lang}/expat-guides.html">')

def fix_destination_link(html, lang):
    return html.replace('href="/en/destination.html"', f'href="/{lang}/destination.html"')

# ─── EUR transform ───────────────────────────────────────────────────────────

def transform_eur(html, lang, filename, existing_langs):
    cfg = EUR[lang]
    flag, label = EUR_LANG_INFO[lang]

    # html lang
    html = re.sub(r'<html\s+lang="[^"]*"[^>]*>', f'<html lang="{cfg["html_lang"]}">', html)

    # canonical + hreflang
    html = fix_canonical(html, lang, filename)
    html = fix_hreflang_block(html, filename, existing_langs)

    # og:url
    html = fix_ogurl(html, lang, filename)

    # Nav items
    for en_l, tr_l in cfg["nav"].items():
        html = html.replace(f'">{en_l}</a>', f'">{tr_l}</a>')

    # Guides link in nav
    html = fix_guides_link(html, lang)
    html = fix_destination_link(html, lang)

    # Dropdown: remove active from all, set active on this lang
    html = re.sub(r'(<a class="dropdown-item) active(")', r'\1\2', html)
    html = re.sub(
        rf'(<a class="dropdown-item")(.*?href="/{lang}/{re.escape(filename)}")',
        r'<a class="dropdown-item active"\2', html
    )

    # Fix toggler label (first occurrence of English/other lang label)
    for old_flag, old_label in [("fi-gb","English"),("fi-fr","Français"),("fi-es","Español"),("fi-br","Português")]:
        pattern = f'<span class="fi {old_flag}"></span> {old_label}</a>'
        if pattern in html:
            html = html.replace(pattern, f'<span class="fi {flag}"></span> {label}</a>', 1)
            break

    # Fix new lang dropdown links (zh/th/ru/ar/ja/ko) pointing to /en/... or wrong page
    for nl, (nflag, nlabel) in NEW_LANG_INFO.items():
        old = rf'href="/{nl}/[^"]*"(><span class="fi {nflag}"></span> {re.escape(nlabel)}</a>)'
        html = re.sub(old, f'href="/{nl}/{filename}"' + r'\1', html)

    # Footer
    html = html.replace(
        '© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
        cfg["footer"]
    )
    html = html.replace('© 2026 eVisa-Card.com\n', f'{cfg["footer"]}\n')

    # Legal link labels
    for en_l, tr_l in cfg["legal_label"].items():
        html = html.replace(f'>{en_l}<', f'>{tr_l}<')

    # Legal link hrefs
    html = fix_legal_links(html, lang)

    return html

# ─── NEW lang transform ──────────────────────────────────────────────────────

def transform_new(html, lang, filename, existing_langs):
    cfg = NEW[lang]
    flag, label = NEW_LANG_INFO[lang]
    dir_attr = cfg["dir"]

    # html lang + dir
    new_tag = f'<html lang="{cfg["html_lang"]}"' + (f' {dir_attr}' if dir_attr else '') + '>'
    html = re.sub(r'<html\s+lang="[^"]*"[^>]*>', new_tag, html)

    # canonical + hreflang
    html = fix_canonical(html, lang, filename)
    html = fix_hreflang_block(html, filename, existing_langs)

    # og:url
    html = fix_ogurl(html, lang, filename)

    # Font
    if cfg["font"] and 'Noto Sans' not in html:
        html = html.replace(
            '<link href="https://fonts.googleapis.com/css?family=Poppins',
            cfg["font"] + '\n    <link href="https://fonts.googleapis.com/css?family=Poppins'
        )

    # Dropdown: fix active + fix all new-lang links
    html = re.sub(r'(<a class="dropdown-item) active(")', r'\1\2', html)

    for nl, (nflag, nlabel) in NEW_LANG_INFO.items():
        old = rf'href="/{nl}/[^"]*"(><span class="fi {nflag}"></span> {re.escape(nlabel)}</a>)'
        html = re.sub(old, f'href="/{nl}/{filename}"' + r'\1', html)

    # EUR dropdown links too
    for el, (eflag, elabel) in EUR_LANG_INFO.items():
        old = rf'href="/{el}/[^"]*"(><span class="fi {eflag}"></span> {re.escape(elabel)}</a>)'
        if el in existing_langs:
            html = re.sub(old, f'href="/{el}/{filename}"' + r'\1', html)

    # Set active on current lang
    html = re.sub(
        rf'(<a class="dropdown-item")(.*?href="/{lang}/{re.escape(filename)}")',
        r'<a class="dropdown-item active"\2', html
    )

    # Fix toggler label
    for old_flag, old_label in [("fi-gb","English"),("fi-fr","Français"),("fi-es","Español"),("fi-br","Português")]:
        pattern = f'<span class="fi {old_flag}"></span> {old_label}</a>'
        if pattern in html:
            html = html.replace(pattern, f'<span class="fi {flag}"></span> {label}</a>', 1)
            break

    # Guides + destination links
    html = fix_guides_link(html, lang)
    html = fix_destination_link(html, lang)

    # Legal links
    html = fix_legal_links(html, lang)

    # UI text substitutions
    for old, new in cfg["ui"]:
        html = html.replace(old, new)

    return html

# ─── Main loop ───────────────────────────────────────────────────────────────

# Get all EN indexable files
en_files = []
for f in glob.glob(os.path.join(WWW, "en", "*.html")):
    html = open(f, encoding="utf-8", errors="ignore").read(2000)
    if not is_noindex(html):
        en_files.append(os.path.basename(f))

en_files.sort()
print(f"EN indexable files: {len(en_files)}")

created = 0
skipped = 0

for filename in en_files:
    en_path = os.path.join(WWW, "en", filename)
    en_html = open(en_path, encoding="utf-8", errors="ignore").read()

    # Determine which langs actually have this file (for hreflang)
    existing = ["en"]
    for l in ["fr","es","pt","zh","th","ru","ar","ja","ko"]:
        if os.path.exists(os.path.join(WWW, l, filename)):
            existing.append(l)

    all_target_langs = list(EUR.keys()) + list(NEW.keys())

    for lang in all_target_langs:
        out_path = os.path.join(WWW, lang, filename)
        if os.path.exists(out_path):
            skipped += 1
            continue

        try:
            if lang in EUR:
                result = transform_eur(en_html, lang, filename, existing + [lang])
            else:
                result = transform_new(en_html, lang, filename, existing + [lang])

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(result)
            created += 1

            if created % 200 == 0:
                print(f"  ... {created} created so far")
        except Exception as e:
            print(f"  ERROR {lang}/{filename}: {e}")

print(f"\nDONE — created: {created} | skipped (already existed): {skipped}")
