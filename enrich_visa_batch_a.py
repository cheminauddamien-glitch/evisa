#!/usr/bin/env python
"""
Enrich visa country pages (A through I) with 5 detailed sections:
1. Complete Visa Categories (id="all-visas")
2. Processing Times & Fees (id="processing")
3. Health & Entry Requirements (id="health-requirements")
4. Visa Extension & Overstay (id="extension")
5. Refusal & Appeals (id="refusal")

Idempotent: skips files that already contain id="all-visas".
"""

import os, re

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "en")

TARGET_FILES = [
    "visa-andorra", "visa-angola", "visa-argentina", "visa-australia",
    "visa-austria", "visa-bahamas", "visa-bahrain", "visa-belgium",
    "visa-belize", "visa-bermuda", "visa-bhutan", "visa-brazil",
    "visa-brunei", "visa-bulgaria", "visa-cambodia", "visa-canada",
    "visa-cape-verde", "visa-chile", "visa-china", "visa-colombia",
    "visa-cook-islands", "visa-costa-rica", "visa-croatia", "visa-cyprus",
    "visa-czech-republic", "visa-denmark", "visa-ecuador", "visa-egypt",
    "visa-fiji", "visa-finland", "visa-france", "visa-georgia",
    "visa-germany", "visa-greece", "visa-guatemala", "visa-hong-kong",
    "visa-hungary", "visa-iceland", "visa-india", "visa-indonesia",
    "visa-iran", "visa-iraq", "visa-ireland", "visa-israel", "visa-italy",
]

# ── Country-specific data ─────────────────────────────────────────────────────
COUNTRY_DATA = {
    "visa-andorra": {
        "name": "Andorra",
        "visa_types": [
            ("Tourist Entry (via Schengen)", "Up to 90 days", "Free (Schengen visa fee applies)", "Valid passport, Schengen visa if required"),
            ("Business Visit", "Up to 90 days", "Free", "Business invitation, passport, Schengen visa"),
            ("Work Permit (Autorització de treball)", "1 year, renewable", "EUR 100-200", "Job contract, employer sponsorship, medical exam"),
            ("Self-Employed Permit", "1 year, renewable", "EUR 200", "Business plan, proof of investment EUR 40,000+"),
            ("Student Residence", "1 year, renewable", "EUR 100", "Enrollment letter, financial proof, insurance"),
            ("Family Reunification", "1 year, renewable", "EUR 100", "Proof of relationship, sponsor's residence permit"),
            ("Investor Residence (Residència passiva)", "2 years, renewable", "EUR 1,000-2,000", "Investment of EUR 600,000+ in Andorran assets"),
            ("Retirement Residence", "2 years, renewable", "EUR 1,000", "Proof of income, health insurance, clean record"),
            ("Temporary Residence", "1 year", "EUR 100", "Proof of means, accommodation, insurance"),
            ("Professional Residence", "1 year, renewable", "EUR 150", "Qualification proof, employer contract"),
        ],
        "processing": [
            ("Tourist/Schengen", "3-5 days", "EUR 80", "1-2 days", "EUR 160"),
            ("Work Permit", "4-8 weeks", "EUR 100", "2-3 weeks", "EUR 200"),
            ("Investor Residence", "6-10 weeks", "EUR 1,500", "3-4 weeks", "EUR 2,500"),
            ("Student Residence", "3-6 weeks", "EUR 100", "1-2 weeks", "EUR 180"),
            ("Family Reunification", "4-8 weeks", "EUR 100", "2-3 weeks", "EUR 200"),
        ],
        "health": "Andorra does not require mandatory vaccinations for entry. However, COVID-19 vaccination certificates may be requested depending on the current health situation. Since access is only through France or Spain, travelers must also comply with Schengen zone health regulations. No mandatory medical exams are required for short-stay visitors. Long-term residents applying for work or investment permits must undergo a medical examination by an approved physician in Andorra, including a general health check, chest X-ray, and blood tests. Travel health insurance is strongly recommended and may be required for residence permits. Police clearance certificates from your country of residence (less than 3 months old) are required for all residence permit applications. Biometric data collection is not currently part of Andorra's entry process, but Schengen biometric requirements apply when entering through France or Spain.",
        "extension": "Tourist stays in Andorra are limited to 90 days within any 180-day period. Extensions beyond 90 days are not generally available for tourists — you must apply for a residence permit instead. Andorra does not issue visa extensions for short-stay visitors. For residence permit holders, renewals must be submitted 30-60 days before expiry at the Servei d'Immigració. Maximum continuous stay without residence authorization is 90 days. Overstay penalties include fines ranging from EUR 300 to EUR 3,000, possible detention, and deportation. Repeat offenders may face entry bans of 1-5 years. Andorran authorities are strict about unauthorized stays, and overstaying can result in difficulties obtaining future Schengen visas since you must transit through the Schengen area to leave Andorra. All overstay cases are recorded in immigration databases.",
        "refusal": "Andorra residence permit applications can be refused for several reasons: incomplete documentation, insufficient financial means (below the required threshold of 300% of Andorra's minimum wage for passive residence), criminal record, previous immigration violations, or failure to meet health requirements. The refusal notification is provided in writing and includes the specific grounds for denial. Applicants have the right to appeal within 30 days of notification through the Andorran administrative tribunal (Batllia d'Andorra). The appeal must be filed in writing with supporting documentation addressing the refusal reasons. Reapplication is permitted after 6 months if the previous grounds for refusal have been resolved. Legal representation is recommended for appeals. A second refusal can be appealed to the Superior Court of Justice of Andorra (Tribunal Superior de Justícia). Processing times for appeals typically range from 2-4 months.",
    },
    "visa-angola": {
        "name": "Angola",
        "visa_types": [
            ("Tourist Visa (Visto de Turismo)", "30 days", "USD 120", "Passport, hotel booking, return ticket, financial proof"),
            ("Business Visa (Visto de Negócios)", "30-60 days", "USD 200", "Business invitation from Angolan company, passport, company letter"),
            ("Work Visa (Visto de Trabalho)", "1 year, renewable", "USD 300-500", "Employment contract, employer sponsorship, medical certificate"),
            ("Student Visa (Visto de Estudante)", "1 year, renewable", "USD 150", "Acceptance letter, financial proof, police clearance"),
            ("Transit Visa (Visto de Trânsito)", "5 days", "USD 40", "Passport, confirmed onward ticket, visa for next destination"),
            ("Family Reunification Visa", "1 year", "USD 200", "Marriage certificate or birth certificate, sponsor proof"),
            ("Investor Visa (Visto de Investidor)", "2 years, renewable", "USD 500", "Investment plan, minimum USD 500,000 capital, company registration"),
            ("Diplomatic/Official Visa", "Varies", "Free", "Diplomatic passport, official letter from government"),
            ("Privileged Visa (Visto Privilegiado)", "2 years", "USD 2,500", "Major investment or special contribution to Angola"),
            ("Temporary Stay Visa", "90 days", "USD 150", "Proof of purpose, financial means, accommodation proof"),
        ],
        "processing": [
            ("Tourist Visa", "5-10 business days", "USD 120", "2-3 days", "USD 200"),
            ("Business Visa", "5-15 business days", "USD 200", "2-3 days", "USD 350"),
            ("Work Visa", "4-8 weeks", "USD 400", "2-3 weeks", "USD 600"),
            ("Student Visa", "3-6 weeks", "USD 150", "1-2 weeks", "USD 250"),
            ("Transit Visa", "2-3 days", "USD 40", "Same day", "USD 80"),
        ],
        "health": "Angola requires a valid Yellow Fever vaccination certificate (International Certificate of Vaccination or Prophylaxis) for all travelers arriving from or transiting through yellow fever endemic areas, and it is strongly recommended for all travelers regardless of origin. Malaria prophylaxis is strongly advised as Angola is a high-risk malaria zone. No routine medical exam is required for tourist visas, but work and residence visa applicants must submit a medical certificate from an approved physician confirming they are free from communicable diseases. The medical certificate must include HIV/AIDS testing, tuberculosis screening via chest X-ray, and hepatitis B/C tests. Health insurance is mandatory for all visa applicants and must cover emergency medical treatment and repatriation. A police clearance certificate (Certificado de Registo Criminal) from your country of residence is required for work, student, and residence visas. Biometric data (fingerprints and photograph) are collected at immigration upon arrival. Travelers should ensure routine vaccinations are up to date, including hepatitis A, typhoid, and polio.",
        "extension": "Tourist visas can be extended once for an additional 30 days at the SME (Serviço de Migração e Estrangeiros) office in Luanda or provincial capitals. The extension fee is approximately USD 100. Apply at least 5 days before your current visa expires. Work and residence permits are renewable 60 days before expiry. Maximum tourist stay is 60 days total (30 + 30 extension). Overstay penalties are severe: fines of USD 75-150 per day of overstay, immediate detention, deportation at the violator's expense, and entry bans of 2-5 years. Repeat offenders face criminal prosecution and possible imprisonment of up to 1 year. Angola's SME maintains strict records of all immigration violations. Travelers who overstay may also be blacklisted from future visa applications across SADC member states.",
        "refusal": "Common reasons for Angolan visa refusal include: incomplete or inconsistent documentation, insufficient financial means, lack of a valid return ticket, no hotel reservation, criminal record, previous overstays or deportations, and failure to provide a valid yellow fever certificate. Refusal is communicated in writing through the consulate or the SME. Applicants can appeal within 15 days of the refusal notification by submitting a written appeal to the Director of the SME with additional supporting documents. Legal representation through an Angolan-licensed attorney is recommended. The appeal process typically takes 4-8 weeks. Reapplication is allowed immediately after addressing the refusal grounds, though waiting 3-6 months with stronger documentation is advisable. A second refusal can be challenged through Angola's administrative courts. Visa refusal does not automatically result in a ban, but multiple refusals may lead to closer scrutiny on future applications.",
    },
    "visa-argentina": {
        "name": "Argentina",
        "visa_types": [
            ("Tourist Visa (Turismo)", "90 days", "USD 150", "Passport, return ticket, hotel booking, financial proof"),
            ("Business Visa (Negocios)", "90 days", "USD 150", "Business invitation, company letter, passport"),
            ("Work Visa (Residencia Temporaria por Trabajo)", "1 year, renewable", "USD 300", "Employment contract, RENURE registration, medical cert"),
            ("Student Visa (Residencia Temporaria por Estudios)", "1-2 years", "USD 200", "University acceptance, financial proof, insurance"),
            ("Transit Visa", "Up to 72 hours", "USD 50", "Passport, onward ticket"),
            ("Family Reunification (Reunificación Familiar)", "1-2 years", "USD 200", "Proof of relationship, sponsor's DNI, financial proof"),
            ("Investor/Entrepreneur Visa (Rentista)", "1 year, renewable", "USD 300-500", "Proof of investment, business plan, minimum capital"),
            ("Retirement Visa (Pensionado)", "1 year, renewable", "USD 200", "Proof of pension income USD 2,500+/month, insurance"),
            ("MERCOSUR Residence", "2 years, then permanent", "USD 100", "MERCOSUR country passport, clean criminal record"),
            ("Digital Nomad Visa (Nómada Digital)", "6 months, renewable once", "USD 200", "Remote employment proof, income USD 1,500+/month"),
        ],
        "processing": [
            ("Tourist Visa", "5-15 business days", "USD 150", "2-3 days", "USD 250"),
            ("Business Visa", "5-10 business days", "USD 150", "2-3 days", "USD 250"),
            ("Work Visa", "4-12 weeks", "USD 300", "2-4 weeks", "USD 500"),
            ("Student Visa", "3-6 weeks", "USD 200", "1-2 weeks", "USD 350"),
            ("Digital Nomad Visa", "2-4 weeks", "USD 200", "1 week", "USD 350"),
        ],
        "health": "Argentina does not require mandatory vaccinations for entry from most countries. However, a Yellow Fever vaccination certificate is required for travelers arriving from or having transited through yellow fever endemic countries in Africa and South America. Travelers visiting the northern provinces (Misiones, Corrientes) where there is a risk of yellow fever are strongly advised to get vaccinated. No medical examination is required for tourist or business visas. Work and residence visa applicants must undergo a medical examination at a hospital in Argentina or at an authorized clinic, including chest X-ray and blood tests for HIV, syphilis, and Chagas disease. Health insurance is recommended but not legally mandatory for tourists; however, it is required for digital nomad visa applicants and recommended for all long-stay visa holders. Police clearance certificates (apostilled and translated into Spanish) from all countries of residence in the last 5 years are required for residence visa applications. Argentina does not currently collect biometric data at its borders, though passport scanning is standard procedure.",
        "extension": "Tourist visas can be extended once for an additional 90 days at the Dirección Nacional de Migraciones office. The extension fee is approximately ARS 10,000 (subject to change). Apply at least 10 days before your visa expires. Many travelers do a 'border run' to Uruguay or Chile to reset their 90-day tourist stay, which is permitted but immigration may question frequent re-entries. Maximum tourist stay is 90 days per entry (180 with extension). Residence permit renewals must be filed 60-90 days before expiry. Overstay penalties include fines of approximately ARS 10,000-50,000, possible deportation, and entry bans of 1-5 years. Argentina is generally lenient with short overstays (a few days), but longer overstays result in increasing fines calculated per day. Deportation costs are borne by the traveler. Overstay records can affect future visa applications to Argentina and other countries.",
        "refusal": "Argentine visa applications may be refused due to incomplete documentation, insufficient financial means (failure to prove adequate funds for the duration of stay), criminal record, previous deportations or immigration violations, public health concerns, or national security considerations. Refusal is communicated by the consulate with reasons stated. Applicants can submit a reconsideration request (recurso de reconsideración) within 10 business days to the same consulate. If denied again, a hierarchical appeal (recurso jerárquico) can be filed within 15 days to the Dirección Nacional de Migraciones. Reapplication is permitted immediately with corrected documentation, though waiting at least 30 days is recommended. Legal representation through an Argentine immigration attorney (abogado de migraciones) is advisable for appeals. The appeal process typically takes 2-6 months. MERCOSUR citizens have stronger appeal rights and rarely face visa refusals due to regional freedom of movement agreements.",
    },
    "visa-australia": {
        "name": "Australia",
        "visa_types": [
            ("ETA (subclass 601)", "Up to 3 months", "AUD 20", "Eligible passport, no criminal record"),
            ("eVisitor (subclass 651)", "Up to 3 months", "Free", "EU/EEA passport holders"),
            ("Visitor Visa (subclass 600)", "3-12 months", "AUD 190-1,120", "Financial proof, health insurance, return ticket"),
            ("Business Innovation (subclass 188)", "4 years", "AUD 6,240", "Business plan, net assets AUD 1.25M+, state nomination"),
            ("Work & Holiday Visa (subclass 462)", "1 year", "AUD 635", "Age 18-30, bilateral agreement country, sufficient funds"),
            ("Working Holiday Visa (subclass 417)", "1 year", "AUD 635", "Age 18-30, eligible country, sufficient funds AUD 5,000"),
            ("Student Visa (subclass 500)", "Duration of studies", "AUD 710", "CoE from registered institution, financial capacity, OSHC"),
            ("Skilled Worker (subclass 482)", "2-4 years", "AUD 1,455-3,035", "Employer sponsorship, skills assessment, English proficiency"),
            ("Partner Visa (subclass 820/801)", "Temporary then permanent", "AUD 8,850", "Genuine relationship proof, health & character checks"),
            ("Global Talent Visa (subclass 858)", "Permanent", "AUD 4,640", "Exceptional talent, nominator, high income threshold"),
        ],
        "processing": [
            ("ETA (subclass 601)", "Minutes to 24 hours", "AUD 20", "N/A", "N/A"),
            ("eVisitor (subclass 651)", "Minutes to 1 day", "Free", "N/A", "N/A"),
            ("Visitor Visa (subclass 600)", "1-4 weeks", "AUD 190", "N/A", "N/A"),
            ("Student Visa (subclass 500)", "4-12 weeks", "AUD 710", "Priority: 2-4 weeks", "AUD 710"),
            ("Working Holiday (subclass 417)", "1-4 weeks", "AUD 635", "N/A", "N/A"),
        ],
        "health": "Australia has strict health requirements for visa applicants. All visa applicants may be required to undergo a health examination depending on their visa type and length of stay. Applicants intending to stay more than 3 months must typically complete a health examination by a Bupa Medical Visa Services (BVMS) panel physician. The examination includes a chest X-ray (for applicants over 11 years), a general physical examination, and additional tests as required (HIV, hepatitis B/C for certain nationalities or occupations). Student visa holders must have Overseas Student Health Cover (OSHC) for the entire duration of their stay. Travelers are not required to show proof of specific vaccinations for entry, though Australia recommends routine immunizations. Yellow fever vaccination is required if arriving from or transiting through a declared yellow fever area. Australia does not require COVID-19 vaccination for entry. Police clearance certificates from all countries where the applicant has lived for 12 months or more in the last 10 years are required for most visa types. Biometric data (fingerprints and photograph) may be collected depending on the applicant's nationality, with mandatory biometrics collection expanding progressively.",
        "extension": "ETA and eVisitor holders cannot extend their stay — they must leave Australia before their authorized stay expires and may apply for a new visa from outside Australia. Visitor Visa (subclass 600) holders may apply for a further stay from within Australia if they hold a visa with 'no further stay' condition waiver. The maximum total stay for tourists is generally 12 months. Student visa holders can extend by applying for a new Student Visa if they change or continue studies. Work visa holders can apply for visa renewal through their employer sponsor. Overstay consequences in Australia are severe: individuals become 'unlawful non-citizens' the moment their visa expires, face mandatory detention and removal, a 3-year re-entry ban (exclusion period), and potential lifetime bans for overstays exceeding 28 days. Voluntary departure before detection may reduce penalties. Overstayers cannot apply for most visas from within Australia. The Department of Home Affairs actively tracks visa compliance.",
        "refusal": "Australian visa refusals are common and typically result from: failing the Genuine Temporary Entrant (GTE) test, insufficient financial evidence, inadequate English proficiency, health or character concerns, incomplete documentation, or previous immigration violations. Refusal decisions are provided in writing with detailed reasons. Applicants may seek merits review through the Administrative Appeals Tribunal (AAT) within 21 days of refusal for onshore applications or 28 days for offshore applications. The AAT fee is approximately AUD 3,374 (refundable if the decision is overturned). Judicial review through the Federal Circuit Court is available for legal errors. Ministerial intervention (section 351 or 417) is a last resort. Reapplication is possible at any time but is not recommended without addressing the refusal reasons. Engaging a registered migration agent (MARA-registered) is strongly advised for complex cases. Student visa refusals can also be appealed if the applicant is in Australia at the time of refusal.",
    },
    "visa-austria": {
        "name": "Austria",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, travel insurance, hotel booking, financial proof"),
            ("National Visa (D-type)", "91-180 days", "EUR 150", "Purpose documentation, financial proof, insurance"),
            ("Work Visa (Rot-Weiß-Rot Karte)", "2 years", "EUR 160", "Job offer, qualification proof, points system, employer filing"),
            ("EU Blue Card", "2 years, renewable", "EUR 160", "Salary 1.5x average, university degree, employer contract"),
            ("Student Visa (Aufenthaltsbewilligung Studierender)", "1 year, renewable", "EUR 160", "University admission, EUR 12,000/year proof, insurance"),
            ("Family Reunification Visa", "1 year, renewable", "EUR 160", "Proof of relationship, sponsor income, German A1 level"),
            ("Investor/Entrepreneur Visa", "2 years", "EUR 160-300", "Business plan, capital proof, economic benefit to Austria"),
            ("Researcher Visa (Aufenthaltsbewilligung Forscher)", "2 years", "EUR 160", "Hosting agreement from research institution"),
            ("Artist Visa", "1-2 years", "EUR 160", "Proof of artistic activity, contracts, financial means"),
            ("Job Seeker Visa (Jobsuche)", "6 months", "EUR 160", "Degree, German B1 or English B2, EUR 12,000 savings"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "3-8 weeks", "EUR 150", "1-2 weeks", "EUR 250"),
            ("Rot-Weiß-Rot Karte", "6-12 weeks", "EUR 160", "4-6 weeks", "EUR 250"),
            ("Student Visa", "4-8 weeks", "EUR 160", "2-3 weeks", "EUR 250"),
            ("Family Reunification", "3-6 months", "EUR 160", "2-3 months", "EUR 250"),
        ],
        "health": "Austria and the Schengen Area require travel medical insurance with a minimum coverage of EUR 30,000 for short-stay visa applicants, covering medical emergencies, hospitalization, and repatriation. No mandatory vaccinations are required for entry into Austria. Long-stay visa and residence permit applicants must undergo a medical examination by an approved physician (Amtsarzt), including a general health check, chest X-ray for tuberculosis screening, and blood tests. Health insurance (either Austrian statutory insurance through employment or private health insurance meeting minimum standards) is mandatory for all residence permit holders. EU/EEA citizens can use their European Health Insurance Card (EHIC). Police clearance certificates from all countries of residence in the past 5 years must be apostilled and translated into German by a certified translator. Biometric data (10 fingerprints and a digital photograph) are collected as part of the VIS (Visa Information System) for all Schengen visa applications at the Austrian embassy or VFS Global center.",
        "extension": "Schengen short-stay visas allow a maximum of 90 days within any 180-day period across the entire Schengen Area and generally cannot be extended except in exceptional circumstances (force majeure, humanitarian reasons, serious personal reasons) at the BFA (Federal Office for Immigration and Asylum). National D-type visas can be converted to a residence permit by applying at the MA35 (in Vienna) or the relevant regional authority (Bezirkshauptmannschaft) before the visa expires. Residence permits must be renewed 3 months before expiry. Overstay penalties include fines of EUR 500-5,000, detention pending deportation, deportation at the violator's expense, and entry bans of 1-5 years across the entire Schengen Area (recorded in the SIS database). Austria is strict about enforcement, and any Schengen overstay is visible to all 27 Schengen member states. Repeat offenders face criminal prosecution and longer entry bans.",
        "refusal": "Austrian visa refusals may be based on: insufficient travel insurance, inadequate financial proof, incomplete documentation, doubts about the purpose of travel or intention to return, previous Schengen violations, security concerns, or failure to meet specific visa type requirements (e.g., points threshold for Rot-Weiß-Rot Karte). The refusal is issued on a standardized Schengen refusal form citing specific reasons from the Schengen Visa Code. Applicants can appeal within 4 weeks to the Federal Administrative Court (Bundesverwaltungsgericht). For Schengen C-type visas, the appeal must cite legal errors or procedural violations. For national visas and residence permits, the appeal process is more comprehensive. Reapplication is permitted immediately with improved documentation. Legal representation through an Austrian immigration attorney (Rechtsanwalt für Fremdenrecht) is recommended. Appeal decisions are typically rendered within 3-6 months. VFS Global application centers can provide guidance on common refusal reasons.",
    },
    "visa-bahamas": {
        "name": "Bahamas",
        "visa_types": [
            ("Tourist Visa", "90 days", "USD 100", "Passport, return ticket, accommodation proof, financial proof"),
            ("Business Visa", "30 days", "USD 100", "Business invitation, company letter, passport"),
            ("Work Permit", "1 year, renewable", "USD 500-25,000", "Job offer, employer application, immigration fees vary by role"),
            ("Student Visa", "Duration of studies", "USD 200", "Acceptance letter, financial proof, health insurance"),
            ("Spousal Permit", "1 year, renewable", "USD 500", "Marriage certificate, sponsor's permanent residency/citizenship"),
            ("Permanent Residence", "Indefinite", "USD 1,000-10,000", "Investment, clean record, 10+ years legal residence or investment"),
            ("BEATS (Extended Access Travel Stay)", "1 year", "USD 25/week", "Remote worker/digital nomad, proof of employment, insurance"),
            ("Annual Homeowner Permit", "1 year", "Free-USD 500", "Property ownership in Bahamas, proof of ownership"),
            ("Transit Visa", "Up to 48 hours", "USD 50", "Valid passport, onward ticket"),
            ("Investor Permanent Residence", "Permanent", "USD 1,000+", "Investment of BSD 500,000+ in Bahamas, police clearance"),
        ],
        "processing": [
            ("Tourist Visa", "3-5 business days", "USD 100", "1-2 days", "USD 175"),
            ("Work Permit", "4-12 weeks", "USD 500-25,000", "2-4 weeks", "Additional 50%"),
            ("Student Visa", "2-4 weeks", "USD 200", "1 week", "USD 350"),
            ("BEATS Program", "5-10 business days", "USD 25/week", "2-3 days", "USD 50/week"),
            ("Permanent Residence", "6-12 months", "USD 1,000-10,000", "3-6 months", "Additional fees"),
        ],
        "health": "The Bahamas does not require mandatory vaccinations for entry from most countries. However, a Yellow Fever vaccination certificate is required for travelers arriving from countries with risk of yellow fever transmission. COVID-19 vaccination may be recommended depending on current health advisories. No medical examination is required for tourist or business visas. Work permit and permanent residence applicants must undergo a medical examination at an approved clinic in the Bahamas or their home country, including chest X-ray, blood work (HIV, hepatitis), and a general physical exam. Health insurance is strongly recommended for all visitors and is required for the BEATS program participants. Proof of adequate health insurance covering hospitalization and medical evacuation is mandatory for long-stay visa holders. Police clearance certificates from all countries of residence are required for work permits and permanent residence applications. The Bahamas Immigration Department collects biometric data (fingerprints and photographs) at ports of entry for all foreign nationals.",
        "extension": "Tourist visas can be extended for additional periods at the Bahamas Immigration Department in Nassau, up to a maximum total stay of 8 months. Extension fee is approximately USD 100 per extension. Applications should be submitted at least 1 week before the current visa expires. Work permits are renewable annually through the employer. BEATS program membership can be renewed for additional years. Overstay penalties include fines of BSD 300-500 per occurrence, detention, deportation (at the violator's expense), and potential entry bans of 1-3 years. Unauthorized employment without a valid work permit carries fines of BSD 5,000-10,000 and/or imprisonment of up to 1 year. The Bahamas takes immigration enforcement seriously, with regular workplace raids and deportation operations. Overstayers may be housed at the Carmichael Road Detention Centre pending deportation.",
        "refusal": "Bahamas visa refusals commonly result from: insufficient financial evidence, incomplete applications, criminal records, previous deportations or immigration violations, inability to demonstrate ties to home country, or health concerns. The refusal is communicated by the consulate or at the port of entry. Applicants refused at the port of entry may be placed on the next available flight home. For consular refusals, applicants may request reconsideration by writing to the Director of Immigration with additional supporting documents. There is no formal appeal tribunal, but ministerial discretion can be exercised in exceptional cases. Reapplication is permitted after 3 months with improved documentation. Port-of-entry refusals may result in a note on the traveler's immigration file. Legal assistance from a Bahamian immigration attorney is recommended for complex cases. The decision process for reconsideration typically takes 4-8 weeks.",
    },
    "visa-bahrain": {
        "name": "Bahrain",
        "visa_types": [
            ("eVisa (Tourist)", "14-30 days", "BHD 9-25 (USD 24-66)", "Passport, hotel booking, return ticket"),
            ("Visa on Arrival", "14 days", "BHD 5 (USD 13)", "Eligible nationalities, passport, return ticket"),
            ("Business Visa", "30 days, extendable", "BHD 25 (USD 66)", "Business invitation, company letter, passport"),
            ("Work Visa (Flexi Permit)", "1 year", "BHD 500 (USD 1,326)", "Self-sponsored, LMRA registration, medical"),
            ("Sponsored Work Visa", "2 years, renewable", "BHD 200 (USD 530)", "Employer sponsorship, labor approval, medical exam"),
            ("Student Visa", "Duration of studies", "BHD 25 (USD 66)", "University acceptance letter, financial proof"),
            ("Family Visit Visa", "30 days", "BHD 25 (USD 66)", "Sponsor letter, relationship proof, financial proof"),
            ("Family Residence Visa", "1 year, renewable", "BHD 100 (USD 265)", "Sponsor income threshold, relationship proof"),
            ("Golden Residency Visa", "10 years", "BHD 1,000+ (USD 2,650+)", "Investment, real estate, or exceptional talent"),
            ("Transit Visa", "48-72 hours", "Free-BHD 5", "Onward ticket, passport"),
        ],
        "processing": [
            ("eVisa Tourist", "1-3 business days", "BHD 9-25", "Same day (online)", "N/A"),
            ("Business Visa", "3-7 business days", "BHD 25", "1-2 days", "BHD 50"),
            ("Work Visa", "2-6 weeks", "BHD 200-500", "1-2 weeks", "BHD 350-750"),
            ("Student Visa", "2-4 weeks", "BHD 25", "1 week", "BHD 50"),
            ("Golden Residency", "4-8 weeks", "BHD 1,000+", "2-3 weeks", "BHD 1,500+"),
        ],
        "health": "Bahrain requires medical examinations for all work and residence visa applicants. The medical test must be conducted at approved health centers in Bahrain and includes blood tests for HIV, hepatitis B and C, syphilis, and tuberculosis (chest X-ray). Applicants testing positive for HIV or active TB will have their visa applications denied. No mandatory vaccinations are required for tourist entry from most countries. A Yellow Fever vaccination certificate is required for travelers from yellow fever endemic areas. COVID-19 vaccination requirements are regularly updated via the Bahrain Ministry of Health. Travel health insurance is recommended for all visitors. Work visa holders are covered under Bahrain's Social Insurance Organization (SIO) health scheme. Family visa applicants must show proof of adequate health insurance coverage for dependents. Police clearance certificates (good conduct certificates) from the applicant's home country are required for work and residence visas. Biometric data (fingerprints and iris scans) are collected at all Bahrain ports of entry for foreign nationals.",
        "extension": "Tourist eVisas can be extended for an additional 14-30 days through the online eVisa portal or at the Nationality, Passports and Residence Affairs (NPRA) office. The extension fee is approximately BHD 25. Work visas are renewed through the employer and the Labour Market Regulatory Authority (LMRA). Family residence visas are renewed annually. Maximum tourist stay is 90 days with extensions. Overstay penalties in Bahrain are strict: fines of BHD 10-50 per week of overstay, detention at the deportation center, deportation at the violator's expense, and entry bans of 1-5 years. Accumulated overstay fines can become substantial. Bahrain conducts regular sweeps targeting illegal workers and overstayers. An amnesty period may occasionally be offered allowing overstayers to leave without penalty. Employers who facilitate visa violations face fines and potential business license revocation.",
        "refusal": "Bahrain visa refusals may occur due to: incomplete applications, insufficient financial proof, criminal record, security concerns, previous overstays or deportations, failure of medical examination, or being on a GCC-wide blacklist. eVisa refusals are communicated online with brief reasons. Applicants can reapply immediately with corrected documentation for eVisas. For work and residence visa refusals, the sponsor/employer can file a reconsideration request with the NPRA within 30 days. Appeals for refusals based on security grounds are typically not accepted. Legal challenges can be filed through Bahrain's administrative courts. Reapplication is generally possible after 3-6 months. GCC nationals rarely face visa issues due to free movement agreements. Engaging a Bahrain-based PRO (Public Relations Officer) or immigration consultant is advisable for complex work visa cases. Medical refusals require new testing after treatment.",
    },
    "visa-belgium": {
        "name": "Belgium",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, travel insurance EUR 30k, hotel, financial proof"),
            ("National Visa (D-type)", "Over 90 days", "EUR 180-350", "Purpose documentation, financial proof, accommodation"),
            ("Work Permit B (Single Permit)", "1 year, renewable", "EUR 180-350", "Employer application, labor market test, qualification proof"),
            ("EU Blue Card", "13 months, renewable", "EUR 180-350", "Salary threshold EUR 57,000+, degree, employer contract"),
            ("Student Visa", "1 year, renewable", "EUR 180-350", "University enrollment, EUR 730/month proof, insurance"),
            ("Family Reunification", "1 year, renewable", "EUR 180-350", "Proof of relationship, sponsor income, A1 language proof"),
            ("Self-Employed/Business Visa", "1 year, renewable", "EUR 180-350", "Professional card, business plan, financial proof"),
            ("Au Pair Visa", "1 year", "EUR 180", "Au pair contract, host family, age 18-25"),
            ("Researcher Visa", "1 year, renewable", "EUR 180-350", "Hosting agreement, research contract"),
            ("Humanitarian Visa", "Varies", "Free-EUR 180", "Humanitarian grounds, protection application"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "4-12 weeks", "EUR 180-350", "2-4 weeks", "Additional EUR 100"),
            ("Single Permit (Work)", "4-6 months", "EUR 180-350", "N/A (fixed process)", "N/A"),
            ("Student Visa", "4-8 weeks", "EUR 180-350", "2-3 weeks", "Additional EUR 100"),
            ("Family Reunification", "4-9 months", "EUR 180-350", "N/A", "N/A"),
        ],
        "health": "Belgium requires travel medical insurance with minimum coverage of EUR 30,000 for all Schengen short-stay visa applicants, covering emergency medical expenses, hospitalization, and repatriation. No mandatory vaccinations are required for entry. Long-stay visa and residence permit applicants must undergo a medical examination by a certified physician, including a chest X-ray for tuberculosis screening. Belgian mutual health insurance (mutualité/mutualiteit) enrollment is mandatory for all residents and workers. Students must have adequate health insurance, either through the Belgian public system or approved private insurance. Police clearance certificates (extrait de casier judiciaire) from all countries of residence in the last 5 years are required for D-type visas, and must be apostilled and translated into French, Dutch, or German by a sworn translator. Biometric data (10 fingerprints and digital photograph) are collected at VFS Global or Belgian embassy for all Schengen visa applicants as part of the VIS system. Additional biometric data is collected for Belgian residence cards.",
        "extension": "Schengen short-stay visas allow 90 days within 180 days across the entire Schengen Area. Extensions are only possible in exceptional circumstances at the commune/gemeente or Immigration Office (Office des Étrangers/Dienst Vreemdelingenzaken). D-type visa holders must register at their local commune within 8 working days of arrival and obtain their Belgian residence card. Residence permits must be renewed 2-3 months before expiry. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines of EUR 200-5,000, an order to leave (Ordre de Quitter le Territoire), forced removal, and Schengen-wide entry bans of 1-5 years recorded in the SIS II database. Belgium actively enforces immigration law through the Immigration Office and police. Overstayers may be detained at closed immigration centers pending removal. Regularization through Article 9bis is possible in exceptional circumstances but has a very low success rate.",
        "refusal": "Belgian visa refusals are commonly based on: insufficient financial guarantees, inadequate travel insurance, incomplete documentation, doubts about travel purpose or intent to return, previous Schengen violations, or security concerns. Refusals are issued on the standardized Schengen refusal form with specific reasons. For Schengen C-type visas, applicants can appeal to the Council for Alien Law Litigation (Conseil du Contentieux des Étrangers/Raad voor Vreemdelingenbetwistingen) within 30 days. For D-type visas, appeals can be filed within 30 days to the same body. Legal representation by a Belgian immigration lawyer (avocat en droit des étrangers) is recommended. Reapplication is possible immediately with improved documentation. The appeal process typically takes 3-9 months. Belgium has one of the higher refusal rates in the Schengen Area, particularly for applications from certain regions, making thorough preparation essential.",
    },
    "visa-belize": {
        "name": "Belize",
        "visa_types": [
            ("Tourist Visa", "30 days", "USD 50", "Passport, return ticket, accommodation proof, financial proof"),
            ("Business Visa", "30 days", "USD 50", "Business invitation, company documents"),
            ("Work Permit", "1 year, renewable", "USD 1,500-3,000", "Employer application, skills not locally available"),
            ("Student Visa", "Duration of studies", "USD 50", "Acceptance letter, financial proof"),
            ("Retired Persons Incentive Program (QRP)", "Renewable annually", "USD 2,000/year", "Age 45+, income USD 2,000+/month, police clearance"),
            ("Permanent Residence", "Permanent", "USD 1,000-2,000", "1+ year legal residence, financial proof, police clearance"),
            ("Temporary Employment Permit", "3-6 months", "USD 500-750", "Specific project, employer sponsorship"),
            ("Dependent Visa", "Matches sponsor", "USD 25-50", "Sponsor's valid visa, proof of relationship"),
            ("Transit Visa", "72 hours", "USD 25", "Passport, onward ticket"),
            ("Investor Visa", "1 year, renewable", "USD 1,000-2,000", "Investment in Belize, business plan, capital proof"),
        ],
        "processing": [
            ("Tourist Visa", "2-5 business days", "USD 50", "1-2 days", "USD 100"),
            ("Work Permit", "4-8 weeks", "USD 1,500-3,000", "2-3 weeks", "Additional 50%"),
            ("QRP Program", "4-8 weeks", "USD 2,000/year", "2-3 weeks", "USD 3,000/year"),
            ("Permanent Residence", "3-12 months", "USD 1,000-2,000", "2-4 months", "Additional fees"),
            ("Student Visa", "2-4 weeks", "USD 50", "1 week", "USD 100"),
        ],
        "health": "Belize requires a Yellow Fever vaccination certificate for travelers arriving from yellow fever endemic countries. No other mandatory vaccinations are required for entry. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, and rabies (for rural areas). Malaria prophylaxis is advisable for areas west of Belize City. No medical examination is required for tourist visas. Work permit and QRP applicants must undergo a medical examination including HIV testing at an approved clinic. Health insurance is strongly recommended but not legally mandatory for tourists. QRP participants must show proof of health insurance. Police clearance certificates from the applicant's country of origin and any country of residence in the past 5 years are required for work permits, permanent residence, and QRP applications. Biometric data (photograph and fingerprints) is collected at the Belize Immigration Department for all non-citizen permit holders.",
        "extension": "Tourist visas can be extended monthly at the Belize Immigration Department for up to 6 months total. Each extension costs approximately BZD 200 (USD 100). After 6 months, you may apply for a new visa from outside Belize or apply for temporary or permanent residence. Extensions must be applied for before the current visa expires. Work permits are renewed annually through the employer. Overstay penalties include fines of BZD 100-500 per month of overstay, detention, deportation at the violator's expense, and entry bans of 1-3 years. Working without a valid permit carries fines of BZD 5,000 and/or imprisonment. Belize immigration conducts periodic checks, especially in tourist areas. Overstayers may be arrested and held pending deportation. Multiple overstays result in longer bans.",
        "refusal": "Belize visa refusals typically result from: insufficient financial means, incomplete documentation, criminal record, previous deportations, health concerns, or inability to demonstrate purpose of visit. Refusals at the port of entry result in immediate return on the next available flight. Consular refusals can be reconsidered by submitting additional documentation. There is no formal appeals tribunal, but the Chief Immigration Officer or the Minister of Immigration can exercise discretion. Reapplication is permitted immediately with improved documentation. Legal representation through a Belizean attorney is advisable for complex cases. QRP refusals can be appealed to the Belize Tourism Board. Work permit refusals are often related to the labor market test requirement, and employers can reapply with better justification for why a local worker cannot fill the position. The reconsideration process typically takes 2-6 weeks.",
    },
    "visa-bermuda": {
        "name": "Bermuda",
        "visa_types": [
            ("Tourist Entry (Visa-Free)", "Up to 90 days (varies)", "Free", "Passport, return ticket, accommodation, financial proof"),
            ("Tourist Visa (for visa-required nationalities)", "90 days", "USD 35-75", "Passport, invitation/hotel, financial proof, return ticket"),
            ("Work Permit", "1-5 years", "USD 2,000-15,000+", "Employer application, job market test, qualifications"),
            ("Student Visa", "Duration of studies", "USD 100-200", "Acceptance letter, financial proof, insurance"),
            ("Spouse/Dependent Permit", "Matches sponsor", "USD 1,000-2,000", "Marriage certificate, sponsor's work permit"),
            ("Permanent Resident Certificate (PRC)", "Permanent", "USD 2,000-5,000", "20+ years residence, no criminal record, community ties"),
            ("Digital Nomad Certificate", "1 year", "USD 263", "Remote employment proof, insurance, income proof"),
            ("Retired Person Permit", "Renewable", "USD 2,000", "Retirement income proof, health insurance"),
            ("Short-Term Work Permit", "Up to 90 days", "USD 500-2,500", "Specific project, employer sponsorship"),
            ("Investor Permit", "2-5 years", "USD 5,000+", "Investment in Bermuda economy, business plan"),
        ],
        "processing": [
            ("Tourist Visa", "3-5 business days", "USD 35-75", "1-2 days", "USD 100-150"),
            ("Work Permit", "6-12 weeks", "USD 2,000-15,000", "3-6 weeks", "Additional fees"),
            ("Digital Nomad Certificate", "5-10 business days", "USD 263", "2-3 days", "USD 500"),
            ("Student Visa", "2-4 weeks", "USD 100-200", "1 week", "USD 300"),
            ("PRC", "6-12 months", "USD 2,000-5,000", "3-6 months", "Additional fees"),
        ],
        "health": "Bermuda does not require mandatory vaccinations for entry from most countries. A Yellow Fever vaccination certificate may be required for travelers from endemic areas. No medical examination is required for tourist visas. Work permit applicants must undergo a medical examination by a Bermuda-approved physician, including a general health check, chest X-ray, and blood tests. Health insurance is mandatory for all residents and work permit holders in Bermuda — the employer must provide Standard Hospital Benefit (HIP) coverage at minimum. Tourists are strongly recommended to have comprehensive travel and medical insurance as healthcare in Bermuda is extremely expensive. Police clearance certificates from the applicant's home country and any country of residence are required for work permits and permanent residence applications. Bermuda immigration collects biometric data (photographs and fingerprints) for all work permit and residence permit applicants. COVID-19 testing and vaccination requirements are updated periodically through the Bermuda Government portal.",
        "extension": "Tourist stays can be extended beyond the initial 90 days by applying at the Bermuda Department of Immigration, generally for up to 6 months total. Extension fees vary based on length requested. Work permits are renewed through the employer before expiry. The Digital Nomad Certificate can be renewed for additional 1-year periods. Overstay penalties include fines of USD 500-2,000, deportation at the violator's expense, entry bans, and potential criminal prosecution with imprisonment of up to 6 months. Working without a valid work permit in Bermuda carries severe penalties including fines of up to USD 5,000 and imprisonment. Bermuda's small size makes detection of immigration violations relatively easy. The Department of Immigration conducts routine compliance checks. Overstayers are typically detained and placed on the next available flight.",
        "refusal": "Bermuda visa and work permit refusals commonly result from: insufficient proof that a local worker is not available for the position (work permits), incomplete documentation, criminal record, previous immigration violations, failure to meet financial thresholds, or health concerns. The refusal is communicated in writing by the Department of Immigration with reasons. Work permit refusals can be appealed to the Work Permit Tribunal within 14 days of the decision. The Tribunal hearing is quasi-judicial and legal representation is recommended. Tourist visa refusals can be reconsidered by writing to the Chief Immigration Officer. Reapplication is permitted after addressing the refusal grounds. Port-of-entry refusals result in immediate return and may affect future applications. Legal representation through a Bermuda-qualified attorney is advisable for work permit appeals. The appeal process typically takes 4-8 weeks.",
    },
    "visa-bhutan": {
        "name": "Bhutan",
        "visa_types": [
            ("Tourist Visa", "Varies (typically 5-30 days)", "Free (SDF applies)", "Passport, approved tour, Sustainable Development Fee"),
            ("Business Visa", "30 days, extendable", "No visa fee (SDF may apply)", "Business invitation, company endorsement"),
            ("Work Permit", "1-2 years, renewable", "No visa fee", "Employer sponsorship, government approval, skills shortage"),
            ("Student Visa", "Duration of studies", "No visa fee", "Institution acceptance, scholarship or financial proof"),
            ("Official/Diplomatic Visa", "Varies", "Free", "Government or diplomatic invitation"),
            ("NGO/Volunteer Visa", "3-12 months", "No visa fee", "NGO endorsement, government approval"),
            ("Transit Visa", "72 hours", "Free", "Drukair/Bhutan Airlines ticket, onward booking"),
            ("Indian/Bangladeshi/Maldivian Entry", "Visa-free (permit)", "Free", "Valid passport or voter ID, entry permit at border"),
            ("Journalist Visa", "As approved", "No visa fee", "Press credentials, government media approval"),
            ("Courtesy Visa", "As approved", "Free", "Government invitation for cultural/academic purposes"),
        ],
        "processing": [
            ("Tourist Visa", "5-7 business days", "SDF: USD 100/night", "2-3 days", "SDF: USD 100/night"),
            ("Business Visa", "2-4 weeks", "No visa fee", "1-2 weeks", "N/A"),
            ("Work Permit", "4-8 weeks", "No visa fee", "2-4 weeks", "N/A"),
            ("Student Visa", "3-6 weeks", "No visa fee", "1-2 weeks", "N/A"),
            ("Transit Visa", "1-3 days", "Free", "Same day", "N/A"),
        ],
        "health": "Bhutan does not require mandatory vaccinations for most travelers but strongly recommends hepatitis A, hepatitis B, typhoid, Japanese encephalitis (for rural areas), and rabies vaccinations. A Yellow Fever vaccination certificate is required for travelers from endemic countries. No medical examination is required for tourist visas. Work permit and long-stay visa applicants may need to undergo medical screening at a Bhutanese health facility. Health insurance with coverage for medical evacuation is strongly recommended, as Bhutan has limited medical facilities and serious cases require evacuation to India or Thailand. The Sustainable Development Fee (SDF) of USD 100 per night (USD 200 per night for non-regional tourists) was introduced in 2023, partially funding healthcare and infrastructure. Police clearance certificates are required for work permits and student visas. Biometric data is collected at Paro International Airport and land border crossings. Altitude sickness precautions are important as many areas in Bhutan are above 2,500 meters.",
        "extension": "Tourist visa extensions can be arranged through your licensed tour operator while in Bhutan, subject to government approval. The SDF continues to apply for each additional night. Maximum tourist stay depends on the approved itinerary and SDF payment. Work permit holders can extend through their employer before expiry. Overstay penalties include fines of approximately Nu 500-1,000 per day, deportation, and bans from future entry of 1-3 years. Since all tourist arrangements must go through licensed operators, overstays are relatively rare. Independent tourism is not permitted for most nationalities (except Indians, Bangladeshis, and Maldivians), making overstay less common. Work permit violations can result in both the employee and employer facing penalties. Bhutan's immigration system is tightly controlled through the Tourism Council of Bhutan and the Department of Immigration.",
        "refusal": "Bhutan visa refusals may occur due to: failure to book through a licensed tour operator (required for most nationalities), insufficient SDF payment, criminal record, security concerns, incomplete documentation, or failure to meet specific visa requirements. Tourist visa refusals are communicated through the tour operator. Business visa refusals are communicated through the sponsoring entity. Appeals can be made to the Department of Immigration in Thimphu through the sponsoring agency. There is no formal public appeals process for tourist visas — the tour operator serves as intermediary. Reapplication through a different or the same tour operator is possible. For work permits, the employer can appeal to the Ministry of Labour and Human Resources. Bhutan maintains strict control over visitor numbers to protect its environment and culture. The best approach is to ensure all documentation and payment are complete before application.",
    },
    "visa-brazil": {
        "name": "Brazil",
        "visa_types": [
            ("Tourist Visa (VITUR)", "90 days, extendable to 180", "USD 40-160", "Passport, return ticket, hotel booking, financial proof"),
            ("Business Visa (VITEM II)", "90 days", "USD 100-160", "Business invitation, company letter, financial proof"),
            ("Work Visa (VITEM V)", "Up to 2 years", "USD 180-290", "Employment contract, company sponsorship, labor ministry approval"),
            ("Student Visa (VITEM IV)", "1 year, renewable", "USD 100-160", "University acceptance, financial proof, insurance"),
            ("Transit Visa (VITR)", "Up to 10 days", "USD 20-40", "Onward ticket, passport"),
            ("MERCOSUR Residence", "2 years, then permanent", "Varies by nationality", "MERCOSUR country passport, clean criminal record"),
            ("Investor Visa (VITEM V-Investor)", "Permanent", "USD 200-290", "Investment of BRL 500,000+ in Brazil, business plan"),
            ("Retirement Visa (VITEM I)", "Permanent", "USD 100", "Income of BRL 6,000+/month, pension proof"),
            ("Digital Nomad Visa", "1 year, renewable", "USD 100", "Remote employment, income USD 1,500+/month"),
            ("Family Reunification Visa", "1-2 years", "USD 100-160", "Marriage cert or birth cert, sponsor's CPF and residency"),
        ],
        "processing": [
            ("Tourist Visa (VITUR)", "5-15 business days", "USD 40-160", "2-3 days", "USD 80-200"),
            ("Business Visa", "5-10 business days", "USD 100-160", "2-3 days", "USD 160-250"),
            ("Work Visa", "4-8 weeks", "USD 180-290", "2-3 weeks", "USD 300-450"),
            ("Student Visa", "3-6 weeks", "USD 100-160", "1-2 weeks", "USD 200-250"),
            ("Digital Nomad Visa", "2-4 weeks", "USD 100", "1 week", "USD 200"),
        ],
        "health": "Brazil requires a Yellow Fever vaccination certificate for travelers visiting the Amazon region, Pantanal, and other high-risk areas. While not always enforced at international entry points, it is mandatory for internal travel to certain states including Amazonia, Goiás, Mato Grosso, and Mato Grosso do Sul. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, and rabies (for rural areas). Malaria prophylaxis is strongly advised for Amazon travel. No medical examination is required for tourist or business visas. Work visa applicants must present a health certificate from a physician. Health insurance is not legally mandatory for tourists but is strongly recommended due to costs at private hospitals. SUS (Sistema Único de Saúde) provides free public healthcare to all people in Brazil, including tourists, though quality varies significantly. Police clearance certificates (apostilled and translated) are required for work, student, and residence visas. Brazil collects biometric data (fingerprints and photograph) from all foreign nationals at ports of entry through the AFIS system.",
        "extension": "Tourist visas can be extended once for an additional 90 days at the Federal Police (Polícia Federal) office, for a total maximum stay of 180 days per year. The extension fee is approximately BRL 200. Apply at least 15 days before expiry. After 180 days, you must leave Brazil and cannot return for 180 days unless you hold a different visa type. Work visa renewals are handled through the employer and the Ministry of Justice. Student visa renewals require continued enrollment. Overstay penalties include fines of BRL 100 per day (up to BRL 10,000 maximum), deportation, and entry bans of 1-5 years. Brazil occasionally offers amnesty programs for long-term undocumented residents. Overstayers must pay all accumulated fines before being allowed to leave Brazil legally. MERCOSUR citizens have more flexible arrangements and rarely face harsh overstay penalties.",
        "refusal": "Brazilian visa refusals may result from: incomplete documentation, insufficient financial proof, criminal record, previous Brazilian immigration violations, inconsistencies in the application, or public health concerns. Refusal notifications are provided by the consulate with general reasons. Applicants can request reconsideration by submitting additional documentation to the same consulate within 30 days. If denied again, an appeal can be filed with the Ministry of Foreign Relations (Itamaraty). Reapplication is permitted immediately with corrected documentation. US citizens should note that Brazil applies reciprocity fees and processing times mirroring US treatment of Brazilian citizens. Legal representation through a Brazilian immigration attorney (advogado de imigração) is advisable for complex cases. The appeal process typically takes 2-4 months. Digital nomad visa refusals are often related to insufficient proof of remote employment or income.",
    },
    "visa-brunei": {
        "name": "Brunei",
        "visa_types": [
            ("Visa-Free Entry (eligible nationalities)", "14-90 days", "Free", "Valid passport, return ticket"),
            ("Tourist Visa (Single Entry)", "90 days", "BND 20 (USD 15)", "Passport, return ticket, accommodation proof"),
            ("Business Visa", "14-90 days", "BND 20", "Business invitation, company letter"),
            ("Work Permit (Foreign Worker License)", "1-2 years", "BND 100-500", "Employer sponsorship, labor department approval"),
            ("Student Visa", "Duration of studies", "BND 20", "Acceptance letter, financial proof, sponsor"),
            ("Dependent Pass", "Matches sponsor", "BND 50-100", "Sponsor's work permit, relationship proof"),
            ("Professional Visit Pass", "30 days", "BND 20", "Company invitation for technical/professional work"),
            ("Transit Visa", "72 hours", "Free-BND 5", "Onward ticket, passport"),
            ("Social Visit Pass (extended)", "Up to 90 days", "BND 20", "Local sponsor, relationship proof"),
            ("Special Pass (Emergency)", "14 days", "BND 50", "Emergency circumstances, immigration discretion"),
        ],
        "processing": [
            ("Tourist Visa", "2-5 business days", "BND 20", "1 day", "BND 40"),
            ("Business Visa", "3-5 business days", "BND 20", "1-2 days", "BND 40"),
            ("Work Permit", "4-8 weeks", "BND 100-500", "2-3 weeks", "BND 200-750"),
            ("Student Visa", "3-6 weeks", "BND 20", "1-2 weeks", "BND 40"),
            ("Transit Visa", "1-2 days", "Free-BND 5", "Same day", "BND 10"),
        ],
        "health": "Brunei does not require mandatory vaccinations for most travelers. A Yellow Fever vaccination certificate is required for travelers from endemic countries. COVID-19 vaccination may be recommended based on current health advisories. No medical examination is required for tourist visas. Work permit applicants must undergo a comprehensive medical examination at a government-approved clinic in Brunei, including chest X-ray, blood tests (HIV, hepatitis B, syphilis, malaria), stool analysis, and a general physical exam. Applicants who test positive for certain conditions will have their work permits denied. Health insurance is not mandatory for tourists but is strongly recommended. Work permit holders are typically covered under employer health schemes. Police clearance certificates from the applicant's home country are required for work permits and student visas. Brunei collects biometric data at all entry points. Brunei has strict drug laws — any traveler found carrying illegal drugs faces severe penalties including the death penalty.",
        "extension": "Tourist visa extensions can be obtained at the Brunei Immigration Department for additional 14-day periods, up to a maximum total stay as approved. Work permits are renewed through the employer before expiry. Overstay penalties in Brunei are strict: fines of BND 1,000-5,000, imprisonment of up to 3 months, whipping (caning) may be imposed in severe cases, deportation, and permanent entry bans. Brunei takes immigration violations very seriously under its strict legal system. Employers who employ foreign workers without valid permits face fines of BND 10,000-30,000 and/or imprisonment. The Immigration Department conducts regular inspections. Overstayers should report to the Immigration Department voluntarily to potentially reduce penalties. Repeat offenders face progressively harsher punishments.",
        "refusal": "Brunei visa refusals may result from: incomplete documentation, criminal record, security concerns, insufficient financial means, previous immigration violations, or failure of medical examination. Refusals are communicated through the embassy or at the border. There is no formal public appeals process for tourist visas. Work permit refusals can be reconsidered by the employer submitting additional documentation to the Labour Department. Port-of-entry refusals result in immediate return. Reapplication is possible after addressing the refusal reasons, typically after a waiting period of 1-3 months. Legal representation in Brunei is limited for immigration cases. The best approach is to ensure thorough documentation before applying. Brunei maintains broad discretion over visa approvals and refusals under the Immigration Act (Chapter 17).",
    },
    "visa-bulgaria": {
        "name": "Bulgaria",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Long-Stay Visa (D-type)", "Up to 1 year", "EUR 100", "Purpose documentation, financial proof"),
            ("Work Visa (Single Permit)", "1 year, renewable", "EUR 100", "Employment contract, employer registration, labor office approval"),
            ("EU Blue Card", "Up to 4 years", "EUR 100", "High-qualification job, salary 1.5x average, degree"),
            ("Student Visa", "1 year, renewable", "EUR 100", "University acceptance, EUR 300/month proof, insurance"),
            ("Family Reunification Visa", "1 year, renewable", "EUR 100", "Relationship proof, sponsor residence, financial proof"),
            ("Business/Self-Employment Visa", "1 year, renewable", "EUR 100", "Business registration, investment, business plan"),
            ("Freelancer Visa", "1 year, renewable", "EUR 100", "Freelance contracts, income proof, insurance"),
            ("Retirement Visa", "1 year, renewable", "EUR 100", "Pension proof EUR 600+/month, health insurance"),
            ("Digital Nomad Visa", "1 year", "EUR 100", "Remote work contract, income EUR 2,000+/month, insurance"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "2-6 weeks", "EUR 100", "1-2 weeks", "EUR 200"),
            ("Work Visa", "4-8 weeks", "EUR 100", "2-3 weeks", "EUR 200"),
            ("Student Visa", "2-4 weeks", "EUR 100", "1 week", "EUR 200"),
            ("Digital Nomad Visa", "2-4 weeks", "EUR 100", "1 week", "EUR 200"),
        ],
        "health": "Bulgaria requires travel medical insurance with minimum coverage of EUR 30,000 for all Schengen short-stay visa applicants. No mandatory vaccinations are required for entry. Long-stay visa and residence permit applicants must undergo a medical examination at a Bulgarian medical facility, including a general health check and tuberculosis screening. Health insurance is mandatory for all residents — either through the National Health Insurance Fund (NHIF) for workers or private insurance. EU/EEA citizens can use the EHIC card. Police clearance certificates from the applicant's country of origin and countries of residence are required for D-type visas and residence permits, and must be apostilled and translated into Bulgarian. Biometric data (fingerprints and photograph) are collected for all visa applicants at Bulgarian embassies or authorized visa application centers. Bulgaria joined the Schengen Area for air and sea borders in 2024, with full land border accession expected.",
        "extension": "Schengen visas allow 90 days within 180 days and generally cannot be extended. National D-type visa holders must apply for a residence permit within 14 days of arrival at the local Migration Directorate. Residence permits are renewable 30 days before expiry. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines of BGN 500-5,000, deportation, and entry bans of 1-5 years. Bulgaria reports overstays to the SIS II database for Schengen-wide bans. Voluntary departure before detection may reduce penalties. Work without a valid permit carries fines for both employee and employer. Bulgaria's Migration Directorate actively monitors visa compliance. EU/EEA citizens have free movement rights but must register after 3 months.",
        "refusal": "Bulgarian visa refusals may result from: insufficient travel insurance, inadequate financial proof, incomplete documentation, doubts about purpose of travel, previous immigration violations, security concerns, or failure to meet specific requirements. Refusals are issued on the standardized form with specific reasons. Schengen visa refusals can be appealed to the Administrative Court within 14 days. D-type visa and residence permit refusals can be challenged within 14 days at the relevant Administrative Court. Reapplication is possible immediately with improved documentation. Legal representation through a Bulgarian immigration attorney is recommended. Bulgaria's refusal rates are moderate. The appeal process typically takes 1-3 months. VFS Global centers processing Bulgarian visa applications can provide guidance on documentation requirements.",
    },
    "visa-cambodia": {
        "name": "Cambodia",
        "visa_types": [
            ("Tourist Visa (T-class)", "30 days", "USD 30", "Passport, passport photo, arrival/departure card"),
            ("eVisa (Tourist)", "30 days", "USD 36", "Online application, passport scan, photo, credit card"),
            ("Visa on Arrival (Tourist)", "30 days", "USD 30", "Passport, passport photo, USD 30 cash"),
            ("Business Visa (E-class)", "30 days, extendable", "USD 35", "Passport, passport photo, may need business letter"),
            ("Work Permit (with E visa extension)", "1 year", "USD 100-300", "Employer sponsorship, E visa, ministry approval"),
            ("Student Visa (E-class extension)", "1 year", "USD 100-300", "Institution acceptance, E visa"),
            ("Retirement Visa (ER extension)", "1 year", "USD 300", "Age 55+, E visa, retirement letter, financial proof"),
            ("Diplomatic Visa (A/B-class)", "Varies", "Free", "Diplomatic passport, official letter"),
            ("Transit Visa", "Up to 72 hours", "Free", "Onward ticket, valid passport"),
            ("Long-Stay Business Extension (EG/EB/ES)", "6-12 months", "USD 160-300", "E visa base, employer/school sponsor, valid passport"),
        ],
        "processing": [
            ("Tourist Visa (T)", "On arrival (minutes)", "USD 30", "N/A", "N/A"),
            ("eVisa", "3-5 business days", "USD 36", "1 business day", "USD 42"),
            ("Business Visa (E)", "On arrival (minutes)", "USD 35", "N/A", "N/A"),
            ("Work Permit", "2-4 weeks", "USD 100-300", "1-2 weeks", "Additional fees"),
            ("E Visa Extensions", "5-10 business days", "USD 160-300", "2-3 days", "Additional USD 30-50"),
        ],
        "health": "Cambodia does not require mandatory vaccinations for most travelers. A Yellow Fever vaccination certificate is required for travelers from endemic countries. Strongly recommended vaccinations include hepatitis A, hepatitis B, typhoid, Japanese encephalitis, and rabies. Malaria prophylaxis is advised for rural and forested areas, especially Mondulkiri and Ratanakiri provinces. No medical examination is required for tourist visas. Work permit applicants must undergo a medical check at a Cambodian-approved clinic. Health insurance is strongly recommended as medical facilities in Cambodia are limited, and serious cases require evacuation to Bangkok or Singapore. Police clearance certificates are required for work permits and long-term business visa extensions. Biometric data (fingerprints and photograph) is collected at Phnom Penh International Airport and Siem Reap International Airport on arrival. Dengue fever is endemic — travelers should take mosquito precautions.",
        "extension": "Tourist visas (T-class) can be extended once for 30 additional days at the General Department of Immigration in Phnom Penh. The extension fee is approximately USD 45. After that, you must leave or switch to an E-class visa. Business visas (E-class) can be extended for 1, 3, 6, or 12 months, making them the preferred option for long-term stays. Overstay penalties are USD 10 per day for the first 30 days of overstay, then potential deportation and entry bans of 1-3 years. Cambodia is generally flexible about visa issues and agents can often assist with extensions. However, recent enforcement has increased. Working without a proper work permit carries fines and deportation. The General Department of Immigration occasionally conducts sweeps in Phnom Penh and Siem Reap targeting overstayers.",
        "refusal": "Cambodia rarely refuses tourist visa applications or visas on arrival. Refusals may occur for: nationals of certain restricted countries, criminal records, previous deportations from Cambodia, national security concerns, or expired/invalid passports. Port-of-entry refusals result in return on the next flight. eVisa refusals are communicated online with limited explanation. Work permit refusals may be due to insufficient documentation or employer non-compliance. There is no formal appeals process for tourist visa refusals. For work permits, the employer can resubmit with corrected documentation. Engaging a local immigration agent or lawyer is common practice in Cambodia for resolving visa issues. Reapplication is possible immediately. Cambodia's immigration system is generally accommodating, especially for tourism-oriented visas.",
    },
    "visa-canada": {
        "name": "Canada",
        "visa_types": [
            ("Electronic Travel Authorization (eTA)", "Up to 6 months per entry", "CAD 7", "Visa-exempt passport, no criminal record"),
            ("Temporary Resident Visa (TRV) - Tourist", "Up to 6 months", "CAD 100", "Passport, financial proof, ties to home country, return ticket"),
            ("Business Visitor", "Up to 6 months", "CAD 100", "Business invitation, no intention to enter labor market"),
            ("Work Permit (LMIA-based)", "Varies", "CAD 155", "Positive LMIA from employer, job offer, qualifications"),
            ("International Experience Canada (IEC/WHV)", "1-2 years", "CAD 172 + CAD 100 (OWP fee)", "Age 18-35, bilateral agreement country"),
            ("Study Permit", "Duration of studies + 90 days", "CAD 150", "Letter of acceptance from DLI, financial proof, medical exam"),
            ("Express Entry (Permanent Residence)", "Permanent", "CAD 1,365", "CRS score, work experience, language tests, education"),
            ("Family Sponsorship", "Permanent", "CAD 1,080", "Sponsor must be citizen/PR, minimum income, relationship proof"),
            ("Start-Up Visa", "Permanent", "CAD 1,625", "Support from designated VC, angel investor, or incubator"),
            ("Super Visa (Parents/Grandparents)", "Up to 5 years per entry", "CAD 100", "Canadian child/grandchild sponsor, insurance CAD 100k+"),
        ],
        "processing": [
            ("eTA", "Minutes (online)", "CAD 7", "N/A", "N/A"),
            ("TRV (Tourist)", "2-8 weeks", "CAD 100", "N/A (online only)", "N/A"),
            ("Work Permit", "2-16 weeks", "CAD 155", "2 weeks (Global Skills)", "CAD 1,000"),
            ("Study Permit", "4-12 weeks", "CAD 150", "20 days (SDS)", "CAD 150"),
            ("Express Entry PR", "4-8 months", "CAD 1,365", "N/A", "N/A"),
        ],
        "health": "Canada requires a medical examination (Immigration Medical Exam or IME) for applicants staying longer than 6 months and for those intending to work in healthcare, education, or childcare. The IME must be performed by a designated panel physician and includes a general physical examination, chest X-ray, blood tests (syphilis, HIV), and urinalysis. Results are valid for 12 months. Applicants with certain conditions (active TB, untreated syphilis) may be refused or required to undergo treatment. No mandatory vaccinations are required for entry, though routine immunizations are recommended. Health insurance is strongly recommended as visitors are not covered by provincial healthcare (e.g., OHIP, MSP). International students and some work permit holders may be eligible for provincial health coverage after a waiting period (typically 3 months). Police certificates from all countries where the applicant has lived for 6+ months since age 18 are required for permanent residence applications. Biometric data (fingerprints and photograph) is collected from nationals of most countries applying for visitor visas, work permits, or study permits, at designated IRCC biometric collection sites.",
        "extension": "Visitors can apply to extend their stay beyond 6 months by submitting a 'Visitor Record' application online before their authorized stay expires. The extension fee is CAD 100. Work permit and study permit holders can extend through IRCC. Implied status allows continued stay/work while an extension application is pending. Maximum tourist stay is generally 6 months per entry (up to 5 years for Super Visa). Overstay consequences include loss of legal status, deportation, entry bans (1 year for departure orders, 2 years for exclusion orders, permanent for deportation orders), and potential criminal charges for misrepresentation. An A44 report is issued for non-compliance. Voluntary departure before a removal order results in no entry ban. Canada Border Services Agency (CBSA) enforces immigration law. Overstay records affect future applications to Canada and may impact applications to other Five Eyes countries (US, UK, Australia, New Zealand).",
        "refusal": "Canadian visa refusals are common, particularly for visitor visas, and typically cite: failure to demonstrate intention to leave Canada (purpose of visit), insufficient financial means, weak ties to home country, incomplete documentation, inadmissibility (criminal, health, security), or previous violations. Refusal letters specify the reasons under IRPA (Immigration and Refugee Protection Act). No formal appeal exists for visitor visa refusals, but applicants may request judicial review at the Federal Court within 15 days (limited to legal errors). Reapplication is permitted immediately with stronger documentation. GCMS (Global Case Management System) notes can be obtained through an ATIP request to understand the officer's reasoning. Using a regulated immigration consultant (RCIC) or lawyer is advisable. Study permit refusals can be addressed through the Student Direct Stream (SDS) for certain countries. Express Entry refusals can be appealed to the Immigration Appeal Division (IAD) in some cases.",
    },
    "visa-cape-verde": {
        "name": "Cape Verde",
        "visa_types": [
            ("Tourist Visa", "30 days, extendable", "EUR 25-35", "Passport, return ticket, hotel booking"),
            ("Airport Pre-Registration (EASE)", "Up to 30 days", "EUR 31 (online)", "Pre-registration online for eligible nationalities"),
            ("Business Visa", "30-90 days", "EUR 35-50", "Business invitation, company letter, financial proof"),
            ("Work Visa (Autorização de Trabalho)", "1 year, renewable", "EUR 100-200", "Employment contract, employer sponsorship, medical cert"),
            ("Student Visa", "1 year, renewable", "EUR 35", "University acceptance, financial proof, insurance"),
            ("Family Reunification Visa", "1 year, renewable", "EUR 35-50", "Proof of relationship, sponsor residency"),
            ("Investor/Business Establishment Visa", "2 years, renewable", "EUR 100-200", "Business plan, capital proof, registration"),
            ("Transit Visa", "Up to 5 days", "EUR 15-25", "Onward ticket, passport"),
            ("Residence Permit (Autorização de Residência)", "1-2 years, renewable", "EUR 50-100", "Valid visa, proof of means, accommodation"),
            ("ECOWAS Free Movement", "90 days visa-free", "Free", "ECOWAS member state passport"),
        ],
        "processing": [
            ("Tourist Visa", "3-5 business days", "EUR 25-35", "1-2 days", "EUR 50-70"),
            ("EASE Registration", "24-48 hours (online)", "EUR 31", "Same day", "N/A"),
            ("Work Visa", "3-8 weeks", "EUR 100-200", "1-2 weeks", "EUR 200-350"),
            ("Student Visa", "2-4 weeks", "EUR 35", "1 week", "EUR 70"),
            ("Business Visa", "3-5 business days", "EUR 35-50", "1-2 days", "EUR 70-100"),
        ],
        "health": "Cape Verde requires a Yellow Fever vaccination certificate for travelers from endemic countries. No other mandatory vaccinations are required, though hepatitis A, hepatitis B, typhoid, and routine immunizations are recommended. Malaria risk is low but exists on some islands — prophylaxis may be advised for Santiago island. No medical examination is required for tourist visas. Work and residence visa applicants must undergo a medical examination at an approved facility. Health insurance is strongly recommended as medical facilities on the islands are limited, and serious cases may require evacuation to Portugal or Senegal. Police clearance certificates are required for work visas and residence permits. Cape Verde collects biometric data at its international airports (Praia, Sal). The EASE (Electronic Pre-Arrival Registration) system is mandatory for visitors from certain countries, serving as a pre-screening tool.",
        "extension": "Tourist visas can be extended at the DREF (Directorate of Foreigners and Borders) office in Praia or local police stations on other islands for additional 30-day periods, up to a maximum total stay of 90 days. Extension fees are approximately EUR 25-50 per extension. Work and residence permits are renewed at DREF before expiry. Overstay penalties include fines of CVE 10,000-50,000, deportation at the violator's expense, and entry bans of 1-3 years. Cape Verde takes immigration compliance seriously, especially on tourist-heavy islands like Sal and Boa Vista. Working without a valid work permit carries additional fines and deportation. The DREF conducts periodic checks in tourist areas and workplaces.",
        "refusal": "Cape Verde visa refusals may result from: incomplete documentation, insufficient financial proof, lack of return ticket, criminal record, or previous immigration violations. Refusals are communicated by the embassy or DREF. Applicants can request reconsideration within 15 days by submitting additional documentation. There is no formal appeals tribunal, but the Director of DREF can review cases. Reapplication is permitted immediately with improved documentation. EASE registration refusals are communicated online and usually relate to nationality restrictions or incomplete information — reapplication with corrected data is possible immediately. Legal representation through a Cape Verdean attorney is advisable for complex cases, particularly for work visa refusals.",
    },
    "visa-chile": {
        "name": "Chile",
        "visa_types": [
            ("Tourist Visa (Turismo)", "90 days", "Free for most; reciprocity fee for some", "Passport, return ticket, financial proof"),
            ("Business Visa", "90 days", "Varies", "Business invitation, company letter"),
            ("Work Visa (Visa Sujeta a Contrato)", "Up to 2 years", "USD 100-200", "Employment contract, employer registration, qualifications"),
            ("Student Visa (Visa de Estudiante)", "Duration of studies", "USD 100", "University acceptance, financial proof, insurance"),
            ("Temporary Residence (Visa Temporaria)", "1 year, renewable", "USD 100-200", "Purpose-specific, financial proof, insurance"),
            ("Family Reunification", "1-2 years", "USD 100-200", "Relationship proof, sponsor's residency/RUT"),
            ("Investor Visa", "1-2 years, renewable", "USD 200-300", "Investment plan, capital of USD 300,000+"),
            ("Digital Nomad Visa (Visa de Nómada Digital)", "1 year", "USD 100", "Remote work proof, income USD 1,500+/month, insurance"),
            ("Retirement Visa (Visa de Jubilado)", "1 year, renewable", "USD 100", "Pension/retirement income proof, health insurance"),
            ("Permanent Residence (Permanencia Definitiva)", "Permanent", "USD 100-200", "1-2 years continuous residence, financial stability"),
        ],
        "processing": [
            ("Tourist Visa", "Visa-free or 2-5 days", "Free or reciprocity", "1-2 days", "Additional fee"),
            ("Work Visa", "3-8 weeks", "USD 100-200", "1-2 weeks", "USD 200-350"),
            ("Student Visa", "2-4 weeks", "USD 100", "1 week", "USD 200"),
            ("Digital Nomad Visa", "2-4 weeks", "USD 100", "1 week", "USD 200"),
            ("Permanent Residence", "2-6 months", "USD 100-200", "1-2 months", "USD 300"),
        ],
        "health": "Chile does not require mandatory vaccinations for entry from most countries. A Yellow Fever vaccination certificate is recommended for travelers arriving from endemic countries. Routine vaccinations (hepatitis A, hepatitis B, typhoid) are recommended. No medical examination is required for tourist visas. Work and residence visa applicants may need to undergo medical screening. Health insurance is mandatory for all visa holders in Chile, either through FONASA (public) or ISAPRE (private). Chile has excellent healthcare facilities, particularly in Santiago. Police clearance certificates (Certificado de Antecedentes) from the applicant's home country (apostilled and translated into Spanish) are required for work and residence visas. Chile collects biometric data at international airports through the PDI (Policía de Investigaciones) immigration system. Easter Island (Rapa Nui) has additional entry requirements including a return ticket and accommodation booking.",
        "extension": "Tourist visas can be extended once for an additional 90 days at the Departamento de Extranjería y Migración (DEM) in Santiago. The extension fee is approximately CLP 100,000-200,000. A common alternative is the 'border run' to Argentina, which resets the 90-day period. Maximum tourist stay is 180 days per year. Work visa renewals must be submitted 90 days before expiry. Overstay penalties include fines of approximately UTM 1-10 (around USD 60-600), deportation with a ban of 5+ years, and inability to regularize status while in Chile. Chile has become stricter with immigration enforcement under the new Migration Law (2021). Working without authorization carries fines for both worker and employer. The PDI monitors immigration compliance through exit records.",
        "refusal": "Chilean visa refusals may result from: incomplete documentation, insufficient financial means, criminal record, previous deportations, health concerns, or failure to meet specific visa requirements. Refusals are communicated by the consulate or DEM. Applicants can submit a recurso de reconsideración (reconsideration request) within 5 business days, or a recurso jerárquico (hierarchical appeal) within 5 days after reconsideration denial. Reapplication is permitted with improved documentation. Legal representation through a Chilean immigration attorney (abogado de extranjería) is recommended. Chile's new Migration Law has made the application process more structured and transparent. The appeal process typically takes 2-4 months. Extranjería offices throughout Chile can provide guidance on requirements.",
    },
    "visa-china": {
        "name": "China",
        "visa_types": [
            ("Tourist Visa (L)", "30-90 days", "USD 140 (US), varies by nationality", "Passport, itinerary, hotel bookings, financial proof"),
            ("Business Visa (M/F)", "30-90 days, multiple entry", "USD 140", "Invitation from Chinese company, business letter"),
            ("Work Visa (Z)", "Initial entry 30 days, then permit", "USD 140", "Work permit notification, employer sponsorship"),
            ("Student Visa (X1/X2)", "X1: over 180 days, X2: under 180", "USD 140", "JW201/JW202 form, admission notice"),
            ("Transit Visa (G)", "Up to 10 days", "USD 140", "Confirmed onward ticket, transit through China"),
            ("Family Visit Visa (Q1/Q2/S1/S2)", "Q1: over 180 days, Q2: under 180", "USD 140", "Invitation from Chinese relative, relationship proof"),
            ("Journalist Visa (J1/J2)", "J1: resident, J2: temporary", "USD 140", "Press credentials, PRC Foreign Ministry approval"),
            ("Crew Visa (C)", "As needed", "USD 140", "Airline/shipping company letter"),
            ("Talent Visa (R)", "Up to 10 years", "USD 140", "High-level talent endorsement, category qualification"),
            ("144-Hour Transit Visa Exemption", "Up to 144 hours (6 days)", "Free", "Eligible nationality, confirmed onward ticket to third country"),
        ],
        "processing": [
            ("Tourist Visa (L)", "4-7 business days", "USD 140 (US)", "2-3 days", "USD 170 (US)"),
            ("Business Visa (M)", "4-7 business days", "USD 140", "2-3 days", "USD 170"),
            ("Work Visa (Z)", "4-7 business days", "USD 140", "2-3 days", "USD 170"),
            ("Student Visa (X1)", "4-7 business days", "USD 140", "2-3 days", "USD 170"),
            ("Transit Visa (G)", "4-5 business days", "USD 140", "1-2 days", "USD 170"),
        ],
        "health": "China requires specific health documentation depending on visa type and duration. Travelers staying more than 1 year (Z, X1, Q1 visa holders) must undergo a health examination at a designated Chinese Health and Quarantine Center within 30 days of arrival. The exam includes blood tests (HIV, syphilis, hepatitis B/C), chest X-ray, ECG, abdominal ultrasound, and general physical examination. No mandatory vaccinations are required for entry from most countries, though a Yellow Fever vaccination certificate is required from endemic countries. COVID-19 requirements have been largely relaxed but may be reinstated. Health insurance is required for student visa holders and recommended for all visitors. Chinese public hospitals are affordable but may have language barriers. Police clearance certificates (authenticated and translated into Chinese) are required for work visa (Z) and long-term residence applications. Biometric data (fingerprints) is collected at all major Chinese ports of entry for foreign nationals aged 14-70. The Public Security Bureau (PSB) handles residence registration within 24 hours of arrival.",
        "extension": "Tourist visa extensions can be obtained at the local Exit-Entry Administration of the Public Security Bureau (PSB) for 30 additional days. The extension fee is approximately CNY 160. Apply at least 7 days before visa expiry. Generally only one extension is granted for tourist visas. Work permit holders follow a separate renewal process through the employer and the Ministry of Human Resources and Social Security. Maximum tourist stay is typically 60 days (30 + 30 extension). Overstay penalties are CNY 500 per day (up to CNY 10,000 maximum), detention of up to 15 days, deportation, and entry bans of 1-5 years (up to 10 years for serious violations). China is very strict about immigration compliance. Overstayers are fingerprinted, photographed, and their information is entered into the national database. Employers who facilitate illegal employment face fines of CNY 5,000-50,000 per unauthorized worker.",
        "refusal": "Chinese visa refusals may result from: incomplete documentation, insufficient travel purpose justification, previous Chinese immigration violations, criminal record, national security concerns, diplomatic factors, or inconsistencies in the application. China does not typically provide detailed reasons for visa refusals. Refusals are communicated by the embassy/consulate with a generic denial notice. There is no formal appeals process, but applicants can reapply immediately with improved documentation. Engaging a visa agency or immigration consultant familiar with Chinese requirements is advisable. Some nationalities face higher scrutiny. Journalists and researchers may face additional vetting. Tibet and Xinjiang travel may require special permits. The 144-hour transit exemption has strict routing requirements — failure to meet these results in denial at the port of entry.",
    },
    "visa-colombia": {
        "name": "Colombia",
        "visa_types": [
            ("Tourist Visa (V-Visitor)", "90 days, extendable", "USD 52", "Passport, return ticket, financial proof, hotel booking"),
            ("Business Visa (V-Visitor)", "Up to 2 years, 180 days/year", "USD 52", "Business invitation, company registration"),
            ("Work Visa (M-Migrant)", "Up to 3 years", "USD 52-232", "Employment contract, company NIT, qualifications"),
            ("Student Visa (M-Migrant)", "Duration of studies", "USD 52", "University acceptance, financial proof, insurance"),
            ("Digital Nomad Visa (V-Visitor)", "2 years", "USD 52", "Remote work proof, income 3x min wage (~USD 900/month)"),
            ("Retirement Visa (M-Migrant)", "Up to 3 years", "USD 52-232", "Pension income 3x min wage, insurance"),
            ("Investment Visa (M-Migrant)", "Up to 3 years", "USD 52-232", "Investment 100x min wage (~USD 100,000+)"),
            ("Marriage/Partner Visa (M-Migrant)", "Up to 3 years", "USD 52-232", "Colombian spouse/partner, marriage/union certificate"),
            ("Resident Visa (R-type)", "Permanent (renewable every 5 years)", "USD 232-399", "5+ years on M visa, or marriage 3+ years, or investment"),
            ("Transit Visa (V-Visitor)", "Up to 5 days", "Free-USD 52", "Onward ticket, passport"),
        ],
        "processing": [
            ("Tourist Visa (V)", "1-5 business days (online)", "USD 52", "Same day (online)", "N/A"),
            ("Digital Nomad Visa", "1-5 business days (online)", "USD 52", "Same day", "N/A"),
            ("Work Visa (M)", "5-15 business days", "USD 52-232", "3-5 days", "Additional fee"),
            ("Student Visa", "5-10 business days", "USD 52", "2-3 days", "Additional fee"),
            ("Resident Visa", "5-15 business days", "USD 232-399", "3-5 days", "Additional fee"),
        ],
        "health": "Colombia requires a Yellow Fever vaccination certificate for travelers visiting certain regions including the Amazon, Llanos, Pacific coast, and some rural areas. The vaccination must be received at least 10 days before travel. No other mandatory vaccinations are required for entry. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, and rabies (for rural areas). Malaria and dengue precautions are advised for tropical lowland areas. No medical examination is required for tourist visas. Work and residence visa applicants may need health certification. Health insurance (EPS) is mandatory for all residents and M-visa holders — registration with an EPS provider is required within the first month. Tourists are strongly recommended to have travel insurance. Colombia has excellent private healthcare facilities in major cities (Bogotá, Medellín, Cali). Police clearance certificates (apostilled) are required for M and R visa applications. Colombia captures biometric data (fingerprints and photograph) at immigration for all foreign arrivals through the Migración Colombia system.",
        "extension": "Tourist visa extensions (Permiso Temporal de Permanencia or PTP/salvoconducto is different — extension is through Migración Colombia) can be obtained at Migración Colombia offices for an additional 90 days, totaling 180 days per calendar year. The extension fee is approximately COP 110,000. After 180 days, you must leave Colombia for 180 days before returning on tourist status. Many travelers do visa runs to Ecuador or Panama. Work and study visa renewals are submitted through the online Cancillería portal before expiry. Overstay penalties include fines of approximately COP 855,000 per violation, deportation, and entry bans of up to 5 years. Colombia has become more enforcement-oriented in recent years. Working without proper authorization carries fines for both worker and employer. Migración Colombia conducts checks at workplaces and through landlord reporting.",
        "refusal": "Colombian visa refusals may result from: incomplete online application, insufficient financial proof, failure to meet minimum income requirements, criminal record, previous deportations, or inconsistent information. Refusals are communicated online through the Cancillería portal. Applicants can file a recurso de reposición (reconsideration request) within 10 business days, and a recurso de apelación (appeal) within 10 days if reconsideration is denied. Reapplication is permitted immediately with corrected documentation. Colombia's online visa system has made the process more transparent and efficient. Legal representation through a Colombian immigration attorney (abogado de migración) is advisable for complex cases. The reconsideration process typically takes 2-4 weeks. Common mistakes include providing inconsistent dates, insufficient bank statements, or inadequate proof of remote employment for digital nomad visas.",
    },
    "visa-cook-islands": {
        "name": "Cook Islands",
        "visa_types": [
            ("Visitor Permit (Visa-Free)", "31 days", "Free", "Valid passport, return ticket, accommodation proof"),
            ("Extended Visitor Permit", "Up to 6 months", "NZD 100-200", "Immigration approval, financial proof, return ticket"),
            ("Work Permit", "1-2 years", "NZD 200-500", "Employer application, skills shortage, medical"),
            ("Student Permit", "Duration of studies", "NZD 100", "Institution acceptance, financial proof"),
            ("Business Visitor Permit", "31 days", "Free", "Business purpose, no local employment"),
            ("Permanent Residence", "Permanent", "NZD 500-1,000", "Long-term residence, community ties"),
            ("Spousal/Dependent Permit", "Matches sponsor", "NZD 100-200", "Sponsor's permit, relationship proof"),
            ("Transit (Visa-Free)", "24 hours", "Free", "Onward ticket, valid passport"),
            ("Religious/Missionary Permit", "Varies", "NZD 100", "Church sponsorship, purpose documentation"),
            ("Seasonal Worker Permit", "3-6 months", "NZD 200", "Employer sponsorship, seasonal industry"),
        ],
        "processing": [
            ("Visitor Permit", "On arrival", "Free", "N/A", "N/A"),
            ("Extended Visitor Permit", "1-2 weeks", "NZD 100-200", "3-5 days", "NZD 200-400"),
            ("Work Permit", "2-6 weeks", "NZD 200-500", "1-2 weeks", "NZD 400-750"),
            ("Student Permit", "1-3 weeks", "NZD 100", "3-5 days", "NZD 200"),
            ("Permanent Residence", "3-12 months", "NZD 500-1,000", "2-4 months", "Additional fees"),
        ],
        "health": "The Cook Islands does not require mandatory vaccinations for entry from most countries. A Yellow Fever vaccination certificate is required for travelers from endemic areas. Recommended vaccinations include hepatitis A, hepatitis B, and typhoid. Dengue fever is present in the Pacific Islands — mosquito precautions are advised. No medical examination is required for visitor permits. Work permit and permanent residence applicants must undergo a medical examination including chest X-ray and blood tests. Health insurance is strongly recommended as the Cook Islands has limited medical facilities — serious cases require evacuation to New Zealand. The Rarotonga Hospital provides basic care. Police clearance certificates are required for work permits and permanent residence. The Cook Islands immigration collects biometric data (photograph) on arrival. The Cook Islands uses New Zealand dollars and has close ties to New Zealand's immigration system.",
        "extension": "Visitor permits can be extended at the Cook Islands Immigration Division in Rarotonga for additional periods up to a maximum of 6 months total. Extensions require proof of adequate funds and a valid return ticket. The fee is approximately NZD 100-200 per extension. Work permits are renewed through the employer. Overstay penalties include fines of NZD 500-2,000, detention, deportation at the violator's expense, and entry bans. Given the small size of the Cook Islands, immigration violations are quickly detected. Working without a valid work permit carries additional fines. The Cook Islands has a small immigration team but maintains close contact with New Zealand immigration authorities.",
        "refusal": "Cook Islands visa and permit refusals may result from: insufficient financial means, lack of return ticket, criminal record, health concerns, or previous immigration violations. Refusals are communicated by the Immigration Division. There is no formal appeals tribunal, but the Principal Immigration Officer can review decisions. Reapplication is permitted with improved documentation. Port-of-entry refusals result in return on the next available flight. Legal representation on the Cook Islands is limited but available through local legal practitioners. The best approach is to ensure all documentation is complete before arrival, as options are limited once on the islands.",
    },
    "visa-costa-rica": {
        "name": "Costa Rica",
        "visa_types": [
            ("Tourist Visa (Visa-Free for many)", "90 days", "Free-USD 50", "Passport, return ticket, financial proof USD 100/day"),
            ("Business Visa", "30-90 days", "USD 50", "Business invitation, company letter"),
            ("Work Permit (Permiso de Trabajo)", "1 year, renewable", "USD 200-500", "Employment contract, employer sponsorship, DGME approval"),
            ("Student Visa (Visa de Estudiante)", "1 year, renewable", "USD 200", "University acceptance, financial proof"),
            ("Retirement Visa (Pensionado)", "2 years, renewable", "USD 250-300", "Pension income USD 1,000+/month"),
            ("Rentista Visa", "2 years, renewable", "USD 250-300", "Unearned income USD 2,500+/month or USD 60,000 deposit"),
            ("Investor Visa (Inversionista)", "2 years, renewable", "USD 250-300", "Investment of USD 150,000+ in Costa Rica"),
            ("Digital Nomad Visa (Nómada Digital)", "1 year, renewable once", "USD 100", "Remote work proof, income USD 3,000+/month or USD 5,000/family"),
            ("Family Reunification", "1-2 years", "USD 200-300", "First-degree relative with CR residency, relationship proof"),
            ("Transit Visa", "Up to 48 hours", "USD 20-50", "Onward ticket, passport"),
        ],
        "processing": [
            ("Tourist Visa", "3-5 business days (or visa-free)", "Free-USD 50", "1-2 days", "USD 100"),
            ("Digital Nomad Visa", "2-4 weeks", "USD 100", "1 week", "USD 200"),
            ("Work Permit", "3-6 months", "USD 200-500", "1-2 months", "USD 500-800"),
            ("Pensionado/Rentista", "3-6 months", "USD 250-300", "1-2 months", "USD 400-500"),
            ("Investor Visa", "3-6 months", "USD 250-300", "1-2 months", "USD 400-500"),
        ],
        "health": "Costa Rica does not require mandatory vaccinations for entry from most countries. A Yellow Fever vaccination certificate is required for travelers from endemic countries. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, and rabies (for rural areas). Malaria and dengue precautions are advised for lowland areas, particularly the Caribbean coast and northern border regions. No medical examination is required for tourist visas. Residence visa applicants (Pensionado, Rentista, etc.) must provide a health certificate from a Costa Rican doctor or the CCSS (Caja Costarricense de Seguro Social). Health insurance through the CCSS is mandatory for all residents — enrollment is required as part of the residency process and costs approximately 7-11% of declared income. Costa Rica has excellent healthcare through both the public CCSS system and private clinics. Police clearance certificates (apostilled and translated into Spanish) from the applicant's home country are required for all residency applications. Costa Rica uses biometric passport scanning at immigration.",
        "extension": "Tourist visas cannot be officially extended in Costa Rica. The maximum stay is 90 days (or 30 days for some nationalities). Many travelers do a 'border run' to Panama or Nicaragua to reset their 90-day period, which is legal but immigration may question frequent re-entries. To stay longer legally, you must apply for a residence visa. Residence permits are renewed through the DGME (Dirección General de Migración y Extranjería) before expiry. Overstay penalties include fines of approximately USD 100 per month of overstay, deportation, and difficulty obtaining future Costa Rican visas. Fines must be paid before departure. Costa Rica has become stricter with overstay enforcement, especially for those who repeatedly do border runs. Working without authorization carries additional penalties. The DGME conducts workplace inspections, particularly in tourist areas.",
        "refusal": "Costa Rican visa refusals may result from: insufficient financial proof (less than USD 100/day), lack of return ticket, criminal record, previous deportations, or failure to demonstrate temporary intent. Refusals at the airport result in immediate return. Consular refusals can be reconsidered by submitting additional documentation. Residency application refusals can be appealed to the Administrative Tribunal of the DGME within 5 business days. Legal representation through a Costa Rican immigration attorney (abogado de migración) is highly recommended for residency applications. Reapplication is permitted with improved documentation. Common residency refusal reasons include incorrect apostilles, expired documents, or insufficient income proof. The appeal process typically takes 2-4 months.",
    },
    "visa-croatia": {
        "name": "Croatia",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Long-Stay Visa (D-type)", "Over 90 days", "EUR 70-100", "Purpose documentation, financial proof"),
            ("Work Permit (Dozvola za Rad)", "1 year, renewable", "EUR 70-100", "Employer application, labor market test, contract"),
            ("EU Blue Card", "Up to 4 years", "EUR 70-100", "High-qualification job, salary threshold, degree"),
            ("Student Visa", "1 year, renewable", "EUR 70-100", "University acceptance, financial proof EUR 400/month"),
            ("Family Reunification", "1 year, renewable", "EUR 70-100", "Relationship proof, sponsor residence, income proof"),
            ("Digital Nomad Permit", "1 year, non-renewable", "EUR 70-100", "Remote work proof, income EUR 2,540+/month, insurance"),
            ("Self-Employment/Business Visa", "1 year, renewable", "EUR 70-100", "Business plan, investment, registration"),
            ("Retirement Residence", "1 year, renewable", "EUR 70-100", "Pension proof, health insurance"),
            ("Seasonal Work Permit", "Up to 90 days", "EUR 30-50", "Employer seasonal quota, contract"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "2-6 weeks", "EUR 70-100", "1-2 weeks", "EUR 140-200"),
            ("Work Permit", "4-8 weeks", "EUR 70-100", "2-3 weeks", "EUR 140-200"),
            ("Digital Nomad Permit", "2-4 weeks", "EUR 70-100", "1 week", "EUR 140-200"),
            ("Student Visa", "2-4 weeks", "EUR 70-100", "1 week", "EUR 140-200"),
        ],
        "health": "Croatia, as a Schengen Area member (joined January 2023), requires travel medical insurance with minimum EUR 30,000 coverage for short-stay visa applicants. No mandatory vaccinations are required for entry. Long-stay visa applicants must undergo a medical examination at a Croatian health facility. Health insurance is mandatory for all residents — either through the Croatian Health Insurance Fund (HZZO) for workers or approved private insurance. EU/EEA citizens can use their EHIC. Digital nomad permit holders must show proof of health insurance covering Croatia. Police clearance certificates from the applicant's home country (apostilled and translated into Croatian) are required for residence permits. Biometric data (10 fingerprints and photograph) is collected for all Schengen visa applications at Croatian embassies or VFS Global centers. Croatia has good healthcare facilities, especially in Zagreb, Split, and Rijeka.",
        "extension": "Schengen short-stay visas allow 90 days within 180 days and cannot be extended except in exceptional circumstances. National D-type visa holders must register at the local police station within 3 days and apply for a residence permit at the MUP (Ministry of Interior). Digital nomad permits cannot be renewed but a new application can be submitted after leaving Croatia. Residence permits must be renewed 30-60 days before expiry. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines of HRK 3,000-30,000 (EUR 400-4,000), deportation, and Schengen-wide entry bans of 1-5 years recorded in SIS II. Croatia actively enforces immigration compliance since joining the Schengen Area. Working without authorization carries significant penalties for both employee and employer.",
        "refusal": "Croatian visa refusals may be based on: insufficient insurance, inadequate financial proof, incomplete documentation, doubts about travel purpose, previous Schengen violations, or security concerns. Refusals follow the standardized Schengen refusal form. Appeals can be filed within 8 days to the Ministry of Interior (MUP). For residence permits, appeals are filed within 15 days to the Administrative Court. Reapplication is possible immediately with improved documentation. Legal representation through a Croatian immigration attorney (odvjetnik za imigraciju) is recommended. Croatia's refusal rates have adjusted to Schengen standards since accession. The appeal process typically takes 2-4 months. VFS Global centers in many countries handle Croatian visa applications.",
    },
    "visa-cyprus": {
        "name": "Cyprus",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Visa (D-type)", "Over 90 days", "EUR 60-150", "Purpose documentation, financial proof"),
            ("Work Permit (Single Permit)", "1-4 years", "EUR 60-150", "Employer contract, labor department approval"),
            ("Student Visa", "1 year, renewable", "EUR 60-150", "University acceptance, EUR 500/month proof, insurance"),
            ("Family Reunification", "1 year, renewable", "EUR 60-150", "Relationship proof, sponsor income, accommodation"),
            ("Self-Employment/Business Visa", "1 year, renewable", "EUR 60-150", "Business plan, capital EUR 15,000+, registration"),
            ("Digital Nomad Visa", "1 year, renewable once", "EUR 70", "Remote work proof, income EUR 3,500+/month, insurance"),
            ("Permanent Residence (Fast Track)", "Permanent", "EUR 500", "Investment EUR 300,000+ in real estate"),
            ("Retirement/Independent Means", "1 year, renewable", "EUR 60-150", "Income EUR 9,000/year + EUR 4,200/dependent"),
            ("Seasonal Worker Permit", "Up to 9 months", "EUR 60", "Employer seasonal quota, contract"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "4-8 weeks", "EUR 60-150", "2-3 weeks", "EUR 120-250"),
            ("Work Permit", "4-12 weeks", "EUR 60-150", "2-4 weeks", "EUR 120-250"),
            ("Digital Nomad Visa", "2-4 weeks", "EUR 70", "1 week", "EUR 140"),
            ("Fast Track PR", "2-3 months", "EUR 500", "1-2 months", "EUR 750"),
        ],
        "health": "Cyprus requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants. No mandatory vaccinations are required for entry. Long-stay visa and residence permit applicants must undergo a medical examination at a government hospital or approved clinic in Cyprus, including chest X-ray, blood tests (HIV, hepatitis B/C, syphilis), and a general physical exam. Registration with the General Healthcare System (GHS/GESY) is mandatory for all legal residents and provides comprehensive healthcare coverage. EU/EEA citizens can use their EHIC. Private health insurance is required for digital nomad visa holders. Police clearance certificates from the applicant's home country and any country of residence (apostilled and translated into English or Greek) are required for all residence applications. Biometric data is collected for Schengen visa applications. Cyprus has modern healthcare facilities, particularly in Nicosia, Limassol, and Larnaca.",
        "extension": "Schengen short-stay visas allow 90 days within 180 days and generally cannot be extended. National visa holders must apply for a residence permit at the Civil Registry and Migration Department within 7 days of arrival. Residence permits are renewable 1-2 months before expiry. Digital nomad visas can be renewed for one additional year. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines, detention, deportation, and entry bans. Cyprus has become part of the Schengen Area (air and sea from 2024), meaning overstays are recorded in the SIS II database. Working without authorization carries fines for both employee and employer. The Migration Department conducts compliance checks. Voluntary departure before detection may reduce penalties.",
        "refusal": "Cyprus visa refusals may result from: insufficient travel insurance, inadequate financial proof, incomplete documentation, doubts about purpose of stay, previous immigration violations, or security concerns. Refusals use the standardized form with specific reasons. Appeals can be filed within 15 days to the Administrative Court. For residence permits, the Reviewing Authority can hear appeals. Reapplication is possible immediately with improved documentation. Legal representation through a Cypriot immigration lawyer is recommended. Cyprus's digital nomad visa has relatively high approval rates with proper documentation. The appeal process typically takes 2-6 months. The Migration Department website provides detailed guidance on requirements.",
    },
    "visa-czech-republic": {
        "name": "Czech Republic",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Long-Stay Visa (D-type)", "Up to 1 year", "CZK 2,500 (EUR 100)", "Purpose documentation, financial proof"),
            ("Employee Card (Zaměstnanecká karta)", "Up to 2 years, renewable", "CZK 2,500", "Job offer in Labor Office database, qualifications"),
            ("EU Blue Card", "Up to 3 years", "CZK 2,500", "High-qualification job, salary 1.5x average, degree"),
            ("Student Visa (Long-Stay)", "1 year, renewable", "CZK 2,500", "University acceptance, CZK 124,500/year proof"),
            ("Family Reunification", "1 year, renewable", "CZK 2,500", "Relationship proof, sponsor residence, income threshold"),
            ("Business/Self-Employment Visa (Živnostenský List)", "1 year, renewable", "CZK 2,500", "Trade license, business plan, financial proof"),
            ("Intra-Company Transfer", "Up to 3 years", "CZK 2,500", "ICT card, multinational company, management/specialist role"),
            ("Zivno Visa (Freelancer)", "1 year, renewable", "CZK 2,500", "Trade license (Živnostenský list), proof of income"),
            ("Permanent Residence", "Permanent (renewable every 10 years)", "CZK 2,500", "5 years continuous residence, Czech B1 language"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "2-4 months", "CZK 2,500", "N/A (long wait)", "N/A"),
            ("Employee Card", "2-4 months", "CZK 2,500", "N/A", "N/A"),
            ("Student Visa", "2-3 months", "CZK 2,500", "N/A", "N/A"),
            ("Permanent Residence", "2-4 months", "CZK 2,500", "N/A", "N/A"),
        ],
        "health": "The Czech Republic requires travel medical insurance with minimum EUR 30,000 coverage for all Schengen short-stay visa applicants. No mandatory vaccinations are required for entry. Long-stay visa applicants (D-type) must obtain comprehensive health insurance valid in the Czech Republic — either public health insurance (VZP) for employees or approved private insurance (e.g., PVZP) for others. The minimum coverage must be CZK 60,000 (approx EUR 2,500). Medical examinations are not routinely required for visa applications but may be requested. Residence permit holders who are employed are covered by Czech public health insurance. Police clearance certificates from all countries of residence are required for long-stay visas and must be apostilled/superlegalized and translated into Czech by a court-appointed translator. Biometric data (10 fingerprints and photograph) is collected for Schengen visa applications and for biometric residence cards. The Czech Republic has excellent healthcare, particularly in Prague and Brno.",
        "extension": "Schengen short-stay visas allow 90 days within 180 days and cannot be extended except in exceptional circumstances at the OAMP (Department for Asylum and Migration Policy). Long-stay visa holders must apply for a residence permit at the regional OAMP office before their visa expires. Residence permits are renewable, and applications should be submitted 120-14 days before expiry. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines of CZK 3,000-10,000, deportation, and Schengen-wide entry bans of 1-5 years recorded in SIS II. Administrative expulsion proceedings can result in longer bans. The Czech Republic is known for strict immigration enforcement. Working without an Employee Card carries fines for both employee (CZK 2,000-5,000) and employer (up to CZK 500,000). Voluntary departure before detection may reduce penalties.",
        "refusal": "Czech visa refusals may result from: insufficient financial proof, inadequate insurance, incomplete documentation, doubts about purpose of travel/return intention, previous Schengen violations, or security concerns. The Czech Republic has notably long processing times for D-type visas (often 2-4 months). Refusals follow the Schengen standardized form for C-type visas. D-type visa refusals can be appealed within 15 days to the Commission for Decision-Making on Residence Matters under the Ministry of Interior. Reapplication is possible immediately. Legal representation through a Czech immigration attorney (advokát pro cizinecké právo) is recommended. The Czech Republic has invested in modernizing its immigration system, but processing backlogs remain common. Appointment availability at Czech embassies can be limited — plan well ahead.",
    },
    "visa-denmark": {
        "name": "Denmark",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Long-Stay Visa (D-type)", "Over 90 days", "DKK 3,025 (EUR 400)", "Purpose documentation, financial proof"),
            ("Work Permit (Opholdstilladelse på baggrund af arbejde)", "Up to 4 years", "DKK 3,025", "Employment contract, salary DKK 465,000+/year, Fast-Track/Pay Limit"),
            ("Start-Up Denmark (Entrepreneur)", "2 years, renewable", "DKK 3,025", "Approved business plan by Danish Business Authority"),
            ("Student Visa", "Duration of studies", "DKK 2,250", "University admission, DKK 6,397/month proof"),
            ("Family Reunification", "Matches sponsor", "DKK 8,280", "24-year rule, financial proof, accommodation, integration"),
            ("EU Blue Card", "Up to 4 years", "DKK 3,025", "High-qualification job, salary threshold, degree"),
            ("Au Pair Visa", "Up to 2 years", "DKK 3,025", "Host family agreement, age 18-30"),
            ("Researcher Visa", "Duration of research", "DKK 3,025", "Hosting agreement, research institution"),
            ("Greenland/Faroe Islands Work Permit", "Varies", "DKK 3,025", "Specific permit for Greenland/Faroe employment"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("Work Permit (Fast-Track)", "2-4 weeks", "DKK 3,025", "10 business days", "DKK 3,025"),
            ("Work Permit (Pay Limit)", "1-3 months", "DKK 3,025", "N/A", "N/A"),
            ("Student Visa", "1-3 months", "DKK 2,250", "N/A", "N/A"),
            ("Family Reunification", "3-10 months", "DKK 8,280", "N/A", "N/A"),
        ],
        "health": "Denmark requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants. No mandatory vaccinations are required for entry. Long-stay visa holders who register with a Danish municipality and obtain a CPR number are covered by the Danish public healthcare system (Sundhedsvæsenet), which provides comprehensive free healthcare. Until CPR registration, private health insurance is necessary. Students must show proof of health insurance for the initial period. Medical examinations may be required for certain residence permits. Police clearance certificates from all countries of residence are required for work and residence permits. Biometric data (fingerprints and photograph) is collected for all Schengen visa applications and for residence cards at the SIRI (Danish Agency for International Recruitment and Integration) service centers. Denmark has an excellent healthcare system consistently ranked among the world's best.",
        "extension": "Schengen visas allow 90 days within 180 days and cannot be extended. Work and residence permit holders must apply for renewal through SIRI's online portal (nyidanmark.dk) before their current permit expires. The renewal application must be submitted at least 3 months before expiry. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines starting at DKK 3,000, deportation, and Schengen-wide entry bans of 2-5 years. Denmark is known for strict immigration enforcement. Re-entry bans are recorded in the SIS II database. Working without authorization carries criminal penalties. Denmark's Udlændingestyrelsen (Immigration Service) and police actively monitor compliance. Greenland and the Faroe Islands have separate immigration rules from mainland Denmark.",
        "refusal": "Danish visa refusals may result from: insufficient financial proof, inadequate insurance, failure to meet salary thresholds (for work permits), incomplete documentation, doubts about genuine purpose, previous Schengen violations, or security concerns. Family reunification has strict requirements including the 24-year rule, attachment requirement, accommodation standards, and financial guarantees. Refusals are issued with reasons. Appeals for residence permits can be filed with the Immigration Appeals Board (Udlændingenævnet) within 8 weeks. Schengen C-type refusals are handled through the administrative appeals process. Reapplication is possible with improved documentation. Legal representation through a Danish immigration attorney (advokat for udlændingeret) is strongly recommended. Denmark's immigration system is considered one of the more restrictive in the EU. Processing times can be lengthy — plan well in advance.",
    },
    "visa-ecuador": {
        "name": "Ecuador",
        "visa_types": [
            ("Tourist Entry (Visa-Free for most)", "90 days", "Free", "Passport, return ticket, financial proof"),
            ("Tourist Visa (for visa-required nationalities)", "90 days", "USD 50", "Passport, return ticket, hotel booking, financial proof"),
            ("Professional Work Visa (12-VI)", "2 years, renewable", "USD 400-500", "Employment contract, employer sponsorship"),
            ("Student Visa (12-V)", "Duration of studies", "USD 200-400", "University acceptance, financial proof"),
            ("Investor Visa (12-II)", "2 years, renewable", "USD 400-500", "Investment USD 40,000+ in Ecuador"),
            ("Retirement Visa (Jubilado) (9-I)", "Indefinite", "USD 50-200", "Pension income USD 1,375+/month"),
            ("Rentista Visa (9-II)", "Indefinite", "USD 50-200", "Fixed income USD 1,375+/month from abroad"),
            ("Professional Visa (9-V)", "Indefinite", "USD 50-200", "Professional degree, employment in Ecuador"),
            ("Family Reunification (Amparo) (9-VI)", "Indefinite", "USD 50-200", "Ecuadorian family member, relationship proof"),
            ("Digital Nomad Visa", "2 years", "USD 400-500", "Remote work proof, income USD 1,375+/month"),
        ],
        "processing": [
            ("Tourist (Visa-Free)", "On arrival", "Free", "N/A", "N/A"),
            ("Work Visa", "3-8 weeks", "USD 400-500", "1-2 weeks", "USD 600-750"),
            ("Retirement Visa", "3-6 weeks", "USD 50-200", "1-2 weeks", "USD 200-400"),
            ("Student Visa", "2-4 weeks", "USD 200-400", "1 week", "USD 400-600"),
            ("Digital Nomad Visa", "2-4 weeks", "USD 400-500", "1 week", "USD 600-750"),
        ],
        "health": "Ecuador requires a Yellow Fever vaccination certificate for travelers visiting the Amazon region (Oriente) and recommends it for all visitors. Other recommended vaccinations include hepatitis A, hepatitis B, typhoid, and rabies (for Amazon travel). Malaria and dengue precautions are advised for lowland areas. No medical examination is required for tourist visas. Residence visa applicants must undergo a medical examination at an approved Ecuadorian clinic. Health insurance is mandatory for all residents and visa holders. Ecuador's public healthcare system (IESS) is available to contributors, and private insurance is widely used. Police clearance certificates (apostilled) from the applicant's home country and any country of residence in the past 5 years are required for all residence visa applications. Ecuador collects biometric data at immigration checkpoints. The Galápagos Islands have special entry requirements including a Transit Control Card (TCT) fee of USD 20.",
        "extension": "Tourist stays can be extended at the Ministry of Foreign Affairs offices for an additional 90 days, for a total of 180 days per year. The extension fee is approximately USD 110. After 180 days, you must leave Ecuador or obtain a residence visa. Residence visas are renewed at the Ministry of Foreign Affairs before expiry. Overstay penalties include fines of approximately USD 200-2,000, deportation, and entry bans of 1-3 years. Ecuador's Cancillería (Ministry of Foreign Affairs) handles all immigration matters. Working without proper authorization is penalized with fines and deportation. Ecuador generally has accessible and affordable visa processes compared to many countries.",
        "refusal": "Ecuadorian visa refusals may result from: incomplete documentation, insufficient financial proof, criminal record, previous immigration violations, or failure to meet income thresholds. Refusals are communicated by the Cancillería. Applicants can file a reconsideration request within 10 business days. Appeals can be escalated to the administrative courts. Reapplication is permitted immediately with improved documentation. Legal representation through an Ecuadorian immigration attorney is advisable. Ecuador's visa system was reformed in 2017 under the Organic Law of Human Mobility (LOMH), making processes more structured. Common mistakes include inadequate apostilles on foreign documents and insufficient bank statements.",
    },
    "visa-egypt": {
        "name": "Egypt",
        "visa_types": [
            ("Tourist eVisa (Single Entry)", "30 days", "USD 25", "Online application, passport scan, credit card"),
            ("Tourist eVisa (Multiple Entry)", "30 days per entry, 180 days validity", "USD 60", "Online application, passport scan, credit card"),
            ("Visa on Arrival", "30 days", "USD 25", "Eligible nationalities, passport, cash USD"),
            ("Business Visa", "30-90 days", "USD 60-100", "Business invitation from Egyptian company"),
            ("Work Visa", "1 year, renewable", "USD 200-500", "Employer sponsorship, work permit from Ministry of Manpower"),
            ("Student Visa", "Duration of studies", "USD 50-100", "University acceptance, financial proof"),
            ("Transit Visa", "Up to 48 hours", "USD 15-25", "Onward ticket, passport"),
            ("Family/Dependent Visa", "1 year, renewable", "USD 100-200", "Sponsor's work permit, relationship proof"),
            ("Investment Visa", "1-5 years", "USD 200-500", "Investment in Egypt, company registration"),
            ("Journalist Visa", "As approved", "USD 100-200", "Press credentials, security clearance"),
        ],
        "processing": [
            ("Tourist eVisa", "3-7 business days", "USD 25-60", "Same day (online)", "N/A"),
            ("Visa on Arrival", "On arrival (minutes)", "USD 25", "N/A", "N/A"),
            ("Business Visa", "5-10 business days", "USD 60-100", "2-3 days", "USD 120-200"),
            ("Work Visa", "4-12 weeks", "USD 200-500", "2-4 weeks", "USD 400-750"),
            ("Student Visa", "2-6 weeks", "USD 50-100", "1-2 weeks", "USD 100-200"),
        ],
        "health": "Egypt does not require mandatory vaccinations for entry from most countries. A Yellow Fever vaccination certificate is required for travelers from endemic countries. COVID-19 requirements have been largely relaxed. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, and rabies. No medical examination is required for tourist visas. Work visa applicants must undergo a medical examination at a government-approved hospital in Egypt, including HIV testing, chest X-ray, and blood tests for hepatitis. Health insurance is recommended but not mandatory for tourists. Work permit holders should have employer-provided health insurance. Police clearance certificates from the applicant's home country are required for work and residence visas. Egypt collects biometric data (photograph and fingerprints) at its airports. Schistosomiasis precautions are advised for travelers who may come in contact with freshwater in the Nile Delta and rural areas.",
        "extension": "Tourist visas can be extended at the Mogamma (Government Complex) in Tahrir Square, Cairo, or at local passport offices for an additional 30 days. The extension fee is approximately EGP 500-1,000. Some travelers do a 'Sinai only' entry for a free 15-day permit. Maximum tourist stay with extensions is generally 6 months. Work permit renewals are handled through the employer and the Ministry of Manpower. Overstay penalties include fines of EGP 1,000-5,000, detention, deportation (at the violator's expense), and entry bans of 1-3 years. Egypt is generally flexible about short overstays (a few days), but longer overstays trigger penalties. Fines are calculated per day/week of overstay and must be paid before departure or upon detection. Egypt's Directorate of Passports, Immigration and Nationality handles immigration enforcement.",
        "refusal": "Egyptian visa refusals may result from: nationality restrictions, incomplete documentation, security concerns, previous immigration violations, or specific travel restrictions (e.g., Israeli passport stamps — though this is no longer generally enforced). eVisa refusals are communicated online. Port-of-entry refusals result in immediate return. There is no formal public appeals process for tourist visa refusals. Work visa refusals can be reconsidered through the employer. Reapplication is possible immediately with corrected documentation. Engaging a local immigration facilitator or attorney is advisable for work visa matters. Certain nationalities face additional scrutiny and may require security clearance. Egypt's visa policies have become more accessible with the introduction of the eVisa system.",
    },
    "visa-fiji": {
        "name": "Fiji",
        "visa_types": [
            ("Visitor Permit (Visa-Free)", "4 months", "Free", "Valid passport, return ticket, accommodation proof, financial proof"),
            ("Tourist Visa (for visa-required nationalities)", "4 months", "FJD 93 (USD 42)", "Passport, return ticket, financial proof"),
            ("Work Permit", "Up to 3 years", "FJD 255-545 (USD 115-245)", "Employer application, skills shortage, qualifications"),
            ("Student Visa", "Duration of studies", "FJD 255 (USD 115)", "University acceptance, financial proof, insurance"),
            ("Business Visitor Permit", "14-30 days", "Free-FJD 93", "Business purpose documentation"),
            ("Investor Permit", "3-7 years", "FJD 545 (USD 245)", "Investment FJD 250,000+ in Fiji"),
            ("Dependent Permit", "Matches sponsor", "FJD 93 (USD 42)", "Sponsor's valid permit, relationship proof"),
            ("Transit Permit", "Up to 72 hours", "Free", "Onward ticket, valid passport"),
            ("Retired Person Permit", "1-3 years", "FJD 255", "Income FJD 40,000+/year, health insurance"),
            ("Yacht Permit", "Varies", "FJD 93", "Yacht registration, clearance documentation"),
        ],
        "processing": [
            ("Visitor Permit", "On arrival", "Free", "N/A", "N/A"),
            ("Work Permit", "4-8 weeks", "FJD 255-545", "2-3 weeks", "FJD 500-800"),
            ("Student Visa", "2-4 weeks", "FJD 255", "1 week", "FJD 400"),
            ("Investor Permit", "4-8 weeks", "FJD 545", "2-3 weeks", "FJD 800"),
            ("Tourist Visa", "3-5 business days", "FJD 93", "1-2 days", "FJD 186"),
        ],
        "health": "Fiji requires a Yellow Fever vaccination certificate for travelers arriving from endemic countries. No other mandatory vaccinations are required. Recommended vaccinations include hepatitis A, hepatitis B, and typhoid. Dengue fever and Zika virus are present — mosquito precautions are essential. No medical examination is required for visitor permits. Work permit applicants must undergo a medical examination at a Fiji-approved clinic including chest X-ray and blood tests. Health insurance is strongly recommended as medical facilities in Fiji are limited, with the main hospital (CWM) in Suva. Serious medical cases may require evacuation to Australia or New Zealand. Police clearance certificates from the applicant's home country are required for work and residence permits. Fiji Immigration collects biometric data at Nadi and Suva airports. COVID-19 requirements have been relaxed but may be reinstated based on health conditions.",
        "extension": "Visitor permits can be extended at the Fiji Immigration Department in Suva or Nadi for additional periods, up to a maximum of 6 months total. Extension fee is approximately FJD 123 per extension. Work permits are renewed through the employer before expiry. Overstay penalties include fines of FJD 500-5,000, detention, deportation at the violator's expense, and entry bans of 1-5 years. Working without a valid work permit carries fines of FJD 10,000 and/or imprisonment of up to 2 years. Fiji Immigration conducts regular compliance checks. Overstayers are typically detained at the Fiji Immigration Detention Centre pending removal. The maximum fine for serious immigration offenses is FJD 20,000 and/or 5 years imprisonment.",
        "refusal": "Fiji visa refusals may result from: insufficient financial proof, lack of return ticket, criminal record, previous immigration violations, or health concerns. Refusals at the port of entry result in return on the next available flight. Consular refusals are communicated in writing. The Director of Immigration can review refusal decisions. There is no formal appeals tribunal, but judicial review is available through the Fiji courts. Reapplication is permitted with improved documentation. Legal representation through a Fiji-qualified lawyer is advisable for complex cases. Fiji is generally welcoming to tourists and visa refusal rates are low for genuine travelers. Work permit refusals often relate to the labor market test showing available local workers.",
    },
    "visa-finland": {
        "name": "Finland",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Visa (D-type)", "Over 90 days", "EUR 80", "Purpose documentation, financial proof"),
            ("Work Residence Permit (Specialist)", "Up to 2 years", "EUR 520", "Employment contract, salary requirement, specialist role"),
            ("Seasonal Work Permit", "Up to 9 months", "EUR 280", "Employer application, seasonal industry"),
            ("Student Residence Permit", "Duration of studies + 1 year", "EUR 450", "University admission, EUR 6,720/year proof, insurance"),
            ("Family Reunification", "Up to 4 years", "EUR 520", "Relationship proof, sponsor income EUR 1,000+/month net"),
            ("Self-Employed Residence Permit", "Up to 2 years", "EUR 520", "Business plan approved by ELY Centre, financial viability"),
            ("Startup Visa", "2 years", "EUR 520", "Business Finland endorsement, innovative business"),
            ("Researcher Residence Permit", "Duration of research", "EUR 520", "Hosting agreement, research institution"),
            ("Permanent Residence Permit (P)", "Permanent (renewed every 4 years)", "EUR 200", "4 years continuous residence, Finnish/Swedish B1, income"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("Work Permit (Specialist)", "1-4 months", "EUR 520", "2 weeks (Fast Track)", "EUR 520"),
            ("Student Permit", "1-3 months", "EUR 450", "N/A", "N/A"),
            ("Family Reunification", "4-9 months", "EUR 520", "N/A", "N/A"),
            ("Startup Visa", "1-3 months", "EUR 520", "N/A", "N/A"),
        ],
        "health": "Finland requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants. No mandatory vaccinations are required for entry. Residence permit holders who work or study in Finland are entitled to Finnish public healthcare through Kela (Social Insurance Institution). Students must show proof of health insurance — EU students can use EHIC; non-EU students need private insurance (at least EUR 100,000 for stays over 2 years). Medical examinations are not routinely required but may be requested for certain residence permits. Police clearance certificates from all countries of residence are required for work and residence permits. Biometric data (10 fingerprints and photograph) is collected at Finnish embassies or VFS Global centers for all visa and residence permit applications. Finland's healthcare system is among the best in the world. Tuberculosis screening may be required for applicants from high-incidence countries.",
        "extension": "Schengen short-stay visas allow 90 days within 180 days and generally cannot be extended. Residence permit renewals must be submitted through the Enter Finland online portal or at a Finnish Immigration Service (Migri) office before the current permit expires. Continuous presence requirements vary by permit type. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include deportation, entry bans of up to 5 years across the Schengen Area (recorded in SIS II), and potential criminal charges. Finland is strict about immigration compliance but generally fair and transparent. Working without a valid permit carries fines for both employee and employer. The Finnish Border Guard (Rajavartiolaitos) and police enforce immigration law. Voluntary departure before an enforcement action may reduce consequences.",
        "refusal": "Finnish visa refusals may result from: insufficient financial proof, inadequate insurance, incomplete documentation, failure to demonstrate genuine purpose, previous Schengen violations, or security concerns. Refusals follow the standardized Schengen form for C-type visas. Residence permit refusals can be appealed to the Administrative Court (Hallinto-oikeus) within 30 days. A further appeal to the Supreme Administrative Court is possible on legal questions. Reapplication is possible with improved documentation. Legal representation through a Finnish immigration attorney is recommended. Finland's Migri provides detailed guidance online and has service points across the country. The appeal process typically takes 3-6 months. Finland's immigration system is transparent and decisions are well-documented.",
    },
    "visa-france": {
        "name": "France",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel/attestation d'accueil, financial proof"),
            ("National Long-Stay Visa (VLS-TS)", "1 year (equivalent to residence permit)", "EUR 99-200", "Purpose documentation, financial proof"),
            ("Work Visa (Salarié/Travailleur Temporaire)", "1-4 years", "EUR 99-200", "Employer petition, DIRECCTE approval, contract"),
            ("Talent Passport (Passeport Talent)", "Up to 4 years", "EUR 99", "Innovative project, investor, researcher, artist, or skilled worker"),
            ("Student Visa (VLS-TS Étudiant)", "1 year, renewable", "EUR 99", "Campus France procedure, university acceptance, EUR 615/month"),
            ("Family Reunification (Regroupement Familial)", "1 year, renewable", "EUR 99-200", "Sponsor income, housing requirements, relationship proof"),
            ("Visitor Visa (Visiteur)", "1 year, renewable", "EUR 99-200", "No work intent, income proof, insurance"),
            ("Working Holiday Visa (PVT)", "1 year", "Free-EUR 99", "Age 18-30, bilateral agreement country"),
            ("Entrepreneur Visa (part of Talent Passport)", "Up to 4 years", "EUR 99", "Business plan, investment EUR 30,000+, economic contribution"),
            ("Retirement Visa (Retraité)", "10 years, renewable", "EUR 99-200", "Pension income, French pension or previous residence"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days (emergency only)", "EUR 80"),
            ("VLS-TS (Long-Stay)", "2-8 weeks", "EUR 99-200", "N/A", "N/A"),
            ("Talent Passport", "2-6 weeks", "EUR 99", "N/A", "N/A"),
            ("Student Visa", "2-6 weeks", "EUR 99", "N/A", "N/A"),
            ("Family Reunification", "4-12 months", "EUR 99-200", "N/A", "N/A"),
        ],
        "health": "France requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants. No mandatory vaccinations are required for entry into metropolitan France. For French overseas territories (Guyane, Mayotte, etc.), additional vaccinations may be required, including Yellow Fever for French Guiana. Long-stay visa holders must undergo a medical examination by OFII (Office Français de l'Immigration et de l'Intégration) within 3 months of arrival, including a chest X-ray, general health check, and vision/hearing tests. Residents are covered by the French healthcare system (Assurance Maladie/Sécurité Sociale) through CPAM, one of the world's best healthcare systems. EU/EEA citizens can use the EHIC. Students are covered by the French social security system. Police clearance certificates (extrait de casier judiciaire) from the home country (apostilled and translated into French by a sworn translator) are required for long-stay visas. Biometric data (fingerprints and photograph) is collected for Schengen visa applications at VFS Global/TLS Contact centers.",
        "extension": "Schengen short-stay visas allow 90 days within 180 days and cannot be extended except in extraordinary circumstances at the prefecture. VLS-TS (long-stay visa validated as residence permit) holders must validate their visa online within 3 months of arrival via the ANEF portal. Residence permit renewals (carte de séjour) must be submitted 2-4 months before expiry at the prefecture or online. Maximum tourist stay is 90 days per 180-day period. Overstay results in an OQTF (Obligation de Quitter le Territoire Français), with an entry ban of 1-3 years across the Schengen Area. Fines of up to EUR 3,750 may be imposed. Deportation costs are borne by the state. France maintains immigration detention centers (CRA) for removal proceedings. Working without authorization carries criminal penalties for both employee and employer. The préfecture handles all residence matters.",
        "refusal": "French visa refusals may result from: insufficient financial proof (less than EUR 65/day for tourism), inadequate insurance, incomplete documentation, doubts about return intention, previous Schengen violations, or security concerns. Refusals include specific reasons on the standardized form. Schengen C-type refusals can be challenged before the Commission de Recours contre les Refus de Visa (CRRV) within 2 months, and then before the Administrative Tribunal of Nantes (Tribunal Administratif de Nantes) within 2 months after CRRV decision. Long-stay visa refusals follow the same procedure. Legal representation (avocat en droit des étrangers) is recommended. Reapplication is possible immediately with improved documentation. France processes more Schengen visa applications than any other country, with a refusal rate varying by consulate. The VFS Global/TLS Contact network handles applications worldwide.",
    },
    "visa-georgia": {
        "name": "Georgia",
        "visa_types": [
            ("Visa-Free Entry (most nationalities)", "1 year", "Free", "Valid passport"),
            ("Short-Stay Visa (C-type)", "90 days within 180 days", "GEL 40 (USD 15)", "Passport, invitation or hotel booking, financial proof"),
            ("Long-Stay Visa (D-type)", "Up to 1 year", "GEL 80 (USD 30)", "Purpose documentation, financial proof"),
            ("Work Permit", "1 year, renewable", "GEL 100-300 (USD 38-115)", "Employment contract, employer registration"),
            ("Student Visa", "Duration of studies", "GEL 80 (USD 30)", "University acceptance, financial proof"),
            ("Family Reunification", "1 year, renewable", "GEL 80 (USD 30)", "Relationship proof, sponsor residency"),
            ("Investment Residence", "1-2 years", "GEL 300-500", "Investment GEL 300,000+ (approx USD 115,000)"),
            ("Freelancer/Remote Worker", "Up to 1 year (visa-free)", "Free", "Passport, self-employment proof"),
            ("Diplomatic/Official Visa", "Varies", "Free", "Government invitation"),
            ("Permanent Residence", "Permanent (renewed every 6 years)", "GEL 180 (USD 70)", "6 years residence or investment/marriage qualification"),
        ],
        "processing": [
            ("Visa-Free Entry", "On arrival", "Free", "N/A", "N/A"),
            ("Short-Stay Visa (C)", "5-10 business days", "GEL 40", "1-3 days", "GEL 80"),
            ("Long-Stay Visa (D)", "2-4 weeks", "GEL 80", "3-5 days", "GEL 160"),
            ("Work Permit", "2-4 weeks", "GEL 100-300", "1 week", "GEL 200-500"),
            ("Permanent Residence", "1-3 months", "GEL 180", "2-4 weeks", "GEL 360"),
        ],
        "health": "Georgia does not require mandatory vaccinations for entry. A Yellow Fever vaccination certificate may be required for travelers from endemic countries. Recommended vaccinations include hepatitis A, hepatitis B, and rabies (for rural areas). No medical examination is required for tourist or short-stay visits. Work and residence permit applicants may need a medical certificate. Georgia provides universal healthcare coverage to its citizens and legal residents. Tourists are not covered and should have comprehensive travel insurance. Health insurance is recommended but not mandatory for most visa types. Police clearance certificates from the applicant's home country are required for residence permits. Georgia has simplified its immigration procedures significantly and is considered one of the easiest countries for foreign residents. Biometric data is collected at Georgian border crossings. Georgia's healthcare is affordable but facilities outside Tbilisi are limited.",
        "extension": "For citizens of visa-free countries, the 1-year stay allowance is generous and rarely requires extension. For visa holders, extensions can be obtained at the Public Service Hall (PSH) before the visa expires. Work permits are renewed through the employer. Overstay penalties are relatively moderate: fines of GEL 180-360, potential deportation, and entry bans of 1-3 years. Georgia is generally lenient and pragmatic about immigration matters. Many visitors from visa-free countries simply leave and re-enter to reset their 1-year period. Working without proper authorization is technically illegal but enforcement is limited. The Public Service Hall provides efficient immigration services throughout the country.",
        "refusal": "Georgian visa refusals are relatively rare, especially given the country's liberal visa policies. Refusals may result from: security concerns, criminal record, previous deportations, or specific restrictions on certain nationalities. Refusals are communicated in writing. Applicants can appeal within 1 month to the Ministry of Internal Affairs or to the court. Reapplication is permitted immediately. Georgia's open immigration policy means most refusals are security-related rather than documentation-based. Legal representation is available through Georgian law firms but is rarely needed for straightforward applications. The Public Service Hall website provides comprehensive application guidance.",
    },
    "visa-germany": {
        "name": "Germany",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Visa (D-type)", "3-6 months (entry visa)", "EUR 75", "Purpose documentation, financial proof"),
            ("Work Visa (Fachkräfteeinwanderung)", "Up to 4 years", "EUR 75", "Employer contract, recognized qualifications, German/English"),
            ("EU Blue Card", "Up to 4 years", "EUR 75", "Salary EUR 45,300+ (STEM: EUR 41,000+), degree"),
            ("Job Seeker Visa (Chancenkarte)", "6-12 months", "EUR 75", "Points system, degree, German A1/English B2, experience"),
            ("Student Visa", "Duration of studies", "EUR 75", "University admission, EUR 11,904/year blocked account"),
            ("Family Reunification (Familiennachzug)", "Matches sponsor", "EUR 75", "German A1 (for spouses), income, adequate housing"),
            ("Self-Employment/Freelance Visa (Selbständige)", "Up to 3 years", "EUR 75", "Business plan, client contracts, experience, financial proof"),
            ("Researcher Visa", "Duration + 9 months job search", "EUR 75", "Hosting agreement, research contract"),
            ("Permanent Settlement Permit (Niederlassungserlaubnis)", "Permanent", "EUR 113", "5 years residence, German B1, pension contributions"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "4-12 weeks", "EUR 75", "N/A", "N/A"),
            ("EU Blue Card", "4-12 weeks", "EUR 75", "Fast-Track: 3-4 weeks", "EUR 411"),
            ("Student Visa", "4-12 weeks", "EUR 75", "N/A", "N/A"),
            ("Chancenkarte", "4-12 weeks", "EUR 75", "N/A", "N/A"),
        ],
        "health": "Germany requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants. No mandatory vaccinations are required, though measles vaccination proof is required for children attending schools and daycare. National visa and residence permit holders must have health insurance — Germany has mandatory health insurance (Gesetzliche Krankenversicherung or GKV for employees earning below the threshold, or Private Krankenversicherung/PKV for those above). Students must prove adequate health insurance (statutory or equivalent private). Police clearance certificates (Führungszeugnis equivalent from home country, apostilled and translated by a sworn translator into German) are required for all national visa applications. Biometric data is collected at German embassies or VFS Global centers. Germany's healthcare system is among the world's best, with mandatory coverage for all residents. TB screening may be required for applicants from high-incidence countries.",
        "extension": "Schengen short-stay visas allow 90 days within 180 days and cannot be extended except in exceptional circumstances. National visa holders must register at the local Bürgeramt within 14 days and apply for a residence permit (Aufenthaltserlaubnis) at the Ausländerbehörde before their visa expires. Residence permits must be renewed 2-3 months before expiry. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines, deportation, and Schengen-wide entry bans of 1-5 years in SIS II. Germany is strict about enforcement. Working without authorization is a criminal offense. The Ausländerbehörde and police enforce immigration law. Appointments at the Ausländerbehörde can be very difficult to obtain, especially in Berlin and Munich — plan well ahead.",
        "refusal": "German visa refusals may result from: insufficient financial proof (EUR 50+/day for tourism), inadequate insurance, incomplete documentation, failure to demonstrate return intention, previous Schengen violations, or security concerns. Refusals use the standardized Schengen form. Schengen C-type refusals can be challenged through Remonstration (informal review by the embassy within 1 month) or by filing a lawsuit at the Berlin Administrative Court (Verwaltungsgericht Berlin) within 1 month. National visa refusals follow the same process. Legal representation by an immigration attorney (Rechtsanwalt für Ausländerrecht) is strongly recommended. Germany receives among the highest numbers of visa applications worldwide. Appointment availability at German embassies can be a significant challenge — booking months in advance is advisable.",
    },
    "visa-greece": {
        "name": "Greece",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Visa (D-type)", "Over 90 days", "EUR 150", "Purpose documentation, financial proof"),
            ("Work Visa", "1 year, renewable", "EUR 150", "Employment contract, employer filing, labor approval"),
            ("EU Blue Card", "Up to 2 years", "EUR 150", "High-qualification job, salary threshold, degree"),
            ("Student Visa", "1 year, renewable", "EUR 150", "University acceptance, EUR 400/month proof, insurance"),
            ("Family Reunification", "1-2 years", "EUR 150", "Relationship proof, sponsor income, 2+ years residence"),
            ("Investment/Golden Visa", "5 years, renewable", "EUR 2,000", "Real estate EUR 250,000+ (EUR 500,000 in some areas)"),
            ("Digital Nomad Visa", "1 year, renewable", "EUR 75", "Remote work proof, income EUR 3,500+/month"),
            ("Self-Employment/Business Visa", "1-2 years", "EUR 150", "Business plan, capital, registration"),
            ("Financially Independent Person", "2 years, renewable", "EUR 150", "Income EUR 2,000+/month (no work in Greece)"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "4-12 weeks", "EUR 150", "2-4 weeks", "EUR 250"),
            ("Golden Visa", "2-6 months", "EUR 2,000", "1-2 months", "EUR 2,000"),
            ("Digital Nomad Visa", "2-4 weeks", "EUR 75", "1 week", "EUR 150"),
            ("Student Visa", "4-8 weeks", "EUR 150", "2-3 weeks", "EUR 250"),
        ],
        "health": "Greece requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants. No mandatory vaccinations are required for entry. Long-stay visa and residence permit applicants must undergo a medical examination at a Greek public hospital, including tests for infectious diseases (tuberculosis, hepatitis, HIV). Health insurance is mandatory for all residents — either through the Greek National Health System (ESY/EOPYY) for workers or approved private insurance. EU/EEA citizens can use the EHIC. Digital nomad visa holders must show proof of comprehensive health insurance. Police clearance certificates (apostilled and translated into Greek by an authorized translator) are required for D-type visas and residence permits. Biometric data is collected for Schengen visa applications and biometric residence cards. Greece has good healthcare facilities in major cities (Athens, Thessaloniki) but more limited services on the islands.",
        "extension": "Schengen visas allow 90 days within 180 days and cannot be extended. National visa holders must apply for a residence permit at the local Aliens and Immigration Division within 30 days of arrival. Residence permits must be renewed 2 months before expiry. Golden Visa holders can renew every 5 years as long as they maintain the qualifying investment. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines, deportation, and Schengen-wide entry bans in SIS II. Greece has become stricter about immigration enforcement. Working without authorization carries penalties for both employee and employer. The Digital Nomad Visa cannot be used for local employment. Greece's processing times can be slow, especially during tourist season.",
        "refusal": "Greek visa refusals may result from: insufficient financial proof, inadequate insurance, incomplete documentation, doubts about purpose/return intention, previous Schengen violations, or security concerns. Refusals use the standardized Schengen form. Appeals can be filed within 30 days to the Greek embassy or consulate that issued the refusal, or through the administrative courts. Golden Visa refusals can be challenged at the Administrative Court. Reapplication is possible immediately with improved documentation. Legal representation through a Greek immigration attorney (dikigoros metanasteftikis nomothesias) is recommended. Greece's Golden Visa program has been very popular but recent reforms have increased the minimum investment threshold in high-demand areas.",
    },
    "visa-guatemala": {
        "name": "Guatemala",
        "visa_types": [
            ("Tourist Visa (CA-4 region visa-free)", "90 days (CA-4 area)", "Free for many nationalities", "Passport, return ticket, financial proof"),
            ("Tourist Visa (for visa-required nationalities)", "90 days", "USD 25-50", "Passport, return ticket, hotel booking, financial proof"),
            ("Business Visa", "90 days", "USD 25-50", "Business invitation, company letter"),
            ("Work Permit (Permiso de Trabajo)", "1 year, renewable", "USD 100-300", "Employment contract, employer application, IGM approval"),
            ("Student Visa", "Duration of studies", "USD 50-100", "University acceptance, financial proof"),
            ("Residency Visa (Residencia Temporal)", "1-2 years", "USD 200-400", "Purpose-specific, financial proof, police clearance"),
            ("Permanent Residency (Residencia Permanente)", "Permanent", "USD 300-500", "5+ years temporary residence, financial stability"),
            ("Pensionado (Retirement) Visa", "1 year, renewable", "USD 200-300", "Pension income USD 1,000+/month"),
            ("Investor Visa (Rentista)", "1-2 years", "USD 200-400", "Investment in Guatemala, business plan"),
            ("Transit Visa", "72 hours", "Free-USD 25", "Onward ticket, passport"),
        ],
        "processing": [
            ("Tourist Visa", "3-5 business days (or visa-free)", "Free-USD 50", "1-2 days", "USD 50-100"),
            ("Work Permit", "4-8 weeks", "USD 100-300", "2-3 weeks", "USD 200-450"),
            ("Residency Visa", "4-12 weeks", "USD 200-400", "2-4 weeks", "USD 400-600"),
            ("Student Visa", "2-4 weeks", "USD 50-100", "1 week", "USD 100-200"),
            ("Pensionado Visa", "4-8 weeks", "USD 200-300", "2-3 weeks", "USD 300-450"),
        ],
        "health": "Guatemala does not require mandatory vaccinations for entry from most countries. A Yellow Fever vaccination certificate is required for travelers from endemic countries. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, rabies (for rural areas), and malaria prophylaxis for lowland areas (Petén, Izabal). No medical examination is required for tourist visas. Residency and work visa applicants must provide a medical certificate from a Guatemalan doctor. Health insurance is recommended but not mandatory for tourists. Guatemala has decent private hospitals in Guatemala City (Herrera Llerandi, Centro Médico) but limited facilities in rural areas. Police clearance certificates (apostilled and translated into Spanish) from the applicant's home country are required for all residency applications. Guatemala collects biometric data at La Aurora International Airport and land border crossings.",
        "extension": "Tourist visas under the CA-4 agreement (Guatemala, Honduras, El Salvador, Nicaragua) allow 90 days total across all four countries. Extensions of up to 90 additional days can be obtained at the IGM (Instituto Guatemalteco de Migración) in Guatemala City. The extension fee is approximately GTQ 200-500 (USD 25-65). After 180 days total, you must leave the CA-4 region for 72 hours before re-entry. Residency permits are renewed at the IGM before expiry. Overstay penalties include fines of approximately GTQ 50-200 per day, deportation, and entry bans of 1-3 years across the CA-4 region. Guatemala is moderately strict about overstays. Working without authorization carries additional penalties.",
        "refusal": "Guatemalan visa refusals may result from: incomplete documentation, insufficient financial means, criminal record, previous deportations, or security concerns. Refusals are communicated by the consulate or at the border. IGM refusals for residency can be reconsidered by submitting additional documentation. There is no formal appeals tribunal, but administrative reconsideration is possible. Reapplication is permitted with improved documentation. Legal representation through a Guatemalan immigration attorney (abogado de migración) is advisable for residency applications. Guatemala's immigration system is less formalized than North American or European systems. The best approach is thorough preparation of documentation before application.",
    },
    "visa-hong-kong": {
        "name": "Hong Kong",
        "visa_types": [
            ("Visa-Free Entry (170+ nationalities)", "7-180 days (varies)", "Free", "Valid passport, return ticket"),
            ("Tourist Visa (Pre-Arrival Registration)", "90 days", "Free (online)", "Eligible nationalities, passport details"),
            ("Employment Visa", "1-2 years, renewable", "HKD 230 (USD 30)", "Job offer, employer sponsorship, qualifications"),
            ("Investment Visa (Entrepreneur)", "1-2 years, renewable", "HKD 230", "Business plan, capital HKD 1M+, economic benefit"),
            ("Student Visa", "Duration of studies", "HKD 230", "University acceptance, financial proof, sponsor"),
            ("Dependent Visa", "Matches sponsor", "HKD 230", "Sponsor's employment visa, relationship proof"),
            ("Quality Migrant Admission Scheme (QMAS)", "1 year, renewable", "HKD 230", "Points-based, qualifications, experience, achievements"),
            ("Top Talent Pass Scheme (TTPS)", "2 years", "HKD 230", "Salary HKD 2.5M+ or top 100 university + 3 years experience"),
            ("Working Holiday Visa", "1 year", "HKD 230", "Age 18-30, bilateral agreement country"),
            ("Training Visa", "12-24 months", "HKD 230", "Company-sponsored training program"),
        ],
        "processing": [
            ("Visa-Free Entry", "On arrival", "Free", "N/A", "N/A"),
            ("Employment Visa", "4-8 weeks", "HKD 230", "2-3 weeks", "N/A"),
            ("QMAS", "6-12 months", "HKD 230", "N/A", "N/A"),
            ("Top Talent Pass", "4 weeks", "HKD 230", "2 weeks", "N/A"),
            ("Student Visa", "4-6 weeks", "HKD 230", "2-3 weeks", "N/A"),
        ],
        "health": "Hong Kong does not require mandatory vaccinations for entry from most countries. A Yellow Fever vaccination certificate is required for travelers from endemic areas. No medical examination is required for visitors or tourist entry. Employment and investment visa applicants are not required to undergo medical examinations as part of the visa process, though employers may require health checks. Health insurance is not mandatory for visitors but is strongly recommended — Hong Kong has excellent but expensive private healthcare. Public hospitals charge non-residents significantly more than residents. Domestic helpers must have employer-provided medical insurance. Police clearance certificates are not routinely required for employment visas but may be requested. Hong Kong Immigration collects biometric data (fingerprints) from certain visa applicants and at immigration checkpoints. Hong Kong has world-class healthcare facilities, including Queen Mary Hospital and Prince of Wales Hospital.",
        "extension": "Visa-free entry periods vary by nationality (7 to 180 days) and generally cannot be extended beyond the initial allowance. Employment visa holders can apply for extension at the Immigration Department (ImmD) at least 4 weeks before expiry. Extensions are typically granted for 2-3 year periods on the pattern 1-2-2-3 years. Student visa extensions require continued enrollment. Overstay is a criminal offense in Hong Kong: penalties include fines of HKD 50,000 and imprisonment of up to 2 years. Working without proper authorization carries the same penalties. Hong Kong Immigration actively enforces immigration law with detention and deportation. The Immigration Department conducts spot checks at workplaces. Overstayers are typically prosecuted before deportation. Entry bans of 1-5+ years may be imposed.",
        "refusal": "Hong Kong visa refusals may result from: insufficient qualifications for the role, failure to demonstrate genuine job offer, inability to show the position cannot be filled locally, criminal record, previous immigration violations, or security concerns. Employment visa refusals often relate to the 'local labor first' policy. Refusals are communicated in writing by ImmD. Appeals can be made by submitting additional documentation or a letter of appeal to the Director of Immigration. There is no formal appeals tribunal, but judicial review is available through the High Court. QMAS refusals are points-based and can be improved by enhancing qualifications or achievements. Reapplication is permitted immediately. Immigration consultants registered with ImmD can assist with applications. The Top Talent Pass Scheme has relatively high approval rates for qualifying applicants.",
    },
    "visa-hungary": {
        "name": "Hungary",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Long-Stay Visa (D-type)", "Over 90 days", "EUR 60-110", "Purpose documentation, financial proof"),
            ("Work Permit (Single Permit)", "Up to 2 years", "EUR 60-110", "Employer application, labor office approval, contract"),
            ("EU Blue Card", "Up to 4 years", "EUR 60-110", "High-qualification job, salary threshold, degree"),
            ("Student Visa", "1 year, renewable", "EUR 60-110", "University acceptance, HUF 1M/year proof, insurance"),
            ("Family Reunification", "1 year, renewable", "EUR 60-110", "Relationship proof, sponsor income, accommodation"),
            ("White Card (Guest Investor Visa)", "10 years", "EUR N/A (bond investment)", "EUR 250,000+ government bond purchase"),
            ("Business/Self-Employment Visa", "1-2 years", "EUR 60-110", "Business plan, company registration, capital"),
            ("Researcher Visa", "Duration of research", "EUR 60-110", "Hosting agreement, research institution"),
            ("Permanent Residence", "Permanent (renewed every 5 years)", "EUR 60", "3-5 years residence, Hungarian B1, income"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "2-6 weeks", "EUR 60-110", "1-2 weeks", "EUR 120-200"),
            ("Work Permit", "3-8 weeks", "EUR 60-110", "1-3 weeks", "EUR 120-200"),
            ("Student Visa", "2-4 weeks", "EUR 60-110", "1 week", "EUR 120-200"),
            ("White Card", "3-4 weeks", "Bond + fees", "2 weeks", "N/A"),
        ],
        "health": "Hungary requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants. No mandatory vaccinations are required for entry. Long-stay visa applicants may need a medical certificate confirming freedom from communicable diseases. Health insurance is mandatory for all residents — either through the Hungarian National Health Insurance Fund (OEP/NEAK) for workers or approved private insurance. EU/EEA citizens can use the EHIC. Students must show proof of adequate health insurance. Police clearance certificates from the applicant's home country (apostilled and translated into Hungarian by an authorized translator) are required for D-type visas and residence permits. Biometric data (fingerprints and photograph) is collected for all Schengen visa applications and biometric residence cards. Hungary has good healthcare facilities, especially in Budapest, though there can be long wait times in the public system.",
        "extension": "Schengen visas allow 90 days within 180 days and cannot be extended. National visa holders must apply for a residence permit at the Immigration and Asylum Office (OIF) within 30 days of arrival. Residence permits must be renewed before expiry. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include fines of HUF 50,000-200,000, deportation, and Schengen-wide entry bans of 1-5 years in SIS II. Hungary actively enforces immigration law. Working without authorization carries fines for both employee and employer. The OIF handles all immigration matters. Voluntary departure before detection may reduce consequences. Hungary's White Card program provides an expedited pathway for investors.",
        "refusal": "Hungarian visa refusals may result from: insufficient financial proof, inadequate insurance, incomplete documentation, doubts about purpose/return intention, previous Schengen violations, or security concerns. Refusals use the standardized Schengen form. Appeals for D-type visas can be filed within 15 days to the administrative court. Schengen C-type refusals can be challenged through remonstration or court proceedings. Reapplication is possible with improved documentation. Legal representation through a Hungarian immigration attorney (bevándorlási ügyvéd) is recommended. Hungary has specific requirements that may differ from other Schengen states. The appeal process typically takes 2-4 months.",
    },
    "visa-iceland": {
        "name": "Iceland",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("Work Residence Permit", "Up to 2 years, renewable", "ISK 15,000 (EUR 100)", "Job offer, employer application, Directorate of Labour"),
            ("Student Residence Permit", "Duration of studies", "ISK 15,000", "University acceptance, ISK 171,000/month proof, insurance"),
            ("Family Reunification", "Matches sponsor", "ISK 15,000", "Relationship proof, sponsor income, accommodation"),
            ("Self-Employment Permit", "Up to 2 years", "ISK 15,000", "Business plan, financial viability, skills"),
            ("Au Pair Permit", "Up to 2 years", "ISK 15,000", "Host family contract, age 18-25"),
            ("Specialist/Expert Work Permit", "Up to 2 years", "ISK 15,000", "Specialist skills, employer application"),
            ("Seasonal Work Permit", "Up to 6 months", "ISK 15,000", "Employer, seasonal industry"),
            ("Humanitarian Protection", "Varies", "Free", "Protection application"),
            ("Long-Term Residence (EU status)", "Permanent", "ISK 15,000", "5 years continuous residence, Icelandic A2"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("Work Permit", "4-12 weeks", "ISK 15,000", "2-4 weeks", "ISK 25,000"),
            ("Student Permit", "4-8 weeks", "ISK 15,000", "2-3 weeks", "ISK 25,000"),
            ("Family Reunification", "4-8 weeks", "ISK 15,000", "2-3 weeks", "ISK 25,000"),
            ("Long-Term Residence", "3-6 months", "ISK 15,000", "1-2 months", "ISK 25,000"),
        ],
        "health": "Iceland requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants (as part of the Schengen Area through the EEA). No mandatory vaccinations are required for entry. Residence permit holders are registered with the Icelandic Health Insurance (Sjúkratryggingar Íslands) after registering their domicile and obtaining a kennitala (national ID number). Healthcare in Iceland is comprehensive and high-quality, though costs for uninsured visitors are very high. Students and workers with valid permits are covered by the national health system. Police clearance certificates from all countries of residence are required for residence permits, translated into Icelandic or English by an authorized translator. Biometric data is collected for Schengen visa applications. Iceland's clean environment means few tropical disease risks, though cold weather preparation is essential.",
        "extension": "Schengen visas allow 90 days within 180 days and generally cannot be extended. Residence permit holders must apply for renewal at the Directorate of Immigration (Útlendingastofnun) before their current permit expires. Applications should be submitted well in advance due to processing times. Maximum tourist stay is 90 days per 180-day period. Overstay penalties include deportation and Schengen-wide entry bans of 1-5 years. Iceland enforces immigration law strictly despite its small population. Working without authorization carries penalties. The Directorate of Immigration handles all immigration matters from their Reykjavik office. Iceland's labor market is small and specialized — work permits are often tied to specific industries facing labor shortages.",
        "refusal": "Icelandic visa refusals may result from: insufficient financial proof, inadequate insurance, incomplete documentation, doubts about purpose of visit, previous Schengen violations, or security concerns. Refusals follow the standardized Schengen form. Residence permit refusals can be appealed to the Immigration and Asylum Appeals Board (Kærunefnd útlendingamála) within 15 days. Schengen visa refusals can be challenged through the same board. Reapplication is possible with improved documentation. Legal representation is available through Icelandic attorneys. Iceland's immigration system is transparent and well-organized. The appeal process typically takes 2-3 months. The Directorate of Immigration website (utl.is) provides comprehensive guidance in English.",
    },
    "visa-india": {
        "name": "India",
        "visa_types": [
            ("e-Tourist Visa (30 days)", "30 days, single/double entry", "USD 10-25", "Online application, passport scan, photo"),
            ("e-Tourist Visa (1 year)", "1 year, multiple entry, 90 days/visit", "USD 25-40", "Online application, passport scan, photo"),
            ("e-Tourist Visa (5 years)", "5 years, multiple entry, 90 days/visit", "USD 80", "Online application, passport scan, photo"),
            ("e-Business Visa", "1 year, 180 days/visit", "USD 80", "Business invitation, company details"),
            ("Employment Visa", "1-5 years", "USD 100-250", "Job offer USD 25,000+/year, employer contract, consular application"),
            ("Student Visa", "Duration of studies", "USD 100", "University acceptance, financial proof"),
            ("e-Medical Visa", "60 days, triple entry", "USD 25", "Hospital appointment letter"),
            ("Transit Visa", "72 hours", "USD 25", "Onward ticket, passport"),
            ("OCI Card (Overseas Citizen of India)", "Lifetime", "USD 275", "Indian origin or spouse of Indian origin"),
            ("Research Visa", "Duration of research", "USD 100-250", "Institution approval, government clearance"),
        ],
        "processing": [
            ("e-Tourist Visa", "1-3 business days", "USD 10-80", "Same day (online)", "N/A"),
            ("e-Business Visa", "1-3 business days", "USD 80", "Same day (online)", "N/A"),
            ("Employment Visa", "3-8 weeks", "USD 100-250", "1-2 weeks", "Additional fees"),
            ("Student Visa", "3-6 weeks", "USD 100", "1-2 weeks", "Additional fees"),
            ("OCI Card", "4-8 weeks", "USD 275", "2-3 weeks", "Additional fees"),
        ],
        "health": "India requires specific health precautions depending on areas visited. A Yellow Fever vaccination certificate is mandatory for travelers arriving from or transiting through yellow fever endemic countries. Malaria prophylaxis is strongly recommended for most areas outside major cities and high altitudes. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, Japanese encephalitis (for rural areas), rabies, and cholera. No routine medical examination is required for eVisa applicants. Employment and student visa holders staying more than 1 year must register with the FRRO (Foreigners Regional Registration Office) within 14 days and may need health screening. Health insurance is strongly recommended as India has excellent private hospitals but costs can be significant. The e-Medical Visa facilitates medical tourism. Police clearance certificates from the applicant's home country are required for employment and student visas. India collects biometric data (fingerprints and photograph) at all international airports for foreign nationals. Dengue and chikungunya precautions are important throughout India.",
        "extension": "e-Tourist Visas (30-day) cannot be extended. The 1-year and 5-year e-Tourist Visas allow multiple entries within their validity period but individual stays are limited to 90 days (60 for some nationalities). Employment visa holders can extend through the FRRO/e-FRRO online system. Student visa extensions require continued enrollment and FRRO approval. Overstay penalties include fines of USD 300 for each year of overstay (or part thereof), possible detention, deportation, and entry bans. India's Bureau of Immigration maintains comprehensive records. FRRO registration is mandatory for stays exceeding 180 days on applicable visa types. Working on a tourist visa is strictly prohibited and carries severe penalties. India occasionally offers amnesty for long-term overstayers. The e-FRRO online system (indianfrro.gov.in) has streamlined many extension and registration processes.",
        "refusal": "Indian visa and eVisa refusals may result from: nationality restrictions (Pakistan, Pakistani-origin), incomplete application, inconsistent information, criminal record, previous Indian immigration violations, or security concerns. eVisa refusals are communicated online with limited explanation. Consular visa refusals are communicated in writing. There is no formal appeals process for eVisa refusals — applicants can reapply immediately. Consular visa refusals can be reconsidered by submitting additional documentation. Some nationalities face additional scrutiny or are ineligible for eVisas. Journalists, researchers, and missionaries may face additional clearance requirements. Engaging a visa agency experienced with Indian visas is advisable for complex cases. The Indian eVisa system processes millions of applications annually with high approval rates for straightforward tourist applications.",
    },
    "visa-indonesia": {
        "name": "Indonesia",
        "visa_types": [
            ("Visa on Arrival (VoA)", "30 days, extendable once", "IDR 500,000 (USD 32)", "Eligible nationality, passport, return ticket"),
            ("Visa-Free Entry (certain nationalities)", "30 days, non-extendable", "Free", "Eligible nationality passport, return ticket"),
            ("e-Visa (B211A - Tourist/Social)", "60 days", "IDR 1,500,000 (USD 96)", "Online application, sponsor or agent, passport"),
            ("Business Visa (B211A - Business)", "60 days", "IDR 1,500,000", "Business invitation, Indonesian company sponsor"),
            ("KITAS (Temporary Stay Permit)", "1-2 years", "USD 200-1,200", "Employer/sponsor, work permit (IMTA), qualifications"),
            ("Student Visa (C316)", "1 year, renewable", "USD 100-200", "University acceptance, sponsor"),
            ("Retirement Visa (KITAS Lansia)", "1 year, renewable", "USD 300-500", "Age 55+, insurance, USD 1,500+/month income"),
            ("Second Home Visa (B2)", "5-10 years", "USD 300-500", "Savings IDR 2 billion (USD 130,000+), insurance"),
            ("Digital Nomad Visa (B211A-Remote Worker)", "1 year", "IDR 1,500,000", "Remote employment, income USD 5,000+/month (proposed threshold)"),
            ("KITAP (Permanent Stay Permit)", "5 years, renewable", "USD 500-1,000", "4+ consecutive years on KITAS, Indonesian spouse, or investor"),
        ],
        "processing": [
            ("Visa on Arrival", "On arrival (minutes)", "IDR 500,000", "N/A", "N/A"),
            ("e-Visa B211A", "3-7 business days", "IDR 1,500,000", "1-2 days", "IDR 2,000,000+"),
            ("KITAS (Work)", "4-8 weeks", "USD 200-1,200", "2-4 weeks", "USD 500-2,000"),
            ("Student Visa", "2-4 weeks", "USD 100-200", "1 week", "USD 200-400"),
            ("Second Home Visa", "5-10 business days", "USD 300-500", "2-3 days", "USD 500-800"),
        ],
        "health": "Indonesia requires a Yellow Fever vaccination certificate for travelers from endemic countries. No other mandatory vaccinations are required but recommended vaccinations include hepatitis A, hepatitis B, typhoid, Japanese encephalitis, rabies, and malaria prophylaxis (for rural areas especially Papua, Kalimantan, Sulawesi). Dengue fever is endemic throughout Indonesia — mosquito precautions are essential. No medical examination is required for tourist visas or VoA. KITAS holders must undergo a medical examination at an approved Indonesian clinic. Health insurance is recommended for tourists and mandatory for KITAS holders. Indonesia has excellent private hospitals in Jakarta (Siloam, Pondok Indah) and Bali (BIMC, Kasih Ibu) but facilities in remote areas are limited. Police clearance certificates (SKCK equivalent from home country) are required for KITAS applications. Indonesia collects biometric data at all international airports.",
        "extension": "Visa on Arrival can be extended once for 30 additional days at the local immigration office (Kantor Imigrasi). The extension fee is approximately IDR 500,000. Visa-free entries cannot be extended. e-Visa B211A can be extended up to 3 times (60 days each). KITAS renewals are handled through the sponsor/employer before expiry. Overstay penalties are IDR 1,000,000 per day (approximately USD 64) for the first 60 days. After 60 days of overstay, the violator is detained, placed in immigration detention (Rudenim), deported, and given an entry ban of 1-5 years. The daily fine is enforced strictly. Indonesia has cracked down on visa violations, particularly in Bali. Working without a valid work permit (IMTA/KITAS) carries fines and deportation. Immigration conducts regular sweeps, especially in tourist areas and coworking spaces.",
        "refusal": "Indonesian visa refusals may result from: nationality restrictions, criminal record, previous immigration violations (especially overstays), incomplete documentation, or security concerns. VoA refusals at the airport are rare but possible. e-Visa refusals are communicated online. KITAS refusals may relate to employer non-compliance or incomplete work permit documentation. There is no formal appeals process for tourist visa refusals. KITAS refusals can be reconsidered through the sponsor/employer submitting corrected documentation. Reapplication is possible after addressing refusal reasons. Engaging a licensed Indonesian visa agent (PPIU) is common and advisable for all non-tourist visa types. Indonesia's immigration system has been digitized significantly, with most applications now processed through the online imigrasi.go.id portal.",
    },
    "visa-iran": {
        "name": "Iran",
        "visa_types": [
            ("Tourist Visa", "30 days", "USD 40-100 (varies by nationality)", "Passport, invitation/reference code, itinerary, insurance"),
            ("Visa on Arrival (Tourist)", "30 days", "USD 40-75", "Eligible nationalities, passport, insurance, hotel booking"),
            ("Business Visa", "30-90 days", "USD 60-150", "Business invitation from Iranian company, MFA authorization"),
            ("Work Visa", "1 year, renewable", "USD 100-300", "Employer sponsorship, Ministry of Labor approval"),
            ("Student Visa", "Duration of studies", "USD 50-100", "University acceptance, Ministry of Science approval"),
            ("Pilgrimage Visa (Ziyarat)", "14-30 days", "USD 20-40", "Pilgrimage group registration, religious site itinerary"),
            ("Press/Journalist Visa", "As approved", "USD 100-200", "IRNA/ISNA accreditation, Ministry of Culture approval"),
            ("Transit Visa", "Up to 7 days", "USD 20-40", "Onward ticket, passport"),
            ("Family/Dependent Visa", "1 year, renewable", "USD 50-100", "Iranian spouse or parent, relationship proof"),
            ("Medical Tourism Visa", "30-90 days", "USD 40-60", "Hospital appointment, medical records"),
        ],
        "processing": [
            ("Tourist Visa", "5-14 business days", "USD 40-100", "2-3 days", "USD 80-150"),
            ("Visa on Arrival", "On arrival (30 min-2 hours)", "USD 40-75", "N/A", "N/A"),
            ("Business Visa", "7-21 business days", "USD 60-150", "3-5 days", "USD 120-250"),
            ("Work Visa", "4-12 weeks", "USD 100-300", "2-4 weeks", "USD 200-450"),
            ("Student Visa", "4-8 weeks", "USD 50-100", "2-3 weeks", "USD 100-200"),
        ],
        "health": "Iran does not require mandatory vaccinations for most travelers. A Yellow Fever vaccination certificate is required for travelers from endemic countries. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, and rabies (for rural areas). No medical examination is required for tourist visas. Work and student visa applicants may need medical screening. Health insurance is mandatory for all tourist visa applicants and visa on arrival — proof of insurance must be shown. Iran has excellent and affordable healthcare, particularly in Tehran (Milad Hospital, Imam Khomeini Hospital). Medical tourism is significant in Iran for procedures like cosmetic surgery. Police clearance certificates may be required for work and residence visas. Iran collects biometric data (fingerprints and photograph) at all ports of entry. Important note: possession of alcohol and certain medications is illegal in Iran — travelers should verify prohibited substances before travel.",
        "extension": "Tourist visas can be extended at the local Police Department (Foreign Affairs Office) for additional 30-day periods, generally up to a total of 90 days. The extension fee is approximately IRR 2,000,000-5,000,000. The process is usually straightforward in major cities (Isfahan, Shiraz, Tehran). Work permits are renewed through the employer before expiry. Overstay penalties include daily fines, potential detention, deportation, and entry bans. Iran is generally lenient about short overstays if you are proactive about extensions. Longer overstays can result in detention and deportation. US, UK, and Canadian citizens face additional restrictions including mandatory guided tours through authorized agencies. Foreign nationals must register within 8 days of arrival if their accommodation does not register them automatically.",
        "refusal": "Iranian visa refusals may result from: nationality restrictions (US, UK, Canadian citizens face additional scrutiny and cannot travel independently), Israeli passport stamps (entry is denied), incomplete documentation, security concerns, or previous immigration violations. Some nationalities may find their MFA authorization code denied. There is no formal appeals process for tourist visa refusals. Applicants can reapply with stronger documentation or through a different travel agency. Business visa refusals can be reconsidered through the Iranian company sponsor. Iran does not admit holders of Israeli passports and may refuse entry to travelers with evidence of travel to Israel. Engaging an authorized Iranian travel agency is essential for US, UK, and Canadian citizens. Iran's visa policies can change based on diplomatic relations.",
    },
    "visa-iraq": {
        "name": "Iraq",
        "visa_types": [
            ("Tourist Visa", "30-60 days", "USD 50-77", "Passport, invitation or hotel booking, return ticket"),
            ("Visa on Arrival (KRI/Federal)", "30 days", "USD 75 (KRI free for some)", "Passport, return ticket, hotel details"),
            ("Business Visa", "30-90 days", "USD 50-100", "Business invitation from Iraqi company"),
            ("Work Visa", "1 year, renewable", "USD 100-300", "Employer sponsorship, labor ministry approval"),
            ("Student Visa", "Duration of studies", "USD 50-100", "University acceptance, financial proof"),
            ("Journalist Visa", "As approved", "USD 50-100", "Press credentials, security clearance"),
            ("Kurdistan Region Visa (KRI-VOA)", "30 days", "Free-USD 75", "Passport, eligible nationality"),
            ("Transit Visa", "Up to 72 hours", "USD 25-50", "Onward ticket, passport"),
            ("Diplomatic/Official Visa", "Varies", "Free", "Government invitation"),
            ("Religious Visa (Ziyarat)", "30 days", "USD 40-50", "Pilgrimage group, religious site itinerary"),
        ],
        "processing": [
            ("Tourist Visa", "5-15 business days", "USD 50-77", "2-3 days", "USD 100-150"),
            ("KRI Visa on Arrival", "On arrival (30 min)", "Free-USD 75", "N/A", "N/A"),
            ("Business Visa", "5-15 business days", "USD 50-100", "2-3 days", "USD 100-200"),
            ("Work Visa", "4-12 weeks", "USD 100-300", "2-4 weeks", "USD 200-450"),
            ("Student Visa", "3-6 weeks", "USD 50-100", "1-2 weeks", "USD 100-200"),
        ],
        "health": "Iraq does not require mandatory vaccinations for most travelers, though a Yellow Fever vaccination certificate is required for travelers from endemic countries. Recommended vaccinations include hepatitis A, hepatitis B, typhoid, rabies, and polio (Iraq had recent polio cases). Malaria prophylaxis may be recommended for southern regions. No medical examination is required for tourist visas. Work visa applicants may need medical screening including HIV testing. Health insurance is strongly recommended as medical facilities vary greatly across Iraq. The Kurdistan Region has better healthcare infrastructure than other areas. Medical evacuation insurance is essential as serious cases may need evacuation to Jordan, Turkey, or the UAE. Police clearance certificates are required for work visas. Iraq collects biometric data at airports and border crossings. Security conditions vary by region — travelers should check current advisories.",
        "extension": "Tourist visas can be extended at the local Residency Office (Mudiriyat al-Jawazat) for additional 30-day periods. The extension fee is approximately USD 20-50. The Kurdistan Region has its own immigration procedures through the KRI Residency Directorate. Work permits are renewed through the employer. Overstay penalties include fines (calculated per day), detention, deportation, and entry bans. Iraq is generally pragmatic about visa extensions but enforcement varies by region. The Kurdistan Region tends to be more flexible and organized. Working without proper authorization is penalized. Security checks are common throughout Iraq. Extended stays may require registration with local authorities.",
        "refusal": "Iraqi visa refusals may result from: nationality restrictions, security concerns, incomplete documentation, previous immigration violations, or diplomatic factors. Some nationalities face additional security screening. Israeli passport holders are denied entry. Refusals are communicated by the embassy or at the border. There is no formal public appeals process. Applicants can reapply with improved documentation. The Kurdistan Region has its own visa authority and may have different policies from federal Iraq. Business visa refusals can be reconsidered through the Iraqi company sponsor. Engaging a local facilitator or travel agency familiar with Iraqi visa procedures is advisable. Iraq's visa policies can change based on security conditions and diplomatic relations.",
    },
    "visa-ireland": {
        "name": "Ireland",
        "visa_types": [
            ("Short-Stay C Visa (Tourist)", "Up to 90 days", "EUR 60 (single), EUR 100 (multi)", "Passport, travel insurance, accommodation, financial proof"),
            ("Short-Stay C Visa (Business)", "Up to 90 days", "EUR 60", "Business invitation, company letter"),
            ("Employment Permit (Critical Skills)", "2 years", "EUR 1,000", "Job offer EUR 32,000+ (Critical Skills list), degree"),
            ("Employment Permit (General)", "2 years, renewable", "EUR 1,000", "Job offer EUR 30,000+, labor market test"),
            ("Study Visa (Stamp 2)", "Duration of studies", "EUR 60-100", "College acceptance, EUR 10,000 proof, insurance"),
            ("Working Holiday Visa", "1 year", "Free-EUR 60", "Age 18-30, bilateral agreement country"),
            ("Family Reunification (Join Family)", "Varies", "EUR 60-100", "Irish resident sponsor, relationship proof"),
            ("Start-Up Entrepreneur Programme (STEP)", "2 years, renewable", "EUR 350", "Innovative business, EUR 50,000+ funding"),
            ("Investor Visa (IIP - Suspended 2023)", "5 years", "N/A (program under review)", "Investment EUR 1M+ (program currently suspended)"),
            ("Stamp 4 (Residency)", "Varies", "EUR 300", "Various qualifying paths, INIS approval"),
        ],
        "processing": [
            ("Short-Stay C Visa", "4-8 weeks", "EUR 60-100", "N/A (no express)", "N/A"),
            ("Critical Skills Permit", "4-8 weeks", "EUR 1,000", "2-4 weeks (Trusted Partner)", "EUR 1,000"),
            ("Study Visa", "4-8 weeks", "EUR 60-100", "N/A", "N/A"),
            ("Working Holiday", "4-8 weeks", "Free-EUR 60", "N/A", "N/A"),
            ("STEP", "4-8 weeks", "EUR 350", "N/A", "N/A"),
        ],
        "health": "Ireland does not require mandatory vaccinations for entry. No medical examination is required for tourist or short-stay visas. Work permit and residence applicants may need to undergo a medical examination. Ireland does not participate in the Schengen Area but has its own visa system. The Common Travel Area (CTA) with the UK allows free movement between Ireland and the UK. Health insurance is not mandatory for EU/EEA citizens who can access the public health system with an EHIC. Non-EEA nationals must show proof of private health insurance for visa applications. Students need private medical insurance. Ireland's public health system (HSE) provides care through the medical card scheme for qualifying residents. Police clearance certificates (Garda vetting equivalent from home country) are required for work permit and residence applications. Ireland collects biometric data for Irish Residence Permit (IRP) cards, including fingerprints and photograph.",
        "extension": "Tourist stays in Ireland are limited to the period stamped in your passport by the immigration officer (usually 90 days). Extensions can be requested at the local Garda National Immigration Bureau (GNIB) or the Burgh Quay Registration Office in Dublin. Work permit holders can renew through the Department of Enterprise, Trade and Employment online system. Students must register with GNIB/IRP and renew annually. Maximum tourist stay is generally 90 days. Overstay penalties include deportation orders, entry bans, and difficulty obtaining future Irish or UK visas (due to the CTA). Ireland does not impose daily fines but overstay records affect all future applications. Working without proper authorization is an offense. The Department of Justice handles immigration enforcement. Ireland's immigration system is separate from the EU/Schengen system.",
        "refusal": "Irish visa refusals commonly result from: insufficient financial evidence (must show EUR 3,000+ for tourists), weak ties to home country, incomplete documentation, previous immigration violations in Ireland or the UK/CTA, or credibility concerns. Refusals are communicated in writing with specific reasons. Applicants can submit an appeal within 2 months of the refusal to the Visa Appeals Officer at the Irish Naturalisation and Immigration Service (INIS). Appeals must address the specific refusal reasons with additional evidence. Reapplication is possible at any time but not recommended without addressing the refusal grounds. Ireland's refusal rate is moderate. Legal representation through an Irish immigration solicitor is advisable. Work permit appeals go through the Employment Permits Appeals process. The appeal process typically takes 4-12 weeks.",
    },
    "visa-israel": {
        "name": "Israel",
        "visa_types": [
            ("Tourist Visa (B/2)", "Up to 3 months", "Free for most nationalities", "Passport, return ticket, financial proof, accommodation"),
            ("Business Visa (B/2)", "Up to 3 months", "Free", "Business invitation, company letter"),
            ("Work Visa (B/1)", "Up to 2 years, renewable", "ILS 175 (USD 48)", "Employer petition to PIBA, work permit approval"),
            ("Student Visa (A/2)", "Duration of studies", "ILS 175", "Institution acceptance, financial proof, insurance"),
            ("Volunteer Visa (A/5)", "Up to 5 years", "ILS 175", "Organization sponsorship, kibbutz/volunteer program"),
            ("Clergy Visa (A/3)", "1 year, renewable", "ILS 175", "Religious institution sponsorship"),
            ("Temporary Residence (A/5)", "1-3 years", "ILS 175", "Various qualifying paths"),
            ("Birthright/Aliyah Visa", "Permanent", "Free", "Jewish ancestry (Law of Return), Jewish Agency process"),
            ("Investor Visa", "1-3 years", "ILS 175", "Significant investment in Israel, business plan"),
            ("Digital Nomad Visa", "1 year", "ILS 175", "Remote work proof, income threshold, insurance"),
        ],
        "processing": [
            ("Tourist Visa", "On arrival or 5-10 days", "Free", "N/A", "N/A"),
            ("Work Visa (B/1)", "4-12 weeks", "ILS 175", "2-4 weeks", "Additional fee"),
            ("Student Visa", "3-8 weeks", "ILS 175", "1-2 weeks", "Additional fee"),
            ("Aliyah Visa", "3-6 months", "Free", "Varies", "N/A"),
            ("Digital Nomad Visa", "2-4 weeks", "ILS 175", "1 week", "Additional fee"),
        ],
        "health": "Israel does not require mandatory vaccinations for entry. Recommended vaccinations include routine immunizations, hepatitis A, and hepatitis B. No medical examination is required for tourist visas. Work and residence visa applicants may need health screening, including HIV testing for certain permit categories. Health insurance is mandatory for all Israeli residents through one of four health funds (Kupot Holim): Clalit, Maccabi, Meuhedet, or Leumit. Work visa holders are typically covered through employer insurance until eligible for health fund enrollment. Tourists should have comprehensive travel insurance as medical care in Israel is excellent but expensive. Police clearance certificates from the applicant's home country are required for work visas and residence permits. Israel uses biometric data collection at Ben Gurion Airport and other border crossings, including fingerprints and facial recognition. Israel does not stamp passports — instead, a small entry card (blue B/2 slip) is issued at border control.",
        "extension": "Tourist visa (B/2) extensions can be obtained at the Population and Immigration Authority (PIBA) offices for additional periods, generally up to a total of 6 months. The extension fee is approximately ILS 175. Apply before the current visa expires. Work visa (B/1) renewals are handled through the employer and PIBA. Students must maintain valid status through their institution. Overstay penalties include deportation, entry bans of up to 10 years, and detention. Israel is very strict about immigration compliance. PIBA conducts enforcement operations targeting unauthorized workers and overstayers. Working on a tourist visa is strictly illegal and carries severe consequences. Entry may be denied to travelers with evidence of previous overstays. Israel's border security is among the most thorough in the world.",
        "refusal": "Israeli visa and entry refusals may result from: security concerns (Israel's security screening is extensive), evidence of connections to countries hostile to Israel, previous overstays or immigration violations, BDS activism, incomplete documentation, or inconsistencies during the border interview. Israel conducts thorough security interviews at Ben Gurion Airport. Refusals at the airport can result in detention and return. Consular visa refusals can be reconsidered by submitting additional documentation to the embassy. PIBA handles appeals for work and residence visa refusals. There is no formal appeals tribunal for tourist entry refusals at the border, though legal representation can assist. Israel maintains broad discretion over border admissions. Travelers with Arab country stamps, particularly Syrian, Lebanese, or Iranian, may face additional questioning but are not automatically refused.",
    },
    "visa-italy": {
        "name": "Italy",
        "visa_types": [
            ("Schengen Short-Stay Visa (C-type)", "Up to 90 days", "EUR 80", "Passport, insurance EUR 30k, hotel booking, financial proof"),
            ("National Long-Stay Visa (D-type)", "Over 90 days", "EUR 116", "Purpose documentation, financial proof"),
            ("Work Visa (Nulla Osta al Lavoro)", "Up to 2 years", "EUR 116", "Job offer within annual quota (Decreto Flussi), employer filing"),
            ("EU Blue Card", "Up to 2 years", "EUR 116", "High-qualification job, salary 1.5x average, degree"),
            ("Student Visa (Visto per Studio)", "1 year, renewable", "EUR 50", "University acceptance, EUR 6,000/year proof, insurance"),
            ("Family Reunification (Ricongiungimento Familiare)", "Matches sponsor", "EUR 116", "Nulla osta from Sportello Unico, relationship proof, income"),
            ("Elective Residence Visa (Residenza Elettiva)", "1 year, renewable", "EUR 116", "No work, passive income EUR 31,000+, accommodation"),
            ("Self-Employment Visa (Lavoro Autonomo)", "Up to 2 years", "EUR 116", "Business plan, capital, Nulla osta, professional qualifications"),
            ("Digital Nomad Visa", "1 year, renewable", "EUR 116", "Remote work contract, income EUR 28,000+/year, insurance"),
            ("Investor Visa (Visto per Investitori)", "2 years, renewable", "EUR 116", "Investment EUR 250,000-2,000,000 depending on category"),
        ],
        "processing": [
            ("Schengen C-type", "10-15 calendar days", "EUR 80", "3-5 days", "EUR 160"),
            ("National D-type", "4-12 weeks", "EUR 116", "N/A", "N/A"),
            ("Work Visa (with Nulla Osta)", "4-6 months total", "EUR 116", "N/A (quota system)", "N/A"),
            ("Student Visa", "4-8 weeks", "EUR 50", "2-3 weeks (pre-enrollment)", "EUR 50"),
            ("Investor Visa", "2-4 weeks", "EUR 116", "2 weeks (fast-track)", "EUR 116"),
        ],
        "health": "Italy requires travel medical insurance with minimum EUR 30,000 coverage for Schengen short-stay visa applicants. No mandatory vaccinations are required for entry, though certain vaccinations may be required for children attending Italian schools. Long-stay visa and residence permit holders must register with the Italian National Health Service (Servizio Sanitario Nazionale or SSN), which provides comprehensive healthcare coverage. Registration is done at the local ASL (Azienda Sanitaria Locale). Students and self-employed workers can register voluntarily by paying an annual fee (approximately EUR 400-700). EU/EEA citizens can use the EHIC. Police clearance certificates (Certificato Penale or equivalent from home country, apostilled and translated into Italian by a sworn translator) are required for all national visa applications. Biometric data (10 fingerprints and photograph) is collected for Schengen visa applications at Italian embassies or VFS Global centers. Italy has an excellent public healthcare system with universal coverage for residents.",
        "extension": "Schengen short-stay visas allow 90 days within 180 days and cannot be extended except in extraordinary circumstances. National visa holders must apply for a Permesso di Soggiorno (residence permit) at the local Questura (police headquarters) within 8 working days of arrival using the kit available at Italian post offices (Poste Italiane). Residence permits must be renewed before expiry. Maximum tourist stay is 90 days per 180-day period. Overstay results in an espulsione (expulsion order), fines, and Schengen-wide entry bans of 1-5 years in SIS II. Italy is relatively strict about enforcement but has had amnesty programs (sanatoria) for irregular workers. Working without authorization is an offense. The Questura handles residence permit matters, and appointments can have long wait times, especially in Rome, Milan, and Naples.",
        "refusal": "Italian visa refusals may result from: insufficient financial proof (EUR 50+/day for tourism), inadequate insurance, incomplete documentation, doubts about return intention, previous Schengen violations, or security concerns. Work visa refusals often relate to the annual quota system (Decreto Flussi) being exhausted or Nulla Osta denial. Refusals follow the standardized Schengen form. Appeals can be filed within 60 days to the TAR (Tribunale Amministrativo Regionale) or within 120 days through an extraordinary appeal to the President of the Republic. Legal representation by an Italian immigration attorney (avvocato per l'immigrazione) is recommended. Reapplication is possible with improved documentation. Italy's work visa quota system makes timing critical — applications submitted during the Decreto Flussi window are processed in order. The investor visa program has a dedicated fast-track evaluation process.",
    },
}


def generate_sections(slug: str) -> str:
    """Generate all 5 enrichment sections for a given country page slug."""
    d = COUNTRY_DATA[slug]
    name = d["name"]

    # ── Section 1: Complete Visa Categories ──
    visa_rows = ""
    for vtype, dur, fee, reqs in d["visa_types"]:
        visa_rows += f"<tr><td><strong>{vtype}</strong></td><td>{dur}</td><td>{fee}</td><td>{reqs}</td></tr>\n"

    s1 = f"""
<h2 id="all-visas">&#128203; Complete Visa Categories for {name}</h2>
<p>{name} offers a variety of visa and permit categories depending on your purpose of travel, intended length of stay, and nationality. Below is a comprehensive overview of the main visa types available, including requirements, validity, and approximate fees. Always verify current requirements with the official immigration authority before applying, as rules and fees can change.</p>
<div class="table-responsive">
<table class="table table-bordered table-sm">
<thead><tr class="table-dark"><th>Visa Type</th><th>Duration</th><th>Fee (approx.)</th><th>Key Requirements</th></tr></thead>
<tbody>
{visa_rows}</tbody>
</table>
</div>
<p>Note: Fees and requirements may vary by nationality and are subject to change. Some visa categories may have additional sub-types or specific conditions not listed above. Check the official {name} immigration portal or your nearest embassy for the most current information.</p>
"""

    # ── Section 2: Processing Times & Fees ──
    proc_rows = ""
    for vtype, std_time, std_fee, exp_time, exp_fee in d["processing"]:
        proc_rows += f"<tr><td><strong>{vtype}</strong></td><td>{std_time}</td><td>{std_fee}</td><td>{exp_time}</td><td>{exp_fee}</td></tr>\n"

    s2 = f"""
<h2 id="processing">&#9200; Processing Times &amp; Fees for {name} Visas</h2>
<p>Processing times for {name} visa applications vary by visa type, applicant nationality, and time of year. Standard processing is the default timeline, while expedited (express or priority) processing is available for certain visa types at an additional cost. During peak travel seasons, processing may take longer than usual. Always apply well in advance of your planned travel date to account for potential delays.</p>
<div class="table-responsive">
<table class="table table-bordered table-sm">
<thead><tr class="table-dark"><th>Visa Type</th><th>Standard Processing</th><th>Standard Fee</th><th>Expedited Processing</th><th>Expedited Fee</th></tr></thead>
<tbody>
{proc_rows}</tbody>
</table>
</div>
<p>All fees are approximate and may be adjusted. Some embassies and consulates charge additional service fees through visa application centers (e.g., VFS Global, TLS Contact). Payment methods vary by location. Keep your payment receipt as proof of fee payment.</p>
"""

    # ── Section 3: Health & Entry Requirements ──
    s3 = f"""
<h2 id="health-requirements">&#127973; Health &amp; Entry Requirements for {name}</h2>
<p>{d['health']}</p>
"""

    # ── Section 4: Visa Extension & Overstay ──
    s4 = f"""
<h2 id="extension">&#128337; Visa Extension &amp; Overstay Rules in {name}</h2>
<p>{d['extension']}</p>
"""

    # ── Section 5: Refusal & Appeals ──
    s5 = f"""
<h2 id="refusal">&#10060; Visa Refusal &amp; Appeals for {name}</h2>
<p>{d['refusal']}</p>
"""

    return s1 + s2 + s3 + s4 + s5


def find_insertion_point(html: str) -> int:
    """Find the best insertion point before E-E-A-T section, eeat-section div, or footer."""
    # Try E-E-A-T comment
    idx = html.find("<!-- E-E-A-T -->")
    if idx != -1:
        return idx

    # Try eeat-section div class
    idx = html.find('class="eeat-section')
    if idx != -1:
        # Go back to the start of the div tag
        div_start = html.rfind("<div", 0, idx)
        if div_start != -1:
            return div_start

    # Try related-guides section
    idx = html.find('class="related-guides')
    if idx != -1:
        div_start = html.rfind("<div", 0, idx)
        if div_start != -1:
            return div_start

    # Try before </article>
    idx = html.find("</article>")
    if idx != -1:
        return idx

    # Try before <footer
    idx = html.find("<footer")
    if idx != -1:
        return idx

    # Try before last </section>
    idx = html.rfind("</section>")
    if idx != -1:
        return idx

    return -1


def process_file(slug: str) -> str:
    filepath = os.path.join(BASE, slug + ".html")
    if not os.path.isfile(filepath):
        return f"SKIP (not found): {filepath}"

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Idempotency check
    if 'id="all-visas"' in html:
        return f"SKIP (already enriched): {slug}"

    sections_html = generate_sections(slug)

    ins_point = find_insertion_point(html)
    if ins_point == -1:
        return f"SKIP (no insertion point found): {slug}"

    new_html = html[:ins_point] + sections_html + html[ins_point:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_html)

    return f"OK: {slug} — inserted 5 sections ({len(sections_html):,} chars)"


def main():
    print("=" * 70)
    print("Visa Page Enrichment — Batch A (A through I)")
    print(f"Base directory: {BASE}")
    print(f"Target files: {len(TARGET_FILES)}")
    print("=" * 70)

    ok = 0
    skip = 0
    fail = 0
    for slug in TARGET_FILES:
        result = process_file(slug)
        print(result)
        if result.startswith("OK"):
            ok += 1
        elif result.startswith("SKIP"):
            skip += 1
        else:
            fail += 1

    print("=" * 70)
    print(f"Done. OK: {ok} | Skipped: {skip} | Failed: {fail}")
    print("=" * 70)


if __name__ == "__main__":
    main()
