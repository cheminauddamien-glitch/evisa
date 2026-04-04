#!/usr/bin/env python3
"""
fix_expat_guides_index_and_dates.py
1. Add 7 missing country cards to expat-guides.html for all 9 non-EN language dirs
2. Update visible "2025" year references → 2026 in blog articles across all langs
"""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"

# ── Per-language data ────────────────────────────────────────────────────────

LANGS = {
    "fr": {
        "btn": "Lire le Guide →",
        "countries": {
            "panama":     ("Panama",    "pa", "Économie dollarisée, avantages Pensionado, aucun impôt sur les revenus étrangers. L'un des programmes de RP les plus faciles au monde."),
            "costa-rica": ("Costa Rica","cr", "Style de vie Pura Vida, biodiversité exceptionnelle, visa Pensionado abordable à 1 000 $/mois. Santé publique CAJA incluse."),
            "greece":     ("Grèce",     "gr", "Golden Visa à partir de 250 000 €, régime Non-Dom à 100 000 € forfait, visa FIP pour nomades. Art de vivre méditerranéen."),
            "georgia":    ("Géorgie",   "ge", "Séjour visa-free 365 jours, impôt forfaitaire 1 % pour petites entreprises, compte bancaire le jour même, coût de vie ultra-abordable."),
            "paraguay":   ("Paraguay",  "py", "RP la moins chère d'Amérique latine (~5 500 $ de dépôt), système fiscal territorial, coût de vie dès 800 $/mois."),
            "laos":       ("Laos",      "la", "Joyau ultra-abordable d'Asie du Sud-Est. Visa LTR renouvelable, coût de vie dès 600 $/mois à Vientiane."),
            "cambodia":   ("Cambodge",  "kh", "Visa My Khmer Home, économie en dollars, appartements dès 50 000 $ à Phnom Penh. Coût de vie dès 700 $/mois."),
        },
    },
    "es": {
        "btn": "Leer la Guía →",
        "countries": {
            "panama":     ("Panamá",      "pa", "Economía dolarizada, descuentos Pensionado, sin impuesto sobre ingresos extranjeros. Uno de los programas de RP más fáciles del mundo."),
            "costa-rica": ("Costa Rica",  "cr", "Estilo de vida Pura Vida, excelente biodiversidad, visa Pensionado asequible con $1,000/mes. Salud pública CAJA incluida."),
            "greece":     ("Grecia",      "gr", "Visa Dorada desde €250k, impuesto Non-Dom €100k fijo, visa FIP para trabajadores remotos. Estilo de vida mediterráneo asequible."),
            "georgia":    ("Georgia",     "ge", "365 días sin visa, impuesto plano del 1% para pequeñas empresas, cuenta bancaria el mismo día, costo de vida ultra asequible."),
            "paraguay":   ("Paraguay",    "py", "PR más barata de Latinoamérica (~$5,500 depósito), sistema fiscal territorial, bajo costo de vida desde $800/mes."),
            "laos":       ("Laos",        "la", "Joya ultra asequible del Sudeste Asiático. Visa LTR renovable, costo de vida desde $600/mes en Vientiane."),
            "cambodia":   ("Camboya",     "kh", "Visa My Khmer Home, economía en dólares, apartamentos desde $50k en Phnom Penh. Costo de vida desde $700/mes."),
        },
    },
    "pt": {
        "btn": "Ler o Guia →",
        "countries": {
            "panama":     ("Panamá",      "pa", "Economia dolarizada, descontos Pensionado, sem imposto sobre rendimentos estrangeiros. Um dos programas de RP mais fáceis do mundo."),
            "costa-rica": ("Costa Rica",  "cr", "Estilo de vida Pura Vida, excelente biodiversidade, visto Pensionado acessível com $1.000/mês. Saúde pública CAJA incluída."),
            "greece":     ("Grécia",      "gr", "Golden Visa a partir de €250k, imposto Non-Dom €100k fixo, visto FIP para trabalhadores remotos. Estilo de vida mediterrâneo."),
            "georgia":    ("Geórgia",     "ge", "365 dias sem visto, imposto fixo de 1% para pequenas empresas, conta bancária no mesmo dia, custo de vida ultra-acessível."),
            "paraguay":   ("Paraguai",    "py", "RP mais barata da América Latina (~$5.500 depósito), sistema fiscal territorial, baixo custo de vida a partir de $800/mês."),
            "laos":       ("Laos",        "la", "Joia ultra-acessível do Sudeste Asiático. Visto LTR renovável, custo de vida a partir de $600/mês em Vientiane."),
            "cambodia":   ("Camboja",     "kh", "Visto My Khmer Home, economia em dólares, apartamentos a partir de $50k em Phnom Penh. Custo de vida a partir de $700/mês."),
        },
    },
    "zh": {
        "btn": "阅读指南 →",
        "countries": {
            "panama":     ("巴拿马",  "pa", "美元化经济，退休金签证享有折扣，境外收入免税。全球最易获批的永居项目之一。"),
            "costa-rica": ("哥斯达黎加","cr","Pura Vida生活方式，生态资源丰富，退休金签证每月仅需$1,000。含CAJA公共医疗。"),
            "greece":     ("希腊",    "gr", "黄金签证低至€25万，Non-Dom定额税€10万，FIP签证适合远程工作者。地中海生活方式。"),
            "georgia":    ("格鲁吉亚","ge", "免签居留365天，小企业1%统一税率，当天开户，生活成本极低。"),
            "paraguay":   ("巴拉圭",  "py", "拉丁美洲最便宜的永居（约$5,500存款），属地税收制度，生活费低至$800/月。"),
            "laos":       ("老挝",    "la", "东南亚超实惠之地。LTR签证可续签，万象生活费低至$600/月。"),
            "cambodia":   ("柬埔寨",  "kh", "My Khmer Home签证，美元经济，金边公寓低至$5万。生活费低至$700/月。"),
        },
    },
    "th": {
        "btn": "อ่านคู่มือ →",
        "countries": {
            "panama":     ("ปานามา",    "pa", "เศรษฐกิจใช้เงินดอลลาร์ ส่วนลด Pensionado ไม่มีภาษีรายได้ต่างประเทศ โปรแกรม PR ที่ของ่ายที่สุดในโลก"),
            "costa-rica": ("คอสตาริกา","cr", "ไลฟ์สไตล์ Pura Vida วีซ่า Pensionado $1,000/เดือน รวมประกันสุขภาพ CAJA"),
            "greece":     ("กรีซ",     "gr", "Golden Visa €250k ภาษีแบบเหมา Non-Dom €100k วีซ่า FIP สำหรับ Remote Worker"),
            "georgia":    ("จอร์เจีย", "ge", "อยู่ได้ 365 วันไม่ต้องวีซ่า ภาษีธุรกิจเล็ก 1% เปิดบัญชีธนาคารได้ในวันเดียว"),
            "paraguay":   ("ปารากวัย", "py", "PR ถูกที่สุดในลาตินอเมริกา (~$5,500 ฝากเงิน) ระบบภาษีเฉพาะในประเทศ"),
            "laos":       ("ลาว",      "la", "อัญมณีเอเชียตะวันออกเฉียงใต้ราคาประหยัด วีซ่า LTR ต่ออายุได้ ค่าครองชีพ $600/เดือน"),
            "cambodia":   ("กัมพูชา",  "kh", "วีซ่า My Khmer Home เศรษฐกิจดอลลาร์ คอนโดพนมเปญเริ่ม $50k"),
        },
    },
    "ru": {
        "btn": "Читать гид →",
        "countries": {
            "panama":     ("Панама",    "pa", "Долларизованная экономика, льготы Pensionado, нет налога на зарубежный доход. Один из самых простых ВНЖ в мире."),
            "costa-rica": ("Коста-Рика","cr", "Стиль жизни Pura Vida, виза Pensionado от $1,000/мес, государственная медстраховка CAJA включена."),
            "greece":     ("Греция",    "gr", "Золотая виза от €250k, фиксированный налог Non-Dom €100k, виза FIP для удалёнщиков. Средиземноморский стиль жизни."),
            "georgia":    ("Грузия",    "ge", "365 дней без визы, налог 1% для малого бизнеса, счёт в банке в тот же день, низкая стоимость жизни."),
            "paraguay":   ("Парагвай",  "py", "Самый дешёвый ВНЖ в Латинской Америке (~$5,500 вклад), территориальная система налогов."),
            "laos":       ("Лаос",      "la", "Доступная жемчужина Юго-Восточной Азии. Виза LTR с продлением, жизнь от $600/мес в Вьентьяне."),
            "cambodia":   ("Камбоджа",  "kh", "Виза My Khmer Home, долларовая экономика, квартиры в Пномпене от $50k. Жизнь от $700/мес."),
        },
    },
    "ar": {
        "btn": "اقرأ الدليل →",
        "countries": {
            "panama":     ("بنما",       "pa", "اقتصاد مدولر، مزايا تأشيرة المتقاعدين، لا ضريبة على الدخل الأجنبي. من أسهل برامج الإقامة الدائمة في العالم."),
            "costa-rica": ("كوستاريكا",  "cr", "أسلوب حياة Pura Vida، تأشيرة معاش $1,000/شهر، تغطية الرعاية الصحية CAJA مشمولة."),
            "greece":     ("اليونان",    "gr", "تأشيرة ذهبية من €250k، ضريبة Non-Dom €100k ثابتة، تأشيرة FIP للعمل عن بُعد."),
            "georgia":    ("جورجيا",     "ge", "إقامة 365 يوماً بدون تأشيرة، ضريبة 1% للأعمال الصغيرة، فتح حساب بنكي في نفس اليوم."),
            "paraguay":   ("باراغواي",   "py", "أرخص إقامة دائمة في أمريكا اللاتينية (~$5,500 وديعة)، نظام ضريبي إقليمي."),
            "laos":       ("لاوس",       "la", "جوهرة جنوب شرق آسيا بأسعار معقولة. تأشيرة LTR قابلة للتجديد، تكاليف معيشة من $600/شهر."),
            "cambodia":   ("كمبوديا",    "kh", "تأشيرة My Khmer Home، اقتصاد بالدولار، شقق بنوم بنه من $50k. تكاليف معيشة من $700/شهر."),
        },
    },
    "ja": {
        "btn": "ガイドを読む →",
        "countries": {
            "panama":     ("パナマ",      "pa", "ドル経済、Pensionadoビザの特典、海外収入非課税。世界最も取得しやすい永住権プログラムの一つ。"),
            "costa-rica": ("コスタリカ",  "cr", "Pura Vidaライフスタイル、月$1,000のPensionadoビザ、CAJA公的健康保険付き。"),
            "greece":     ("ギリシャ",    "gr", "ゴールデンビザ€25万〜、Non-Dom定額税€10万、リモートワーカー向けFIPビザ。地中海の生活。"),
            "georgia":    ("ジョージア",  "ge", "365日ビザ不要滞在、中小企業1%定率税、当日銀行口座開設、超低コスト生活。"),
            "paraguay":   ("パラグアイ",  "py", "中南米最安の永住権（約$5,500入金）、属地主義税制、生活費は月$800〜。"),
            "laos":       ("ラオス",      "la", "東南アジアの超リーズナブルな隠れ家。LTRビザ更新可、ビエンチャンで月$600〜の生活。"),
            "cambodia":   ("カンボジア",  "kh", "My Khmer Homeビザ、ドル経済、プノンペンのコンドミニアム$5万〜。月$700〜の生活。"),
        },
    },
    "ko": {
        "btn": "가이드 읽기 →",
        "countries": {
            "panama":     ("파나마",    "pa", "달러 경제, Pensionado 혜택, 해외 소득 무세금. 세계에서 가장 쉬운 영주권 프로그램 중 하나."),
            "costa-rica": ("코스타리카","cr", "Pura Vida 라이프스타일, 월 $1,000 Pensionado 비자, CAJA 공공 의료 포함."),
            "greece":     ("그리스",    "gr", "골든 비자 €25만〜, Non-Dom 정액세 €10만, 원격 근무자용 FIP 비자. 지중해 생활."),
            "georgia":    ("조지아",    "ge", "365일 무비자 체류, 소기업 1% 단일세율, 당일 계좌 개설, 초저렴 생활비."),
            "paraguay":   ("파라과이",  "py", "중남미 최저 영주권 (~$5,500 예금), 속지주의 세금 제도, 월 $800〜 생활비."),
            "laos":       ("라오스",    "la", "동남아시아의 초저렴 숨은 보석. LTR 비자 갱신 가능, 비엔티안 월 $600〜 생활."),
            "cambodia":   ("캄보디아",  "kh", "My Khmer Home 비자, 달러 경제, 프놈펜 콘도 $5만〜. 월 $700〜 생활비."),
        },
    },
}


def make_card_full(lang_code, slug, name, flag, desc, btn):
    """Full image card for FR/ES/PT."""
    return f'''                <div class="col-md-4 col-sm-6 mb-4">
                    <div class="card h-100 shadow-sm border-0" style="border-radius:8px;overflow:hidden;">
                        <div style="height:160px;overflow:hidden;position:relative;">
                            <img src="https://flagcdn.com/w640/{flag}.png" alt="{name}" style="width:100%;height:100%;object-fit:cover;object-position:center;"/>
                            <div style="position:absolute;inset:0;background:rgba(13,36,97,0.55);"></div>
                            <h5 style="position:absolute;bottom:12px;left:16px;right:16px;color:#fff;margin:0;font-size:1.2rem;font-weight:700;">{name}</h5>
                        </div>
                        <div class="card-body d-flex flex-column">
                            <p style="font-size:.88rem;color:#555;flex:1;margin-bottom:12px;">{desc}</p>
                            <a href="/{lang_code}/expat-guide-{slug}.html" class="btn btn-primary btn-sm align-self-start">{btn}</a>
                        </div>
                    </div>
                </div>'''


def make_card_simple(lang_code, slug, name, flag, btn):
    """Simple flag+button card for ZH/TH/RU/AR/JA/KO."""
    return f'''        <div class="col-md-4 mb-4">
          <div class="card h-100">
            <div class="card-body text-center">
              <span class="fi fi-{flag}" style="font-size:2rem;"></span>
              <h3 class="h5 mt-2">{name}</h3>
              <a href="/{lang_code}/expat-guide-{slug}.html" class="btn btn-outline-primary btn-sm mt-2">{btn}</a>
            </div>
          </div>
        </div>'''


SIMPLE_LANGS = {"zh", "th", "ru", "ar", "ja", "ko"}
FULL_LANGS   = {"fr", "es", "pt"}


def fix_expat_guides_index():
    fixed = 0
    for lang_code, data in LANGS.items():
        filepath = os.path.join(BASE, lang_code, "expat-guides.html")
        if not os.path.isfile(filepath):
            print(f"  MISSING: {filepath}")
            continue

        with open(filepath, encoding="utf-8", errors="ignore") as f:
            html = f.read()

        # Check which country slugs are already present
        new_cards = ""
        for slug, (name, flag, desc) in data["countries"].items():
            if f"expat-guide-{slug}.html" not in html:
                if lang_code in FULL_LANGS:
                    new_cards += make_card_full(lang_code, slug, name, flag, desc, data["btn"]) + "\n"
                else:
                    new_cards += make_card_simple(lang_code, slug, name, flag, data["btn"]) + "\n"

        if not new_cards:
            print(f"  SKIP {lang_code}/expat-guides.html (all countries present)")
            continue

        # Try multiple anchor patterns (indentation differs by lang)
        anchors = [
            "        </div>\n    </div>\n</section>",   # FR/ES/PT
            "    </div>\n  </div>\n</section>",          # ZH/TH/RU/AR/JA/KO
            "    </div>\n</section>",                    # fallback
        ]
        inserted = False
        for anchor in anchors:
            if anchor in html:
                html = html.replace(anchor, new_cards + anchor, 1)
                inserted = True
                break

        if not inserted:
            print(f"  WARN: Could not find anchor in {lang_code}/expat-guides.html")
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        added = len([s for s in data["countries"] if f"expat-guide-{s}.html" not in open(filepath, encoding='utf-8').read().replace(new_cards, "")])
        print(f"  OK {lang_code}/expat-guides.html")
        fixed += 1

    return fixed


def update_blog_dates():
    """Replace visible year '2025' with '2026' in blog-style date strings across all langs."""
    updated = 0
    # Date patterns that should be updated to 2026
    patterns = [
        # "January 2025", "February 2025" ... "December 2025"
        (r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+2025\b', r'\1 2026'),
        # "2025" in date schema fields
        (r'("datePublished"\s*:\s*")\d{4}(-\d{2}-\d{2}")', r'\g<1>2026\2'),
        (r'("dateModified"\s*:\s*")\d{4}(-\d{2}-\d{2}")', r'\g<1>2026\2'),
        # "© 2025"
        (r'©\s*2025', '© 2026'),
        # "Updated: 2025" / "Last updated: 2025"
        (r'((?:Last\s+)?[Uu]pdated?:?\s*)2025', r'\g<1>2026'),
        # "mis à jour.*2025", "Dernière mise à jour.*2025"
        (r'((?:Mis à jour|Dernière mise à jour|Actualizado|Atualizado|Обновлено)\s*:?\s*)2025', r'\g<1>2026'),
    ]

    langs_all = ["en","fr","es","pt","zh","th","ru","ar","ja","ko"]
    for lang in langs_all:
        lang_dir = os.path.join(BASE, lang)
        if not os.path.isdir(lang_dir):
            continue
        for fname in os.listdir(lang_dir):
            if not fname.endswith(".html"):
                continue
            fpath = os.path.join(lang_dir, fname)
            try:
                with open(fpath, encoding="utf-8", errors="ignore") as f:
                    html = f.read()
            except Exception:
                continue

            new_html = html
            for pat, rep in patterns:
                new_html = re.sub(pat, rep, new_html)

            if new_html != html:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_html)
                updated += 1

    return updated


if __name__ == "__main__":
    print("=== 1. Adding missing country cards to expat-guides.html ===")
    g = fix_expat_guides_index()
    print(f"    {g} index pages updated\n")

    print("=== 2. Updating 2025 to 2026 date references site-wide ===")
    d = update_blog_dates()
    print(f"    {d} HTML files updated with 2026 dates")

    print("\nDone.")
