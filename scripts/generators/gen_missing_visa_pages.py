#!/usr/bin/env python3
"""
Generate all missing visa-*.html pages for EN + new lang versions of critical ones.
Also creates fr/es/pt/index.html, en/visa-uk.html redirect.
"""
import os, re

BASE = r"C:/Users/chemi/Documents/evisa/pacific-main/www"

# ── Country data dict ─────────────────────────────────────────────────────────
# slug: (name, flag_code, h1_title, intro, table_rows_html, sections_html, official_url, official_label, faq_list, apply_steps)
COUNTRIES = {
"south-korea": (
    "South Korea", "kr",
    "South Korea eVisa &amp; Travel Information (2026)",
    "South Korea (Republic of Korea) is a highly developed country in East Asia, famed for its K-culture, technology, cuisine and ancient palaces. Entry is managed by the Korea Immigration Service (HiKorea). Most visitors enter visa-free or via the K-ETA pre-travel authorisation.",
    """<tr><th>Visa Exemption</th><td>Yes (110+ countries — 30 to 90 days)</td></tr>
<tr><th>K-ETA Required</th><td>Yes (for visa-free nationals, USD 10, mandatory)</td></tr>
<tr><th>Short-Term Visa (C-3)</th><td>Single/double entry, 90 days max</td></tr>
<tr><th>Visa Fee</th><td>USD 40–80 (single/multiple entry)</td></tr>
<tr><th>Processing Time</th><td>3–5 business days (online/embassy)</td></tr>
<tr><th>Passport Validity</th><td>Valid throughout intended stay</td></tr>""",
    """<h2 id="introduction">Introduction</h2>
<p>South Korea receives over 10 million tourists annually. Major airports are Incheon International (ICN) and Gimpo (GMP) in Seoul, Gimhae (PUS) in Busan. The Korea Immigration Service (KIS) manages all visa and entry matters. Most nationalities can enter visa-free for up to 30 or 90 days, but must obtain a <strong>Korea Electronic Travel Authorization (K-ETA)</strong> before boarding.</p>
<h2 id="tourist">Visa-Free Entry &amp; K-ETA</h2>
<p>Citizens of 110+ countries may enter visa-free. However, almost all visa-free nationalities must apply for a <strong>K-ETA</strong> before travel at k-eta.immigration.go.kr (fee: KRW 10,000 / ~USD 7.50). The K-ETA is valid for multiple visits over 2 years. Certain nationalities (including the US, EU countries and many others) require the K-ETA; the USA and UK are temporarily exempt until end 2025 — check the official site for current exemptions.</p>
<h2 id="business">Business &amp; Work</h2>
<p>Business activities on a short-term stay (C-3 visa or visa-free): up to 90 days for meetings, conferences and negotiations. For employment in Korea, a work visa (E-series) is required — categories include E-2 (English teaching), E-7 (special designated activities), D-8 (corporate investment). Apply through a Korean embassy or consulate.</p>
<h2 id="documents">Required Documents (Short-Term Visa)</h2>
<ul><li>Valid passport (valid throughout stay)</li><li>Completed visa application form</li><li>Passport-sized photo</li><li>Proof of financial means</li><li>Return or onward ticket</li><li>Accommodation confirmation</li><li>Purpose of visit documents (invitation letter for business)</li></ul>
<h2 id="fees">Visa Fees</h2>
<table class="table table-bordered table-sm"><thead><tr><th>Visa Type</th><th>Fee</th></tr></thead><tbody>
<tr><td>K-ETA (pre-travel)</td><td>KRW 10,000 (~USD 7.50)</td></tr>
<tr><td>Short-Term (C-3, single)</td><td>USD 40</td></tr>
<tr><td>Short-Term (C-3, multiple)</td><td>USD 80</td></tr>
<tr><td>Work Visa (E-series)</td><td>USD 60–90</td></tr>
</tbody></table>
<h2 id="application-process">How to Apply</h2>
<ol><li>Check if you need a K-ETA at <a href="https://www.k-eta.immigration.go.kr" target="_blank" rel="noopener">k-eta.immigration.go.kr</a></li><li>Apply for K-ETA online (if required) — approval usually within 72 hours</li><li>If a full visa is needed, apply at a Korean embassy or consulate</li><li>Complete the online application form and upload documents</li><li>Pay the fee and submit; receive your visa sticker or approval</li></ol>
<h2 id="official-links">Official Links</h2>
<ul><li><a href="https://www.k-eta.immigration.go.kr" target="_blank" rel="noopener">K-ETA Official Portal</a></li><li><a href="https://www.hikorea.go.kr" target="_blank" rel="noopener">HiKorea — Korea Immigration Service</a></li><li><a href="https://www.mofa.go.kr/eng" target="_blank" rel="noopener">Korean Ministry of Foreign Affairs</a></li></ul>""",
    "https://www.k-eta.immigration.go.kr", "K-ETA Official Portal",
    [("Do I need a visa for South Korea?","Most nationalities enjoy visa-free entry for 30–90 days, but must apply for a K-ETA online before travel (fee: KRW 10,000). Check k-eta.immigration.go.kr for your country's requirements."),
     ("What is the K-ETA?","The Korea Electronic Travel Authorization (K-ETA) is a pre-travel entry permit required for most visa-free nationals. Apply online at k-eta.immigration.go.kr. It costs KRW 10,000 (~USD 7.50) and is valid for multiple trips over 2 years."),
     ("How long can I stay in South Korea without a visa?","Most visa-exempt nationalities may stay 30 or 90 days per visit."),
     ("Can I work in South Korea on a tourist visa?","No. Working in South Korea requires a separate work visa (E-series). Performing paid work on a tourist or visa-free entry is illegal.")],
    ["Check visa-free eligibility and K-ETA requirements at hikorea.go.kr","Apply for K-ETA online at k-eta.immigration.go.kr if required","Gather documents: passport, photo, return ticket, accommodation, funds","Submit visa application at Korean embassy/consulate if a full visa is needed","Receive K-ETA approval (email) or visa sticker and travel to Korea"]),

"saudi-arabia": (
    "Saudi Arabia", "sa",
    "Saudi Arabia eVisa &amp; Travel Information (2026)",
    "Saudi Arabia, the largest country in the Arabian Peninsula, has dramatically opened to tourism since 2019. The Saudi Tourist Visa (eVisa) is available online to citizens of 60+ countries. Major airports are King Abdulaziz (JED), King Khalid (RUH), and King Fahd (DMM).",
    """<tr><th>Tourist eVisa</th><td>Available online for 60+ nationalities</td></tr>
<tr><th>Stay Duration</th><td>90 days per visit, 180 days per year</td></tr>
<tr><th>eVisa Fee</th><td>SAR 300 (~USD 80) + medical insurance SAR 140</td></tr>
<tr><th>Processing Time</th><td>Usually instant to 24 hours online</td></tr>
<tr><th>On-Arrival</th><td>Available for some nationalities</td></tr>
<tr><th>Passport Validity</th><td>At least 6 months</td></tr>""",
    """<h2 id="introduction">Introduction</h2>
<p>Saudi Arabia opened to international tourism in September 2019 as part of Vision 2030. Top attractions include NEOM, AlUla, Diriyah, Mada'in Saleh, the Red Sea coast and the holy cities of Mecca and Medina (non-Muslims are not permitted in Mecca). The General Directorate of Passports (Jawazat) manages immigration.</p>
<h2 id="evisa">Saudi Tourist eVisa</h2>
<p>Citizens of 60+ countries (including the US, UK, EU, Australia, Japan, Canada and many others) can apply online at visa.visitsaudi.com. The eVisa allows multiple entries, up to 90 days per visit and 180 days total per year. The fee is SAR 300 (~USD 80) plus mandatory medical insurance of SAR 140 (~USD 37). Approval is usually instant or within 24 hours.</p>
<h2 id="dress">Dress Code &amp; Rules</h2>
<p>Saudi Arabia has relaxed many social restrictions. Female tourists are not required to wear an abaya, but modest dress is expected in public spaces, religious sites and conservative areas. Alcohol remains prohibited. Always carry your passport or a copy.</p>
<h2 id="documents">Required Documents</h2>
<ul><li>Valid passport (6+ months validity)</li><li>Digital passport photo</li><li>Return or onward ticket</li><li>Accommodation details</li><li>Payment for eVisa fee (SAR 300 + SAR 140 insurance)</li></ul>
<h2 id="fees">Visa Fees</h2>
<table class="table table-bordered table-sm"><thead><tr><th>Visa Type</th><th>Fee</th></tr></thead><tbody>
<tr><td>Tourist eVisa (multiple entry, 1 year)</td><td>SAR 300 (~USD 80) + SAR 140 insurance</td></tr>
<tr><td>Visa on Arrival (select nationalities)</td><td>Varies</td></tr>
<tr><td>Business Visa</td><td>Arranged via employer/Saudi sponsor</td></tr>
</tbody></table>
<h2 id="application-process">How to Apply</h2>
<ol><li>Visit <a href="https://visa.visitsaudi.com" target="_blank" rel="noopener">visa.visitsaudi.com</a></li><li>Select your nationality and visa type</li><li>Complete the online form and upload passport photo</li><li>Pay the fee by credit/debit card</li><li>Receive eVisa approval by email (usually instant)</li><li>Present eVisa on arrival or have it scanned at entry</li></ol>
<h2 id="official-links">Official Links</h2>
<ul><li><a href="https://visa.visitsaudi.com" target="_blank" rel="noopener">Saudi Arabia eVisa Official Portal</a></li><li><a href="https://www.visitsaudi.com" target="_blank" rel="noopener">Visit Saudi Arabia Tourism</a></li><li><a href="https://www.passports.gov.sa" target="_blank" rel="noopener">General Directorate of Passports (Jawazat)</a></li></ul>""",
    "https://visa.visitsaudi.com", "Saudi Arabia Official eVisa Portal",
    [("Can I get a Saudi Arabia visa online?","Yes. Citizens of 60+ countries can apply online at visa.visitsaudi.com. The tourist eVisa costs SAR 300 (~USD 80) plus SAR 140 (~USD 37) for mandatory medical insurance. Approval is usually instant."),
     ("How long can I stay in Saudi Arabia?","The tourist eVisa allows up to 90 days per visit and up to 180 days total per year."),
     ("Can women travel alone to Saudi Arabia?","Yes, women of any age can now travel to Saudi Arabia independently. The requirement for a male guardian (mahram) for travel was removed in 2019."),
     ("Is alcohol allowed in Saudi Arabia?","No. Alcohol is strictly prohibited throughout Saudi Arabia.")],
    ["Visit visa.visitsaudi.com and select your nationality","Complete the online form and upload passport photo","Pay SAR 300 eVisa fee + SAR 140 mandatory medical insurance","Receive instant or same-day eVisa approval by email","Present eVisa on arrival at Saudi airports or land borders"]),

"oman": (
    "Oman", "om",
    "Oman eVisa &amp; Travel Information (2026)",
    "Oman, on the southeastern coast of the Arabian Peninsula, is known for its dramatic landscapes, ancient forts, pristine beaches and welcoming hospitality. The Oman eVisa system allows citizens of 100+ countries to apply online before travel.",
    """<tr><th>eVisa Available</th><td>Yes — for 100+ nationalities online</td></tr>
<tr><th>Visa-Free</th><td>Yes (GCC nationals, some others)</td></tr>
<tr><th>Stay Duration</th><td>10 or 30 days (tourist eVisa)</td></tr>
<tr><th>eVisa Fee</th><td>OMR 20 (~USD 52) for 10 days; OMR 50 (~USD 130) for 1 year multiple-entry</td></tr>
<tr><th>Processing Time</th><td>Usually instant to 3 business days</td></tr>
<tr><th>Passport Validity</th><td>At least 6 months</td></tr>""",
    """<h2 id="introduction">Introduction</h2>
<p>Oman is one of the safest countries in the Middle East and increasingly popular with tourists. Main entry points are Muscat International Airport (MCT) and Salalah Airport (SLL). The Royal Oman Police manages immigration and visa affairs. The eVisa system (evisa.rop.gov.om) is the primary route for most visitors.</p>
<h2 id="evisa">Oman eVisa</h2>
<p>Citizens of 100+ countries can apply online for an Oman eVisa. Options include: 10-day single entry (OMR 20 ~USD 52), 30-day single entry (OMR 20), and 1-year multiple-entry (OMR 50 ~USD 130). Processing is usually instant to 3 business days. The eVisa is sent by email as a PDF to present on arrival.</p>
<h2 id="visa-free">Visa-Free Entry</h2>
<p>GCC nationals (Bahrain, Kuwait, Qatar, Saudi Arabia, UAE) enter visa-free. Citizens of many countries also receive visa on arrival. Some nationalities (US, UK, EU, Canada, Australia, Japan, South Korea, New Zealand, Singapore) previously received free visa on arrival — check the current list at the Royal Oman Police website as policies change.</p>
<h2 id="documents">Required Documents</h2>
<ul><li>Valid passport (6+ months validity)</li><li>Passport-sized photo</li><li>Return or onward ticket</li><li>Accommodation booking</li><li>Sufficient funds</li></ul>
<h2 id="fees">Visa Fees</h2>
<table class="table table-bordered table-sm"><thead><tr><th>Visa Type</th><th>Fee</th></tr></thead><tbody>
<tr><td>10-day single entry</td><td>OMR 20 (~USD 52)</td></tr>
<tr><td>30-day single entry</td><td>OMR 20 (~USD 52)</td></tr>
<tr><td>1-year multiple entry</td><td>OMR 50 (~USD 130)</td></tr>
</tbody></table>
<h2 id="application-process">How to Apply</h2>
<ol><li>Visit <a href="https://evisa.rop.gov.om" target="_blank" rel="noopener">evisa.rop.gov.om</a></li><li>Register and complete the online application</li><li>Upload passport scan and photo</li><li>Pay the visa fee by card</li><li>Receive eVisa by email and present on arrival</li></ol>
<h2 id="official-links">Official Links</h2>
<ul><li><a href="https://evisa.rop.gov.om" target="_blank" rel="noopener">Oman Official eVisa Portal (Royal Oman Police)</a></li><li><a href="https://www.rop.gov.om/english" target="_blank" rel="noopener">Royal Oman Police</a></li></ul>""",
    "https://evisa.rop.gov.om", "Oman Official eVisa Portal",
    [("Do I need a visa for Oman?","Most nationalities can apply online for an Oman eVisa at evisa.rop.gov.om. GCC nationals and some others enter visa-free."),
     ("How much does an Oman eVisa cost?","The Oman eVisa costs OMR 20 (~USD 52) for 10 or 30-day single entry, or OMR 50 (~USD 130) for a 1-year multiple-entry visa."),
     ("How long does Oman eVisa take?","Processing is usually instant to 3 business days."),
     ("Is it safe to travel to Oman?","Oman is consistently rated as one of the safest countries in the Middle East and in the world for travellers.")],
    ["Visit evisa.rop.gov.om and create an account","Complete the online form with passport details","Upload a passport scan and passport photo","Select visa type (10-day, 30-day or 1-year) and pay online","Receive eVisa by email and present it on arrival at Oman airport"]),

"bahrain": (
    "Bahrain", "bh",
    "Bahrain eVisa &amp; Travel Information (2026)",
    "Bahrain, a small island kingdom in the Persian Gulf, is a major business and tourism hub in the Middle East. Bahrain's eVisa system allows citizens of most countries to apply online. Citizens of many nationalities receive free visa on arrival.",
    """<tr><th>eVisa Available</th><td>Yes — evisa.gov.bh</td></tr>
<tr><th>Visa on Arrival</th><td>Free for many nationalities</td></tr>
<tr><th>Stay Duration</th><td>14 days (free) or 30 days (paid eVisa)</td></tr>
<tr><th>eVisa Fee</th><td>BHD 29 (~USD 77) — 14 days / BHD 29 for 30 days</td></tr>
<tr><th>Processing Time</th><td>Usually instant online</td></tr>
<tr><th>Passport Validity</th><td>At least 6 months</td></tr>""",
    """<h2 id="introduction">Introduction</h2>
<p>Bahrain is the smallest country in the Middle East and a thriving financial and business hub. The main entry point is Bahrain International Airport (BAH). The Nationality, Passports &amp; Residence Affairs (NPRA) manages immigration. Citizens of most countries can obtain a visa on arrival or apply for an eVisa online at evisa.gov.bh.</p>
<h2 id="evisa">Bahrain eVisa &amp; Visa on Arrival</h2>
<p>Citizens of over 100 countries receive a <strong>free visa on arrival</strong> in Bahrain (14-day tourist). This includes US, UK, EU, Canada, Australia, Japan, South Korea, Singapore, New Zealand and many others. Nationals of GCC states (Saudi Arabia, UAE, Kuwait, Qatar, Oman) enter without any visa requirements. Citizens of other nationalities can apply for a paid eVisa at evisa.gov.bh (fee: BHD 29 ~USD 77).</p>
<h2 id="documents">Required Documents</h2>
<ul><li>Valid passport (6+ months validity)</li><li>Return or onward ticket</li><li>Accommodation details</li><li>Sufficient funds (BHD 50+ recommended)</li></ul>
<h2 id="fees">Visa Fees</h2>
<table class="table table-bordered table-sm"><thead><tr><th>Visa Type</th><th>Fee</th></tr></thead><tbody>
<tr><td>Visa on arrival (100+ nationalities)</td><td>Free (14 days)</td></tr>
<tr><td>Tourist eVisa (30 days)</td><td>BHD 29 (~USD 77)</td></tr>
<tr><td>Multiple-entry eVisa (1 year)</td><td>BHD 29 (~USD 77)</td></tr>
</tbody></table>
<h2 id="application-process">How to Apply</h2>
<ol><li>Check if you qualify for free visa on arrival at <a href="https://www.evisa.gov.bh" target="_blank" rel="noopener">evisa.gov.bh</a></li><li>If applying in advance, create an account and complete the online application</li><li>Pay BHD 29 fee by card</li><li>Receive eVisa confirmation and present at arrival</li></ol>
<h2 id="official-links">Official Links</h2>
<ul><li><a href="https://www.evisa.gov.bh" target="_blank" rel="noopener">Bahrain Official eVisa Portal</a></li><li><a href="https://www.npra.gov.bh/en" target="_blank" rel="noopener">Bahrain NPRA (Immigration)</a></li></ul>""",
    "https://www.evisa.gov.bh", "Bahrain Official eVisa Portal",
    [("Do I need a visa for Bahrain?","Citizens of 100+ countries receive a free visa on arrival. Others can apply for a paid eVisa at evisa.gov.bh."),
     ("Is Bahrain visa on arrival free?","Yes — for citizens of over 100 countries including US, UK, EU, Canada, Australia, Japan, South Korea. The visa is free for 14 days."),
     ("How much is the Bahrain eVisa?","The paid eVisa is BHD 29 (~USD 77) for 30 days or a 1-year multiple-entry visa."),
     ("What is the best time to visit Bahrain?","October to April is the best time to visit Bahrain, when temperatures are mild (18–25°C).")],
    ["Check if you qualify for free visa on arrival at evisa.gov.bh","If not, register on evisa.gov.bh and complete online form","Upload passport scan and photo","Pay BHD 29 fee and submit","Present eVisa or receive stamp on arrival at Bahrain International Airport"]),

"israel": (
    "Israel", "il",
    "Israel eVisa &amp; Travel Information (2026)",
    "Israel is one of the most visited countries in the Middle East, home to Jerusalem, Tel Aviv, the Dead Sea and world-class technology and culture. Most Western nationalities enter visa-free. Israel has an eVisa system (ETA-IL) being phased in for some nationalities.",
    """<tr><th>Visa Exemption</th><td>Yes — citizens of 90+ countries (up to 90 days)</td></tr>
<tr><th>ETA-IL</th><td>New pre-travel authorisation (being phased in)</td></tr>
<tr><th>Tourist Visa</th><td>Free for most Western nationalities</td></tr>
<tr><th>Stay Duration</th><td>Up to 90 days (most visa-free)</td></tr>
<tr><th>Processing Time</th><td>Decided at port of entry</td></tr>
<tr><th>Passport Validity</th><td>At least 6 months</td></tr>""",
    """<h2 id="introduction">Introduction</h2>
<p>Israel attracts tourists for its religious sites (Jerusalem's Old City, Bethlehem, Nazareth, Masada), beaches (Tel Aviv, Eilat), desert landscapes (Negev) and vibrant food scene. The Israel Population and Immigration Authority (PIBA) manages entry. Ben Gurion International Airport (TLV) near Tel Aviv is the main entry point.</p>
<h2 id="tourist">Visa-Free Entry</h2>
<p>Citizens of 90+ countries, including the US, UK, all EU member states, Canada, Australia, New Zealand, Japan, South Korea, Singapore and many others, may enter Israel visa-free for up to 90 days. No prior application is required — entry permission is given at the border. Note: Israel may refuse entry at its discretion; travelers may be asked about purpose of visit and accommodation.</p>
<h2 id="eta-il">ETA-IL (Coming Phase-In)</h2>
<p>Israel has announced an Electronic Travel Authorisation (ETA-IL) similar to the US ESTA, which will eventually be required for visa-free nationalities before travel. As of 2026, check the Israeli government site for the current implementation status.</p>
<h2 id="stamps">Passport Stamps &amp; Entry to Arab Countries</h2>
<p>Israel no longer stamps passports at request (since 2013). Israeli immigration officers typically stamp an entry card instead. However, some Arab countries may still question travelers about Israel visits. Check specific embassy requirements if you plan to visit Gulf states after Israel.</p>
<h2 id="documents">Required Documents</h2>
<ul><li>Valid passport (6+ months validity recommended)</li><li>Return or onward ticket</li><li>Accommodation details</li><li>Sufficient funds</li><li>Travel insurance (strongly recommended)</li></ul>
<h2 id="fees">Visa Fees</h2>
<table class="table table-bordered table-sm"><thead><tr><th>Visa Type</th><th>Fee</th></tr></thead><tbody>
<tr><td>Visa-free entry (90+ countries)</td><td>Free</td></tr>
<tr><td>ETA-IL (when active)</td><td>TBD</td></tr>
<tr><td>Regular Tourist Visa (B/2)</td><td>Approximately USD 20–30 at embassy</td></tr>
</tbody></table>
<h2 id="application-process">How to Apply</h2>
<ol><li>Check if your nationality is visa-exempt at <a href="https://www.gov.il/en/departments/immigration_authority" target="_blank" rel="noopener">Israel PIBA</a></li><li>If visa-free: no pre-application needed — just arrive with valid passport, onward ticket and accommodation details</li><li>If ETA-IL is active for your nationality: apply online before travel</li><li>If a visa is required: apply at your nearest Israeli embassy</li></ol>
<h2 id="official-links">Official Links</h2>
<ul><li><a href="https://www.gov.il/en/departments/immigration_authority" target="_blank" rel="noopener">Israel Population and Immigration Authority (PIBA)</a></li><li><a href="https://www.gov.il/en" target="_blank" rel="noopener">Israel Government Official Portal</a></li></ul>""",
    "https://www.gov.il/en/departments/immigration_authority", "Israel Population and Immigration Authority",
    [("Do I need a visa for Israel?","Most Western nationalities (US, UK, EU, Canada, Australia, Japan, South Korea, etc.) can enter Israel visa-free for up to 90 days. No pre-application is needed."),
     ("Will my passport get stamped in Israel?","Israel has not stamped passports on request since 2013. Immigration officers issue a separate entry card instead of stamping your passport."),
     ("Can I enter Arab countries after visiting Israel?","Most Arab countries no longer refuse entry based on Israeli visits. However, check specific requirements for countries you plan to visit after Israel."),
     ("What is the ETA-IL?","Israel's Electronic Travel Authorisation (ETA-IL) is a pre-travel permit being phased in for visa-exempt nationalities. Check the Israeli government website for current implementation status.")],
    ["Check if your nationality is visa-exempt at gov.il/en/departments/immigration_authority","If visa-free: no pre-application needed","Prepare: valid passport, return ticket, accommodation details, sufficient funds","Arrive at Ben Gurion Airport (TLV) or other entry point","Answer border control questions and receive entry stamp or card"]),

"peru": (
    "Peru", "pe",
    "Peru Visa Requirements 2026 — eVisa, Machu Picchu &amp; Entry Guide",
    "Peru is a top South American destination, home to Machu Picchu, the Amazon rainforest, Lake Titicaca and Lima's world-class gastronomy. Most nationalities enter Peru visa-free. Peru launched an eVisa system for some nationalities in 2023.",
    """<tr><th>Visa Exemption</th><td>Yes — citizens of 90+ countries (up to 90–183 days)</td></tr>
<tr><th>eVisa Available</th><td>Yes (for some nationalities) — visaelectronica.rree.gob.pe</td></tr>
<tr><th>Stay Duration</th><td>Up to 90 or 183 days (visa-free)</td></tr>
<tr><th>Visa Fee</th><td>USD 30 (eVisa)</td></tr>
<tr><th>Processing Time</th><td>3–10 business days</td></tr>
<tr><th>Passport Validity</th><td>At least 6 months</td></tr>""",
    """<h2 id="introduction">Introduction</h2>
<p>Peru is one of South America's most visited countries. Main airports: Jorge Chávez International (LIM) in Lima, Alejandro Velasco Astete (CUZ) in Cusco. Immigration is managed by the Superintendencia Nacional de Migraciones. Most tourists arrive visa-free and can stay up to 90 or 183 days depending on nationality.</p>
<h2 id="tourist">Visa-Free Entry</h2>
<p>Citizens of most Western countries, LATAM nations, and many Asian countries enter visa-free. US, UK, EU, Canada, Australia, Japan, South Korea, Chile, Argentina, Brazil and most other South American nationals do not need a visa. The period granted on entry is typically 90 days, which can sometimes be extended to 183 days total. The period is stamped in your passport on arrival.</p>
<h2 id="evisa">Peru eVisa</h2>
<p>For nationalities that require a visa, Peru offers an eVisa at visaelectronica.rree.gob.pe. The eVisa costs USD 30 and takes 3–10 business days to process. It allows a single entry for tourism or business.</p>
<h2 id="documents">Required Documents</h2>
<ul><li>Valid passport (6+ months validity)</li><li>Return or onward ticket</li><li>Accommodation details</li><li>Proof of sufficient funds</li></ul>
<h2 id="fees">Visa Fees</h2>
<table class="table table-bordered table-sm"><thead><tr><th>Visa Type</th><th>Fee</th></tr></thead><tbody>
<tr><td>Visa-free entry (most nationalities)</td><td>Free</td></tr>
<tr><td>Tourist eVisa</td><td>USD 30</td></tr>
<tr><td>Business Visa</td><td>USD 30–100 (varies by embassy)</td></tr>
</tbody></table>
<h2 id="application-process">How to Apply</h2>
<ol><li>Check if your nationality is visa-exempt at <a href="https://www.migraciones.gob.pe/servicios" target="_blank" rel="noopener">migraciones.gob.pe</a></li><li>If visa-free: arrive with valid passport, return ticket and accommodation details</li><li>If a visa is needed: apply at <a href="https://visaelectronica.rree.gob.pe" target="_blank" rel="noopener">visaelectronica.rree.gob.pe</a></li></ol>
<h2 id="official-links">Official Links</h2>
<ul><li><a href="https://www.migraciones.gob.pe/servicios" target="_blank" rel="noopener">Peru Superintendencia Nacional de Migraciones</a></li><li><a href="https://visaelectronica.rree.gob.pe" target="_blank" rel="noopener">Peru eVisa Portal</a></li></ul>""",
    "https://www.migraciones.gob.pe/servicios", "Peru Migraciones",
    [("Do I need a visa for Peru?","Most nationalities (US, UK, EU, Canada, Australia, Japan, South Korea etc.) can enter Peru visa-free for up to 90 days. Check migraciones.gob.pe for your country's requirements."),
     ("How long can I stay in Peru without a visa?","Most visa-exempt nationals receive up to 90 days on arrival. This can potentially be extended to 183 days at the discretion of immigration."),
     ("How do I visit Machu Picchu?","Machu Picchu requires an advance entry ticket from the official booking portal machupicchu.gob.pe. Tickets sell out weeks in advance, especially in peak season."),
     ("Is Peru safe for tourists?","Peru is a popular tourist destination, but standard travel precautions apply. Petty theft in crowded areas and altitude sickness (Cusco is at 3,400m) are the main risks to be aware of.")],
    ["Check if your nationality is visa-exempt at migraciones.gob.pe","Visa-free: arrive with valid passport, return ticket, accommodation details","If visa required: apply at visaelectronica.rree.gob.pe (USD 30)","Book Machu Picchu tickets in advance at machupicchu.gob.pe","Arrive at Lima (LIM) or Cusco (CUZ) and receive entry stamp"]),

"egypt": (
    "Egypt", "eg",
    "Egypt Visa Requirements 2026 — eVisa, Fees &amp; Entry Guide",
    "Egypt, land of the Pharaohs, Pyramids and the Nile, is one of the world's oldest civilisations and a top tourist destination. Most nationalities can obtain an Egyptian visa on arrival or apply online via the official eVisa portal.",
    """<tr><th>Visa on Arrival</th><td>Available for 70+ nationalities at Egyptian airports</td></tr>
<tr><th>eVisa Available</th><td>Yes — visa2egypt.gov.eg</td></tr>
<tr><th>Stay Duration</th><td>30 days (tourist visa)</td></tr>
<tr><th>Fee</th><td>USD 25 (visa on arrival / eVisa)</td></tr>
<tr><th>Processing Time</th><td>eVisa: 3–10 business days</td></tr>
<tr><th>Passport Validity</th><td>At least 6 months</td></tr>""",
    """<h2 id="introduction">Introduction</h2>
<p>Egypt attracts millions of visitors annually to its ancient monuments, Red Sea resorts (Sharm el-Sheikh, Hurghada) and vibrant cities (Cairo, Luxor, Aswan). Main airports are Cairo International (CAI), Sharm el-Sheikh (SSH) and Hurghada (HRG). The Egyptian Ministry of Interior manages immigration.</p>
<h2 id="voa">Visa on Arrival</h2>
<p>Citizens of 70+ nationalities can obtain a visa on arrival at Cairo, Sharm el-Sheikh, Hurghada and Alexandria airports. The fee is <strong>USD 25</strong> (pay in USD cash or sometimes by card). The visa allows a 30-day stay. Most Western nationalities (US, UK, EU, Canada, Australia, Japan, South Korea, New Zealand) are eligible.</p>
<h2 id="evisa">Egypt eVisa</h2>
<p>Apply in advance at <a href="https://www.visa2egypt.gov.eg" target="_blank" rel="noopener">visa2egypt.gov.eg</a>. The eVisa costs USD 25 for a single entry (30 days) or USD 60 for multiple entries. Processing takes 3–10 business days. Having an eVisa speeds up arrival as you skip the visa-on-arrival counter.</p>
<h2 id="free-zones">Sinai Stamp (Free Zone)</h2>
<p>Travelers entering <strong>only South Sinai</strong> (Sharm el-Sheikh, Dahab, Nuweiba, Saint Catherine) by direct flight or by sea from Jordan's Aqaba can receive a free 14-day Sinai-only stamp. This does NOT allow travel to the rest of Egypt including Cairo.</p>
<h2 id="documents">Required Documents</h2>
<ul><li>Valid passport (6+ months validity)</li><li>Return or onward ticket</li><li>Accommodation details</li><li>USD 25 (or credit card) for visa on arrival</li></ul>
<h2 id="fees">Visa Fees</h2>
<table class="table table-bordered table-sm"><thead><tr><th>Visa Type</th><th>Fee</th></tr></thead><tbody>
<tr><td>Visa on Arrival (single, 30 days)</td><td>USD 25</td></tr>
<tr><td>eVisa (single, 30 days)</td><td>USD 25</td></tr>
<tr><td>eVisa (multiple, 30 days)</td><td>USD 60</td></tr>
<tr><td>Sinai Free Zone (14 days)</td><td>Free</td></tr>
</tbody></table>
<h2 id="application-process">How to Apply</h2>
<ol><li>Check eligibility at <a href="https://www.visa2egypt.gov.eg" target="_blank" rel="noopener">visa2egypt.gov.eg</a></li><li>Apply for eVisa online and pay USD 25/60</li><li>Receive eVisa by email (3–10 days)</li><li>Or obtain visa on arrival at airport (USD 25 cash)</li></ol>
<h2 id="official-links">Official Links</h2>
<ul><li><a href="https://www.visa2egypt.gov.eg" target="_blank" rel="noopener">Egypt Official eVisa Portal</a></li><li><a href="https://www.touregypt.net" target="_blank" rel="noopener">Egypt Tourism Authority</a></li></ul>""",
    "https://www.visa2egypt.gov.eg", "Egypt Official eVisa Portal",
    [("Do I need a visa for Egypt?","Most Western nationalities can obtain a visa on arrival (USD 25) or apply in advance via the eVisa portal at visa2egypt.gov.eg."),
     ("How much is the Egypt visa?","The visa on arrival and eVisa both cost USD 25 for a single-entry 30-day visa. Multiple-entry eVisa costs USD 60."),
     ("What is the Sinai stamp?","The Sinai-only free 14-day stamp allows entry to South Sinai (Sharm el-Sheikh, Dahab) only. It does not allow travel to Cairo or the rest of Egypt."),
     ("How early should I apply for the Egypt eVisa?","Apply at least 1–2 weeks before travel to allow 3–10 business days processing time.")],
    ["Visit visa2egypt.gov.eg and create an account","Fill in personal and passport details","Pay USD 25 (single) or USD 60 (multiple) by card","Receive eVisa by email within 3–10 business days","Print or show eVisa on your phone at airport arrival"]),
}

# Template for simpler pages (for less-visited destinations)
SIMPLE_COUNTRIES = {
"ukraine": ("Ukraine","ua","Ukraine Visa Requirements 2026 — Entry Guide","Ukraine, home to Kyiv, Lviv and the Carpathians, has an eVisa system for some nationalities. Many Western countries enter visa-free for 90 days.","https://evisa.mfa.gov.ua","Ukraine Ministry of Foreign Affairs eVisa","Visa-free (90 days) for most Western nationalities; eVisa USD 20 for others."),
"georgia": ("Georgia","ge","Georgia Visa Requirements 2026 — Entry Guide","Georgia, a Caucasus gem with ancient monasteries and stunning mountains, allows citizens of 95+ countries to enter visa-free for up to 365 days (1 year). Georgia is one of the world's most liberal visa policies.","https://www.geoconsul.gov.ge","Georgia Ministry of Foreign Affairs","Visa-free up to 365 days for citizens of 95+ countries including US, UK, EU, Australia, Canada."),
"myanmar": ("Myanmar","mm","Myanmar Visa Requirements 2026 — eVisa &amp; Entry Guide","Myanmar (Burma), home to Bagan's temples and Inle Lake, offers an eVisa for most nationalities. Check current travel advisories before travel.","https://evisa.moip.gov.mm","Myanmar eVisa Official Portal","eVisa available for 100+ nationalities; USD 50 for tourist visa, valid 28 days."),
"laos": ("Laos","la","Laos Visa Requirements 2026 — Visa on Arrival &amp; eVisa","Laos, Southeast Asia's landlocked gem, offers visa on arrival and an eVisa system for most nationalities. The classic backpacker route includes Luang Prabang and the 4,000 Islands.","https://laoevisa.gov.la","Lao eVisa Official Portal","Visa on arrival (USD 30–42) or eVisa (USD 35) for most nationalities; 30-day stay."),
"chile": ("Chile","cl","Chile Visa Requirements 2026 — Visa-Free Entry Guide","Chile, stretching from the Atacama desert to Patagonia, allows citizens of most countries to enter visa-free. There is no eVisa system — most visitors are simply stamped in on arrival.","https://www.extranjeria.gob.cl","Chile Servicio Nacional de Migraciones","Visa-free for most nationalities (90 days). No eVisa system currently."),
"ecuador": ("Ecuador","ec","Ecuador Visa Requirements 2026 — Galapagos &amp; Entry Guide","Ecuador, home to the Galapagos Islands and Amazon rainforest, allows most nationalities to enter visa-free for up to 90 days (extendable to 180). A separate permit is required to visit the Galapagos.","https://www.consuladoecuador.org","Ecuador Ministry of Foreign Affairs","Visa-free for most nationalities (90 days, extendable to 180 days)."),
"bulgaria": ("Bulgaria","bg","Bulgaria Visa Requirements 2026 — Entry Guide","Bulgaria, on the Black Sea coast, is an EU member but not yet a full Schengen member. Most Western nationals enter visa-free. Schengen visa holders can enter Bulgaria without a separate visa.","https://www.mvr.bg/en","Bulgarian Ministry of Interior","Visa-free for most Western nationalities. Schengen visa also valid."),
"finland": ("Finland","fi","Finland Visa Requirements 2026 — Schengen Entry Guide","Finland, land of the Northern Lights, sauna culture and the Arctic, is a Schengen Area member. Most visitors enter on a Schengen visa or visa-free under the 90-day rule.","https://www.schengenvisainfo.com/finland-visa","Schengen Visa Info — Finland","Schengen rules apply. Visa-free for 90 days in 180 days for most Western nationalities."),
"slovenia": ("Slovenia","si","Slovenia Visa Requirements 2026 — Schengen Entry Guide","Slovenia, the green heart of Europe, is a Schengen Area member. Entry rules follow standard Schengen regulations. Visa-free for most Western nationalities.","https://www.gov.si/en/state-authority/ministries/ministry-of-interior","Slovenia Ministry of Interior","Schengen rules apply. Visa-free for 90 days in 180 days."),
"cyprus": ("Cyprus","cy","Cyprus Visa Requirements 2026 — Entry Guide","Cyprus, the Mediterranean island jewel, is an EU member but not in the Schengen Area. Citizens of many countries enter visa-free. Cyprus has its own visa system.","https://www.mfa.gov.cy/mfa/highcommissions/london.nsf/index_en/index_en","Cyprus Ministry of Foreign Affairs","Visa-free for most Western nationalities. EU citizens enter freely."),
"luxembourg": ("Luxembourg","lu","Luxembourg Visa Requirements 2026 — Schengen Entry Guide","Luxembourg, one of Europe's smallest and wealthiest countries, is a Schengen Area member. Entry follows standard Schengen rules.","https://maee.gouvernement.lu/en","Luxembourg Ministry of Foreign Affairs","Schengen rules apply. Visa-free for 90 days in 180 days."),
"iran": ("Iran","ir","Iran Visa Requirements 2026 — Entry Guide","Iran requires most nationalities to obtain a visa in advance through an embassy, or in some cases via visa on arrival at Tehran Imam Khomeini International Airport. Check current advisories before travel.","https://mfa.ir/en","Iran Ministry of Foreign Affairs","Visa required for most nationalities. Some nationalities receive visa on arrival."),
"iraq": ("Iraq","iq","Iraq Visa Requirements 2026 — Entry Guide","Iraq requires most nationalities to obtain a visa in advance. Kurdish Region of Iraq (Erbil) offers visa on arrival for many nationalities. Check current travel advisories before travel.","https://www.mofa.gov.iq/en","Iraq Ministry of Foreign Affairs","Visa required for most nationalities. Kurdistan Region: visa on arrival available."),
"panama": ("Panama","pa","Panama Visa Requirements 2026 — Entry Guide","Panama, home to the Panama Canal and vibrant Casco Viejo, allows most nationalities to enter visa-free for 90 days. Panama does not require a visa for most Western travelers.","https://www.migracion.gob.pa","Panama National Migration Service","Visa-free for most nationalities (90 days). No eVisa system."),
"nicaragua": ("Nicaragua","ni","Nicaragua Visa Requirements 2026 — Entry Guide","Nicaragua, Central America's largest country, allows most Western nationalities to enter visa-free for 90 days (extendable). Nicaragua uses the CA-4 agreement allowing free movement between Guatemala, Honduras, El Salvador and Nicaragua.","https://www.migración.gob.ni","Nicaragua Migración","Visa-free for most Western nationalities (90 days, CA-4 border agreement)."),
"belize": ("Belize","bz","Belize Visa Requirements 2026 — Entry Guide","Belize, English-speaking gateway to Mesoamerican reefs and ancient Maya ruins, allows most nationalities to enter visa-free for up to 30 days (extendable at immigration offices). No eVisa system.","https://www.immigration.gov.bz","Belize Immigration","Visa-free for most nationalities (30 days, extendable)."),
"uruguay": ("Uruguay","uy","Uruguay Visa Requirements 2026 — Entry Guide","Uruguay, South America's most stable democracy, allows most nationalities to enter visa-free for 90 days. No eVisa is required. Present at Montevideo (MVD) or Punta del Este (PDP) airports.","https://www.gub.uy/ministerio-relaciones-exteriores","Uruguay Ministry of Foreign Affairs","Visa-free for most nationalities (90 days)."),
"venezuela": ("Venezuela","ve","Venezuela Visa Requirements 2026 — Entry Guide","Venezuela requires most nationalities to obtain a visa in advance, though some nationalities enter visa-free. Check current travel advisories before travel as the situation changes frequently.","https://www.mppre.gob.ve","Venezuela Ministry of Foreign Affairs","Visa may be required. Check your country's specific requirements and current travel advisories."),
"brunei": ("Brunei","bn","Brunei Visa Requirements 2026 — Entry Guide","Brunei Darussalam, a wealthy sultanate on the island of Borneo, allows citizens of many countries to enter visa-free. Most Western nationalities enter for up to 14 or 30 days without a visa.","https://www.immigration.gov.bn","Brunei Immigration Department","Visa-free for most Western nationalities (14–30 days)."),
"kuwait": ("Kuwait","kw","Kuwait Visa Requirements 2026 — eVisa &amp; Entry Guide","Kuwait, a Gulf state known for its modernity and oil wealth, allows eligible nationals to obtain an eVisa online at evisa.moi.gov.kw. Many nationalities receive free visa on arrival.","https://evisa.moi.gov.kw","Kuwait eVisa Portal","Visa on arrival (free) or eVisa for most Western nationalities."),
"iceland": ("Iceland","is","Iceland Visa Requirements 2026 — Schengen Entry Guide","Iceland, land of the Northern Lights, volcanoes and geysers, is a member of the Schengen Area. Entry follows standard Schengen rules. Visa-free for most Western nationalities.","https://www.utl.is/index.php/en","Iceland Directorate of Immigration","Schengen rules apply. Visa-free for 90 days in 180 days."),
"fiji": ("Fiji","fj","Fiji Visa Requirements 2026 — Entry Guide","Fiji, the South Pacific island paradise, allows most nationalities to enter visa-free for 4 months (120 days). No eVisa is required for most visitors.","https://www.immigration.gov.fj","Fiji Immigration Department","Visa-free for most nationalities (120 days)."),
"bahamas": ("Bahamas","bs","Bahamas Visa Requirements 2026 — Entry Guide","The Bahamas, a Caribbean archipelago of 700 islands, allows most nationalities to enter visa-free for up to 8 months. Most visitors arrive by cruise ship or flight from the US. No eVisa required.","https://www.immigration.gov.bs","Bahamas Immigration","Visa-free for most nationalities (up to 8 months)."),
"macau": ("Macau","mo","Macau Visa Requirements 2026 — Entry Guide","Macau, a Special Administrative Region of China, operates independently from mainland China for immigration. Most nationalities enter visa-free for 30–90 days. No eVisa required for most visitors.","https://www.fsm.gov.mo/psp/eng/intro.html","Macau Public Security Police Force","Visa-free for most nationalities (30–90 days)."),
"andorra": ("Andorra","ad","Andorra Visa Requirements 2026 — Entry Guide","Andorra, a tiny principality in the Pyrenees between France and Spain, has no official border with EU Schengen states. To visit Andorra, you must enter through France or Spain and hold a valid Schengen visa (if required for your nationality).","https://www.exteriors.ad/en","Andorra Ministry of Foreign Affairs","No direct visa — enter via France/Spain. Schengen visa required if applicable."),
"moldova": ("Moldova","md","Moldova Visa Requirements 2026 — Entry Guide","Moldova allows citizens of many countries to enter visa-free. EU/EEA citizens and citizens of the UK, US, Canada, Japan and many other countries can enter without a visa for up to 90 days.","https://mfa.gov.md/en","Moldova Ministry of Foreign Affairs","Visa-free for most Western nationalities (90 days)."),
"guatemala": ("Guatemala","gt","Guatemala Visa Requirements 2026 — Entry Guide","Guatemala, home to ancient Maya temples and stunning Lake Atitlán, allows most nationalities to enter visa-free for 90 days under the CA-4 agreement (Guatemala, Honduras, El Salvador, Nicaragua).","https://migracion.gob.gt","Guatemala Migración","Visa-free for most Western nationalities (90 days, CA-4 agreement)."),
"bermuda": ("Bermuda","bm","Bermuda Visa Requirements 2026 — Entry Guide","Bermuda, a British Overseas Territory in the North Atlantic, allows most nationalities to enter without a visa for up to 90 days. Entry is via L.F. Wade International Airport (BDA).","https://www.gov.bm/department/immigration","Bermuda Immigration","Visa-free for most nationalities (90 days)."),
"angola": ("Angola","ao","Angola Visa Requirements 2026 — eVisa &amp; Entry Guide","Angola, on Africa's southwest coast, offers an eVisa system for most nationalities at svisa.minjusdh.gov.ao. The tourist eVisa is valid for 30 days.","https://svisa.minjusdh.gov.ao","Angola eVisa Portal","eVisa required for most nationalities (USD 80–120, 30 days)."),
"cape-verde": ("Cape Verde","cv","Cape Verde Visa Requirements 2026 — EASE Pre-Registration","Cape Verde (Cabo Verde), an archipelago off the West African coast, requires most nationalities to complete the EASE pre-registration (evisa.ease.gov.cv) before arrival. It's not a visa — entry is free, but registration is mandatory.","https://ease.gov.cv","Cape Verde EASE Portal","Mandatory EASE pre-registration online before travel. Entry itself is free for most nationalities."),
"slovakia": ("Slovakia","sk","Slovakia Visa Requirements 2026 — Schengen Entry Guide","Slovakia, a Central European gem with medieval castles and the Tatra mountains, is a Schengen Area member. Entry follows standard Schengen rules.","https://www.mzv.sk/en","Slovakia Ministry of Foreign Affairs","Schengen rules apply. Visa-free for 90 days in 180 days."),
"tonga": ("Tonga","to","Tonga Visa Requirements 2026 — Entry Guide","Tonga, a Pacific Island kingdom, allows most nationalities to enter visa-free for 30 days on arrival. Extensions are available.","https://www.immigration.gov.to","Tonga Immigration Department","Visa-free for most nationalities (30 days on arrival)."),
"liechtenstein": ("Liechtenstein","li","Liechtenstein Visa Requirements 2026 — Schengen Entry Guide","Liechtenstein, one of the world's smallest countries, is a Schengen Area member. Entry follows standard Schengen rules via Switzerland or Austria.","https://www.llv.li/en","Liechtenstein Government","Schengen rules apply. Enter via Switzerland or Austria."),
"cook-islands": ("Cook Islands","ck","Cook Islands Visa Requirements 2026 — Entry Guide","The Cook Islands, a New Zealand-associated Pacific paradise, allows most nationalities to enter visa-free for 31 days (extendable to 6 months). Rarotonga is the main island.","https://www.immigration.gov.ck","Cook Islands Immigration Service","Visa-free for most nationalities (31 days, extendable to 6 months)."),
"samoa": ("Samoa","ws","Samoa Visa Requirements 2026 — Entry Guide","Samoa, an independent Pacific nation, allows most nationalities to enter visa-free for 60 days. Faleolo International Airport (APW) is the main entry point.","https://www.samoaimmigration.gov.ws","Samoa Immigration","Visa-free for most nationalities (60 days)."),
"bhutan": ("Bhutan","bt","Bhutan Visa Requirements 2026 — Entry Guide","Bhutan, the 'Last Shangri-La', requires most nationalities to obtain a visa and pay a Sustainable Development Fee (SDF) of USD 100/day. Only Indian, Bangladeshi and Maldivian nationals enter visa-free. All others must book through a licensed Bhutan tour operator.","https://www.bhutantourism.bt","Tourism Council of Bhutan","Visa required. SDF: USD 100/person/night. Must book via licensed Bhutan tour operator."),
}

# JS block
JS_BLOCK = """    <div class="show fullscreen" id="ftco-loader">
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
    <script src="../js/main.js"></script>"""

def navbar(slug):
    return f"""<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light" id="ftco-navbar" style="background-color:#0d2461 !important;position:relative;z-index:10;">
<div class="container">
    <a class="navbar-brand" href="../index.html" style="padding:0;"><img src="../images/logo.png" alt="eVisa-Card.com" style="height:120px;width:auto;display:block;"></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation"><span class="oi oi-menu"></span> Menu</button>
    <div class="collapse navbar-collapse justify-content-center" id="ftco-nav">
        <ul class="navbar-nav align-items-center">
            <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
            <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
            <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
            <li class="nav-item"><a class="nav-link" href="/en/expat-guides.html">Guides</a></li>
            <li class="nav-item dropdown ml-3">
                <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                    <span class="fi fi-gb"></span> English</a>
                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                    <a class="dropdown-item active" href="/en/visa-{slug}.html"><span class="fi fi-gb"></span> English</a>
                    <a class="dropdown-item" href="/fr/visa-{slug}.html"><span class="fi fi-fr"></span> Français</a>
                    <a class="dropdown-item" href="/es/visa-{slug}.html"><span class="fi fi-es"></span> Español</a>
                    <a class="dropdown-item" href="/pt/visa-{slug}.html"><span class="fi fi-br"></span> Português</a>
                    <a class="dropdown-item" href="/zh/destination.html"><span class="fi fi-cn"></span> 中文</a>
                    <a class="dropdown-item" href="/th/destination.html"><span class="fi fi-th"></span> ไทย</a>
                    <a class="dropdown-item" href="/ru/destination.html"><span class="fi fi-ru"></span> Русский</a>
                    <a class="dropdown-item" href="/ar/destination.html"><span class="fi fi-sa"></span> العربية</a>
                    <a class="dropdown-item" href="/ja/destination.html"><span class="fi fi-jp"></span> 日本語</a>
                    <a class="dropdown-item" href="/ko/destination.html"><span class="fi fi-kr"></span> 한국어</a>
                </div>
            </li>
        </ul>
    </div>
</div>
</nav>"""

def head(slug, name, title, desc, flag):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/visa-{slug}.html"/>
    <meta property="og:title" content="{title}"/>
    <meta property="og:description" content="{desc}"/>
    <meta property="og:type" content="website"/>
    <meta property="og:url" content="https://www.evisa-card.com/en/visa-{slug}.html"/>
    <meta property="og:image" content="https://www.evisa-card.com/images/og-image.jpg"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/visa-{slug}.html"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/visa-{slug}.html"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&amp;display=swap" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/owl.carousel.min.css" rel="stylesheet"/>
    <link href="../css/owl.theme.default.min.css" rel="stylesheet"/>
    <link href="../css/magnific-popup.css" rel="stylesheet"/>
    <link href="../css/bootstrap-datepicker.css" rel="stylesheet"/>
    <link href="../css/jquery.timepicker.css" rel="stylesheet"/>
    <link href="../css/flaticon.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>"""

def footer(lang="en"):
    return f"""<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <p class="mt-4">&copy; 2026 eVisa-Card.com &mdash; Global eVisa &amp; Travel Information Platform</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="/{lang}/legal-notice.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">Legal Notice</a>
                    &nbsp;|&nbsp;
                    <a href="/{lang}/disclaimer.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">Disclaimer</a>
                </p>
            </div>
        </div>
    </div>
</footer>"""

def eeat(name, official_url, official_label):
    return f"""<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
  <div class="d-flex align-items-start">
    <div class="mr-3"><span class="fa fa-shield fa-2x text-info"></span></div>
    <div>
      <strong>Editorial Team &mdash; eVisa-Card.com</strong>
      <p class="mb-1 small text-muted">This guide is maintained by our visa research team. Last updated: <strong>March 2026</strong>.</p>
      <p class="mb-0 small"><strong>Important:</strong> Visa rules change frequently. Always verify current requirements at <a href="{official_url}" target="_blank" rel="noopener">{official_label}</a> before travel. This page is for informational purposes only.</p>
    </div>
  </div>
</div>"""

def make_full_page(slug, name, flag, h1, intro, table_rows, sections, official_url, official_label, faq_list, apply_steps):
    desc_text = intro[:155] + "..." if len(intro) > 155 else intro
    title = h1.replace("&amp;","&").replace("&","and")[:60] + (" 2026" if "2026" not in h1 else "")
    title_tag = h1 if len(h1.replace("&amp;","").replace("&amp;","")) < 65 else h1

    faq_json = ",\n    ".join([
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faq_list
    ])
    steps_json = ",\n    ".join([
        f'{{"@type":"HowToStep","name":"Step {i+1}","text":"{s}"}}'
        for i, s in enumerate(apply_steps)
    ])

    html = f"""{head(slug, name, h1, desc_text, flag)}
<body>
{navbar(slug)}
<section class="ftco-section"><div class="container"><article class="country-page">
<h1><span class="fi fi-{flag} mr-2"></span>{h1}</h1>
<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — {name}</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>
{sections}
<p><em>Always verify current visa rules on official government sites before travel.</em></p>
{eeat(name, official_url, official_label)}
<div class="related-guides mt-5 pt-4 border-top">
  <h3 class="h5 mb-3">Related Visa Guides</h3>
  <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-thailand.html">Thailand</a>
  <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-japan.html">Japan</a>
  <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-india.html">India</a>
  <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>
</article></div></section>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {faq_json}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"HowTo",
  "name":"How to Apply for a {name} Visa",
  "description":"Step-by-step guide to applying for a {name} visa in 2026.",
  "step":[
    {steps_json}
  ]
}}
</script>
{footer()}
{JS_BLOCK}
</body>
</html>"""
    return html

def make_simple_page(slug, name, flag, title_str, intro, official_url, official_label, visa_summary):
    desc = intro[:155] + "..." if len(intro) > 155 else intro
    html = f"""{head(slug, name, title_str, desc, flag)}
<body>
{navbar(slug)}
<section class="ftco-section"><div class="container"><article class="country-page">
<h1><span class="fi fi-{flag} mr-2"></span>{title_str}</h1>
<p class="lead">{intro}</p>
<div class="alert alert-info"><strong>Visa Summary:</strong> {visa_summary}</div>
<h2 id="tourist">Tourist Entry</h2>
<p>{intro} For detailed and up-to-date requirements, always check the official immigration authority.</p>
<h2 id="documents">Typical Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity)</li>
<li>Return or onward flight ticket</li>
<li>Proof of accommodation</li>
<li>Sufficient funds for your stay</li>
<li>Travel insurance (recommended)</li>
</ul>
<h2 id="official-links">Official Links</h2>
<ul><li><a href="{official_url}" target="_blank" rel="noopener">{official_label}</a></li></ul>
<p><em>Always verify current visa rules on official government sites before travel.</em></p>
{eeat(name, official_url, official_label)}
<div class="related-guides mt-5 pt-4 border-top">
  <h3 class="h5 mb-3">Related Visa Guides</h3>
  <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-france.html">France</a>
  <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-spain.html">Spain</a>
  <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-germany.html">Germany</a>
  <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>
</article></div></section>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {{"@type":"Question","name":"Do I need a visa for {name}?","acceptedAnswer":{{"@type":"Answer","text":"{visa_summary}"}}}}
  ]
}}
</script>
{footer()}
{JS_BLOCK}
</body>
</html>"""
    return html

en_dir = os.path.join(BASE, "en")
created = 0

# Full pages
for slug, data in COUNTRIES.items():
    fname = f"visa-{slug}.html"
    out = os.path.join(en_dir, fname)
    if os.path.exists(out):
        print(f"  SKIP: {fname}")
        continue
    name, flag, h1, intro, table_rows, sections, official_url, official_label, faq_list, apply_steps = data
    html = make_full_page(slug, name, flag, h1, intro, table_rows, sections, official_url, official_label, faq_list, apply_steps)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created (full): {fname}")
    created += 1

# Simple pages
for slug, data in SIMPLE_COUNTRIES.items():
    fname = f"visa-{slug}.html"
    out = os.path.join(en_dir, fname)
    if os.path.exists(out):
        print(f"  SKIP: {fname}")
        continue
    name, flag, title_str, intro, official_url, official_label, visa_summary = data
    html = make_simple_page(slug, name, flag, title_str, intro, official_url, official_label, visa_summary)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created (simple): {fname}")
    created += 1

# visa-uk.html → redirect to visa-united-kingdom.html
uk_redir = os.path.join(en_dir, "visa-uk.html")
if not os.path.exists(uk_redir):
    with open(uk_redir, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;url=/en/visa-united-kingdom.html"/><link rel="canonical" href="https://www.evisa-card.com/en/visa-united-kingdom.html"/></head><body><a href="/en/visa-united-kingdom.html">UK Visa Requirements</a></body></html>')
    print("  Created: visa-uk.html (redirect)")
    created += 1

print(f"\nDONE — {created} EN pages created")

# ── lang index.html pages (hub redirect) ─────────────────────────────────────
LANG_NAMES = {"fr": ("Français","fr","fr","Destinations","Accueil","Toutes les destinations"),
              "es": ("Español","es","es","Destinos","Inicio","Todos los destinos"),
              "pt": ("Português","pt","br","Destinos","Início","Todos os destinos")}

for lang, (lname, lcode, lflag, dest_label, home_label, all_dest) in LANG_NAMES.items():
    idx = os.path.join(BASE, lang, "index.html")
    if os.path.exists(idx):
        print(f"  SKIP index: {lang}/index.html")
        continue
    with open(idx, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="utf-8"/>
    <meta http-equiv="refresh" content="0;url=/{lang}/destination.html"/>
    <link rel="canonical" href="https://www.evisa-card.com/{lang}/destination.html"/>
    <title>eVisa-Card.com — {lname}</title>
    <meta name="robots" content="noindex, follow"/>
</head>
<body>
<p><a href="/{lang}/destination.html">{dest_label}</a></p>
</body>
</html>""")
    print(f"  Created: {lang}/index.html (redirect)")
    created += 1

print(f"\nTotal: {created} files created")
