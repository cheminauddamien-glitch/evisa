#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
translate_guides_ko.py
Translates remaining English text in KO (Korean) expat guide HTML files.
"""

import os

KO_DIR = os.path.join(os.path.dirname(__file__), "www", "ko")

# ---------------------------------------------------------------------------
# Ordered replacement table  (longest / most specific first where needed)
# Each entry: (exact_string_to_find, replacement)
# We use plain str.replace so the order matters for overlapping patterns.
# ---------------------------------------------------------------------------

REPLACEMENTS = [
    # -----------------------------------------------------------------------
    # Title tag translations
    # -----------------------------------------------------------------------
    ("Expat Guide Thailand 2026 — How to Live in Thailand | eVisa-Card.com",
     "태국 이민자 가이드 2026 — 태국에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Vietnam 2026 — How to Live in Vietnam | eVisa-Card.com",
     "베트남 이민자 가이드 2026 — 베트남에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Portugal 2026 — How to Live in Portugal | eVisa-Card.com",
     "포르투갈 이민자 가이드 2026 — 포르투갈에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Spain 2026 — How to Live in Spain | eVisa-Card.com",
     "스페인 이민자 가이드 2026 — 스페인에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Japan 2026 — How to Live in Japan | eVisa-Card.com",
     "일본 이민자 가이드 2026 — 일본에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Malaysia 2026 — How to Live in Malaysia | eVisa-Card.com",
     "말레이시아 이민자 가이드 2026 — 말레이시아에서의 생활 | eVisa-Card.com"),
    ("Expat Guide UAE 2026 — How to Live in Dubai & Abu Dhabi | eVisa-Card.com",
     "UAE 이민자 가이드 2026 — 두바이 & 아부다비에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Mexico 2026 — How to Live in Mexico | eVisa-Card.com",
     "멕시코 이민자 가이드 2026 — 멕시코에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Colombia 2026 — How to Live in Colombia | eVisa-Card.com",
     "콜롬비아 이민자 가이드 2026 — 콜롬비아에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Colombia 2026 — Live & Work in Colombia | eVisa-Card.com",
     "콜롬비아 이민자 가이드 2026 — 콜롬비아에서 생활 및 근무 | eVisa-Card.com"),
    ("Expat Guide Costa Rica 2026 — How to Live in Costa Rica | eVisa-Card.com",
     "코스타리카 이민자 가이드 2026 — 코스타리카에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Panama 2026 — How to Live in Panama | eVisa-Card.com",
     "파나마 이민자 가이드 2026 — 파나마에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Paraguay 2026 — How to Live in Paraguay | eVisa-Card.com",
     "파라과이 이민자 가이드 2026 — 파라과이에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Greece 2026 — How to Live in Greece | eVisa-Card.com",
     "그리스 이민자 가이드 2026 — 그리스에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Georgia 2026 — How to Live in Georgia | eVisa-Card.com",
     "조지아 이민자 가이드 2026 — 조지아에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Cambodia 2026 — How to Live in Cambodia | eVisa-Card.com",
     "캄보디아 이민자 가이드 2026 — 캄보디아에서의 생활 | eVisa-Card.com"),
    ("Expat Guide Laos 2026 — How to Live in Laos | eVisa-Card.com",
     "라오스 이민자 가이드 2026 — 라오스에서의 생활 | eVisa-Card.com"),

    # -----------------------------------------------------------------------
    # Hero breadcrumbs
    # -----------------------------------------------------------------------
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Thailand <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>태국 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Vietnam <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>베트남 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Portugal <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>포르투갈 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Spain <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>스페인 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Japan <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>일본 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Malaysia <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>말레이시아 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide UAE <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>UAE 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Mexico <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>멕시코 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Colombia <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>콜롬비아 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Costa Rica <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>코스타리카 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Panama <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>파나마 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Paraguay <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>파라과이 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Greece <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>그리스 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Georgia <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>조지아 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Cambodia <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>캄보디아 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Laos <i class=\"fa fa-chevron-right\"></i></span>",
     ">홈 <i class=\"fa fa-chevron-right\"></i></a></span> <span>라오스 이민자 가이드 <i class=\"fa fa-chevron-right\"></i></span>"),

    # -----------------------------------------------------------------------
    # H1 page headings (without year — Colombia has different format)
    # -----------------------------------------------------------------------
    ("Expat Guide: Living in Colombia",
     "이민자 가이드: 콜롬비아 생활"),

    # Step-by-Step with "Moving" variant
    ("Step-by-Step: Moving to Colombia",
     "콜롬비아 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Cambodia",
     "캄보디아 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Laos",
     "라오스 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Georgia",
     "조지아 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Greece",
     "그리스 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Panama",
     "파나마 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Paraguay",
     "파라과이 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Costa Rica",
     "코스타리카 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Malaysia",
     "말레이시아 이주 단계별 가이드"),
    ("Step-by-Step: Moving to Mexico",
     "멕시코 이주 단계별 가이드"),

    # -----------------------------------------------------------------------
    # H1 page headings
    # -----------------------------------------------------------------------
    ("Expat Guide: Living in Thailand 2026",
     "이민자 가이드: 2026년 태국 생활"),
    ("Expat Guide: Living in Vietnam 2026",
     "이민자 가이드: 2026년 베트남 생활"),
    ("Expat Guide: Living in Portugal 2026",
     "이민자 가이드: 2026년 포르투갈 생활"),
    ("Expat Guide: Living in Spain 2026",
     "이민자 가이드: 2026년 스페인 생활"),
    ("Expat Guide: Living in Japan 2026",
     "이민자 가이드: 2026년 일본 생활"),
    ("Expat Guide: Living in Malaysia 2026",
     "이민자 가이드: 2026년 말레이시아 생활"),
    ("Expat Guide: Living in the UAE 2026",
     "이민자 가이드: 2026년 UAE 생활"),
    ("Expat Guide: Living in Mexico 2026",
     "이민자 가이드: 2026년 멕시코 생활"),
    ("Expat Guide: Living in Colombia 2026",
     "이민자 가이드: 2026년 콜롬비아 생활"),
    ("Expat Guide: Living in Costa Rica 2026",
     "이민자 가이드: 2026년 코스타리카 생활"),
    ("Expat Guide: Living in Panama 2026",
     "이민자 가이드: 2026년 파나마 생활"),
    ("Expat Guide: Living in Paraguay 2026",
     "이민자 가이드: 2026년 파라과이 생활"),
    ("Expat Guide: Living in Greece 2026",
     "이민자 가이드: 2026년 그리스 생활"),
    ("Expat Guide: Living in Georgia 2026",
     "이민자 가이드: 2026년 조지아 생활"),
    ("Expat Guide: Living in Cambodia 2026",
     "이민자 가이드: 2026년 캄보디아 생활"),
    ("Expat Guide: Living in Laos 2026",
     "이민자 가이드: 2026년 라오스 생활"),

    # -----------------------------------------------------------------------
    # "at a Glance" country boxes
    # -----------------------------------------------------------------------
    ("Thailand at a Glance", "태국 개요"),
    ("Vietnam at a Glance", "베트남 개요"),
    ("Portugal at a Glance", "포르투갈 개요"),
    ("Spain at a Glance", "스페인 개요"),
    ("Japan at a Glance", "일본 개요"),
    ("Malaysia at a Glance", "말레이시아 개요"),
    ("UAE at a Glance", "UAE 개요"),
    ("Mexico at a Glance", "멕시코 개요"),
    ("Colombia at a Glance", "콜롬비아 개요"),
    ("Costa Rica at a Glance", "코스타리카 개요"),
    ("Panama at a Glance", "파나마 개요"),
    ("Paraguay at a Glance", "파라과이 개요"),
    ("Greece at a Glance", "그리스 개요"),
    ("Georgia at a Glance", "조지아 개요"),
    ("Cambodia at a Glance", "캄보디아 개요"),
    ("Laos at a Glance", "라오스 개요"),

    # -----------------------------------------------------------------------
    # Key Facts labels
    # -----------------------------------------------------------------------
    ("<strong>Capital</strong>", "<strong>수도</strong>"),
    ("<strong>Currency</strong>", "<strong>통화</strong>"),
    ("<strong>Language</strong>", "<strong>언어</strong>"),
    ("<strong>Time Zone</strong>", "<strong>시간대</strong>"),
    ("<strong>Climate</strong>", "<strong>기후</strong>"),
    ("<strong>Schengen Area</strong>", "<strong>솅겐 지역</strong>"),
    ("<strong>Schengen</strong>", "<strong>솅겐</strong>"),
    ("<strong>Income Tax</strong>", "<strong>소득세</strong>"),
    ("<strong>비용 of Living</strong>", "<strong>생활비</strong>"),
    ("<strong>Cost of Living</strong>", "<strong>생활비</strong>"),

    # -----------------------------------------------------------------------
    # Section headings
    # -----------------------------------------------------------------------
    (">Visa &amp; Residency Options<", ">비자 및 거주 옵션<"),
    (">Visa & Residency Options<", ">비자 및 거주 옵션<"),

    # Step-by-step headings
    ("Step-by-Step: How to Move to Thailand",
     "태국 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Vietnam",
     "베트남 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Portugal",
     "포르투갈 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Spain",
     "스페인 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Japan",
     "일본 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Malaysia",
     "말레이시아 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to the UAE",
     "UAE 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Mexico",
     "멕시코 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Colombia",
     "콜롬비아 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Costa Rica",
     "코스타리카 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Panama",
     "파나마 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Paraguay",
     "파라과이 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Greece",
     "그리스 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Georgia",
     "조지아 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Cambodia",
     "캄보디아 이주 단계별 가이드"),
    ("Step-by-Step: How to Move to Laos",
     "라오스 이주 단계별 가이드"),

    # FAQ heading
    (">Frequently Asked Questions<",
     ">자주 묻는 질문<"),

    # Tax section heading (appears with whitespace in h2)
    ("&#128176; Tax &amp; Fiscal Exile",
     "&#128176; 세금 및 재정 망명"),
    ("&#128176; Tax & Fiscal Exile",
     "&#128176; 세금 및 재정 망명"),

    # -----------------------------------------------------------------------
    # Practical info card headings
    # -----------------------------------------------------------------------
    (">🏠 Housing<", ">🏠 주거<"),
    (">🏦 Banking<", ">🏦 은행 서비스<"),
    (">🏥 Healthcare<", ">🏥 의료<"),
    (">💰 비용 of Living<", ">💰 생활비<"),
    (">💰 Cost of Living<", ">💰 생활비<"),

    # -----------------------------------------------------------------------
    # Tax card labels
    # -----------------------------------------------------------------------
    (">Capital Gains Tax<", ">자본이득세<"),
    (">Tax Regime<", ">세제<"),
    (">Crypto-Friendliness<", ">암호화폐 친화도<"),
    (">Exit Tax<", ">출국세<"),

    # -----------------------------------------------------------------------
    # Tax section body text
    # -----------------------------------------------------------------------
    ("<strong>Capital Gains Tax:</strong>", "<strong>자본이득세:</strong>"),
    (">Key Tax Points<", ">주요 세금 포인트<"),
    (">Simulate Your Tax Savings<", ">세금 절약 시뮬레이션<"),
    ("&#128640; Simulate Your Tax Savings &rarr;",
     "&#128640; 세금 절약 시뮬레이션 &rarr;"),

    # Tax CTA country-specific text
    ("Use our free tax exile simulator to compare your tax savings in Thailand.",
     "무료 재정 망명 시뮬레이터를 사용하여 태국에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Vietnam.",
     "무료 재정 망명 시뮬레이터를 사용하여 베트남에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Portugal.",
     "무료 재정 망명 시뮬레이터를 사용하여 포르투갈에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Spain.",
     "무료 재정 망명 시뮬레이터를 사용하여 스페인에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Japan.",
     "무료 재정 망명 시뮬레이터를 사용하여 일본에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Malaysia.",
     "무료 재정 망명 시뮬레이터를 사용하여 말레이시아에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in UAE.",
     "무료 재정 망명 시뮬레이터를 사용하여 UAE에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Mexico.",
     "무료 재정 망명 시뮬레이터를 사용하여 멕시코에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Colombia.",
     "무료 재정 망명 시뮬레이터를 사용하여 콜롬비아에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Costa Rica.",
     "무료 재정 망명 시뮬레이터를 사용하여 코스타리카에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Panama.",
     "무료 재정 망명 시뮬레이터를 사용하여 파나마에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Paraguay.",
     "무료 재정 망명 시뮬레이터를 사용하여 파라과이에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Greece.",
     "무료 재정 망명 시뮬레이터를 사용하여 그리스에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Georgia.",
     "무료 재정 망명 시뮬레이터를 사용하여 조지아에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Cambodia.",
     "무료 재정 망명 시뮬레이터를 사용하여 캄보디아에서의 세금 절약액을 비교하세요."),
    ("Use our free tax exile simulator to compare your tax savings in Laos.",
     "무료 재정 망명 시뮬레이터를 사용하여 라오스에서의 세금 절약액을 비교하세요."),
    ("Compare tax rates across 27+ countries with our interactive simulator",
     "인터랙티브 시뮬레이터로 27개국 이상의 세율을 비교하세요"),

    # Tax disclaimer
    ("<em>Tax information provided for general guidance only. Consult a qualified tax advisor before making relocation decisions.</em>",
     "<em>세금 정보는 일반적인 참고 목적으로만 제공됩니다. 이주 결정 전 자격을 갖춘 세무 전문가와 상담하세요.</em>"),

    # -----------------------------------------------------------------------
    # Official Sources section
    # -----------------------------------------------------------------------
    (">&#128218; Official Sources &amp; References<",
     ">&#128218; 공식 자료 및 참고문헌<"),
    (">&#128218; Official Sources & References<",
     ">&#128218; 공식 자료 및 참고문헌<"),

    # -----------------------------------------------------------------------
    # Author box
    # -----------------------------------------------------------------------
    (">Editorial Team — eVisa-Card.com<",
     ">편집팀 — eVisa-Card.com<"),

    # Country-specific author box descriptions
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Thailand.",
     "태국에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Vietnam.",
     "베트남에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Portugal.",
     "포르투갈에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Spain.",
     "스페인에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Japan.",
     "일본에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Malaysia.",
     "말레이시아에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in the UAE.",
     "UAE에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Mexico.",
     "멕시코에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Colombia.",
     "콜롬비아에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Costa Rica.",
     "코스타리카에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Panama.",
     "파나마에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Paraguay.",
     "파라과이에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Greece.",
     "그리스에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Georgia.",
     "조지아에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Cambodia.",
     "캄보디아에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Laos.",
     "라오스에서 직접 생활한 여행 전문가, 이민 전문가, 현지 경험자들이 작성한 이민자 가이드입니다."),

    # Verified info footer in author box
    ("&#x2714; Verified information", "&#x2714; 검증된 정보"),
    ("&#x2714; Updated March 2026", "&#x2714; 2026년 3월 업데이트"),
    ("&#x2714; Official sources cited", "&#x2714; 공식 자료 인용"),

    # -----------------------------------------------------------------------
    # "Last updated" line
    # -----------------------------------------------------------------------
    ("Last updated: March 2026 — <em>편집팀, eVisa-Card.com</em>",
     "최종 업데이트: 2026년 3월 — <em>편집팀, eVisa-Card.com</em>"),
    ("Last updated: March 2026 — 편집팀, eVisa-Card.com",
     "최종 업데이트: 2026년 3월 — 편집팀, eVisa-Card.com"),

    # -----------------------------------------------------------------------
    # Yes / No in tax cards
    # -----------------------------------------------------------------------
    (">Yes (> 100M JPY in assets)<", ">예 (1억엔 초과 자산)<"),
    (">Yes (> 4 years residency, > 4M assets)<", ">예 (4년 초과 거주, 자산 400만 유로 초과)<"),
    (";color:#28a745;\">No<", ";color:#28a745;\">아니오<"),
    (";color:#dc3545;\">Yes<", ";color:#dc3545;\">예<"),

    # -----------------------------------------------------------------------
    # Country intro paragraphs
    # -----------------------------------------------------------------------
    ("Thailand is one of the world's top expat destinations, attracting retirees, digital nomads and families with its warm climate, affordable cost of living, world-class cuisine and welcoming culture. This guide walks you through everything you need to know to relocate to Thailand in 2026.",
     "태국은 따뜻한 기후, 저렴한 생활비, 세계적인 요리, 친근한 문화로 은퇴자, 디지털 노마드, 가족들을 끌어들이는 세계 최고의 이민자 목적지 중 하나입니다. 이 가이드는 2026년 태국으로 이주하기 위해 알아야 할 모든 것을 안내합니다."),

    ("Vietnam has emerged as one of Southeast Asia's top expat and digital nomad destinations, with ultra-low cost of living, vibrant cities, and stunning landscapes. Hanoi, Ho Chi Minh City, Da Nang and Hoi An offer exceptional quality of life at a fraction of Western costs.",
     "베트남은 매우 낮은 생활비, 활기찬 도시, 아름다운 경관으로 동남아시아 최고의 이민자 및 디지털 노마드 목적지로 부상했습니다. 하노이, 호치민시, 다낭, 호이안은 서구 비용의 일부로 탁월한 삶의 질을 제공합니다."),

    ("Portugal has become one of Europe's most sought-after expat destinations, offering a D7 Passive Income Visa, Golden Visa, affordable cost of living compared to Western Europe, mild climate, safety, and the NHR tax regime for significant tax savings. This guide covers everything you need to relocate to Portugal.",
     "포르투갈은 D7 소득 비자, 골든 비자, 서유럽 대비 저렴한 생활비, 온화한 기후, 안전성, 그리고 상당한 절세가 가능한 NHR 세제를 제공하며 유럽에서 가장 인기 있는 이민자 목적지 중 하나가 되었습니다. 이 가이드는 포르투갈로 이주하는 데 필요한 모든 것을 다룹니다."),

    ("Spain remains one of the world's top expat destinations thanks to its Mediterranean climate, vibrant culture, excellent healthcare, high quality of life and relatively affordable cost of living outside major cities. Whether you're retiring, working remotely or starting a business, Spain has a path for you.",
     "스페인은 지중해성 기후, 활기찬 문화, 우수한 의료 시스템, 높은 삶의 질, 주요 도시 외부의 비교적 저렴한 생활비 덕분에 세계 최고의 이민자 목적지로 남아 있습니다. 은퇴, 원격 근무, 사업 시작 등 어떤 목적이든 스페인에 맞는 비자가 있습니다."),

    ("Japan offers a unique expat experience: ultra-safe, technologically advanced, culturally rich and with excellent public services. Tokyo, Osaka, Kyoto and Fukuoka attract expats with high quality of life, world-class healthcare and efficient public transport. Japan introduced a digital nomad visa in 2024.",
     "일본은 초안전하고 기술적으로 발전했으며 문화적으로 풍부하고 우수한 공공 서비스를 갖춘 독특한 이민 경험을 제공합니다. 도쿄, 오사카, 교토, 후쿠오카는 높은 삶의 질, 세계적 수준의 의료 시스템, 효율적인 대중교통으로 이민자를 끌어들입니다. 일본은 2024년 디지털 노마드 비자를 도입했습니다."),

    ("The United Arab Emirates offers one of the world's most attractive expat packages: zero income tax, world-class infrastructure, multicultural society and a strategic location between East and West. Dubai and Abu Dhabi attract professionals, entrepreneurs and retirees with multiple residency pathways introduced in recent years.",
     "아랍에미리트는 소득세 제로, 세계적 수준의 인프라, 다문화 사회, 동서를 연결하는 전략적 위치로 세계에서 가장 매력적인 이민 패키지를 제공합니다. 두바이와 아부다비는 최근 도입된 다양한 거주 경로로 전문직, 기업가, 은퇴자를 끌어들입니다."),

    # -----------------------------------------------------------------------
    # Full Visa Requirements links
    # -----------------------------------------------------------------------
    ("→ Full Thailand Visa Requirements &amp; Application Guide",
     "→ 태국 비자 요건 및 신청 가이드 (전체)"),
    ("→ Full Thailand Visa Requirements & Application Guide",
     "→ 태국 비자 요건 및 신청 가이드 (전체)"),
    ("→ Full Vietnam Visa Requirements Guide",
     "→ 베트남 비자 요건 가이드 (전체)"),
    ("→ Full Portugal Visa Requirements &amp; Application Guide",
     "→ 포르투갈 비자 요건 및 신청 가이드 (전체)"),
    ("→ Full Portugal Visa Requirements & Application Guide",
     "→ 포르투갈 비자 요건 및 신청 가이드 (전체)"),
    ("→ Full Spain Visa Requirements Guide",
     "→ 스페인 비자 요건 가이드 (전체)"),
    ("→ Full Japan Visa Requirements Guide",
     "→ 일본 비자 요건 가이드 (전체)"),
    ("→ Full Malaysia Visa Requirements Guide",
     "→ 말레이시아 비자 요건 가이드 (전체)"),
    ("→ Full UAE Visa Requirements Guide",
     "→ UAE 비자 요건 가이드 (전체)"),
    ("→ Full Mexico Visa Requirements Guide",
     "→ 멕시코 비자 요건 가이드 (전체)"),
    ("→ Full Colombia Visa Requirements Guide",
     "→ 콜롬비아 비자 요건 가이드 (전체)"),
    ("→ Full Costa Rica Visa Requirements Guide",
     "→ 코스타리카 비자 요건 가이드 (전체)"),
    ("→ Full Panama Visa Requirements Guide",
     "→ 파나마 비자 요건 가이드 (전체)"),
    ("→ Full Paraguay Visa Requirements Guide",
     "→ 파라과이 비자 요건 가이드 (전체)"),
    ("→ Full Greece Visa Requirements Guide",
     "→ 그리스 비자 요건 가이드 (전체)"),
    ("→ Full Georgia Visa Requirements Guide",
     "→ 조지아 비자 요건 가이드 (전체)"),
    ("→ Full Cambodia Visa Requirements Guide",
     "→ 캄보디아 비자 요건 가이드 (전체)"),
    ("→ Full Laos Visa Requirements Guide",
     "→ 라오스 비자 요건 가이드 (전체)"),

    # -----------------------------------------------------------------------
    # Powered by line
    # -----------------------------------------------------------------------
    ("Powered by", "제공:"),

    # -----------------------------------------------------------------------
    # Table of Contents link text (detailed-format pages)
    # -----------------------------------------------------------------------
    (">Visa &amp; Residency<", ">비자 및 거주<"),
    (">Visa & Residency<", ">비자 및 거주<"),
    (">Healthcare<", ">의료<"),
    (">Health Insurance<", ">건강 보험<"),
    (">Bank Account<", ">은행 계좌<"),
    (">Buying Property<", ">부동산 구매<"),
    (">Tax &amp; Fiscal Exile<", ">세금 및 재정 망명<"),
    (">Tax & Fiscal Exile<", ">세금 및 재정 망명<"),
    (">Cost of Living<", ">생활비<"),

    # -----------------------------------------------------------------------
    # Section headings with emoji prefix (detailed-format pages)
    # -----------------------------------------------------------------------
    ("🛂 Visa & Residency Options", "🛂 비자 및 거주 옵션"),
    ("🛂 Visa &amp; Residency Options", "🛂 비자 및 거주 옵션"),
    ("🏥 Healthcare in Cambodia", "🏥 캄보디아의 의료"),
    ("🏥 Healthcare in Laos", "🏥 라오스의 의료"),
    ("🏥 Healthcare in Georgia", "🏥 조지아의 의료"),
    ("🏥 Healthcare in Greece", "🏥 그리스의 의료"),
    ("🏥 Healthcare in Panama", "🏥 파나마의 의료"),
    ("🏥 Healthcare in Paraguay", "🏥 파라과이의 의료"),
    ("🏥 Healthcare in Colombia", "🏥 콜롬비아의 의료"),
    ("🏥 Healthcare in Costa Rica", "🏥 코스타리카의 의료"),
    ("🏥 Healthcare in Mexico", "🏥 멕시코의 의료"),
    ("🏥 Healthcare in Malaysia", "🏥 말레이시아의 의료"),
    ("🏥 Healthcare in UAE", "🏥 UAE의 의료"),
    ("🛡️ Health Insurance in Cambodia", "🛡️ 캄보디아의 건강 보험"),
    ("🛡️ Health Insurance in Laos", "🛡️ 라오스의 건강 보험"),
    ("🛡️ Health Insurance in Georgia", "🛡️ 조지아의 건강 보험"),
    ("🛡️ Health Insurance in Greece", "🛡️ 그리스의 건강 보험"),
    ("🛡️ Health Insurance in Panama", "🛡️ 파나마의 건강 보험"),
    ("🛡️ Health Insurance in Paraguay", "🛡️ 파라과이의 건강 보험"),
    ("🛡️ Health Insurance in Colombia", "🛡️ 콜롬비아의 건강 보험"),
    ("🛡️ Health Insurance in Costa Rica", "🛡️ 코스타리카의 건강 보험"),
    ("🏦 Opening a Bank Account in Cambodia", "🏦 캄보디아 은행 계좌 개설"),
    ("🏦 Opening a Bank Account in Laos", "🏦 라오스 은행 계좌 개설"),
    ("🏦 Opening a Bank Account in Georgia", "🏦 조지아 은행 계좌 개설"),
    ("🏦 Opening a Bank Account in Greece", "🏦 그리스 은행 계좌 개설"),
    ("🏦 Opening a Bank Account in Panama", "🏦 파나마 은행 계좌 개설"),
    ("🏦 Opening a Bank Account in Paraguay", "🏦 파라과이 은행 계좌 개설"),
    ("🏦 Opening a Bank Account in Colombia", "🏦 콜롬비아 은행 계좌 개설"),
    ("🏦 Opening a Bank Account in Costa Rica", "🏦 코스타리카 은행 계좌 개설"),
    ("🏠 Buying Property in Cambodia", "🏠 캄보디아 부동산 구매"),
    ("🏠 Buying Property in Laos", "🏠 라오스 부동산 구매"),
    ("🏠 Buying Property in Georgia", "🏠 조지아 부동산 구매"),
    ("🏠 Buying Property in Greece", "🏠 그리스 부동산 구매"),
    ("🏠 Buying Property in Panama", "🏠 파나마 부동산 구매"),
    ("🏠 Buying Property in Paraguay", "🏠 파라과이 부동산 구매"),
    ("🏠 Buying Property in Colombia", "🏠 콜롬비아 부동산 구매"),
    ("🏠 Buying Property in Costa Rica", "🏠 코스타리카 부동산 구매"),
    ("📋 Table of Contents", "📋 목차"),

    # Step-by-Step Process as h3 (detailed pages)
    (">Step-by-Step Process<", ">단계별 절차<"),

    # at-a-glance table labels (td format, not strong tag)
    ("\">Capital<", "\">수도<"),
    ("\">Currency<", "\">통화<"),
    ("\">Language<", "\">언어<"),
    ("\">Time Zone<", "\">시간대<"),
    ("\">Climate<", "\">기후<"),
    ("\">Monthly cost<", "\">월 생활비<"),

    # Breadcrumbs for detailed pages
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Cambodia<",
     ">이민자 가이드 <i class=\"fa fa-chevron-right\"></i></a></span> <span>캄보디아<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Laos<",
     ">이민자 가이드 <i class=\"fa fa-chevron-right\"></i></a></span> <span>라오스<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Georgia<",
     ">이민자 가이드 <i class=\"fa fa-chevron-right\"></i></a></span> <span>조지아<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Greece<",
     ">이민자 가이드 <i class=\"fa fa-chevron-right\"></i></a></span> <span>그리스<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Panama<",
     ">이민자 가이드 <i class=\"fa fa-chevron-right\"></i></a></span> <span>파나마<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Paraguay<",
     ">이민자 가이드 <i class=\"fa fa-chevron-right\"></i></a></span> <span>파라과이<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Colombia<",
     ">이민자 가이드 <i class=\"fa fa-chevron-right\"></i></a></span> <span>콜롬비아<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Costa Rica<",
     ">이민자 가이드 <i class=\"fa fa-chevron-right\"></i></a></span> <span>코스타리카<"),

    # Last updated line (different format in some files)
    ("Last updated: March 2026",
     "최종 업데이트: 2026년 3월"),

    # -----------------------------------------------------------------------
    # Remaining inline English fragments (partial translation artifacts)
    # -----------------------------------------------------------------------
    ("<strong>비용 of Living</strong>", "<strong>생활비</strong>"),
    ("비용 of Living", "생활비"),
    ("비용s significantly lower", "비용이 훨씬 저렴합니다"),
    ("비용s high but insurance", "비용이 높지만 보험으로"),
    ("비용a del Sol", "코스타 델 솔"),
    ("비용a Blanca", "코스타 블랑카"),
    ("비용s 70-80% lower than USA", "비용은 미국보다 70~80% 저렴"),

    # -----------------------------------------------------------------------
    # Footer copyright line
    # -----------------------------------------------------------------------
    ("Global eVisa &amp; Travel Information Platform",
     "글로벌 전자비자 및 여행 정보 플랫폼"),
    ("Global eVisa & Travel Information Platform",
     "글로벌 전자비자 및 여행 정보 플랫폼"),
    ("Follow eVisa-Card.com", "eVisa-Card.com 팔로우"),
]


def translate_file(filepath: str) -> tuple[int, str]:
    """Apply all replacements to a single file. Returns (changed, filepath)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    for eng, kor in REPLACEMENTS:
        content = content.replace(eng, kor)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return (1, filepath)
    return (0, filepath)


def main():
    files = [
        os.path.join(KO_DIR, f)
        for f in os.listdir(KO_DIR)
        if f.endswith(".html") and "expat-guide" in f
    ]
    files.sort()

    print(f"Processing {len(files)} file(s) in: {KO_DIR}\n")
    changed = 0
    for fp in files:
        status, path = translate_file(fp)
        label = "UPDATED" if status else "no change"
        print(f"  [{label}] {os.path.basename(path)}")
        changed += status

    print(f"\nDone. {changed}/{len(files)} file(s) updated.")


if __name__ == "__main__":
    main()
