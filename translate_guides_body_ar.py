#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate remaining English body content in AR expat guide pages."""
import os

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\ar"

REPLACEMENTS = [
    # ── PAGE TITLES ──────────────────────────────────────────────────────────
    ("Complete Expat Guide Cambodia 2026 — Live & Retire in Cambodia", "دليل المغتربين الكامل كمبوديا 2026 — الحياة في كمبوديا"),
    ("Expat Guide Colombia 2026 — Live & Work in Colombia | eVisa-Card.com", "دليل المغتربين كولومبيا 2026 — الحياة في كولومبيا | eVisa-Card.com"),
    ("Complete Expat Guide Georgia 2026 — Live & Work in Georgia (Caucasus)", "دليل المغتربين الكامل جورجيا 2026 — الحياة في جورجيا"),
    ("Complete Expat Guide Greece 2026 — Live & Retire in Greece", "دليل المغتربين الكامل اليونان 2026 — الحياة في اليونان"),
    ("Complete Expat Guide Laos 2026 — Live & Work in Laos", "دليل المغتربين الكامل لاوس 2026 — الحياة في لاوس"),
    ("Complete Expat Guide Panama 2026 — Live & Retire in Panama", "دليل المغتربين الكامل بنما 2026 — الحياة في بنما"),
    ("Complete Expat Guide Paraguay 2026 — Live & Retire in Paraguay", "دليل المغتربين الكامل باراغواي 2026 — الحياة في باراغواي"),
    ("Expat Guide UAE 2026 — How to Live in Dubai & Abu Dhabi | eVisa-Card.com", "دليل المغتربين الإمارات 2026 — الحياة في دبي وأبوظبي | eVisa-Card.com"),
    ("Complete Expat Guide Costa Rica 2026 — Live & Retire in Costa Rica", "دليل المغتربين الكامل كوستاريكا 2026 — الحياة في كوستاريكا"),

    # ── VISA SECTION ─────────────────────────────────────────────────────────
    ("Thailand offers several long-stay options: the Tourist Visa (60 days, extendable), Non-Immigrant O-A Retirement Visa (1 year, renewable, for 50+), Thailand Elite Visa (5–20 years, premium), Long-Term Resident (LTR) Visa for professionals and digital nomads. There is no standard permanent residency path but long-term visa holders can renew indefinitely.",
     "تقدم تايلاند عدة خيارات للإقامة طويلة الأمد: تأشيرة سياحية (60 يوماً، قابلة للتمديد)، تأشيرة التقاعد O-A غير المهاجرة (سنة، قابلة للتجديد، لمن هم فوق 50)، تأشيرة تايلاند إيليت (5-20 سنة، مميزة)، تأشيرة المقيم طويل الأمد (LTR) للمهنيين والعمال الرقميين. لا يوجد مسار للإقامة الدائمة المعتادة لكن يمكن لحاملي التأشيرات طويلة الأمد التجديد إلى أجل غير مسمى."),

    # ── STEP-BY-STEP ─────────────────────────────────────────────────────────
    ("Choose your visa type", "اختر نوع تأشيرتك"),
    ("Gather required documents", "اجمع المستندات المطلوبة"),
    ("Apply at a Thai embassy or consulate", "تقدم بطلب في السفارة أو القنصلية التايلاندية"),
    ("Arrive and register your address", "اصل وسجّل عنوانك"),
    ("Open a Thai bank account", "افتح حساباً مصرفياً تايلاندياً"),
    ("Get health insurance", "احصل على تأمين صحي"),
    ("Annual extension / 90-day report", "التمديد السنوي / تقرير 90 يوماً"),

    ("Determine if you qualify for the Retirement O-A (50+, pension/savings proof), LTR Visa (remote worker, $80k income), or Thailand Elite. Most expats start with a Tourist Visa and switch after arrival.",
     "حدد ما إذا كنت مؤهلاً للتقاعد O-A (50+، إثبات المعاش/المدخرات)، تأشيرة LTR (عامل عن بُعد، دخل 80 ألف دولار)، أو تايلاند إيليت. يبدأ معظم المغتربين بتأشيرة سياحية ثم يتحولون بعد الوصول."),
    ("Passport (6+ months validity), passport photos, bank statements (800,000 THB in Thai bank for retirement visa or proof of $80k income for LTR), health insurance, medical certificate.",
     "جواز سفر (صالح 6+ أشهر)، صور جواز سفر، كشوف حساب بنكية (800,000 بات في بنك تايلاندي لتأشيرة التقاعد أو إثبات دخل 80 ألف دولار لـ LTR)، تأمين صحي، شهادة طبية."),
    ("Mandatory for retirement and LTR visas. Compare providers: Pacific Cross, BUPA Thailand, AXA. Budget ฿15,000–฿60,000/year depending on age and coverage.",
     "إلزامي لتأشيرات التقاعد وLTR. قارن مقدمي الخدمة: Pacific Cross، BUPA Thailand، AXA. ميزانية 15,000–60,000 بات/سنة حسب العمر والتغطية."),

    # ── COMMON ────────────────────────────────────────────────────────────────
    ("Visa & Residency Options", "خيارات التأشيرة والإقامة"),
    ("Pro Tips", "نصائح الخبراء"),
    ("Frequently Asked Questions", "الأسئلة الشائعة"),
    ("Last updated: March 2026", "آخر تحديث: مارس 2026"),
    ("March 2026", "مارس 2026"),
    ("Global eVisa & Travel Information Platform", "منصة معلومات التأشيرة الإلكترونية والسفر العالمية"),
    ("Follow eVisa-Card.com", "تابعوا eVisa-Card.com"),
    ("Visa Type", "نوع التأشيرة"),
    ("Duration", "المدة"),
    ("Requirements", "المتطلبات"),
    ("Best For", "الأنسب لـ"),
    ("Processing Time", "وقت المعالجة"),
    ("Fee", "الرسوم"),
    ("Mandatory", "إلزامي"),
    ("Recommended", "موصى به"),
    ("Optional", "اختياري"),
    ("per year", "سنوياً"),
    ("per month", "شهرياً"),
    ("per night", "لليلة الواحدة"),
]

def main():
    total = 0
    for fname in sorted(os.listdir(BASE)):
        if not fname.startswith("expat-guide-") or not fname.endswith(".html"):
            continue
        fpath = os.path.join(BASE, fname)
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        original = html
        for eng, ar in REPLACEMENTS:
            html = html.replace(eng, ar)
        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
            print(f"  OK {fname}")
    print(f"\nDone: {total} files updated.")

if __name__ == "__main__":
    main()
