#!/usr/bin/env python3
"""
Translate English UI/table text in expat-guide pages for ZH, JA, KO, RU, AR, TH languages.
Processes 6 languages x 16 countries = 96 files.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WWW_DIR = os.path.join(BASE_DIR, "www")

LANGUAGES = ["zh", "ja", "ko", "ru", "ar", "th"]

COUNTRIES = [
    "thailand", "portugal", "spain", "mexico", "vietnam", "malaysia",
    "japan", "uae", "colombia", "panama", "costa-rica", "greece",
    "georgia", "paraguay", "laos", "cambodia"
]

# ---------------------------------------------------------------------------
# Translation dictionaries per language
# Order matters: longer / more specific strings first to avoid partial matches
# ---------------------------------------------------------------------------

TRANSLATIONS = {
    "zh": [
        # Typo variant first
        ("Estimated Cout", "预估费用"),
        # Multi-word phrases (longer first)
        ("Available Type de Visas", "可用签证类型"),
        ("Available Visa Types", "可用签证类型"),
        ("Step-by-Step Residency Process", "居留申请步骤"),
        ("Typical Healthcare Costs", "典型医疗费用"),
        ("Typical Purchase Costs", "购买费用"),
        ("Ownership Options for Foreigners", "外国人产权选择"),
        ("Top Providers for Expats", "最佳外籍人士保险公司"),
        ("Hospitalisation (per night)", "住院（每晚）"),
        ("Eye exam + glasses", "视力检查+眼镜"),
        ("Specialist consultation", "专科医生咨询"),
        ("GP consultation", "全科医生咨询"),
        ("Emergency room visit", "急诊就诊"),
        ("Dental cleaning", "洁牙"),
        ("Public Healthcare", "公立医疗"),
        ("Private Healthcare", "私立医疗"),
        ("Recommended Banks", "推荐银行"),
        ("Required Documents", "所需文件"),
        ("Purchase Process", "购买流程"),
        ("Related Expat Guides", "相关移居指南"),
        ("All Expat Guides", "所有移居指南"),
        ("About This Guide", "关于本指南"),
        ("Estimated Cost", "预估费用"),
        ("Agent commission", "中介佣金"),
        ("Withholding tax", "预扣税"),
        ("Transfer fee", "过户费"),
        ("Stamp duty", "印花税"),
        ("Lawyer fees", "律师费"),
        ("Pro Tip:", "专家提示："),
        ("Recommended:", "推荐："),
        ("Visa Type", "签证类型"),
        ("Details", "详情"),
        ("Service", "服务"),
        ("Cost", "费用"),
        # Fix links
        ('href="/en/', 'href="/zh/'),
    ],
    "ja": [
        ("Estimated Cout", "推定費用"),
        ("Available Type de Visas", "利用可能なビザの種類"),
        ("Available Visa Types", "利用可能なビザの種類"),
        ("Step-by-Step Residency Process", "居住申請手順"),
        ("Typical Healthcare Costs", "一般的な医療費"),
        ("Typical Purchase Costs", "購入費用"),
        ("Ownership Options for Foreigners", "外国人の不動産所有オプション"),
        ("Top Providers for Expats", "外国人向け保険会社"),
        ("Hospitalisation (per night)", "入院（1泊あたり）"),
        ("Eye exam + glasses", "視力検査＋メガネ"),
        ("Specialist consultation", "専門医診療"),
        ("GP consultation", "一般診療"),
        ("Emergency room visit", "救急外来"),
        ("Dental cleaning", "歯のクリーニング"),
        ("Public Healthcare", "公的医療"),
        ("Private Healthcare", "民間医療"),
        ("Recommended Banks", "おすすめ銀行"),
        ("Required Documents", "必要書類"),
        ("Purchase Process", "購入手順"),
        ("Related Expat Guides", "関連ガイド"),
        ("All Expat Guides", "すべてのガイド"),
        ("About This Guide", "このガイドについて"),
        ("Estimated Cost", "推定費用"),
        ("Pro Tip:", "プロのヒント："),
        ("Visa Type", "ビザの種類"),
        ("Details", "詳細"),
        ("Service", "サービス"),
        ("Cost", "費用"),
        ('href="/en/', 'href="/ja/'),
    ],
    "ko": [
        ("Estimated Cout", "예상 비용"),
        ("Available Type de Visas", "이용 가능한 비자 유형"),
        ("Available Visa Types", "이용 가능한 비자 유형"),
        ("Step-by-Step Residency Process", "거주 신청 절차"),
        ("Typical Healthcare Costs", "일반 의료비"),
        ("Typical Purchase Costs", "구매 비용"),
        ("Ownership Options for Foreigners", "외국인 부동산 소유 옵션"),
        ("Top Providers for Expats", "외국인 추천 보험사"),
        ("Hospitalisation (per night)", "입원 (1박당)"),
        ("Eye exam + glasses", "시력 검사 + 안경"),
        ("Specialist consultation", "전문의 진료"),
        ("GP consultation", "일반 진료"),
        ("Emergency room visit", "응급실 방문"),
        ("Dental cleaning", "치과 스케일링"),
        ("Public Healthcare", "공공 의료"),
        ("Private Healthcare", "민간 의료"),
        ("Recommended Banks", "추천 은행"),
        ("Required Documents", "필요 서류"),
        ("Purchase Process", "구매 절차"),
        ("Related Expat Guides", "관련 가이드"),
        ("All Expat Guides", "모든 가이드"),
        ("About This Guide", "이 가이드 소개"),
        ("Estimated Cost", "예상 비용"),
        ("Pro Tip:", "전문가 팁:"),
        ("Visa Type", "비자 유형"),
        ("Details", "세부사항"),
        ("Service", "서비스"),
        ("Cost", "비용"),
        ('href="/en/', 'href="/ko/'),
    ],
    "ru": [
        ("Estimated Cout", "Ориентировочная стоимость"),
        ("Available Type de Visas", "Доступные типы виз"),
        ("Available Visa Types", "Доступные типы виз"),
        ("Step-by-Step Residency Process", "Пошаговый процесс получения ВНЖ"),
        ("Typical Healthcare Costs", "Типичные расходы на здравоохранение"),
        ("Ownership Options for Foreigners", "Варианты владения недвижимостью для иностранцев"),
        ("Top Providers for Expats", "Лучшие страховщики для экспатов"),
        ("Hospitalisation (per night)", "Госпитализация (за ночь)"),
        ("Eye exam + glasses", "Проверка зрения + очки"),
        ("Specialist consultation", "Прием специалиста"),
        ("GP consultation", "Прием терапевта"),
        ("Emergency room visit", "Визит в скорую помощь"),
        ("Dental cleaning", "Чистка зубов"),
        ("Public Healthcare", "Государственная медицина"),
        ("Private Healthcare", "Частная медицина"),
        ("Recommended Banks", "Рекомендуемые банки"),
        ("Required Documents", "Необходимые документы"),
        ("Purchase Process", "Процесс покупки"),
        ("Related Expat Guides", "Связанные руководства"),
        ("All Expat Guides", "Все руководства"),
        ("About This Guide", "О данном руководстве"),
        ("Estimated Cost", "Ориентировочная стоимость"),
        ("Pro Tip:", "Совет:"),
        ("Visa Type", "Тип визы"),
        ("Details", "Подробности"),
        ("Service", "Услуга"),
        ("Cost", "Стоимость"),
        ('href="/en/', 'href="/ru/'),
    ],
    "ar": [
        ("Estimated Cout", "التكلفة التقديرية"),
        ("Available Type de Visas", "أنواع التأشيرات المتاحة"),
        ("Available Visa Types", "أنواع التأشيرات المتاحة"),
        ("Step-by-Step Residency Process", "خطوات الحصول على الإقامة"),
        ("Typical Healthcare Costs", "التكاليف الطبية النموذجية"),
        ("Ownership Options for Foreigners", "خيارات التملك للأجانب"),
        ("Top Providers for Expats", "أفضل شركات التأمين للمغتربين"),
        ("Hospitalisation (per night)", "الإقامة في المستشفى (لليلة)"),
        ("Eye exam + glasses", "فحص النظر + نظارات"),
        ("Specialist consultation", "استشارة أخصائي"),
        ("GP consultation", "استشارة طبيب عام"),
        ("Emergency room visit", "زيارة غرفة الطوارئ"),
        ("Dental cleaning", "تنظيف الأسنان"),
        ("Public Healthcare", "الرعاية الصحية العامة"),
        ("Private Healthcare", "الرعاية الصحية الخاصة"),
        ("Recommended Banks", "البنوك الموصى بها"),
        ("Required Documents", "المستندات المطلوبة"),
        ("Purchase Process", "عملية الشراء"),
        ("Related Expat Guides", "أدلة ذات صلة"),
        ("All Expat Guides", "جميع الأدلة"),
        ("About This Guide", "حول هذا الدليل"),
        ("Estimated Cost", "التكلفة التقديرية"),
        ("Pro Tip:", "نصيحة:"),
        ("Visa Type", "نوع التأشيرة"),
        ("Details", "التفاصيل"),
        ("Service", "الخدمة"),
        ("Cost", "التكلفة"),
        ('href="/en/', 'href="/ar/'),
    ],
    "th": [
        ("Estimated Cout", "ค่าใช้จ่ายโดยประมาณ"),
        ("Available Type de Visas", "ประเภทวีซ่าที่มี"),
        ("Available Visa Types", "ประเภทวีซ่าที่มี"),
        ("Step-by-Step Residency Process", "ขั้นตอนการขอถิ่นที่อยู่"),
        ("Typical Healthcare Costs", "ค่ารักษาพยาบาลทั่วไป"),
        ("Ownership Options for Foreigners", "ตัวเลือกการถือครองสำหรับชาวต่างชาติ"),
        ("Top Providers for Expats", "บริษัทประกันแนะนำสำหรับชาวต่างชาติ"),
        ("Hospitalisation (per night)", "ค่าห้องพัก (ต่อคืน)"),
        ("Eye exam + glasses", "ตรวจสายตา + แว่นตา"),
        ("Specialist consultation", "พบแพทย์เฉพาะทาง"),
        ("GP consultation", "พบแพทย์ทั่วไป"),
        ("Emergency room visit", "ห้องฉุกเฉิน"),
        ("Dental cleaning", "ทำความสะอาดฟัน"),
        ("Public Healthcare", "สาธารณสุข"),
        ("Private Healthcare", "โรงพยาบาลเอกชน"),
        ("Recommended Banks", "ธนาคารแนะนำ"),
        ("Required Documents", "เอกสารที่ต้องใช้"),
        ("Purchase Process", "ขั้นตอนการซื้อ"),
        ("Related Expat Guides", "คู่มือที่เกี่ยวข้อง"),
        ("All Expat Guides", "คู่มือทั้งหมด"),
        ("About This Guide", "เกี่ยวกับคู่มือนี้"),
        ("Estimated Cost", "ค่าใช้จ่ายโดยประมาณ"),
        ("Pro Tip:", "เคล็ดลับ:"),
        ("Visa Type", "ประเภทวีซ่า"),
        ("Details", "รายละเอียด"),
        ("Service", "บริการ"),
        ("Cost", "ค่าใช้จ่าย"),
        ('href="/en/', 'href="/th/'),
    ],
}


def translate_file(filepath, replacements):
    """Apply all replacements to a single file. Returns number of replacements made."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    total_replacements = 0
    for english, translated in replacements:
        count = content.count(english)
        if count > 0:
            content = content.replace(english, translated)
            total_replacements += count

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return total_replacements


def main():
    grand_total = 0

    for lang in LANGUAGES:
        replacements = TRANSLATIONS[lang]
        lang_dir = os.path.join(WWW_DIR, lang)
        lang_total = 0
        files_processed = 0
        files_changed = 0

        for country in COUNTRIES:
            filename = f"expat-guide-{country}.html"
            filepath = os.path.join(lang_dir, filename)

            if not os.path.isfile(filepath):
                print(f"  [SKIP] {filepath} — file not found")
                continue

            count = translate_file(filepath, replacements)
            files_processed += 1
            if count > 0:
                files_changed += 1
            lang_total += count

        print(f"[{lang.upper()}] {files_processed} files processed, "
              f"{files_changed} files changed, "
              f"{lang_total} total replacements")
        grand_total += lang_total

    print(f"\n=== DONE === {grand_total} total replacements across "
          f"{len(LANGUAGES)} languages x {len(COUNTRIES)} countries")


if __name__ == "__main__":
    main()
