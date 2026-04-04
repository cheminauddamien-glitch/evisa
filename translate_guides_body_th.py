#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate remaining English body content in TH expat guide pages."""
import os

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\th"

REPLACEMENTS = [
    # ── PAGE TITLES ──────────────────────────────────────────────────────────
    ("Complete Expat Guide Cambodia 2026 — Live & Retire in Cambodia", "คู่มือชาวต่างชาติกัมพูชา 2026 — การอยู่อาศัยในกัมพูชา"),
    ("Expat Guide Colombia 2026 — Live & Work in Colombia | eVisa-Card.com", "คู่มือชาวต่างชาติโคลอมเบีย 2026 — การอยู่อาศัยในโคลอมเบีย | eVisa-Card.com"),
    ("Complete Expat Guide Georgia 2026 — Live & Work in Georgia (Caucasus)", "คู่มือชาวต่างชาติจอร์เจีย 2026 — การอยู่อาศัยในจอร์เจีย"),
    ("Complete Expat Guide Greece 2026 — Live & Retire in Greece", "คู่มือชาวต่างชาติกรีซ 2026 — การอยู่อาศัยในกรีซ"),
    ("Complete Expat Guide Laos 2026 — Live & Work in Laos", "คู่มือชาวต่างชาติลาว 2026 — การอยู่อาศัยในลาว"),
    ("Complete Expat Guide Panama 2026 — Live & Retire in Panama", "คู่มือชาวต่างชาติปานามา 2026 — การอยู่อาศัยในปานามา"),
    ("Complete Expat Guide Paraguay 2026 — Live & Retire in Paraguay", "คู่มือชาวต่างชาติปารากวัย 2026 — การอยู่อาศัยในปารากวัย"),
    ("Expat Guide UAE 2026 — How to Live in Dubai & Abu Dhabi | eVisa-Card.com", "คู่มือชาวต่างชาติสหรัฐอาหรับเอมิเรตส์ 2026 — การอยู่อาศัยในดูไบและอาบูดาบี | eVisa-Card.com"),
    ("Complete Expat Guide Costa Rica 2026 — Live & Retire in Costa Rica", "คู่มือชาวต่างชาติคอสตาริกา 2026 — การอยู่อาศัยในคอสตาริกา"),

    # ── VISA SECTION ─────────────────────────────────────────────────────────
    ("Thailand offers several long-stay options: the Tourist Visa (60 days, extendable), Non-Immigrant O-A Retirement Visa (1 year, renewable, for 50+), Thailand Elite Visa (5–20 years, premium), Long-Term Resident (LTR) Visa for professionals and digital nomads. There is no standard permanent residency path but long-term visa holders can renew indefinitely.",
     "ประเทศไทยมีตัวเลือกการพำนักระยะยาวหลายประเภท: วีซ่าท่องเที่ยว (60 วัน ต่ออายุได้), วีซ่าเกษียณ Non-Immigrant O-A (1 ปี ต่ออายุได้ สำหรับอายุ 50+), วีซ่าไทยเอลิท (5-20 ปี พรีเมียม), วีซ่าผู้พำนักระยะยาว (LTR) สำหรับผู้เชี่ยวชาญและดิจิทัลโนแมด ไม่มีเส้นทางการพำนักถาวรมาตรฐาน แต่ผู้ถือวีซ่าระยะยาวสามารถต่ออายุได้ไม่จำกัด"),

    # ── STEP-BY-STEP ─────────────────────────────────────────────────────────
    ("Choose your visa type", "เลือกประเภทวีซ่า"),
    ("Gather required documents", "รวบรวมเอกสารที่จำเป็น"),
    ("Apply at a Thai embassy or consulate", "ยื่นขอวีซ่าที่สถานทูตหรือสถานกงสุลไทย"),
    ("Arrive and register your address", "เดินทางมาและลงทะเบียนที่อยู่"),
    ("Open a Thai bank account", "เปิดบัญชีธนาคารไทย"),
    ("Get health insurance", "ซื้อประกันสุขภาพ"),
    ("Annual extension / 90-day report", "ต่ออายุรายปี / รายงาน 90 วัน"),

    ("Mandatory for retirement and LTR visas. Compare providers: Pacific Cross, BUPA Thailand, AXA. Budget ฿15,000–฿60,000/year depending on age and coverage.",
     "บังคับสำหรับวีซ่าเกษียณและ LTR เปรียบเทียบผู้ให้บริการ: Pacific Cross, BUPA Thailand, AXA งบประมาณ 15,000–60,000 บาท/ปี ขึ้นอยู่กับอายุและความคุ้มครอง"),
    ("Renew your visa annually at the local Immigration office. File 90-day reports in person, by post, or online via the Immigration Bureau website.",
     "ต่ออายุวีซ่าประจำปีที่สำนักงานตรวจคนเข้าเมืองในท้องถิ่น ยื่นรายงาน 90 วันด้วยตนเอง ทางไปรษณีย์ หรือออนไลน์ผ่านเว็บไซต์สำนักงานตรวจคนเข้าเมือง"),

    # ── COMMON ────────────────────────────────────────────────────────────────
    ("Visa & Residency Options", "ตัวเลือกวีซ่าและการพำนัก"),
    ("Pro Tips", "เคล็ดลับจากผู้เชี่ยวชาญ"),
    ("Frequently Asked Questions", "คำถามที่พบบ่อย"),
    ("Last updated: March 2026", "อัปเดตล่าสุด: มีนาคม 2026"),
    ("March 2026", "มีนาคม 2026"),
    ("Global eVisa & Travel Information Platform", "แพลตฟอร์มข้อมูล eVisa และการท่องเที่ยวระดับโลก"),
    ("Follow eVisa-Card.com", "ติดตาม eVisa-Card.com"),
    ("Visa Type", "ประเภทวีซ่า"),
    ("Duration", "ระยะเวลา"),
    ("Requirements", "ข้อกำหนด"),
    ("Best For", "เหมาะสำหรับ"),
    ("Processing Time", "เวลาดำเนินการ"),
    ("Fee", "ค่าธรรมเนียม"),
    ("Mandatory", "บังคับ"),
    ("Recommended", "แนะนำ"),
    ("Optional", "ตัวเลือก"),
    ("per year", "ต่อปี"),
    ("per month", "ต่อเดือน"),
    ("per night", "ต่อคืน"),
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
        for eng, th in REPLACEMENTS:
            html = html.replace(eng, th)
        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
            print(f"  OK {fname}")
    print(f"\nDone: {total} files updated.")

if __name__ == "__main__":
    main()
