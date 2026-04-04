#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate remaining English body content in KO expat guide pages."""
import os

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\ko"

REPLACEMENTS = [
    # ── PAGE TITLES ──────────────────────────────────────────────────────────
    ("Complete Expat Guide Cambodia 2026 — Live & Retire in Cambodia", "캄보디아 이민자 가이드 2026 — 캄보디아 생활"),
    ("Expat Guide Colombia 2026 — Live & Work in Colombia | eVisa-Card.com", "콜롬비아 이민자 가이드 2026 — 콜롬비아 생활 | eVisa-Card.com"),
    ("Complete Expat Guide Georgia 2026 — Live & Work in Georgia (Caucasus)", "조지아 이민자 가이드 2026 — 조지아 생활"),
    ("Complete Expat Guide Greece 2026 — Live & Retire in Greece", "그리스 이민자 가이드 2026 — 그리스 생활"),
    ("Complete Expat Guide Laos 2026 — Live & Work in Laos", "라오스 이민자 가이드 2026 — 라오스 생활"),
    ("Complete Expat Guide Panama 2026 — Live & Retire in Panama", "파나마 이민자 가이드 2026 — 파나마 생활"),
    ("Complete Expat Guide Paraguay 2026 — Live & Retire in Paraguay", "파라과이 이민자 가이드 2026 — 파라과이 생활"),
    ("Expat Guide UAE 2026 — How to Live in Dubai & Abu Dhabi | eVisa-Card.com", "UAE 이민자 가이드 2026 — 두바이·아부다비 생활 | eVisa-Card.com"),
    ("Complete Expat Guide Costa Rica 2026 — Live & Retire in Costa Rica", "코스타리카 이민자 가이드 2026 — 코스타리카 생활"),

    # ── VISA SECTION PARAGRAPH ────────────────────────────────────────────────
    ("Thailand offers several long-stay options: the Tourist Visa (60 days, extendable), Non-Immigrant O-A Retirement Visa (1 year, renewable, for 50+), Thailand Elite Visa (5–20 years, premium), Long-Term Resident (LTR) Visa for professionals and digital nomads. There is no standard permanent residency path but long-term visa holders can renew indefinitely.",
     "태국에는 여러 장기 체류 옵션이 있습니다: 관광 비자(60일, 연장 가능), 비이민 O-A 은퇴 비자(1년, 갱신 가능, 50세 이상), 태국 엘리트 비자(5~20년, 프리미엄), 전문가 및 디지털 노마드를 위한 장기 거주자(LTR) 비자. 표준적인 영주권 경로는 없지만 장기 비자 소지자는 무기한 갱신할 수 있습니다."),

    # ── STEP-BY-STEP TITLES ──────────────────────────────────────────────────
    ("Choose your visa type", "비자 유형 선택"),
    ("Gather required documents", "필요 서류 준비"),
    ("Apply at a Thai embassy or consulate", "태국 대사관 또는 영사관에서 신청"),
    ("Arrive and register your address", "입국 및 주소 등록"),
    ("Open a Thai bank account", "태국 은행 계좌 개설"),
    ("Get health insurance", "건강 보험 가입"),
    ("Annual extension / 90-day report", "연간 갱신 / 90일 보고"),

    # ── STEP-BY-STEP CONTENT ─────────────────────────────────────────────────
    ("Determine if you qualify for the Retirement O-A (50+, pension/savings proof), LTR Visa (remote worker, $80k income), or Thailand Elite. Most expats start with a Tourist Visa and switch after arrival.",
     "은퇴 O-A(50세 이상, 연금/저축 증명), LTR 비자(원격 근무자, 연 소득 8만 달러), 또는 태국 엘리트 자격 여부를 확인하세요. 대부분의 이민자는 관광 비자로 시작하여 입국 후 전환합니다."),
    ("Passport (6+ months validity), passport photos, bank statements (800,000 THB in Thai bank for retirement visa or proof of $80k income for LTR), health insurance, medical certificate.",
     "여권(유효기간 6개월 이상), 여권 사진, 은행 명세서(은퇴 비자의 경우 태국 은행에 80만 바트, 또는 LTR의 경우 연 소득 8만 달러 증명), 건강 보험, 의료 진단서."),
    ("Submit your visa application at your nearest Thai embassy. Processing takes 3–5 business days. You can also enter on a tourist visa and extend at the Immigration Bureau in Thailand.",
     "가까운 태국 대사관에서 비자 신청서를 제출하세요. 처리에는 3~5 영업일이 소요됩니다. 관광 비자로 입국하여 태국의 이민국에서 연장할 수도 있습니다."),
    ("Within 24 hours of arriving, notify your accommodation. If renting, your landlord must file a TM.30 report. You receive a TM.6 arrival card.",
     "도착 후 24시간 이내에 숙소에 통보하세요. 임대 시 집주인은 TM.30 보고서를 제출해야 합니다. TM.6 입국 카드를 받습니다."),
    ("Open a Kasikorn Bank (KBank) or Bangkok Bank account. You'll need your passport, Non-Immigrant visa, and proof of address. Required for the 800,000 THB retirement deposit.",
     "카시콘 은행(KBank) 또는 방콕 은행 계좌를 개설하세요. 여권, 비이민 비자, 주소 증명이 필요합니다. 80만 바트 은퇴 예금에 필요합니다."),
    ("Mandatory for retirement and LTR visas. Compare providers: Pacific Cross, BUPA Thailand, AXA. Budget ฿15,000–฿60,000/year depending on age and coverage.",
     "은퇴 비자와 LTR 비자에는 필수입니다. 제공업체를 비교하세요: Pacific Cross, BUPA Thailand, AXA. 나이와 보장 범위에 따라 연간 15,000~60,000바트의 예산이 필요합니다."),
    ("Renew your visa annually at the local Immigration office. File 90-day reports in person, by post, or online via the Immigration Bureau website.",
     "지역 이민국에서 매년 비자를 갱신하세요. 90일 보고서는 직접, 우편, 또는 이민국 웹사이트를 통해 온라인으로 제출할 수 있습니다."),

    # ── COMMON SECTIONS ───────────────────────────────────────────────────────
    ("Visa & Residency Options", "비자 및 거주 옵션"),
    ("Healthcare in Thailand", "태국의 의료"),
    ("Healthcare in Japan", "일본의 의료"),
    ("Healthcare in Vietnam", "베트남의 의료"),
    ("Banking in Thailand", "태국의 은행"),
    ("Cost of Living in Thailand", "태국의 생활비"),
    ("Real Estate in Thailand", "태국의 부동산"),
    ("Pro Tips", "전문가 팁"),
    ("Frequently Asked Questions", "자주 묻는 질문"),
    ("Last updated: March 2026", "최종 업데이트: 2026년 3월"),
    ("March 2026", "2026년 3월"),
    ("Global eVisa & Travel Information Platform", "글로벌 전자비자 및 여행 정보 플랫폼"),
    ("Follow eVisa-Card.com", "eVisa-Card.com 팔로우"),
    ("Visa Type", "비자 유형"),
    ("Duration", "기간"),
    ("Requirements", "요건"),
    ("Best For", "최적 대상"),
    ("Processing Time", "처리 시간"),
    ("Fee", "수수료"),
    ("Mandatory", "필수"),
    ("Recommended", "권장"),
    ("Optional", "선택"),
    ("per year", "연간"),
    ("per month", "월간"),
    ("per night", "1박"),
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
        for eng, ko in REPLACEMENTS:
            html = html.replace(eng, ko)
        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
            print(f"  OK {fname}")
    print(f"\nDone: {total} files updated.")

if __name__ == "__main__":
    main()
