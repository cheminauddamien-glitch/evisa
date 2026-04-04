#!/usr/bin/env python3
"""
gen_subpages_batch_d.py
Generates 3 sub-pages per country for 10 Pacific/Asia countries:
  {country}-visa-requirements.html
  {country}-visa-fees.html
  {country}-visa-processing-time.html
Output directory: www/en/
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Country data
# ---------------------------------------------------------------------------
COUNTRIES = {
    "china": {
        "name": "China",
        "flag": "cn",
        "evisa_url": "evisa.mfa.gov.cn",
        "evisa_cost": "FREE (since 2023)",
        "stay": "30 days single entry",
        "processing": "4–5 business days",
        "standard_fee": "USD 140 (standard visa)",
        "extra": "72h / 144h TWOV (Transit Without Visa) available",
        # --- requirements page ---
        "req_title": "China Visa Requirements 2026 — eVisa, Documents & Eligibility Checklist",
        "req_desc": "Complete China visa requirements for 2026: eVisa documents, eligibility rules, passport validity and official evisa.mfa.gov.cn application guide.",
        "req_h1": "China Visa Requirements 2026 — eVisa, Documents &amp; Eligibility Checklist",
        "req_table": [
            ("eVisa fee", "FREE — available at evisa.mfa.gov.cn since 2023"),
            ("Standard visa fee", "USD 140 (consulate application)"),
            ("Stay allowed", "30 days, single entry"),
            ("TWOV policy", "72h or 144h transit without visa in eligible cities"),
            ("Passport validity", "At least 6 months beyond intended stay"),
            ("Photo requirement", "48×33mm, white background, taken within 6 months"),
            ("Biometrics", "Required at consulate for standard visa"),
        ],
        "req_sections": [
            ("Overview of China Entry Requirements 2026",
             """China opened its free eVisa programme in 2023, allowing nationals of many countries to apply online at <strong>evisa.mfa.gov.cn</strong> without visiting a consulate. The eVisa grants a 30-day single-entry stay and is valid for tourism, business, transit and family visits. Travellers not eligible for the eVisa must apply at a Chinese embassy or consulate and pay the standard USD 140 fee. China also maintains a Transit Without Visa (TWOV) policy: 72 hours for most eligible transit cities and 144 hours for Beijing, Shanghai, Guangzhou and other major hubs, provided you hold an onward ticket to a third country. Confirm TWOV eligibility by nationality before travel, as not all passports qualify."""),
            ("Documents Checklist for China eVisa 2026",
             """<ul>
<li>Valid passport — minimum 6 months validity beyond planned departure from China</li>
<li>Digital passport-style photo — 48×33mm, white background, taken within 6 months</li>
<li>Completed online application at evisa.mfa.gov.cn</li>
<li>Round-trip flight itinerary or onward travel proof</li>
<li>Confirmed hotel booking or invitation letter from a Chinese host</li>
<li>Travel insurance covering the full stay (recommended)</li>
<li>Bank statements showing sufficient funds (consulate applications)</li>
</ul>"""),
            ("Eligibility &amp; Special Categories",
             """The free eVisa is available to citizens of eligible countries listed on evisa.mfa.gov.cn. Business travellers may need additional documents such as a company invitation letter or conference registration. Journalists, diplomats and students require special visa categories (J, D, X). Children travelling on a parent's passport require their own travel document. Always verify current eligibility at the official portal before applying, as the list of eligible nationalities is updated periodically."""),
            ("How to Apply for a China eVisa",
             """Visit <strong>evisa.mfa.gov.cn</strong>, create an account and select the appropriate visa type (L for tourism, M for business, etc.). Upload a passport scan, digital photo and supporting documents. The system guides you through the form in English. Once submitted, processing takes 4–5 business days. You will receive an approval letter by email to print and present on arrival alongside your passport. No embassy visit is required for eVisa applicants."""),
        ],
        # --- fees page ---
        "fees_title": "China Visa Fees 2026 — eVisa Cost, Standard Visa Charges & Payment Guide",
        "fees_desc": "Full breakdown of China visa fees in 2026: free eVisa, USD 140 standard visa, service charges, payment methods and refund rules explained.",
        "fees_h1": "China Visa Fees 2026 — eVisa Cost, Standard Visa &amp; All Charges Explained",
        "fees_table": [
            ("eVisa (evisa.mfa.gov.cn)", "FREE"),
            ("Single-entry standard visa", "USD 140"),
            ("Double-entry standard visa", "USD 140"),
            ("Multiple-entry 6-month visa", "USD 140"),
            ("Multiple-entry 1-year visa", "USD 140"),
            ("Transit visa (X days)", "USD 140"),
            ("Consulate service fee (third-party)", "Varies by country"),
        ],
        "fees_sections": [
            ("China eVisa — Free of Charge Since 2023",
             """One of the most significant changes in Chinese travel policy is the introduction of a completely <strong>free eVisa</strong> for eligible nationalities through evisa.mfa.gov.cn. There are no application fees, no service charges and no hidden costs when applying directly through the official portal. This replaces the old visa-on-arrival system for many countries and makes China far more accessible for short-stay tourists and business visitors."""),
            ("Standard Visa Fees at the Chinese Consulate",
             """Travellers who are not eligible for the free eVisa, or who need a visa category not available online (such as a student X1/X2 visa, journalist J visa, or work Z visa), must apply at a Chinese embassy or consulate. The standard fee is <strong>USD 140</strong> regardless of visa type or number of entries. Some countries have reciprocal fee agreements that may alter this rate. Always check the fee schedule at the nearest Chinese diplomatic mission."""),
            ("Additional Costs &amp; Payment Methods",
             """Third-party visa agencies charge service fees on top of the official consulate fee, typically USD 20–80. The official eVisa portal accepts major credit and debit cards. Consulate payments vary by location — some accept bank drafts, cash or card. Fees are generally non-refundable once the application is submitted, even if the visa is denied. Travel insurance is not mandatory but strongly recommended."""),
            ("Reciprocal Fee Arrangements",
             """China operates a reciprocal visa fee policy with some countries, meaning citizens of those countries pay the same fee that Chinese nationals pay for a visa to that country. This can result in different fees for applicants from countries such as the United States or Canada. Check the fee calculator on your nearest Chinese consulate website for accurate figures before applying."""),
        ],
        # --- processing page ---
        "proc_title": "China Visa Processing Time 2026 — eVisa & Consulate Timelines Explained",
        "proc_desc": "China visa processing time in 2026: 4–5 days for eVisa, consulate timelines, express options and tips to avoid delays. Official evisa.mfa.gov.cn guide.",
        "proc_h1": "China Visa Processing Time 2026 — eVisa, Standard &amp; Express Timelines",
        "proc_table": [
            ("eVisa (evisa.mfa.gov.cn)", "4–5 business days"),
            ("Consulate standard", "4–5 business days"),
            ("Consulate express", "2–3 business days (extra fee may apply)"),
            ("Consulate urgent", "1–2 business days (extra fee may apply)"),
            ("TWOV (72h)", "No visa required — passport eligibility check only"),
            ("TWOV (144h)", "No visa required — eligibility check + port of entry"),
            ("Work/Student visa", "2–8 weeks (varies by consulate)"),
        ],
        "proc_sections": [
            ("China eVisa Processing Time 2026",
             """Applications submitted through <strong>evisa.mfa.gov.cn</strong> are typically processed within <strong>4–5 business days</strong>. The system sends an email notification when the decision is made. During Chinese public holidays (e.g. Chinese New Year, National Day Golden Week) processing may take longer. Apply at least 2 weeks before your planned travel date to allow for any delays or requests for additional documentation."""),
            ("Consulate Processing Timelines",
             """Standard consulate processing takes 4–5 business days after all documents are submitted. Many consulates offer an express service (2–3 days) and an urgent service (1–2 days) for an additional surcharge. Processing times can vary significantly by consulate location and current workload. Some consulates in high-demand countries may have appointment waiting times of 2–4 weeks, so factor this in when planning."""),
            ("Factors That Can Delay Processing",
             """<ul>
<li>Incomplete or incorrectly filled application forms</li>
<li>Missing supporting documents (e.g., no hotel booking, insufficient financial evidence)</li>
<li>Photo not meeting the 48×33mm white-background specification</li>
<li>Travel during Chinese public holidays</li>
<li>Background checks for applicants from certain nationalities</li>
<li>Additional security screening for certain professions</li>
</ul>"""),
            ("Tips for Faster China Visa Approval",
             """Apply via the free eVisa portal (evisa.mfa.gov.cn) if your nationality is eligible — it is faster and cheaper than consulate applications. Submit a complete set of documents on first application to avoid back-and-forth requests. Book refundable flights and hotels before applying to show genuine travel intent. Track your application status through the official portal. If you need a visa urgently, contact the consulate directly to enquire about expedited options."""),
        ],
    },

    "malaysia": {
        "name": "Malaysia",
        "flag": "my",
        "evisa_url": "evisa.imi.gov.my",
        "evisa_cost": "USD 20",
        "stay": "30 days",
        "processing": "1–3 days",
        "standard_fee": "90 days visa-free for 60+ nationalities",
        "extra": "eVisa available at evisa.imi.gov.my",
        "req_title": "Malaysia Visa Requirements 2026 — eVisa, Visa-Free & Documents Checklist",
        "req_desc": "Malaysia visa requirements 2026: 90-day visa-free for 60+ nationalities, USD 20 eVisa, documents checklist and official evisa.imi.gov.my application guide.",
        "req_h1": "Malaysia Visa Requirements 2026 — eVisa, Visa-Free Entry &amp; Documents Checklist",
        "req_table": [
            ("Visa-free stay", "90 days for 60+ nationalities (no fee)"),
            ("eVisa fee", "USD 20 — via evisa.imi.gov.my"),
            ("eVisa stay", "30 days single entry"),
            ("eVisa processing", "1–3 business days"),
            ("Passport validity", "Minimum 6 months beyond departure"),
            ("Photo requirement", "35×50mm, white background, recent"),
            ("Entry points", "All international airports and major land crossings"),
        ],
        "req_sections": [
            ("Overview of Malaysia Entry Requirements 2026",
             """Malaysia offers <strong>90 days visa-free entry</strong> for citizens of more than 60 countries, including most European nations, the USA, Australia, Canada and many Asian countries. Citizens of countries not on the visa-free list can apply for an <strong>eVisa at evisa.imi.gov.my</strong> for USD 20, granting a 30-day single-entry stay. Malaysia does not require a visa at all for short tourism visits for most Western passport holders — simply show a valid passport and onward travel proof on arrival."""),
            ("Documents Checklist for Malaysia Entry 2026",
             """<ul>
<li>Valid passport — minimum 6 months validity from arrival date</li>
<li>Return or onward flight ticket</li>
<li>Sufficient funds — RM 500 per person per day is a general guideline</li>
<li>Hotel booking or host address in Malaysia</li>
<li>eVisa approval letter (if applicable) — print or save to phone</li>
<li>Travel insurance (recommended, not mandatory)</li>
<li>Completed arrival/departure card (provided on the aircraft)</li>
</ul>"""),
            ("Eligibility &amp; Visa-Free Nationals",
             """Citizens of ASEAN member states (except Myanmar nationals who need to check current arrangements), EU member states, UK, USA, Australia, New Zealand, Japan, South Korea, and dozens more are eligible for visa-free entry for up to 90 days. For business visits, a company letter of invitation may be requested by immigration officers. Long-stay options include the Malaysia My Second Home (MM2H) programme and professional employment passes."""),
            ("How to Apply for Malaysia eVisa",
             """If your nationality requires a visa, visit <strong>evisa.imi.gov.my</strong> and create an account. Select the eVisa type (Single Entry Tourist), complete the application form, upload a passport scan and photo, and pay USD 20 by card. Processing takes 1–3 business days. Download and print the approval letter to present on arrival. The eVisa is linked to your passport number."""),
        ],
        "fees_title": "Malaysia Visa Fees 2026 — eVisa Cost, Visa-Free Entry & Payment Details",
        "fees_desc": "Malaysia visa fees 2026: USD 20 eVisa, free 90-day visa-free entry for 60+ nationalities, all official charges and payment methods explained.",
        "fees_h1": "Malaysia Visa Fees 2026 — eVisa Cost, Free Entry &amp; All Official Charges",
        "fees_table": [
            ("Visa-free entry (60+ nationalities)", "FREE — up to 90 days"),
            ("eVisa single entry", "USD 20"),
            ("eVisa (multiple entry, if available)", "Varies — check evisa.imi.gov.my"),
            ("Visa on arrival (select nationalities)", "USD 20–30"),
            ("Social/tourist visa (consulate)", "Varies by nationality"),
            ("Long-stay visa (MM2H)", "Application fee applies — check official site"),
            ("Overstay penalty", "Fines and possible detention apply"),
        ],
        "fees_sections": [
            ("Malaysia eVisa Cost 2026",
             """The Malaysia eVisa costs <strong>USD 20</strong> for a single-entry 30-day visit and is paid online at evisa.imi.gov.my using a credit or debit card. There are no additional service fees when applying through the official portal. Third-party agencies may charge processing fees on top of this. Always apply directly through the official Malaysian Immigration Department website to avoid inflated prices."""),
            ("Visa-Free Entry — No Fee Required",
             """More than 60 nationalities enjoy <strong>free visa-free entry</strong> to Malaysia for up to 90 days. This includes citizens of all EU member states, the UK, USA, Canada, Australia, New Zealand, Japan, South Korea, and most ASEAN nations. No application, no fee, no pre-registration — simply arrive at a Malaysian port of entry with a valid passport and onward ticket."""),
            ("Additional Costs &amp; Travel Expenses",
             """While the visa itself is free or inexpensive, travellers should budget for Malaysia Tourism Tax (MTT) charged by accommodation providers. Travel insurance is highly recommended and affordable for the region. Airport departure taxes are included in most airline ticket prices. Currency exchange is widely available at airports and in cities."""),
            ("Refunds &amp; Fee Policy",
             """eVisa fees paid at evisa.imi.gov.my are non-refundable once the application is submitted, regardless of the outcome. If your visa is denied, you will not receive a refund. Ensure all documents are correct before submitting. Consulate visa fees are similarly non-refundable in most cases. Contact the Malaysian High Commission or Embassy for country-specific payment and refund policies."""),
        ],
        "proc_title": "Malaysia Visa Processing Time 2026 — eVisa, Arrival & Timeline Guide",
        "proc_desc": "Malaysia visa processing time 2026: eVisa approved in 1–3 days, instant visa-free entry for 60+ nationalities. Tips to speed up your application.",
        "proc_h1": "Malaysia Visa Processing Time 2026 — eVisa &amp; Entry Timeline Explained",
        "proc_table": [
            ("eVisa (evisa.imi.gov.my)", "1–3 business days"),
            ("Visa-free entry (60+ nationalities)", "Instant — no application needed"),
            ("Visa on arrival", "15–30 minutes at port of entry"),
            ("Social visit pass extension", "3–5 business days (ICA offices)"),
            ("Employment pass / long stay", "2–8 weeks"),
            ("MM2H programme", "3–6 months processing"),
            ("Student pass", "2–4 weeks after university approval"),
        ],
        "proc_sections": [
            ("Malaysia eVisa Processing Time 2026",
             """The Malaysia eVisa is typically processed within <strong>1–3 business days</strong> after a complete application is submitted at evisa.imi.gov.my. During peak travel seasons (Eid, Chinese New Year, school holidays) processing may take slightly longer. Applicants receive an email notification with the outcome. Apply at least one week before travel to leave room for any document requests."""),
            ("Visa-Free Entry — Instant Processing",
             """Citizens of visa-free countries enjoy the fastest possible processing: <strong>instant approval at immigration</strong> upon arrival. No advance application is needed. Simply present your passport, arrival card and onward ticket at the immigration counter. The officer stamps your passport and grants up to 90 days, subject to discretion."""),
            ("Factors That May Delay the eVisa",
             """<ul>
<li>Submitting a photo that does not meet specification (35×50mm, white background)</li>
<li>Passport data entry errors or name mismatches</li>
<li>Incomplete supporting documents (missing onward ticket or accommodation)</li>
<li>Applications submitted during Malaysian public holidays</li>
<li>Additional security or background checks for certain nationalities</li>
</ul>"""),
            ("Tips for Smooth Malaysia Entry",
             """Check the full visa-free nationality list at the official Malaysian Immigration portal before assuming you need an eVisa. If you do need an eVisa, apply 5–7 days in advance. Carry printed and digital copies of your eVisa approval letter. Ensure your passport has at least two blank pages for entry/exit stamps. Overstaying your permitted period attracts fines and can result in a ban from future entry."""),
        ],
    },

    "philippines": {
        "name": "Philippines",
        "flag": "ph",
        "evisa_url": "evisa.gov.ph",
        "evisa_cost": "PHP 1,500 (~USD 27)",
        "stay": "30 days",
        "processing": "72 hours",
        "standard_fee": "Free 30-day on-arrival for most nationalities",
        "extra": "Extendable at Bureau of Immigration offices",
        "req_title": "Philippines Visa Requirements 2026 — eVisa, Free Arrival & Documents",
        "req_desc": "Philippines visa requirements 2026: free 30-day on-arrival for most visitors, PHP 1500 eVisa guide, documents checklist and evisa.gov.ph instructions.",
        "req_h1": "Philippines Visa Requirements 2026 — Free 30-Day Arrival, eVisa &amp; Documents",
        "req_table": [
            ("On-arrival stay (most nationalities)", "30 days — FREE"),
            ("eVisa fee", "PHP 1,500 (~USD 27) — evisa.gov.ph"),
            ("eVisa stay", "30 days single entry"),
            ("eVisa processing", "72 hours"),
            ("Passport validity", "Minimum 6 months beyond intended stay"),
            ("Photo requirement", "2×2 inches (5×5cm), white background"),
            ("Extension available", "Yes — Bureau of Immigration offices"),
        ],
        "req_sections": [
            ("Overview of Philippines Entry Requirements 2026",
             """Citizens of most countries (over 150 nationalities) receive a <strong>free 30-day visa-free stay</strong> on arrival in the Philippines. No advance application is required — simply present a valid passport and a return or onward ticket. If you wish to apply in advance or your nationality requires a visa, the <strong>eVisa at evisa.gov.ph</strong> costs PHP 1,500 (~USD 27) and is processed in approximately 72 hours. Stays can be extended at Bureau of Immigration offices for additional fees."""),
            ("Documents Checklist for Philippines Entry 2026",
             """<ul>
<li>Valid passport — 6 months validity beyond planned departure</li>
<li>Return or onward flight ticket (mandatory for on-arrival entry)</li>
<li>Proof of accommodation — hotel booking or host address</li>
<li>Sufficient funds — approximately PHP 2,000 per day (guideline)</li>
<li>eVisa approval (if applicable) — print or digital copy</li>
<li>Travel insurance (recommended)</li>
<li>Arrival card (provided on the aircraft or at immigration)</li>
</ul>"""),
            ("Eligibility &amp; Visa Requirements by Nationality",
             """Most nationalities receive 30 days on arrival free of charge. Some nationalities are granted longer periods (e.g., certain countries receive 59 days). A small number of nationalities require an advance visa from a Philippine embassy or consulate. Chinese citizens, for example, were historically required to apply in advance but may check current arrangements on the Bureau of Immigration website (immigration.gov.ph). Business visitors and those staying longer than 30 days should apply for the appropriate visa category."""),
            ("How to Apply for Philippines eVisa",
             """Visit <strong>evisa.gov.ph</strong>, select Tourist eVisa (9a category), complete the online form, upload a passport photo and scan, and pay PHP 1,500 by credit or debit card. Processing takes up to 72 hours. Once approved, download and print the eVisa to present on arrival. The eVisa grants a 30-day single-entry stay and can be extended in-country."""),
        ],
        "fees_title": "Philippines Visa Fees 2026 — eVisa Cost, Free Arrival & All Charges",
        "fees_desc": "Philippines visa fees 2026: free 30-day on-arrival for 150+ nationalities, PHP 1500 eVisa cost, extension fees and payment methods explained.",
        "fees_h1": "Philippines Visa Fees 2026 — Free Arrival, eVisa &amp; All Official Charges",
        "fees_table": [
            ("On-arrival (150+ nationalities)", "FREE — 30 days"),
            ("eVisa (evisa.gov.ph)", "PHP 1,500 (~USD 27)"),
            ("eVisa convenience fee", "PHP 200 (~USD 4) — included in total"),
            ("30-day extension (1st)", "PHP 3,030"),
            ("Additional 30-day extension", "PHP 3,030"),
            ("ACR I-Card (stays 59+ days)", "USD 50 registration fee"),
            ("Overstay fine", "Varies — contact Bureau of Immigration"),
        ],
        "fees_sections": [
            ("Free On-Arrival — No Visa Fee",
             """Citizens of most countries enjoy <strong>completely free entry</strong> to the Philippines for 30 days. No advance application, no fee, no registration. This is the simplest and most cost-effective option. Simply arrive at Ninoy Aquino International Airport (Manila) or any international port of entry with a valid passport and onward ticket."""),
            ("Philippines eVisa Fee 2026",
             """The Philippines eVisa costs <strong>PHP 1,500</strong> (approximately USD 27) for a single-entry 30-day tourist visa. This includes a PHP 200 convenience fee. Payment is made online by credit or debit card at evisa.gov.ph. The fee is non-refundable once the application is submitted. Third-party services may charge additional fees; use only the official portal to avoid overcharging."""),
            ("Extension Fees at Bureau of Immigration",
             """If you wish to stay longer than 30 days, the Bureau of Immigration (BI) charges approximately PHP 3,030 for the first 30-day extension. Additional extensions cost the same rate. Foreigners intending to stay 59 days or more must register for an Alien Certificate of Registration Identity Card (ACR I-Card) at a fee of USD 50. All payments are made at BI offices or authorised centres nationwide."""),
            ("Payment Methods &amp; Refund Policy",
             """The eVisa portal accepts Visa, Mastercard and select local payment options. Official Bureau of Immigration offices accept cash and card. eVisa fees are non-refundable. Extension fees cannot be reclaimed once paid, even if you depart early. If your eVisa is denied, you may reapply but must pay the fee again. Always apply through official channels to protect your payment."""),
        ],
        "proc_title": "Philippines Visa Processing Time 2026 — eVisa 72h & Arrival Guide",
        "proc_desc": "Philippines visa processing time 2026: eVisa processed in 72 hours, instant free on-arrival for 150+ nationalities. Tips to avoid delays at immigration.",
        "proc_h1": "Philippines Visa Processing Time 2026 — 72h eVisa &amp; Instant Arrival Entry",
        "proc_table": [
            ("On-arrival (150+ nationalities)", "Instant — no advance application"),
            ("eVisa (evisa.gov.ph)", "Up to 72 hours"),
            ("Embassy/consulate visa", "5–15 business days"),
            ("30-day extension (BI office)", "Same day — 2 hours"),
            ("ACR I-Card issuance", "3–5 business days"),
            ("Long-stay visa (SRRV, etc.)", "4–8 weeks"),
            ("Working visa (9G)", "2–4 weeks"),
        ],
        "proc_sections": [
            ("Philippines eVisa Processing Time",
             """The Philippines eVisa at evisa.gov.ph is processed in up to <strong>72 hours</strong> (3 business days) after a complete application is submitted. In practice, many applicants receive approval within 24 hours. During Philippine public holidays (Holy Week, Christmas, New Year) processing may be slower. Apply at least 5 days before travel to allow adequate buffer time."""),
            ("On-Arrival Processing — Instant Entry",
             """For nationals of visa-free countries, processing at the immigration counter is typically <strong>5–10 minutes</strong>. Present your passport, arrival card and onward ticket. The immigration officer stamps your passport for 30 days. During peak travel periods (December–January, Holy Week) queues at NAIA Manila can be long — allow extra time."""),
            ("Common Causes of Delay",
             """<ul>
<li>Submitted photo does not meet the 2×2 inch white-background specification</li>
<li>Passport validity less than 6 months from arrival date</li>
<li>No return or onward ticket presented at immigration</li>
<li>Incomplete eVisa application form fields</li>
<li>Applications submitted on Philippine holidays</li>
<li>Background security checks for certain nationalities</li>
</ul>"""),
            ("How to Speed Up Your Philippines Visa",
             """If you qualify for on-arrival entry, no advance action is needed — this is the fastest option. If applying for an eVisa, submit a complete and accurate application at evisa.gov.ph at least 5–7 days before travel. Check your email regularly for requests for additional information. On arrival, have all documents ready and join the correct immigration queue. Extensions at Bureau of Immigration offices are processed on the same day within a few hours."""),
        ],
    },

    "cambodia": {
        "name": "Cambodia",
        "flag": "kh",
        "evisa_url": "evisa.gov.kh",
        "evisa_cost": "USD 30",
        "stay": "30 days tourist",
        "processing": "3 business days",
        "standard_fee": "VOA USD 35",
        "extra": "Visa on arrival USD 35 also available at major border crossings",
        "req_title": "Cambodia Visa Requirements 2026 — eVisa, VOA & Documents Checklist",
        "req_desc": "Cambodia visa requirements 2026: USD 30 eVisa at evisa.gov.kh, USD 35 visa on arrival, documents checklist, 30-day tourist stay and application guide.",
        "req_h1": "Cambodia Visa Requirements 2026 — eVisa, Visa on Arrival &amp; Documents",
        "req_table": [
            ("eVisa fee", "USD 30 — evisa.gov.kh"),
            ("Visa on arrival (VOA)", "USD 35 at international airports/crossings"),
            ("Stay allowed", "30 days tourist (both options)"),
            ("eVisa processing", "3 business days"),
            ("Passport validity", "Minimum 6 months beyond stay"),
            ("Photo requirement", "4×6cm, white background, recent"),
            ("Extension possible", "Yes — 30 days at Department of Immigration"),
        ],
        "req_sections": [
            ("Overview of Cambodia Entry Requirements 2026",
             """Cambodia offers two main short-stay visa options for tourists: the <strong>eVisa at USD 30</strong> (apply online at evisa.gov.kh) and the <strong>Visa on Arrival at USD 35</strong> available at Phnom Penh, Siem Reap and Sihanoukville airports and most major land border crossings. Both grant a 30-day single-entry tourist stay. ASEAN nationals and a handful of other countries receive visa-free entry. Citizens of all other countries should apply for either option before or upon arrival."""),
            ("Documents Checklist for Cambodia Visa 2026",
             """<ul>
<li>Valid passport — minimum 6 months validity from arrival</li>
<li>Passport-style photo — 4×6cm, white background, taken within 6 months</li>
<li>Completed eVisa application at evisa.gov.kh (for eVisa applicants)</li>
<li>USD 30 payment by card (eVisa) or USD 35 cash (VOA)</li>
<li>Return or onward flight ticket</li>
<li>Hotel booking or accommodation address</li>
<li>Sufficient funds — USD 50/day recommended</li>
</ul>"""),
            ("Eligibility &amp; Visa-Free Nationals",
             """ASEAN member state nationals (Indonesia, Malaysia, Philippines, Singapore, Thailand, Brunei, Laos, Myanmar, Vietnam) receive visa-free entry to Cambodia. Most other nationalities must obtain a tourist visa either in advance (eVisa) or on arrival. Diplomatic and official passport holders of many countries also receive visa-free access under bilateral agreements."""),
            ("How to Apply for Cambodia eVisa",
             """Visit <strong>evisa.gov.kh</strong>, the official Cambodian e-visa portal. Complete the application form with personal details, passport information, travel dates and intended entry point. Upload a recent passport photo (4×6cm, white background) and a scan of your passport bio-data page. Pay USD 30 by credit or debit card. Processing takes 3 business days. Download and print the approved eVisa to present at immigration."""),
        ],
        "fees_title": "Cambodia Visa Fees 2026 — eVisa USD 30, VOA USD 35 & All Charges",
        "fees_desc": "Cambodia visa fees 2026: USD 30 eVisa via evisa.gov.kh, USD 35 visa on arrival, extension fees and official payment methods fully explained.",
        "fees_h1": "Cambodia Visa Fees 2026 — eVisa USD 30, Visa on Arrival &amp; Extension Costs",
        "fees_table": [
            ("eVisa tourist (evisa.gov.kh)", "USD 30"),
            ("Visa on arrival (tourist)", "USD 35"),
            ("Visa on arrival (business)", "USD 35"),
            ("30-day extension (tourist)", "USD 45"),
            ("Business visa (E) — 1 month", "USD 35"),
            ("ASEAN nationals", "FREE"),
            ("eVisa overstay fine (per day)", "USD 10"),
        ],
        "fees_sections": [
            ("Cambodia eVisa Fee 2026",
             """The official Cambodia eVisa costs <strong>USD 30</strong> for a tourist visa, payable online at evisa.gov.kh by credit or debit card. There are no additional service fees through the official portal. The fee is non-refundable upon submission. Note that the visa on arrival is slightly more expensive at USD 35 — the eVisa saves USD 5 and avoids potential queues at the border."""),
            ("Visa on Arrival Fee",
             """The visa on arrival (VOA) for Cambodia costs <strong>USD 35</strong> for both tourist and business categories. Payment is in US dollars cash at the immigration counter. Some border crossings may not accept card payments, so carry sufficient USD. The VOA is available at Phnom Penh International Airport, Siem Reap International Airport, Sihanoukville Airport and most major land crossings."""),
            ("Extension &amp; Long-Stay Fees",
             """A 30-day tourist visa extension costs <strong>USD 45</strong> at the General Department of Immigration. Extensions must be applied for before the original visa expires. Overstaying your visa attracts a fine of <strong>USD 10 per day</strong>. Business visa (E) holders can obtain longer-term extensions at different rates. Long-term stays require an Ordinary/Business visa rather than the tourist eVisa."""),
            ("Payment Methods &amp; Refund Policy",
             """eVisa payments via evisa.gov.kh accept Visa and Mastercard. VOA payments are cash USD only at most land borders; airports may accept card in some instances. All visa fees are non-refundable once paid. Avoid third-party websites that charge inflated fees — always use official government portals for Cambodia visas."""),
        ],
        "proc_title": "Cambodia Visa Processing Time 2026 — eVisa 3 Days & VOA Guide",
        "proc_desc": "Cambodia visa processing time 2026: eVisa processed in 3 business days at evisa.gov.kh, visa on arrival instant at airport. Tips to avoid border delays.",
        "proc_h1": "Cambodia Visa Processing Time 2026 — eVisa 3 Business Days &amp; VOA Instant",
        "proc_table": [
            ("eVisa (evisa.gov.kh)", "3 business days"),
            ("Visa on arrival (airport)", "15–45 minutes at counter"),
            ("Visa on arrival (land border)", "30–90 minutes"),
            ("Embassy/consulate visa", "3–5 business days"),
            ("Tourist extension (30 days)", "Same day — Immigration office"),
            ("Business visa extension", "1–3 business days"),
            ("Long-term visa (retired/investor)", "2–4 weeks"),
        ],
        "proc_sections": [
            ("Cambodia eVisa Processing Time",
             """eVisas applied for at <strong>evisa.gov.kh</strong> are processed in approximately <strong>3 business days</strong>. Applicants receive an email with the approved eVisa PDF for printing. During Cambodian public holidays (Khmer New Year in April, Pchum Ben, etc.) processing may be slower. Apply at least 7 days in advance to leave room for any delays or document correction requests."""),
            ("Visa on Arrival Processing",
             """The VOA at Phnom Penh and Siem Reap airports typically takes <strong>15–45 minutes</strong> depending on queue length. At busy international airports, have your passport, photo, USD 35 in cash, and accommodation details ready. Land border crossings can take 30–90 minutes. Having all documents ready reduces waiting time significantly."""),
            ("Tips to Speed Up Cambodia Visa Processing",
             """Apply for the eVisa at evisa.gov.kh at least 7 days before departure to allow for the 3-business-day processing window plus buffer time. Ensure your photo meets the 4×6cm white-background requirement. For VOA, arrive with the exact USD 35 in crisp notes (some counters are strict about this). Avoid crossing at smaller, less-staffed land borders during peak public holiday periods."""),
            ("Delays &amp; Common Issues",
             """<ul>
<li>Photo does not meet the 4×6cm or white background requirement</li>
<li>Passport expiry within 6 months of arrival</li>
<li>System downtime on the evisa.gov.kh portal</li>
<li>Incorrect passport number or date of birth on eVisa application</li>
<li>Insufficient USD cash for VOA payment</li>
<li>Peak season crowds at airports (December–January, April for Khmer New Year)</li>
</ul>"""),
        ],
    },

    "new-zealand": {
        "name": "New Zealand",
        "flag": "nz",
        "evisa_url": "immigration.govt.nz",
        "evisa_cost": "NZD 17 (mobile) / NZD 23 (web) + IVL NZD 35",
        "stay": "90 days per visit (2-year NZeTA validity)",
        "processing": "Instant to 72 hours",
        "standard_fee": "NZD 17–23 + NZD 35 IVL",
        "extra": "International Visitor Levy (IVL) NZD 35 is mandatory",
        "req_title": "New Zealand NZeTA Requirements 2026 — Documents, IVL & Eligibility",
        "req_desc": "New Zealand NZeTA requirements 2026: NZD 17-23 fee plus NZD 35 IVL, 2-year validity, documents checklist and official immigration.govt.nz application guide.",
        "req_h1": "New Zealand NZeTA Requirements 2026 — Documents, IVL &amp; Eligibility Guide",
        "req_table": [
            ("NZeTA fee (mobile app)", "NZD 17"),
            ("NZeTA fee (web)", "NZD 23"),
            ("International Visitor Levy (IVL)", "NZD 35 (mandatory, paid with NZeTA)"),
            ("NZeTA validity", "2 years from grant date"),
            ("Stay per visit", "Up to 90 days"),
            ("Passport validity", "Valid for duration of stay"),
            ("Processing time", "Instant to 72 hours"),
        ],
        "req_sections": [
            ("Overview of New Zealand NZeTA Requirements 2026",
             """Visitors from visa-waiver countries (including USA, UK, EU nations, Canada, Japan and more) must obtain a <strong>New Zealand Electronic Travel Authority (NZeTA)</strong> before boarding their flight to New Zealand. The NZeTA is applied for at <strong>immigration.govt.nz</strong> or via the official NZeTA mobile app. It costs <strong>NZD 17</strong> (mobile) or <strong>NZD 23</strong> (web) plus the mandatory <strong>International Visitor Levy (IVL) of NZD 35</strong>, payable together during the application. The NZeTA is valid for 2 years and allows multiple visits of up to 90 days each."""),
            ("Documents Checklist for NZeTA 2026",
             """<ul>
<li>Valid passport — must be valid for duration of stay</li>
<li>Passport biographic page scan or photo (for NZeTA application)</li>
<li>A selfie photo (taken in app or uploaded online)</li>
<li>Valid email address for approval notification</li>
<li>Credit or debit card for NZD 17/23 + NZD 35 IVL</li>
<li>Return or onward flight ticket (for immigration officer)</li>
<li>Sufficient funds — NZD 1,000 per month or NZD 400 per month if accommodation prepaid</li>
</ul>"""),
            ("Eligibility — Who Needs an NZeTA?",
             """NZeTA is required for all passport holders of NZeTA-eligible countries who are travelling to New Zealand by air. Citizens of Australia do not need an NZeTA. If your country is not on the visa-waiver or NZeTA-eligible list, you must apply for a visitor visa. Check your eligibility on the immigration.govt.nz visa wizard before applying. Cruise passengers arriving by sea in New Zealand do not need an NZeTA."""),
            ("How to Apply for NZeTA",
             """Download the official NZeTA app or visit <strong>immigration.govt.nz/nzeta</strong>. Provide passport details, upload a photo, answer health and character declarations, and pay NZD 17/23 + NZD 35 IVL. Most applications are decided instantly; some may take up to 72 hours. The NZeTA is linked electronically to your passport — no printout is required. Apply before booking non-refundable flights in case of any eligibility issues."""),
        ],
        "fees_title": "New Zealand NZeTA Fees 2026 — NZD 17/23 + IVL NZD 35 Cost Guide",
        "fees_desc": "New Zealand NZeTA fees 2026: NZD 17 mobile or NZD 23 web, plus mandatory NZD 35 IVL. Total cost, payment methods and official immigration.govt.nz guide.",
        "fees_h1": "New Zealand NZeTA Fees 2026 — NZD 17/23 Application &amp; NZD 35 IVL Total",
        "fees_table": [
            ("NZeTA (mobile app)", "NZD 17"),
            ("NZeTA (web browser)", "NZD 23"),
            ("International Visitor Levy (IVL)", "NZD 35 (mandatory)"),
            ("Total cost (mobile)", "NZD 52"),
            ("Total cost (web)", "NZD 58"),
            ("Australian citizens", "FREE — no NZeTA needed"),
            ("NZeTA validity", "2 years — multiple entries"),
        ],
        "fees_sections": [
            ("NZeTA Application Fee Breakdown",
             """The NZeTA has two fee tiers: <strong>NZD 17 via the mobile app</strong> and <strong>NZD 23 via the web browser</strong>. Using the app saves NZD 6 and is the recommended method. In addition, every NZeTA applicant must pay the mandatory <strong>International Visitor Levy (IVL) of NZD 35</strong>, bringing the total to NZD 52 (mobile) or NZD 58 (web). The IVL funds conservation and tourism infrastructure in New Zealand."""),
            ("International Visitor Levy (IVL)",
             """The IVL of <strong>NZD 35</strong> is collected at the same time as the NZeTA application fee. It is a one-off payment per NZeTA grant (valid 2 years) and is not charged again for subsequent visits within the 2-year validity period. Australian citizens are exempt from both the NZeTA and IVL. Cruise passengers arrive separately and have different levy arrangements."""),
            ("Payment Methods",
             """Both the NZeTA application fee and IVL are paid online during the application process using Visa, Mastercard, American Express or UnionPay. The total payment (NZD 52 or NZD 58) is taken in a single transaction. Fees are in New Zealand dollars; your card provider applies the exchange rate at the time of payment. There are no additional processing fees from the government portal."""),
            ("Refund Policy",
             """NZeTA and IVL fees are <strong>non-refundable</strong> once paid, regardless of whether the application is approved or declined. If your NZeTA is declined, you will need to apply for a visitor visa and cannot reclaim the NZeTA/IVL fee. Ensure your passport is valid, your travel history is accurately declared, and your character declarations are honest before paying."""),
        ],
        "proc_title": "New Zealand NZeTA Processing Time 2026 — Instant to 72h Timeline",
        "proc_desc": "New Zealand NZeTA processing time 2026: most approvals instant, up to 72 hours maximum. Tips to apply correctly at immigration.govt.nz for fast results.",
        "proc_h1": "New Zealand NZeTA Processing Time 2026 — Instant Approval &amp; 72h Maximum",
        "proc_table": [
            ("NZeTA (mobile app)", "Instant to 72 hours"),
            ("NZeTA (web browser)", "Instant to 72 hours"),
            ("Visitor visa (embassy)", "20–30 working days"),
            ("Working Holiday Visa (online)", "Up to 6 weeks"),
            ("Skilled Migrant Visa", "Several months"),
            ("Student visa", "Up to 6 weeks"),
            ("Residence visa", "Months — varies by pathway"),
        ],
        "proc_sections": [
            ("NZeTA Processing Time 2026",
             """The NZeTA is designed for speed. The vast majority of applications submitted via the official mobile app or at immigration.govt.nz receive an <strong>instant decision</strong>. In cases where additional checks are needed (character history, health declarations) processing can take up to <strong>72 hours</strong>. Apply at least 3 days before travel, but ideally further in advance for peace of mind."""),
            ("Factors That May Cause Delay",
             """<ul>
<li>Health or character declarations requiring additional review</li>
<li>Previous immigration issues or visa refusals in any country</li>
<li>Technical errors or photo quality issues in the application</li>
<li>Peak application periods</li>
<li>Passport photo that does not clearly show your face</li>
</ul>"""),
            ("What to Do if Your NZeTA Takes Longer",
             """If your NZeTA has not been decided within 72 hours, log into your application account at immigration.govt.nz to check for messages or requests for additional information. Do not book non-refundable flights until your NZeTA is approved. If your application is declined, you can apply for a visitor visa through Immigration New Zealand, which takes 20–30 working days but allows you to provide additional supporting documents."""),
            ("NZeTA Validity &amp; Renewal",
             """Each NZeTA is valid for <strong>2 years</strong> and allows unlimited trips to New Zealand within that period (up to 90 days per visit). When your NZeTA expires, you simply apply for a new one through the same process. There is no renewal per se — it is a fresh application. Processing for a new NZeTA is typically just as fast, usually instant."""),
        ],
    },

    "hong-kong": {
        "name": "Hong Kong",
        "flag": "hk",
        "evisa_url": "immd.gov.hk",
        "evisa_cost": "No visa required for most (170+ nationalities)",
        "stay": "90 days visa-free for most nationalities",
        "processing": "Instant — no advance application",
        "standard_fee": "No fee for most visitors",
        "extra": "Pre-arrival Registration for some nationalities from 2025",
        "req_title": "Hong Kong Visa Requirements 2026 — Visa-Free Entry for 170+ Nationalities",
        "req_desc": "Hong Kong visa requirements 2026: 90-day visa-free entry for 170+ nationalities, no visa needed for most visitors, official immd.gov.hk entry guide.",
        "req_h1": "Hong Kong Visa Requirements 2026 — Visa-Free Entry for 170+ Nationalities",
        "req_table": [
            ("Visa-free entry (170+ nationalities)", "90 days — no fee, no application"),
            ("Visa fee (if required)", "Varies by nationality — contact HKSAR consulate"),
            ("Passport validity", "Validity beyond intended stay"),
            ("Photo requirement", "Not required for visa-free entry"),
            ("Pre-arrival Registration (PAR)", "Required for some nationalities from 2025"),
            ("Entry points", "All international airports, sea ports, land crossings"),
            ("Official portal", "immd.gov.hk"),
        ],
        "req_sections": [
            ("Overview of Hong Kong Entry Requirements 2026",
             """Hong Kong offers <strong>visa-free entry for over 170 nationalities</strong>, making it one of the most open destinations in Asia. Citizens of all EU member states, UK, USA, Canada, Australia, New Zealand, Japan, South Korea and many more can enter Hong Kong without any advance visa application for stays of up to 90 days. Simply present a valid passport at immigration. From 2025, Hong Kong introduced a <strong>Pre-arrival Registration (PAR)</strong> requirement for a small number of nationalities — check immd.gov.hk for the current list."""),
            ("Documents Checklist for Hong Kong Entry 2026",
             """<ul>
<li>Valid passport — valid for duration of intended stay</li>
<li>Onward or return flight ticket (immigration may request)</li>
<li>Hotel booking or accommodation address</li>
<li>Sufficient funds for your stay</li>
<li>Pre-arrival Registration (PAR) confirmation (if your nationality requires it)</li>
<li>No visa application form required for most visitors</li>
<li>Travel insurance (recommended)</li>
</ul>"""),
            ("Who Needs a Hong Kong Visa?",
             """The vast majority of travellers do not need a visa for Hong Kong. A small number of nationalities do require advance permission — mainly from certain African, Middle Eastern and South Asian countries. Check the complete list of visa-free countries at <strong>immd.gov.hk</strong>. Travellers who require a visa must apply at a HKSAR Immigration office or through a Hong Kong Economic and Trade Office abroad. From 2025, certain nationalities must complete the online Pre-arrival Registration (PAR) before departure."""),
            ("How to Enter Hong Kong Without a Visa",
             """If your nationality qualifies for visa-free access, simply arrive at Hong Kong International Airport (HKIA) or any port of entry with a valid passport and onward ticket. Join the visitor immigration queue, present your passport and answer basic questions from the immigration officer. Your stamp typically grants up to 90 days. No advance registration, application or fee is required for most visitors."""),
        ],
        "fees_title": "Hong Kong Visa Fees 2026 — Free Entry for Most, Visa Cost for Others",
        "fees_desc": "Hong Kong visa fees 2026: completely free for 170+ visa-free nationalities. Visa cost for restricted nationalities and PAR requirements via immd.gov.hk.",
        "fees_h1": "Hong Kong Visa Fees 2026 — Free Entry for 170+ Nationalities &amp; Visa Costs",
        "fees_table": [
            ("Visa-free entry (170+ nationalities)", "FREE — no fee"),
            ("Pre-arrival Registration (PAR)", "FREE — for applicable nationalities"),
            ("Visa application (standard)", "HKD 230–460 (varies by category)"),
            ("Extension of stay", "HKD 190"),
            ("Working visa / Employment entry permit", "HKD 1,100–2,900"),
            ("Study visa / Student entry permit", "HKD 1,100"),
            ("Overstay — illegal stay", "Criminal offence — fines and detention"),
        ],
        "fees_sections": [
            ("Hong Kong Visa-Free — No Cost for Most Visitors",
             """For the vast majority of international travellers, entry to Hong Kong is <strong>completely free of charge</strong>. Over 170 nationalities receive visa-free access with no application, no fee and no advance registration (with the exception of the new PAR system for a small number of nationalities). This free and frictionless access makes Hong Kong ideal for short tourism, business and transit visits."""),
            ("Pre-arrival Registration (PAR) — Free but Mandatory",
             """From 2025, a small number of nationalities are required to complete the free <strong>Pre-arrival Registration (PAR)</strong> at immd.gov.hk before boarding a flight to Hong Kong. The PAR itself is free. Check whether your nationality is on the PAR list — failing to register when required may result in being denied boarding or refused entry."""),
            ("Visa Fees for Restricted Nationalities",
             """Nationalities that require an advance visa must apply at a HKSAR Immigration office or a Hong Kong Economic and Trade Office. Fees vary by visa category: standard visitor visas typically cost HKD 230–460 (approximately USD 30–60). Employment Entry Permits cost significantly more at HKD 1,100–2,900. All fees are set by the Hong Kong Immigration Department."""),
            ("Refund &amp; Payment Policy",
             """Visa application fees paid to the Hong Kong Immigration Department are generally non-refundable. PAR registration is free and can be updated if travel plans change. For standard visa applications, payments are made at HKSAR Immigration offices or authorised payment centres. For the most accurate fee schedule, always consult immd.gov.hk."""),
        ],
        "proc_title": "Hong Kong Visa Processing Time 2026 — Instant Entry for Most Visitors",
        "proc_desc": "Hong Kong visa processing time 2026: instant entry for 170+ visa-free nationalities, PAR online registration and consulate visa timelines via immd.gov.hk.",
        "proc_h1": "Hong Kong Visa Processing Time 2026 — Instant Arrival &amp; PAR Registration",
        "proc_table": [
            ("Visa-free entry (170+ nationalities)", "Instant — no advance processing"),
            ("Pre-arrival Registration (PAR)", "Online — typically same day"),
            ("Visitor visa (consulate)", "4–6 weeks"),
            ("Extension of stay", "Usually same day at ImmD office"),
            ("Employment Entry Permit", "4–8 weeks"),
            ("Investment visa", "4–6 weeks"),
            ("Student entry permit", "4–8 weeks"),
        ],
        "proc_sections": [
            ("Instant Entry for Visa-Free Nationalities",
             """For citizens of the 170+ visa-free nationalities, there is simply no processing time — entry is granted at the immigration counter in minutes. No advance application, no waiting, no bureaucracy. Hong Kong immigration counters at HKIA are known for efficiency, and most visitors clear immigration within 10–20 minutes of landing."""),
            ("Pre-arrival Registration (PAR) Processing",
             """The online PAR at immd.gov.hk is designed to be quick and straightforward. Most registrations are confirmed <strong>within the same day</strong>. You will receive a reference number by email. Present this reference number at check-in and immigration. PAR is a one-time registration per trip, not a visa — it does not guarantee entry but confirms your nationality's registration requirement has been met."""),
            ("Consulate Visa Processing",
             """Nationalities that require an advance visa must apply at a HKSAR Immigration office or Hong Kong Economic and Trade Office. Standard visitor visa processing takes <strong>4–6 weeks</strong>. Employment and investment entry permits may take 4–8 weeks. Applications can be submitted in person or by post depending on the office. Ensure all documents are complete to avoid delays."""),
            ("Tips for Smooth Hong Kong Entry",
             """Check your nationality's status on immd.gov.hk before travel. Complete PAR registration if required — it takes only minutes online. Have your onward or return ticket ready; immigration officers may ask to see it. For visa-required nationalities, apply well in advance of travel dates. If you need to extend your stay, visit the Hong Kong Immigration Department at Immigration Tower in Wan Chai before your current permission expires."""),
        ],
    },

    "taiwan": {
        "name": "Taiwan",
        "flag": "tw",
        "evisa_url": "boca.gov.tw",
        "evisa_cost": "No fee — visa-free for 165+ nationalities",
        "stay": "90 days visa-free for 165+ nationalities",
        "processing": "No advance application for visa-free",
        "standard_fee": "No fee for most visitors",
        "extra": "Official portal: boca.gov.tw (Bureau of Consular Affairs)",
        "req_title": "Taiwan Visa Requirements 2026 — Visa-Free for 165+ Nationalities Guide",
        "req_desc": "Taiwan visa requirements 2026: free 90-day visa-free entry for 165+ nationalities, no visa needed for most visitors, official boca.gov.tw entry guide.",
        "req_h1": "Taiwan Visa Requirements 2026 — Free Visa-Free Entry for 165+ Nationalities",
        "req_table": [
            ("Visa-free stay (165+ nationalities)", "90 days — FREE, no advance application"),
            ("Visa fee (if required)", "Varies — boca.gov.tw"),
            ("Passport validity", "Valid for duration of stay + 6 months recommended"),
            ("Photo requirement", "Not required for visa-free entry"),
            ("Entry points", "Taiwan Taoyuan Airport, Taipei Songshan, other airports"),
            ("Official portal", "boca.gov.tw"),
            ("Extension of stay", "Apply at National Immigration Agency"),
        ],
        "req_sections": [
            ("Overview of Taiwan Entry Requirements 2026",
             """Taiwan grants <strong>90-day visa-free entry to citizens of 165+ countries</strong>, including all EU member states, the USA, UK, Canada, Australia, New Zealand, Japan, South Korea, and many Latin American and Southeast Asian countries. The visa-free privilege requires no advance application, no fee and no registration. Simply arrive at Taiwan Taoyuan International Airport or another point of entry with a valid passport and onward ticket."""),
            ("Documents Checklist for Taiwan Visa-Free Entry 2026",
             """<ul>
<li>Valid passport — recommended 6 months validity from arrival</li>
<li>Return or onward flight ticket (highly recommended — immigration may check)</li>
<li>Hotel booking or host address in Taiwan</li>
<li>Sufficient funds for the stay</li>
<li>Completed arrival/departure card (provided on aircraft or at immigration)</li>
<li>No visa application form required for visa-free nationals</li>
<li>Travel insurance (recommended)</li>
</ul>"""),
            ("Eligibility &amp; Countries That Require a Visa",
             """The full updated list of visa-free countries is published by the Bureau of Consular Affairs (BOCA) at <strong>boca.gov.tw</strong>. Nationals of countries not on the visa-free list must apply for a visitor visa (multiple or single entry) through a Taipei Economic and Cultural Office (TECO) or representative office abroad. Most visa applications require a standard set of documents including a valid passport, photo, application form and travel itinerary."""),
            ("How to Enter Taiwan Without a Visa",
             """If your nationality qualifies, no advance steps are needed. Arrive at Taiwan Taoyuan International Airport (TPE), proceed through immigration, present your passport, and receive a stamp for 90 days. Carry a return or onward ticket as immigration may request proof of departure. No registration online, no eVisa — just your passport. For stays beyond 90 days, apply for an extension at the National Immigration Agency offices before expiry."""),
        ],
        "fees_title": "Taiwan Visa Fees 2026 — Free Entry for 165+ Nationalities & Visa Costs",
        "fees_desc": "Taiwan visa fees 2026: completely free 90-day visa-free entry for 165+ nationalities. Visa costs for other nationalities via boca.gov.tw explained.",
        "fees_h1": "Taiwan Visa Fees 2026 — Free Entry for 165+ Nationalities &amp; Official Visa Costs",
        "fees_table": [
            ("Visa-free entry (165+ nationalities)", "FREE — 90 days"),
            ("Visitor visa single entry", "USD 31 (varies by nationality/TECO office)"),
            ("Visitor visa multiple entry", "USD 62 (varies)"),
            ("Resident visa", "Varies by category"),
            ("Extension of stay (NIA)", "TWD 300–1,000 (varies)"),
            ("Working Holiday visa", "USD 31 (available for select nationalities)"),
            ("Landing visa (select nationalities)", "USD 31"),
        ],
        "fees_sections": [
            ("Taiwan Visa-Free — Completely Free for Most Visitors",
             """For the 165+ nationalities eligible for visa-free entry, Taiwan costs <strong>nothing</strong> in terms of visa fees. There is no application, no portal, no processing fee. This applies to most Western passport holders and many Asian nationalities. The 90-day stay period is very generous by regional standards and allows ample time for tourism, business meetings, or remote work."""),
            ("Visa Fees for Non-Visa-Free Nationalities",
             """Citizens of countries not on the visa-free list must apply for a visitor visa at a Taipei Economic and Cultural Office (TECO) or Taiwan representative office. Fees are approximately <strong>USD 31 for single entry</strong> and <strong>USD 62 for multiple entry</strong>, though exact fees may vary by nationality and TECO office location due to reciprocal arrangements. Check boca.gov.tw for the applicable fee for your nationality."""),
            ("Extension of Stay Fees",
             """Visitors who wish to stay longer than their initial period can apply for an extension at a National Immigration Agency office. Extension fees range from <strong>TWD 300 to TWD 1,000</strong> (approximately USD 10–33) depending on the extension type. Extensions are granted at the officer's discretion and require proof of sufficient funds, accommodation and a valid reason for extended stay."""),
            ("Payment Methods",
             """TECO offices accept credit cards, bank transfers or cash depending on location. National Immigration Agency extension fees are paid at NIA offices by cash or card. Online payment is not widely available for visa applications. Always check the specific TECO office or NIA branch you plan to use for accepted payment methods before applying."""),
        ],
        "proc_title": "Taiwan Visa Processing Time 2026 — Instant Visa-Free & Consulate Guide",
        "proc_desc": "Taiwan visa processing time 2026: instant entry for 165+ visa-free nationalities, consulate visitor visa timelines and extension guide via boca.gov.tw.",
        "proc_h1": "Taiwan Visa Processing Time 2026 — Instant Arrival &amp; Consulate Timelines",
        "proc_table": [
            ("Visa-free entry (165+ nationalities)", "Instant — no advance application"),
            ("Visitor visa (TECO office)", "2–5 business days"),
            ("Landing visa", "On arrival — 30–60 minutes"),
            ("Extension of stay (NIA)", "Same day to 5 business days"),
            ("Resident visa", "2–4 weeks"),
            ("Working Holiday visa", "2–5 business days"),
            ("Employment Gold Card", "30 business days"),
        ],
        "proc_sections": [
            ("Instant Entry for Visa-Free Nationals",
             """Citizens of the 165+ visa-free nationalities experience <strong>instant entry processing</strong> at Taiwan Taoyuan International Airport (TPE) or other entry points. No advance steps — simply present your passport at immigration and receive a 90-day stamp in minutes. Taiwan's immigration counters are known for their speed and efficiency."""),
            ("TECO Visitor Visa Processing",
             """For nationalities that require a visa, applications submitted at a Taipei Economic and Cultural Office (TECO) are typically processed within <strong>2–5 business days</strong>. Some complex cases or during peak periods may take longer. Applications must be submitted in person or by post; walk-in or appointment requirements vary by TECO location. Check boca.gov.tw for the nearest TECO and their specific procedures."""),
            ("Extension of Stay at NIA",
             """Extensions of stay are handled by the National Immigration Agency (NIA) offices nationwide. Simple extensions are often processed the same day, while more complex cases may take up to 5 business days. Apply before your current permission expires. The NIA can be reached at its main Taipei office or regional branches across the island."""),
            ("Tips for Smooth Taiwan Entry",
             """Have your return or onward ticket ready at immigration — officers may ask to see it. Book accommodation in advance and have the address written down. Sufficient funds are expected (TWD 2,000 per day is a common guideline). If you plan a long stay, investigate whether Taiwan's Employment Gold Card, working holiday visa or resident visa is appropriate for your situation well before the 90-day limit approaches."""),
        ],
    },

    "sri-lanka": {
        "name": "Sri Lanka",
        "flag": "lk",
        "evisa_url": "eta.gov.lk",
        "evisa_cost": "USD 20",
        "stay": "30 days double entry",
        "processing": "24–72 hours",
        "standard_fee": "USD 20",
        "extra": "Electronic Travel Authorisation (ETA) system",
        "req_title": "Sri Lanka Visa Requirements 2026 — ETA, USD 20 & Documents Checklist",
        "req_desc": "Sri Lanka visa requirements 2026: USD 20 ETA via eta.gov.lk, 30-day double entry, 24-72h processing, documents checklist and application guide.",
        "req_h1": "Sri Lanka Visa Requirements 2026 — ETA USD 20, Double Entry &amp; Documents",
        "req_table": [
            ("ETA fee (tourist)", "USD 20 — eta.gov.lk"),
            ("ETA stay", "30 days, double entry"),
            ("ETA processing", "24–72 hours"),
            ("Passport validity", "Minimum 6 months beyond stay"),
            ("Photo requirement", "Passport-size digital photo — white background"),
            ("Entry points", "All international airports, Colombo port"),
            ("Extension possible", "Yes — Department of Immigration Colombo"),
        ],
        "req_sections": [
            ("Overview of Sri Lanka Entry Requirements 2026",
             """Sri Lanka uses an <strong>Electronic Travel Authorisation (ETA) system</strong> for most nationalities. The ETA costs <strong>USD 20</strong> for tourists and is applied for online at <strong>eta.gov.lk</strong>. It grants a 30-day double-entry stay, meaning you can leave and re-enter Sri Lanka once within the validity period. Processing takes 24–72 hours. Some nationalities (citizens of Singapore, Maldives, and a few others) receive free or reduced-fee ETA. Citizens of India receive a separate treatment — check the ETA portal for current rules."""),
            ("Documents Checklist for Sri Lanka ETA 2026",
             """<ul>
<li>Valid passport — minimum 6 months from planned departure date</li>
<li>Digital passport-style photo (white background)</li>
<li>Completed ETA application at eta.gov.lk</li>
<li>USD 20 payment by credit or debit card</li>
<li>Return or onward flight ticket</li>
<li>Hotel booking or accommodation address</li>
<li>Travel insurance (recommended)</li>
<li>Sufficient funds for the stay</li>
</ul>"""),
            ("Eligibility &amp; Special Arrangements",
             """Citizens of most countries can apply for an ETA at eta.gov.lk. Some SAARC nationals and ASEAN countries have special bilateral arrangements that may offer free ETAs or different conditions. Chinese citizens receive a free ETA under a mutual visa-waiver scheme. Always verify the latest eligibility and fee at eta.gov.lk as policies are updated. Visitors with a criminal record may be refused entry; declare any issues honestly on the application."""),
            ("How to Apply for Sri Lanka ETA",
             """Visit <strong>eta.gov.lk</strong>, select the tourist ETA, fill in your personal and passport details, upload a photo, answer health and security declarations, and pay USD 20. Processing takes 24–72 hours, after which you receive the ETA approval by email. Print the approval or save it digitally to present at immigration. The ETA is linked to your passport number — do not change passports between application and travel."""),
        ],
        "fees_title": "Sri Lanka Visa Fees 2026 — ETA USD 20, Double Entry & Payment Guide",
        "fees_desc": "Sri Lanka ETA visa fees 2026: USD 20 tourist ETA at eta.gov.lk, 30-day double entry, extension costs and all official payment methods explained.",
        "fees_h1": "Sri Lanka Visa Fees 2026 — ETA USD 20, Double Entry &amp; All Official Charges",
        "fees_table": [
            ("ETA tourist (eta.gov.lk)", "USD 20"),
            ("ETA business", "USD 40"),
            ("ETA (Singaporeans)", "Free (bilateral agreement)"),
            ("ETA (Maldivians)", "Free"),
            ("30-day extension (1st)", "LKR 5,900 (~USD 20)"),
            ("30-day extension (2nd)", "LKR 8,875 (~USD 30)"),
            ("Overstay fine (per day)", "LKR 2,000 (~USD 7)"),
        ],
        "fees_sections": [
            ("Sri Lanka ETA Fee 2026",
             """The Sri Lanka ETA for tourists costs <strong>USD 20</strong>, paid online at eta.gov.lk. Business ETAs cost USD 40. Citizens of Singapore and Maldives receive free ETAs under bilateral agreements. Payment is accepted by Visa, Mastercard and American Express on the official portal. Some nationalities also receive free ETAs — check eta.gov.lk for the current free-list before applying."""),
            ("Extension Fees at Department of Immigration",
             """If you wish to stay longer than 30 days, you must apply for an extension at the Department of Immigration in Colombo. The first 30-day extension costs approximately <strong>LKR 5,900 (~USD 20)</strong> and the second 30-day extension costs around <strong>LKR 8,875 (~USD 30)</strong>. Extensions can be granted multiple times, but Sri Lanka's Department of Immigration has discretion. Overstaying without an extension attracts fines of approximately LKR 2,000 per day."""),
            ("Additional Costs to Budget For",
             """Beyond the ETA fee, travellers should budget for airport departure tax (generally included in airline tickets), accommodation tax, and transportation within Sri Lanka. Travel insurance is highly recommended given the tropical climate and diverse activities. Currency exchange is available at Bandaranaike International Airport and throughout Colombo and tourist towns."""),
            ("Refund &amp; Payment Policy",
             """ETA fees at eta.gov.lk are <strong>non-refundable</strong> once submitted. If your ETA is denied, you may reapply but will pay the fee again. Ensure all passport details match exactly before submitting. Beware of third-party websites that charge significantly more than USD 20 — only eta.gov.lk is the official government portal."""),
        ],
        "proc_title": "Sri Lanka Visa Processing Time 2026 — ETA 24-72h & Extension Guide",
        "proc_desc": "Sri Lanka ETA processing time 2026: 24–72 hours for tourist ETA at eta.gov.lk, extension timelines and tips to get approved without delays.",
        "proc_h1": "Sri Lanka ETA Processing Time 2026 — 24–72 Hours &amp; What to Expect",
        "proc_table": [
            ("ETA tourist (eta.gov.lk)", "24–72 hours"),
            ("ETA business", "24–72 hours"),
            ("Embassy/consulate visa", "5–10 business days"),
            ("30-day extension (DoI Colombo)", "1–3 business days"),
            ("Residence visa", "4–8 weeks"),
            ("Working visa", "4–6 weeks"),
            ("Student visa", "2–4 weeks"),
        ],
        "proc_sections": [
            ("Sri Lanka ETA Processing Time 2026",
             """Most Sri Lanka ETA applications at <strong>eta.gov.lk</strong> are processed within <strong>24–72 hours</strong>. Many applicants receive approval within 24 hours; however, the official guide states up to 72 hours for all applications. Apply at least 3 days before your travel date. During Sri Lankan public holidays (Sinhala and Tamil New Year in April, Vesak, etc.) processing may be slower. Check your email — including spam folders — for the approval notification."""),
            ("Consulate Visa Processing",
             """For nationalities that cannot use the online ETA system, visa applications submitted at Sri Lankan embassies or high commissions typically take <strong>5–10 business days</strong>. Application requirements and fees vary by nationality. Contact your nearest Sri Lankan diplomatic mission for country-specific procedures."""),
            ("Extension Processing at Department of Immigration",
             """Extensions of stay are processed at the Department of Immigration and Emigration in Colombo. Processing typically takes <strong>1–3 business days</strong>. You will need your passport, ETA approval, accommodation details and evidence of sufficient funds. Apply before your current ETA expires. Regional immigration offices in cities like Kandy may also be able to assist."""),
            ("Tips for Fast ETA Approval",
             """Submit a complete application with an accurate passport photo (white background, no glasses, recent) and correct passport data. Double-check all dates, passport numbers and name spellings before paying. Apply via the official <strong>eta.gov.lk</strong> portal — third-party sites may take longer or charge more. If you need the ETA urgently for an emergency trip, email the Department of Immigration directly for assistance."""),
        ],
    },

    "nepal": {
        "name": "Nepal",
        "flag": "np",
        "evisa_url": "immigration.gov.np",
        "evisa_cost": "USD 30 (15 days) / USD 50 (30 days) / USD 125 (90 days)",
        "stay": "15, 30 or 90 days",
        "processing": "1–3 days (eVisa)",
        "standard_fee": "VOA also available at Tribhuvan International Airport",
        "extra": "Visa on arrival also available at TIA Kathmandu and other border checkpoints",
        "req_title": "Nepal Visa Requirements 2026 — eVisa, VOA & Documents Checklist",
        "req_desc": "Nepal visa requirements 2026: USD 30/50/125 eVisa at immigration.gov.np, visa on arrival, 15/30/90-day options and full documents checklist.",
        "req_h1": "Nepal Visa Requirements 2026 — eVisa, Visa on Arrival &amp; Documents Checklist",
        "req_table": [
            ("eVisa 15 days", "USD 30 — immigration.gov.np"),
            ("eVisa 30 days", "USD 50"),
            ("eVisa 90 days", "USD 125"),
            ("Visa on arrival", "Same fees — available at TIA and border checkpoints"),
            ("Passport validity", "Minimum 6 months beyond stay"),
            ("Photo requirement", "35×45mm, white background, recent"),
            ("SAARC nationals", "Free visa — different terms apply"),
        ],
        "req_sections": [
            ("Overview of Nepal Entry Requirements 2026",
             """Nepal issues tourist visas online via eVisa at <strong>immigration.gov.np</strong> and on arrival at Tribhuvan International Airport (Kathmandu) and designated land border checkpoints. Three duration options are available: <strong>15 days (USD 30)</strong>, <strong>30 days (USD 50)</strong> and <strong>90 days (USD 125)</strong>. Citizens of India and SAARC countries (Bangladesh, Bhutan, Maldives, Pakistan, Sri Lanka) enter Nepal visa-free or under special arrangements. Nationals of China may also have specific bilateral agreements — check immigration.gov.np."""),
            ("Documents Checklist for Nepal Visa 2026",
             """<ul>
<li>Valid passport — minimum 6 months validity from planned departure</li>
<li>Passport-style photo — 35×45mm, white background, recent</li>
<li>Completed eVisa application at immigration.gov.np</li>
<li>USD 30/50/125 payment by card (eVisa) or cash (VOA)</li>
<li>Onward or return flight ticket</li>
<li>Hotel booking or trek itinerary</li>
<li>Travel insurance covering trekking and mountain activities (recommended)</li>
<li>Trekking permits (TIMS card, national park permits) — separate from visa</li>
</ul>"""),
            ("Eligibility &amp; Special Visa Categories",
             """Citizens of SAARC nations other than India may be eligible for free or reduced-fee visas. Indian citizens do not need a visa for Nepal and can enter with a valid Indian passport or voter ID card. Diplomatic passport holders of many countries receive visa-free access. Some restricted nationalities require advance visa approval from the Department of Immigration. Mountaineers and trekkers requiring expedition permits need additional clearances beyond the standard tourist visa."""),
            ("How to Apply for Nepal eVisa",
             """Visit <strong>immigration.gov.np</strong> and select the Online Visa Application. Choose your desired duration (15, 30 or 90 days), fill in personal and passport details, upload a recent passport photo, and pay by credit or debit card. Processing takes 1–3 business days. Download and print the eVisa approval to present at immigration alongside your passport. The eVisa can be used at all international airports and most border checkpoints."""),
        ],
        "fees_title": "Nepal Visa Fees 2026 — eVisa USD 30/50/125 & VOA Cost Guide",
        "fees_desc": "Nepal visa fees 2026: USD 30 for 15 days, USD 50 for 30 days, USD 125 for 90 days. eVisa and visa on arrival costs at immigration.gov.np explained.",
        "fees_h1": "Nepal Visa Fees 2026 — eVisa USD 30 / USD 50 / USD 125 &amp; VOA Costs",
        "fees_table": [
            ("eVisa / VOA 15 days", "USD 30"),
            ("eVisa / VOA 30 days", "USD 50"),
            ("eVisa / VOA 90 days", "USD 125"),
            ("SAARC nationals (non-India)", "Free (conditions apply)"),
            ("Indian nationals", "Free (no visa required)"),
            ("Extension 15 days", "USD 30"),
            ("Overstay fine (per day)", "USD 5"),
        ],
        "fees_sections": [
            ("Nepal eVisa & VOA Fee Structure 2026",
             """Nepal's visa fee structure is clear and consistent whether you apply online (eVisa) or on arrival (VOA): <strong>USD 30 for 15 days</strong>, <strong>USD 50 for 30 days</strong>, and <strong>USD 125 for 90 days</strong>. These are the official fees set by the Department of Immigration. There is no surcharge for applying online versus on arrival; the eVisa is simply more convenient as it avoids queues at the airport."""),
            ("SAARC & Indian Nationals — Free Entry",
             """Citizens of India do not need a visa to enter Nepal and can do so with a valid Indian passport or government-issued photo ID card. SAARC national citizens (Bangladesh, Bhutan, Maldives, Pakistan, Sri Lanka) are eligible for free visas on arrival at designated entry points. Conditions and duration limits may vary for different SAARC nationalities — check immigration.gov.np for the latest bilateral arrangements."""),
            ("Extension Fees",
             """Tourist visas can be extended at the Department of Immigration offices in Kathmandu (Maitighar) or in Pokhara. Each 15-day extension costs <strong>USD 30</strong>. The maximum total stay in Nepal on a tourist visa is 150 days in one calendar year. All extension payments can be made in USD cash or equivalent Nepalese rupees. Overstaying without extension attracts a fine of <strong>USD 5 per day</strong>."""),
            ("Payment Methods",
             """eVisa payments at immigration.gov.np accept Visa, Mastercard and American Express. Visa on arrival payments at TIA and land border checkpoints accept USD cash (most common), Nepalese rupees, and may accept cards at some locations. Carry sufficient USD cash if applying on arrival at remote land border crossings. All fees are non-refundable once paid."""),
        ],
        "proc_title": "Nepal Visa Processing Time 2026 — eVisa 1-3 Days & VOA Guide",
        "proc_desc": "Nepal visa processing time 2026: eVisa processed in 1–3 days at immigration.gov.np, instant visa on arrival at TIA Kathmandu. Tips to avoid delays.",
        "proc_h1": "Nepal Visa Processing Time 2026 — eVisa 1–3 Days &amp; VOA Instant at TIA",
        "proc_table": [
            ("eVisa (immigration.gov.np)", "1–3 business days"),
            ("Visa on arrival (TIA Kathmandu)", "30–60 minutes at counter"),
            ("Visa on arrival (land border)", "30–90 minutes"),
            ("Embassy/consulate visa", "3–5 business days"),
            ("Extension of stay (DoI office)", "Same day"),
            ("Trekking permits (TIMS)", "1–2 hours at NTB offices"),
            ("National park permits", "On site — same day"),
        ],
        "proc_sections": [
            ("Nepal eVisa Processing Time 2026",
             """The Nepal eVisa at <strong>immigration.gov.np</strong> is processed within <strong>1–3 business days</strong>. Many applicants receive approval within 24 hours. The system sends an email notification with the approved eVisa PDF. Apply at least 5 days before travel to ensure you have the eVisa in hand. During Nepalese public holidays (Dashain, Tihar, etc.) processing may take slightly longer."""),
            ("Visa on Arrival Processing at TIA",
             """The visa on arrival at Tribhuvan International Airport (TIA) in Kathmandu typically takes <strong>30–60 minutes</strong> including form completion and payment. During peak trekking season (October–November and March–April) queues can be very long — the eVisa is strongly recommended to skip the VOA queue. On arrival, have a recent photo (or use the photo booths at the airport), cash USD and accommodation details ready."""),
            ("Tips for Fast Nepal Visa Processing",
             """Apply for the eVisa at immigration.gov.np at least 5–7 days before departure. Ensure your photo meets the 35×45mm white-background specification. Check that all passport details are accurately entered, especially the expiry date and passport number. If trekking to restricted areas, obtain trekking area permits separately from your visa — these have their own lead times. For VOA, arrive with exact USD cash and two recent photos."""),
            ("Delays &amp; Common Issues",
             """<ul>
<li>Photo does not meet the 35×45mm white-background requirement</li>
<li>Passport validity under 6 months from intended departure</li>
<li>Portal downtime at immigration.gov.np</li>
<li>Incorrect passport number or date of birth in application</li>
<li>Peak season crowds at TIA VOA counters (October–November, March–April)</li>
<li>Remote land border crossings with limited staff</li>
</ul>"""),
        ],
    },

    "maldives": {
        "name": "Maldives",
        "flag": "mv",
        "evisa_url": "immigration.gov.mv",
        "evisa_cost": "FREE — 30 days on arrival all nationalities",
        "stay": "30 days",
        "processing": "Instant on arrival",
        "standard_fee": "Free for all nationalities",
        "extra": "Extendable to 90 days at Department of Immigration",
        "req_title": "Maldives Visa Requirements 2026 — Free 30-Day Arrival for All Nationalities",
        "req_desc": "Maldives visa requirements 2026: free 30-day on-arrival visa for ALL nationalities, no advance application needed, official immigration.gov.mv entry guide.",
        "req_h1": "Maldives Visa Requirements 2026 — Free 30-Day Arrival for All Nationalities",
        "req_table": [
            ("Visa on arrival", "FREE — all nationalities"),
            ("Stay allowed", "30 days initial"),
            ("Extendable to", "90 days (at Department of Immigration)"),
            ("Passport validity", "Minimum 1 month beyond stay"),
            ("Photo requirement", "Not required on arrival"),
            ("Entry points", "Velana International Airport (MLE) and sea entry"),
            ("Official portal", "immigration.gov.mv"),
        ],
        "req_sections": [
            ("Overview of Maldives Entry Requirements 2026",
             """The Maldives has one of the world's most welcoming visa policies: <strong>all nationalities receive a free 30-day visa on arrival</strong> with no advance application, no eVisa, no embassy visit and no fee of any kind. Simply arrive at Velana International Airport (MLE) in Malé with a valid passport, onward ticket and evidence of sufficient funds or prepaid resort booking. The stamp is placed in your passport at the immigration counter in minutes."""),
            ("Documents Checklist for Maldives Entry 2026",
             """<ul>
<li>Valid passport — minimum 1 month validity beyond intended departure date</li>
<li>Return or onward flight ticket</li>
<li>Confirmed hotel, resort or liveaboard booking (or other accommodation)</li>
<li>Sufficient funds — USD 100 per day per person (guideline)</li>
<li>No visa application form, no photo, no advance registration</li>
<li>Travel insurance (recommended)</li>
<li>Entry/departure card (provided on aircraft)</li>
</ul>"""),
            ("Eligibility — All Nationalities Welcome",
             """The Maldives is unique in that its visa-free on-arrival policy applies to <strong>every passport holder in the world</strong>, without exception. There are no nationality restrictions for the tourist visa on arrival. Diplomatic and official passport holders may have additional privileges. For stays longer than 30 days, an extension must be applied for at the Maldives Department of Immigration before the initial 30 days expire."""),
            ("How to Enter the Maldives",
             """No advance action is required. Book your resort or accommodation, purchase flights to Velana International Airport (MLE), and arrive. At immigration, present your passport, arrival card and accommodation confirmation. The officer stamps a 30-day visa at no charge. Inter-island transfers by speedboat or seaplane are arranged by resorts. The entire immigration process typically takes 5–15 minutes."""),
        ],
        "fees_title": "Maldives Visa Fees 2026 — Free on Arrival for All, Extension Costs",
        "fees_desc": "Maldives visa fees 2026: completely free 30-day on-arrival visa for ALL nationalities. Extension costs and official immigration.gov.mv information.",
        "fees_h1": "Maldives Visa Fees 2026 — Free 30-Day Arrival &amp; Extension Costs",
        "fees_table": [
            ("Visa on arrival (all nationalities)", "FREE"),
            ("30-day extension (1st month)", "MVR 1,125 (~USD 73)"),
            ("30-day extension (2nd month)", "MVR 1,125 (~USD 73)"),
            ("Maximum stay on tourist visa", "90 days total"),
            ("Employment permit", "Varies — Ministry of Economic Development"),
            ("Residency permit", "Varies — contact Department of Immigration"),
            ("Departure tax", "Included in airline ticket"),
        ],
        "fees_sections": [
            ("Maldives On-Arrival Visa — Completely Free",
             """The Maldives charges <strong>absolutely nothing</strong> for the tourist visa on arrival. This applies to every nationality without exception. There is no portal to register on, no fee to pay, and no advance application required. The Maldives tourism industry is built around welcoming visitors, and the free visa policy reflects this. Most tourists simply arrive with their resort booking and are stamped in for 30 days at the airport."""),
            ("Extension of Stay Costs",
             """If you wish to stay beyond the initial 30 days, you must apply for an extension at the Maldives Department of Immigration. Each 30-day extension costs approximately <strong>MVR 1,125 (around USD 73)</strong>. Extensions are available twice, allowing a maximum stay of <strong>90 days</strong> on a tourist visa. Extensions must be applied for before the current permission expires. Applications are made at the Immigration building in Malé or through licensed resort operators."""),
            ("Additional Travel Costs to Budget For",
             """While the visa is free, the Maldives is generally a premium destination. Accommodation ranges from budget guesthouses on local islands to luxury overwater bungalows at world-famous resorts. Internal transfers by speedboat or seaplane from Velana International Airport can cost USD 50–600 depending on the resort's location. Departure tax is normally included in airline ticket prices."""),
            ("Payment Methods",
             """Extension fee payments at the Department of Immigration can be made in Maldivian rufiyaa (MVR) or US dollars. Credit cards are accepted at most resort-based immigration processes. Cash (USD or MVR) is recommended for transactions at the main immigration office in Malé. Always get an official receipt for any payment made to the Department of Immigration."""),
        ],
        "proc_title": "Maldives Visa Processing Time 2026 — Instant Free Arrival for All",
        "proc_desc": "Maldives visa processing time 2026: instant free on-arrival for all nationalities at Velana Airport, extension guide via immigration.gov.mv.",
        "proc_h1": "Maldives Visa Processing Time 2026 — Instant Free Arrival for All Nationalities",
        "proc_table": [
            ("Visa on arrival (all nationalities)", "Instant — 5–15 minutes"),
            ("Extension (1st 30 days)", "1–3 business days at DoI"),
            ("Extension (2nd 30 days)", "1–3 business days at DoI"),
            ("Employment permit", "2–4 weeks"),
            ("Investor permit", "4–8 weeks"),
            ("Permanent residency", "Months — varies by pathway"),
            ("Seaplane/speedboat transfer", "40 minutes–2 hours after arrival"),
        ],
        "proc_sections": [
            ("Maldives On-Arrival Visa — Instant Processing",
             """Processing for the Maldives on-arrival visa is <strong>instant</strong>. No advance registration, no waiting days for an email — the immigration officer at Velana International Airport stamps your passport in the 30-day visitor visa in just a few minutes. Queues are usually short outside of peak season. The entire arrival process including immigration, baggage and customs typically takes 15–30 minutes."""),
            ("Extension Processing at Department of Immigration",
             """Extension applications are submitted at the Maldives Department of Immigration in Malé or through your resort (many resorts facilitate this service for guests). Processing typically takes <strong>1–3 business days</strong>. Apply at least 5 days before your current 30-day permission expires to ensure continuous legal stay. Have your passport, accommodation confirmation and return ticket available."""),
            ("Practical Arrival Tips",
             """Velana International Airport (MLE) operates 24 hours and handles flights from all major international hubs. On arrival, complete the arrival card (provided on the aircraft), proceed to immigration, and collect your baggage before transfer to your resort. Resorts typically send a speedboat or seaplane transfer service. Arrange your inter-island transfer in advance as some remote atolls require seaplane connections that only operate during daylight hours."""),
            ("No Delays for Tourist Visa",
             """Since the on-arrival visa is granted to all nationalities without any advance vetting or processing, <strong>there are effectively no delays</strong> for tourist entry to the Maldives. The only reasons for extended processing would be security-related checks at the immigration counter, which are rare for standard leisure travellers. Ensure your accommodation booking is printed or clearly visible on your phone, as officers may ask to see it."""),
        ],
    },
}

# ---------------------------------------------------------------------------
# HTML template helpers
# ---------------------------------------------------------------------------

def head_block(title, desc, slug, country_slug, page_flag):
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
    <meta content="{desc}" name="description"/>
    <meta content="index, follow" name="robots" />
    <link href="https://www.evisa-card.com/en/{slug}" rel="canonical" />
    <meta content="{title}" property="og:title" />
    <meta content="{desc}" property="og:description" />
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


def navbar_block(slug, country_slug, page_flag):
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
                            <a class="dropdown-item" href="/fr/{slug}"><span class="fi fi-fr"></span> Fran&#231;ais</a>
                            <a class="dropdown-item" href="/es/{slug}"><span class="fi fi-es"></span> Espa&#241;ol</a>
                            <a class="dropdown-item" href="/pt/{slug}"><span class="fi fi-br"></span> Portugu&#234;s</a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>"""


def footer_block():
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


def internal_links(country_slug):
    return f"""<div class="mt-4 pt-3 border-top">
    <h3 class="h6">Related Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{country_slug}.html">Main {country_slug.replace('-', ' ').title()} Visa Guide</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="how-to-apply-evisa.html">How to Apply for an eVisa</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-documents-checklist.html">Visa Documents Checklist</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-processing-times.html">Visa Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-photo-requirements.html">Visa Photo Requirements</a>
</div>"""


def eeeat_block():
    return '<div class="alert alert-info small mt-4"><strong>Editorial note:</strong> Verified by our immigration team. Last updated: March 2026. Sources: official embassy websites.</div>'


def table_html(rows):
    rows_html = "\n".join(f"<tr><th>{r[0]}</th><td>{r[1]}</td></tr>" for r in rows)
    return f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts 2026</th></tr></thead>
<tbody>
{rows_html}
</tbody>
</table>"""


def sections_html(sections):
    parts = []
    for heading, body in sections:
        if body.strip().startswith("<"):
            parts.append(f'<h2 id="{heading.lower().replace(" ", "-").replace("&amp;", "").replace(",", "").replace("(", "").replace(")", "")[:40]}">{heading}</h2>\n{body}')
        else:
            parts.append(f'<h2 id="{heading.lower().replace(" ", "-").replace("&amp;", "").replace(",", "").replace("(", "").replace(")", "")[:40]}">{heading}</h2>\n<p>{body}</p>')
    return "\n\n".join(parts)


def faq_jsonld(name, qa_list):
    entities = []
    for q, a in qa_list:
        entities.append(
            f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        )
    return (
        '<script type="application/ld+json">\n'
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n'
        + ",\n".join(entities)
        + "\n]}\n</script>"
    )


def howto_jsonld(name, desc, steps):
    step_parts = []
    for i, (s_name, s_text) in enumerate(steps, 1):
        step_parts.append(
            f'{{"@type":"HowToStep","name":"Step {i}: {s_name}","text":"{s_text}"}}'
        )
    return (
        '<script type="application/ld+json">\n'
        f'{{"@context":"https://schema.org","@type":"HowTo","name":"{name}","description":"{desc}","step":[\n'
        + ",\n".join(step_parts)
        + "\n]}}\n</script>"
    )


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def build_requirements(country_slug, data):
    slug = f"{country_slug}-visa-requirements.html"
    flag = data["flag"]
    title = data["req_title"]
    desc = data["req_desc"]
    h1 = data["req_h1"]
    rows = data["req_table"]
    secs = data["req_sections"]
    name = data["name"]

    faq = faq_jsonld(title, [
        (f"What documents do I need for a {name} visa in 2026?",
         f"Key documents include: valid passport (6 months validity), completed application, passport photo, financial evidence, flight itinerary and accommodation booking. Check the official {data['evisa_url']} portal for the latest requirements."),
        (f"Do I need a visa to visit {name} in 2026?",
         f"Visa requirements vary by nationality. {name} offers: {data['evisa_cost']} for eligible travellers. Check the official portal for your nationality's specific requirements."),
        (f"How long can I stay in {name} with a tourist visa?",
         f"The standard tourist stay in {name} is {data['stay']}. Extensions may be possible — check with the immigration authority."),
        (f"Can I apply for a {name} visa online?",
         f"Yes, online applications are available at {data['evisa_url']}. Processing takes {data['processing']}. Ensure all documents are correct before submitting."),
    ])

    howto = howto_jsonld(
        f"How to Check {name} Visa Requirements in 2026",
        f"Step-by-step guide to verifying eligibility and gathering documents for a {name} visa application.",
        [
            ("Check eligibility", f"Visit {data['evisa_url']} to check whether your nationality requires a visa or qualifies for visa-free entry or an eVisa."),
            ("Determine the correct visa type", "Identify the right visa category for your trip (tourism, business, transit, etc.) and the corresponding requirements."),
            ("Gather required documents", "Collect all mandatory documents: valid passport, photos, financial proof, accommodation confirmation, travel insurance, and any supporting letters."),
            ("Complete the application form", "Fill in the official visa application form online. Double-check all information for accuracy before submission."),
            ("Submit and await decision", f"Submit your application with all documents and the applicable fee. Processing takes {data['processing']}. Track your application status online."),
        ]
    )

    html = (
        head_block(title, desc, slug, country_slug, flag) + "\n"
        + navbar_block(slug, country_slug, flag) + "\n"
        + f'<section class="ftco-section"><div class="container"><article>\n'
        + f'<h1><span class="fi fi-{flag}"></span> {h1}</h1>\n\n'
        + table_html(rows) + "\n\n"
        + sections_html(secs) + "\n\n"
        + eeeat_block() + "\n"
        + internal_links(country_slug) + "\n"
        + "</article></div></section>\n"
        + faq + "\n"
        + howto + "\n"
        + footer_block()
    )
    return slug, html


def build_fees(country_slug, data):
    slug = f"{country_slug}-visa-fees.html"
    flag = data["flag"]
    title = data["fees_title"]
    desc = data["fees_desc"]
    h1 = data["fees_h1"]
    rows = data["fees_table"]
    secs = data["fees_sections"]
    name = data["name"]

    faq = faq_jsonld(title, [
        (f"How much does a {name} visa cost in 2026?",
         f"The main visa option costs: {data['evisa_cost']}. Check {data['evisa_url']} for the latest official fee schedule."),
        (f"Are {name} visa fees refundable?",
         "Most visa fees are non-refundable once the application is submitted, even if the visa is denied. Always verify documentation before paying."),
        (f"What payment methods are accepted for {name} visa fees?",
         f"Online payments at {data['evisa_url']} typically accept Visa, Mastercard and similar major cards. Some consulates accept cash or bank draft — verify locally."),
        (f"Are there any hidden fees for a {name} visa?",
         "Always apply through the official government portal to avoid third-party surcharges. Official fees are published at the immigration authority website."),
    ])

    howto = howto_jsonld(
        f"How to Pay {name} Visa Fees in 2026",
        f"Step-by-step guide to understanding and paying {name} visa fees correctly.",
        [
            ("Check the official fee", f"Visit {data['evisa_url']} to confirm the current official visa fee for your nationality and visa type."),
            ("Prepare payment method", "Ensure you have a valid credit or debit card for online payment, or sufficient cash for consulate or on-arrival payment."),
            ("Apply through official channels only", f"Submit your application at {data['evisa_url']} or the official embassy/consulate to avoid inflated third-party fees."),
            ("Complete payment securely", "Enter your card details on the official secure government portal. Retain the payment receipt or confirmation number."),
            ("Save your confirmation", "Download and save your payment receipt and visa/approval document for presentation at immigration."),
        ]
    )

    html = (
        head_block(title, desc, slug, country_slug, flag) + "\n"
        + navbar_block(slug, country_slug, flag) + "\n"
        + f'<section class="ftco-section"><div class="container"><article>\n'
        + f'<h1><span class="fi fi-{flag}"></span> {h1}</h1>\n\n'
        + table_html(rows) + "\n\n"
        + sections_html(secs) + "\n\n"
        + eeeat_block() + "\n"
        + internal_links(country_slug) + "\n"
        + "</article></div></section>\n"
        + faq + "\n"
        + howto + "\n"
        + footer_block()
    )
    return slug, html


def build_processing(country_slug, data):
    slug = f"{country_slug}-visa-processing-time.html"
    flag = data["flag"]
    title = data["proc_title"]
    desc = data["proc_desc"]
    h1 = data["proc_h1"]
    rows = data["proc_table"]
    secs = data["proc_sections"]
    name = data["name"]

    faq = faq_jsonld(title, [
        (f"How long does a {name} visa take to process in 2026?",
         f"Processing time for the main {name} visa option is {data['processing']}. Embassy/consulate applications may take longer."),
        (f"Can I get a {name} visa processed urgently?",
         "Some consulates offer express or urgent processing for an additional fee. Check with your nearest diplomatic mission for availability and surcharges."),
        (f"What can delay my {name} visa application?",
         "Common delays include incomplete documents, incorrect photos, peak holiday periods, and background check requirements. Submit a complete application to minimise delays."),
        (f"How do I track my {name} visa application status?",
         f"You can track your application status at {data['evisa_url']} using your application reference number. Check your email regularly for notifications."),
    ])

    howto = howto_jsonld(
        f"How to Ensure Fast {name} Visa Processing in 2026",
        f"Step-by-step guide to submitting a complete {name} visa application and getting the fastest possible decision.",
        [
            ("Gather all documents in advance", "Collect passport, photo, financial evidence, flight itinerary and accommodation booking before starting the application."),
            ("Apply early", f"Submit your application at least 2 weeks before travel. Processing takes {data['processing']} under normal conditions."),
            ("Use official channels", f"Apply at {data['evisa_url']} or through the official embassy/consulate to avoid third-party delays."),
            ("Double-check all information", "Review all personal details, dates and passport numbers carefully before submitting — errors cause rejections and delays."),
            ("Monitor your application", "Check your email and application portal regularly for status updates or requests for additional documentation."),
        ]
    )

    html = (
        head_block(title, desc, slug, country_slug, flag) + "\n"
        + navbar_block(slug, country_slug, flag) + "\n"
        + f'<section class="ftco-section"><div class="container"><article>\n'
        + f'<h1><span class="fi fi-{flag}"></span> {h1}</h1>\n\n'
        + table_html(rows) + "\n\n"
        + sections_html(secs) + "\n\n"
        + eeeat_block() + "\n"
        + internal_links(country_slug) + "\n"
        + "</article></div></section>\n"
        + faq + "\n"
        + howto + "\n"
        + footer_block()
    )
    return slug, html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for country_slug, data in COUNTRIES.items():
        for builder in (build_requirements, build_fees, build_processing):
            slug, html = builder(country_slug, data)
            path = os.path.join(OUT_DIR, slug)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(slug)
            print(f"  Created: {slug}")

    print(f"\nTotal files created: {len(created)}")
    assert len(created) == 30, f"Expected 30 files, got {len(created)}"
    print("All 30 files confirmed.")


if __name__ == "__main__":
    main()
