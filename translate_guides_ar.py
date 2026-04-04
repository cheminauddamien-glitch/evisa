#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate English text in Arabic (ar) expat guide pages.
Processes all expat-guide-*.html files in www/ar/
"""

import os
import glob

# Directory containing AR guide files
AR_DIR = os.path.join(os.path.dirname(__file__), "www", "ar")

REPLACEMENTS = [
    # ── Title / meta ──────────────────────────────────────────────────────────
    ("How to Live in Thailand | eVisa-Card.com",
     "كيفية العيش في تايلاند | eVisa-Card.com"),
    ("How to Live in Portugal | eVisa-Card.com",
     "كيفية العيش في البرتغال | eVisa-Card.com"),
    ("How to Live in Spain | eVisa-Card.com",
     "كيفية العيش في إسبانيا | eVisa-Card.com"),
    ("How to Live in Japan | eVisa-Card.com",
     "كيفية العيش في اليابان | eVisa-Card.com"),
    ("How to Live in Vietnam | eVisa-Card.com",
     "كيفية العيش في فيتنام | eVisa-Card.com"),
    ("How to Live in Cambodia | eVisa-Card.com",
     "كيفية العيش في كمبوديا | eVisa-Card.com"),
    ("How to Live in Malaysia | eVisa-Card.com",
     "كيفية العيش في ماليزيا | eVisa-Card.com"),
    ("How to Live in Georgia | eVisa-Card.com",
     "كيفية العيش في جورجيا | eVisa-Card.com"),
    ("How to Live in Greece | eVisa-Card.com",
     "كيفية العيش في اليونان | eVisa-Card.com"),
    ("How to Live in Mexico | eVisa-Card.com",
     "كيفية العيش في المكسيك | eVisa-Card.com"),
    ("How to Live in Colombia | eVisa-Card.com",
     "كيفية العيش في كولومبيا | eVisa-Card.com"),
    ("How to Live in Panama | eVisa-Card.com",
     "كيفية العيش في بنما | eVisa-Card.com"),
    ("How to Live in Paraguay | eVisa-Card.com",
     "كيفية العيش في باراغواي | eVisa-Card.com"),
    ("How to Live in Costa Rica | eVisa-Card.com",
     "كيفية العيش في كوستاريكا | eVisa-Card.com"),
    ("How to Live in Laos | eVisa-Card.com",
     "كيفية العيش في لاوس | eVisa-Card.com"),
    ("How to Live in Dubai & Abu Dhabi | eVisa-Card.com",
     "كيفية العيش في دبي وأبوظبي | eVisa-Card.com"),

    # ── Page H1 titles ────────────────────────────────────────────────────────
    ("Expat Guide: Living in Thailand 2026",
     "دليل المغتربين: العيش في تايلاند 2026"),
    ("Expat Guide: Living in Portugal 2026",
     "دليل المغتربين: العيش في البرتغال 2026"),
    ("Expat Guide: Living in Spain 2026",
     "دليل المغتربين: العيش في إسبانيا 2026"),
    ("Expat Guide: Living in Japan 2026",
     "دليل المغتربين: العيش في اليابان 2026"),
    ("Expat Guide: Living in Vietnam 2026",
     "دليل المغتربين: العيش في فيتنام 2026"),
    ("Expat Guide: Living in Cambodia 2026",
     "دليل المغتربين: العيش في كمبوديا 2026"),
    ("Expat Guide: Living in Malaysia 2026",
     "دليل المغتربين: العيش في ماليزيا 2026"),
    ("Expat Guide: Living in Georgia 2026",
     "دليل المغتربين: العيش في جورجيا 2026"),
    ("Expat Guide: Living in Greece 2026",
     "دليل المغتربين: العيش في اليونان 2026"),
    ("Expat Guide: Living in Mexico 2026",
     "دليل المغتربين: العيش في المكسيك 2026"),
    ("Expat Guide: Living in Colombia 2026",
     "دليل المغتربين: العيش في كولومبيا 2026"),
    ("Expat Guide: Living in Panama 2026",
     "دليل المغتربين: العيش في بنما 2026"),
    ("Expat Guide: Living in Paraguay 2026",
     "دليل المغتربين: العيش في باراغواي 2026"),
    ("Expat Guide: Living in Costa Rica 2026",
     "دليل المغتربين: العيش في كوستاريكا 2026"),
    ("Expat Guide: Living in Laos 2026",
     "دليل المغتربين: العيش في لاوس 2026"),
    ("Expat Guide: Living in the UAE 2026",
     "دليل المغتربين: العيش في الإمارات 2026"),

    # ── Breadcrumb "Home" link ─────────────────────────────────────────────────
    ('>Home <i class="fa fa-chevron-right"></i></a>',
     '>الرئيسية <i class="fa fa-chevron-right"></i></a>'),

    # ── Breadcrumb expat guide label ───────────────────────────────────────────
    ('Expat Guide Thailand <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: تايلاند <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Portugal <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: البرتغال <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Spain <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: إسبانيا <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Japan <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: اليابان <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Vietnam <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: فيتنام <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Cambodia <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: كمبوديا <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Malaysia <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: ماليزيا <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Georgia <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: جورجيا <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Greece <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: اليونان <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Mexico <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: المكسيك <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Colombia <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: كولومبيا <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Panama <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: بنما <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Paraguay <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: باراغواي <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Costa Rica <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: كوستاريكا <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Laos <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: لاوس <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide UAE <i class="fa fa-chevron-right"></i>',
     'دليل المغتربين: الإمارات <i class="fa fa-chevron-right"></i>'),

    # ── "at a Glance" section headings ────────────────────────────────────────
    ("Thailand at a Glance", "نظرة عامة على تايلاند"),
    ("Portugal at a Glance", "نظرة عامة على البرتغال"),
    ("Spain at a Glance", "نظرة عامة على إسبانيا"),
    ("Japan at a Glance", "نظرة عامة على اليابان"),
    ("Vietnam at a Glance", "نظرة عامة على فيتنام"),
    ("Cambodia at a Glance", "نظرة عامة على كمبوديا"),
    ("Malaysia at a Glance", "نظرة عامة على ماليزيا"),
    ("Georgia at a Glance", "نظرة عامة على جورجيا"),
    ("Greece at a Glance", "نظرة عامة على اليونان"),
    ("Mexico at a Glance", "نظرة عامة على المكسيك"),
    ("Colombia at a Glance", "نظرة عامة على كولومبيا"),
    ("Panama at a Glance", "نظرة عامة على بنما"),
    ("Paraguay at a Glance", "نظرة عامة على باراغواي"),
    ("Costa Rica at a Glance", "نظرة عامة على كوستاريكا"),
    ("Laos at a Glance", "نظرة عامة على لاوس"),
    ("UAE at a Glance", "نظرة عامة على الإمارات"),

    # ── Key fact labels ───────────────────────────────────────────────────────
    ("<strong>Capital</strong>", "<strong>العاصمة</strong>"),
    ("<strong>Currency</strong>", "<strong>العملة</strong>"),
    ("<strong>Language</strong>", "<strong>اللغة</strong>"),
    ("<strong>Time Zone</strong>", "<strong>المنطقة الزمنية</strong>"),
    ("<strong>Climate</strong>", "<strong>المناخ</strong>"),

    # ── Last updated line ─────────────────────────────────────────────────────
    ("Last updated: March 2026", "آخر تحديث: مارس 2026"),
    ("Updated March 2026", "تحديث: مارس 2026"),

    # ── Section headings ─────────────────────────────────────────────────────
    ("Visa &amp; Residency Options", "خيارات التأشيرة والإقامة"),
    ("Visa & Residency Options", "خيارات التأشيرة والإقامة"),

    # Step-by-Step with country names
    ("Step-by-Step: How to Move to Thailand",
     "دليل خطوة بخطوة للانتقال إلى تايلاند"),
    ("Step-by-Step: How to Move to Portugal",
     "دليل خطوة بخطوة للانتقال إلى البرتغال"),
    ("Step-by-Step: How to Move to Spain",
     "دليل خطوة بخطوة للانتقال إلى إسبانيا"),
    ("Step-by-Step: How to Move to Japan",
     "دليل خطوة بخطوة للانتقال إلى اليابان"),
    ("Step-by-Step: How to Move to Vietnam",
     "دليل خطوة بخطوة للانتقال إلى فيتنام"),
    ("Step-by-Step: How to Move to Cambodia",
     "دليل خطوة بخطوة للانتقال إلى كمبوديا"),
    ("Step-by-Step: How to Move to Malaysia",
     "دليل خطوة بخطوة للانتقال إلى ماليزيا"),
    ("Step-by-Step: How to Move to Georgia",
     "دليل خطوة بخطوة للانتقال إلى جورجيا"),
    ("Step-by-Step: How to Move to Greece",
     "دليل خطوة بخطوة للانتقال إلى اليونان"),
    ("Step-by-Step: How to Move to Mexico",
     "دليل خطوة بخطوة للانتقال إلى المكسيك"),
    ("Step-by-Step: How to Move to Colombia",
     "دليل خطوة بخطوة للانتقال إلى كولومبيا"),
    ("Step-by-Step: How to Move to Panama",
     "دليل خطوة بخطوة للانتقال إلى بنما"),
    ("Step-by-Step: How to Move to Paraguay",
     "دليل خطوة بخطوة للانتقال إلى باراغواي"),
    ("Step-by-Step: How to Move to Costa Rica",
     "دليل خطوة بخطوة للانتقال إلى كوستاريكا"),
    ("Step-by-Step: How to Move to Laos",
     "دليل خطوة بخطوة للانتقال إلى لاوس"),
    ("Step-by-Step: How to Move to the UAE",
     "دليل خطوة بخطوة للانتقال إلى الإمارات"),

    # Practical sections
    ("🏠 Housing", "🏠 السكن"),
    ("🏦 Banking", "🏦 الخدمات المصرفية"),
    ("🏥 Healthcare", "🏥 الرعاية الصحية"),

    # Cost of Living — handle Arabic partial translations too
    ("التكلفة of Living", "تكلفة المعيشة"),
    ("💰 التكلفة of Living", "💰 تكلفة المعيشة"),
    ("Cost of Living", "تكلفة المعيشة"),
    ("💰 Cost of Living", "💰 تكلفة المعيشة"),
    # Costs artifact التكلفةs → التكاليف
    ("التكلفةs", "التكاليف"),

    ("Frequently Asked Questions", "الأسئلة المتكررة"),

    # ── Tax section ───────────────────────────────────────────────────────────
    ("Tax &amp; Fiscal Exile", "الضرائب والإقامة الضريبية"),
    ("Tax & Fiscal Exile", "الضرائب والإقامة الضريبية"),
    ("Capital Gains Tax", "ضريبة أرباح رأس المال"),
    ("Tax Regime", "النظام الضريبي"),
    ("Crypto-Friendliness", "الموقف من العملات المشفرة"),
    ("Exit Tax", "ضريبة الخروج"),
    ("Key Tax Points", "النقاط الضريبية الرئيسية"),
    ("Simulate Your Tax Savings", "احسب وفورات الضرائب"),
    ("Use our free tax exile simulator to compare your tax savings",
     "استخدم أداتنا المجانية لمقارنة وفورات الضرائب"),
    ("Tax information provided for general guidance only. Consult a qualified tax advisor before making relocation decisions.",
     "المعلومات الضريبية مقدمة للإرشاد العام فقط. استشر مستشاراً ضريبياً مؤهلاً قبل اتخاذ قرارات الانتقال."),

    # ── Author box ────────────────────────────────────────────────────────────
    ("Editorial Team — eVisa-Card.com", "الفريق التحريري — eVisa-Card.com"),
    (">Expat guides written by travel experts, immigration specialists and expats with first-hand experience in",
     ">أدلة المغتربين كتبها خبراء السفر ومتخصصو الهجرة والمغتربون ذوو الخبرة المباشرة في"),
    ("&#x2714; Verified information", "&#x2714; معلومات موثقة"),
    ("&#x2714; Updated March 2026", "&#x2714; تحديث مارس 2026"),
    ("&#x2714; Official sources cited", "&#x2714; مصادر رسمية"),

    # ── Official Sources section ───────────────────────────────────────────────
    ("&#128218; Official Sources &amp; References",
     "&#128218; المصادر والمراجع الرسمية"),

    # ── Pro Tips ─────────────────────────────────────────────────────────────
    ("Pro Tips", "نصائح الخبراء"),

    # ── Table headers ─────────────────────────────────────────────────────────
    (">Visa Type<", ">نوع التأشيرة<"),
    (">Stay<", ">مدة الإقامة<"),
    (">Requirements<", ">المتطلبات<"),
    (">Best For<", ">الأنسب لـ<"),
    (">Fee<", ">الرسوم<"),
    (">Processing<", ">وقت المعالجة<"),

    # Badge labels
    (">Mandatory<", ">إلزامي<"),
    (">Recommended<", ">موصى به<"),
    (">Optional<", ">اختياري<"),
    ("Mandatory</", "إلزامي</"),
    ("Recommended</", "موصى به</"),
    ("Optional</", "اختياري</"),

    # Per-period labels
    ("/year", " سنوياً"),
    ("/month", " شهرياً"),
    ("/night", " لليلة الواحدة"),
    ("per year", "سنوياً"),
    ("per month", "شهرياً"),
    ("per night", "لليلة الواحدة"),

    # Yes / No
    (">Yes<", ">نعم<"),
    (">No<", ">لا<"),

    # ── Footer ────────────────────────────────────────────────────────────────
    ("Global eVisa &amp; Travel Information Platform",
     "منصة معلومات التأشيرة الإلكترونية والسفر العالمية"),
    ("Global eVisa & Travel Information Platform",
     "منصة معلومات التأشيرة الإلكترونية والسفر العالمية"),
    ("Follow eVisa-Card.com", "تابعوا eVisa-Card.com"),
]


def translate_file(filepath: str) -> tuple[int, int]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    total_changes = 0
    patterns_applied = 0

    for pattern, replacement in REPLACEMENTS:
        if pattern in content:
            count = content.count(pattern)
            content = content.replace(pattern, replacement)
            total_changes += count
            patterns_applied += 1

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return total_changes, patterns_applied


def main():
    files = sorted(glob.glob(os.path.join(AR_DIR, "expat-guide-*.html")))
    if not files:
        print(f"No expat-guide-*.html files found in {AR_DIR}")
        return

    print(f"Found {len(files)} expat guide files in {AR_DIR}\n")

    grand_total = 0
    for filepath in files:
        name = os.path.basename(filepath)
        changes, patterns = translate_file(filepath)
        grand_total += changes
        if changes:
            print(f"  [OK] {name:45s} {changes:4d} replacement(s) across {patterns} pattern(s)")
        else:
            print(f"  [--] {name:45s}  (no changes needed)")

    print(f"\nDone. Total replacements made: {grand_total}")


if __name__ == "__main__":
    main()
