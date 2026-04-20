#!/usr/bin/env python3
"""Korean (ko) translations for FAQ page — all 48 questions and 7 categories."""

CATEGORY_TRANSLATIONS = {
    "General Visa Questions": "비자 일반 질문",
    "Schengen &amp; European Visas": "솅겐 및 유럽 비자",
    "Documents &amp; Application Process": "서류 및 신청 절차",
    "Fees &amp; Processing Times": "수수료 및 처리 시간",
    "Extensions, Overstay &amp; Refusal": "연장, 체류 초과 및 거부",
    "Special Visa Types": "특수 비자 유형",
    "Embassy &amp; Application Process": "대사관 및 신청 절차",
}

FAQ_TRANSLATIONS = [
    # ── Category 1: General Visa Questions (7) ──
    {
        "q_en": "What is an eVisa?",
        "q_ko": "전자비자(eVisa)란 무엇인가요?",
        "a_ko": '전자비자(eVisa)는 디지털로 발급되는 여행 허가증입니다. 온라인으로 신청하고 수수료를 납부하면 이메일로 승인을 받습니다. 대사관 방문이 필요 없습니다. <a href="/ko/visa-turkey.html">터키</a>, <a href="/ko/visa-india.html">인도</a>, <a href="/ko/visa-vietnam.html">베트남</a>, <a href="/ko/visa-cambodia.html">캄보디아</a>, <a href="/ko/visa-australia.html">호주</a> 등의 국가에서 전자비자를 제공합니다.',
    },
    {
        "q_en": "What is the difference between a visa and an eVisa?",
        "q_ko": "비자와 전자비자의 차이점은 무엇인가요?",
        "a_ko": "전통적인 비자는 대사관이나 영사관을 방문하여 서류를 제출하고 때로는 인터뷰에 참석해야 합니다. 전자비자는 완전히 온라인으로 신청하며, 처리가 더 빠르고(보통 24~72시간 이내), 이메일로 전자 방식으로 전달됩니다.",
    },
    {
        "q_en": "What is an ETA (Electronic Travel Authorization)?",
        "q_ko": "전자여행허가(ETA)란 무엇인가요?",
        "a_ko": '전자여행허가(ETA)는 비자 면제 국가 국민을 위한 사전 여행 심사입니다. 비자가 아닌 여권에 연동된 여행 허가입니다. <a href="/ko/visa-australia.html">호주</a>, 캐나다, 뉴질랜드, 영국 등이 ETA 시스템을 운영합니다. EU의 ETIAS 시스템은 2026년에 시행됩니다.',
    },
    {
        "q_en": "What is visa-free travel?",
        "q_ko": "무비자 여행이란 무엇인가요?",
        "a_ko": "무비자 여행이란 사전에 비자를 신청하지 않고 입국할 수 있는 것을 말합니다. 입국심사 시 여권만 제시하면 됩니다. 허용 체류 기간은 보통 30~90일입니다. 일본, 싱가포르, EU 등 강력한 여권을 보유한 국가는 190개 이상의 국가에 무비자로 입국할 수 있습니다.",
    },
    {
        "q_en": "What is a visa-on-arrival (VOA)?",
        "q_ko": "도착비자(VOA)란 무엇인가요?",
        "a_ko": '도착비자는 사전 신청 없이 입국 시점(공항 또는 국경)에서 발급됩니다. 여권을 제시하고 양식을 작성하고 수수료를 납부하면 비자 스탬프를 받습니다. <a href="/ko/visa-indonesia.html">인도네시아</a>, <a href="/ko/visa-nepal.html">네팔</a>, <a href="/ko/visa-jordan.html">요르단</a> 등이 많은 국적자에게 도착비자를 제공합니다.',
    },
    {
        "q_en": "How do I check if I need a visa?",
        "q_ko": "비자가 필요한지 어떻게 확인하나요?",
        "a_ko": '비자 요건은 국적과 목적지에 따라 다릅니다. 홈페이지의 <a href="../index.html">비자 검색 도구</a>를 이용하거나 해당 <a href="../destination.html">국가 페이지</a>를 확인하세요. 일반적으로 강력한 여권 국가(EU, 미국, 영국, 일본) 국민은 150개 이상의 국가에 무비자로 입국할 수 있습니다.',
    },
    {
        "q_en": "What is the strongest passport in the world?",
        "q_ko": "세계에서 가장 강력한 여권은 무엇인가요?",
        "a_ko": "2026년 기준으로 일본, 싱가포르, 그리고 여러 EU 여권이 가장 강력하며, 190개 이상의 국가에 무비자 또는 도착비자로 입국할 수 있습니다. 헨리 여권 지수와 아톤 캐피털 지수가 분기별로 여행 자유도를 기준으로 여권을 순위 매깁니다.",
    },

    # ── Category 2: Schengen & European Visas (6) ──
    {
        "q_en": "What is a Schengen visa?",
        "q_ko": "솅겐 비자란 무엇인가요?",
        "a_ko": '솅겐 비자는 단일 비자로 27개 유럽 국가를 여행할 수 있게 해줍니다. 180일 중 최대 90일까지 단기 체류가 가능합니다. 가장 오래 머무를 국가(또는 처음 입국하는 국가)의 대사관에 신청합니다. <a href="/ko/visa-france.html">프랑스</a>, <a href="/ko/visa-germany.html">독일</a>, <a href="/ko/visa-spain.html">스페인</a>, <a href="/ko/visa-italy.html">이탈리아</a> 비자 페이지를 참조하세요.',
    },
    {
        "q_en": "How many countries are in the Schengen Area?",
        "q_ko": "솅겐 지역에는 몇 개의 국가가 포함되어 있나요?",
        "a_ko": "2026년 기준 솅겐 지역에는 27개국이 포함됩니다: 오스트리아, 벨기에, 크로아티아, 체코, 덴마크, 에스토니아, 핀란드, 프랑스, 독일, 그리스, 헝가리, 아이슬란드, 이탈리아, 라트비아, 리히텐슈타인, 리투아니아, 룩셈부르크, 몰타, 네덜란드, 노르웨이, 폴란드, 포르투갈, 루마니아, 슬로바키아, 슬로베니아, 스페인, 스웨덴, 스위스.",
    },
    {
        "q_en": "Can I visit multiple Schengen countries with one visa?",
        "q_ko": "하나의 비자로 여러 솅겐 국가를 방문할 수 있나요?",
        "a_ko": "네. 솅겐 비자로 허가된 체류 기간(180일 중 최대 90일) 동안 27개 솅겐 국가를 자유롭게 이동할 수 있습니다. 주요 목적지 또는 첫 입국 국가의 대사관에 신청해야 합니다.",
    },
    {
        "q_en": "What is the 90/180 rule for Schengen?",
        "q_ko": "솅겐의 90/180 규칙이란 무엇인가요?",
        "a_ko": '90/180 규칙은 180일 기간 내에 솅겐 지역에 최대 90일까지 체류할 수 있다는 것을 의미합니다. 이는 롤링 방식으로 계산됩니다. 90일을 모두 사용하면 솅겐 지역을 떠나 충분한 일수가 "경과"될 때까지 기다려야 재입국할 수 있습니다.',
    },
    {
        "q_en": "What is ETIAS and when does it start?",
        "q_ko": "ETIAS란 무엇이며 언제 시행되나요?",
        "a_ko": "ETIAS(유럽 여행 정보 및 허가 시스템)는 솅겐 지역을 방문하는 비자 면제 여행자를 위한 새로운 사전 여행 허가입니다. 2026년에 시행됩니다. 60개 이상 국가(미국, 영국, 캐나다, 호주, 일본)의 국민은 유럽 여행 전 ETIAS 승인(7유로, 3년 유효)을 받아야 합니다.",
    },
    {
        "q_en": "Can I enter a Schengen country different from my visa country?",
        "q_ko": "비자 발급 국가가 아닌 다른 솅겐 국가로 입국할 수 있나요?",
        "a_ko": "네, 하지만 솅겐 비자는 주요 목적지(가장 오래 체류하는 국가) 국가에서 발급받아야 합니다. 다른 국가를 통해 입국하면 입국심사에서 여행 일정에 대해 질문받을 수 있습니다. 모든 체류 기간이 동일하면 첫 입국 국가에 신청하세요.",
    },

    # ── Category 3: Documents & Application Process (9) ──
    {
        "q_en": "What documents do I need for a visa application?",
        "q_ko": "비자 신청에 어떤 서류가 필요한가요?",
        "a_ko": '일반적인 요건: 유효한 여권(유효기간 6개월 이상), 여권 사진, 작성된 신청서, 여행 일정, 호텔 예약, 재정 증명(은행 명세서), 여행 보험, 초청장(해당되는 경우). <a href="/ko/visa-documents-checklist.html">서류 체크리스트</a>를 참조하세요.',
    },
    {
        "q_en": "What size photo is needed for a visa?",
        "q_ko": "비자에 필요한 사진 크기는 얼마인가요?",
        "a_ko": '대부분의 국가에서 흰색 배경의 35x45mm 사진을 요구합니다. 미국은 51x51mm(2x2인치)를 요구합니다. 사진은 최근 촬영(6개월 이내)이어야 하며, 무표정이고 특정 조명 요건을 충족해야 합니다. <a href="/ko/visa-photo-requirements.html">비자 사진 요건 가이드</a>를 참조하세요.',
    },
    {
        "q_en": "Do I need travel insurance for a visa?",
        "q_ko": "비자 신청 시 여행 보험이 필요한가요?",
        "a_ko": '네, 솅겐 비자의 경우 최소 3만 유로 보장의 여행 보험이 필요합니다. 다른 많은 국가에서도 여행 보험을 요구하거나 강력히 권장합니다. <a href="/ko/travel-insurance-for-visa-applications.html">여행 보험 가이드</a>를 참조하세요.',
    },
    {
        "q_en": "How long must my passport be valid for travel?",
        "q_ko": "여행을 위해 여권 유효기간이 얼마나 남아있어야 하나요?",
        "a_ko": "대부분의 국가에서 체류 예정일로부터 최소 6개월의 여권 유효기간을 요구합니다. 솅겐 국가는 출국일로부터 3개월의 유효기간과 빈 페이지 2장을 요구합니다. 항상 해당 국가의 구체적인 요건을 확인하세요.",
    },
    {
        "q_en": "What bank statement amount do I need for a visa?",
        "q_ko": "비자 신청 시 은행 잔고가 얼마나 필요한가요?",
        "a_ko": "요건은 다양합니다. 솅겐 비자의 경우 체류 일당 50~100유로를 증명해야 합니다. 미국 B1/B2의 경우 충분한 자금을 증명해야 합니다(고정 금액 없음). 영국의 경우 3~6개월의 꾸준한 수입을 보여야 합니다. 일반적으로 여행 비용 외에 30~50% 여유 자금을 보유한 잔고를 보여주세요.",
    },
    {
        "q_en": "Is a hotel booking required for a visa application?",
        "q_ko": "비자 신청에 호텔 예약이 필요한가요?",
        "a_ko": "대부분의 비자 신청에는 전체 체류 기간의 숙소 증명이 필요합니다. 호텔 예약(선불 필수 아님), 에어비앤비 예약 또는 초청자의 편지가 가능합니다. 솅겐 비자의 경우 모든 숙박을 커버해야 합니다.",
    },
    {
        "q_en": "Do I need a return ticket to get a visa?",
        "q_ko": "비자를 받으려면 왕복 항공권이 필요한가요?",
        "a_ko": "대부분의 국가에서는 비자 신청 및 입국심사 시 출국 또는 왕복 여행 증명을 요구합니다. 비자 만료 전에 출국할 계획을 보여주는 확정된 항공편 예약, 버스 티켓 또는 페리 티켓이 가능합니다.",
    },
    {
        "q_en": "What is an invitation letter for a visa?",
        "q_ko": "비자 초청장이란 무엇인가요?",
        "a_ko": "초청장은 목적지 국가의 개인이나 기관이 방문을 초청하는 문서입니다. 초청자 정보, 관계, 방문 목적 및 날짜, 숙박 안배, 재정 책임 등이 포함됩니다. 많은 솅겐 비자 및 비즈니스 비자 신청에 필요합니다.",
    },
    {
        "q_en": "What are biometrics for a visa?",
        "q_ko": "비자 생체인식이란 무엇인가요?",
        "a_ko": "생체인식에는 비자 신청 시 수집되는 지문 스캔과 디지털 사진이 포함됩니다. 솅겐 국가, 영국, 미국, 캐나다 등 많은 국가에서 생체인식을 요구합니다. 신원 확인을 위해 데이터베이스에 저장되며 보통 5년간 유효합니다.",
    },

    # ── Category 4: Fees & Processing Times (6) ──
    {
        "q_en": "How much does a visa cost?",
        "q_ko": "비자 비용은 얼마인가요?",
        "a_ko": '비자 수수료는 매우 다양합니다. 예시: 솅겐 비자 80유로, 미국 B1/B2 비자 185달러, 인도 전자비자 25~80달러, 터키 전자비자 50달러, 호주 ETA 20호주달러, 캄보디아 전자비자 36달러. 어린이 및 일부 국적자는 할인 수수료를 받을 수 있습니다. <a href="/ko/visa-processing-times.html">처리 시간</a> 페이지를 참조하세요.',
    },
    {
        "q_en": "How long does visa processing take?",
        "q_ko": "비자 처리에 얼마나 걸리나요?",
        "a_ko": "전자비자는 보통 24~72시간이 소요됩니다. 솅겐 비자는 15~45일이 소요됩니다. 미국 B1/B2 비자는 대사관에 따라 수 주에서 수 개월이 걸릴 수 있습니다. 항상 여행일 전에 충분한 여유를 두고 신청하세요.",
    },
    {
        "q_en": "How far in advance should I apply for a visa?",
        "q_ko": "비자는 얼마나 미리 신청해야 하나요?",
        "a_ko": "전자비자: 여행 1~2주 전. 솅겐 비자: 3~6개월 전(최대 6개월 전, 최소 출발 15일 전). 미국 비자: 대기 시간이 길어 3~6개월 이상. 성수기에는 더 일찍 신청해야 할 수 있습니다.",
    },
    {
        "q_en": "Can I get a visa refund if my application is rejected?",
        "q_ko": "비자 신청이 거부되면 환불받을 수 있나요?",
        "a_ko": "대부분의 경우 비자 수수료는 결과에 관계없이 환불이 불가합니다. 수수료는 신청 처리 비용이지 승인을 보장하는 것이 아닙니다.",
    },
    {
        "q_en": "How do I track my visa application status?",
        "q_ko": "비자 신청 상태를 어떻게 추적하나요?",
        "a_ko": "대부분의 대사관과 VFS 글로벌 사무소에서 온라인 추적을 제공합니다. 신청서 제출 시 참조번호를 받게 됩니다. 이 번호를 대사관 또는 VFS 웹사이트에 입력하여 상태를 확인하세요. 일부 국가에서는 각 처리 단계에서 이메일/SMS 알림을 보냅니다.",
    },
    {
        "q_en": "What is VFS Global?",
        "q_ko": "VFS 글로벌이란 무엇인가요?",
        "a_ko": "VFS 글로벌은 정부를 대신하여 비자 신청을 처리하는 민간 기업입니다. 전 세계에 비자 신청 센터(VAC)를 운영합니다. 대사관 대신 VFS 센터에 서류를 제출합니다. VFS는 비자 수수료 외에 별도의 서비스 수수료를 부과합니다.",
    },

    # ── Category 5: Extensions, Overstay & Refusal (4) ──
    {
        "q_en": "Can I extend my visa?",
        "q_ko": "비자를 연장할 수 있나요?",
        "a_ko": '국가와 비자 유형에 따라 다릅니다. 일부 국가에서는 연장을 허용합니다(예: 인도네시아 도착비자는 30일 연장 가능, 태국 관광비자는 30일 연장 가능). 솅겐 비자는 예외적인 상황에서만 연장이 가능합니다. <a href="/ko/visa-rejection-reasons.html">비자 거부 사유</a> 페이지에서 관련 정보를 확인하세요.',
    },
    {
        "q_en": "What happens if my visa is refused?",
        "q_ko": "비자가 거부되면 어떻게 되나요?",
        "a_ko": "사유가 포함된 서면 통지를 받게 됩니다. 일반적인 거부 사유로는 재정 증명 부족, 서류 미비, 이민 의도 의심 등이 있습니다. 보통 1~3개월 이내에 이의를 제기하거나 보완된 서류로 재신청할 수 있습니다.",
    },
    {
        "q_en": "What is overstaying a visa?",
        "q_ko": "비자 체류 초과란 무엇인가요?",
        "a_ko": "체류 초과란 허가된 체류 기간을 넘겨 해당 국가에 머무는 것을 말합니다. 벌금(예: 태국은 1일당 500바트), 추방, 구금, 입국 금지(1~10년), 향후 비자 발급 어려움 등의 제재가 있습니다. 항상 비자 유효 기간을 준수하세요.",
    },
    {
        "q_en": "What happens if I lose my passport with a valid visa?",
        "q_ko": "유효한 비자가 있는 여권을 분실하면 어떻게 되나요?",
        "a_ko": "즉시 가장 가까운 자국 대사관에 연락하여 긴급 여행 문서를 발급받으세요. 분실된 여권의 비자는 무효로 처리되므로 새 비자를 신청해야 합니다. 경찰 신고서를 작성하고 새 비자 신청용으로 사본을 보관하세요.",
    },

    # ── Category 6: Special Visa Types (10) ──
    {
        "q_en": "What is a transit visa?",
        "q_ko": "통과비자란 무엇인가요?",
        "a_ko": "통과비자는 최종 목적지로 가는 도중에 한 국가를 경유할 수 있게 해줍니다. 보통 24~72시간 동안 유효합니다. 일부 국가에서는 공항을 떠나지 않더라도 통과비자를 요구합니다.",
    },
    {
        "q_en": "Can I work on a tourist visa?",
        "q_ko": "관광비자로 일할 수 있나요?",
        "a_ko": "아니요. 관광비자는 일반적으로 취업을 허용하지 않습니다. 관광비자로 근무하는 것은 대부분의 국가에서 불법이며, 추방, 벌금, 향후 비자 거부로 이어질 수 있습니다. 취업을 위해서는 별도의 취업비자 또는 취업허가가 필요합니다.",
    },
    {
        "q_en": "What is a digital nomad visa?",
        "q_ko": "디지털 노마드 비자란 무엇인가요?",
        "a_ko": '디지털 노마드 비자는 해외 고용주나 클라이언트를 위해 원격으로 일하면서 다른 나라에 거주할 수 있게 해줍니다. 인기 국가로는 <a href="/ko/visa-portugal.html">포르투갈</a>, <a href="/ko/visa-spain.html">스페인</a>, <a href="/ko/visa-thailand.html">태국</a>, <a href="/ko/visa-colombia.html">콜롬비아</a>, <a href="/ko/visa-indonesia.html">인도네시아</a> 등이 있습니다. <a href="/ko/digital-nomad-visas-guide.html">디지털 노마드 비자 가이드</a>를 참조하세요.',
    },
    {
        "q_en": "What is a student visa?",
        "q_ko": "학생비자란 무엇인가요?",
        "a_ko": "학생비자는 다른 나라의 교육기관에서 수학할 수 있게 해줍니다. 요건에는 입학허가서, 등록금 납부 또는 장학금 증명, 생활비 재정 증명, 건강보험, 그리고 때로는 어학 능력 증명서가 포함됩니다.",
    },
    {
        "q_en": "What is a Working Holiday Visa?",
        "q_ko": "워킹홀리데이 비자란 무엇인가요?",
        "a_ko": '워킹홀리데이 비자(WHV)는 청년(보통 18~30세 또는 18~35세)이 다른 나라에서 1~2년간 여행하며 일할 수 있게 해줍니다. 인기 프로그램으로는 <a href="/ko/visa-australia.html">호주</a>, <a href="/ko/visa-new-zealand.html">뉴질랜드</a>, <a href="/ko/visa-canada.html">캐나다</a>, <a href="/ko/visa-japan.html">일본</a> 등이 있습니다.',
    },
    {
        "q_en": "What is a Golden Visa?",
        "q_ko": "골든비자란 무엇인가요?",
        "a_ko": '골든비자는 국가에 상당한 금융 투자(주로 부동산 또는 사업)를 한 투자자에게 부여되는 거주 허가입니다. <a href="/ko/visa-portugal.html">포르투갈</a>, <a href="/ko/visa-spain.html">스페인</a>, <a href="/ko/visa-greece.html">그리스</a>, <a href="/ko/visa-uae.html">UAE</a> 등에서 인기 프로그램을 운영합니다. 투자 금액은 25만~50만 유로 이상입니다.',
    },
    {
        "q_en": "What is a long-stay visa (Type D)?",
        "q_ko": "장기체류비자(D형)란 무엇인가요?",
        "a_ko": "D형 비자(국가비자)는 특정 국가에 90일 이상 체류할 수 있게 해줍니다. 솅겐 단기체류비자(C형)와 달리, D형은 학업, 취업, 가족 합류, 은퇴 등의 목적으로 개별 국가에서 발급됩니다.",
    },
    {
        "q_en": "What is a multiple-entry visa?",
        "q_ko": "복수입국비자란 무엇인가요?",
        "a_ko": "복수입국비자는 비자 유효 기간 동안 여러 번 출입국할 수 있게 해줍니다. 비즈니스 여행자나 인근 국가를 방문하는 사람에게 유용합니다. 단수입국비자는 한 번 출국하면 무효가 됩니다.",
    },
    {
        "q_en": "Do children need their own visa?",
        "q_ko": "어린이도 별도의 비자가 필요한가요?",
        "a_ko": "네, 대부분의 경우 영유아를 포함하여 어린이도 별도의 비자가 필요합니다. 일부 국가에서는 6세 또는 12세 미만 어린이에게 할인 수수료를 제공합니다. 대부분의 국제 여행에서 어린이도 자체 여권이 필요합니다.",
    },
    {
        "q_en": "Can dual citizens use either passport for visas?",
        "q_ko": "이중 국적자는 비자 신청 시 어느 여권이든 사용할 수 있나요?",
        "a_ko": "네, 이중 국적자는 어느 여권을 사용할지 선택할 수 있습니다. 더 나은 비자 조건을 제공하는 여권을 사용하세요. 항상 같은 여권으로 입출국하세요. 일부 국가에서는 이중 국적을 인정하지 않으므로 양국의 법률을 확인하세요.",
    },

    # ── Category 7: Embassy & Application Process (5) ──
    {
        "q_en": "How do I apply for a visa at an embassy?",
        "q_ko": "대사관에서 비자를 어떻게 신청하나요?",
        "a_ko": '절차: 1) 대사관 웹사이트에서 요건을 확인합니다. 2) 서류를 준비합니다. 3) 예약을 합니다. 4) 방문하여 서류를 제출합니다. 5) 수수료를 납부합니다. 6) 처리를 기다립니다. 7) 비자가 부착된 여권을 수령합니다. <a href="/ko/how-to-apply-evisa.html">신청 방법 가이드</a>를 참조하세요.',
    },
    {
        "q_en": "What is a visa interview?",
        "q_ko": "비자 인터뷰란 무엇인가요?",
        "a_ko": "일부 국가(특히 미국, 영국, 캐나다)에서는 대사관에서 직접 인터뷰를 요구합니다. 영사관 직원이 여행 계획, 본국과의 유대 관계, 재정 상황, 방문 목적에 대해 질문합니다. 솔직하게 답변하고 증빙 서류를 지참하세요.",
    },
    {
        "q_en": "Can I apply for a visa from a country I am not a citizen of?",
        "q_ko": "국적국이 아닌 나라에서 비자를 신청할 수 있나요?",
        "a_ko": "네, 많은 경우 합법적으로 거주하는 국가의 대사관에서 신청할 수 있습니다. 합법적 거주 증명(거주 허가, 장기 비자)이 필요합니다. 일부 국가에서는 해당 국가의 국민 또는 영주권자의 신청만 받습니다.",
    },
    {
        "q_en": "What is a visa sticker vs stamp vs e-visa?",
        "q_ko": "비자 스티커, 스탬프, 전자비자의 차이점은 무엇인가요?",
        "a_ko": "비자 스티커는 여권 페이지에 부착되는 물리적 라벨입니다(솅겐, 미국, 영국). 비자 스탬프는 입국심사 시 찍히는 출입국 도장입니다. 전자비자는 여권번호에 연동된 디지털 허가로 물리적 스티커가 필요 없습니다.",
    },
    {
        "q_en": "Can I travel with a visa in a cancelled passport?",
        "q_ko": "취소된 여권에 있는 비자로 여행할 수 있나요?",
        "a_ko": "비자가 아직 유효한 경우 가능한 경우가 있습니다. 미국과 영국은 새 여권과 함께 구 여권의 유효한 비자로 여행할 수 있도록 허용합니다. 구체적인 국가 규정을 확인하세요. 일부 국가에서는 새 여권으로 비자를 이전해야 합니다.",
    },
]
