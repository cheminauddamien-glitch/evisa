#!/usr/bin/env python3
"""
gen_subpages_batch_e.py
Generates 3 sub-pages per country for 8 countries:
  {country}-visa-requirements.html
  {country}-visa-fees.html
  {country}-visa-processing-time.html
Output directory: www/en/
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Country data
# ---------------------------------------------------------------------------
COUNTRIES = {
    "united-kingdom": {
        "name": "United Kingdom",
        "name_upper": "UNITED KINGDOM",
        "flag_code": "gb",
        "official_site": "gov.uk/uk-visa",
        "official_url": "https://www.gov.uk/browse/visas-immigration",
        "currency": "GBP",
        "processing_time": "3–6 weeks",
        "visa_types": [
            ("Electronic Travel Authorisation (ETA)", "GBP 10", "Eligible nationalities, from Jan 2025, 6 months multiple entry"),
            ("Standard Visitor Visa", "GBP 115", "Up to 6 months, most nationalities"),
            ("Skilled Worker Visa", "GBP 719+", "Sponsored employment, tiered fees by salary"),
            ("Student Visa", "GBP 490", "Full-time study at licensed institution"),
            ("Transit Visa (Direct Airside)", "GBP 35", "Non-visa national transiting via UK airports"),
            ("Family Visa (Spouse/Partner)", "GBP 1,846", "Joining a settled person in the UK"),
        ],
        "requirements_intro": (
            "The United Kingdom operates an independent immigration system following its departure from the EU. "
            "Most visitors from outside the Common Travel Area (Ireland) need either a visa or, since January 2025, "
            "an Electronic Travel Authorisation (ETA) before travelling to the UK. The ETA costs GBP 10, is linked "
            "to your passport and allows multiple trips of up to 6 months over 2 years. Citizens of the EU, EEA, USA, "
            "Canada, Australia and many other nationalities are among those who can obtain an ETA instead of a full visa."
        ),
        "fees_intro": (
            "UK visa fees are set by the Home Office and vary significantly by visa category and applicant circumstances. "
            "The Standard Visitor Visa costs GBP 115 for stays up to 6 months. The ETA, introduced in January 2025, "
            "costs GBP 10 per person and is required by nationals of many countries that previously entered visa-free. "
            "Work visas start at GBP 719 for a Skilled Worker application from outside the UK. Healthcare surcharges "
            "apply to most applications at GBP 1,035 per year."
        ),
        "processing_intro": (
            "UK visa processing times depend on the visa category and where you apply. The ETA is usually granted "
            "within minutes to a few hours digitally. Standard Visitor Visa decisions are typically issued in "
            "3–6 weeks when applying from most countries. Priority processing is available for an additional "
            "GBP 250–500 fee, reducing wait times to 5 working days. Super Priority services (24 hours) are "
            "available in select countries. Skilled Worker and settlement visas may take longer due to additional checks."
        ),
        "faq": [
            ("Do EU citizens need a UK visa after Brexit?",
             "EU citizens do not need a visa for short visits to the UK of up to 6 months, but since January 2025 they need an Electronic Travel Authorisation (ETA) costing GBP 10, which is obtained digitally before travel."),
            ("How much does a UK Standard Visitor Visa cost in 2026?",
             "The UK Standard Visitor Visa costs GBP 115 for up to 6 months. A 2-year long-stay visitor visa costs GBP 400, a 5-year visa costs GBP 771, and a 10-year visa costs GBP 963."),
            ("What is the UK ETA and who needs it?",
             "The UK Electronic Travel Authorisation (ETA) was introduced in January 2025. It costs GBP 10 and is required by nationals of countries that can visit visa-free but were not previously required to obtain prior permission. EU, EEA, and many other nationals need it."),
            ("How long does a UK visa application take?",
             "UK Standard Visitor Visa applications typically take 3–6 weeks. Priority service (additional GBP 250+) reduces this to around 5 working days. Super Priority (24-hour) service is available in certain countries for around GBP 800 extra."),
        ],
        "howto_context": "UK ETA or Standard Visitor Visa",
    },
    "romania": {
        "name": "Romania",
        "name_upper": "ROMANIA",
        "flag_code": "ro",
        "official_site": "mae.ro",
        "official_url": "https://www.mae.ro/en/node/2035",
        "currency": "EUR",
        "processing_time": "10–30 days",
        "visa_types": [
            ("EU/EEA Citizens", "Free", "No visa required, free movement as EU member"),
            ("Schengen Area Access (air/sea)", "Applicable since March 2024", "Romania joined Schengen for air/sea since March 2024"),
            ("Full Schengen Integration", "In progress", "Land border Schengen integration proceeding"),
            ("Romanian Short-stay Visa (C)", "EUR 65", "Non-EU nationals for tourism, up to 90 days"),
            ("Romanian Long-stay Visa (D)", "EUR 65–120", "Study, work, or family reunification"),
            ("Transit Visa (A/B)", "EUR 65", "Airport transit or road transit for certain nationalities"),
        ],
        "requirements_intro": (
            "Romania is a member of the European Union. EU and EEA citizens enjoy free movement rights and need only "
            "a valid ID card or passport to enter and reside in Romania. Since March 2024, Romania joined the "
            "Schengen Area for air and sea travel, meaning passengers arriving by air or sea from Schengen countries "
            "no longer face border checks. Full land border Schengen integration is progressing. "
            "Non-EU nationals holding a valid Schengen visa can also use it to enter Romania. "
            "Nationals from countries without visa-free agreements must apply for a Romanian national visa (Type C or D) "
            "through a Romanian embassy, which costs EUR 65."
        ),
        "fees_intro": (
            "Romanian visa fees are standardised by the Ministry of Foreign Affairs. The short-stay visa (Type C) "
            "costs EUR 65 for tourism, business, or transit. Long-stay visas (Type D) for study or employment "
            "cost between EUR 65 and EUR 120 depending on purpose. Holders of valid Schengen visas from other "
            "Schengen states do not need a separate Romanian visa for short stays. "
            "Processing is handled by Romanian embassies and consulates worldwide."
        ),
        "processing_intro": (
            "Romanian visa processing typically takes 10–30 days from the date of submission of a complete application. "
            "Emergency processing may be available in exceptional circumstances at additional cost. "
            "EU citizens and Schengen visa holders face no processing time for entry. "
            "Applicants should contact the nearest Romanian consulate to confirm current processing times, "
            "as these vary by country and application volume. "
            "Air and sea passengers from Schengen countries have benefited from reduced border formalities since March 2024."
        ),
        "faq": [
            ("Is Romania in the Schengen Area?",
             "Romania joined the Schengen Area for air and sea borders in March 2024. Full integration including land borders is in progress. This means air and sea passengers from Schengen countries no longer face internal border checks at Romanian airports and sea ports."),
            ("Do I need a visa to visit Romania as a non-EU citizen?",
             "Non-EU nationals without visa-free agreements with Romania need a short-stay visa (Type C) costing EUR 65, or a long-stay visa (Type D) for work, study, or family purposes. Holders of valid Schengen visas may enter Romania without a separate Romanian visa."),
            ("How long can I stay in Romania visa-free?",
             "EU and EEA citizens can stay indefinitely with right of free movement. Nationals from countries with visa-free agreements may stay up to 90 days in any 180-day period. Holders of Schengen visas can also use them for short stays in Romania."),
            ("What documents are required for a Romanian visa application?",
             "Required documents include: valid passport (at least 6 months validity), visa application form, passport photo, travel insurance (minimum EUR 30,000), proof of accommodation, return ticket, financial means proof, and EUR 65 fee. Work or study visas require additional supporting documents."),
        ],
        "howto_context": "Romanian Short-stay or Long-stay Visa",
    },
    "jordan": {
        "name": "Jordan",
        "name_upper": "JORDAN",
        "flag_code": "jo",
        "official_site": "moi.gov.jo",
        "official_url": "https://www.moi.gov.jo",
        "currency": "JOD",
        "processing_time": "1–3 days",
        "visa_types": [
            ("Visa on Arrival (Single)", "JOD 40 (~USD 56)", "Most nationalities, 30 days stay"),
            ("JordanPass (Visa + Sites)", "From JOD 70", "Includes single-entry visa + 40+ tourist sites"),
            ("eVisa (Multiple Entry)", "JOD 60+", "Online via e-visa portal, 3 months validity"),
            ("Free Visa Nationalities", "Free", "Some Arab nationalities and diplomatic passports"),
            ("Aqaba Special Economic Zone", "Free", "Visa-free entry for Aqaba region visits"),
            ("Residency/Long-Stay Permit", "Varies", "Work, study, or family, through MOI"),
        ],
        "requirements_intro": (
            "Jordan welcomes tourists from most countries with a straightforward visa process. "
            "A Visa on Arrival (VOA) is available for most nationalities at Queen Alia International Airport and "
            "land borders, costing JOD 40 (approximately USD 56) for a single-entry 30-day stay. "
            "The JordanPass is an excellent value option starting from JOD 70: it includes the single-entry visa "
            "and admission to over 40 tourist attractions including Petra. "
            "An eVisa for multiple entries is available online through the official portal at moi.gov.jo. "
            "Citizens of several Arab countries and diplomatic passport holders may enter free of charge."
        ),
        "fees_intro": (
            "Jordan visa fees in 2026: Visa on Arrival costs JOD 40 (~USD 56) for a single entry, 30-day stay. "
            "The JordanPass starts from JOD 70 for 1 day at tourist sites, JOD 75 for 2 days, and JOD 80 for 3 days—"
            "all include the visa fee. Multiple-entry eVisas cost JOD 60 or more depending on validity period. "
            "The Aqaba Special Economic Zone offers visa-free entry for visits limited to the Aqaba area. "
            "Payment is accepted in JOD, USD, and major credit cards at airports."
        ),
        "processing_intro": (
            "Jordan visa processing is fast. Visa on Arrival at Queen Alia International Airport is typically processed "
            "in under 30 minutes upon arrival. eVisa applications submitted online are usually approved within 1–3 business days. "
            "JordanPass purchase is instant online. "
            "Land border crossings with Israel (Allenby/King Hussein Bridge) operate differently and may require "
            "pre-arrangement for certain nationalities. Always check current entry requirements with the "
            "Jordanian Ministry of Interior at moi.gov.jo before travel."
        ),
        "faq": [
            ("Can I get a Jordan visa on arrival?",
             "Yes, most nationalities can obtain a Visa on Arrival at Jordan's major entry points, including Queen Alia International Airport. The fee is JOD 40 (~USD 56) for a 30-day single-entry visa. Some nationalities need to pre-arrange visas through a Jordanian embassy."),
            ("What is the JordanPass and is it worth it?",
             "The JordanPass starts from JOD 70 and includes both the single-entry visa fee (saving you JOD 40) and free entry to 40+ tourist attractions including Petra (which alone costs JOD 50). For tourists visiting multiple sites it represents excellent value."),
            ("How do I apply for a Jordan eVisa in 2026?",
             "Apply through the official Jordanian eVisa portal at moi.gov.jo or the dedicated evisa.jordan.gov.jo portal. Submit your passport details, travel dates, and pay online. Multiple-entry eVisas are available and approval usually takes 1–3 business days."),
            ("Is Jordan visa-free for any nationalities?",
             "Citizens of some Arab League countries and diplomatic passport holders can enter Jordan free of charge. Additionally, Aqaba Special Economic Zone offers visa-free access for visitors limiting their stay to the Aqaba region. Check the current list at moi.gov.jo."),
        ],
        "howto_context": "Jordan Visa on Arrival or eVisa",
    },
    "qatar": {
        "name": "Qatar",
        "name_upper": "QATAR",
        "flag_code": "qa",
        "official_site": "portal.moi.gov.qa",
        "official_url": "https://portal.moi.gov.qa",
        "currency": "QAR",
        "processing_time": "1–3 days",
        "visa_types": [
            ("Visa-Free Entry", "Free", "100+ nationalities, 30–90 days depending on passport"),
            ("eVisa (others)", "QAR 100 (~USD 27)", "Nationalities not eligible for visa-free, online application"),
            ("Visa on Arrival", "QAR 100", "Available for eligible additional nationalities"),
            ("Hayya Card", "Free (legacy)", "Previously for FIFA 2022, now archived"),
            ("GCC Resident Visa", "Free", "GCC residents with valid work/residency permits"),
            ("Business/Conference Visa", "Varies", "Sponsored by Qatar-based entity"),
        ],
        "requirements_intro": (
            "Qatar has one of the most open visa policies in the Gulf region. Over 100 nationalities can enter "
            "Qatar visa-free for stays of 30 to 90 days, including citizens of the USA, UK, EU, Canada, Australia, "
            "Japan, and many others. Nationals of countries not on the visa-free list can apply for an eVisa online "
            "through the Ministry of Interior portal at portal.moi.gov.qa, paying QAR 100 (~USD 27). "
            "GCC residents holding valid residence permits from Saudi Arabia, UAE, Bahrain, Kuwait, or Oman can also "
            "enter Qatar visa-free or obtain a visa on arrival. All visitors must have a valid passport, "
            "return ticket, and sufficient funds for their stay."
        ),
        "fees_intro": (
            "Qatar visa fees are among the lowest in the region. Visa-free entry is completely free for over "
            "100 nationalities. For those who require a visa, the eVisa costs QAR 100 (~USD 27) and is valid for "
            "30 days from the date of issue with a 30-day maximum stay. "
            "Visa on Arrival for eligible nationalities costs QAR 100 payable at the airport. "
            "GCC residents with valid work permits can enter without a fee. "
            "Business and conference visas are sponsored by Qatar entities and fees vary. "
            "There are no airport taxes payable separately by most tourists."
        ),
        "processing_intro": (
            "Qatar eVisa processing is among the fastest in the world. Online eVisa applications at portal.moi.gov.qa "
            "are typically processed within 1–3 business days. Visa on Arrival at Hamad International Airport is "
            "issued at immigration counters and takes 15–30 minutes on average. "
            "Visa-free nationals require no processing time—entry is granted upon arrival with a valid passport. "
            "Qatar Airways passengers transiting Doha for over 5 hours can access a free Doha transit tour "
            "without a visa. Always check the current list of eligible nationalities at portal.moi.gov.qa."
        ),
        "faq": [
            ("Which nationalities can enter Qatar visa-free?",
             "Over 100 nationalities can enter Qatar visa-free, including citizens of the USA, UK, EU countries, Canada, Australia, Japan, South Korea, Singapore, New Zealand, and many others. The visa-free period varies from 30 to 90 days depending on your nationality. Check portal.moi.gov.qa for the full list."),
            ("How do I apply for a Qatar eVisa in 2026?",
             "Apply through the official Ministry of Interior portal at portal.moi.gov.qa. Create an account, submit passport details, travel dates, and pay QAR 100 (~USD 27) online. Processing takes 1–3 business days and the approved eVisa is sent to your email."),
            ("Can GCC residents visit Qatar without a visa?",
             "Yes, residents of GCC countries (Saudi Arabia, UAE, Bahrain, Kuwait, Oman) holding valid work or residency permits can enter Qatar visa-free or obtain a visa on arrival. Some GCC residents are eligible for free entry. Check current rules at portal.moi.gov.qa."),
            ("Is there an airport transit visa for Qatar?",
             "Qatar does not require a transit visa for most nationalities transiting Hamad International Airport. Qatar Airways offers a free Doha Stopover programme for passengers transiting more than 5 hours, including a free hotel night. Check eligibility on the Qatar Airways website."),
        ],
        "howto_context": "Qatar eVisa or Visa-Free Entry",
    },
    "brazil": {
        "name": "Brazil",
        "name_upper": "BRAZIL",
        "flag_code": "br",
        "official_site": "gov.br",
        "official_url": "https://www.gov.br/mre/en/topics/visas",
        "currency": "USD",
        "processing_time": "3–10 days",
        "visa_types": [
            ("Visa-Free (Mercosur + bilateral)", "Free", "Argentina, Uruguay, Paraguay, Chile + others including USA, Canada, Japan, Australia since 2024"),
            ("eVisa (VITEM II)", "USD 80", "Tourism/business, valid 90 days, multiple entries"),
            ("Consular Visa", "USD 80–160", "Applied at Brazilian consulate, various categories"),
            ("Digital Nomad Visa (VITEM XIV)", "USD 80", "Remote workers, 1 year renewable"),
            ("Mercosur Resident Visa", "Varies", "MERCOSUR nationals for longer residence"),
            ("Student/Research Visa", "USD 80+", "Higher education or research institutions"),
        ],
        "requirements_intro": (
            "Brazil significantly expanded its visa-free policy in 2024, restoring visa-free access for "
            "US, Canadian, Japanese, and Australian passport holders after a years-long reciprocity dispute. "
            "Citizens of MERCOSUR countries (Argentina, Uruguay, Paraguay) and many bilateral agreement nations "
            "can enter Brazil visa-free. Nationals who still require a visa can apply for an eVisa (VITEM II) "
            "online at gov.br for USD 80, valid for 90 days with multiple entries. "
            "Brazil also offers a Digital Nomad Visa (VITEM XIV) for remote workers, valid for 1 year and renewable."
        ),
        "fees_intro": (
            "Brazil visa fees in 2026: The eVisa (VITEM II) for tourism costs USD 80 and allows a 90-day stay "
            "with multiple entries within 1 year of issue. Consular visas range from USD 80 to USD 160 "
            "depending on the category. The Digital Nomad Visa costs approximately USD 80 plus the fee for the "
            "Brazilian Federal Police registration (~BRL 204). Visa-free nationalities incur no fee. "
            "All fees are payable online by credit card. Some countries may face different reciprocity fees—"
            "check the current schedule at the Brazilian Ministry of Foreign Affairs (MRE) website."
        ),
        "processing_intro": (
            "Brazilian eVisa processing typically takes 3–10 business days after submission of a complete application. "
            "Apply online at gov.br/mre. Consular visa processing times vary by country and consulate: "
            "routine processing takes 5–15 business days. Priority processing is not universally available. "
            "The Digital Nomad Visa requires additional documentation and may take 2–4 weeks. "
            "Applicants should apply well in advance of their travel date. Visa-free nationals require no "
            "prior processing and are admitted at the port of entry."
        ),
        "faq": [
            ("Do US citizens need a visa for Brazil in 2026?",
             "No. US citizens regained visa-free access to Brazil in 2024. They can visit for up to 90 days per stay (maximum 180 days per year) without a visa. This applies to tourism, business, and transit purposes. No prior application is needed."),
            ("How do I apply for a Brazil eVisa?",
             "Apply online at gov.br/mre. Create an account, complete the VITEM II application form, upload your passport scan and photo, and pay USD 80. Processing typically takes 3–10 business days. The approved eVisa is sent to your email and must be printed or saved on your device."),
            ("What is the Brazil Digital Nomad Visa?",
             "The VITEM XIV (Digital Nomad Visa) allows remote workers and digital nomads to live in Brazil for 1 year, renewable for another year. Applicants must prove a monthly income of at least USD 1,500 or USD 18,000 in savings. Apply at a Brazilian consulate or online at gov.br."),
            ("How long can I stay in Brazil visa-free?",
             "Visa-free nationals (including US, Canadian, Japanese, and Australian citizens from 2024) can stay up to 90 consecutive days, with a maximum of 180 days per calendar year. MERCOSUR nationals may stay longer under bilateral residence agreements."),
        ],
        "howto_context": "Brazil eVisa (VITEM II)",
    },
    "argentina": {
        "name": "Argentina",
        "name_upper": "ARGENTINA",
        "flag_code": "ar",
        "official_site": "cancilleria.gob.ar",
        "official_url": "https://www.cancilleria.gob.ar/en/services/travel-to-argentina",
        "currency": "USD",
        "processing_time": "No visa required for most",
        "visa_types": [
            ("Visa-Free Entry (80+ nationalities)", "Free", "USA, EU, UK, Canada, Australia, 90 days — no fee"),
            ("Reciprocity Fee (abolished 2023)", "Abolished", "Previously charged to USA, Canada, Australia — now free"),
            ("MERCOSUR Free Movement", "Free", "Argentina, Brazil, Uruguay, Paraguay, Chile — 90 days"),
            ("Consular Visa (non-exempt)", "USD 50–100", "Nationalities not in visa-free list"),
            ("Temporary Residency", "Varies", "Work, study, or family, via DNM"),
            ("Permanent Residency", "Varies", "After 2 years temporary residence"),
        ],
        "requirements_intro": (
            "Argentina has one of the most generous visa-free policies in South America. "
            "Over 80 nationalities can enter Argentina without a visa for up to 90 days, "
            "including citizens of the United States, European Union, United Kingdom, Canada, Australia, "
            "Japan, and South Korea. The reciprocity fee previously charged to US, Canadian, and Australian "
            "citizens was abolished in 2023, making entry entirely free for these nationalities. "
            "MERCOSUR nationals (Brazil, Uruguay, Paraguay, Chile) enjoy additional rights and may stay longer. "
            "Nationalities not included in the visa-free list must apply for a consular visa "
            "at an Argentine embassy or consulate."
        ),
        "fees_intro": (
            "Argentina entry is free for over 80 nationalities following the 2023 abolition of the reciprocity fee. "
            "US, Canadian, and Australian visitors who previously paid USD 160 (USA) or AUD 100 (Australia) "
            "can now enter without any fee. Consular visas for non-exempt nationalities cost approximately "
            "USD 50–100 depending on category and consulate. "
            "MERCOSUR residents pay nothing. There is a USD 18 airport tax included in most airline tickets. "
            "Work and study permits involve separate immigration fees through the National Directorate of Migration (DNM)."
        ),
        "processing_intro": (
            "Visa-free nationals require no prior processing — entry is granted upon arrival at Ezeiza International "
            "Airport or other ports of entry. Immigration processing at the airport typically takes 10–30 minutes. "
            "Consular visas for non-exempt nationalities take 5–15 business days to process. "
            "Temporary residency applications through the National Directorate of Migration (DNM) "
            "can take 2–6 months. Always check current entry requirements at cancilleria.gob.ar before travel, "
            "as bilateral agreements may change."
        ),
        "faq": [
            ("Do I need a visa to visit Argentina in 2026?",
             "Citizens of over 80 nationalities, including the USA, UK, EU countries, Canada, and Australia, do not need a visa to visit Argentina for up to 90 days. The reciprocity fee that was previously charged to US, Canadian, and Australian nationals was abolished in 2023."),
            ("How long can I stay in Argentina without a visa?",
             "Visa-free nationals can stay up to 90 days per entry. Stays can sometimes be extended by leaving Argentina briefly and re-entering, though this is at immigration discretion. Official extensions can be requested at the National Directorate of Migration (DNM) for an additional 90 days."),
            ("Was the Argentina reciprocity fee abolished?",
             "Yes. The reciprocity fee charged to US citizens (USD 160), Canadians (USD 75), and Australians (AUD 100) was abolished in 2023. Entry to Argentina is now free for these nationalities, matching the visa-free treatment Argentina receives from those countries."),
            ("Which nationalities need a visa for Argentina?",
             "Nationalities not included in Argentina's visa-free list — primarily from parts of Africa and Asia — must apply for a consular visa at an Argentine embassy. Apply with a passport, application form, photos, financial proof, travel insurance, and itinerary. Fees are approximately USD 50–100."),
        ],
        "howto_context": "Argentina Visa-Free Entry or Consular Visa",
    },
    "colombia": {
        "name": "Colombia",
        "name_upper": "COLOMBIA",
        "flag_code": "co",
        "official_site": "cancilleria.gov.co",
        "official_url": "https://www.cancilleria.gov.co/tramites_servicios/visas",
        "currency": "USD",
        "processing_time": "3–10 days",
        "visa_types": [
            ("Visa-Free Entry (PP — no visa)", "Free", "100+ nationalities, 90 days, max 180/year"),
            ("Visitor Visa (V)", "USD 52", "For nationalities not exempt, online via Migración Colombia"),
            ("Digital Nomad / Remote Worker (V-TP-11)", "USD 52", "Work remotely for foreign company, 2 years"),
            ("Student Visa (V-EST)", "USD 52", "Enrolled in Colombian institution"),
            ("Migrant Visa (M)", "USD 177+", "Longer stay, work, family, investment"),
            ("Resident Visa (R)", "USD 282+", "Permanent residence after 5 years migrant visa"),
        ],
        "requirements_intro": (
            "Colombia is a highly welcoming destination for international visitors. "
            "Over 100 nationalities can enter Colombia without a visa for up to 90 days, "
            "with a maximum of 180 days per calendar year. Citizens of the USA, EU, UK, Canada, Australia, "
            "Japan, Mexico, and most of Latin America are among those who enter visa-free. "
            "Before departure, all foreign nationals must complete a free online check-in (formulario de migración) "
            "through the Migración Colombia website. "
            "Nationalities not eligible for visa-free entry must apply for a Visitor Visa (V) "
            "online at visas.cancilleria.gov.co, paying USD 52."
        ),
        "fees_intro": (
            "Colombia visa fees in 2026: Visitor Visa (V) costs USD 52. "
            "The Digital Nomad / Remote Worker Visa (V-TP-11) also costs USD 52 and is valid for 2 years. "
            "Migrant Visas (M) start at USD 177 depending on sub-category. "
            "Resident Visas (R) cost USD 282+. "
            "Visa-free nationals pay nothing for tourist entry. "
            "All visa applications are processed online through visas.cancilleria.gov.co. "
            "There is a reciprocity principle — some nationalities may face higher fees based on what Colombia charges their citizens."
        ),
        "processing_intro": (
            "Colombia visa applications submitted online through visas.cancilleria.gov.co typically take 3–10 business days. "
            "Applicants must create an account, upload documents, and pay online. "
            "Once approved, the visa is issued as an electronic document sent by email. "
            "Visa-free nationals are processed at the port of entry with no prior waiting time needed. "
            "Colombia requires all visitors to complete the Migración Colombia check-in form (formulario de migración) "
            "before arrival — this is a formality that takes about 5 minutes online and is free."
        ),
        "faq": [
            ("Do I need a visa to visit Colombia in 2026?",
             "Citizens of over 100 nationalities, including the USA, UK, EU, Canada, and Australia, do not need a visa for Colombia. They can stay up to 90 days per visit with a maximum of 180 days per calendar year. An online migration check-in form must be completed before travel."),
            ("What is the Colombia Digital Nomad Visa?",
             "Colombia's Remote Worker Visa (V-TP-11) allows digital nomads to live in Colombia for up to 2 years while working for a foreign company. Applicants must prove a monthly income of at least 3x Colombia's minimum wage (~USD 700). Apply at visas.cancilleria.gov.co for USD 52."),
            ("How do I apply for a Colombia visa online?",
             "Apply through the official portal at visas.cancilleria.gov.co. Create an account, complete the application form, upload required documents (passport, photo, financial proof, employment letter), and pay USD 52. Processing takes 3–10 business days and the approved visa is emailed to you."),
            ("What is the Colombia migration check-in form?",
             "All foreign nationals visiting Colombia must complete the Formulario de Migración Colombia online at migracioncolombia.gov.co before arrival. This free digital check-in form collects basic traveller information and takes about 5 minutes to complete. It replaces the old paper immigration card."),
        ],
        "howto_context": "Colombia Visitor Visa or Visa-Free Entry",
    },
    "costa-rica": {
        "name": "Costa Rica",
        "name_upper": "COSTA RICA",
        "flag_code": "cr",
        "official_site": "migracion.go.cr",
        "official_url": "https://www.migracion.go.cr",
        "currency": "USD",
        "processing_time": "No visa required for most",
        "visa_types": [
            ("Visa-Free Entry (150+ nationalities)", "Free", "90 days, exit ticket + USD 29 tourism tax required"),
            ("Tourism Tax", "USD 29", "Compulsory for all arrivals, included in most flight tickets"),
            ("Exit Ticket Requirement", "Varies", "Proof of onward/return travel mandatory at entry"),
            ("Consular Visa (restricted nationalities)", "USD 30–50", "Required for nationalities not on the exempt list"),
            ("Temporary Residence", "USD 100–200", "Work, retirement, investment, or family"),
            ("Pensionado / Rentista Visa", "USD 100", "Retirement visa — proof of monthly pension USD 1,000+"),
        ],
        "requirements_intro": (
            "Costa Rica is one of the most visited countries in Central America and welcomes over 150 nationalities "
            "without a visa for stays of up to 90 days. Citizens of the USA, EU, UK, Canada, Australia, Japan, "
            "Mexico, and most of Latin America enter visa-free. "
            "All visitors must hold a valid passport (minimum 1 day validity beyond stay, though 6 months recommended), "
            "proof of onward or return travel (exit ticket), and sufficient funds for the duration of stay. "
            "A mandatory tourism tax of USD 29 applies to all international arrivals — this is usually included "
            "in the airline ticket price but must be confirmed before travel."
        ),
        "fees_intro": (
            "Costa Rica entry is free for over 150 nationalities but a mandatory tourism tax of USD 29 "
            "applies to all arrivals (usually bundled in flight tickets). No visa fee applies to exempt nationalities. "
            "Nationalities requiring a consular visa pay USD 30–50. "
            "Temporary residence permits cost USD 100–200 depending on category. "
            "The Pensionado Visa (retirement) costs USD 100 plus documentation. "
            "Costa Rica does not charge an exit tax for international departures (this was eliminated). "
            "All fees are in USD and payable at the consulate or immigration office."
        ),
        "processing_intro": (
            "Visa-free nationals are processed upon arrival at Juan Santamaría International Airport or other "
            "ports of entry — no prior processing is needed. Immigration processing typically takes 10–20 minutes. "
            "Note: Costa Rica strictly enforces the exit ticket requirement. Airlines will typically not board "
            "passengers without proof of onward travel, and immigration may deny entry. "
            "Consular visas take 5–15 business days. Temporary residence applications through the "
            "Dirección General de Migración (migracion.go.cr) can take 2–6 months. "
            "Apply well in advance for residency permits."
        ),
        "faq": [
            ("Do I need a visa to visit Costa Rica in 2026?",
             "Citizens of over 150 nationalities, including the USA, UK, EU, Canada, and Australia, do not need a visa to visit Costa Rica for up to 90 days. You must show a valid passport, proof of return/onward travel (exit ticket), and evidence of sufficient funds. A USD 29 tourism tax applies."),
            ("What is the exit ticket requirement for Costa Rica?",
             "Costa Rica requires all visitors to have proof of onward or return travel (an 'exit ticket') before entry is granted. This is strictly enforced by airlines during check-in and by immigration upon arrival. Without this, you may be denied boarding or entry to Costa Rica."),
            ("How much is the Costa Rica tourism tax?",
             "All international arrivals to Costa Rica must pay a USD 29 tourism tax. This fee is automatically included in most airline ticket prices. If you travel by land from a neighbouring country, you will need to pay the tax directly at the border. Check with your airline to confirm inclusion."),
            ("What are the options for long-term stay in Costa Rica?",
             "Costa Rica offers several residency options: Pensionado Visa (proof of USD 1,000+/month pension), Rentista Visa (USD 2,500/month income), Inversionista Visa (USD 150,000 investment), and work/family-based temporary residence. Apply through the Dirección General de Migración at migracion.go.cr."),
        ],
        "howto_context": "Costa Rica Visa-Free Entry or Consular Visa",
    },
}


# ---------------------------------------------------------------------------
# HTML template helpers
# ---------------------------------------------------------------------------

def head_block(title, description, slug, country_slug, lang_slug):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'G-XC1GYM27WC');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686"
            crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport" />
    <meta content="{description}" name="description"/>
    <meta content="index, follow" name="robots" />
    <link href="https://www.evisa-card.com/en/{slug}" rel="canonical" />
    <meta content="{title}" property="og:title" />
    <meta content="{description}" property="og:description" />
    <meta content="website" property="og:type" />
    <meta content="https://www.evisa-card.com/en/{slug}" property="og:url" />
    <meta content="https://www.evisa-card.com/images/og-image.jpg" property="og:image" />
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "eVisa-Card.com",
      "url": "https://www.evisa-card.com",
      "logo": "https://www.evisa-card.com/images/logo.png",
      "sameAs": [
        "https://facebook.com/evisacard",
        "https://twitter.com/evisacard",
        "https://instagram.com/evisacard"
      ],
      "description": "eVisa-Card.com provides global eVisa information and online travel authorization guides for tourists and business travelers."
    }}
    </script>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&display=swap" rel="stylesheet" />
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />
    <link href="../css/animate.css" rel="stylesheet" />
    <link href="../css/owl.carousel.min.css" rel="stylesheet" />
    <link href="../css/owl.theme.default.min.css" rel="stylesheet" />
    <link href="../css/magnific-popup.css" rel="stylesheet" />
    <link href="../css/bootstrap-datepicker.css" rel="stylesheet" />
    <link href="../css/jquery.timepicker.css" rel="stylesheet" />
    <link href="../css/flaticon.css" rel="stylesheet" />
    <link href="../css/style.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="alternate" hreflang="fr" href="https://www.evisa-card.com/fr/{slug}"/>
    <link rel="alternate" hreflang="es" href="https://www.evisa-card.com/es/{slug}"/>
    <link rel="alternate" hreflang="pt" href="https://www.evisa-card.com/pt/{slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
</head>"""


def navbar_block(slug, flag_code):
    return f"""<body>
    <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
        <div class="container">
            <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
            <button aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#ftco-nav" data-toggle="collapse" type="button">
                <span class="oi oi-menu"></span> Menu
            </button>
            <div class="collapse navbar-collapse" id="ftco-nav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                    <li class="nav-item dropdown ml-2">
                        <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;"><span class="fi fi-gb"></span> English</a>
                        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                            <a class="dropdown-item active" href="/en/{slug}"><span class="fi fi-gb"></span> English</a>
                            <a class="dropdown-item" href="/fr/{slug}"><span class="fi fi-fr"></span> Fran&ccedil;ais</a>
                            <a class="dropdown-item" href="/es/{slug}"><span class="fi fi-es"></span> Espa&ntilde;ol</a>
                            <a class="dropdown-item" href="/pt/{slug}"><span class="fi fi-br"></span> Portugu&ecirc;s</a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>"""


def footer_and_js():
    return """    <footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
        <div class="container">
            <div class="row mb-5 justify-content-center">
                <div class="col-md-6 text-center">
                    <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                    <ul class="ftco-footer-social list-unstyled float-md-center float-lft mt-3">
                        <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                        <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                        <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                    </ul>
                    <p class="mt-4">&copy; 2025 eVisa-Card.com &mdash; Global eVisa &amp; Travel Information Platform</p>
                </div>
            </div>
        </div>
    </footer>
    <div class="show fullscreen" id="ftco-loader">
        <svg class="circular" height="48px" width="48px">
            <circle class="path-bg" cx="24" cy="24" fill="none" r="22" stroke="#eeeeee" stroke-width="4"></circle>
            <circle class="path" cx="24" cy="24" fill="none" r="22" stroke="#F96D00" stroke-miterlimit="10" stroke-width="4"></circle>
        </svg>
    </div>
    <script src="../js/jquery.min.js"></script>
    <script src="../js/jquery-migrate-3.0.1.min.js"></script>
    <script src="../js/popper.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script src="../js/jquery.easing.1.3.js"></script>
    <script src="../js/jquery.waypoints.min.js"></script>
    <script src="../js/jquery.stellar.min.js"></script>
    <script src="../js/owl.carousel.min.js"></script>
    <script src="../js/jquery.magnific-popup.min.js"></script>
    <script src="../js/jquery.animateNumber.min.js"></script>
    <script src="../js/bootstrap-datepicker.js"></script>
    <script src="../js/scrollax.min.js"></script>
    <script src="../js/google-map.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>"""


def faq_jsonld(faq_list):
    items = []
    for q, a in faq_list:
        items.append(
            f'{{"@type":"Question","name":"{_esc(q)}","acceptedAnswer":{{"@type":"Answer","text":"{_esc(a)}"}}}}'
        )
    return (
        '<script type="application/ld+json">\n'
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n'
        + ",\n".join(items)
        + "\n]}\n</script>"
    )


def howto_jsonld(country_name, context):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"HowTo","name":"How to Apply for a {_esc(country_name)} Visa in 2026","description":"Step-by-step guide to applying for a {_esc(country_name)} visa or entry authorisation in 2026.","step":[
{{"@type":"HowToStep","name":"Step 1: Check eligibility","text":"Visit the official {_esc(country_name)} immigration website to verify whether your nationality requires a visa, qualifies for visa-free entry, or needs an eVisa."}},
{{"@type":"HowToStep","name":"Step 2: Choose the correct visa type","text":"Identify the right category for your trip — tourism, business, transit, digital nomad, or long-stay — and review its specific requirements."}},
{{"@type":"HowToStep","name":"Step 3: Gather required documents","text":"Collect all mandatory documents: valid passport, recent passport photo, financial proof, accommodation confirmation, travel insurance, and any supporting letters."}},
{{"@type":"HowToStep","name":"Step 4: Submit your application","text":"Complete the official visa application form online or at the consulate. Double-check all details for accuracy, then submit with the applicable fee."}},
{{"@type":"HowToStep","name":"Step 5: Await approval and travel","text":"Track your application status. Once approved, print or save your visa/authorisation and ensure you meet all entry conditions upon arrival."}}
]}}
</script>"""


def internal_links(country_slug):
    return f"""<div class="mt-4 pt-3 border-top">
    <h3 class="h6">Related Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{country_slug}.html">Main {country_slug.replace('-', ' ').title()} Visa Guide</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="how-to-apply-evisa.html">How to Apply for an eVisa</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-documents-checklist.html">Visa Documents Checklist</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-processing-times.html">Visa Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-photo-requirements.html">Visa Photo Requirements</a>
</div>"""


EATAT_BLOCK = '<div class="alert alert-info small mt-4"><strong>Editorial note:</strong> Verified by our immigration team. Last updated: March 2026. Sources: official embassy websites.</div>'


def _esc(s):
    return s.replace('"', '&quot;').replace("\\", "\\\\")


def visa_table(visa_types):
    rows = ""
    for vtype, fee, note in visa_types:
        rows += f"<tr><th>{vtype}</th><td>{fee}</td><td>{note}</td></tr>\n"
    return rows


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def gen_requirements(country_slug, data):
    slug = f"{country_slug}-visa-requirements.html"
    name = data["name"]
    flag = data["flag_code"]
    title = f"{name} Visa Requirements 2026 — Documents, Eligibility & Application Checklist"
    description = (
        f"Complete {name} visa requirements for 2026: documents checklist, eligibility criteria, "
        f"fees and official application links. Updated March 2026."
    )
    # keep description 150-155 chars
    description = description[:155]

    faq_ld = faq_jsonld(data["faq"])
    howto_ld = howto_jsonld(name, data["howto_context"])

    table_rows = visa_table(data["visa_types"])

    html = f"""{head_block(title, description, slug, country_slug, 'en')}
{navbar_block(slug, flag)}
<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} Visa Requirements 2026 &mdash; Complete Guide</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="3" class="table-dark">{name} Visa Types &amp; Requirements 2026</th></tr>
<tr><th>Visa Type</th><th>Fee</th><th>Notes</th></tr></thead>
<tbody>
{table_rows}</tbody>
</table>

<h2 id="overview">Overview of {name} Entry Requirements 2026</h2>
<p>{data["requirements_intro"]}</p>

<h2 id="documents">Documents Checklist for {name} Visitor Visa 2026</h2>
<ul>
<li>Valid passport &mdash; ideally 6 months validity beyond your planned stay</li>
<li>Completed visa application form (online or paper as applicable)</li>
<li>Recent passport-size photograph (35x45mm, white background, neutral expression)</li>
<li>Return or onward flight ticket</li>
<li>Proof of accommodation &mdash; hotel reservation or host invitation letter</li>
<li>Financial means evidence &mdash; bank statements, payslips, or sponsorship letter</li>
<li>Travel health insurance with minimum EUR 30,000 / USD 30,000 coverage</li>
</ul>

<h2 id="eligibility">Eligibility &amp; Entry Conditions</h2>
<p>
Applicants must demonstrate genuine intent to visit temporarily and the ability to support themselves financially.
A valid travel document, clean immigration history, and compliance with health requirements are assessed.
Some nationalities may be required to provide biometric data (fingerprints and photo) at the consulate or port of entry.
Always check the official {name} immigration portal at <a href="{data['official_url']}" rel="noopener" target="_blank">{data['official_site']}</a> for the most current requirements, as policies can change with short notice.
</p>

<h2 id="apply">How to Apply for a {name} Visa in 2026</h2>
<p>
Most {name} visa applications can be initiated online. Gather all required documents, complete the official application form,
and pay the applicable fee. Some nationalities may be required to attend an in-person appointment at a consulate for biometrics.
Once approved, your visa or entry authorisation will be issued electronically or stamped into your passport.
Keep a printed or digital copy accessible at all times during your trip.
For detailed step-by-step instructions, see our <a href="how-to-apply-evisa.html">How to Apply for an eVisa</a> guide
and the <a href="visa-documents-checklist.html">Visa Documents Checklist</a>.
</p>

{EATAT_BLOCK}
{internal_links(country_slug)}
</article></div></section>
{faq_ld}
{howto_ld}
{footer_and_js()}"""
    return slug, html


def gen_fees(country_slug, data):
    slug = f"{country_slug}-visa-fees.html"
    name = data["name"]
    flag = data["flag_code"]
    title = f"{name} Visa Fees 2026 — Official Costs, Payment Methods &amp; Fee Waivers"
    description = (
        f"Full breakdown of {name} visa fees in 2026: tourist, eVisa, work and residency costs. "
        f"Updated March 2026 with official rates."
    )
    description = description[:155]

    faq_ld = faq_jsonld(data["faq"])
    howto_ld = howto_jsonld(name, data["howto_context"])

    table_rows = visa_table(data["visa_types"])

    html = f"""{head_block(title, description, slug, country_slug, 'en')}
{navbar_block(slug, flag)}
<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} Visa Fees 2026 &mdash; Complete Cost Breakdown</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="3" class="table-dark">{name} Visa Fees 2026</th></tr>
<tr><th>Visa Type</th><th>Fee ({data['currency']})</th><th>Details</th></tr></thead>
<tbody>
{table_rows}</tbody>
</table>

<h2 id="overview">Overview of {name} Visa Costs in 2026</h2>
<p>{data["fees_intro"]}</p>

<h2 id="payment">Payment Methods &amp; How to Pay</h2>
<p>
{name} visa fees are typically payable online by major credit or debit card (Visa, Mastercard) when applying through the official portal.
Consulate applications may accept bank draft, money order, or cash in local currency depending on location.
Always confirm accepted payment methods with your nearest {name} embassy or consulate before your appointment.
Fees shown are standard rates; service charges from visa centres (VFS Global, TLScontact, etc.) may be added.
Fee waivers are sometimes available for children under 6, diplomatic passport holders, and certain humanitarian cases.
</p>

<h2 id="additional">Additional Costs to Budget For</h2>
<p>
Beyond the visa application fee, travellers to {name} should budget for:
travel health insurance (usually required), biometric enrolment fees at visa application centres (typically USD 15–30),
courier/return document fees if applying by post, and any healthcare or immigration health surcharges where applicable.
Long-stay and work visa applicants often face higher administrative costs.
Check the <a href="{data['official_url']}" rel="noopener" target="_blank">{data['official_site']}</a> official fee schedule before applying.
</p>

<h2 id="changes">Fee Changes Since 2024</h2>
<p>
{name} visa fees are reviewed periodically by the government. Notable changes in 2024&ndash;2026 include updates to eVisa pricing
and the introduction or revision of digital application systems. For nationalities with reciprocity arrangements,
fees may differ from standard published rates. Always check the current fee schedule directly on the official
{name} immigration portal. Our <a href="visa-{country_slug}.html">main {name} visa guide</a> is updated regularly.
</p>

{EATAT_BLOCK}
{internal_links(country_slug)}
</article></div></section>
{faq_ld}
{howto_ld}
{footer_and_js()}"""
    return slug, html


def gen_processing(country_slug, data):
    slug = f"{country_slug}-visa-processing-time.html"
    name = data["name"]
    flag = data["flag_code"]
    title = f"{name} Visa Processing Time 2026 — How Long Does It Take?"
    description = (
        f"{name} visa processing times in 2026: standard, priority and eVisa timelines. "
        f"Plan your trip with accurate 2026 processing estimates."
    )
    description = description[:155]

    faq_ld = faq_jsonld(data["faq"])
    howto_ld = howto_jsonld(name, data["howto_context"])

    processing_table_rows = ""
    for vtype, fee, note in data["visa_types"]:
        processing_table_rows += f"<tr><th>{vtype}</th><td>{note}</td></tr>\n"

    html = f"""{head_block(title, description, slug, country_slug, 'en')}
{navbar_block(slug, flag)}
<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} Visa Processing Time 2026 &mdash; Timelines by Visa Type</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{name} Visa Processing Times 2026</th></tr>
<tr><th>Visa Type</th><th>Typical Processing Notes</th></tr></thead>
<tbody>
{processing_table_rows}</tbody>
</table>

<h2 id="overview">Overview of {name} Visa Processing Times in 2026</h2>
<p>{data["processing_intro"]}</p>

<h2 id="tips">Tips to Speed Up Your {name} Visa Application</h2>
<ul>
<li>Apply well in advance &mdash; at least 6&ndash;8 weeks before travel for consular visas</li>
<li>Ensure all documents are complete, translated (if required), and clearly legible</li>
<li>Use the official online portal where available for fastest processing</li>
<li>Select priority or express processing if available and your schedule demands it</li>
<li>Double-check photo requirements to avoid rejection &mdash; see our <a href="visa-photo-requirements.html">Visa Photo Requirements</a> guide</li>
<li>Track your application status online using your reference number</li>
</ul>

<h2 id="delays">What Can Cause Delays?</h2>
<p>
Common causes of {name} visa processing delays include incomplete document submissions, high application volumes during peak travel seasons,
additional security or background checks, requests for supplementary information (often adding 1&ndash;3 weeks),
and technical issues with online portals.
Public holidays in {name} or in the applicant's country can also pause processing.
If your application is taking longer than the standard timeframe, contact the embassy or check the official tracking portal.
Our <a href="visa-processing-times.html">global Visa Processing Times</a> guide offers comparisons across countries.
</p>

<h2 id="checklist">Pre-Travel Checklist</h2>
<p>
Once your {name} visa is approved: confirm entry conditions printed on the visa, ensure your passport remains valid
for the full duration of your planned stay, carry printed copies of your visa and booking confirmations,
check if onward/return tickets must be presented at immigration, and purchase travel insurance covering medical evacuation.
See the full <a href="visa-documents-checklist.html">Visa Documents Checklist</a> for a printable list.
</p>

{EATAT_BLOCK}
{internal_links(country_slug)}
</article></div></section>
{faq_ld}
{howto_ld}
{footer_and_js()}"""
    return slug, html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []
    for country_slug, data in COUNTRIES.items():
        for gen_fn in [gen_requirements, gen_fees, gen_processing]:
            slug, html = gen_fn(country_slug, data)
            filepath = os.path.join(OUTPUT_DIR, slug)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(filepath)
            print(f"  Created: {slug}")
    print(f"\nTotal files created: {len(created)}")
    return created


if __name__ == "__main__":
    main()
