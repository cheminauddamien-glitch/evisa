#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate English text in Thai (th) expat guide pages.
Processes all expat-guide-*.html files in www/th/
"""

import os
import glob

# Directory containing TH guide files
TH_DIR = os.path.join(os.path.dirname(__file__), "www", "th")

REPLACEMENTS = [
    # ── Title / meta ──────────────────────────────────────────────────────────
    ("How to Live in Thailand | eVisa-Card.com",
     "วิธีอยู่อาศัยในประเทศไทย | eVisa-Card.com"),
    ("How to Live in Portugal | eVisa-Card.com",
     "วิธีอยู่อาศัยในโปรตุเกส | eVisa-Card.com"),
    ("How to Live in Spain | eVisa-Card.com",
     "วิธีอยู่อาศัยในสเปน | eVisa-Card.com"),
    ("How to Live in Japan | eVisa-Card.com",
     "วิธีอยู่อาศัยในญี่ปุ่น | eVisa-Card.com"),
    ("How to Live in Vietnam | eVisa-Card.com",
     "วิธีอยู่อาศัยในเวียดนาม | eVisa-Card.com"),
    ("How to Live in Cambodia | eVisa-Card.com",
     "วิธีอยู่อาศัยในกัมพูชา | eVisa-Card.com"),
    ("How to Live in Malaysia | eVisa-Card.com",
     "วิธีอยู่อาศัยในมาเลเซีย | eVisa-Card.com"),
    ("How to Live in Georgia | eVisa-Card.com",
     "วิธีอยู่อาศัยในจอร์เจีย | eVisa-Card.com"),
    ("How to Live in Greece | eVisa-Card.com",
     "วิธีอยู่อาศัยในกรีซ | eVisa-Card.com"),
    ("How to Live in Mexico | eVisa-Card.com",
     "วิธีอยู่อาศัยในเม็กซิโก | eVisa-Card.com"),
    ("How to Live in Colombia | eVisa-Card.com",
     "วิธีอยู่อาศัยในโคลอมเบีย | eVisa-Card.com"),
    ("How to Live in Panama | eVisa-Card.com",
     "วิธีอยู่อาศัยในปานามา | eVisa-Card.com"),
    ("How to Live in Paraguay | eVisa-Card.com",
     "วิธีอยู่อาศัยในปารากวัย | eVisa-Card.com"),
    ("How to Live in Costa Rica | eVisa-Card.com",
     "วิธีอยู่อาศัยในคอสตาริกา | eVisa-Card.com"),
    ("How to Live in Laos | eVisa-Card.com",
     "วิธีอยู่อาศัยในลาว | eVisa-Card.com"),
    ("How to Live in Dubai & Abu Dhabi | eVisa-Card.com",
     "วิธีอยู่อาศัยในดูไบและอาบูดาบี | eVisa-Card.com"),

    # ── Page H1 titles ────────────────────────────────────────────────────────
    ("Expat Guide: Living in Thailand 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในประเทศไทย 2026"),
    ("Expat Guide: Living in Portugal 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในโปรตุเกส 2026"),
    ("Expat Guide: Living in Spain 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในสเปน 2026"),
    ("Expat Guide: Living in Japan 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในญี่ปุ่น 2026"),
    ("Expat Guide: Living in Vietnam 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในเวียดนาม 2026"),
    ("Expat Guide: Living in Cambodia 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในกัมพูชา 2026"),
    ("Expat Guide: Living in Malaysia 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในมาเลเซีย 2026"),
    ("Expat Guide: Living in Georgia 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในจอร์เจีย 2026"),
    ("Expat Guide: Living in Greece 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในกรีซ 2026"),
    ("Expat Guide: Living in Mexico 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในเม็กซิโก 2026"),
    ("Expat Guide: Living in Colombia 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในโคลอมเบีย 2026"),
    ("Expat Guide: Living in Panama 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในปานามา 2026"),
    ("Expat Guide: Living in Paraguay 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในปารากวัย 2026"),
    ("Expat Guide: Living in Costa Rica 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในคอสตาริกา 2026"),
    ("Expat Guide: Living in Laos 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในลาว 2026"),
    ("Expat Guide: Living in the UAE 2026",
     "คู่มือชาวต่างชาติ: การอยู่อาศัยในสหรัฐอาหรับเอมิเรตส์ 2026"),

    # ── Breadcrumb "Home" link ─────────────────────────────────────────────────
    ('>Home <i class="fa fa-chevron-right"></i></a>',
     '>หน้าหลัก <i class="fa fa-chevron-right"></i></a>'),

    # ── Breadcrumb expat guide label ───────────────────────────────────────────
    ('Expat Guide Thailand <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: ประเทศไทย <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Portugal <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: โปรตุเกส <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Spain <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: สเปน <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Japan <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: ญี่ปุ่น <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Vietnam <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: เวียดนาม <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Cambodia <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: กัมพูชา <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Malaysia <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: มาเลเซีย <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Georgia <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: จอร์เจีย <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Greece <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: กรีซ <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Mexico <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: เม็กซิโก <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Colombia <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: โคลอมเบีย <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Panama <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: ปานามา <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Paraguay <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: ปารากวัย <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Costa Rica <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: คอสตาริกา <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Laos <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: ลาว <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide UAE <i class="fa fa-chevron-right"></i>',
     'คู่มือชาวต่างชาติ: สหรัฐอาหรับเอมิเรตส์ <i class="fa fa-chevron-right"></i>'),

    # ── "at a Glance" section headings ────────────────────────────────────────
    ("Thailand at a Glance", "ภาพรวมประเทศไทย"),
    ("Portugal at a Glance", "ภาพรวมโปรตุเกส"),
    ("Spain at a Glance", "ภาพรวมสเปน"),
    ("Japan at a Glance", "ภาพรวมญี่ปุ่น"),
    ("Vietnam at a Glance", "ภาพรวมเวียดนาม"),
    ("Cambodia at a Glance", "ภาพรวมกัมพูชา"),
    ("Malaysia at a Glance", "ภาพรวมมาเลเซีย"),
    ("Georgia at a Glance", "ภาพรวมจอร์เจีย"),
    ("Greece at a Glance", "ภาพรวมกรีซ"),
    ("Mexico at a Glance", "ภาพรวมเม็กซิโก"),
    ("Colombia at a Glance", "ภาพรวมโคลอมเบีย"),
    ("Panama at a Glance", "ภาพรวมปานามา"),
    ("Paraguay at a Glance", "ภาพรวมปารากวัย"),
    ("Costa Rica at a Glance", "ภาพรวมคอสตาริกา"),
    ("Laos at a Glance", "ภาพรวมลาว"),
    ("UAE at a Glance", "ภาพรวมสหรัฐอาหรับเอมิเรตส์"),

    # ── Key fact labels ───────────────────────────────────────────────────────
    ("<strong>Capital</strong>", "<strong>เมืองหลวง</strong>"),
    ("<strong>Currency</strong>", "<strong>สกุลเงิน</strong>"),
    ("<strong>Language</strong>", "<strong>ภาษา</strong>"),
    ("<strong>Time Zone</strong>", "<strong>เขตเวลา</strong>"),
    ("<strong>Climate</strong>", "<strong>สภาพอากาศ</strong>"),

    # ── Last updated line ─────────────────────────────────────────────────────
    ("Last updated: March 2026", "อัปเดตล่าสุด: มีนาคม 2026"),
    ("Updated March 2026", "อัปเดต: มีนาคม 2026"),

    # ── Section headings ─────────────────────────────────────────────────────
    ("Visa &amp; Residency Options", "ตัวเลือกวีซ่าและการพำนัก"),
    ("Visa & Residency Options", "ตัวเลือกวีซ่าและการพำนัก"),

    # Step-by-Step with country names
    ("Step-by-Step: How to Move to Thailand",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: ประเทศไทย"),
    ("Step-by-Step: How to Move to Portugal",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: โปรตุเกส"),
    ("Step-by-Step: How to Move to Spain",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: สเปน"),
    ("Step-by-Step: How to Move to Japan",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: ญี่ปุ่น"),
    ("Step-by-Step: How to Move to Vietnam",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: เวียดนาม"),
    ("Step-by-Step: How to Move to Cambodia",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: กัมพูชา"),
    ("Step-by-Step: How to Move to Malaysia",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: มาเลเซีย"),
    ("Step-by-Step: How to Move to Georgia",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: จอร์เจีย"),
    ("Step-by-Step: How to Move to Greece",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: กรีซ"),
    ("Step-by-Step: How to Move to Mexico",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: เม็กซิโก"),
    ("Step-by-Step: How to Move to Colombia",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: โคลอมเบีย"),
    ("Step-by-Step: How to Move to Panama",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: ปานามา"),
    ("Step-by-Step: How to Move to Paraguay",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: ปารากวัย"),
    ("Step-by-Step: How to Move to Costa Rica",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: คอสตาริกา"),
    ("Step-by-Step: How to Move to Laos",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: ลาว"),
    ("Step-by-Step: How to Move to the UAE",
     "คู่มือย้ายถิ่นฐานทีละขั้นตอน: สหรัฐอาหรับเอมิเรตส์"),

    # Practical sections
    ("🏠 Housing", "🏠 ที่พักอาศัย"),
    ("🏦 Banking", "🏦 บริการธนาคาร"),
    ("🏥 Healthcare", "🏥 การดูแลสุขภาพ"),

    # Cost of Living — handle Thai partial translations too
    ("ค่าใช้จ่าย of Living", "ค่าครองชีพ"),
    ("💰 ค่าใช้จ่าย of Living", "💰 ค่าครองชีพ"),
    ("Cost of Living", "ค่าครองชีพ"),
    ("💰 Cost of Living", "💰 ค่าครองชีพ"),
    # Costs artifact ค่าใช้จ่ายs → ค่าใช้จ่าย
    ("ค่าใช้จ่ายs", "ค่าใช้จ่าย"),

    ("Frequently Asked Questions", "คำถามที่พบบ่อย"),

    # ── Tax section ───────────────────────────────────────────────────────────
    ("Tax &amp; Fiscal Exile", "ภาษีและการย้ายถิ่นฐานเพื่อภาษี"),
    ("Tax & Fiscal Exile", "ภาษีและการย้ายถิ่นฐานเพื่อภาษี"),
    ("Capital Gains Tax", "ภาษีกำไรจากการลงทุน"),
    ("Tax Regime", "ระบบภาษี"),
    ("Crypto-Friendliness", "ความเป็นมิตรต่อคริปโต"),
    ("Exit Tax", "ภาษีออกจากประเทศ"),
    ("Key Tax Points", "ประเด็นภาษีสำคัญ"),
    ("Simulate Your Tax Savings", "คำนวณการประหยัดภาษีของคุณ"),
    ("Use our free tax exile simulator to compare your tax savings",
     "ใช้เครื่องมือฟรีของเราเพื่อเปรียบเทียบการประหยัดภาษี"),
    ("Tax information provided for general guidance only. Consult a qualified tax advisor before making relocation decisions.",
     "ข้อมูลภาษีจัดทำขึ้นเพื่อการแนะนำทั่วไปเท่านั้น ควรปรึกษาที่ปรึกษาภาษีที่มีคุณสมบัติก่อนตัดสินใจย้ายถิ่นฐาน"),

    # ── Author box ────────────────────────────────────────────────────────────
    ("Editorial Team — eVisa-Card.com", "ทีมบรรณาธิการ — eVisa-Card.com"),
    (">Expat guides written by travel experts, immigration specialists and expats with first-hand experience in",
     ">คู่มือผู้อพยพเขียนโดยผู้เชี่ยวชาญด้านการเดินทาง ผู้เชี่ยวชาญด้านการย้ายถิ่นฐาน และผู้อพยพที่มีประสบการณ์จริงใน"),
    ("&#x2714; Verified information", "&#x2714; ข้อมูลที่ได้รับการตรวจสอบ"),
    ("&#x2714; Updated March 2026", "&#x2714; อัปเดตมีนาคม 2026"),
    ("&#x2714; Official sources cited", "&#x2714; อ้างอิงแหล่งข้อมูลทางการ"),

    # ── Official Sources section ───────────────────────────────────────────────
    ("&#128218; Official Sources &amp; References",
     "&#128218; แหล่งข้อมูลและเอกสารอ้างอิงทางการ"),

    # ── Pro Tips ─────────────────────────────────────────────────────────────
    ("Pro Tips", "เคล็ดลับจากผู้เชี่ยวชาญ"),

    # ── Table headers ─────────────────────────────────────────────────────────
    (">Visa Type<", ">ประเภทวีซ่า<"),
    (">Stay<", ">ระยะพำนัก<"),
    (">Requirements<", ">ข้อกำหนด<"),
    (">Best For<", ">เหมาะสำหรับ<"),
    (">Fee<", ">ค่าธรรมเนียม<"),
    (">Processing<", ">เวลาดำเนินการ<"),

    # Badge labels
    (">Mandatory<", ">บังคับ<"),
    (">Recommended<", ">แนะนำ<"),
    (">Optional<", ">ตัวเลือก<"),
    ("Mandatory</", "บังคับ</"),
    ("Recommended</", "แนะนำ</"),
    ("Optional</", "ตัวเลือก</"),

    # Per-period labels
    ("/year", " ต่อปี"),
    ("/month", " ต่อเดือน"),
    ("/night", " ต่อคืน"),
    ("per year", "ต่อปี"),
    ("per month", "ต่อเดือน"),
    ("per night", "ต่อคืน"),

    # Yes / No
    (">Yes<", ">ใช่<"),
    (">No<", ">ไม่ใช่<"),

    # ── Footer ────────────────────────────────────────────────────────────────
    ("Global eVisa &amp; Travel Information Platform",
     "แพลตฟอร์มข้อมูล eVisa และการท่องเที่ยวระดับโลก"),
    ("Global eVisa & Travel Information Platform",
     "แพลตฟอร์มข้อมูล eVisa และการท่องเที่ยวระดับโลก"),
    ("Follow eVisa-Card.com", "ติดตาม eVisa-Card.com"),
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
    files = sorted(glob.glob(os.path.join(TH_DIR, "expat-guide-*.html")))
    if not files:
        print(f"No expat-guide-*.html files found in {TH_DIR}")
        return

    print(f"Found {len(files)} expat guide files in {TH_DIR}\n")

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
