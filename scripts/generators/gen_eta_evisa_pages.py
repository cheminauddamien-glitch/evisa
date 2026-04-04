#!/usr/bin/env python3
"""
gen_eta_evisa_pages.py
Generates 14 dedicated ETA / eVisa HTML pages in www/en/.
Run from the pacific-main directory.
"""

import os, json, textwrap

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "en")

LANGUAGES = [
    ("en", "gb", "English"),
    ("fr", "fr", "Francais"),
    ("es", "es", "Espanol"),
    ("pt", "br", "Portugues"),
    ("zh", "cn", "Chinese"),
    ("th", "th", "Thai"),
    ("ru", "ru", "Russian"),
    ("ar", "sa", "Arabic"),
    ("ja", "jp", "Japanese"),
    ("ko", "kr", "Korean"),
]

BG_IMAGES = ["bg_1.jpg", "bg_2.jpg", "bg_3.jpg", "bg_4.jpg", "bg_5.jpg"]

# ---------------------------------------------------------------------------
# Page definitions
# ---------------------------------------------------------------------------
PAGES = [
    # 1  Australia ETA
    {
        "filename": "australia-eta.html",
        "title": "Australia ETA (Electronic Travel Authority) Subclass 601 — Apply Online 2026",
        "meta_desc": "Apply for the Australia ETA (subclass 601) online. AUD 20 fee, instant to 72-hour processing, 90-day stays for tourism or business.",
        "h1": "Australia ETA — Electronic Travel Authority (Subclass 601)",
        "bg_idx": 0,
        "intro": (
            "The Australia Electronic Travel Authority (ETA, subclass 601) is a digital visa that allows eligible passport holders to visit Australia for tourism or business for up to 90 days per visit. "
            "The ETA costs AUD 20 and is processed instantly in most cases, though some applications may take up to 72 hours. "
            "It is valid for 12 months and permits multiple entries."
        ),
        "key_facts": [
            ("Visa Type", "Electronic Travel Authority (ETA) — Subclass 601"),
            ("Cost", "AUD 20 (approx. USD 13)"),
            ("Validity", "12 months, multiple entry, up to 90 days per visit"),
            ("Processing Time", "Instant to 72 hours"),
            ("Official Website", '<a href="https://www.eta.homeaffairs.gov.au" target="_blank" rel="noopener">eta.homeaffairs.gov.au</a>'),
        ],
        "who_needs": (
            "Citizens of eligible countries including the United States, Canada, United Kingdom, Japan, South Korea, Singapore, Malaysia, Brunei, and most EU/EEA nations can apply for the ETA. "
            "Passport holders from countries not eligible for the ETA may apply for the eVisitor (subclass 651) or a standard Visitor visa (subclass 600)."
        ),
        "application_steps": [
            "Download the Australian ETA app from the App Store or Google Play.",
            "Create an account and scan your passport using your phone's NFC reader.",
            "Fill in personal and travel details including planned dates and accommodation.",
            "Pay the AUD 20 application fee via credit or debit card.",
            "Receive your ETA confirmation — most approvals are instant.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Smartphone with NFC capability for passport scanning",
            "Credit or debit card for payment",
            "Email address for confirmation receipt",
            "Travel itinerary (dates, accommodation details)",
        ],
        "related_links": [
            ("visa-australia.html", "Australia Visa Requirements"),
            ("australia-visa-fees.html", "Australia Visa Fees"),
            ("australia-visa-extension.html", "Australia Visa Extension"),
            ("australia-visa-requirements.html", "Australia Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Australia ETA subclass 601?", "The Australia ETA (Electronic Travel Authority) subclass 601 is a digital travel permit that allows eligible passport holders to visit Australia for tourism or business purposes for up to 90 days per visit. It is valid for 12 months and permits multiple entries."),
            ("How much does the Australia ETA cost?", "The Australia ETA costs AUD 20, which is approximately USD 13. The fee is paid online during the application process through the official Australian ETA app."),
            ("How long does the Australia ETA take to process?", "Most Australia ETA applications are processed instantly. However, some applications may take up to 72 hours if additional checks are required."),
            ("Can I work on an Australia ETA?", "No, the Australia ETA subclass 601 does not permit work. It is only valid for tourism, visiting family and friends, or short-term business activities such as attending meetings or conferences."),
            ("Which countries are eligible for the Australia ETA?", "Eligible countries include the United States, Canada, Japan, South Korea, Singapore, Malaysia, Brunei, Hong Kong SAR, and several other passport holders. EU/EEA citizens typically apply for the eVisitor (subclass 651) instead."),
        ],
    },

    # 2  Sri Lanka ETA
    {
        "filename": "sri-lanka-eta.html",
        "title": "Sri Lanka ETA (Electronic Travel Authorization) — Online Application 2026",
        "meta_desc": "Apply for Sri Lanka ETA online. USD 50 for tourism, 30 days stay, double entry permitted. Fast processing for over 100 nationalities.",
        "h1": "Sri Lanka ETA — Electronic Travel Authorization",
        "bg_idx": 1,
        "intro": (
            "The Sri Lanka Electronic Travel Authorization (ETA) is an official entry permit required for most foreign nationals visiting Sri Lanka for tourism, business, or transit. "
            "The tourism ETA costs USD 50, allows a 30-day stay with double entry, and can be extended up to 90 days once in Sri Lanka. "
            "Applications are processed online and approval is typically granted within 24 hours."
        ),
        "key_facts": [
            ("Visa Type", "Electronic Travel Authorization (ETA)"),
            ("Cost", "USD 50 (tourism), USD 50 (business), USD 0 (transit up to 2 days)"),
            ("Validity", "30 days, double entry (extendable to 90 days)"),
            ("Processing Time", "24 hours (standard), 1 hour (urgent)"),
            ("Official Website", '<a href="https://www.eta.gov.lk" target="_blank" rel="noopener">eta.gov.lk</a>'),
        ],
        "who_needs": (
            "Citizens of most countries require an ETA to enter Sri Lanka. Nationals of Singapore, the Maldives, and the Seychelles are exempt. "
            "Travelers from over 100 countries can apply online. Citizens of countries not eligible for the online system must apply through a Sri Lankan embassy or consulate."
        ),
        "application_steps": [
            "Visit the official Sri Lanka ETA website at eta.gov.lk.",
            "Select your visa category: Tourist, Business, or Transit.",
            "Complete the application form with personal and passport details.",
            "Pay the ETA fee using Visa, MasterCard, or American Express.",
            "Receive your ETA approval notice via email within 24 hours.",
            "Print the approval notice and present it upon arrival in Sri Lanka.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Return or onward flight ticket",
            "Proof of sufficient funds for the stay",
            "Hotel reservation or accommodation address in Sri Lanka",
            "Credit or debit card for online payment",
        ],
        "related_links": [
            ("visa-sri-lanka.html", "Sri Lanka Visa Requirements"),
            ("sri-lanka-visa-fees.html", "Sri Lanka Visa Fees"),
            ("sri-lanka-visa-extension.html", "Sri Lanka Visa Extension"),
            ("sri-lanka-visa-requirements.html", "Sri Lanka Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Sri Lanka ETA?", "The Sri Lanka ETA (Electronic Travel Authorization) is an online entry permit required for most foreign nationals. It allows stays of up to 30 days for tourism or business and can be extended up to 90 days at the Department of Immigration in Colombo."),
            ("How much does the Sri Lanka ETA cost?", "The Sri Lanka ETA costs USD 50 for both tourism and business categories. Transit ETAs (stays up to 2 days) are free of charge. Fees are paid online during the application."),
            ("Can I extend my Sri Lanka ETA?", "Yes, the Sri Lanka ETA can be extended from 30 days to 90 days by visiting the Department of Immigration and Emigration in Colombo before your initial ETA expires."),
            ("How long does Sri Lanka ETA processing take?", "Standard processing takes up to 24 hours. Urgent processing is available for an additional fee and can deliver approval within 1 hour."),
        ],
    },

    # 3  India e-Visa
    {
        "filename": "india-evisa.html",
        "title": "India e-Visa — Tourist, Business & Medical eVisa Application 2026",
        "meta_desc": "Apply for India e-Visa online. USD 25-80, available in 5 categories: tourist, business, medical, conference, and yoga. 30 to 365-day validity.",
        "h1": "India e-Visa — Tourist, Business, Medical, Conference & Yoga",
        "bg_idx": 2,
        "intro": (
            "The India e-Visa is an electronic visa available to citizens of over 165 countries for visiting India. "
            "It comes in five categories — eTourist, eBusiness, eMedical, eConference, and eYoga — with fees ranging from USD 25 to USD 80. "
            "Validity ranges from 30 days (single or double entry) up to 1 year or 5 years with multiple entry, depending on the category and nationality."
        ),
        "key_facts": [
            ("Visa Type", "e-Visa (eTourist, eBusiness, eMedical, eConference, eYoga)"),
            ("Cost", "USD 25 (30-day), USD 40 (1-year), USD 80 (5-year) — varies by nationality"),
            ("Validity", "30 days / 1 year / 5 years depending on category"),
            ("Processing Time", "3-5 business days"),
            ("Official Website", '<a href="https://indianvisaonline.gov.in" target="_blank" rel="noopener">indianvisaonline.gov.in</a>'),
        ],
        "who_needs": (
            "Citizens of over 165 countries are eligible for the India e-Visa. Notable exceptions include Pakistan, Afghanistan, and a few other countries whose nationals must apply through Indian embassies. "
            "The e-Visa allows entry through 28 designated airports and 5 seaports in India."
        ),
        "application_steps": [
            "Visit the official India e-Visa portal at indianvisaonline.gov.in.",
            "Select the appropriate e-Visa category (Tourist, Business, Medical, Conference, or Yoga).",
            "Fill in the detailed application form with personal, passport, and travel information.",
            "Upload a recent passport-size photograph and a scan of your passport's bio page.",
            "Pay the e-Visa fee online using a credit/debit card, PayPal, or other accepted methods.",
            "Receive your e-Visa (ETA) via email within 3-5 business days.",
            "Print the e-Visa and carry it when traveling to India.",
        ],
        "documents": [
            "Valid passport with at least 6 months validity and 2 blank pages",
            "Recent passport-size color photograph (white background, 2x2 inches)",
            "Scanned copy of passport bio page (PDF or JPEG)",
            "Return or onward flight ticket",
            "Proof of accommodation in India",
            "Proof of sufficient funds",
            "Business letter (for eBusiness) or hospital letter (for eMedical) if applicable",
        ],
        "related_links": [
            ("visa-india.html", "India Visa Requirements"),
            ("india-visa-fees.html", "India Visa Fees"),
            ("india-visa-extension.html", "India Visa Extension"),
            ("india-visa-requirements.html", "India Visa Application Guide"),
        ],
        "faqs": [
            ("What are the India e-Visa categories?", "India offers five e-Visa categories: eTourist Visa for tourism and sightseeing, eBusiness Visa for business activities, eMedical Visa for medical treatment, eConference Visa for attending conferences organized by the Government of India, and eYoga Visa for participating in yoga programs."),
            ("How much does the India e-Visa cost?", "The India e-Visa costs USD 25 for a 30-day visa, USD 40 for a 1-year visa, and USD 80 for a 5-year visa. Fees vary by nationality and some countries receive fee waivers or discounts."),
            ("How long can I stay in India on an e-Visa?", "The 30-day eTourist Visa allows a continuous stay of 30 days with double entry. The 1-year and 5-year eTourist Visas allow stays of up to 90 days per visit (180 days for US, UK, Canada, and Japan citizens) with multiple entries."),
            ("Can I extend my India e-Visa?", "No, the India e-Visa cannot be extended or converted to another visa type while in India. You must apply for a new visa if you wish to stay longer than the permitted duration."),
            ("Which airports accept the India e-Visa?", "The India e-Visa is accepted at 28 designated airports including Delhi, Mumbai, Chennai, Kolkata, Bengaluru, Hyderabad, Goa, and Cochin, as well as 5 seaports including Mumbai, Goa, Mangalore, Chennai, and Cochin."),
        ],
    },

    # 4  Indonesia eVOA
    {
        "filename": "indonesia-evoa.html",
        "title": "Indonesia eVOA (Electronic Visa on Arrival) — Online Application 2026",
        "meta_desc": "Apply for Indonesia eVOA online before your trip. IDR 500,000 (~USD 32), 30 days extendable, via the official Molina immigration portal.",
        "h1": "Indonesia eVOA — Electronic Visa on Arrival",
        "bg_idx": 3,
        "intro": (
            "The Indonesia eVOA (Electronic Visa on Arrival) allows eligible travelers to obtain their visa online before arriving in Indonesia, skipping the on-arrival queue. "
            "The eVOA costs IDR 500,000 (approximately USD 32), is valid for 30 days with single entry, and can be extended once for an additional 30 days. "
            "It is available for citizens of over 90 countries and can be applied for through the official Molina immigration portal."
        ),
        "key_facts": [
            ("Visa Type", "Electronic Visa on Arrival (eVOA)"),
            ("Cost", "IDR 500,000 (approx. USD 32)"),
            ("Validity", "30 days, single entry (extendable once for 30 more days)"),
            ("Processing Time", "Up to 48 hours (usually within a few hours)"),
            ("Official Website", '<a href="https://molina.imigrasi.go.id" target="_blank" rel="noopener">molina.imigrasi.go.id</a>'),
        ],
        "who_needs": (
            "Citizens of over 90 countries are eligible for the Indonesia eVOA, including nationals of the United States, United Kingdom, Australia, Canada, most EU countries, Japan, South Korea, and many others. "
            "Some ASEAN nationals can enter Indonesia visa-free for 30 days and do not need the eVOA."
        ),
        "application_steps": [
            "Visit the official Molina portal at molina.imigrasi.go.id.",
            "Create an account and select 'Visa on Arrival' as the visa type.",
            "Fill in the application form with your personal, passport, and travel details.",
            "Upload your passport photo and a passport bio page scan.",
            "Pay the IDR 500,000 fee via credit card or other accepted payment method.",
            "Receive your eVOA approval via email — print or save the QR code.",
            "Present the QR code at the designated eVOA counter upon arrival at an Indonesian airport.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Passport-size color photograph",
            "Scanned passport bio page",
            "Return or onward flight ticket",
            "Proof of accommodation in Indonesia",
            "Credit or debit card for payment",
        ],
        "related_links": [
            ("visa-indonesia.html", "Indonesia Visa Requirements"),
            ("indonesia-visa-fees.html", "Indonesia Visa Fees"),
            ("indonesia-visa-extension.html", "Indonesia Visa Extension"),
            ("indonesia-visa-requirements.html", "Indonesia Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Indonesia eVOA?", "The Indonesia eVOA (Electronic Visa on Arrival) is an online version of the traditional Visa on Arrival. It allows eligible travelers to apply and pay for their visa before arriving in Indonesia, saving time at the airport by skipping the VOA queue."),
            ("How much does the Indonesia eVOA cost?", "The Indonesia eVOA costs IDR 500,000, which is approximately USD 32. This is the same price as the traditional Visa on Arrival but with the convenience of applying online before travel."),
            ("Can I extend the Indonesia eVOA?", "Yes, the Indonesia eVOA can be extended once for an additional 30 days at a local immigration office in Indonesia. The extension must be applied for before your initial 30-day visa expires."),
            ("What is the difference between the eVOA and the traditional VOA?", "The eVOA and the traditional VOA are essentially the same visa with the same cost and validity. The only difference is that the eVOA is obtained online before travel, while the traditional VOA is obtained upon arrival at the airport, which may involve longer queues."),
        ],
    },

    # 5  Thailand e-Visa
    {
        "filename": "thailand-evisa.html",
        "title": "Thailand e-Visa — Tourist, Transit & Non-Immigrant Visa Application 2026",
        "meta_desc": "Apply for a Thailand e-Visa online. THB 2,000 for tourist visa, multiple categories including transit and non-immigrant visas. Fast electronic processing.",
        "h1": "Thailand e-Visa — Tourist, Transit & Non-Immigrant Visa",
        "bg_idx": 4,
        "intro": (
            "The Thailand e-Visa system allows travelers to apply online for Thai visas through the official Thai e-Visa portal, eliminating the need to visit a consulate in person. "
            "The Tourist e-Visa (TR) costs THB 2,000 (approximately USD 57) and permits a 60-day stay with single entry. "
            "Other categories include Transit, Non-Immigrant B (business), Non-Immigrant O (family visit), and Non-Immigrant ED (education)."
        ),
        "key_facts": [
            ("Visa Type", "e-Visa (Tourist TR, Transit TS, Non-Immigrant B/O/ED)"),
            ("Cost", "THB 2,000 (Tourist), THB 800 (Transit), THB 5,000+ (Non-Immigrant)"),
            ("Validity", "60 days (Tourist), 30 days (Transit), 90 days (Non-Immigrant)"),
            ("Processing Time", "5-10 business days"),
            ("Official Website", '<a href="https://www.thaievisa.go.th" target="_blank" rel="noopener">thaievisa.go.th</a>'),
        ],
        "who_needs": (
            "Citizens of many countries can enter Thailand visa-free for 30 or 60 days depending on nationality. "
            "Travelers who wish to stay longer or who are not eligible for visa exemption must apply for an e-Visa. "
            "The e-Visa is available for applicants residing in countries where a Thai embassy or consulate provides the online service."
        ),
        "application_steps": [
            "Visit the official Thai e-Visa portal at thaievisa.go.th.",
            "Create an account and select the visa type you need (Tourist, Transit, or Non-Immigrant).",
            "Fill in the application form with personal, passport, and travel details.",
            "Upload required documents including passport photo, passport bio page, flight itinerary, and accommodation proof.",
            "Pay the visa fee via credit or debit card.",
            "Attend a consulate appointment if required (some embassies waive this step).",
            "Receive your e-Visa approval via email and the e-Visa is electronically linked to your passport.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity and at least 1 blank page",
            "Recent passport-size photograph (4x6 cm, white background)",
            "Confirmed flight itinerary (round trip)",
            "Proof of accommodation (hotel booking or invitation letter)",
            "Proof of financial means (bank statement, minimum THB 20,000 for tourist visa)",
            "Travel insurance covering the duration of stay",
        ],
        "related_links": [
            ("visa-thailand.html", "Thailand Visa Requirements"),
            ("thailand-visa-fees.html", "Thailand Visa Fees"),
            ("thailand-visa-extension.html", "Thailand Visa Extension"),
            ("thailand-visa-requirements.html", "Thailand Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Thailand e-Visa?", "The Thailand e-Visa is an electronic visa application system that allows travelers to apply for Thai visas online through the official thaievisa.go.th portal, rather than visiting a Thai embassy or consulate in person."),
            ("How much does the Thailand Tourist e-Visa cost?", "The Thailand Tourist e-Visa (TR category) costs THB 2,000, approximately USD 57. Transit visas cost THB 800, and Non-Immigrant visas start from THB 5,000 depending on the category."),
            ("How long can I stay in Thailand with a Tourist e-Visa?", "The Thailand Tourist e-Visa allows a stay of up to 60 days. It can be extended once at a Thai Immigration office for an additional 30 days, giving a maximum stay of 90 days."),
            ("Do I still need to visit the embassy for the Thailand e-Visa?", "In most cases, the Thailand e-Visa process is entirely online. However, some Thai embassies may require applicants to submit their passport in person or attend a brief appointment after the online application is approved."),
        ],
    },

    # 6  Vietnam e-Visa
    {
        "filename": "vietnam-evisa.html",
        "title": "Vietnam e-Visa — Online Application for 80+ Countries 2026",
        "meta_desc": "Apply for Vietnam e-Visa online. USD 25, 30 days single entry, available for citizens of 80+ countries. Fast 3-day processing via the official portal.",
        "h1": "Vietnam e-Visa — Electronic Visa for 80+ Countries",
        "bg_idx": 0,
        "intro": (
            "The Vietnam e-Visa is an electronic visa that allows citizens of over 80 countries to enter Vietnam for tourism or business purposes without visiting an embassy. "
            "It costs USD 25, is valid for 30 days with single entry, and is processed within 3 business days. "
            "The e-Visa is accepted at all international airports, land border crossings, and seaports in Vietnam."
        ),
        "key_facts": [
            ("Visa Type", "e-Visa (Electronic Visa)"),
            ("Cost", "USD 25"),
            ("Validity", "30 days, single entry"),
            ("Processing Time", "3 business days"),
            ("Official Website", '<a href="https://evisa.xuatnhapcanh.gov.vn" target="_blank" rel="noopener">evisa.xuatnhapcanh.gov.vn</a>'),
        ],
        "who_needs": (
            "Citizens of over 80 countries are eligible for the Vietnam e-Visa, including nationals of the United States, United Kingdom, Canada, Australia, France, Germany, Japan, South Korea, and many others. "
            "Some countries such as those in ASEAN may enter visa-free for 14 to 30 days. Travelers who require longer stays or multiple entries should consider a traditional visa from a Vietnamese embassy."
        ),
        "application_steps": [
            "Visit the official Vietnam e-Visa website at evisa.xuatnhapcanh.gov.vn.",
            "Click 'Apply for e-Visa' and fill in the online application form.",
            "Upload a recent 4x6 cm passport-size photograph and a scan of your passport data page.",
            "Pay the USD 25 e-Visa fee via credit card, debit card, or other accepted payment methods.",
            "Receive your e-Visa approval via email within 3 business days.",
            "Print two copies of the e-Visa approval letter and present one at immigration upon arrival.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Recent passport-size photograph (4x6 cm, white background, without glasses)",
            "Scanned copy of passport data page",
            "Credit or debit card for the USD 25 fee",
            "Email address for receiving the approval letter",
        ],
        "related_links": [
            ("visa-vietnam.html", "Vietnam Visa Requirements"),
            ("vietnam-visa-fees.html", "Vietnam Visa Fees"),
            ("vietnam-visa-extension.html", "Vietnam Visa Extension"),
            ("vietnam-visa-requirements.html", "Vietnam Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Vietnam e-Visa?", "The Vietnam e-Visa is an electronic visa issued by the Vietnam Immigration Department that allows eligible foreign nationals to enter Vietnam for up to 30 days. It is a single-entry visa and can be used for tourism, business, and other approved purposes."),
            ("How much does the Vietnam e-Visa cost?", "The Vietnam e-Visa costs USD 25 per application. This is a non-refundable fee that must be paid online during the application process."),
            ("How long does the Vietnam e-Visa take to process?", "The Vietnam e-Visa typically takes 3 business days to process. Applicants are advised to apply at least one week before their intended travel date to allow for any delays."),
            ("Can I extend the Vietnam e-Visa?", "The Vietnam e-Visa itself cannot be directly extended. However, once in Vietnam, you may be able to apply for a visa extension through a local travel agency or the Immigration Department, subject to approval and additional fees."),
            ("Which entry points accept the Vietnam e-Visa?", "The Vietnam e-Visa is accepted at all international airports (including Hanoi, Ho Chi Minh City, Da Nang), major land border crossings, and designated seaports throughout Vietnam."),
        ],
    },

    # 7  Nepal e-Visa
    {
        "filename": "nepal-evisa.html",
        "title": "Nepal e-Visa — Online Visa Application for Tourism 2026",
        "meta_desc": "Apply for a Nepal e-Visa online. USD 30/50/125 for 15/30/90 days. Apply at the official immigration.gov.np portal before traveling to Nepal.",
        "h1": "Nepal e-Visa — Online Tourist Visa Application",
        "bg_idx": 1,
        "intro": (
            "The Nepal e-Visa allows tourists to apply for their Nepalese visa online before traveling, reducing wait times at Tribhuvan International Airport in Kathmandu. "
            "Fees are USD 30 for 15 days, USD 50 for 30 days, and USD 125 for 90 days, with multiple entry permitted. "
            "The online application pre-fills your details so you only need to submit biometrics and payment upon arrival."
        ),
        "key_facts": [
            ("Visa Type", "Tourist Visa (online pre-application)"),
            ("Cost", "USD 30 (15 days), USD 50 (30 days), USD 125 (90 days)"),
            ("Validity", "15 / 30 / 90 days, multiple entry"),
            ("Processing Time", "Online form completed instantly; visa issued on arrival"),
            ("Official Website", '<a href="https://immigration.gov.np" target="_blank" rel="noopener">immigration.gov.np</a>'),
        ],
        "who_needs": (
            "Almost all foreign nationals require a visa to enter Nepal. Citizens of India can enter visa-free. "
            "Nationals of most other countries can obtain a visa on arrival at Kathmandu airport or land borders, but the online pre-application speeds up the process significantly. "
            "Citizens of Nigeria, Ghana, Zimbabwe, Swaziland, Cameroon, Somalia, Liberia, Ethiopia, Iraq, Palestine, and Afghanistan must obtain a visa from a Nepalese embassy before travel."
        ),
        "application_steps": [
            "Visit the official Nepal Department of Immigration website at immigration.gov.np.",
            "Click on 'Apply Online' and fill in the application form with personal and passport details.",
            "Upload a recent passport-size photograph.",
            "Select the visa duration: 15, 30, or 90 days.",
            "Submit the form and receive a confirmation receipt with a barcode.",
            "Print the receipt and present it at the immigration counter upon arrival in Nepal.",
            "Pay the visa fee in cash (USD or equivalent) and provide biometrics at the arrival counter.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Recent passport-size photograph (digital for online upload, physical for arrival)",
            "Printed confirmation receipt from the online application",
            "Cash (USD or equivalent) for visa fee payment on arrival",
            "Return or onward ticket",
        ],
        "related_links": [
            ("visa-nepal.html", "Nepal Visa Requirements"),
            ("nepal-visa-fees.html", "Nepal Visa Fees"),
            ("nepal-visa-extension.html", "Nepal Visa Extension"),
            ("nepal-visa-requirements.html", "Nepal Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Nepal e-Visa?", "The Nepal e-Visa is an online pre-application system that allows tourists to fill in their visa details before arriving in Nepal. The actual visa is stamped upon arrival after payment and biometric submission, but the online process significantly speeds up the arrival procedure."),
            ("How much does the Nepal visa cost?", "Nepal tourist visa fees are USD 30 for 15 days, USD 50 for 30 days, and USD 125 for 90 days. Children under 10 years of age receive a free visa. Payment is made upon arrival in Nepal."),
            ("Can I extend my Nepal visa?", "Yes, Nepal tourist visas can be extended at the Department of Immigration in Kathmandu or the Immigration Office in Pokhara. Extensions are available up to a maximum of 150 days within a calendar year."),
            ("Do Indian citizens need a Nepal visa?", "No, Indian citizens do not need a visa to enter Nepal. They can enter freely with a valid passport or certain other government-issued identity documents."),
        ],
    },

    # 8  Taiwan Travel Authorization
    {
        "filename": "taiwan-evisa.html",
        "title": "Taiwan Travel Authorization Certificate — Free Entry for Eligible Nationalities 2026",
        "meta_desc": "Apply for a Taiwan Travel Authorization Certificate online. Free for many nationalities, 90-day stay. Apply at evisa.immigration.gov.tw.",
        "h1": "Taiwan Travel Authorization Certificate",
        "bg_idx": 2,
        "intro": (
            "The Taiwan Travel Authorization Certificate allows eligible foreign nationals to enter Taiwan for tourism or business without a traditional visa. "
            "The authorization is free for citizens of many countries, permits stays of up to 90 days, and can be applied for online in minutes. "
            "The system is designed for passport holders from countries that have a visa-free or simplified entry arrangement with Taiwan."
        ),
        "key_facts": [
            ("Visa Type", "Travel Authorization Certificate / e-Visa"),
            ("Cost", "Free (for visa-exempt nationalities), fees vary for other e-Visas"),
            ("Validity", "90 days (visa-exempt), varies for e-Visa"),
            ("Processing Time", "Instant (travel authorization), 5-10 days (e-Visa)"),
            ("Official Website", '<a href="https://evisa.immigration.gov.tw" target="_blank" rel="noopener">evisa.immigration.gov.tw</a>'),
        ],
        "who_needs": (
            "Citizens of the United States, Canada, United Kingdom, Australia, New Zealand, Japan, South Korea, EU/Schengen countries, and many other nations can enter Taiwan visa-free for up to 90 days. "
            "Nationals of countries such as India, the Philippines, Vietnam, Indonesia, Myanmar, Cambodia, and Laos may apply for the Taiwan e-Visa through the online portal. "
            "Chinese mainland residents must apply through separate arrangements."
        ),
        "application_steps": [
            "Visit the Taiwan e-Visa portal at evisa.immigration.gov.tw.",
            "Select your nationality and check your eligibility for visa-exempt entry or e-Visa.",
            "If visa-exempt, apply for the Travel Authorization Certificate by entering passport and travel details.",
            "If applying for an e-Visa, upload required documents and pay the applicable fee.",
            "Receive your authorization or e-Visa confirmation via email.",
            "Print the authorization certificate and present it at the airline check-in counter and upon arrival in Taiwan.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Return or onward flight ticket",
            "Proof of accommodation in Taiwan",
            "Proof of financial means for the duration of stay",
            "Recent passport-size photograph (for e-Visa applicants)",
        ],
        "related_links": [
            ("visa-taiwan.html", "Taiwan Visa Requirements"),
            ("taiwan-visa-fees.html", "Taiwan Visa Fees"),
            ("taiwan-visa-extension.html", "Taiwan Visa Extension"),
            ("taiwan-visa-requirements.html", "Taiwan Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Taiwan Travel Authorization Certificate?", "The Taiwan Travel Authorization Certificate is a free online authorization for citizens of visa-exempt countries to enter Taiwan. It simplifies the entry process and is available for nationals of countries with visa-free arrangements with Taiwan."),
            ("Is the Taiwan Travel Authorization free?", "Yes, the Travel Authorization Certificate is free for citizens of visa-exempt countries. Nationals who require an e-Visa may need to pay a processing fee, which varies by nationality and visa type."),
            ("How long can I stay in Taiwan with the Travel Authorization?", "The Taiwan Travel Authorization permits stays of up to 90 days for most eligible nationalities. Extensions are generally not available for visa-exempt entries, so travelers must depart before the 90-day limit."),
            ("Who needs a Taiwan e-Visa?", "Nationals of countries such as India, the Philippines, Vietnam, Indonesia, and several others who do not qualify for visa-free entry must apply for a Taiwan e-Visa. This can be done online through the official portal at evisa.immigration.gov.tw."),
        ],
    },

    # 9  China e-Visa
    {
        "filename": "china-evisa.html",
        "title": "China e-Visa & Transit-Free Entry — Application Guide 2026",
        "meta_desc": "China e-Visa application guide. USD 140 fee (varies by nationality), 30-day transit-free entry for eligible nationalities, multiple visa categories.",
        "h1": "China e-Visa & Transit-Free Entry Guide",
        "bg_idx": 3,
        "intro": (
            "China offers electronic visa application options for certain nationalities, as well as a generous transit-free (visa-free) policy allowing travelers from over 50 countries to transit through China for up to 144 hours without a visa. "
            "Standard Chinese tourist visa (L visa) fees are approximately USD 140 for US citizens, with fees varying significantly by nationality. "
            "China has been expanding its visa-free transit and group tour visa exemption programs in recent years."
        ),
        "key_facts": [
            ("Visa Type", "e-Visa / L (Tourist), M (Business), F (Non-Commercial Visit), Transit-Free Entry"),
            ("Cost", "USD 140 (US citizens), USD 60-85 (most other nationalities)"),
            ("Validity", "30/60/90 days per entry, 10-year multiple entry (US/Canada)"),
            ("Processing Time", "4-7 business days (standard), 2-3 days (express)"),
            ("Official Website", '<a href="https://www.visaforchina.cn" target="_blank" rel="noopener">visaforchina.cn</a>'),
        ],
        "who_needs": (
            "Most foreign nationals need a visa to enter China, except those eligible for transit-free entry (72/144-hour visa-free transit at designated ports). "
            "Citizens of certain countries including Singapore, Brunei, Japan (under specific programs), and some others may enter visa-free for short periods. "
            "US and Canadian citizens can obtain 10-year multiple-entry visas at higher fees."
        ),
        "application_steps": [
            "Visit the Chinese Visa Application Service Center (CVASC) website at visaforchina.cn.",
            "Complete the online application form and print the confirmation page.",
            "Gather required supporting documents including passport photo, itinerary, and hotel bookings.",
            "Submit the application in person at your nearest CVASC or Chinese embassy/consulate.",
            "Pay the visa fee (varies by nationality and processing speed).",
            "Collect your passport with the visa sticker after 4-7 business days.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity and 2 blank visa pages",
            "Completed visa application form with recent 48x33 mm photograph",
            "Round-trip flight reservation",
            "Hotel booking confirmation for the entire stay in China",
            "Proof of financial means (bank statements)",
            "Invitation letter (for M/F visa categories)",
            "Travel itinerary with dates and locations",
        ],
        "related_links": [
            ("visa-china.html", "China Visa Requirements"),
            ("china-visa-fees.html", "China Visa Fees"),
            ("china-visa-extension.html", "China Visa Extension"),
            ("china-visa-requirements.html", "China Visa Application Guide"),
        ],
        "faqs": [
            ("Do I need a visa for China?", "Most foreign nationals need a visa to enter China. However, citizens of over 50 countries can enter China visa-free for 72 or 144 hours under the transit-free entry policy when transiting through designated Chinese airports and ports."),
            ("How much does a China visa cost?", "China visa fees vary by nationality. US citizens pay approximately USD 140 for a 10-year multiple-entry visa. Citizens of most other countries pay between USD 60 and USD 85. Express processing incurs an additional fee."),
            ("What is the China 144-hour transit-free policy?", "The 144-hour transit-free entry policy allows citizens of 54 countries to transit through designated Chinese cities for up to 6 days without a visa, provided they hold a confirmed onward ticket to a third country. This is available at major ports including Beijing, Shanghai, Guangzhou, and others."),
            ("How long does China visa processing take?", "Standard processing takes 4-7 business days. Express processing (2-3 days) and rush processing (1 day) are available at additional cost, subject to availability at your local visa center."),
            ("Can I apply for a China visa online?", "While the application form can be completed online at visaforchina.cn, most applicants still need to submit documents in person at a Chinese Visa Application Service Center. Some nationalities and programs may qualify for fully electronic processing."),
        ],
    },

    # 10  Brazil e-Visa
    {
        "filename": "brazil-evisa.html",
        "title": "Brazil e-Visa (eVisitor) — USD 44.50 Online Application 2026",
        "meta_desc": "Apply for a Brazil e-Visa online. USD 44.50, 90 days per entry, 5-year multiple entry validity for eligible nationalities including US, Canada, Australia, and Japan.",
        "h1": "Brazil e-Visa (eVisitor) — 5-Year Multiple Entry",
        "bg_idx": 4,
        "intro": (
            "The Brazil e-Visa (eVisitor) allows citizens of eligible countries to obtain a Brazilian visa online without visiting a consulate. "
            "It costs USD 44.50, is valid for 5 years with multiple entries, and allows stays of up to 90 days per entry (180 days per year). "
            "The e-Visa is available for tourism, business, artistic/sports activities, and transit purposes."
        ),
        "key_facts": [
            ("Visa Type", "e-Visa (eVisitor) — VIVIS, VITEM categories"),
            ("Cost", "USD 44.50"),
            ("Validity", "5 years, multiple entry, up to 90 days per entry"),
            ("Processing Time", "5-10 business days"),
            ("Official Website", '<a href="https://formulario-mre.serpro.gov.br" target="_blank" rel="noopener">formulario-mre.serpro.gov.br</a>'),
        ],
        "who_needs": (
            "Citizens of the United States, Canada, Australia, and Japan are eligible for the Brazil e-Visa. "
            "Many countries including EU member states, the United Kingdom, Argentina, and others can enter Brazil visa-free for up to 90 days. "
            "Citizens of countries not eligible for visa-free entry or the e-Visa must apply for a traditional visa at a Brazilian consulate."
        ),
        "application_steps": [
            "Visit the official Brazilian e-Visa portal at formulario-mre.serpro.gov.br.",
            "Create an account and select the e-Visa category (Visit Visa for tourism/business).",
            "Fill in the application form with personal, passport, and travel information.",
            "Upload a recent digital photo, passport scan, and proof of accommodation.",
            "Pay the USD 44.50 fee via credit card.",
            "Receive your e-Visa approval via email within 5-10 business days.",
            "Print the e-Visa or save it on your mobile device for presentation at immigration.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Recent digital photograph (5x7 cm, white background)",
            "Scanned copy of passport bio page",
            "Round-trip flight reservation or itinerary",
            "Proof of accommodation (hotel booking, invitation letter, or rental agreement)",
            "Proof of financial means (bank statement, credit card statement)",
        ],
        "related_links": [
            ("visa-brazil.html", "Brazil Visa Requirements"),
            ("brazil-visa-fees.html", "Brazil Visa Fees"),
            ("brazil-visa-extension.html", "Brazil Visa Extension"),
            ("brazil-visa-requirements.html", "Brazil Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Brazil e-Visa?", "The Brazil e-Visa (eVisitor) is an electronic visa that allows eligible foreign nationals to apply for a Brazilian visa online. It is valid for 5 years with multiple entries and permits stays of up to 90 days per entry."),
            ("How much does the Brazil e-Visa cost?", "The Brazil e-Visa costs USD 44.50 per application. This fee is non-refundable and must be paid online via credit card during the application process."),
            ("Which countries are eligible for the Brazil e-Visa?", "The Brazil e-Visa is currently available for citizens of the United States, Canada, Australia, and Japan. Citizens of many other countries can enter Brazil visa-free for 90 days and do not need the e-Visa."),
            ("How long can I stay in Brazil with the e-Visa?", "The Brazil e-Visa allows a maximum stay of 90 days per entry. Within a 12-month period, you may stay up to 180 days total. The visa itself is valid for 5 years from the date of issue."),
        ],
    },

    # 11  Cambodia e-Visa
    {
        "filename": "cambodia-evisa.html",
        "title": "Cambodia e-Visa — USD 36 Online Tourist Visa Application 2026",
        "meta_desc": "Apply for Cambodia e-Visa online. USD 36 (USD 30 visa + USD 6 processing), 30 days single entry, processed in 3 business days.",
        "h1": "Cambodia e-Visa — Online Tourist Visa",
        "bg_idx": 0,
        "intro": (
            "The Cambodia e-Visa is an electronic tourist visa that allows visitors to enter Cambodia for tourism purposes without visiting an embassy. "
            "It costs USD 36 (USD 30 visa fee plus USD 6 processing fee), is valid for 30 days with a single entry, and is processed within 3 business days. "
            "The e-Visa is accepted at Phnom Penh and Siem Reap international airports as well as selected land border crossings."
        ),
        "key_facts": [
            ("Visa Type", "e-Visa (Tourist — Type T)"),
            ("Cost", "USD 36 (USD 30 visa fee + USD 6 processing fee)"),
            ("Validity", "30 days, single entry (extendable once for 30 days)"),
            ("Processing Time", "3 business days"),
            ("Official Website", '<a href="https://www.evisa.gov.kh" target="_blank" rel="noopener">evisa.gov.kh</a>'),
        ],
        "who_needs": (
            "Citizens of most countries can apply for the Cambodia e-Visa. ASEAN member state nationals may enter Cambodia visa-free for up to 30 days. "
            "Citizens of certain countries including Afghanistan, Algeria, Bangladesh, Iran, Iraq, Pakistan, Saudi Arabia, Sri Lanka, and Sudan are not eligible for the e-Visa and must apply at a Cambodian embassy. "
            "The e-Visa is only for tourism; business visitors should apply for a Type E visa on arrival."
        ),
        "application_steps": [
            "Visit the official Cambodia e-Visa website at evisa.gov.kh.",
            "Click 'Apply Now' and fill in the online application form.",
            "Upload a recent passport-size photograph (JPEG format, 4x6 cm).",
            "Pay the USD 36 fee via Visa, MasterCard, or other accepted payment methods.",
            "Receive your e-Visa approval via email within 3 business days.",
            "Print the e-Visa approval letter — you will need two copies.",
            "Present one copy at departure and one at Cambodian immigration upon arrival.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity and 1 blank page",
            "Recent passport-size digital photograph (JPEG, 4x6 cm)",
            "Credit or debit card for online payment (Visa or MasterCard)",
            "Email address for receiving the e-Visa approval",
            "Travel itinerary with accommodation details",
        ],
        "related_links": [
            ("visa-cambodia.html", "Cambodia Visa Requirements"),
            ("cambodia-visa-fees.html", "Cambodia Visa Fees"),
            ("cambodia-visa-extension.html", "Cambodia Visa Extension"),
            ("cambodia-visa-requirements.html", "Cambodia Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Cambodia e-Visa?", "The Cambodia e-Visa is an electronic tourist visa that allows visitors to enter Cambodia for up to 30 days. It is an online alternative to the Visa on Arrival and can be obtained before travel through the official portal at evisa.gov.kh."),
            ("How much does the Cambodia e-Visa cost?", "The Cambodia e-Visa costs a total of USD 36, which includes the USD 30 visa fee and a USD 6 processing fee. The fee is non-refundable and paid online during the application."),
            ("Can I extend the Cambodia e-Visa?", "Yes, the Cambodia e-Visa (tourist visa) can be extended once for an additional 30 days at the Cambodian Immigration Department in Phnom Penh. The extension must be applied for before the initial visa expires."),
            ("Which entry points accept the Cambodia e-Visa?", "The Cambodia e-Visa is accepted at Phnom Penh International Airport, Siem Reap International Airport, and selected land border crossings including Bavet (Moc Bai), Cham Yeam (Hat Lek), and Poi Pet (Aranyaprathet)."),
            ("What is the difference between Cambodia e-Visa and Visa on Arrival?", "Both the Cambodia e-Visa and Visa on Arrival are tourist visas with the same validity (30 days, single entry). The e-Visa costs USD 36 (including processing fee) and is applied for online before travel, while the Visa on Arrival costs USD 30 and is obtained at the airport or border upon arrival."),
        ],
    },

    # 12  Turkey e-Visa
    {
        "filename": "turkey-evisa.html",
        "title": "Turkey e-Visa — Online Application via evisa.gov.tr 2026",
        "meta_desc": "Apply for a Turkey e-Visa online via evisa.gov.tr. USD 50 (varies by nationality), 30-90 days stay, processed instantly. Available for 100+ nationalities.",
        "h1": "Turkey e-Visa — Online Application via evisa.gov.tr",
        "bg_idx": 1,
        "intro": (
            "The Turkey e-Visa is an electronic visa that allows citizens of over 100 countries to enter Turkey for tourism or business by applying online. "
            "Fees vary by nationality, with most paying approximately USD 50, and the e-Visa permits stays of 30 to 90 days depending on your passport. "
            "The application is processed almost instantly, and the e-Visa is linked electronically to your passport."
        ),
        "key_facts": [
            ("Visa Type", "e-Visa (Tourism / Business)"),
            ("Cost", "USD 50 (varies by nationality; some pay more or less)"),
            ("Validity", "180 days from issue, single or multiple entry, 30-90 day stay"),
            ("Processing Time", "Instant (minutes)"),
            ("Official Website", '<a href="https://www.evisa.gov.tr" target="_blank" rel="noopener">evisa.gov.tr</a>'),
        ],
        "who_needs": (
            "Citizens of many countries including the United States, Canada, United Kingdom, Australia, China, India, and most African nations require an e-Visa to enter Turkey. "
            "EU/Schengen citizens, Japanese, South Korean, and several other nationalities can enter Turkey visa-free for 30-90 days. "
            "Always check the official evisa.gov.tr portal for your specific nationality's requirements and fees."
        ),
        "application_steps": [
            "Visit the official Turkey e-Visa website at evisa.gov.tr.",
            "Select your nationality and travel document type.",
            "Enter your travel dates and verify your eligibility.",
            "Fill in personal and passport details.",
            "Pay the e-Visa fee via Visa, MasterCard, or UnionPay debit/credit card.",
            "Receive your e-Visa instantly via email.",
            "Print the e-Visa or save it on your mobile device for presentation at immigration.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity beyond entry date",
            "Credit or debit card for online payment (Visa, MasterCard, or UnionPay)",
            "Valid email address for receiving the e-Visa",
            "Return or onward flight ticket (may be requested at entry)",
            "Proof of accommodation in Turkey (may be requested at entry)",
        ],
        "related_links": [
            ("visa-turkey.html", "Turkey Visa Requirements"),
            ("turkey-visa-fees.html", "Turkey Visa Fees"),
            ("turkey-visa-extension.html", "Turkey Visa Extension"),
            ("turkey-visa-requirements.html", "Turkey Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Turkey e-Visa?", "The Turkey e-Visa is an electronic travel authorization that allows eligible foreign nationals to enter Turkey for tourism or business purposes. It replaces the traditional sticker visa for most nationalities and can be obtained online in minutes through the official evisa.gov.tr portal."),
            ("How much does the Turkey e-Visa cost?", "Turkey e-Visa fees vary by nationality. US, Canadian, and Australian citizens typically pay around USD 50. UK citizens and some other nationalities may have different fees. Some nationalities are exempt from the e-Visa and can enter visa-free."),
            ("How long can I stay in Turkey with the e-Visa?", "The Turkey e-Visa typically allows stays of 30 to 90 days depending on your nationality. US citizens can stay up to 90 days within a 180-day period. The e-Visa itself is valid for 180 days from the date of issue."),
            ("Is the Turkey e-Visa single or multiple entry?", "The Turkey e-Visa can be single or multiple entry depending on your nationality. US, UK, and Canadian citizens typically receive multiple-entry e-Visas, while other nationalities may receive single-entry e-Visas. Check evisa.gov.tr for your specific nationality."),
        ],
    },

    # 13  Mexico FMM
    {
        "filename": "mexico-fmm-tourist-card.html",
        "title": "Mexico FMM Tourist Card (Forma Migratoria Multiple) — Entry Guide 2026",
        "meta_desc": "Mexico FMM Tourist Card guide. Free for flights, MXN 575 (~USD 35) by land. Up to 180 days stay for tourism. All you need to know about the Forma Migratoria Multiple.",
        "h1": "Mexico FMM — Forma Migratoria Multiple (Tourist Card)",
        "bg_idx": 2,
        "intro": (
            "The Mexico FMM (Forma Migratoria Multiple) is a tourist card required for all foreign visitors entering Mexico for tourism, transit, or short business trips. "
            "The FMM is free when arriving by air (included in your airline ticket), but costs approximately MXN 575 (about USD 35) when entering by land. "
            "It allows stays of up to 180 days, though immigration officers may grant fewer days at their discretion."
        ),
        "key_facts": [
            ("Visa Type", "FMM — Forma Migratoria Multiple (Tourist Card)"),
            ("Cost", "Free (by air, included in airline ticket) / MXN 575 (~USD 35) by land"),
            ("Validity", "Up to 180 days (at immigration officer's discretion)"),
            ("Processing Time", "On arrival (or can be completed online before travel)"),
            ("Official Website", '<a href="https://www.inm.gob.mx" target="_blank" rel="noopener">inm.gob.mx</a>'),
        ],
        "who_needs": (
            "All foreign nationals entering Mexico need an FMM, regardless of whether they are visa-exempt. "
            "Citizens of the United States, Canada, EU/Schengen countries, United Kingdom, Japan, South Korea, and many other countries do not need a visa but must still obtain the FMM upon arrival. "
            "Citizens of countries that require a Mexican visa must obtain their visa before travel and will also receive the FMM at the border."
        ),
        "application_steps": [
            "For air travel: the FMM is distributed on the plane or at the immigration counter upon arrival. You can also pre-fill it online at inm.gob.mx.",
            "Fill in the FMM form with personal, passport, and flight information.",
            "Present the completed FMM along with your passport at the immigration counter.",
            "The immigration officer will stamp the FMM and assign the number of authorized days (up to 180).",
            "Keep the FMM card safe throughout your stay — you must return it when departing Mexico.",
            "For land entry: pay the MXN 575 fee at a bank (Banjercito) at the border crossing.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Completed FMM form (available online or at the airport/border)",
            "Return or onward flight ticket",
            "Proof of accommodation in Mexico (may be requested)",
            "Proof of sufficient funds (may be requested)",
            "Mexican visa (only for nationalities that require it)",
        ],
        "related_links": [
            ("visa-mexico.html", "Mexico Visa Requirements"),
            ("mexico-visa-fees.html", "Mexico Visa Fees"),
            ("mexico-visa-extension.html", "Mexico Visa Extension"),
            ("mexico-visa-requirements.html", "Mexico Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Mexico FMM?", "The Mexico FMM (Forma Migratoria Multiple) is a tourist card that all foreign visitors must complete when entering Mexico. It is not a visa but an immigration form that authorizes your stay for tourism, transit, or short business visits for up to 180 days."),
            ("Do I need to pay for the Mexico FMM?", "If you are arriving in Mexico by air, the FMM fee is included in your airline ticket price, so there is no additional charge. If you enter Mexico by land and plan to stay beyond the border zone (approximately 20 km from the border) or for more than 7 days, you must pay MXN 575 (approximately USD 35) at a Banjercito bank at the border."),
            ("How many days will I get on the Mexico FMM?", "The maximum authorized stay on the FMM is 180 days. However, the immigration officer has discretion to grant fewer days based on your travel plans, documentation, and other factors. If you need more days, you can politely explain your planned itinerary."),
            ("What happens if I lose my Mexico FMM?", "If you lose your FMM, you must visit an INM (Instituto Nacional de Migracion) office in Mexico to obtain a replacement before departing. There is a fee for replacement, and you will need to provide your passport and any documentation of your original entry."),
            ("Can I extend my Mexico FMM?", "The FMM generally cannot be extended once issued. However, you can visit an INM office and request additional days if your original FMM was issued for fewer than 180 days. Alternatively, some travelers do a border run (exit and re-enter Mexico) to obtain a new FMM."),
        ],
    },

    # 14  Qatar Hayya Visa
    {
        "filename": "qatar-hayya-visa.html",
        "title": "Qatar Hayya Visa & Visit Visa — Tourist Entry Guide 2026",
        "meta_desc": "Apply for Qatar Hayya or Visit Visa. QAR 100 (~USD 27) tourist visa, 30 days extendable, Hayya card system for events. Complete Qatar entry guide.",
        "h1": "Qatar Hayya Visa & Visit Visa — Tourist Entry Guide",
        "bg_idx": 3,
        "intro": (
            "Qatar offers multiple entry options for visitors, including the Hayya card system (originally created for the FIFA World Cup 2022 and now used for major events) and the standard Visit Visa for tourism. "
            "The Qatar tourist Visit Visa costs QAR 100 (approximately USD 27), is valid for 30 days, and can be extended. "
            "Many nationalities also qualify for visa-free entry to Qatar for 30 to 90 days depending on their passport."
        ),
        "key_facts": [
            ("Visa Type", "Hayya Card (events) / Visit Visa (tourism) / Visa-Free Entry"),
            ("Cost", "QAR 100 (~USD 27) for tourist visa; Hayya card free for event attendees"),
            ("Validity", "30 days (extendable), visa-free: 30-90 days by nationality"),
            ("Processing Time", "3-7 business days (Visit Visa), instant (Hayya for events)"),
            ("Official Website", '<a href="https://www.visitqatar.qa" target="_blank" rel="noopener">visitqatar.qa</a> / <a href="https://hayya.qatar2022.qa" target="_blank" rel="noopener">hayya.qatar2022.qa</a>'),
        ],
        "who_needs": (
            "Citizens of over 90 countries can enter Qatar visa-free, including nationals of the United States, United Kingdom, Canada, Australia, EU/Schengen countries, and many others. "
            "Nationals of GCC countries have unrestricted entry. "
            "Citizens of countries not eligible for visa-free entry can apply for a Visit Visa online or obtain a visa through a hotel or tour operator acting as sponsor."
        ),
        "application_steps": [
            "Check if your nationality qualifies for visa-free entry to Qatar.",
            "If a visa is required, visit the Qatar Ministry of Interior portal or arrange sponsorship through a hotel.",
            "Fill in the visa application form online with personal and passport details.",
            "Upload a recent passport-size photograph and passport bio page scan.",
            "Pay the QAR 100 visa fee via credit or debit card.",
            "Receive your visa approval via email within 3-7 business days.",
            "For events: apply for a Hayya card through the official Hayya portal with your event ticket details.",
        ],
        "documents": [
            "Valid passport with at least 6 months remaining validity",
            "Recent passport-size photograph",
            "Confirmed return or onward flight ticket",
            "Hotel booking or accommodation confirmation in Qatar",
            "Proof of financial means for the stay",
            "Event ticket or registration (for Hayya card applicants)",
        ],
        "related_links": [
            ("visa-qatar.html", "Qatar Visa Requirements"),
            ("qatar-visa-fees.html", "Qatar Visa Fees"),
            ("qatar-visa-extension.html", "Qatar Visa Extension"),
            ("qatar-visa-requirements.html", "Qatar Visa Application Guide"),
        ],
        "faqs": [
            ("What is the Qatar Hayya card?", "The Qatar Hayya card is a digital entry permit system originally developed for the FIFA World Cup 2022. It now serves as a fan ID and entry authorization for major events in Qatar, allowing holders to enter the country without a traditional visa during event periods."),
            ("Do I need a visa for Qatar?", "Citizens of over 90 countries can enter Qatar visa-free for 30 to 90 days depending on nationality. If your country is not on the visa-free list, you will need to apply for a Visit Visa before traveling, either online or through a sponsor such as a hotel."),
            ("How much does the Qatar tourist visa cost?", "The Qatar tourist Visit Visa costs QAR 100, approximately USD 27. Visa-free entry has no fee. The Hayya card for event attendees is also free when linked to a valid event ticket."),
            ("Can I extend my Qatar visa?", "Yes, the Qatar Visit Visa can be extended for an additional period at the Ministry of Interior. Visa-free stays may also be extendable depending on nationality. Extensions are generally granted for tourism purposes."),
        ],
    },
]


# ---------------------------------------------------------------------------
# Template
# ---------------------------------------------------------------------------
def build_hreflang_block(filename: str) -> str:
    lines = []
    for code, _flag, _label in LANGUAGES:
        url = f"https://www.evisa-card.com/{code}/{filename}"
        lines.append(f'    <link rel="alternate" hreflang="{code}" href="{url}"/>')
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{filename}"/>')
    return "\n".join(lines)


def build_faq_schema(faqs: list) -> str:
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [],
    }
    for question, answer in faqs:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": answer,
            },
        })
    return json.dumps(schema, indent=4, ensure_ascii=False)


def build_lang_dropdown(filename: str) -> str:
    items = []
    for code, flag, label in LANGUAGES:
        active = ' active' if code == 'en' else ''
        items.append(
            f'                        <a class="dropdown-item{active}" href="/{code}/{filename}">'
            f'<span class="fi fi-{flag}"></span> {label}</a>'
        )
    return "\n".join(items)


def build_key_facts_table(facts: list) -> str:
    rows = []
    for label, value in facts:
        rows.append(f"        <tr><td><strong>{label}</strong></td><td>{value}</td></tr>")
    return (
        '<table class="table table-bordered table-striped">\n'
        "    <tbody>\n"
        + "\n".join(rows)
        + "\n    </tbody>\n</table>"
    )


def build_steps_list(steps: list) -> str:
    items = "\n".join(f"    <li>{s}</li>" for s in steps)
    return f"<ol>\n{items}\n</ol>"


def build_ul(items: list) -> str:
    li = "\n".join(f"    <li>{item}</li>" for item in items)
    return f"<ul>\n{li}\n</ul>"


def build_related_links(links: list) -> str:
    li = "\n".join(
        f'    <li><a href="{href}">{text}</a></li>' for href, text in links
    )
    return f"<ul>\n{li}\n</ul>"


def build_content(page: dict) -> str:
    parts = []
    # Intro
    parts.append(f"<p>{page['intro']}</p>")
    parts.append("")
    # Key Facts
    parts.append("<h2>Key Facts</h2>")
    parts.append(build_key_facts_table(page["key_facts"]))
    parts.append("")
    # Who Needs
    parts.append("<h2>Who Needs This Visa?</h2>")
    parts.append(f"<p>{page['who_needs']}</p>")
    parts.append("")
    # Application Process
    parts.append("<h2>Application Process</h2>")
    parts.append(build_steps_list(page["application_steps"]))
    parts.append("")
    # Required Documents
    parts.append("<h2>Required Documents</h2>")
    parts.append(build_ul(page["documents"]))
    parts.append("")
    # FAQs rendered as visible accordion-style (simple headings)
    parts.append("<h2>Frequently Asked Questions</h2>")
    for q, a in page["faqs"]:
        parts.append(f"<h3>{q}</h3>")
        parts.append(f"<p>{a}</p>")
    parts.append("")
    # Related Pages
    parts.append("<h2>Related Pages</h2>")
    parts.append(build_related_links(page["related_links"]))
    return "\n".join(parts)


PAGE_TEMPLATE = textwrap.dedent("""\
<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{filename}"/>
{hreflang_block}
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&display=swap" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/owl.carousel.min.css" rel="stylesheet"/>
    <link href="../css/owl.theme.default.min.css" rel="stylesheet"/>
    <link href="../css/magnific-popup.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <script type="application/ld+json">
    {faq_schema}
    </script>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light" id="ftco-navbar" style="background-color:#0d2461 !important;position:relative;z-index:10;">
    <div class="container">
        <a class="navbar-brand" href="../index.html" style="padding:0;"><img src="../images/logo.png" alt="eVisa-Card.com" style="height:120px;width:auto;display:block;"></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse justify-content-center" id="ftco-nav">
            <ul class="navbar-nav align-items-center">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/expat-guides.html">Guides</a></li>
                <li class="nav-item dropdown ml-3">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi fi-gb"></span> English</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
{lang_dropdown}
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="hero-wrap hero-wrap-2" style="background-image:url('../images/{bg_img}');background-size:cover;background-position:center top;">
    <div class="overlay"></div>
    <div class="container">
        <div class="row no-gutters slider-text align-items-end justify-content-center">
            <div class="col-md-9 ftco-animate text-center pb-5">
                <h1 class="mb-0 bread">{h1}</h1>
            </div>
        </div>
    </div>
</section>

<section class="ftco-section">
<div class="container" style="max-width:960px;">
    {content}
</div>
</section>

<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                <ul class="ftco-footer-social list-unstyled float-md-center mt-3">
                    <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                    <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                    <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                </ul>
                <p class="mt-4">&copy; 2026 eVisa-Card.com &mdash; Global eVisa &amp; Travel Information Platform</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="/en/legal-notice.html" style="color:#ffffff;text-decoration:underline;">Legal Notice</a>
                    &nbsp;|&nbsp;
                    <a href="/en/disclaimer.html" style="color:#ffffff;text-decoration:underline;">Disclaimer</a>
                </p>
            </div>
        </div>
    </div>
</footer>
<script src="../js/jquery.min.js"></script>
<script src="../js/jquery-migrate-3.0.1.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/jquery.easing.1.3.js"></script>
<script src="../js/jquery.waypoints.min.js"></script>
<script src="../js/jquery.stellar.min.js"></script>
<script src="../js/owl.carousel.min.js"></script>
<script src="../js/jquery.magnific-popup.min.js"></script>
<script src="../js/scrollax.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>
""")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for page in PAGES:
        filename = page["filename"]
        bg_img = BG_IMAGES[page["bg_idx"] % len(BG_IMAGES)]

        html = PAGE_TEMPLATE.format(
            title=page["title"],
            meta_desc=page["meta_desc"],
            filename=filename,
            hreflang_block=build_hreflang_block(filename),
            faq_schema=build_faq_schema(page["faqs"]),
            lang_dropdown=build_lang_dropdown(filename),
            bg_img=bg_img,
            h1=page["h1"],
            content=build_content(page),
        )

        out_path = os.path.join(OUT_DIR, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        created.append(filename)
        print(f"  Created: {filename}")

    print(f"\nDone — {len(created)} pages written to {OUT_DIR}")


if __name__ == "__main__":
    main()
