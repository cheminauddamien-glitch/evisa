#!/usr/bin/env python
"""
deep_enrich_visa_group1.py
Enriches the TOP 20 most important visa country pages in www/en/
with comprehensive visa data: visa types matrix, processing times,
health & character requirements, extension info, refusal & appeals, and enhanced FAQ.

Idempotent: checks for existing section IDs before injecting.
"""
import os
import re
import json

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "en")

# ---------------------------------------------------------------------------
# Country data registry
# ---------------------------------------------------------------------------
COUNTRIES = {
    "thailand": {
        "file": "thailand-visa-requirements.html",
        "name": "Thailand",
        "flag": "th",
        "visa_types": [
            ("Tourist", "Visa Exemption", "60 days (extendable 30 days)", "Free", "Passport with 6+ months validity, return ticket, proof of funds (THB 10,000)"),
            ("Tourist", "Tourist Visa (TR) Single Entry", "60 days (extendable 30 days)", "THB 2,000 (~USD 57)", "Passport, photo, return ticket, hotel booking, bank statement"),
            ("Tourist", "Tourist Visa (TR) Multiple Entry", "60 days per entry, valid 6 months", "THB 5,000 (~USD 143)", "Same as single entry + proof of income or savings"),
            ("Tourist", "Special Tourist Visa (STV)", "90 days per entry (2 extensions)", "THB 2,000", "Long-stay tourism, proof of accommodation, insurance"),
            ("Business", "Non-Immigrant B (Business)", "90 days (extendable to 1 year)", "THB 2,000 (single) / THB 5,000 (multi)", "Invitation letter from Thai company, corporate documents"),
            ("Work", "Non-Immigrant B (Employment)", "90 days (then Work Permit)", "THB 2,000", "Job offer from Thai employer, WP3 form, qualifications"),
            ("Work", "Smart Visa", "Up to 4 years", "Free", "Highly skilled professionals in targeted industries (S-curve)"),
            ("Work", "BOI Promotion Visa", "1-4 years", "Free", "Board of Investment promoted company sponsorship"),
            ("Student", "Non-Immigrant ED", "90 days (extendable yearly)", "THB 2,000", "Acceptance letter from Thai educational institution"),
            ("Family", "Non-Immigrant O (Family)", "90 days (extendable yearly)", "THB 2,000", "Marriage certificate or birth certificate of Thai family member"),
            ("Retirement", "Non-Immigrant O-A (Retirement)", "1 year (renewable)", "THB 2,000", "Age 50+, THB 800,000 in bank or THB 65,000/month income, health insurance"),
            ("Retirement", "Non-Immigrant O-X (10-Year)", "5 years + 5 years", "THB 10,000", "Age 50+, THB 3,000,000 in bank, health insurance"),
            ("Retirement", "Thailand Privilege (Elite)", "5-20 years", "THB 600,000 - 2,140,000", "Investment/membership fee, no age or income requirements"),
            ("Digital Nomad", "DTV (Destination Thailand Visa)", "180 days (extendable 180 days)", "THB 10,000", "Remote workers, freelancers, proof of employment/contract"),
            ("Transit", "Transit Visa (TS)", "30 days", "THB 800", "Confirmed onward ticket within 30 days"),
            ("Diplomatic", "Diplomatic / Official Visa", "Duration of assignment", "Free", "Diplomatic passport, government assignment letter"),
            ("Investor", "Non-Immigrant B (Investment)", "1 year (renewable)", "THB 2,000", "Minimum THB 10 million investment in approved business"),
            ("Long-Term Resident", "LTR Visa", "10 years", "THB 50,000", "Wealthy pensioners, wealthy global citizens, work-from-Thailand professionals, highly skilled professionals"),
        ],
        "processing_times": [
            ("Visa Exemption", "Instant (on arrival)", "N/A", "N/A"),
            ("Tourist Visa (TR)", "5-7 business days", "2-3 business days", "THB 1,000 surcharge"),
            ("Non-Immigrant B", "5-10 business days", "3-5 business days", "THB 1,000 surcharge"),
            ("Non-Immigrant ED", "5-10 business days", "3-5 business days", "THB 1,000 surcharge"),
            ("Non-Immigrant O/O-A", "5-10 business days", "3-5 business days", "THB 1,000 surcharge"),
            ("Smart Visa", "30 business days", "N/A", "N/A"),
            ("LTR Visa", "20 business days", "N/A", "N/A"),
            ("DTV", "5-10 business days", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for Non-Immigrant O-A (retirement) visa — must be performed by an approved hospital. Certificate must show applicant is free from leprosy, tuberculosis, elephantiasis, drug addiction, and syphilis.</li>
<li><strong>Health insurance:</strong> Mandatory for O-A retirement visa — minimum THB 40,000 outpatient and THB 400,000 inpatient coverage from a Thai-approved insurer. Recommended for all other visa types.</li>
<li><strong>Vaccinations:</strong> Yellow fever certificate required if arriving from an endemic country. No other mandatory vaccinations but Hepatitis A/B and Typhoid recommended.</li>
<li><strong>COVID-19:</strong> No vaccination or testing requirements as of 2026.</li>
<li><strong>Police clearance:</strong> Required for work permits, O-A retirement visa, and LTR visa. Must be apostilled or authenticated and less than 6 months old.</li>
<li><strong>Biometrics:</strong> Fingerprints and photographs collected at port of entry for all foreign nationals.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Visa-exempt entry:</strong> Extendable by 30 days at any Immigration Office — fee THB 1,900. Maximum total stay 90 days.</li>
<li><strong>Tourist Visa (TR):</strong> Extendable by 30 days at Immigration — fee THB 1,900. Total maximum 90 days per entry.</li>
<li><strong>Non-Immigrant visas:</strong> Can be extended at Immigration Bureau in Bangkok or provincial offices. Extensions range from 90 days to 1 year depending on category.</li>
<li><strong>Retirement O-A:</strong> Renewable annually at Immigration — must maintain THB 800,000 bank balance and valid health insurance.</li>
<li><strong>90-day reporting:</strong> All foreign nationals staying over 90 days must report to Immigration every 90 days (in person, online, or by mail).</li>
<li><strong>Overstay penalties:</strong> THB 500 per day (max THB 20,000). Overstay exceeding 90 days can result in multi-year re-entry bans.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient financial proof, incomplete documentation, previous overstay in Thailand, criminal record, suspected intention to work on a tourist visa, lack of confirmed accommodation.</li>
<li><strong>Appeal process:</strong> Thailand does not have a formal appeal process for visa refusals. Applicants may reapply with improved documentation after addressing the reasons for refusal.</li>
<li><strong>Reapplication:</strong> There is no mandatory waiting period to reapply. Applicants should submit the application to the same or different Thai embassy/consulate with strengthened supporting documents.</li>
<li><strong>Blacklist:</strong> Travelers deported or with significant overstays may be placed on a blacklist preventing re-entry for 1-10 years depending on the offense.</li>
</ul>""",
        "extra_faqs": [
            ("How long can I stay in Thailand without a visa in 2026?", "Citizens of 93 countries can stay in Thailand visa-free for up to 60 days. This can be extended by 30 days at any Thai Immigration Office for THB 1,900, giving a maximum stay of 90 days."),
            ("What is the Thailand DTV (Digital Nomad Visa)?", "The Destination Thailand Visa (DTV) launched in 2024 allows remote workers, freelancers, and digital nomads to stay in Thailand for 180 days (extendable by another 180 days). The fee is THB 10,000 and applicants need to show proof of remote employment or freelance contracts."),
            ("Do I need health insurance for a Thailand retirement visa?", "Yes. The Non-Immigrant O-A retirement visa requires mandatory health insurance from a Thai-approved insurer with minimum coverage of THB 40,000 for outpatient and THB 400,000 for inpatient treatment."),
            ("What happens if I overstay my Thailand visa?", "Overstay fines are THB 500 per day up to a maximum of THB 20,000. If caught by authorities, you may be detained and deported. Overstays exceeding 90 days result in re-entry bans ranging from 1 to 10 years."),
            ("Can I convert a tourist visa to a work visa in Thailand?", "You cannot directly convert a tourist visa to a work visa inside Thailand. You must exit the country and apply for a Non-Immigrant B visa at a Thai embassy abroad, or your employer can arrange a change of visa category in certain cases through Immigration Bureau with a valid job offer."),
        ],
    },
    "usa": {
        "file": "usa-visa-requirements.html",
        "name": "USA",
        "flag": "us",
        "visa_types": [
            ("Tourist/Visitor", "B-1 (Business Visitor)", "Up to 6 months", "USD 185", "DS-160, interview, business purpose letter, ties to home country"),
            ("Tourist/Visitor", "B-2 (Tourist/Medical)", "Up to 6 months", "USD 185", "DS-160, interview, travel itinerary, financial evidence"),
            ("Tourist/Visitor", "ESTA (Visa Waiver Program)", "90 days", "USD 21", "Passport from VWP country, no prior visa refusals/overstays"),
            ("Work", "H-1B (Specialty Occupation)", "3 years (extendable to 6)", "USD 185 + USD 460 petition", "Bachelor's degree, employer sponsorship, labor condition application"),
            ("Work", "H-2A (Temporary Agricultural)", "Up to 1 year", "USD 185 + petition", "Employer sponsorship, seasonal agricultural work"),
            ("Work", "H-2B (Temporary Non-Agricultural)", "Up to 1 year", "USD 185 + petition", "Employer sponsorship, temporary non-agricultural work"),
            ("Work", "L-1A/L-1B (Intracompany Transfer)", "Up to 7 years (L-1A) / 5 years (L-1B)", "USD 185 + USD 460 petition", "Managerial/executive role or specialized knowledge, 1 year employment with company"),
            ("Work", "O-1 (Extraordinary Ability)", "Up to 3 years", "USD 185 + USD 460 petition", "Extraordinary ability in sciences, arts, education, business, or athletics"),
            ("Work", "E-2 (Treaty Investor)", "2 years (renewable)", "USD 315", "Substantial investment in US business, treaty country citizen"),
            ("Work", "TN (USMCA Professional)", "3 years (renewable)", "USD 185", "Canadian/Mexican citizen, qualifying profession under USMCA"),
            ("Student", "F-1 (Academic Student)", "Duration of study + 60 days", "USD 185 + USD 350 SEVIS", "I-20 from SEVP-certified school, financial evidence"),
            ("Student", "M-1 (Vocational Student)", "Duration of study + 30 days", "USD 185 + USD 350 SEVIS", "I-20 from vocational institution, financial proof"),
            ("Student", "J-1 (Exchange Visitor)", "Duration of program", "USD 185 + USD 220 SEVIS", "DS-2019 from exchange program sponsor"),
            ("Family", "K-1 (Fiance(e))", "90 days to marry", "USD 185 + USD 535 petition", "US citizen petitioner, proof of genuine relationship, meeting within 2 years"),
            ("Family", "IR/CR (Spouse of US Citizen)", "Permanent", "USD 185 + USD 535 petition + USD 325 immigrant fee", "Marriage certificate, I-130 petition from US citizen spouse"),
            ("Investor", "EB-5 (Immigrant Investor)", "Permanent (conditional 2 years)", "USD 185 + USD 3,675 petition", "USD 1,050,000 investment (USD 800,000 in TEA), job creation for 10 US workers"),
            ("Transit", "C-1 (Transit)", "Up to 29 days", "USD 185", "Confirmed onward ticket, visa to destination country"),
            ("Crew", "C-1/D (Transit/Crew)", "Duration of port stay", "USD 185", "Airline or shipping company employment letter"),
            ("Diplomatic", "A-1/A-2 (Diplomatic)", "Duration of assignment", "Free", "Diplomatic passport, government note verbale"),
            ("Media", "I (Media/Journalist)", "Duration of assignment", "USD 185", "Press credentials, employer letter from media organization"),
        ],
        "processing_times": [
            ("ESTA (VWP)", "Usually instant (up to 72 hours)", "N/A", "N/A"),
            ("B-1/B-2 Tourist/Business", "3-5 business days after interview", "N/A (no expedite available)", "N/A"),
            ("H-1B", "3-6 months (regular), subject to cap lottery", "15 calendar days (Premium Processing)", "USD 2,805"),
            ("L-1A/L-1B", "2-6 months", "15 calendar days (Premium Processing)", "USD 2,805"),
            ("O-1", "2-6 months", "15 calendar days (Premium Processing)", "USD 2,805"),
            ("F-1 Student", "2-8 weeks after interview", "N/A", "N/A"),
            ("K-1 Fiance", "12-18 months total", "N/A", "N/A"),
            ("EB-5 Investor", "24-52 months", "N/A", "N/A"),
            ("E-2 Treaty Investor", "2-6 weeks after interview", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam (immigrant visas only):</strong> Required for all immigrant visa applicants (Green Card). Performed by a USCIS-designated panel physician. Includes physical exam, blood tests, chest X-ray, and review of vaccination history.</li>
<li><strong>Vaccinations (immigrant visas):</strong> Must show proof of: Mumps, Measles, Rubella, Polio, Tetanus/Diphtheria, Pertussis, Hepatitis A & B, Influenza, Varicella, Pneumococcal, Rotavirus (age-appropriate), and COVID-19.</li>
<li><strong>Nonimmigrant visas:</strong> No routine medical exam required for tourist, student, or work visas. However, applicants with known communicable diseases (e.g., tuberculosis) may be required to undergo examination.</li>
<li><strong>Police clearance:</strong> Required for immigrant visas — applicants aged 16+ must provide police certificates from all countries where they lived for 6+ months after age 16.</li>
<li><strong>Biometrics:</strong> Fingerprints collected at the visa interview (consulate) or ASC (Application Support Center) for adjustment of status applicants within the US.</li>
<li><strong>Inadmissibility grounds:</strong> Communicable diseases of public health significance, drug abuse/addiction, mental disorders with harmful behavior, and failure to show required vaccinations can result in visa denial under INA Section 212(a)(1).</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>B-1/B-2 extension:</strong> Can be extended by filing Form I-539 with USCIS before current status expires. Maximum total stay generally 1 year. Fee: USD 370. Processing: 5-12 months.</li>
<li><strong>ESTA/VWP:</strong> Cannot be extended. Maximum 90 days with no exceptions. Must leave the US before the 90 days expire.</li>
<li><strong>F-1 Student:</strong> Valid for duration of status (D/S). Program extensions require updated I-20 from the school. No separate extension filing needed.</li>
<li><strong>H-1B Work:</strong> Extendable in 3-year increments up to 6 years total. Extensions beyond 6 years possible if I-140 approved or labor certification pending for 365+ days (AC21).</li>
<li><strong>Change of status:</strong> Possible within the US by filing I-539 (nonimmigrant) or I-485 (immigrant). Cannot change status if entered on VWP/ESTA, C-1 transit, or crew visa.</li>
<li><strong>Overstay consequences:</strong> Overstaying more than 180 days triggers a 3-year re-entry bar. Overstaying 1+ year triggers a 10-year bar. ESTA overstays permanently disqualify from VWP.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Section 214(b) — failure to demonstrate non-immigrant intent (most common for B and F visas). Insufficient financial evidence, weak ties to home country, prior immigration violations, incomplete DS-160, criminal inadmissibility, prior visa fraud.</li>
<li><strong>Section 221(g) — Administrative Processing:</strong> Application placed on hold for additional review. Can last weeks to months. Applicant may be asked to submit additional documents. Not a final refusal.</li>
<li><strong>Appeal process:</strong> There is no formal appeal for nonimmigrant visa refusals. Applicants may reapply at any time by paying a new MRV fee and scheduling a new interview. The consular officer's decision is generally final under INA 104(a).</li>
<li><strong>Reapplication:</strong> No mandatory waiting period. However, applicants should only reapply when their circumstances have materially changed. Submitting the same application repeatedly without changes is unlikely to result in a different outcome.</li>
<li><strong>Immigrant visa refusals:</strong> May be overcome by submitting requested evidence (for 221(g)) or filing a waiver (for certain inadmissibility grounds under INA 212(d)(3) or I-601).</li>
</ul>""",
        "extra_faqs": [
            ("What is the difference between ESTA and a US tourist visa?", "ESTA is an automated travel authorization for citizens of 40+ Visa Waiver Program countries, allowing 90-day visits for USD 21 with no interview. A B-2 tourist visa requires a DS-160 form, USD 185 fee, and a consular interview, but allows stays of up to 6 months and can be extended."),
            ("How long is the US visa interview wait time in 2026?", "Interview wait times vary significantly by embassy. Major cities like Mumbai, Manila, and Bogota may have waits of 200-600+ days for B-1/B-2 appointments. European and East Asian posts typically have shorter waits of 10-60 days. Check travel.state.gov for current wait times at your embassy."),
            ("Can I work in the US on a tourist visa?", "No. The B-1/B-2 visa strictly prohibits employment. Working without authorization is a violation that can result in deportation, visa revocation, and bars on future US entry. Work authorization requires a separate visa such as H-1B, L-1, O-1, or an employment-based green card."),
            ("What is US visa administrative processing (Section 221g)?", "Administrative processing under Section 221(g) occurs when the consular officer needs additional information or security clearance. Your passport is typically retained, and the case can take weeks to months. It is not a refusal but a pending status. You can check the status at ceac.state.gov."),
            ("How much bank balance is needed for a US tourist visa?", "There is no fixed minimum, but applicants should demonstrate sufficient funds to cover all travel expenses. Generally, showing USD 5,000-10,000 in savings along with stable income and employment is considered adequate. The key factor is showing consistent financial history, not just a large current balance."),
        ],
    },
    "australia": {
        "file": "australia-visa-requirements.html",
        "name": "Australia",
        "flag": "au",
        "visa_types": [
            ("Tourist/Visitor", "ETA (Subclass 601)", "90 days per visit, valid 12 months", "AUD 20", "Passport from 8 eligible countries (US, UK, Canada, Japan, etc.), no TB history"),
            ("Tourist/Visitor", "eVisitor (Subclass 651)", "90 days per visit, valid 12 months", "Free", "EU/EEA passport holders, no criminal convictions"),
            ("Tourist/Visitor", "Visitor Visa (Subclass 600)", "3, 6, or 12 months", "AUD 190", "All nationalities, financial evidence, genuine temporary entrant"),
            ("Business", "Business Visitor (Subclass 600 Business Stream)", "Up to 3 months", "AUD 190", "Business activities only (no work), invitation from Australian business"),
            ("Work", "Temporary Skill Shortage (Subclass 482)", "2 years (Short-term) / 4 years (Medium-term)", "AUD 1,455 - 3,035", "Employer sponsorship, skills assessment, English proficiency (IELTS 5.0+)"),
            ("Work", "Employer Nomination Scheme (Subclass 186)", "Permanent", "AUD 4,640", "Employer nomination, skills assessment, 3 years relevant experience"),
            ("Work", "Skilled Independent (Subclass 189)", "Permanent", "AUD 4,640", "Points test (65+), skills assessment, English proficiency, EOI via SkillSelect"),
            ("Work", "Skilled Nominated (Subclass 190)", "Permanent", "AUD 4,640", "State/territory nomination, points test (65+), skills on state list"),
            ("Work", "Skilled Work Regional (Subclass 491)", "5 years provisional", "AUD 4,640", "State nomination or family sponsorship, regional area, points test (65+)"),
            ("Work", "Working Holiday (Subclass 417)", "12 months", "AUD 635", "Age 18-30 (35 for some countries), eligible passport, first-time applicant"),
            ("Work", "Work and Holiday (Subclass 462)", "12 months", "AUD 635", "Age 18-30, eligible passport, government support letter, functional English"),
            ("Work", "Global Talent (Subclass 858)", "Permanent", "AUD 4,640", "Exceptional talent in target sector, nominator, salary above threshold (AUD 167,500)"),
            ("Student", "Student Visa (Subclass 500)", "Duration of course + 2 months", "AUD 710", "CoE from CRICOS provider, GTE requirement, financial capacity, OSHC, English test"),
            ("Student", "Student Guardian (Subclass 590)", "Duration of student's visa", "AUD 710", "Guardian of student under 18, welfare arrangement"),
            ("Family", "Partner Visa (Subclass 309/100)", "Temporary then Permanent", "AUD 8,850", "Genuine relationship with Australian citizen/PR, joint financial/social evidence"),
            ("Family", "Parent Visa (Subclass 143)", "Permanent", "AUD 4,990 + AUD 47,755 second installment", "Child is settled Australian citizen/PR, balance of family test"),
            ("Family", "Child Visa (Subclass 101)", "Permanent", "AUD 2,880", "Dependent child of Australian citizen/PR"),
            ("Investor", "Business Innovation & Investment (Subclass 188/888)", "Provisional 5 years then Permanent", "AUD 6,370", "Business/investor stream, state nomination, significant capital investment"),
            ("Retirement", "Investor Retirement (Subclass 405)", "4 years (renewable)", "AUD 4,640", "Age 55+, AUD 750,000 investment in state government bond"),
            ("Transit", "Transit Visa (Subclass 771)", "72 hours", "Free", "Confirmed onward ticket, visa for destination country"),
            ("Diplomatic", "Diplomatic (Subclass 995)", "Duration of posting", "Free", "Diplomatic or official passport, government note"),
        ],
        "processing_times": [
            ("ETA (Subclass 601)", "Instant to 24 hours", "N/A", "N/A"),
            ("eVisitor (Subclass 651)", "1-3 business days", "N/A", "N/A"),
            ("Visitor (Subclass 600)", "1-30 days (75% within 16 days)", "N/A", "N/A"),
            ("Student (Subclass 500)", "4-6 weeks (75% within 29 days)", "N/A", "N/A"),
            ("TSS (Subclass 482)", "1-4 months", "N/A", "N/A"),
            ("Skilled Independent (189)", "6-12 months", "N/A", "N/A"),
            ("Partner (309/100)", "15-27 months", "N/A", "N/A"),
            ("Working Holiday (417)", "1-30 days", "N/A", "N/A"),
            ("Global Talent (858)", "2-6 months", "N/A", "N/A"),
            ("Parent (143)", "12+ years (contributory queue)", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for most visa subclasses. Must be conducted by a Bupa Medical Visa Services panel physician. Includes chest X-ray (age 11+), physical examination, and HIV/Hepatitis B testing for some applicants.</li>
<li><strong>Health conditions:</strong> Applicants with conditions requiring significant healthcare costs or community services may fail the health requirement. A Health Waiver may be available for some visa subclasses.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for short-term visitors. Student visa (500) applicants under 20 may need to provide evidence of measles and pertussis vaccination.</li>
<li><strong>COVID-19:</strong> No vaccination or testing requirements as of 2026.</li>
<li><strong>Police clearance:</strong> AFP (Australian Federal Police) national police check for applicants in Australia. Home-country police certificate for all countries lived in for 12+ months in the past 10 years. Required for most visa types.</li>
<li><strong>Biometrics:</strong> Required from some nationalities. Fingerprints and facial photograph collected at an Australian Visa Application Centre (AVAC).</li>
<li><strong>OSHC:</strong> Overseas Student Health Cover is mandatory for the full duration of stay on a Student Visa (Subclass 500). Must be purchased from an approved Australian provider (e.g., Medibank, Bupa, Allianz).</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>ETA / eVisitor:</strong> Cannot be extended. Must leave Australia before 90 days expire. Can re-enter for another 90 days within the 12-month validity period.</li>
<li><strong>Visitor Visa (Subclass 600):</strong> May be extended by applying for a new Subclass 600 visa before the current one expires. Apply through ImmiAccount. No guarantee of approval — genuine temporary entrant requirement applies.</li>
<li><strong>Student Visa (500):</strong> Extend by obtaining a new CoE for further study and applying for a new Subclass 500. Must maintain enrollment and attendance requirements.</li>
<li><strong>Working Holiday (417/462):</strong> Can apply for 2nd and 3rd year visas by completing specified work in regional Australia (88 days for 2nd year, 6 months for 3rd year).</li>
<li><strong>Bridging visas:</strong> If you apply for a new substantive visa while in Australia, you are typically granted a Bridging Visa A that allows you to remain lawfully until the new application is decided.</li>
<li><strong>Overstay consequences:</strong> Overstaying results in a 3-year exclusion period for future Australian visas. Repeat offenders or those who stay unlawfully for 12+ months face a permanent exclusion bar.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Failure to meet genuine temporary entrant (GTE) requirement, insufficient financial evidence, health or character concerns, incomplete documentation, previous visa cancellations or overstays, failing points test for skilled visas.</li>
<li><strong>Review process:</strong> Most visa refusals can be appealed to the Administrative Appeals Tribunal (AAT) within 21-28 days (onshore) or 28 days (offshore). The AAT conducts a merits review — a fresh assessment of the case.</li>
<li><strong>AAT fees:</strong> AUD 1,826 (general migration), refundable if the decision is overturned.</li>
<li><strong>Ministerial intervention:</strong> In exceptional circumstances, the Minister for Immigration may intervene under Section 351 or 417 of the Migration Act to substitute a more favorable decision.</li>
<li><strong>Reapplication:</strong> No mandatory waiting period to reapply after refusal (unless subject to exclusion period). Applications should address the specific reasons cited in the refusal notice.</li>
</ul>""",
        "extra_faqs": [
            ("What is the difference between an ETA and an eVisitor for Australia?", "The ETA (Subclass 601) costs AUD 20 and is for citizens of 8 countries including the US, Canada, and Japan. The eVisitor (Subclass 651) is free and available to EU/EEA passport holders. Both allow 90-day visits for tourism or business within a 12-month period."),
            ("How much bank balance do I need for an Australian visitor visa?", "There is no fixed minimum, but you should demonstrate sufficient funds to cover your stay. Generally, AUD 5,000-10,000 for a short visit is considered adequate. For longer stays, you may need to show more substantial savings or a sponsor's financial support."),
            ("Can I work on an Australian tourist visa?", "No. Visitor visas (Subclass 600, 601, 651) do not permit work. To work in Australia, you need a work visa such as the Working Holiday (417/462), TSS (482), or a skilled migration visa (189/190/491)."),
            ("How do I get a second Working Holiday visa for Australia?", "To qualify for a second Working Holiday Visa (Subclass 417), you must complete 88 days of specified work in regional Australia during your first year. Eligible work includes agriculture, mining, construction, and other specified industries in designated regional areas."),
            ("What is the Australian Genuine Temporary Entrant (GTE) requirement?", "The GTE requirement applies to Student Visa (500) and some other visa applicants. Immigration officers assess whether the applicant genuinely intends to stay temporarily based on their circumstances in their home country, potential circumstances in Australia, value of the course, immigration history, and any other relevant matters."),
        ],
    },
    "india": {
        "file": "india-visa-requirements.html",
        "name": "India",
        "flag": "in",
        "visa_types": [
            ("Tourist", "e-Tourist Visa (30 days)", "30 days, single/double entry", "USD 10", "Online application, 4 eligible ports of entry expanded to 28 airports/5 seaports"),
            ("Tourist", "e-Tourist Visa (1 year)", "1 year, multiple entry, 90 days per visit", "USD 25", "Online application at indianvisaonline.gov.in, photo upload"),
            ("Tourist", "e-Tourist Visa (5 years)", "5 years, multiple entry, 90 days per visit", "USD 40", "Online application, valid passport with 6+ months validity"),
            ("Tourist", "Regular Tourist Visa", "6 months to 10 years (country dependent)", "Varies (USD 50-160)", "Embassy application, interview may be required"),
            ("Business", "e-Business Visa", "1 year, multiple entry", "USD 80", "Business invitation, company registration, financial proof"),
            ("Business", "Business Visa (Regular)", "1-5 years", "Varies", "Embassy application, Indian business partner letter, company documents"),
            ("Medical", "e-Medical Visa", "60 days, triple entry", "USD 80", "Hospital recommendation letter from recognized Indian hospital"),
            ("Medical", "Medical Attendant e-Visa", "60 days, triple entry", "USD 80", "Accompanying e-Medical visa holder, relationship proof"),
            ("Work", "Employment Visa", "Up to 5 years", "USD 100-200", "Employment contract, minimum salary USD 25,000/year, company sponsorship"),
            ("Work", "Project Visa", "Duration of project", "Varies", "Government/PSU project, inter-governmental agreement"),
            ("Student", "Student Visa", "Duration of course", "USD 80-100", "Admission letter from recognized Indian institution, financial proof"),
            ("Student", "Research Visa", "Duration of research (up to 5 years)", "Varies", "Research approval from Indian authorities, institutional sponsorship"),
            ("Family", "Entry Visa (Spouse/Dependent)", "Up to 5 years", "Varies", "Marriage certificate, spouse's valid India visa, relationship proof"),
            ("Family", "OCI (Overseas Citizen of India)", "Lifetime", "USD 275", "Person of Indian origin or spouse, lifetime entry rights, no voting rights"),
            ("Family", "PIO Card (merged with OCI)", "Now merged into OCI", "N/A", "Apply for OCI instead"),
            ("Journalist", "Journalist Visa (J Visa)", "3-6 months", "Varies", "Press accreditation, prior approval from Ministry of External Affairs"),
            ("Transit", "e-Transit Visa", "72 hours", "USD 25", "Confirmed onward ticket, transit through India"),
            ("Conference", "e-Conference Visa", "30 days", "USD 80", "Invitation from organizer, conference in India by government/PSU/NIC recognized body"),
            ("Diplomatic", "Diplomatic/Official Visa", "Duration of posting", "Free", "Diplomatic passport, government note verbale"),
        ],
        "processing_times": [
            ("e-Tourist Visa (30-day)", "24-72 hours", "N/A", "N/A"),
            ("e-Tourist Visa (1-year/5-year)", "24-72 hours", "N/A", "N/A"),
            ("e-Business Visa", "24-72 hours", "N/A", "N/A"),
            ("e-Medical Visa", "24-72 hours", "N/A", "N/A"),
            ("Regular Tourist Visa", "5-7 business days", "2-3 business days", "USD 20-50 surcharge"),
            ("Employment Visa", "7-15 business days", "5 business days", "Varies by embassy"),
            ("Student Visa", "5-10 business days", "3-5 business days", "Varies"),
            ("OCI Card", "3-6 weeks", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Yellow Fever:</strong> Yellow Fever vaccination certificate is MANDATORY for travelers arriving from or transiting through yellow fever endemic countries in Africa and South America. Without it, you may be quarantined for up to 6 days.</li>
<li><strong>Medical exam:</strong> Not routinely required for tourist or business visas. Employment visas for longer stays may require HIV testing (though India removed mandatory HIV testing for most visa categories).</li>
<li><strong>Recommended vaccinations:</strong> Hepatitis A & B, Typhoid, Japanese Encephalitis (for rural areas), Rabies (for extended stays), Polio booster, Tetanus/Diphtheria.</li>
<li><strong>Malaria:</strong> No vaccination required but antimalarial prophylaxis recommended for certain regions.</li>
<li><strong>Police clearance:</strong> Required for Employment Visa, Research Visa, and Missionary Visa. Must be from applicant's home country and less than 6 months old.</li>
<li><strong>Biometrics:</strong> Fingerprints and photograph collected at Indian Visa Application Centres (IVAC) for regular visa applicants. Not required for e-Visa (collected on arrival).</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>e-Tourist Visa (30-day):</strong> Cannot be extended. Must leave India before expiry.</li>
<li><strong>e-Tourist Visa (1-year/5-year):</strong> Each visit limited to 90 days (180 days for US, UK, Canadian, Japanese citizens). Cannot be extended — must exit and re-enter.</li>
<li><strong>Regular Tourist Visa:</strong> Can be extended at the Foreigners Regional Registration Office (FRRO) in exceptional circumstances (medical emergency, flight cancellation). Fee: INR 3,000-6,000.</li>
<li><strong>Employment Visa:</strong> Extendable at FRRO. Must apply 60 days before expiry. Extension in 1-year increments up to 5 years.</li>
<li><strong>Student Visa:</strong> Extendable annually at FRRO with continued enrollment proof.</li>
<li><strong>Overstay penalties:</strong> Fine of USD 300 for each calendar year of overstay (minimum USD 300). Overstays can result in arrest, deportation, and future visa denial. Registration with FRRO required for stays exceeding 180 days on certain visa types.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Incomplete application, incorrect photo specifications, passport with insufficient validity, applicants from restricted nationalities (Pakistan, Bangladesh, Sri Lanka, Afghanistan, Iran, China may face additional scrutiny), prior overstay in India, suspicious travel history.</li>
<li><strong>e-Visa specific refusals:</strong> Incorrect passport details, mismatched photo, prior e-Visa violation, citizenship of non-eligible country.</li>
<li><strong>Appeal process:</strong> No formal appeal process. Applicants may reapply immediately with corrected documentation. For regular visas, contact the Indian embassy directly to understand refusal reasons.</li>
<li><strong>Reapplication:</strong> e-Visa can be reapplied immediately (pay new fee). Embassy visa refusals may benefit from a waiting period to improve documentation. Pakistani nationals face stricter review and longer processing.</li>
<li><strong>Security clearance:</strong> Certain nationalities require mandatory security clearance from the Ministry of Home Affairs, which can take 4-8 weeks. Refusal at this stage is typically final.</li>
</ul>""",
        "extra_faqs": [
            ("How long does an Indian e-Visa take to process?", "Indian e-Visas are typically processed within 24-72 hours. Applications submitted at least 4 days before travel are recommended. The e-Visa is sent to the applicant's email and must be printed for presentation at the Indian port of entry."),
            ("Which airports accept Indian e-Visas?", "As of 2026, Indian e-Visas are accepted at 28 designated international airports and 5 seaports. Major airports include Delhi, Mumbai, Chennai, Kolkata, Bengaluru, Hyderabad, Kochi, and Goa. Exit is allowed from any authorized immigration checkpoint."),
            ("What is the difference between e-Visa and regular visa for India?", "The e-Visa is applied online at indianvisaonline.gov.in and processed within 72 hours, available for tourism, business, medical, and conference purposes. Regular visas are applied at the embassy/consulate, offer longer validity (up to 10 years), and cover additional categories like employment, student, and research."),
            ("Do I need a Yellow Fever certificate for India?", "Yes, if you are arriving from or transiting through a yellow fever endemic country (most of Sub-Saharan Africa and parts of South America). Without a valid certificate, you may be quarantined at the port of entry for up to 6 days."),
            ("What is OCI and how is it different from Indian citizenship?", "OCI (Overseas Citizen of India) is a lifetime visa for persons of Indian origin and their spouses. It grants multiple entry, no registration requirement, and parity with NRI (Non-Resident Indian) in most areas except voting, government jobs, and agricultural property purchase. OCI is not dual citizenship."),
        ],
    },
    "japan": {
        "file": "japan-visa-requirements.html",
        "name": "Japan",
        "flag": "jp",
        "visa_types": [
            ("Tourist", "Visa Exemption (Temporary Visitor)", "15/30/90 days (nationality dependent)", "Free", "Passport from 68+ visa-exempt countries, return ticket, sufficient funds"),
            ("Tourist", "Temporary Visitor Visa", "15/30/90 days", "Free - varies by country", "Passport, invitation/itinerary, financial evidence, guarantor in Japan"),
            ("Business", "Short-Term Business (Temporary Visitor)", "90 days maximum", "Free - varies", "Business invitation, company letter, meeting itinerary"),
            ("Work", "Engineer/Specialist in Humanities/International Services", "1-5 years", "JPY 3,000 (single) / JPY 6,000 (multi)", "COE, university degree or 10+ years experience, employer sponsorship"),
            ("Work", "Skilled Labor", "1-5 years", "JPY 3,000 / JPY 6,000", "COE, specialized skills (chef, craftsman, etc.), employer sponsorship"),
            ("Work", "Intra-company Transferee", "1-5 years", "JPY 3,000 / JPY 6,000", "COE, transfer from overseas branch/subsidiary, 1+ year with company"),
            ("Work", "Specified Skilled Worker (SSW-i)", "Up to 5 years", "JPY 3,000 / JPY 6,000", "COE, passed skills test and Japanese language test (JLPT N4+), 14 sectors"),
            ("Work", "Specified Skilled Worker (SSW-ii)", "Renewable indefinitely", "JPY 3,000 / JPY 6,000", "Higher skills test, family can accompany, path to permanent residence"),
            ("Work", "Highly Skilled Professional (HSP)", "5 years initially", "JPY 3,000 / JPY 6,000", "Points-based (70+ points), fast track to PR (1-3 years), family benefits"),
            ("Work", "Instructor", "1-5 years", "JPY 3,000 / JPY 6,000", "COE, teaching position at educational institution"),
            ("Work", "Working Holiday", "1 year", "Free", "Age 18-30, bilateral agreement country, limited work permitted"),
            ("Student", "College Student (Ryugaku)", "Duration of study (max 4 years 3 months)", "JPY 3,000 / JPY 6,000", "COE, acceptance from Japanese institution, financial proof (JPY 2M+ in bank)"),
            ("Student", "Pre-college (Shuugaku)", "Up to 2 years", "JPY 3,000 / JPY 6,000", "Japanese language school acceptance, financial proof"),
            ("Family", "Spouse or Child of Japanese National", "1-5 years", "JPY 3,000 / JPY 6,000", "Marriage certificate, family register (koseki tohon), financial support proof"),
            ("Family", "Spouse of Permanent Resident", "1-5 years", "JPY 3,000 / JPY 6,000", "Spouse's PR card, marriage certificate, financial evidence"),
            ("Family", "Dependent", "Duration of primary visa holder", "JPY 3,000 / JPY 6,000", "Relationship proof, primary visa holder's status, limited work (28 hrs/week)"),
            ("Investor", "Business Manager", "1-5 years", "JPY 3,000 / JPY 6,000", "COE, JPY 5M+ investment or 2+ full-time employees, business plan"),
            ("Long-term", "Permanent Resident", "Indefinite", "JPY 8,000", "10+ years continuous residence (or 1-3 years for HSP), good conduct, stable income"),
            ("Transit", "Shore Pass / Transit", "72 hours", "Free", "Crew or passenger with confirmed onward flight, airport transit"),
            ("Diplomatic", "Diplomatic / Official", "Duration of assignment", "Free", "Diplomatic passport, government note verbale"),
            ("Trainee", "Technical Intern Training (TITP)", "Up to 5 years", "JPY 3,000", "Approved supervising organization, training plan, developing country national"),
            ("Digital Nomad", "Digital Nomad Visa", "6 months", "Free", "Annual income JPY 10M+, remote work for non-Japanese company, health insurance"),
        ],
        "processing_times": [
            ("Visa Exemption", "Instant (on arrival)", "N/A", "N/A"),
            ("Temporary Visitor Visa", "5 business days", "N/A", "N/A"),
            ("COE (Certificate of Eligibility)", "1-3 months", "N/A", "N/A"),
            ("Work Visa (with COE)", "5 business days after COE received", "N/A", "N/A"),
            ("Student Visa (with COE)", "5 business days", "N/A", "N/A"),
            ("Highly Skilled Professional", "10 business days (expedited COE)", "N/A", "N/A"),
            ("Permanent Residence", "6-12 months", "N/A", "N/A"),
            ("Business Manager", "1-3 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Not required for short-term visitors or most visa categories. May be required for long-term stays if health concerns are flagged. Tuberculosis screening may be requested for nationals of high-risk countries.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry. Recommended: Japanese Encephalitis (especially rural areas), Influenza, Hepatitis A & B, Measles-Rubella.</li>
<li><strong>COVID-19:</strong> No vaccination or testing requirements as of 2026. Visit Japan Web registration recommended for smooth entry.</li>
<li><strong>Health insurance:</strong> Not mandatory but strongly recommended. National Health Insurance (NHI) enrollment is required for residents staying 3+ months.</li>
<li><strong>Police clearance:</strong> Not routinely required for visa applications. May be requested for permanent residence applications or certain employment categories.</li>
<li><strong>Biometrics:</strong> Fingerprints and photograph collected at the port of entry for all foreign nationals aged 16+ (except special permanent residents, diplomats, and those under 16).</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Temporary Visitor (tourist):</strong> Can be extended once for up to 90 days total stay at the nearest Immigration Bureau. Fee: JPY 4,000. Requires valid reason (illness, unavoidable circumstances). Extension is discretionary.</li>
<li><strong>Work visas:</strong> Renewable in 1, 3, or 5-year increments at the Regional Immigration Bureau before expiry. Must maintain the same qualifying activity. Fee: JPY 4,000.</li>
<li><strong>Student visa:</strong> Renewable in 1-2 year increments with continued enrollment. Must maintain minimum attendance (80%+) and academic progress.</li>
<li><strong>Change of status:</strong> Possible within Japan by filing at the Immigration Bureau. Common changes: student to work, dependent to specified activities. Fee: JPY 4,000.</li>
<li><strong>Re-entry permit:</strong> Special Re-entry Permit valid for 1 year (automatically granted) if returning within the visa validity. Regular Re-entry Permit (JPY 3,000 single / JPY 6,000 multiple) for longer absence.</li>
<li><strong>Overstay consequences:</strong> Overstay is a criminal offense in Japan. Penalties include detention, deportation, and a 5-year (first offense) or 10-year (repeat) re-entry ban. A voluntary departure through the departure order system results in a 1-year ban.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient financial proof, weak ties to home country, incomplete or inconsistent documentation, prior overstay or deportation from Japan, criminal record, COE issues, suspected intention to work illegally.</li>
<li><strong>COE refusal:</strong> If the Certificate of Eligibility is denied by the Immigration Services Agency of Japan, the employer/sponsor can file an objection or resubmit with additional documentation.</li>
<li><strong>Visa refusal at embassy:</strong> No formal appeal process. Applicants may reapply with improved documentation. The embassy is not required to disclose specific reasons for refusal.</li>
<li><strong>Reapplication:</strong> No mandatory waiting period. Address the suspected reasons and strengthen the application. Multiple refusals without changed circumstances may result in prolonged scrutiny.</li>
<li><strong>Landing denial:</strong> Immigration officers at the port of entry can deny landing even with a valid visa. This can be challenged through an oral hearing (kouryoku shinsa) at the airport.</li>
</ul>""",
        "extra_faqs": [
            ("What is a Certificate of Eligibility (COE) for Japan?", "A COE is a document issued by the Immigration Services Agency of Japan that pre-approves your eligibility for a specific visa status. It is required for most long-term visas (work, student, spouse). Your employer or school in Japan applies for the COE, which typically takes 1-3 months. Once received, you apply for the visa at a Japanese embassy, which takes about 5 business days."),
            ("How long can I stay in Japan without a visa?", "Citizens of 68+ countries can stay in Japan visa-free for 15 to 90 days depending on nationality. Most Western countries receive 90 days. The stay cannot exceed the granted period, but one extension may be possible at the Immigration Bureau for a total of 90 days."),
            ("Does Japan have a digital nomad visa?", "Yes. Japan introduced a Digital Nomad Visa in 2024 that allows remote workers to stay for up to 6 months. Requirements include an annual income of JPY 10 million or more, working remotely for a non-Japanese company, and having private health insurance covering your stay in Japan."),
            ("Can I work part-time on a student visa in Japan?", "Yes, with a Permission to Engage in Activity Other Than That Permitted (shikakugai katsudou kyoka). Student visa holders can work up to 28 hours per week during school terms and up to 40 hours per week during official school breaks. Apply at the Immigration Bureau."),
            ("How do I get permanent residence in Japan?", "Generally requires 10+ continuous years of residence in Japan (5 years of work). Highly Skilled Professionals can qualify in 1-3 years with 70-80+ points. Requirements include good conduct, sufficient income to support yourself, and being a benefit to Japan. Application fee is JPY 8,000."),
        ],
    },
    "canada": {
        "file": "canada-visa-requirements.html",
        "name": "Canada",
        "flag": "ca",
        "visa_types": [
            ("Tourist", "eTA (Electronic Travel Authorization)", "Up to 6 months per visit", "CAD 7", "Visa-exempt passport, no criminal inadmissibility, valid credit card"),
            ("Tourist", "Temporary Resident Visa (TRV)", "Up to 6 months", "CAD 100", "Financial proof, ties to home country, travel purpose, no criminal inadmissibility"),
            ("Tourist", "Super Visa (Parents/Grandparents)", "Up to 5 years per visit", "CAD 100 + medical insurance", "Parent/grandparent of Canadian citizen/PR, private medical insurance, financial support letter"),
            ("Business", "Business Visitor", "Up to 6 months", "CAD 100 (TRV) or CAD 7 (eTA)", "Business meeting purpose, not entering labour market, employer letter"),
            ("Work", "Employer-Specific Work Permit (LMIA-based)", "Duration of LMIA", "CAD 155", "Positive LMIA from employer, job offer, proof of qualifications"),
            ("Work", "Open Work Permit", "Varies", "CAD 155 + CAD 100 OWP fee", "Specific categories: spousal, post-graduation, bridging, etc."),
            ("Work", "PGWP (Post-Graduation Work Permit)", "8 months - 3 years", "CAD 255", "Completed program at DLI, applied within 180 days of graduation"),
            ("Work", "Intra-Company Transfer (ICT)", "Duration of transfer", "CAD 155", "LMIA-exempt, 1+ year with company, executive/management/specialized knowledge"),
            ("Work", "International Experience Canada (IEC)", "Up to 2 years", "CAD 161 + CAD 100", "Age 18-35, bilateral agreement country (Working Holiday, Young Professionals, Co-op)"),
            ("Work", "Global Talent Stream", "2 weeks processing", "CAD 155 (LMIA exempt)", "Category A (unique talent) or B (in-demand occupations), employer-driven"),
            ("Student", "Study Permit", "Duration of program + 90 days", "CAD 150", "Acceptance from DLI, proof of funds (CAD 20,635/year + tuition), Quebec CAQ if applicable"),
            ("Family", "Spousal Sponsorship (PR)", "Permanent", "CAD 1,050 (sponsorship + PR fees)", "Canadian citizen/PR spouse, genuine relationship proof, financial undertaking"),
            ("Family", "Parent/Grandparent Sponsorship (PR)", "Permanent", "CAD 1,050", "Income requirement (LICO+30%), undertaking for 20 years"),
            ("Investor", "Start-Up Visa", "Permanent Residence", "CAD 1,575 (PR fee)", "Letter of support from designated venture capital, angel investor, or business incubator"),
            ("Express Entry", "Express Entry (Federal Skilled Worker)", "Permanent Residence", "CAD 1,575", "CRS score (currently ~500+), skilled work experience, language test (CLB 7+), education credential"),
            ("Express Entry", "Express Entry (Canadian Experience Class)", "Permanent Residence", "CAD 1,575", "1 year Canadian skilled work experience in past 3 years, language proficiency"),
            ("Express Entry", "Provincial Nominee Program (PNP)", "Permanent Residence", "CAD 1,575 + provincial fee", "Provincial nomination, meet federal requirements, varies by province"),
            ("Transit", "Transit Visa", "48 hours", "Free", "Transiting through Canada, confirmed onward ticket"),
            ("Diplomatic", "Diplomatic / Official", "Duration of assignment", "Free", "Diplomatic passport, government note verbale"),
        ],
        "processing_times": [
            ("eTA", "Usually instant (up to 72 hours)", "N/A", "N/A"),
            ("Temporary Resident Visa (TRV)", "7-188 days (varies by country)", "N/A", "N/A"),
            ("Study Permit", "1-16 weeks (varies by country)", "20 business days (Student Direct Stream)", "Free (SDS)"),
            ("Work Permit (LMIA-based)", "2-16 weeks", "2 weeks (Global Talent Stream)", "Employer pays CAD 1,000 LMIA fee"),
            ("PGWP", "1-6 months", "N/A", "N/A"),
            ("Express Entry (FSW/CEC)", "6 months (80% target)", "N/A", "N/A"),
            ("Spousal Sponsorship", "12-16 months", "N/A", "N/A"),
            ("Super Visa", "2-25 weeks", "N/A", "N/A"),
            ("Start-Up Visa", "12-36 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required if staying longer than 6 months or if you lived in a designated country. Must be performed by a panel physician designated by IRCC. Includes physical exam, urinalysis, chest X-ray (age 11+), and blood tests (HIV, syphilis).</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry. Routine vaccines recommended (measles, chickenpox, flu, COVID-19).</li>
<li><strong>Health inadmissibility:</strong> Applicants may be found inadmissible if their health condition poses a danger to public health/safety or would cause excessive demand on Canadian health/social services (threshold: CAD 24,057/year).</li>
<li><strong>Police clearance:</strong> Required for all applicants aged 18+ for permanent residence. Police certificates from every country lived in for 6+ months since age 18. For temporary visas, may be requested if deemed necessary.</li>
<li><strong>Biometrics:</strong> Required for most visa, permit, and PR applicants aged 14-79. Collected at a Visa Application Centre (VAC). Fee: CAD 85 (individual) / CAD 170 (family). Valid for 10 years.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Visitor Record:</strong> Visitors can apply to extend their stay by submitting a Visitor Record application online before their authorized stay expires. Fee: CAD 100. Implied status allows continued stay while the application is pending.</li>
<li><strong>Study Permit extension:</strong> Apply at least 30 days before expiry. Fee: CAD 150. Must maintain full-time enrollment at a DLI.</li>
<li><strong>Work Permit extension:</strong> Apply before current permit expires. Implied status allows continued work. Fee: CAD 155. Bridging Open Work Permit available for those with PR applications pending.</li>
<li><strong>Restoration of status:</strong> If your status has expired within the last 90 days, you can apply for restoration of status. Fee: CAD 229 (on top of regular fees). No guaranteed approval.</li>
<li><strong>Overstay consequences:</strong> Remaining beyond authorized stay may lead to a removal order, inadmissibility for future applications, and difficulty obtaining future Canadian visas or PR.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient ties to home country, inadequate financial proof, travel history concerns, purpose of visit not clearly established, previous immigration violations, criminal inadmissibility, health inadmissibility.</li>
<li><strong>GCMS notes:</strong> Applicants can request officer's notes through an Access to Information and Privacy (ATIP) request to understand detailed refusal reasons. Processing takes 30 days.</li>
<li><strong>Judicial review:</strong> Permanent residence refusals can be challenged through Federal Court judicial review within 15 days (inland) or 60 days (overseas). Leave must be granted before review proceeds.</li>
<li><strong>Reapplication:</strong> No mandatory waiting period for temporary visa refusals. Address the specific refusal reasons and submit a strengthened application. Letter of explanation addressing previous refusal is recommended.</li>
<li><strong>Criminal rehabilitation:</strong> Applicants deemed criminally inadmissible can apply for Criminal Rehabilitation (if 5+ years since completion of sentence) or obtain a Temporary Resident Permit (TRP) for urgent travel.</li>
</ul>""",
        "extra_faqs": [
            ("What is the difference between an eTA and a Canadian visitor visa?", "An eTA costs CAD 7, is processed almost instantly, and is for visa-exempt nationals (e.g., UK, EU, Japan, Australia) flying to Canada. A Temporary Resident Visa (TRV) costs CAD 100, requires more documentation, and is for nationals who need a visa (e.g., India, China, Philippines)."),
            ("How does Canada Express Entry work?", "Express Entry is a points-based immigration system managing three programs: Federal Skilled Worker, Canadian Experience Class, and Federal Skilled Trades. Create a profile, receive a CRS score based on age, education, language, and work experience, then wait for an Invitation to Apply (ITA) when your score meets the draw cutoff."),
            ("Can I work while studying in Canada?", "Yes. Study permit holders at a DLI can work up to 20 hours per week during academic sessions and full-time during scheduled breaks without a separate work permit. Co-op or internship work placements require a co-op work permit."),
            ("What is the Super Visa for Canada?", "The Super Visa allows parents and grandparents of Canadian citizens/permanent residents to visit for up to 5 years per entry without renewing status. Requirements include a letter of invitation, proof of private medical insurance from a Canadian company, and evidence of financial support."),
            ("How long does it take to get Canadian PR through Express Entry?", "IRCC targets processing 80% of Express Entry applications within 6 months of receiving a complete application. Current processing times may vary. The overall timeline from profile creation to PR can be 8-14 months including gathering documents and medical exams."),
        ],
    },
    "france": {
        "file": "france-visa-requirements.html",
        "name": "France",
        "flag": "fr",
        "visa_types": [
            ("Tourist", "Schengen Short-Stay Visa (C)", "90 days within 180-day period", "EUR 80 (adults) / EUR 40 (children 6-12)", "Application via TLScontact/VFS, travel insurance EUR 30,000 minimum"),
            ("Tourist", "Visa-Free (Schengen)", "90 days in 180 days", "Free", "Passport from 60+ visa-exempt countries (US, UK, Canada, Australia, Japan, etc.)"),
            ("Business", "Schengen Business Visa (C)", "90 days in 180 days", "EUR 80", "Business invitation from French company, company letter, financial proof"),
            ("Work", "Talent Passport (Passeport Talent)", "Up to 4 years", "EUR 225", "Highly skilled workers, researchers, artists, investors — 10 subcategories"),
            ("Work", "Temporary Worker (Travailleur Temporaire)", "Up to 1 year", "EUR 225", "Work contract, employer authorization, DIRECCTE approval"),
            ("Work", "Employee on Assignment (Salarie Detache)", "Up to 3 years", "EUR 225", "Intra-company transfer, assignment letter from employer"),
            ("Work", "Seasonal Worker", "6 months per 12-month period", "EUR 99", "Seasonal work contract, employer must be registered"),
            ("Work", "Working Holiday Visa (PVT)", "1 year", "Free", "Age 18-30, bilateral agreement country (Canada, Australia, Japan, etc.)"),
            ("Student", "Long-Stay Student Visa (VLS-TS)", "Duration of study (1 year, renewable)", "EUR 99", "Campus France registration, acceptance from French institution, financial proof (EUR 615/month)"),
            ("Student", "Short-Stay Student Visa", "90 days", "EUR 80", "Enrollment in short course, financial proof"),
            ("Family", "Family Reunification (Regroupement Familial)", "Long-stay", "EUR 225", "Spouse/children of legal resident, minimum income, adequate housing"),
            ("Family", "Spouse of French National", "Long-stay", "EUR 50", "Marriage certificate, proof of genuine relationship"),
            ("Investor", "Talent Passport — Investor", "4 years", "EUR 225", "EUR 300,000 direct investment in French company, business plan"),
            ("Investor", "Talent Passport — Business Creator", "4 years", "EUR 225", "Viable business plan, EUR 30,000+ investment"),
            ("Transit", "Airport Transit Visa (A)", "Transit only", "EUR 80", "Required for certain nationalities transiting through French airports"),
            ("Diplomatic", "Diplomatic / Official", "Duration of assignment", "Free", "Diplomatic passport, government note verbale"),
            ("Digital Nomad", "No specific visa — use Talent Passport", "Up to 4 years", "EUR 225", "Self-employed or remote worker subcategory of Talent Passport"),
        ],
        "processing_times": [
            ("Schengen Short-Stay (C)", "15 calendar days (up to 45 days)", "N/A", "N/A"),
            ("Long-Stay Student (VLS-TS)", "3-6 weeks", "N/A", "N/A"),
            ("Talent Passport", "2-3 months", "N/A", "N/A"),
            ("Temporary Worker", "2-3 months", "N/A", "N/A"),
            ("Family Reunification", "4-12 months", "N/A", "N/A"),
            ("Working Holiday (PVT)", "2-4 weeks", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for long-stay visa holders upon arrival in France as part of the OFII validation process. Includes chest X-ray and general health assessment at an OFII-approved center.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry. Recommended: routine vaccines, Hepatitis A, Measles-Mumps-Rubella (MMR). Children must have 11 mandatory vaccinations for school enrollment in France.</li>
<li><strong>Travel insurance:</strong> Mandatory for Schengen visa applicants — minimum EUR 30,000 coverage for medical expenses, hospitalization, and repatriation. Must be valid for the entire Schengen area.</li>
<li><strong>COVID-19:</strong> No vaccination or testing requirements as of 2026.</li>
<li><strong>Police clearance:</strong> Required for long-stay visa applications — criminal record extract (extrait de casier judiciaire) from home country, translated and apostilled.</li>
<li><strong>Biometrics:</strong> Fingerprints and photo collected at VFS/TLScontact application center for Schengen and long-stay visa applicants.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Schengen short-stay:</strong> Cannot be extended except in exceptional circumstances (force majeure, humanitarian reasons, serious personal reasons). Apply at the local Prefecture.</li>
<li><strong>Long-stay visa (VLS-TS):</strong> Must be validated at OFII within 3 months of arrival. Renewable by applying for a residence permit (titre de sejour) at the Prefecture 2 months before expiry.</li>
<li><strong>Student residence permit:</strong> Renewable annually with proof of continued enrollment, academic progress, and financial means.</li>
<li><strong>Talent Passport:</strong> Renewable for up to 4 years. Multi-year permits available after first renewal.</li>
<li><strong>Overstay consequences:</strong> Overstaying a Schengen visa results in fines, deportation, and a ban on re-entry to the Schengen area for up to 5 years. Recorded in the Schengen Information System (SIS).</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient travel insurance, inadequate financial means, lack of proof of accommodation, unclear purpose of travel, previous Schengen violations, incomplete application, doubts about intention to return.</li>
<li><strong>Appeal process:</strong> Schengen visa refusals can be appealed to the Commission de Recours contre les Decisions de Refus de Visa (CRV) within 2 months of notification. A further appeal to the administrative tribunal (Tribunal Administratif de Nantes) is possible within 2 months of the CRV decision.</li>
<li><strong>Long-stay refusal:</strong> Can be challenged through the CRV and then the administrative courts.</li>
<li><strong>Reapplication:</strong> Applicants may reapply immediately with improved documentation. A refusal does not prevent future applications but is noted in the Visa Information System (VIS) for 5 years.</li>
</ul>""",
        "extra_faqs": [
            ("Do I need a visa to visit France as a tourist?", "Citizens of 60+ countries (including the US, UK, Canada, Australia, and Japan) can visit France visa-free for up to 90 days within any 180-day period under the Schengen agreement. Other nationalities need a Schengen Short-Stay Visa (Type C) costing EUR 80."),
            ("What is the France Talent Passport visa?", "The Talent Passport (Passeport Talent) is a multi-year residence permit for highly skilled workers, researchers, artists, investors, and entrepreneurs. It has 10 subcategories, is valid for up to 4 years, and costs EUR 225. It offers a simplified process compared to standard work visas."),
            ("How do I validate my French long-stay visa?", "Within 3 months of arrival in France, you must validate your VLS-TS visa online through the ANEF platform (formerly OFII). This involves paying a tax (EUR 200-225), completing a medical exam, and registering your residence. Without validation, your visa is not considered valid."),
            ("Can I work in France on a student visa?", "Yes. Student visa holders can work up to 964 hours per year (approximately 20 hours per week). No separate work permit is needed. Working beyond this limit requires changing to a work-based residence status."),
            ("What is ETIAS and when will it apply to France?", "ETIAS (European Travel Information and Authorisation System) is an upcoming pre-travel authorization for visa-exempt nationals visiting the Schengen area. Once implemented, travelers from countries like the US, UK, Canada, and Australia will need to register online (EUR 7 fee) before entering France or other Schengen countries."),
        ],
    },
    "germany": {
        "file": "germany-visa-requirements.html",
        "name": "Germany",
        "flag": "de",
        "visa_types": [
            ("Tourist", "Schengen Short-Stay Visa (C)", "90 days within 180-day period", "EUR 80 / EUR 40 (children 6-12)", "Application via VFS/embassy, travel insurance, financial means"),
            ("Tourist", "Visa-Free (Schengen)", "90 days in 180 days", "Free", "60+ visa-exempt countries"),
            ("Business", "Schengen Business Visa (C)", "90 days", "EUR 80", "Business invitation, company registration, itinerary"),
            ("Work", "EU Blue Card", "Up to 4 years", "EUR 100 (national) / EUR 75 (long-stay visa)", "University degree, job offer with minimum salary EUR 43,800 (shortage: EUR 39,682), recognized qualification"),
            ("Work", "Skilled Worker Visa (Fachkrafte)", "Up to 4 years", "EUR 100", "Recognized qualification, job offer in related field, German language skills may be required"),
            ("Work", "ICT Card (Intra-Corporate Transfer)", "Up to 3 years", "EUR 100", "Transfer from non-EU company, 6+ months employment, manager/specialist"),
            ("Work", "Job Seeker Visa", "6 months", "EUR 75", "University degree, financial self-sufficiency (EUR 1,027/month), health insurance"),
            ("Work", "Opportunity Card (Chancenkarte)", "1 year", "EUR 75", "Points-based (6+ points), qualification recognition, basic German (A1) or English (B2)"),
            ("Work", "Working Holiday", "1 year", "Free", "Age 18-30, bilateral agreement country"),
            ("Student", "Student Visa (National D)", "Duration of study", "EUR 75", "University admission, blocked account (EUR 11,904/year), health insurance"),
            ("Student", "Language Course Visa", "Duration of course (3-12 months)", "EUR 75", "Enrollment in intensive language course (18+ hours/week), financial proof"),
            ("Family", "Family Reunion Visa", "Long-stay", "EUR 75", "Spouse/child of German resident, basic German (A1 for spouses), adequate housing/income"),
            ("Investor", "Self-Employment Visa", "Up to 3 years", "EUR 100", "Business plan, economic interest/regional need, EUR 250,000+ investment or sufficient funding"),
            ("Freelance", "Freelance Visa (Freiberufler)", "Up to 3 years", "EUR 100", "Proof of freelance skills, client contracts or letters of intent, financial means"),
            ("Transit", "Airport Transit Visa (A)", "Transit only", "EUR 80", "Required for certain nationalities"),
            ("Diplomatic", "Diplomatic / Official", "Duration of assignment", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("Schengen Short-Stay (C)", "15 calendar days (up to 45 days)", "N/A", "N/A"),
            ("EU Blue Card", "1-3 months", "N/A", "N/A"),
            ("Skilled Worker (Fachkrafte)", "1-4 months", "4 weeks (Fast-Track via employer)", "EUR 411 fast-track fee"),
            ("Student Visa", "4-12 weeks", "N/A", "N/A"),
            ("Job Seeker Visa", "2-4 months", "N/A", "N/A"),
            ("Family Reunion", "2-6 months", "N/A", "N/A"),
            ("Opportunity Card", "2-4 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Travel insurance:</strong> Mandatory for Schengen visa — minimum EUR 30,000 medical coverage including repatriation. Must cover the entire Schengen area.</li>
<li><strong>Health insurance (long-stay):</strong> Mandatory for all residents. Students must have statutory (gesetzliche) or private health insurance. Workers are automatically enrolled in statutory health insurance if earning below EUR 69,300/year.</li>
<li><strong>Medical exam:</strong> Not routinely required for visa applications. Tuberculosis screening may be requested for nationals of high-risk countries.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry. Measles vaccination or immunity proof required for children attending school/daycare and certain workers.</li>
<li><strong>Police clearance:</strong> Required for national visa (D type) applications — criminal record certificate from home country, apostilled and translated into German.</li>
<li><strong>Biometrics:</strong> Fingerprints and photo collected at visa application center or embassy.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Schengen short-stay:</strong> Cannot be extended except in extraordinary circumstances (force majeure). Apply at the local Foreigners Authority (Auslanderbehorde).</li>
<li><strong>National visa (D):</strong> Must apply for a residence permit (Aufenthaltserlaubnis) at the Auslanderbehorde within 90 days of arrival. Renewable based on continued eligibility.</li>
<li><strong>EU Blue Card:</strong> Renewable and leads to permanent residence (Niederlassungserlaubnis) after 27 months (or 21 months with B1 German).</li>
<li><strong>Student residence permit:</strong> Renewable with continued enrollment. Maximum total study duration is 10 years. 18 months post-study job search permitted.</li>
<li><strong>Permanent residence:</strong> Available after 5 years of legal residence (shorter for EU Blue Card). Requires German language skills (B1), financial self-sufficiency, and pension contributions.</li>
<li><strong>Overstay consequences:</strong> Fines, deportation, and Schengen-wide entry ban of up to 5 years. Recorded in SIS database.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient financial proof, inadequate travel insurance, incomplete documents, unclear travel purpose, previous Schengen violations, weak ties to home country, suspected immigration intent.</li>
<li><strong>Appeal (Remonstration):</strong> Applicants can file a written objection (Remonstration) to the embassy within 1 month of the refusal notification. The embassy reviews the case again with any new evidence.</li>
<li><strong>Court appeal:</strong> If remonstration fails, applicants can file a lawsuit at the Administrative Court (Verwaltungsgericht) in Berlin within 1 month. Legal representation recommended.</li>
<li><strong>Reapplication:</strong> Can reapply at any time with improved documentation. Previous refusals are recorded in VIS for 5 years.</li>
</ul>""",
        "extra_faqs": [
            ("What is the Germany Opportunity Card (Chancenkarte)?", "The Opportunity Card is a new points-based visa introduced in 2024 allowing skilled workers to come to Germany for 1 year to seek employment. Points are awarded for qualifications, language skills (German A1 or English B2), professional experience, age, and connection to Germany. Minimum 6 points required."),
            ("What is the EU Blue Card for Germany?", "The EU Blue Card is a work and residence permit for highly qualified non-EU workers. It requires a recognized university degree and a job offer with a minimum annual salary of EUR 43,800 (EUR 39,682 for shortage occupations). It leads to permanent residence after 27 months (21 months with B1 German)."),
            ("Do I need a blocked account for a German student visa?", "Yes. International students must open a blocked account (Sperrkonto) with a minimum of EUR 11,904 for the first year. You can withdraw up to EUR 992 per month. Approved providers include Expatrio, Fintiba, and Deutsche Bank."),
            ("Can I work in Germany on a student visa?", "Yes. Student visa holders can work 140 full days or 280 half days per year without additional permission. Exceeding this limit requires approval from the Foreigners Authority and the Federal Employment Agency."),
            ("What are Germany's skilled worker visa requirements?", "Since the Skilled Immigration Act, Germany offers visas for skilled workers with recognized qualifications. You need a recognized professional or academic qualification, a concrete job offer in a related field, and your employer may use the fast-track procedure (4 weeks, EUR 411) through the Foreigners Authority."),
        ],
    },
    "united-kingdom": {
        "file": "united-kingdom-visa-requirements.html",
        "name": "United Kingdom",
        "flag": "gb",
        "visa_types": [
            ("Tourist", "Standard Visitor Visa", "Up to 6 months", "GBP 115", "Financial proof, accommodation, ties to home country, genuine visitor intent"),
            ("Tourist", "Visa-Free Entry", "Up to 6 months", "Free", "EU/EEA, US, Canada, Australia, Japan, etc. — no visa required"),
            ("Tourist", "Electronic Travel Authorisation (ETA)", "Up to 6 months per visit, valid 2 years", "GBP 10", "Nationals of specified countries (rolling out 2024-2025)"),
            ("Business", "Standard Visitor (Business)", "Up to 6 months", "GBP 115", "Business meetings, conferences, training — no paid work"),
            ("Work", "Skilled Worker Visa", "Up to 5 years", "GBP 719 - GBP 1,420", "CoS from licensed sponsor, job on eligible occupations list, salary threshold GBP 38,700"),
            ("Work", "Health and Care Worker Visa", "Up to 5 years", "GBP 284", "NHS or social care role, CoS, lower salary threshold GBP 29,000"),
            ("Work", "Global Talent Visa", "Up to 5 years", "GBP 716", "Endorsement from recognized body in science, humanities, engineering, arts, or digital technology"),
            ("Work", "Scale-Up Visa", "2 years", "GBP 822", "Job with qualifying scale-up company, salary GBP 36,300+"),
            ("Work", "Intra-Company Transfer (Senior/Specialist)", "Up to 5 years", "GBP 719 - GBP 1,420", "Transfer from overseas linked entity, salary GBP 48,500+"),
            ("Work", "Youth Mobility Scheme", "2 years", "GBP 298", "Age 18-30, eligible nationality (Australia, Canada, Japan, etc.), ballot selection"),
            ("Work", "Seasonal Worker Visa", "6 months", "GBP 298", "Agriculture or poultry work, licensed sponsor"),
            ("Student", "Student Visa", "Duration of course + wrap-up", "GBP 490", "CAS from licensed student sponsor, financial proof (GBP 1,023/month London, GBP 820/month outside)"),
            ("Student", "Child Student Visa", "Duration of course", "GBP 490", "Independent school admission, parental consent, financial proof"),
            ("Student", "Graduate Visa", "2 years (3 years for PhD)", "GBP 822", "Completed eligible UK degree, applied within 2 years of student visa expiry"),
            ("Family", "Spouse/Partner Visa", "2.5 years (initial, then extension)", "GBP 1,846", "Financial requirement GBP 29,000, genuine relationship, English A1"),
            ("Family", "Parent Visa", "2.5 years", "GBP 1,846", "Sole responsibility for child settled in UK, or access rights"),
            ("Investor", "Innovator Founder Visa", "3 years", "GBP 1,292", "Endorsement from approved body, innovative business idea, GBP 50,000+ investment funds"),
            ("Transit", "Direct Airside Transit Visa (DATV)", "Transit only", "GBP 64", "Required for certain nationalities changing planes at UK airports"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("Standard Visitor Visa", "3 weeks (15 working days)", "5 working days (priority) / 24h (super priority)", "GBP 500 (priority) / GBP 1,000 (super priority)"),
            ("Skilled Worker Visa", "3 weeks (outside UK) / 8 weeks (inside UK)", "5 working days (priority)", "GBP 500"),
            ("Student Visa", "3 weeks (outside UK) / 8 weeks (inside UK)", "5 working days (priority)", "GBP 500"),
            ("Global Talent", "Endorsement: 5-8 weeks; Visa: 3 weeks", "N/A", "N/A"),
            ("Spouse/Partner Visa", "12 weeks (outside UK) / 8 weeks (inside UK)", "5 working days (priority)", "GBP 500"),
            ("Graduate Visa", "8 weeks", "N/A", "N/A"),
            ("Youth Mobility Scheme", "3 weeks", "5 working days", "GBP 500"),
        ],
        "health_requirements": """<ul>
<li><strong>Immigration Health Surcharge (IHS):</strong> Mandatory for all visa applicants staying 6+ months. GBP 1,035 per year (GBP 776 for students and Youth Mobility). Grants access to NHS services.</li>
<li><strong>TB test:</strong> Required for applicants from listed high-risk TB countries applying for a visa of 6+ months. Must be conducted at an approved clinic. Valid for 6 months.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry to the UK.</li>
<li><strong>Medical exam:</strong> Not routinely required for visa applications beyond the TB test. Applicants with known serious health conditions may need to disclose them.</li>
<li><strong>Police clearance:</strong> Required for certain visa types — ACRO police certificate for those in the UK, home-country police certificate for overseas applicants. Required for settlement and some work visas.</li>
<li><strong>Biometrics:</strong> Fingerprints and photo required for all visa applicants. Collected at a Visa Application Centre (VAC) or UKVCAS service point (inside UK). Reusable for subsequent applications in some cases.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Visitor visa:</strong> Cannot be extended beyond 6 months (except for medical treatment, academic visitors up to 12 months, or permitted paid engagements).</li>
<li><strong>Skilled Worker:</strong> Can be extended in up to 5-year increments. Eligible for Indefinite Leave to Remain (ILR/settlement) after 5 years of continuous employment.</li>
<li><strong>Student visa:</strong> Can apply for a new CAS and extend for further study. After completion, can switch to Graduate Visa (2-3 years) or Skilled Worker Visa.</li>
<li><strong>Spouse/Partner:</strong> Initial 2.5 years, then extend for another 2.5 years. ILR eligible after 5 years total. Relationship must be genuine and subsisting throughout.</li>
<li><strong>Switching in-country:</strong> Most long-term visa categories allow switching from within the UK without leaving. Visitors cannot switch to most work or study routes (some exceptions).</li>
<li><strong>Overstay consequences:</strong> Overstaying is a criminal offense. Leads to removal, re-entry ban (1-10 years), and a marker on immigration record. Voluntary departure within 30 days of overstay avoids a re-entry ban.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient funds, inadequate ties to home country, document fraud or deception, previous immigration violations, not meeting salary threshold (work visas), inadequate English proficiency, sham relationship concerns (spouse visas).</li>
<li><strong>Administrative Review:</strong> Available for eligible decisions (Points-Based System refusals). Must be filed within 28 days (14 days if in UK). Fee: GBP 80. An independent caseworker reviews the original decision.</li>
<li><strong>Appeal:</strong> Some refusals (e.g., human rights claims, EU Settlement Scheme) carry a right of appeal to the First-tier Tribunal (Immigration and Asylum Chamber). Must be filed within 14-28 days.</li>
<li><strong>Judicial Review:</strong> For decisions with no appeal or administrative review right, an application for Judicial Review can be made to the Upper Tribunal or High Court.</li>
<li><strong>Reapplication:</strong> No ban on reapplying (unless deception found). New applications should address refusal reasons with strengthened evidence.</li>
</ul>""",
        "extra_faqs": [
            ("Do I need a visa to visit the UK as a tourist?", "Citizens of many countries including the US, EU, Canada, Australia, and Japan can visit the UK visa-free for up to 6 months. Other nationals need a Standard Visitor Visa (GBP 115). The UK is introducing an Electronic Travel Authorisation (ETA) for visa-exempt nationals."),
            ("What is the UK Immigration Health Surcharge?", "The IHS is a mandatory fee for visa applicants staying 6+ months. It costs GBP 1,035 per year (GBP 776 for students and Youth Mobility). It grants access to NHS healthcare services on the same basis as a UK resident. Must be paid upfront for the full visa duration."),
            ("What is the UK Skilled Worker visa salary threshold?", "The general salary threshold for the Skilled Worker visa is GBP 38,700 per year (or the going rate for the occupation, whichever is higher). Some exceptions apply: new entrants pay GBP 30,960, and Health and Care Workers have a lower threshold of GBP 29,000."),
            ("Can I switch from a UK student visa to a work visa?", "Yes. After completing your studies, you can apply for the Graduate Visa (2 years, or 3 years for PhD, no sponsor needed). Alternatively, if you have a job offer from a licensed sponsor meeting the salary threshold, you can switch directly to a Skilled Worker Visa from within the UK."),
            ("What is the UK Global Talent visa?", "The Global Talent visa is for leaders or potential leaders in academia, research, arts, culture, or digital technology. It requires endorsement from a recognized body (e.g., Tech Nation, UKRI, British Academy). It leads to settlement after 3-5 years and does not require employer sponsorship."),
        ],
    },
    "spain": {
        "file": "spain-visa-requirements.html",
        "name": "Spain",
        "flag": "es",
        "visa_types": [
            ("Tourist", "Schengen Short-Stay (C)", "90 days in 180 days", "EUR 80 / EUR 40 (children 6-12)", "Travel insurance, accommodation, financial means"),
            ("Tourist", "Visa-Free (Schengen)", "90 days in 180 days", "Free", "60+ visa-exempt countries"),
            ("Work", "Highly Qualified Professional (HQP)", "Up to 2 years", "EUR 80 (visa) + EUR 100 (work permit)", "Job offer in qualifying profession, university degree, employer registration"),
            ("Work", "Entrepreneur Visa", "1 year (renewable)", "EUR 80 (visa)", "Viable business plan, EUR 25,000+ capital, approval from Commercial Office"),
            ("Work", "Intra-Company Transfer", "Up to 3 years", "EUR 80", "Transfer from non-EU company, managerial or specialist role"),
            ("Work", "Seasonal Worker", "Up to 9 months", "EUR 80", "Employer sponsorship, seasonal work contract"),
            ("Student", "Student Visa (D)", "Duration of course", "EUR 80", "Acceptance from Spanish institution, financial proof (EUR 600/month), health insurance"),
            ("Family", "Family Reunification", "1 year (renewable)", "EUR 80", "Legal resident sponsor, income requirement, adequate housing"),
            ("Digital Nomad", "Digital Nomad Visa", "Up to 1 year (renewable to 3)", "EUR 80 (visa) + EUR 70 (permit)", "Remote worker for non-Spanish company, income 200% of Spanish minimum wage, health insurance"),
            ("Retirement", "Non-Lucrative Visa", "1 year (renewable)", "EUR 80", "Passive income EUR 2,400/month (EUR 600 per additional family member), no work permitted, health insurance"),
            ("Investor", "Golden Visa (Investor)", "2 years (renewable)", "EUR 80 (visa) + EUR 1,050 (permit)", "EUR 500,000 real estate, or EUR 1M bank deposit, or EUR 2M government bonds, or EUR 1M business investment"),
            ("Transit", "Airport Transit (A)", "Transit only", "EUR 80", "Required for certain nationalities"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("Schengen Short-Stay (C)", "15 calendar days (up to 45 days)", "N/A", "N/A"),
            ("Student Visa (D)", "1-3 months", "N/A", "N/A"),
            ("Digital Nomad Visa", "20 business days (visa) + 20 days (permit)", "N/A", "N/A"),
            ("Golden Visa", "20 business days", "N/A", "N/A"),
            ("Non-Lucrative Visa", "1-3 months", "N/A", "N/A"),
            ("Highly Qualified Professional", "20-45 business days", "N/A", "N/A"),
            ("Family Reunification", "2-6 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Travel insurance:</strong> Mandatory for Schengen visa — minimum EUR 30,000 coverage for medical and repatriation.</li>
<li><strong>Health insurance (long-stay):</strong> Private health insurance with no co-payments required for non-lucrative, student, and digital nomad visas. Must cover the full duration of stay in Spain.</li>
<li><strong>Medical exam:</strong> Health certificate required for long-stay visa applications — issued by a doctor confirming no diseases subject to International Health Regulations.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry.</li>
<li><strong>Police clearance:</strong> Criminal record certificate required for all long-stay visa applications. Must be apostilled and translated into Spanish. Valid for 3 months from issue date.</li>
<li><strong>Biometrics:</strong> Fingerprints and photo collected at the embassy or VFS center.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Schengen short-stay:</strong> Cannot be extended except in exceptional circumstances.</li>
<li><strong>Long-stay residence permits:</strong> Apply for renewal at the Oficina de Extranjeria 60 days before expiry. Most permits renewable in 2-year increments after the first year.</li>
<li><strong>Non-lucrative visa:</strong> First renewal for 2 years, then 2-year renewals. After 5 years: long-term residence (residence de larga duracion).</li>
<li><strong>Digital Nomad Visa:</strong> Initial 1 year, renewable for up to 3 years total.</li>
<li><strong>Golden Visa:</strong> Initial 2 years, renewable for 5-year periods as long as investment maintained.</li>
<li><strong>Overstay:</strong> Fines of EUR 501-10,000, deportation proceedings, and Schengen-wide entry ban up to 5 years.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient financial proof, inadequate health insurance, incomplete documentation, previous Schengen violations, criminal record.</li>
<li><strong>Appeal (Recurso):</strong> Schengen visa refusals can be appealed through recurso de reposicion (1 month) or directly to the administrative court (contencioso-administrativo, 2 months).</li>
<li><strong>Long-stay refusal:</strong> Can be appealed through administrative channels (recurso de alzada) or the courts.</li>
<li><strong>Reapplication:</strong> No mandatory waiting period. Address the specific refusal reasons.</li>
</ul>""",
        "extra_faqs": [
            ("Does Spain offer a digital nomad visa?", "Yes. Spain's Digital Nomad Visa (Ley de Startups) allows remote workers employed by non-Spanish companies to live in Spain for up to 1 year, renewable to 3 years. Income must be at least 200% of the Spanish minimum wage. The visa costs EUR 80 plus EUR 70 for the residence permit."),
            ("What is Spain's Golden Visa?", "Spain's Golden Visa grants residency to investors who make qualifying investments: EUR 500,000 in real estate, EUR 1M in bank deposits, EUR 2M in government bonds, or EUR 1M in business investment. It grants 2-year residence renewable for 5-year periods and allows free Schengen travel."),
            ("Can I retire in Spain with a non-lucrative visa?", "Yes. The Non-Lucrative Visa is designed for retirees and those with passive income. You need EUR 2,400/month (plus EUR 600 per dependent), private health insurance, and you cannot work in Spain. It is renewable and leads to permanent residence after 5 years."),
            ("How much does Schengen travel insurance cost for Spain?", "Schengen travel insurance for Spain typically costs EUR 30-100 for a short trip, depending on duration, age, and coverage level. The minimum required coverage is EUR 30,000 for medical expenses and repatriation, and the policy must be valid for the entire Schengen area."),
        ],
    },
    "italy": {
        "file": "italy-visa-requirements.html",
        "name": "Italy",
        "flag": "it",
        "visa_types": [
            ("Tourist", "Schengen Short-Stay (C)", "90 days in 180 days", "EUR 80 / EUR 40 (children 6-12)", "Travel insurance, accommodation, financial means"),
            ("Tourist", "Visa-Free (Schengen)", "90 days in 180 days", "Free", "60+ visa-exempt countries"),
            ("Work", "Work Visa (Subordinate Employment)", "Up to 2 years", "EUR 116", "Nulla Osta from immigration office, employer quota allocation, annual Decreto Flussi"),
            ("Work", "EU Blue Card (Italy)", "Up to 2 years", "EUR 116", "University degree, job offer with minimum salary (1.5x average), employer sponsorship"),
            ("Work", "Self-Employment Visa", "Up to 2 years", "EUR 116", "Chamber of Commerce registration, adequate funding, Nulla Osta"),
            ("Work", "Seasonal Worker", "Up to 9 months", "EUR 116", "Employer quota allocation via Decreto Flussi, seasonal work contract"),
            ("Student", "Student Visa (D)", "Duration of course", "EUR 50", "University pre-enrollment, financial proof (EUR 489/month), accommodation, health insurance"),
            ("Family", "Family Reunification", "Up to 2 years", "EUR 116", "Sponsor with valid permit, income threshold, adequate housing (idoneita abitativa)"),
            ("Investor", "Investor Visa", "2 years (renewable)", "EUR 116", "EUR 250,000 innovative startup, EUR 500,000 Italian company, EUR 1M philanthropic, EUR 2M government bonds"),
            ("Digital Nomad", "Digital Nomad Visa", "Up to 1 year (renewable)", "EUR 116", "Remote worker, income EUR 28,000+/year, health insurance, non-Italian employer"),
            ("Retirement", "Elective Residence Visa", "1 year (renewable)", "EUR 116", "Passive income (pensions, investments), no employment, adequate accommodation"),
            ("Transit", "Airport Transit (A)", "Transit only", "EUR 80", "Required for certain nationalities"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("Schengen Short-Stay (C)", "15 calendar days (up to 45 days)", "N/A", "N/A"),
            ("Work Visa (with Nulla Osta)", "30-120 days for Nulla Osta + 30 days for visa", "N/A", "N/A"),
            ("Student Visa (D)", "2-6 weeks", "N/A", "N/A"),
            ("Investor Visa", "30 days for committee + 30 days visa", "N/A", "N/A"),
            ("Family Reunification", "90-180 days for Nulla Osta + 30 days visa", "N/A", "N/A"),
            ("Elective Residence", "2-3 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Travel insurance:</strong> Mandatory for Schengen visa — EUR 30,000 minimum medical coverage.</li>
<li><strong>Health insurance (long-stay):</strong> Private health insurance required for student, elective residence, and digital nomad visas. Or enrollment in Italy's SSN (Servizio Sanitario Nazionale) upon obtaining residence permit (voluntary enrollment: EUR 388/year for students, EUR 2,000/year for others).</li>
<li><strong>Medical exam:</strong> Not required for most visa categories.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry. Children must have mandatory vaccinations for school enrollment (10 vaccines required by Italian law).</li>
<li><strong>Police clearance:</strong> Criminal record certificate required for long-stay visa applications — apostilled and translated into Italian.</li>
<li><strong>Biometrics:</strong> Collected at visa application center or embassy.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Schengen short-stay:</strong> Cannot be extended except in exceptional circumstances.</li>
<li><strong>Permesso di Soggiorno (residence permit):</strong> Must apply at the post office (kit postale) within 8 days of arrival. Renewed at the Questura before expiry.</li>
<li><strong>Work permits:</strong> Renewable based on continued employment. After 5 years: EU long-term residence permit.</li>
<li><strong>Student permits:</strong> Renewable annually with enrollment proof. Can convert to work permit upon graduation.</li>
<li><strong>Overstay:</strong> Results in deportation order (espulsione), Schengen entry ban up to 5 years, and administrative fines.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient funds, incomplete documents, previous Schengen violations, Decreto Flussi quota exhausted (work visas), criminal record.</li>
<li><strong>Appeal:</strong> Schengen visa refusals can be appealed to the TAR (Tribunale Amministrativo Regionale) within 60 days. Long-stay refusals can be challenged through administrative courts.</li>
<li><strong>Reapplication:</strong> No mandatory waiting period for short-stay visa refusals.</li>
</ul>""",
        "extra_faqs": [
            ("Does Italy have a digital nomad visa?", "Yes. Italy introduced its Digital Nomad Visa for remote workers employed by non-Italian companies with an annual income of at least EUR 28,000. It allows a stay of up to 1 year (renewable) and requires private health insurance."),
            ("What is Italy's Investor Visa?", "Italy's Investor Visa offers 2-year residence (renewable) for investments in Italian companies (EUR 500,000), innovative startups (EUR 250,000), government bonds (EUR 2M), or philanthropic donations (EUR 1M). It includes a fast-track process."),
            ("Can I retire in Italy?", "Yes. The Elective Residence Visa (Visto per Residenza Elettiva) allows retirees with stable passive income to live in Italy. You need adequate income from pensions, investments, or property, and must not engage in employment. It is renewable annually."),
            ("What is the Decreto Flussi for Italy work visas?", "The Decreto Flussi is the annual quota decree that sets the number of non-EU workers allowed to enter Italy for employment each year. Employers must apply for quota allocations, and applications are processed on a first-come, first-served basis. The decree is published annually (usually in January) and quotas fill quickly."),
        ],
    },
    "turkey": {
        "file": "turkey-visa-requirements.html",
        "name": "Turkey",
        "flag": "tr",
        "visa_types": [
            ("Tourist", "e-Visa", "30-90 days (nationality dependent)", "USD 50 (most nationalities)", "Online at evisa.gov.tr, passport, return ticket"),
            ("Tourist", "Visa-Free Entry", "Up to 90 days", "Free", "EU, Japan, South Korea, Brazil, etc."),
            ("Tourist", "Sticker Visa (Embassy)", "30-90 days", "Varies", "Embassy application, travel itinerary, financial proof"),
            ("Business", "Business Visa", "30-90 days", "USD 50-100", "Business invitation from Turkish company, company letter"),
            ("Work", "Work Permit", "Up to 1 year (renewable)", "Application fee varies", "Employer sponsorship, application through e-devlet, Ministry of Labour approval"),
            ("Work", "Turquoise Card", "Indefinite", "Free", "Highly qualified professionals, investors, scientists — Turkey's equivalent of a green card"),
            ("Student", "Student Visa", "Duration of course", "Varies by nationality", "Acceptance from Turkish institution, financial proof, health insurance"),
            ("Family", "Family Residence Permit", "Up to 2 years (renewable)", "Varies", "Spouse or child of Turkish citizen/legal resident"),
            ("Investor", "Investment Visa / Citizenship by Investment", "Citizenship", "N/A", "USD 400,000 real estate, or USD 500,000 bank deposit, or USD 500,000 capital investment"),
            ("Retirement", "Short-Term Residence Permit", "Up to 2 years", "Varies", "Sufficient income, health insurance, no employment"),
            ("Transit", "Transit Visa", "72 hours", "Free or USD 30", "Confirmed onward ticket"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("e-Visa", "Instant to 24 hours", "N/A", "N/A"),
            ("Sticker Visa (Embassy)", "5-15 business days", "3 business days", "USD 30-50 surcharge"),
            ("Work Permit", "30-90 days", "N/A", "N/A"),
            ("Student Visa", "5-15 business days", "N/A", "N/A"),
            ("Residence Permit", "30-90 days (after in-country application)", "N/A", "N/A"),
            ("Turquoise Card", "3-6 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for work permits and residence permits exceeding 1 year. Must be performed at a Turkish public hospital.</li>
<li><strong>Health insurance:</strong> Mandatory for all residence permit applications. Must be from a Turkish-approved insurer or SGK (Social Security) enrollment for work permit holders.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry.</li>
<li><strong>Police clearance:</strong> Required for work permits and long-term residence — apostilled criminal record from home country.</li>
<li><strong>Biometrics:</strong> Fingerprints and photo collected at residence permit appointment at the Provincial Directorate of Migration Management (Il Goc Idaresi).</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>e-Visa / tourist visa:</strong> Cannot be extended. Must exit and re-enter or apply for a residence permit.</li>
<li><strong>Residence permit:</strong> Apply for renewal online through e-ikamet.goc.gov.tr at least 60 days before expiry. Short-term permits renewable up to a total of 8 years, then eligible for long-term permit.</li>
<li><strong>Work permit:</strong> Renewable through employer application. After 8 years of legal work: eligible for indefinite work permit.</li>
<li><strong>Overstay:</strong> Fines and deportation. Overstay exceeding the administrative fine period results in entry bans (1-5 years). Voluntary departure within 10 days may reduce penalties.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient funds, criminal record, security concerns, incomplete documentation, previous overstay in Turkey.</li>
<li><strong>Appeal:</strong> e-Visa refusals have no formal appeal. Embassy visa refusals can be reconsidered by submitting additional documents. Residence permit refusals can be appealed to administrative courts within 60 days.</li>
<li><strong>Reapplication:</strong> Can reapply for e-Visa or embassy visa immediately. Address refusal reasons in the new application.</li>
</ul>""",
        "extra_faqs": [
            ("How do I get a Turkey e-Visa?", "Apply online at evisa.gov.tr. Select your nationality, enter travel dates and passport details, pay the fee (typically USD 50), and receive the e-Visa instantly or within 24 hours via email. Print it and present at the Turkish border."),
            ("Can I get Turkish citizenship through investment?", "Yes. Turkey offers citizenship by investment through purchasing real estate worth USD 400,000+, depositing USD 500,000 in a Turkish bank, or making a capital investment of USD 500,000+. The process takes 3-6 months and includes spouse and children under 18."),
            ("What is Turkey's Turquoise Card?", "The Turquoise Card is Turkey's equivalent of a permanent residence or green card for highly qualified individuals. It offers indefinite residence and work rights and is available to qualified scientists, investors, athletes, artists, and professionals with international recognition."),
            ("Do I need a visa for Turkey from the EU?", "Most EU citizens can enter Turkey visa-free for up to 90 days within a 180-day period. Some EU nationalities (e.g., certain Eastern European countries) may need an e-Visa. Check evisa.gov.tr for your specific nationality."),
        ],
    },
    "uae": {
        "file": "uae-visa-requirements.html",
        "name": "UAE",
        "flag": "ae",
        "visa_types": [
            ("Tourist", "Visa on Arrival", "30 days (extendable)", "Free", "70+ nationalities including EU, US, UK, Australia — passport stamped at airport"),
            ("Tourist", "Tourist Visa (30 days)", "30 days", "AED 300 (~USD 82)", "Sponsor (hotel, airline, or tour operator), passport copy, photo"),
            ("Tourist", "Tourist Visa (90 days)", "90 days", "AED 650 (~USD 177)", "Sponsor required, passport, photo"),
            ("Tourist", "Multiple Entry Tourist Visa (5 years)", "90 days per visit", "AED 650 (~USD 177)", "Valid passport, photo, proof of financial means"),
            ("Business", "Business/Visit Visa", "30-90 days", "AED 500-1,000", "UAE company sponsorship, invitation letter"),
            ("Work", "Employment Visa", "2-3 years", "AED 5,000-10,000 (employer-sponsored)", "Employer sponsorship, work permit from MOHRE, medical fitness test, Emirates ID"),
            ("Work", "Golden Visa", "10 years", "AED 2,800-4,000", "Investors (AED 2M), entrepreneurs, specialized talents, scientists, outstanding students, frontline heroes"),
            ("Work", "Green Visa (Self-Sponsored)", "5 years", "AED 2,800", "Skilled professionals, freelancers, investors — no employer sponsor needed"),
            ("Work", "Freelancer Visa", "1-5 years", "AED 7,500-15,000", "Freelance permit from a free zone, professional portfolio"),
            ("Student", "Student Visa", "1 year (renewable)", "AED 2,500-5,000", "Acceptance from UAE institution, financial proof, medical fitness"),
            ("Family", "Family/Dependent Visa", "2-3 years (tied to sponsor)", "AED 3,000-5,000", "Sponsor with minimum salary (AED 4,000 or AED 3,000 + accommodation), marriage/birth certificates attested"),
            ("Investor", "Investor Visa (Property)", "2-10 years", "Varies", "Property value AED 750,000+ (2-year) or AED 2M+ (Golden Visa)"),
            ("Retirement", "Retirement Visa", "5 years (renewable)", "AED 2,800", "Age 55+, property worth AED 1M, savings of AED 1M, or income of AED 20,000/month"),
            ("Transit", "Transit Visa", "48-96 hours", "Free (via airlines)", "Confirmed onward ticket, arranged by airline"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("Visa on Arrival", "Instant", "N/A", "N/A"),
            ("Tourist Visa (30/90 days)", "3-5 business days", "24 hours (express)", "AED 250 surcharge"),
            ("Employment Visa", "2-4 weeks (work permit + entry permit)", "N/A", "N/A"),
            ("Golden Visa", "30 days", "N/A", "N/A"),
            ("Student Visa", "2-4 weeks", "N/A", "N/A"),
            ("Family Visa", "2-4 weeks", "N/A", "N/A"),
            ("Retirement Visa", "2-4 weeks", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical fitness test:</strong> Required for all residence visa holders (employment, family, student). Includes blood test (HIV, Hepatitis B/C, syphilis, tuberculosis) and chest X-ray. Conducted at SEHA health centers or approved clinics. Cost: AED 250-500.</li>
<li><strong>Failing medical:</strong> Positive results for HIV, Hepatitis B/C, or active tuberculosis may result in visa denial and deportation (though policies have been relaxed for Hepatitis B in some cases).</li>
<li><strong>Health insurance:</strong> Mandatory for all residents in Dubai (ISAHD) and Abu Dhabi (HAAD). Employer must provide health insurance for employees.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry.</li>
<li><strong>Police clearance:</strong> Not routinely required for visa applications. May be required for certain employment or government positions.</li>
<li><strong>Emirates ID:</strong> Biometric Emirates ID card required for all residents. Includes fingerprints and iris scan. Applied for after entry on residence visa.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Visa on Arrival (30 days):</strong> Extendable for 30 days at a GDRFA office or online. Fee: AED 600-1,000. Can extend twice for a total of 90 days.</li>
<li><strong>Tourist Visa:</strong> Extendable twice (30 days each). Total maximum stay varies by visa type.</li>
<li><strong>Employment Visa:</strong> Renewed by employer through MOHRE. Must maintain valid Emirates ID and medical fitness.</li>
<li><strong>Golden Visa:</strong> Automatically renewable for 10 years as long as qualifying conditions are maintained.</li>
<li><strong>Grace period:</strong> 30-day grace period after visa expiry or cancellation to either leave the UAE or change status.</li>
<li><strong>Overstay:</strong> Fine of AED 50 per day (first 6 months), increasing to AED 100/day thereafter. Maximum fine before legal action.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Previous overstay or absconding record, failed medical fitness test, security concerns, incomplete documentation, previous deportation.</li>
<li><strong>Appeal:</strong> No formal public appeal process for tourist visa refusals. Employment visa denials can be challenged through MOHRE. Medical fitness failures may allow re-testing.</li>
<li><strong>Blacklist:</strong> Immigration blacklist can result from absconding from employer, criminal record, or deportation. Removal requires employer or legal intervention.</li>
<li><strong>Reapplication:</strong> For tourist visas, reapply with corrected documentation. Entry bans from overstay or absconding require clearance from GDRFA.</li>
</ul>""",
        "extra_faqs": [
            ("Do I need a visa for the UAE?", "Citizens of 70+ countries (including the EU, US, UK, and Australia) receive a free visa on arrival for 30 days. Other nationalities need a tourist visa arranged through a UAE sponsor (hotel, airline, or tour operator). Check the official ICP website for your nationality."),
            ("What is the UAE Golden Visa?", "The UAE Golden Visa is a 10-year renewable residence permit for investors (AED 2M+), entrepreneurs, specialized talents, researchers, outstanding students, and frontline heroes. It does not require an employer sponsor and allows extended stays outside the UAE without losing residency."),
            ("How much is the UAE overstay fine?", "The UAE overstay fine is AED 50 per day for the first 6 months, increasing to AED 100 per day after that. There is a 30-day grace period after visa expiry. To clear overstay fines, you must pay at a GDRFA office or through an approved travel agency."),
            ("Can I work as a freelancer in the UAE?", "Yes. The UAE offers freelancer visas through free zones (such as Dubai Media City, DMCC, or Fujairah Creative City). Freelancers can self-sponsor their residence visa for 1-5 years. The Green Visa also allows skilled professionals to be self-sponsored without an employer."),
        ],
    },
    "singapore": {
        "file": "singapore-visa-requirements.html",
        "name": "Singapore",
        "flag": "sg",
        "visa_types": [
            ("Tourist", "Visa-Free Entry", "30-90 days (nationality dependent)", "Free", "US, UK, EU, Japan, South Korea, etc. — stamp at immigration"),
            ("Tourist", "Tourist Visa", "30 days", "SGD 30", "Sponsor in Singapore (citizen/PR or company), SG Arrival Card required"),
            ("Business", "Business Visa", "30 days", "SGD 30", "Company sponsor in Singapore, business purpose letter"),
            ("Work", "Employment Pass (EP)", "Up to 2 years (renewable)", "SGD 105", "Job offer with minimum salary SGD 5,000 (SGD 5,500 for financial sector), COMPASS framework points"),
            ("Work", "S Pass", "Up to 2 years", "SGD 105", "Mid-skilled workers, minimum salary SGD 3,150, employer quota and levy"),
            ("Work", "Work Permit (WP)", "Up to 2 years", "SGD 35", "Semi-skilled workers in construction, manufacturing, marine, services, domestic work. Employer quota and levy."),
            ("Work", "EntrePass", "1 year (renewable)", "SGD 105", "Entrepreneurs with innovative business, VC funding, or significant IP"),
            ("Work", "Personalised Employment Pass (PEP)", "3 years (non-renewable)", "SGD 105", "EP holders earning SGD 22,500/month or overseas professionals earning SGD 18,000/month equivalent"),
            ("Work", "Overseas Networks & Expertise Pass (ONE Pass)", "5 years", "SGD 105", "Top talent earning SGD 30,000/month or with outstanding achievements in arts, sports, science, academia"),
            ("Work", "Work Holiday Pass", "6 months", "Free", "Age 18-25, from approved university in Australia, France, Germany, Japan, etc."),
            ("Student", "Student Pass", "Duration of course", "SGD 30", "Acceptance from approved institution, Form 16, financial proof"),
            ("Family", "Dependant's Pass", "Tied to EP/S Pass holder", "SGD 105", "Spouse or children of EP/S Pass holder with minimum salary SGD 6,000"),
            ("Family", "Long-Term Visit Pass (LTVP)", "Up to 5 years", "SGD 105", "Spouse of Singapore citizen, parents, common-law spouse"),
            ("Investor", "Global Investor Programme (GIP)", "Permanent Residence", "SGD 7,000 (PR fee)", "SGD 10M investment in business/fund, or SGD 25M in Single Family Office, 5 years business track record"),
            ("Transit", "Transit (no visa required)", "96 hours (VFTF)", "Free", "Visa-Free Transit Facility — eligible nationalities with onward ticket"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("Visa-Free Entry", "Instant", "N/A", "N/A"),
            ("Tourist Visa", "3-5 business days", "N/A", "N/A"),
            ("Employment Pass (EP)", "3-8 weeks", "N/A", "N/A"),
            ("S Pass", "3-8 weeks", "N/A", "N/A"),
            ("ONE Pass", "4-8 weeks", "N/A", "N/A"),
            ("Student Pass", "2-4 weeks", "N/A", "N/A"),
            ("Dependant's Pass", "3-8 weeks", "N/A", "N/A"),
            ("GIP (PR)", "6-12 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for all work pass holders (EP, S Pass, Work Permit). Includes HIV test, syphilis screening, malaria, chest X-ray, and pregnancy test for female WP holders. Must be performed by a registered Singapore doctor.</li>
<li><strong>6-monthly medical exam:</strong> Work Permit holders in certain sectors require medical exams every 6 months.</li>
<li><strong>Vaccinations:</strong> Yellow fever certificate required if arriving from an endemic area. No other mandatory vaccinations for entry.</li>
<li><strong>COVID-19:</strong> No vaccination or testing requirements as of 2026.</li>
<li><strong>Health insurance:</strong> Employers are required to provide medical insurance for Work Permit and S Pass holders (minimum SGD 15,000 annual coverage).</li>
<li><strong>Biometrics:</strong> Fingerprints and photo collected at immigration checkpoint for all visitors.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Tourist visa / visa-free:</strong> May be extended online through ICA e-Service for up to 89 days total. Fee: SGD 40 per extension. Approval is discretionary.</li>
<li><strong>Employment Pass:</strong> Renewable in 2-3 year increments. Apply at least 3 months before expiry through EP Online. Must continue to meet salary and COMPASS requirements.</li>
<li><strong>S Pass / Work Permit:</strong> Renewable by employer. Work Permits have maximum employment periods by nationality and sector.</li>
<li><strong>Student Pass:</strong> Renewable with continued enrollment.</li>
<li><strong>Overstay:</strong> Criminal offense in Singapore. Penalties include imprisonment (up to 6 months), fine, caning (for males under 50, if illegal entry), and deportation with re-entry ban.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient documentation, security concerns, previous immigration violations, employer quota exceeded (S Pass/WP), failed COMPASS criteria (EP), salary below threshold, false information.</li>
<li><strong>Appeal:</strong> EP/S Pass refusals can be appealed within 3 months through EP Online with additional supporting documents. Tourist visa refusals have no formal appeal.</li>
<li><strong>Reapplication:</strong> Can reapply with improved documentation. Multiple consecutive rejections may trigger additional scrutiny.</li>
</ul>""",
        "extra_faqs": [
            ("What is Singapore's COMPASS framework for Employment Pass?", "COMPASS is a points-based framework for Employment Pass applications introduced in 2023. Applicants are assessed on salary, qualifications, diversity, support for local employment, and bonus criteria (skills bonus, strategic economic priorities). A minimum of 40 points is required. Salary and qualification criteria carry the most weight."),
            ("What is the ONE Pass for Singapore?", "The Overseas Networks and Expertise Pass (ONE Pass) is Singapore's top-tier work visa for exceptional talent. It requires a fixed monthly salary of SGD 30,000 or outstanding achievements in arts, sports, science, or academia. Valid for 5 years with the flexibility to work for multiple employers and start businesses."),
            ("Can I get permanent residence in Singapore?", "Yes. Routes include the Global Investor Programme (SGD 10M+ investment), applying after holding EP/S Pass for 2+ years, or through family ties (spouse/child of citizen/PR). Singapore PR applications are assessed holistically on age, qualifications, income, time in Singapore, and family profile."),
            ("Is overstaying in Singapore a serious offense?", "Yes. Overstaying in Singapore is a criminal offense punishable by imprisonment (up to 6 months), fines, and for those who entered illegally, possible caning for males under 50. Singapore has strict immigration enforcement."),
        ],
    },
    "malaysia": {
        "file": "malaysia-visa-requirements.html",
        "name": "Malaysia",
        "flag": "my",
        "visa_types": [
            ("Tourist", "Visa-Free Entry", "14-90 days (nationality dependent)", "Free", "US, EU, UK, most ASEAN — 90 days; Indian/Chinese — 30 days with MDAC"),
            ("Tourist", "Tourist Visa (Single Entry)", "30 days", "MYR 80-150", "Embassy application, financial proof, itinerary"),
            ("Tourist", "Tourist Visa (Multiple Entry)", "30 days per entry, 3-12 months validity", "MYR 150-300", "Embassy application, frequent traveler profile"),
            ("Business", "Business Visa", "30 days", "MYR 80-150", "Business invitation from Malaysian company"),
            ("Work", "Employment Pass (EP)", "2-5 years", "MYR 200-2,000", "Minimum salary MYR 5,000 (EP-I: MYR 10,000+, EP-II: MYR 5,000-9,999), employer sponsorship via ESD"),
            ("Work", "Professional Visit Pass (PVP)", "Up to 12 months", "MYR 200", "Short-term professional assignment, employer sponsorship"),
            ("Work", "DE Rantau (Digital Nomad)", "Up to 1 year (renewable)", "MYR 1,000", "Income USD 24,000/year, remote worker for non-Malaysian company"),
            ("Student", "Student Pass", "Duration of course", "MYR 60-200", "Acceptance from approved Malaysian institution, financial proof, medical exam"),
            ("Family", "Dependent Pass", "Tied to EP holder", "MYR 200-500", "Spouse or children of EP holder"),
            ("Retirement", "MM2H (Malaysia My Second Home)", "5-15 years", "MYR 500-5,000", "Age 35+, financial requirements (fixed deposit MYR 500,000-1,000,000, offshore income MYR 40,000/month)"),
            ("Investor", "Premium Visa Programme (PVIP)", "20 years (renewable)", "MYR 200,000", "Ultra high net worth: MYR 2M fixed deposit, MYR 1M liquid assets, offshore income MYR 40,000/month"),
            ("Transit", "Transit Without Visa (TWOV)", "120 hours", "Free", "Confirmed onward ticket, certain nationalities"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("Visa-Free Entry", "Instant", "N/A", "N/A"),
            ("Tourist Visa", "3-5 business days", "1-2 business days", "MYR 50-100 surcharge"),
            ("Employment Pass", "2-8 weeks", "N/A", "N/A"),
            ("Student Pass", "2-4 weeks", "N/A", "N/A"),
            ("MM2H", "3-6 months", "N/A", "N/A"),
            ("DE Rantau", "2-4 weeks", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for Employment Pass and Student Pass holders. Includes blood tests, chest X-ray, and general health assessment at FOMEMA-registered clinics.</li>
<li><strong>Yellow Fever:</strong> Certificate required if arriving from endemic area.</li>
<li><strong>Health insurance:</strong> Required for MM2H and DE Rantau visa holders from approved Malaysian insurers.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for short-stay visitors.</li>
<li><strong>Police clearance:</strong> Required for work passes and MM2H — from home country, less than 6 months old.</li>
<li><strong>Biometrics:</strong> Fingerprints collected at immigration for visitors from certain countries.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Visa-free entry:</strong> Cannot be extended beyond the stamped duration. Must exit and re-enter.</li>
<li><strong>Tourist visa:</strong> Can be extended at the Immigration Department for up to 2 months in certain cases.</li>
<li><strong>Employment Pass:</strong> Renewable through employer via ESD. Must maintain minimum salary requirement.</li>
<li><strong>MM2H:</strong> Renewable. Must maintain fixed deposit and meet annual stay requirements.</li>
<li><strong>Overstay:</strong> Fine of MYR 10,000 or imprisonment up to 5 years, or both. Possible caning for immigration offenses.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient funds, previous overstay, security concerns, incomplete documentation, blacklisted.</li>
<li><strong>Appeal:</strong> No formal appeal for tourist visa refusals. Work pass refusals can be reconsidered with additional documents.</li>
<li><strong>Reapplication:</strong> Can reapply with improved documentation. Address specific refusal reasons.</li>
</ul>""",
        "extra_faqs": [
            ("What is the Malaysia DE Rantau (Digital Nomad) visa?", "DE Rantau is Malaysia's digital nomad visa allowing remote workers earning at least USD 24,000/year to live in Malaysia for up to 1 year (renewable). It requires employment with a non-Malaysian company and private health insurance. The pass costs MYR 1,000."),
            ("What is Malaysia My Second Home (MM2H)?", "MM2H is a long-term residence program for foreigners aged 35+ with substantial financial means. Requirements include a fixed deposit of MYR 500,000-1,000,000 and monthly offshore income of MYR 40,000. It grants 5-15 year renewable residence."),
            ("Can I enter Malaysia visa-free?", "Citizens of most Western countries (US, UK, EU, Australia, Japan, etc.) can enter Malaysia visa-free for up to 90 days. Citizens of India and China can get visa-free entry for 30 days under the MDAC arrangement. Check with Malaysian immigration for your specific nationality."),
        ],
    },
    "indonesia": {
        "file": "indonesia-visa-requirements.html",
        "name": "Indonesia",
        "flag": "id",
        "visa_types": [
            ("Tourist", "Visa on Arrival (VoA)", "30 days (extendable once)", "IDR 500,000 (~USD 32)", "92 eligible nationalities, payment at airport, return ticket"),
            ("Tourist", "Visa-Free Entry", "30 days (not extendable)", "Free", "ASEAN nationals and select countries"),
            ("Tourist", "e-Visa (B211A - Tourist)", "60 days (extendable)", "IDR 1,500,000 (~USD 96)", "Online application at molina.imigrasi.go.id, sponsor or agent required"),
            ("Business", "e-Visa (B211A - Business)", "60 days (extendable)", "IDR 1,500,000", "Indonesian business sponsor, invitation letter"),
            ("Work", "KITAS (Limited Stay Permit)", "1-2 years", "Varies (employer-sponsored)", "Employer sponsorship, work permit (IMTA), Ministry of Manpower approval"),
            ("Work", "Investor KITAS", "1-2 years", "Varies", "Investment in Indonesian company, BKPM approval"),
            ("Work", "Digital Nomad (B211A Remote Worker)", "6-12 months", "IDR 1,500,000 - 3,000,000", "Remote worker for non-Indonesian company, minimum income proof"),
            ("Student", "Student KITAS", "1 year (renewable)", "Varies", "Acceptance from Indonesian institution, sponsor"),
            ("Family", "Spouse/Family KITAS", "1-2 years", "Varies", "Married to Indonesian citizen, or dependent of KITAS holder"),
            ("Retirement", "Retirement KITAS (Lansia)", "1 year (renewable)", "Varies", "Age 55+, pension/income proof USD 1,500/month, health insurance, Indonesian designated agent"),
            ("Investor", "Second Home Visa", "5-10 years", "IDR 3,000,000", "Bank deposit IDR 2 billion (~USD 130,000) or property ownership, passive income"),
            ("Transit", "Transit Visa", "7 days", "Free", "Confirmed onward ticket"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("Visa on Arrival", "Instant (at airport)", "N/A", "N/A"),
            ("e-Visa B211A", "3-7 business days", "N/A", "N/A"),
            ("KITAS (Work)", "4-8 weeks", "N/A", "N/A"),
            ("Student KITAS", "4-6 weeks", "N/A", "N/A"),
            ("Retirement KITAS", "4-8 weeks", "N/A", "N/A"),
            ("Second Home Visa", "2-4 weeks", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for KITAS (work/family/retirement) — conducted at Indonesian government hospital.</li>
<li><strong>Yellow Fever:</strong> Certificate required if arriving from endemic area.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for most travelers.</li>
<li><strong>Health insurance:</strong> Required for retirement KITAS and recommended for all long-stay visas.</li>
<li><strong>Police clearance:</strong> SKCK (Surat Keterangan Catatan Kepolisian) from home country required for work KITAS.</li>
<li><strong>Biometrics:</strong> Collected at immigration office during KITAS processing.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Visa on Arrival:</strong> Extendable once for 30 days at any immigration office. Fee: IDR 500,000. Total maximum: 60 days.</li>
<li><strong>Visa-Free Entry:</strong> CANNOT be extended. Must exit Indonesia.</li>
<li><strong>e-Visa B211A:</strong> Extendable up to 4 times for 60 days each. Apply through immigration agent or immigration office.</li>
<li><strong>KITAS:</strong> Renewable. After 4 consecutive years on KITAS: eligible for KITAP (Permanent Stay Permit).</li>
<li><strong>Overstay:</strong> Fine of IDR 1,000,000 per day (max IDR 500,000,000). Detention and deportation possible.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Previous overstay, blacklisted, insufficient funds, incomplete documents, security concerns.</li>
<li><strong>Appeal:</strong> No formal appeal for e-Visa refusals. KITAS refusals can be reconsidered with additional documentation.</li>
<li><strong>Reapplication:</strong> Can reapply with corrected documentation. Blacklisted individuals must seek clearance from Indonesian immigration.</li>
</ul>""",
        "extra_faqs": [
            ("What is the difference between Visa on Arrival and visa-free for Indonesia?", "Visa on Arrival (IDR 500,000) is available for 92 nationalities and allows a 30-day stay extendable by 30 more days. Visa-free entry is available for ASEAN and select nationals for 30 days but CANNOT be extended. If you may need more time, always choose Visa on Arrival."),
            ("Does Indonesia have a digital nomad visa?", "Indonesia offers a B211A e-Visa for remote workers, allowing stays of 60 days extendable up to multiple times. For longer stays, the Second Home Visa (5-10 years) is available with a bank deposit of IDR 2 billion. A dedicated digital nomad visa category is under discussion."),
            ("What is Indonesia's Second Home Visa?", "The Second Home Visa allows stays of 5-10 years for those who deposit IDR 2 billion (~USD 130,000) in an Indonesian bank or own property of equivalent value. It does not permit employment but allows holders to live in Indonesia long-term."),
        ],
    },
    "vietnam": {
        "file": "vietnam-visa-requirements.html",
        "name": "Vietnam",
        "flag": "vn",
        "visa_types": [
            ("Tourist", "e-Visa", "90 days, single or multiple entry", "USD 25", "Online at evisa.xuatnhapcanh.gov.vn, 13 entry points expanded to all"),
            ("Tourist", "Visa-Free Entry", "15-45 days (nationality dependent)", "Free", "ASEAN 30 days, Japan/South Korea/Scandinavia 45 days, EU 45 days, UK 45 days"),
            ("Tourist", "Visa on Arrival (approval letter)", "30-90 days", "USD 25 (approval) + USD 25-50 (stamping)", "Approval letter from Vietnamese travel agency, collect visa at airport"),
            ("Tourist", "Embassy Visa", "30-90 days", "USD 40-100", "Embassy/consulate application, photo, passport"),
            ("Business", "Business Visa (DN)", "Up to 12 months", "Varies", "Vietnamese company sponsorship, invitation letter, business license"),
            ("Work", "Work Permit + Temporary Residence Card", "Up to 2 years", "Varies", "Employer sponsorship, degree/experience, medical exam, police clearance"),
            ("Work", "Expert Visa", "Up to 2 years", "Varies", "Expert certificate, employer sponsorship"),
            ("Student", "Student Visa (DH)", "Duration of course", "Varies", "Acceptance from Vietnamese institution, sponsor"),
            ("Family", "Family Visa (TT)", "Up to 5 years", "Varies", "Spouse/child of Vietnamese citizen or foreigner with work permit"),
            ("Investor", "Investor Visa (DT)", "Up to 5 years", "Varies", "Investment in Vietnamese company, business registration certificate"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
            ("Transit", "Transit (no visa needed)", "N/A", "Free", "Transit through Vietnamese airports without leaving airside"),
        ],
        "processing_times": [
            ("e-Visa", "3 business days", "1 business day (rush)", "USD 10 surcharge"),
            ("Visa on Arrival (approval letter)", "1-3 business days", "4-8 hours (urgent)", "USD 10-20 surcharge"),
            ("Embassy Visa", "5-7 business days", "1-2 business days", "Varies"),
            ("Work Permit", "5-7 business days (after documents ready)", "N/A", "N/A"),
            ("Business Visa", "5-10 business days", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for work permit applicants. Must be performed at a Vietnamese government-designated hospital.</li>
<li><strong>Vaccinations:</strong> Yellow Fever certificate required if arriving from endemic area. No other mandatory vaccinations.</li>
<li><strong>Health insurance:</strong> Not mandatory for tourists but recommended. Required for work permit and temporary residence card holders.</li>
<li><strong>Police clearance:</strong> Required for work permit applications — from home country, apostilled and translated into Vietnamese.</li>
<li><strong>Biometrics:</strong> Fingerprints and photo may be collected at immigration checkpoints.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>e-Visa (90 days):</strong> Cannot be extended. Must exit and obtain a new e-Visa.</li>
<li><strong>Visa-free entry:</strong> Cannot be extended. Must exit Vietnam for at least 30 days before re-entering visa-free (for most nationalities).</li>
<li><strong>Tourist/business visa:</strong> Can be extended through a Vietnamese travel agency or immigration office. Extensions in 30-day increments. Cost: USD 50-100 per extension.</li>
<li><strong>Work permit / TRC:</strong> Renewable through employer.</li>
<li><strong>Overstay:</strong> Fine of USD 25 per day (approximately). Deportation and entry ban possible for serious overstays.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Incorrect passport details on application, previously blacklisted, security concerns, incomplete documents.</li>
<li><strong>Appeal:</strong> No formal appeal process. Reapply with corrected information.</li>
<li><strong>Reapplication:</strong> Can reapply immediately. Ensure all details match passport exactly.</li>
</ul>""",
        "extra_faqs": [
            ("How long can I stay in Vietnam with an e-Visa?", "Vietnam's e-Visa allows a stay of up to 90 days with single or multiple entry. The e-Visa costs USD 25 and is processed within 3 business days. Apply at evisa.xuatnhapcanh.gov.vn."),
            ("Do EU citizens need a visa for Vietnam?", "EU citizens can enter Vietnam visa-free for up to 45 days (single entry). For longer stays or multiple entries, an e-Visa (USD 25, up to 90 days) is required."),
            ("Can I extend my Vietnam visa?", "Tourist and business visas can be extended through a travel agency or immigration office in 30-day increments. E-Visas and visa-free entries cannot be extended — you must exit and re-enter with a new visa."),
        ],
    },
    "china": {
        "file": "china-visa-requirements.html",
        "name": "China",
        "flag": "cn",
        "visa_types": [
            ("Tourist", "L Visa (Tourist)", "30-90 days, single/double/multiple", "USD 140 (US) / varies by nationality", "Invitation letter or hotel bookings, itinerary, financial proof"),
            ("Tourist", "Visa-Free Transit (TWOV)", "24-144 hours", "Free", "Transit through designated cities, onward ticket to third country"),
            ("Tourist", "Visa-Free Entry (Bilateral)", "15-30 days", "Free", "Selected countries with visa-free agreements (expanding in 2024-2025)"),
            ("Business", "M Visa (Business/Trade)", "30-90 days", "USD 140 (US)", "Invitation from Chinese business, company documents"),
            ("Work", "Z Visa (Work)", "30 days (entry), then Work Permit", "USD 140 (US)", "Work permit notification letter, employer sponsorship, medical exam"),
            ("Work", "R Visa (High-Level Talent)", "Up to 5 years", "USD 140 (US)", "Recognized high-level talent or urgently needed specialist"),
            ("Student", "X1 Visa (Long-term Study)", "Over 180 days", "USD 140 (US)", "JW201/JW202 form, admission notice from Chinese institution"),
            ("Student", "X2 Visa (Short-term Study)", "Under 180 days", "USD 140 (US)", "Admission notice from Chinese institution"),
            ("Family", "Q1 Visa (Long-term Family Reunion)", "Over 180 days", "USD 140 (US)", "Invitation from Chinese citizen/PR family member, relationship proof"),
            ("Family", "Q2 Visa (Short-term Family Visit)", "Under 180 days", "USD 140 (US)", "Invitation from Chinese citizen/PR family member"),
            ("Family", "S1/S2 Visa (Dependent of Foreigner)", "S1: over 180 days / S2: under 180 days", "USD 140 (US)", "Spouse/parent/child of foreigner working/studying in China"),
            ("Journalist", "J1/J2 Visa (Journalist)", "J1: resident / J2: temporary", "USD 140 (US)", "Approval from Chinese authorities, media organization letter"),
            ("Transit", "G Visa (Transit)", "Duration of transit", "USD 140 (US)", "Confirmed onward ticket, transit through China"),
            ("Crew", "C Visa (Crew)", "As needed", "USD 140 (US)", "Airline/shipping company employment"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport, government note verbale"),
        ],
        "processing_times": [
            ("L Visa (Tourist)", "4 business days (regular)", "2-3 business days (express)", "USD 20 (express) / USD 30 (rush)"),
            ("M Visa (Business)", "4 business days", "2-3 business days", "USD 20 (express)"),
            ("Z Visa (Work)", "4-10 business days", "2-3 business days", "USD 20 (express)"),
            ("X1/X2 Visa (Student)", "4 business days", "2-3 business days", "USD 20 (express)"),
            ("Visa-Free Transit (TWOV)", "Instant (on arrival)", "N/A", "N/A"),
            ("Work Permit (after arrival)", "15-30 business days", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for Z Visa (work) and X1 Visa (long-term study). Physical Examination Record for Foreigner form must be completed at an approved hospital. Includes blood tests, chest X-ray, ECG, and general exam. The exam done abroad must be re-verified at a local Entry-Exit Inspection and Quarantine Bureau within 30 days of arrival.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry. Yellow Fever certificate required if arriving from endemic area.</li>
<li><strong>Health insurance:</strong> Not mandatory but recommended. Health insurance is required by many Chinese universities for international students.</li>
<li><strong>Police clearance:</strong> Required for work permit applications — from home country, notarized and authenticated by Chinese embassy.</li>
<li><strong>Biometrics:</strong> Fingerprints collected at the Chinese Visa Application Service Center for applicants aged 14-70.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>L Visa (Tourist):</strong> Can be extended once at the local Public Security Bureau (PSB) Exit-Entry Administration. Fee: CNY 160. Apply at least 7 days before expiry. Extension usually 30 days.</li>
<li><strong>Visa-Free Transit:</strong> Cannot be extended. Must depart within the permitted hours.</li>
<li><strong>Z Visa / Work Permit:</strong> Work permit renewable annually. Residence permit renewable through employer at PSB.</li>
<li><strong>X1 Visa (Student):</strong> Must apply for a Residence Permit within 30 days of arrival at the local PSB. Renewable annually with enrollment proof.</li>
<li><strong>Temporary Registration:</strong> All foreigners must register with the local police station within 24 hours of arrival (hotel guests are automatically registered by the hotel).</li>
<li><strong>Overstay:</strong> Fine of CNY 500 per day (max CNY 10,000). Detention of 5-15 days possible. Serious overstays result in deportation and 1-5 year re-entry bans.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Incomplete documents, previous Chinese visa violations, security concerns, nationality restrictions, inconsistent information, journalist or NGO connections without proper authorization.</li>
<li><strong>Appeal:</strong> No formal appeal process. Applicants can request reconsideration at the Chinese embassy/consulate with additional documentation.</li>
<li><strong>Reapplication:</strong> Can reapply immediately with improved documentation and additional supporting evidence.</li>
<li><strong>Tip:</strong> China's visa policies can change rapidly. Always check with the nearest Chinese embassy or visa application center for the latest requirements.</li>
</ul>""",
        "extra_faqs": [
            ("What is China's 144-hour visa-free transit?", "China offers 144-hour (6-day) visa-free transit for citizens of 54 countries transiting through designated cities including Beijing, Shanghai, Guangzhou, Chengdu, and others. You must have a confirmed onward ticket to a third country (not the country you arrived from) and stay within the permitted area."),
            ("How much does a Chinese visa cost?", "Fees vary by nationality. US citizens pay USD 140 for all visa types. Citizens of most other countries pay USD 30-80. Express processing costs an additional USD 20, and rush processing USD 30. Check with your nearest Chinese Visa Application Service Center."),
            ("Do I need a visa for China in 2026?", "It depends on your nationality and purpose. China has expanded visa-free agreements with many countries for stays of 15-30 days. Citizens of 54 countries can transit visa-free for up to 144 hours. For longer stays, most nationalities need a visa. Check the latest policies as they are frequently updated."),
            ("What is the temporary registration requirement in China?", "All foreigners must register with the local police station within 24 hours of arrival at each city (within 72 hours in rural areas). Hotels handle this automatically. If staying at a private residence, you must register in person at the nearest police station with your passport and the host's ID."),
        ],
    },
    "south-korea": {
        "file": "visa-south-korea.html",
        "name": "South Korea",
        "flag": "kr",
        "visa_types": [
            ("Tourist", "K-ETA (Korea Electronic Travel Authorization)", "Up to 90 days", "KRW 10,000 (~USD 8)", "112 eligible countries, online at k-eta.go.kr (currently suspended for some nationalities)"),
            ("Tourist", "Visa-Free Entry", "30-90 days (nationality dependent)", "Free", "US, EU, Japan, Australia, etc. — currently 90 days visa-free for many countries"),
            ("Tourist", "Tourist Visa (C-3-9)", "90 days", "USD 40 (single) / USD 70 (multiple)", "Embassy application, itinerary, financial proof"),
            ("Business", "Short-term Business (C-3-4)", "90 days", "USD 40", "Business invitation from Korean company, company registration"),
            ("Work", "E-7 (Specially Designated Activities)", "Up to 3 years", "USD 60", "Job offer in specialized field, employer sponsorship, qualifications"),
            ("Work", "E-1 to E-5 (Professional)", "1-3 years", "USD 60", "University professor, language instructor, researcher, technical specialist"),
            ("Work", "E-9 (Non-Professional Employment)", "Up to 3 years", "USD 60", "EPS (Employment Permit System), bilateral agreement countries, manufacturing/agriculture"),
            ("Work", "H-1 (Working Holiday)", "1 year", "Free or USD 40", "Age 18-30, bilateral agreement country, limited work permitted"),
            ("Work", "D-8 (Investor)", "2-5 years", "USD 60", "Investment of KRW 100M+ (~USD 75,000) in Korean business"),
            ("Student", "D-2 (Student)", "Duration of course", "USD 60", "Acceptance from Korean institution, financial proof (KRW 20M in bank), study plan"),
            ("Student", "D-4 (Language Training)", "Up to 2 years", "USD 60", "Korean language institute enrollment, financial proof"),
            ("Family", "F-6 (Spouse of Korean National)", "Up to 3 years", "USD 60", "Marriage to Korean citizen, proof of genuine relationship, basic Korean ability"),
            ("Family", "F-1 (Family Visit)", "90 days", "USD 60", "Visiting family in Korea, relationship proof"),
            ("Family", "F-4 (Overseas Korean)", "Up to 3 years", "USD 60", "Ethnic Korean with foreign citizenship (certain conditions)"),
            ("Long-term", "F-5 (Permanent Residence)", "Indefinite", "USD 60", "5+ years residence, income threshold, Korean language ability, or investment KRW 500M+"),
            ("Transit", "Transit (no visa)", "N/A", "Free", "Airside transit without leaving airport — no visa needed"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("K-ETA", "Instant to 72 hours", "N/A", "N/A"),
            ("Visa-Free Entry", "Instant", "N/A", "N/A"),
            ("Tourist Visa (C-3-9)", "5-10 business days", "3 business days (some embassies)", "Varies"),
            ("E-7 Work Visa", "2-4 weeks", "N/A", "N/A"),
            ("D-2 Student Visa", "2-4 weeks", "N/A", "N/A"),
            ("F-6 Spouse Visa", "1-3 months", "N/A", "N/A"),
            ("F-5 Permanent Residence", "3-6 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for E-type (work) visa holders after arrival — conducted at designated hospitals. Includes HIV, drug screening, chest X-ray, and general health assessment.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry.</li>
<li><strong>Health insurance:</strong> National Health Insurance (NHI) enrollment mandatory for all visa holders staying 6+ months (since 2021).</li>
<li><strong>COVID-19:</strong> No vaccination or testing requirements as of 2026. Q-CODE registration recommended for expedited entry.</li>
<li><strong>Police clearance:</strong> Not routinely required for visa applications. May be requested for certain employment or residence categories.</li>
<li><strong>Biometrics:</strong> Fingerprints and photo collected at immigration for all foreign nationals aged 17+.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Visa-free / K-ETA:</strong> Cannot be extended. Must leave before the 90-day limit.</li>
<li><strong>Tourist visa (C-3):</strong> Generally not extendable. Apply for a different visa status if needing to stay longer.</li>
<li><strong>Work visas (E-type):</strong> Renewable at the local Immigration Office before expiry. Must maintain qualifying employment.</li>
<li><strong>Student visa (D-2):</strong> Renewable with continued enrollment and adequate academic performance.</li>
<li><strong>Status change:</strong> Possible within Korea at the Immigration Office (e.g., D-2 student to E-7 work).</li>
<li><strong>Overstay:</strong> Fines, detention, deportation, and re-entry ban of 1-10 years. Voluntary departure reporting may reduce penalties.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient financial evidence, weak ties to home country, previous Korean visa violations, criminal record, suspected intent to overstay or work illegally.</li>
<li><strong>Appeal:</strong> No formal appeal for tourist/short-stay visa refusals. Work and residence visa refusals can be reconsidered with additional documentation or through employer intervention.</li>
<li><strong>Reapplication:</strong> Can reapply after 6 months for C-3 visa refusals (some embassies). Other visa types may allow earlier reapplication.</li>
</ul>""",
        "extra_faqs": [
            ("What is K-ETA for South Korea?", "K-ETA (Korea Electronic Travel Authorization) is an online travel authorization for visa-exempt nationals. It costs KRW 10,000 and is valid for 2 years allowing multiple entries of up to 90 days. As of 2024-2025, K-ETA requirements have been temporarily suspended for many nationalities — check k-eta.go.kr for current status."),
            ("How long can I stay in South Korea without a visa?", "Most Western nationals (US, UK, EU, Australia, Canada, etc.) can stay in South Korea visa-free for up to 90 days for tourism. ASEAN nationals typically receive 30 days. Japanese nationals receive 90 days. Always verify with the Korean embassy for your specific nationality."),
            ("Can I work in South Korea on a tourist visa?", "No. Working on a tourist visa or visa-free entry is illegal in South Korea. You need an appropriate work visa (E-1 through E-7, E-9, or H-1 Working Holiday). Penalties for illegal work include fines, deportation, and re-entry bans."),
            ("How do I get permanent residence (F-5) in South Korea?", "F-5 permanent residence requires 5+ years of continuous legal residence, meeting income thresholds, Korean language ability (TOPIK Level 5+), and knowledge of Korean culture. Investors can qualify with KRW 500M+ investment. Marriage visa (F-6) holders can apply after 2 years of marriage and legal residence."),
        ],
    },
    "new-zealand": {
        "file": "new-zealand-visa-requirements.html",
        "name": "New Zealand",
        "flag": "nz",
        "visa_types": [
            ("Tourist", "NZeTA (Electronic Travel Authority)", "Up to 90 days per visit", "NZD 17 (app) / NZD 23 (online) + NZD 35 IVL", "Visa-waiver countries (US, UK, EU, etc.), online at immigration.govt.nz"),
            ("Tourist", "Visitor Visa", "Up to 9 months (varies)", "NZD 246", "All nationalities, financial evidence, genuine visitor intent"),
            ("Tourist", "Visa-Free (Australian citizens)", "Indefinite", "Free", "Australian citizens — automatic right to live and work"),
            ("Business", "Business Visitor Visa", "Up to 3 months", "NZD 246", "Business meetings, conferences, no employment"),
            ("Work", "Accredited Employer Work Visa (AEWV)", "Up to 3 years", "NZD 750", "Job offer from accredited employer, median wage or above, job check"),
            ("Work", "Working Holiday Visa", "12-23 months", "NZD 455", "Age 18-30 (35 for some countries), bilateral agreement country"),
            ("Work", "Post-Study Work Visa", "1-3 years", "NZD 700", "Completed eligible NZ qualification, applied within 3 months of study visa expiry"),
            ("Work", "Essential Skills Work Visa", "Up to 5 years", "NZD 750", "Job offer in skill-shortage area, employer support"),
            ("Work", "Skilled Migrant Category (SMC)", "Permanent Residence", "NZD 580 (EOI) + NZD 3,310 (PR)", "Points-based (160+ points), skilled employment, age under 56"),
            ("Student", "Student Visa", "Duration of course", "NZD 375", "Offer of place from NZ institution, financial proof (NZD 20,000/year), NZQA approved"),
            ("Family", "Partnership Visa", "Temporary or Permanent", "NZD 760 (temp) / NZD 1,840 (residence)", "Genuine and stable relationship with NZ citizen/resident (12+ months cohabitation)"),
            ("Family", "Parent Visa (Resident)", "Permanent", "NZD 3,310", "Sponsored by adult child in NZ, income requirements, expression of interest"),
            ("Investor", "Investor Visa (Category 1)", "Permanent", "NZD 3,310", "NZD 15M investment for 3 years, no English/age requirements"),
            ("Investor", "Investor Visa (Category 2)", "Permanent", "NZD 3,310", "NZD 3M investment for 4 years, age under 65, English (IELTS 3+), 3 years business experience"),
            ("Transit", "Transit Visa", "24 hours", "Free", "Transit through Auckland, confirmed onward flight"),
            ("Diplomatic", "Diplomatic / Official", "Duration of posting", "Free", "Diplomatic passport"),
        ],
        "processing_times": [
            ("NZeTA", "Usually instant (up to 72 hours)", "N/A", "N/A"),
            ("Visitor Visa", "20-25 business days", "N/A", "N/A"),
            ("AEWV (Work Visa)", "20-30 business days", "N/A", "N/A"),
            ("Student Visa", "20-25 business days", "N/A", "N/A"),
            ("Working Holiday", "10-20 business days", "N/A", "N/A"),
            ("Partnership Visa", "6-12 months", "N/A", "N/A"),
            ("SMC (Permanent)", "6-12 months", "N/A", "N/A"),
            ("Investor Category 2", "6-12 months", "N/A", "N/A"),
        ],
        "health_requirements": """<ul>
<li><strong>Medical exam:</strong> Required for visas with potential stays of 6+ months, or if from a high-risk TB country for any duration. Includes chest X-ray and general medical certificate. Must be performed by a panel physician approved by Immigration New Zealand.</li>
<li><strong>Vaccinations:</strong> No mandatory vaccinations for entry. Recommended: routine vaccines, Hepatitis A/B, Influenza.</li>
<li><strong>Health insurance:</strong> Not mandatory for visitors but strongly recommended. International students must have compliant medical and travel insurance.</li>
<li><strong>Police clearance:</strong> Required for visitors staying 24+ months and for all work and residence visa applicants. Police certificate from every country lived in for 5+ years since age 17.</li>
<li><strong>Biometrics:</strong> Required for some visa applicants — collected at a Visa Application Centre.</li>
<li><strong>IVL (International Visitor Conservation and Tourism Levy):</strong> NZD 35 payable by most visitors as part of NZeTA or visa application. Funds conservation and tourism infrastructure.</li>
</ul>""",
        "extension_info": """<ul>
<li><strong>Visitor visa:</strong> Can be extended within New Zealand but total stay cannot exceed 9 months in any 18-month period (or 18 months in any 36-month period if visitor cap waived). Apply online through Immigration NZ.</li>
<li><strong>Work visa (AEWV):</strong> Renewable with continued accredited employment. Apply before current visa expires.</li>
<li><strong>Student visa:</strong> Renewable with continued enrollment. Apply online or at an INZ branch.</li>
<li><strong>Working Holiday:</strong> Cannot be extended beyond the initial period. Some nationalities can apply for a second Working Holiday after completing seasonal work.</li>
<li><strong>Interim visa:</strong> Granted automatically if you apply for a new visa before your current one expires. Allows continued lawful stay.</li>
<li><strong>Overstay:</strong> Deportation and re-entry ban. Section 157 deportation liability for those who overstay or breach visa conditions.</li>
</ul>""",
        "refusal_info": """<ul>
<li><strong>Common refusal reasons:</strong> Insufficient evidence of genuine visit intent, inadequate financial proof, health or character concerns, previous immigration issues in NZ or other countries, incomplete documentation.</li>
<li><strong>Appeal:</strong> Most visa refusals can be appealed to the Immigration and Protection Tribunal (IPT) within 42 days. Some decisions (e.g., temporary visa refusals offshore) may have limited appeal rights.</li>
<li><strong>Reconsideration:</strong> Applicants can request reconsideration by the decision-maker with new information before lodging a formal appeal.</li>
<li><strong>Reapplication:</strong> Can reapply at any time with improved documentation addressing the refusal reasons.</li>
</ul>""",
        "extra_faqs": [
            ("What is the NZeTA for New Zealand?", "The NZeTA (New Zealand Electronic Travel Authority) is required for visa-waiver nationals (US, UK, EU, etc.) and transit passengers. It costs NZD 17 via the app or NZD 23 online, plus a NZD 35 International Visitor Conservation and Tourism Levy (IVL). It is valid for 2 years and allows multiple entries of up to 90 days."),
            ("Can I work in New Zealand on a visitor visa?", "No. Visitor visas do not permit work. To work in New Zealand, you need an Accredited Employer Work Visa (AEWV), Working Holiday Visa, or other work-class visa. Students on a student visa can work up to 20 hours per week during term."),
            ("How do I get permanent residence in New Zealand?", "The main pathway is the Skilled Migrant Category (SMC), a points-based system requiring 160+ points based on age, qualifications, skilled employment in NZ, and partner qualifications. Other routes include investor visas, partnership visas, and parent visas."),
            ("What is the IVL levy for New Zealand?", "The International Visitor Conservation and Tourism Levy (IVL) is a NZD 35 fee charged to most visitors. It funds conservation projects and tourism infrastructure in New Zealand. It is collected as part of the NZeTA or visa application process. Australian citizens and some visa categories are exempt."),
        ],
    },
}


# ---------------------------------------------------------------------------
# HTML generators
# ---------------------------------------------------------------------------

def build_visa_types_table(rows):
    """Build the Complete Visa Categories table."""
    lines = [
        '<h2 id="all-visas">Complete Visa Categories</h2>',
        '<div class="table-responsive"><table class="table table-bordered table-sm">',
        '<thead class="table-dark"><tr><th>Category</th><th>Visa Type</th><th>Duration</th><th>Fee</th><th>Key Requirements</th></tr></thead>',
        '<tbody>',
    ]
    for cat, vtype, dur, fee, reqs in rows:
        lines.append(f'<tr><td>{cat}</td><td>{vtype}</td><td>{dur}</td><td>{fee}</td><td>{reqs}</td></tr>')
    lines.append('</tbody></table></div>')
    return "\n".join(lines)


def build_processing_table(rows):
    """Build the Processing Times table."""
    lines = [
        '<h2 id="processing">Processing Times by Visa Type</h2>',
        '<div class="table-responsive"><table class="table table-bordered table-sm">',
        '<thead class="table-dark"><tr><th>Visa Type</th><th>Standard Processing</th><th>Expedited Processing</th><th>Expedited Cost</th></tr></thead>',
        '<tbody>',
    ]
    for vtype, std, exp, cost in rows:
        lines.append(f'<tr><td>{vtype}</td><td>{std}</td><td>{exp}</td><td>{cost}</td></tr>')
    lines.append('</tbody></table></div>')
    return "\n".join(lines)


def build_health_section(html_content):
    return f'<h2 id="health-requirements">Health &amp; Character Requirements</h2>\n{html_content}'


def build_extension_section(html_content):
    return f'<h2 id="extension">Visa Extension &amp; Renewal</h2>\n{html_content}'


def build_refusal_section(html_content):
    return f'<h2 id="refusal">Visa Refusal &amp; Appeals</h2>\n{html_content}'


def build_extra_faq_json(existing_faq_json, extra_faqs):
    """Merge extra FAQs into existing FAQ JSON-LD, avoiding duplicates."""
    try:
        faq_data = json.loads(existing_faq_json)
    except Exception:
        faq_data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": []}

    existing_names = {q.get("name", "").lower().strip() for q in faq_data.get("mainEntity", [])}

    for q, a in extra_faqs:
        if q.lower().strip() not in existing_names:
            faq_data["mainEntity"].append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })
    return json.dumps(faq_data, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Main enrichment logic
# ---------------------------------------------------------------------------

SECTION_IDS = ["all-visas", "processing", "health-requirements", "extension", "refusal"]


def enrich_file(country_key, data):
    filepath = os.path.join(BASE_DIR, data["file"])
    if not os.path.isfile(filepath):
        print(f"  [SKIP] File not found: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # --- Check which sections already exist ---
    existing_ids = set()
    for sid in SECTION_IDS:
        if f'id="{sid}"' in content:
            existing_ids.add(sid)

    if len(existing_ids) == len(SECTION_IDS):
        # Check if FAQs were already enriched by seeing if any of the extra FAQ questions are present
        all_faqs_present = True
        for q, _ in data.get("extra_faqs", []):
            if q not in content:
                all_faqs_present = False
                break
        if all_faqs_present:
            print(f"  [SKIP] All sections already exist for {data['name']}")
            return False

    # --- Build new sections HTML ---
    new_sections = []

    if "all-visas" not in existing_ids:
        new_sections.append(build_visa_types_table(data["visa_types"]))
    if "processing" not in existing_ids:
        new_sections.append(build_processing_table(data["processing_times"]))
    if "health-requirements" not in existing_ids:
        new_sections.append(build_health_section(data["health_requirements"]))
    if "extension" not in existing_ids:
        new_sections.append(build_extension_section(data["extension_info"]))
    if "refusal" not in existing_ids:
        new_sections.append(build_refusal_section(data["refusal_info"]))

    if not new_sections and not data.get("extra_faqs"):
        print(f"  [SKIP] Nothing to add for {data['name']}")
        return False

    injection_html = "\n\n".join(new_sections)

    # --- Find insertion point ---
    # Strategy: insert before the editorial note div
    insertion_marker = '<div class="alert alert-info small mt-4">'
    if insertion_marker not in content:
        # Fallback: insert before Related Guides
        insertion_marker = '<div class="mt-4 pt-3 border-top">'
    if insertion_marker not in content:
        # Fallback: insert before </article>
        insertion_marker = '</article>'

    if insertion_marker in content:
        idx = content.index(insertion_marker)
        content = content[:idx] + "\n" + injection_html + "\n\n" + content[idx:]
    else:
        print(f"  [WARN] Could not find insertion point for {data['name']}")
        return False

    # --- Enrich FAQ JSON-LD ---
    if data.get("extra_faqs"):
        faq_pattern = re.compile(
            r'(<script type="application/ld\+json">\s*\{[^<]*?"@type"\s*:\s*"FAQPage"[^<]*?</script>)',
            re.DOTALL
        )
        match = faq_pattern.search(content)
        if match:
            old_block = match.group(1)
            # Extract the JSON
            json_start = old_block.index("{")
            json_end = old_block.rindex("}") + 1
            old_json = old_block[json_start:json_end]
            new_json = build_extra_faq_json(old_json, data["extra_faqs"])
            new_block = '<script type="application/ld+json">\n    ' + new_json + '\n    </script>'
            content = content.replace(old_block, new_block)
        else:
            # No existing FAQ block — inject one before the footer
            faq_entries = []
            for q, a in data["extra_faqs"]:
                faq_entries.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
            faq_obj = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_entries}
            faq_script = '<script type="application/ld+json">\n    ' + json.dumps(faq_obj, ensure_ascii=False) + '\n    </script>\n'
            footer_marker = '<footer '
            if footer_marker in content:
                fidx = content.index(footer_marker)
                content = content[:fidx] + faq_script + content[fidx:]

    # --- Write back ---
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    sections_added = len(new_sections)
    faqs_added = len(data.get("extra_faqs", []))
    print(f"  [OK] {data['name']}: {sections_added} sections injected, {faqs_added} FAQs merged")
    return True


def main():
    print("=" * 60)
    print("Deep Enrichment — Group 1 (Top 20 Countries)")
    print("=" * 60)
    total = 0
    enriched = 0
    for key, data in COUNTRIES.items():
        total += 1
        print(f"\n[{total}/{len(COUNTRIES)}] Processing {data['name']}...")
        if enrich_file(key, data):
            enriched += 1

    print(f"\n{'=' * 60}")
    print(f"Done. {enriched}/{total} files enriched.")
    print("=" * 60)


if __name__ == "__main__":
    main()
