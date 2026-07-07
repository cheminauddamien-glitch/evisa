/**
 * visa-search.js
 * Interactive visa search form for evisa-card.com homepage
 * Handles: nationality × destination × purpose → result panel
 * NO Google AdSense in result panel
 */
(function () {
  "use strict";

  // ── 49 Destination countries ──
  var DESTINATIONS = [
    { s: "argentina", n: "Argentina", f: "ar" },
    { s: "australia", n: "Australia", f: "au" },
    { s: "austria", n: "Austria", f: "at" },
    { s: "belgium", n: "Belgium", f: "be" },
    { s: "brazil", n: "Brazil", f: "br" },
    { s: "cambodia", n: "Cambodia", f: "kh" },
    { s: "canada", n: "Canada", f: "ca" },
    { s: "china", n: "China", f: "cn" },
    { s: "colombia", n: "Colombia", f: "co" },
    { s: "costa-rica", n: "Costa Rica", f: "cr" },
    { s: "croatia", n: "Croatia", f: "hr" },
    { s: "czech-republic", n: "Czech Republic", f: "cz" },
    { s: "denmark", n: "Denmark", f: "dk" },
    { s: "france", n: "France", f: "fr" },
    { s: "germany", n: "Germany", f: "de" },
    { s: "greece", n: "Greece", f: "gr" },
    { s: "hong-kong", n: "Hong Kong", f: "hk" },
    { s: "hungary", n: "Hungary", f: "hu" },
    { s: "india", n: "India", f: "in" },
    { s: "indonesia", n: "Indonesia", f: "id" },
    { s: "ireland", n: "Ireland", f: "ie" },
    { s: "italy", n: "Italy", f: "it" },
    { s: "japan", n: "Japan", f: "jp" },
    { s: "jordan", n: "Jordan", f: "jo" },
    { s: "malaysia", n: "Malaysia", f: "my" },
    { s: "maldives", n: "Maldives", f: "mv" },
    { s: "mexico", n: "Mexico", f: "mx" },
    { s: "nepal", n: "Nepal", f: "np" },
    { s: "netherlands", n: "Netherlands", f: "nl" },
    { s: "new-zealand", n: "New Zealand", f: "nz" },
    { s: "norway", n: "Norway", f: "no" },
    { s: "philippines", n: "Philippines", f: "ph" },
    { s: "poland", n: "Poland", f: "pl" },
    { s: "portugal", n: "Portugal", f: "pt" },
    { s: "qatar", n: "Qatar", f: "qa" },
    { s: "romania", n: "Romania", f: "ro" },
    { s: "singapore", n: "Singapore", f: "sg" },
    { s: "spain", n: "Spain", f: "es" },
    { s: "sri-lanka", n: "Sri Lanka", f: "lk" },
    { s: "sweden", n: "Sweden", f: "se" },
    { s: "switzerland", n: "Switzerland", f: "ch" },
    { s: "taiwan", n: "Taiwan", f: "tw" },
    { s: "thailand", n: "Thailand", f: "th" },
    { s: "turkey", n: "Turkey", f: "tr" },
    { s: "uae", n: "UAE", f: "ae" },
    { s: "united-kingdom", n: "United Kingdom", f: "gb" },
    { s: "usa", n: "United States", f: "us" },
    { s: "vietnam", n: "Vietnam", f: "vn" },
    { s: "panama", n: "Panama", f: "pa" }
  ];

  // ── 23 Nationalities ──
  var NATIONALITIES = [
    { s: "argentinian", n: "Argentinian", f: "ar" },
    { s: "australian", n: "Australian", f: "au" },
    { s: "bangladeshi", n: "Bangladeshi", f: "bd" },
    { s: "brazilian", n: "Brazilian", f: "br" },
    { s: "canadian", n: "Canadian", f: "ca" },
    { s: "chinese", n: "Chinese", f: "cn" },
    { s: "french", n: "French", f: "fr" },
    { s: "german", n: "German", f: "de" },
    { s: "indian", n: "Indian", f: "in" },
    { s: "indonesian", n: "Indonesian", f: "id" },
    { s: "japanese", n: "Japanese", f: "jp" },
    { s: "korean", n: "Korean", f: "kr" },
    { s: "mexican", n: "Mexican", f: "mx" },
    { s: "new-zealand", n: "New Zealander", f: "nz" },
    { s: "nigerian", n: "Nigerian", f: "ng" },
    { s: "pakistani", n: "Pakistani", f: "pk" },
    { s: "philippine", n: "Filipino", f: "ph" },
    { s: "russian", n: "Russian", f: "ru" },
    { s: "singaporean", n: "Singaporean", f: "sg" },
    { s: "south-african", n: "South African", f: "za" },
    { s: "turkish", n: "Turkish", f: "tr" },
    { s: "uk", n: "British", f: "gb" },
    { s: "us", n: "American", f: "us" }
  ];

  // ── 5 Purposes ──
  var PURPOSES = [
    { s: "tourism", n: "Tourism / Vacation" },
    { s: "student", n: "Student / Study" },
    { s: "work", n: "Work / Employment" },
    { s: "retirement", n: "Retirement" },
    { s: "digital_nomad", n: "Digital Nomad" }
  ];

  // ── Visa data per destination × purpose ──
  // Each entry: [visa_type, duration, overstay_penalty, entry_exit_strategy, requirements]
  var D = {
    "thailand": {
      tourism:       ["Tourist Visa / Visa Exempt", "30-60 days", "500 THB/day fine; >90 days overstay = 1-10 year ban + possible detention", "Extend 30 days at Immigration (1,900 THB). Border run to reset. Max 2 visa-exempt entries by land per year.", "Passport valid 6+ months, proof of onward travel, 20,000 THB equivalent funds"],
      student:       ["Non-Immigrant ED Visa", "1 year (renewable)", "Same fines + visa revocation", "Renew annually at Immigration with enrollment proof. 90-day reporting required.", "Acceptance letter from Thai school/university, financial proof, medical certificate"],
      work:          ["Non-Immigrant B Visa + Work Permit", "1 year (renewable)", "Working without permit = fine + deportation", "Annual renewal with employer sponsorship. 90-day reporting. Re-entry permit if traveling.", "Job offer from Thai company, work permit application, medical certificate, degree certificate"],
      retirement:    ["Non-Immigrant O-A (Retirement)", "1 year (renewable indefinitely)", "Same fines + may lose retirement visa status", "Annual renewal at Immigration. 90-day reporting. Must maintain 800k THB in bank at all times.", "Age 50+, 800,000 THB in Thai bank OR 65,000 THB/month income, health insurance (40k outpatient / 400k inpatient)"],
      digital_nomad: ["LTR Visa (Long-Term Resident)", "10 years", "Standard overstay fines apply", "No 90-day reporting required. Multiple entries. 17% flat tax on Thai income.", "Income $80,000+/year from foreign employer, or $250,000+ in assets for retiree track. $10,000 application fee."]
    },
    "portugal": {
      tourism:       ["Schengen Visa / Visa-Free", "90 days in 180-day period", "Fine up to 400 EUR, deportation, Schengen-wide ban possible", "Leave Schengen zone for 90 days, then return. No extension possible for tourist stays.", "Valid passport, travel insurance, proof of accommodation & funds"],
      student:       ["D4 Student Visa → Residence Permit", "1 year (renewable up to 5 years)", "Illegal stay = deportation + re-entry ban", "Renew residence permit annually at AIMA. Can work part-time (20h/week).", "University acceptance, proof of funds (~705 EUR/month), health insurance, clean criminal record"],
      work:          ["D1 Work Visa → Residence Permit", "1-2 years (renewable)", "Working without permit = fines + deportation", "Renew at AIMA. After 5 years → permanent residency. After 5 years → citizenship.", "Job contract with Portuguese employer, employer must prove no EU candidate available"],
      retirement:    ["D7 Passive Income Visa", "2 years (renewable, then 3 years)", "Overstay = loss of NHR tax benefits + deportation risk", "Renew at AIMA. Must spend 183+ days/year in Portugal. Path to citizenship in 5 years.", "Passive income min. 760 EUR/month (pension, dividends, rental), NIF (tax number), Portuguese bank account, health insurance"],
      digital_nomad: ["D8 Digital Nomad Visa", "1 year (renewable once)", "Same as tourist overstay penalties", "Renewable once for 1 additional year. Must apply for D7 or other visa after.", "Income min. 3,040 EUR/month from foreign employer/clients, proof of remote work, health insurance"]
    },
    "spain": {
      tourism:       ["Schengen Visa / Visa-Free", "90 days in 180-day period", "Fine 501-10,000 EUR + deportation + 5-year Schengen ban", "Leave Schengen zone for 90 days. No extension. Canary Islands count as Schengen.", "Valid passport, return ticket, 100 EUR/day minimum funds, travel insurance"],
      student:       ["Student Visa (Visado de Estudios)", "1 year (renewable)", "Deportation + study visa revocation", "Renew annually at Oficina de Extranjeria. Can work 20h/week. Convert to work visa after.", "University acceptance, proof of funds (~600 EUR/month), health insurance, background check"],
      work:          ["Work Visa + Residence Permit", "1 year (renewable)", "Working illegally = 501-10,000 EUR fine + deportation", "Renew annually. After 5 years → permanent. 10 years → citizenship. Beckham Law: 24% flat tax for 6 years.", "Job offer, employer sponsorship, labor market test (no EU candidate available)"],
      retirement:    ["Non-Lucrative Visa (Visado No Lucrativo)", "1 year (renewable up to 5 years)", "Loss of visa + deportation", "Renew annually. Cannot work in Spain. Must prove income each renewal.", "Income min. 2,400 EUR/month (individual) or 3,000 EUR/month (couple), health insurance, no criminal record"],
      digital_nomad: ["Digital Nomad Visa (Ley de Startups)", "1 year (renewable to 3 years)", "Standard overstay penalties", "Renewable for 2 additional years. Beckham Law eligible: 24% flat tax instead of 47%.", "Income min. 2,334 EUR/month, remote work for non-Spanish company, degree or 3+ years experience"]
    },
    "france": {
      tourism:       ["Schengen Visa / Visa-Free", "90 days in 180-day period", "Fine + deportation + Schengen ban", "Leave Schengen zone for 90 days then return. No tourist visa extension in France.", "Valid passport, travel insurance 30k EUR coverage, proof of accommodation & funds"],
      student:       ["Long-Stay Student Visa (VLS-TS)", "1 year (renewable)", "Deportation + study interruption", "Renew at Prefecture. Work 20h/week allowed. Talent Passport for researchers.", "Campus France procedure, university acceptance, proof of 615 EUR/month, health insurance"],
      work:          ["Long-Stay Work Visa (Salarié)", "1 year (renewable)", "Heavy fines for employer + deportation for employee", "Renew at Prefecture. After 5 years → carte de résident (10 years). EU Blue Card available.", "Work contract, employer authorization from DREETS, salary min. 1.5x SMIC for Blue Card"],
      retirement:    ["Visitor Visa (VLS-TS Visiteur)", "1 year (renewable)", "Loss of visa + deportation", "Renew annually at Prefecture. Cannot work. Must maintain private health insurance.", "Proof of sufficient income (no fixed minimum, ~1,500+ EUR/month), health insurance, accommodation proof"],
      digital_nomad: ["Talent Passport (Passeport Talent)", "Up to 4 years", "Standard overstay penalties", "Renewable. Allows freelance activity. Family reunification included.", "Innovative project or skills, business plan or freelance contract, min. income ~2,000 EUR/month"]
    },
    "japan": {
      tourism:       ["Visa-Free / Tourist Visa", "90 days (most Western nations)", "1 day overstay = detention + deportation + 5-year re-entry ban", "No extension possible for visa-free stays. Must leave and re-enter. Maximum 180 days/year cumulative.", "Valid passport, return ticket, sufficient funds. No working allowed."],
      student:       ["Student Visa (留学)", "1-2 years (renewable)", "Deportation + study ban", "Renew at Immigration Bureau. Work permit for 28h/week (別活動許可). After graduation, 1-year job search visa.", "Certificate of Eligibility (COE) from school, financial proof (~200,000 JPY/month), health insurance"],
      work:          ["Work Visa (Engineer/Humanities/etc.)", "1-5 years (renewable)", "Detention + deportation + re-entry ban", "Renew at Immigration. After 10 years → permanent residency. Highly Skilled Professional visa: PR in 1-3 years.", "COE from employer, degree matching job category, employer sponsorship"],
      retirement:    ["No Retirement Visa", "N/A", "N/A", "Japan has no retirement visa. Options: Investor visa (¥5M investment), Spouse visa, or Designated Activities visa.", "No direct retirement pathway. Must qualify under another visa category."],
      digital_nomad: ["Digital Nomad Visa (2024)", "6 months (non-renewable)", "Standard overstay penalties", "Single entry, non-renewable. Must leave after 6 months. Can re-apply after leaving.", "Income min. ¥10M/year (~$70,000), private health insurance, work for non-Japanese company"]
    },
    "usa": {
      tourism:       ["B1/B2 Tourist Visa / ESTA", "Up to 6 months (B2) / 90 days (ESTA)", "Automatic 3-year or 10-year re-entry ban depending on overstay length", "ESTA: max 90 days, no extension. B2: can request extension (Form I-539) before expiry. No border runs.", "ESTA: $21 fee, valid 2 years. B2: embassy interview, proof of ties to home country, $185 fee"],
      student:       ["F-1 Student Visa", "Duration of Status (D/S)", "Loss of status = deportation + SEVIS record", "Valid as long as enrolled. OPT: 12 months work after graduation (36 months for STEM). CPT during studies.", "I-20 from SEVP-certified school, proof of funds for 1 year, SEVIS fee $350, visa interview"],
      work:          ["H-1B Work Visa", "3 years (renewable to 6 years)", "Working without authorization = deportation + ban", "H-1B lottery (April). L-1 for intracompany transfers. O-1 for extraordinary ability. Green card pathway.", "Employer sponsorship, specialty occupation, bachelor's degree minimum, $460-$780 filing fee"],
      retirement:    ["No Retirement Visa", "N/A", "N/A", "USA has no retirement visa. Options: EB-5 investor ($800,000+), Green Card lottery, or family sponsorship.", "No direct retirement pathway. E-2 treaty investor visa if from qualifying country."],
      digital_nomad: ["No Digital Nomad Visa", "N/A", "N/A", "USA has no DN visa. Options: B1/B2 (no US-source work), ESTA 90 days, or O-1/EB-1 if exceptional ability.", "Remote workers must use tourist visa. Cannot earn US-source income without work authorization."]
    },
    "mexico": {
      tourism:       ["Tourist Visa / FMM Card", "180 days", "Fine 2,000-5,000 MXN + deportation risk", "FMM auto-issued at entry for visa-exempt nationalities. Can extend once at INM. No border run needed within 180 days.", "Valid passport, FMM form (free at entry or $575 MXN if by air), proof of funds (~$1,620/month)"],
      student:       ["Temporary Resident (Student)", "1 year (renewable to 4 years)", "Loss of visa + deportation", "Renew annually at INM. Can apply for work permit with student visa.", "University acceptance, proof of funds, health insurance, background check"],
      work:          ["Temporary Resident (Work)", "1-4 years", "Working without permit = fines + deportation", "Employer applies at INM. Renewable. After 4 years → permanent residency.", "Job offer from Mexican company, employer sponsorship at INM, salary min. ~$3,000/month"],
      retirement:    ["Temporary Resident → Permanent", "4 years temp then permanent", "Loss of status", "Temporary: prove $3,000/month income or $100,000 savings. After 4 years → permanent residency (no income proof).", "Proof of pension/income $3,000+/month or savings $100,000+, background check"],
      digital_nomad: ["Tourist FMM (de facto)", "180 days", "Standard overstay fines", "180-day FMM allows remote work for foreign companies. Leave and re-enter for new 180 days. No formal DN visa.", "Valid passport, no specific income requirement, proof of return/onward travel"]
    },
    "uae": {
      tourism:       ["Tourist Visa / Visa-Free", "30-90 days (varies by nationality)", "100 AED/day overstay fine + possible detention + deportation", "Exit to Oman/Bahrain and re-enter for visa reset. Or apply for tourist visa extension online.", "Valid passport 6+ months, return ticket, hotel booking, sufficient funds"],
      student:       ["Student Residence Visa", "1 year (renewable)", "100 AED/day + visa cancellation", "Renew annually. Sponsored by university. Can work part-time (certain universities).", "University acceptance, sponsor (university), health insurance, Emirates ID"],
      work:          ["Employment Visa + Residence", "2-3 years (renewable)", "Heavy fines + deportation + potential labor ban", "Employer sponsors visa. Golden Visa for high earners (10 years). Freelance permit available.", "Job offer, employer sponsorship, medical fitness test, Emirates ID, security clearance"],
      retirement:    ["Retirement Visa (5 years)", "5 years (renewable)", "Standard overstay fines", "Renewable. No income tax. Must maintain qualifying investment/savings/income.", "Age 55+, property worth AED 2M+ OR savings AED 1M+ OR monthly income AED 20,000+"],
      digital_nomad: ["Virtual Working Visa (Dubai)", "1 year (renewable)", "Standard overstay fines", "Renewable annually. No UAE income tax. Must have own health insurance.", "Income min. $3,500/month, employment contract or business ownership proof, health insurance"]
    },
    "india": {
      tourism:       ["e-Visa / Tourist Visa", "30-180 days (e-Visa) / 5 years (regular)", "Overstay fine $300 + per-day penalty + possible blacklisting", "e-Tourist: 30-day (double entry) or 1-year/5-year (multiple entry). Regular tourist visa from embassy for longer stays.", "Passport 6+ months valid, recent photo, return ticket, $10-$100 fee depending on nationality"],
      student:       ["Student Visa", "Duration of course (up to 5 years)", "Deportation + academic suspension", "Renew at FRRO. Must register within 14 days of arrival. Part-time work generally not allowed.", "University admission letter, proof of funds, sponsor letter, background check"],
      work:          ["Employment Visa", "1-5 years", "Fine + deportation + possible criminal charges", "Renew at FRRO. Income tax applies (30%+ for foreigners). Must register within 14 days.", "Employment contract, salary min. $25,000/year, employer sponsorship, PAN card for tax"],
      retirement:    ["No Retirement Visa", "N/A", "N/A", "India has no retirement visa. Long-term options: Business visa (10 years for some nationalities), or OCI card for persons of Indian origin.", "PIO/OCI card grants lifelong multiple entry. Otherwise, extended tourist visa."],
      digital_nomad: ["e-Business Visa / Tourist", "1 year (e-Business)", "Standard overstay penalties", "No formal DN visa. e-Business visa allows attending meetings. Tourist visa allows remote work for foreign employer.", "e-Business: invitation from Indian company. Tourist: proof of funds & accommodation."]
    },
    "indonesia": {
      tourism:       ["Visa on Arrival / eVOA / B211A", "30 days (VoA) / 60 days (B211A)", "1,000,000 IDR/day overstay fine + detention + deportation + 1-year ban", "VoA extendable once (30 days) at Immigration. B211A extendable up to 180 days. Exit to Singapore/Malaysia and re-enter.", "Passport 6+ months, return ticket, 500,000 IDR VoA fee. B211A: sponsor or agent required."],
      student:       ["KITAS Student Visa", "1 year (renewable)", "Deportation + study ban", "Renew annually. Sponsored by Indonesian educational institution. KITAS card issued.", "University acceptance, sponsor (school), health check, police clearance"],
      work:          ["KITAS Work Visa", "1 year (renewable to 5 years)", "1M IDR/day + deportation + employer fines", "Employer applies via TKA system. IMTA work permit required. After 4-5 years → KITAP (permanent).", "Employer sponsorship, IMTA permit, degree certificate, experience proof"],
      retirement:    ["Retirement KITAS (D317)", "1 year (renewable to 5 years)", "Standard overstay fines", "Renewable annually. Must use designated retirement areas (Bali, Yogyakarta, etc.). Cannot work.", "Age 55+, pension/income $1,500+/month, health insurance, accommodation proof in designated area"],
      digital_nomad: ["B211A Digital Nomad (de facto)", "60 days (extendable to 180)", "1M IDR/day fine", "B211A visa via agent (~$200-300). Extend monthly. Bali is the main DN hub. No formal DN visa yet.", "Agent/sponsor in Indonesia, proof of funds, return ticket. Second Home Visa for 5-10 years ($130k min savings)."]
    },
    "australia": {
      tourism:       ["ETA / eVisitor / Tourist Visa (600)", "90 days (ETA/eVisitor) / 3-12 months (600)", "Mandatory detention + deportation + 3-year exclusion period", "ETA/eVisitor: no extension. Visa 600: can apply to extend. No border runs work for Australia.", "ETA $20 AUD, Visitor 600 $190-$1,120 AUD. Health insurance recommended. Proof of funds."],
      student:       ["Student Visa (500)", "Duration of course + 2-3 months", "Visa cancellation + detention + 3-year ban", "Can work 48h/fortnight during semester. Unlimited during breaks. Post-study visa 485 for 2-4 years.", "CoE from CRICOS provider, OSHC health insurance, financial proof ($24,505 AUD/year), English proficiency"],
      work:          ["Temporary Skill Shortage (482)", "1-4 years", "Detention + deportation + 3-year ban + employer sanctions", "482 → PR pathway via 186 after 2-3 years. 491 for regional. Points-based 189/190.", "Employer sponsorship, skills assessment, English proficiency (IELTS 5-6), occupation on skills list"],
      retirement:    ["Investor Retirement (405) — CLOSED", "N/A", "N/A", "Australia's retirement visa (405) is closed to new applications. Parent visa (143/173) if you have Australian children.", "No current retirement visa pathway. Investor visa 188 requires $1.5M+ AUD business investment."],
      digital_nomad: ["No DN Visa", "N/A", "N/A", "No digital nomad visa. Use tourist visa (90 days ETA). Working Holiday Visa (462/417) for ages 18-35.", "Working Holiday: 1 year, work for same employer max 6 months. Ages 18-35 from eligible countries."]
    },
    "canada": {
      tourism:       ["eTA / Visitor Visa (TRV)", "6 months", "Voluntary departure notice → removal order → 1-year re-entry ban", "Can apply to extend status (Visitor Record) before expiry. No automatic reset by border run.", "eTA $7 CAD (visa-exempt). TRV $100 CAD + biometrics $85. Proof of funds, ties to home country."],
      student:       ["Study Permit", "Duration of program + 90 days", "Removal order + re-entry ban", "Can work 20h/week during studies. PGWP after graduation (1-3 years). Pathway to PR via Express Entry.", "Letter of acceptance from DLI, proof of funds ($20,635 CAD/year), language test, police clearance"],
      work:          ["Work Permit (LMIA/LMIA-exempt)", "1-3 years", "Removal + IRCC ban", "LMIA from employer or LMIA-exempt (IEC, intracompany). After 1-2 years → Express Entry for PR.", "Job offer, LMIA approval or exemption, $155 CAD fee + biometrics. Open work permit for spouses."],
      retirement:    ["No Retirement Visa", "N/A", "N/A", "Canada has no retirement visa. Options: Super Visa for parents (10 years, 2 year stays), or investor immigration.", "Super Visa: Canadian child/grandchild sponsor, $100k CAD health insurance, financial proof."],
      digital_nomad: ["No DN Visa (Tourist entry)", "6 months", "Removal order", "No formal DN visa. Enter as visitor for 6 months. Cannot do Canadian-source work. International Experience Canada (IEC) for ages 18-35.", "Visitor status. Remote work for non-Canadian employer technically allowed under visitor entry."]
    },
    "malaysia": {
      tourism:       ["Visa-Free / eVISA", "90 days (most Western)", "Fine up to RM10,000 + jail up to 5 years + caning + deportation", "Leave and re-enter. No extension for visa-free. eVisa for restricted nationalities only.", "Passport 6+ months, return ticket, proof of funds"],
      student:       ["Student Pass", "Duration of course", "Fine + deportation + possible caning", "Renew via university. Can work 20h/week during semester breaks only. No part-time during studies.", "University acceptance (EMGS approval), financial proof, medical exam, insurance"],
      work:          ["Employment Pass (EP)", "2 years (renewable)", "Heavy fines + jail + caning + deportation", "Employer sponsors via ESD. Categories I/II/III by salary. After 5 years → PR possible.", "Job offer, employer sponsorship via ESD, salary min. RM5,000-10,000/month depending on category"],
      retirement:    ["MM2H (Malaysia My Second Home)", "5-10 years (renewable)", "Standard overstay fines", "Renewed every 5-10 years. Fixed deposit required. Cannot work (investment income OK).", "Age 35+, income RM40,000+/month, fixed deposit RM1M (Sabah/Sarawak: RM500k), health insurance"],
      digital_nomad: ["DE Rantau (Digital Nomad Pass)", "1 year (renewable)", "Standard penalties", "Renewable. DE Rantau program for tech workers. Valid at participating co-working spaces.", "Income min. RM24,000/month ($5,000), work for foreign company, 3+ years experience in tech/digital"]
    },
    "vietnam": {
      tourism:       ["e-Visa / Visa on Arrival", "30-90 days (e-Visa)", "Fine $5-10/day overstay. >14 days = detention + deportation + ban", "e-Visa 90 days (single/multiple entry, $25). Extendable at Immigration. Exit and re-enter for new e-Visa.", "Passport 6+ months, return ticket, $25 e-Visa fee, passport photo"],
      student:       ["Student Visa (DH)", "1 year (renewable)", "Deportation + study ban", "Renew via university. TRC (Temporary Residence Card) for 1-2 years with sponsor.", "University acceptance, sponsor (school), financial proof, health exam"],
      work:          ["Work Permit + TRC", "2 years (renewable)", "Fine + deportation. Employer fined VND 30-75M", "Employer applies for work permit at DOLISA. TRC issued after. Annual tax return required (20% flat for residents).", "Job offer, employer sponsorship, degree certificate apostilled, 3+ years experience, health exam"],
      retirement:    ["No Retirement Visa", "N/A", "N/A", "Vietnam has no retirement visa. Long-term options: e-Visa cycling (90 days), TRC via local sponsor/school.", "No direct pathway. Many retirees cycle 90-day e-Visas or enroll in language school for TRC sponsorship."],
      digital_nomad: ["e-Visa (de facto)", "90 days (renewable)", "Standard overstay fines", "No formal DN visa. Use 90-day e-Visa ($25). Renew by exiting and re-applying. Ho Chi Minh City & Da Nang are main DN hubs.", "Passport, $25 fee. Remote work for foreign company tolerated. No formal requirements."]
    },
    "colombia": {
      tourism:       ["Visa-Free / Tourist Visa", "90 days (extendable to 180)", "Fine ~$250 USD + deportation risk", "90-day stamp extendable once (90 more days) at Migracion Colombia office for ~$45. Max 180 days per year.", "Passport 3+ months valid, proof of return, financial proof (~$35/day)"],
      student:       ["M Visa (Student)", "Duration of course", "Deportation + cedula revocation", "Renew via university. Cedula de Extranjeria issued. Can apply for R visa after 5 years.", "University acceptance, proof of funds, health insurance, background check"],
      work:          ["M Visa (Work)", "Up to 3 years", "Working without permit = fines + deportation", "Employer sponsorship. Cedula de Extranjeria. After 5 years continuous → R visa (permanent).", "Job contract, employer registered with Migracion, salary min. 3x minimum wage"],
      retirement:    ["M Visa (Pensioner)", "Up to 3 years (renewable)", "Standard penalties", "Renewable. After 5 years → R visa (permanent residency). Low cost of living.", "Pension min. 3x Colombian minimum wage (~$689/month), health insurance EPS"],
      digital_nomad: ["V Visa (Digital Nomad)", "2 years", "Standard penalties", "2-year visa. Remote work for non-Colombian employer. Can apply for M visa after.", "Income min. 3x Colombian minimum wage (~$684/month), proof of remote work, health insurance"]
    },
    "panama": {
      tourism:       ["Tourist Visa / Visa-Free", "90-180 days", "Fine $50/month overstay + deportation risk", "Many nationalities get 180 days stamp. Exit to Costa Rica/Colombia and re-enter for reset.", "Passport 3+ months, return ticket, proof of $500 funds. Tourist card $5 at entry."],
      student:       ["Student Visa", "Duration of course", "Deportation + study ban", "Renew annually. Must maintain enrollment. Can apply for work permit separately.", "University acceptance, financial proof, health certificate, background check"],
      work:          ["Work Permit + Residence", "1 year (renewable)", "Working without permit = fines + deportation", "Employer sponsors work permit at MITRADEL. Renewable. Leads to temporary residency.", "Job offer, employer sponsorship, labor market test (10 Panamanians per 1 foreigner ratio)"],
      retirement:    ["Pensionado Visa", "Permanent", "N/A (permanent visa)", "Permanent residency from day 1. No renewal needed. Discounts on utilities, flights, restaurants, healthcare.", "Pension min. $1,000/month from any country, health certificate, background check. Best retirement visa globally."],
      digital_nomad: ["Short Stay (Remote Work Visa)", "9 months (renewable once)", "Standard overstay fines", "Renewable once for 9 more months. Can transition to Friendly Nations Visa for permanent.", "Income min. $3,000/month, proof of remote employment, health insurance"]
    },
    "georgia": {
      tourism:       ["Visa-Free", "365 days", "Fine GEL 500-2,000 + potential deportation", "365 days visa-free for 90+ nationalities. Simply exit and re-enter for a new 365-day period.", "Valid passport only. No visa, no registration, no questions. One of the world's easiest entries."],
      student:       ["Study Residence Permit", "1 year (renewable)", "Standard overstay fines after 365 days", "Apply at Public Service Hall. Renew annually. Affordable tuition (~$2,000-8,000/year).", "University acceptance, proof of funds, passport, application at Public Service Hall (~$60 fee)"],
      work:          ["Work Residence Permit", "1 year (renewable)", "Standard fines", "Easy process. No labor market test. Small Business Status: 1% turnover tax.", "Job offer or business registration, passport, application at Public Service Hall (~$60)"],
      retirement:    ["Visa-Free (de facto)", "365 days (renewable by exit/re-entry)", "Standard fines if overstay", "No retirement visa needed — 365 days visa-free. Exit briefly and re-enter. TBC Bank opens same-day with passport.", "No formal requirements. Zero capital gains tax. 1% small business tax. Very low cost of living."],
      digital_nomad: ["Remotely from Georgia", "1 year", "Standard fines", "Remotely from Georgia program. 365-day stay. 0% tax on foreign income (Virtual Zone for IT companies).", "Income min. $2,000/month, proof of remote employment or freelance, health insurance"]
    },
    "greece": {
      tourism:       ["Schengen Visa / Visa-Free", "90 days in 180-day period", "Fine + deportation + Schengen-wide ban", "Leave Schengen zone for 90 days. No extension. Greek islands count as Schengen.", "Valid passport, travel insurance, proof of accommodation & funds, 120 EUR/day minimum"],
      student:       ["National D Visa (Student)", "1 year (renewable)", "Deportation + study ban", "Renew at Aliens Bureau. Can work 20h/week. Tuition often free at public universities (in Greek).", "University acceptance, proof of funds (~5,000 EUR/year), health insurance, background check"],
      work:          ["Work Visa + Residence Permit", "1 year (renewable)", "Heavy fines + deportation", "Renew at Aliens Bureau. After 5 years → long-term residence. After 7 years → citizenship.", "Job offer, employer authorization, no EU candidate available, visa D from embassy"],
      retirement:    ["Non-Dom / FIP Visa", "Renewable annually", "Standard penalties", "Non-Dom regime: 100,000 EUR flat tax on worldwide income for 15 years. Golden Visa: 250k-800k property investment.", "Income proof (~2,000 EUR/month minimum) or Golden Visa property investment. Health insurance."],
      digital_nomad: ["Digital Nomad Visa", "2 years (renewable once)", "Standard Schengen overstay penalties", "Renewable once for 2 more years. 50% tax reduction on income first 7 years (Non-Dom separate).", "Income min. 3,500 EUR/month, remote work for non-Greek employer, health insurance"]
    },
    "paraguay": {
      tourism:       ["Visa-Free / Tourist Visa", "90 days", "Fine + deportation risk", "Many nationalities get 90-day stamp. Exit to Argentina/Brazil and re-enter. Extension possible at Migraciones.", "Valid passport, proof of return, yellow fever vaccination from endemic areas"],
      student:       ["Student Visa", "Duration of course", "Standard fines + deportation", "Renew via university. Affordable education. Spanish language.", "University acceptance, proof of funds, health certificate"],
      work:          ["Temporary Residency (Work)", "1 year (renewable)", "Working without permit = fines", "Apply at Migraciones with work contract. Easy process. After 3 years → permanent.", "Job offer or self-employment proof, background check, health certificate"],
      retirement:    ["Permanent Residency", "Permanent from day 1", "N/A (permanent)", "Permanent residency with just $5,500 bank deposit. Territorial tax: 0% on foreign income. 10% flat on local income.", "Bank deposit ~$5,500 in Paraguayan bank, background check, health certificate. One of the easiest PR programs."],
      digital_nomad: ["Tourist / Permanent Resident", "90 days (tourist) or permanent", "Standard fines", "No formal DN visa. Get permanent residency easily ($5,500 deposit) for unlimited stay. 0% tax on foreign income.", "Passport + $5,500 bank deposit for PR. Or cycle 90-day tourist entries."]
    }
  };

  // ── Missing countries with specific data ──
  D["argentina"] = {
    tourism:       ["Visa-Free / eVisa", "90 days", "Fine + deportation", "90-day stays, extendable once for 90 days at Migraciones. Visa-free for 80+ countries.", "Valid passport, return ticket, proof of funds"],
    student:       ["Student Visa (Residencia Estudiantil)", "1 year (renewable)", "Deportation + study ban", "Renew at Migraciones. Can work 20h/week. After 2 years → temporary residency.", "University acceptance, proof of funds, health insurance, apostilled documents"],
    work:          ["Work Visa (Residencia Temporaria)", "1 year (renewable)", "Working illegally = fines + deportation", "Employer sponsors work visa. After 3 years → permanent residency.", "Job offer, employer sponsorship, apostilled documents, CUIT tax number"],
    retirement:    ["Pensioner Visa (Residencia Rentista)", "1 year (renewable)", "Loss of visa", "Prove pension/passive income. Low cost of living. Path to citizenship in 2 years.", "Pension of ~$500 USD/month or equivalent passive income, health insurance"],
    digital_nomad: ["Digital Nomad Visa (2024)", "6 months (renewable once)", "Standard overstay fines", "Renewable once for 6 more months (12 total). Must earn from foreign sources.", "Income min. $1,500 USD/month, proof of remote employment/freelance, health insurance"]
  };
  D["brazil"] = {
    tourism:       ["Visa-Free / Tourist Visa", "90 days in 180-day period", "Fine ~R$100/day + deportation + re-entry ban", "90 days, extendable once for 90 more at Policia Federal. Visa-free for many countries.", "Valid passport (6+ months), return ticket, proof of accommodation & funds"],
    student:       ["VITEM IV Student Visa", "1 year (renewable)", "Deportation + study visa revocation", "Renew at Policia Federal. Work allowed 20h/week with authorization.", "University acceptance, proof of funds (~R$2,000/month), health insurance, clean criminal record"],
    work:          ["VITEM V Work Visa", "2 years (renewable)", "Heavy fines for employer + deportation", "Employer must apply at Ministry of Labour. After 4 years → permanent.", "Job offer, employer sponsorship, degree/experience, work permit from MTE"],
    retirement:    ["Permanent Visa (VIPER Aposentado)", "Permanent", "N/A", "Direct permanent residency for retirees. Transfer $2,000 USD/month to Brazil.", "Pension/income of $2,000 USD/month transferred to Brazilian bank, clean criminal record"],
    digital_nomad: ["Digital Nomad Visa (2022)", "1 year (non-renewable)", "Standard overstay fines", "Must leave after 1 year. Can re-apply. No Brazilian-source income allowed.", "Income min. $1,500 USD/month, proof of remote work, health insurance, no criminal record"]
  };
  D["cambodia"] = {
    tourism:       ["Tourist eVisa / Visa on Arrival", "30 days (extendable once)", "Fine $10/day overstay + deportation if >30 days", "eVisa ($36) or VOA ($30) at airport. Extend once for 30 days at Immigration.", "Passport 6+ months, passport photo, return ticket. Apply at evisa.gov.kh"],
    student:       ["E-Visa (Business/Education)", "1 year (renewable)", "Deportation + ban", "Use E-class visa for long-term study. Renew via school sponsorship.", "School acceptance, E-visa, health certificate"],
    work:          ["E-Visa (Business/Work)", "1 year (renewable)", "Working without permit = fines + deportation", "E-visa ($36) + work permit from Ministry of Labour. Renew annually.", "Job offer, E-visa, work permit application, health certificate, $100-280 work permit fee"],
    retirement:    ["ER Visa (Retirement)", "1 year (renewable)", "Standard penalties", "Must be 55+ and have pension/savings. Relatively new programme.", "Age 55+, proof of $50,000 savings or pension, health insurance"],
    digital_nomad: ["Tourist / Business e-Visa", "30 days (tourist) or 1 year (E-visa)", "Standard penalties", "No formal DN visa. Use tourist visa + extensions, or E-visa for longer stay.", "Apply eVisa at evisa.gov.kh ($36). E-visa for 1-year stays."]
  };
  D["china"] = {
    tourism:       ["L Tourist Visa", "30-90 days per entry", "Fine 500 CNY/day + detention + deportation + 1-10 year ban", "No visa-free (except 144h transit). Must apply at embassy or visa centre. 10-year multiple entry for US/UK/Canada.", "Passport 6+ months, hotel booking, return ticket, completed application, photo 48x33mm. Apply at visaforchina.cn"],
    student:       ["X1/X2 Student Visa", "X1: 4 years / X2: 6 months", "Heavy penalties + study ban + deportation", "X1 for degree programs, X2 for short courses. Must register at PSB within 30 days. JW202 form required.", "JW201/JW202 form, university acceptance, physical exam report, financial proof"],
    work:          ["Z Work Visa + Work Permit", "1-5 years", "Working illegally = 5,000-20,000 CNY fine + detention + deportation", "Employer applies for work permit notification. Categories A/B/C. After 5 years → permanent residence possible.", "Job offer, work permit notification letter, degree (authenticated), 2 years experience, health check"],
    retirement:    ["No Retirement Visa", "N/A", "N/A", "China has no retirement visa. Options: family reunion visa (Q1/Q2) if married to Chinese citizen.", "No direct pathway. Must qualify under family, work, or investor categories."],
    digital_nomad: ["No DN Visa (Tourist/Business)", "30-90 days (L visa)", "Standard heavy penalties", "No DN visa. Use L tourist visa or M business visa. 144h visa-free transit at select cities.", "Must apply for L or M visa. Remote work technically not permitted on tourist visa."]
  };
  D["costa-rica"] = {
    tourism:       ["Visa-Free / Tourist Visa", "90 days", "Fine $100/month overstay + deportation", "90 days visa-free for many nationalities. Border run to Nicaragua/Panama resets 90-day clock.", "Passport 6+ months, return ticket, proof of funds ($100/day), no eVisa needed for most"],
    student:       ["Student Visa (Residencia Estudiantil)", "1 year (renewable)", "Deportation + study ban", "Apply at DGME. Can work part-time with authorization.", "University acceptance, proof of funds, health insurance (CAJA or private), background check"],
    work:          ["Work Visa (Residencia Temporal Trabajador)", "1 year (renewable)", "Working illegally = deportation + ban", "Employer sponsors at DGME. After 3 years → permanent residency.", "Job offer, employer sponsorship, CAJA health insurance enrollment, background check"],
    retirement:    ["Pensionado Visa", "2 years (renewable)", "Loss of residency", "Min. $1,000/month pension. Must join CAJA ($50-150/month). Path to citizenship in 7 years.", "Pension of $1,000 USD/month minimum, background check, health insurance, Costa Rica bank account"],
    digital_nomad: ["Digital Nomad Visa (2021)", "1 year (renewable once)", "Standard penalties", "First in Central America. Renewable once for 1 more year. Tax-exempt on foreign income.", "Income min. $3,000 USD/month or $60,000/year savings, health insurance, remote work proof"]
  };
  D["germany"] = {
    tourism:       ["Schengen Visa / Visa-Free", "90 days in 180-day period", "Fine + deportation + Schengen-wide ban up to 5 years", "Leave Schengen zone for 90 days then return. No extension for tourist stays.", "Valid passport, travel insurance 30k EUR, proof of accommodation & funds"],
    student:       ["National Visa (Student)", "1-2 years (renewable)", "Deportation + study ban", "Apply at German embassy. Renew at Auslanderbehorde. 120 full days/240 half days work/year. After graduation → 18-month job search visa.", "University acceptance, blocked account (11,904 EUR/year), health insurance, language proof"],
    work:          ["EU Blue Card / Work Visa", "4 years (Blue Card)", "Fines + deportation + ban", "EU Blue Card: min. 45,300 EUR salary (39,682 for shortage occupations). PR after 21-33 months. Opportunity Card (2024) for job seekers.", "Job offer, degree recognition, salary threshold, health insurance, A1/B1 German for some roles"],
    retirement:    ["Residence Permit (private purposes)", "1 year (renewable)", "Loss of permit + deportation", "No formal retirement visa. Apply for residence permit based on sufficient funds. Health insurance mandatory.", "Proof of pension/income (~1,200+ EUR/month), comprehensive health insurance, accommodation proof"],
    digital_nomad: ["Freelance Visa (Freiberufler)", "1-3 years", "Standard Schengen penalties", "Germany offers freelance visa for self-employed. Must show client contracts and professional plan.", "Business plan, client contracts, professional qualifications, health insurance, sufficient income proof"]
  };
  D["hong-kong"] = {
    tourism:       ["Visa-Free / Tourist Visa", "14-180 days depending on nationality", "Fine + detention + deportation + ban", "UK/EU/US/Canada: 90 days visa-free. Japanese: 90 days. Chinese Mainland: Exit-Entry Permit. Extension possible at Immigration.", "Valid passport, return ticket, proof of funds. No eVisa system."],
    student:       ["Student Visa", "Duration of course", "Deportation + study ban", "Apply at Hong Kong Immigration. Can work 20h/week during term, unlimited during breaks. After graduation: IANG scheme (2 years).", "University acceptance, financial proof (HKD 100,000+/year), sponsor letter"],
    work:          ["Employment Visa / GEP", "2-3 years (renewable)", "Heavy penalties + deportation", "General Employment Policy: no quota. Top Talent Pass: $2.5M HKD income or top 100 university degree. After 7 years → PR.", "Job offer or Top Talent qualification, degree, relevant experience, employer sponsorship"],
    retirement:    ["Capital Investment Entrant Scheme", "2 years (renewable)", "Loss of visa", "CIES restarted 2024: invest $30M HKD in approved assets. No retirement visa otherwise.", "Investment of $30M HKD minimum in approved financial assets"],
    digital_nomad: ["No DN Visa", "90 days (tourist)", "Standard penalties", "No formal DN visa. Use visa-free entry (90 days for many). Cannot do local work.", "Enter as tourist. Remote work for overseas employer generally tolerated."]
  };

  // Add simplified entries for remaining countries (Schengen block, etc.)
  var schengenData = {
    tourism:       ["Schengen Visa / Visa-Free", "90 days in 180-day period", "Fine + deportation + Schengen-wide ban up to 5 years", "Leave Schengen zone for 90 days then return. No extension possible for tourist stays.", "Valid passport, travel insurance 30k EUR, proof of accommodation & funds"],
    student:       ["National D Visa (Student)", "1 year (renewable)", "Deportation + visa revocation", "Renew annually at local immigration. Can work part-time in most EU countries.", "University acceptance, proof of funds, health insurance, background check"],
    work:          ["Work Visa + Residence Permit", "1-2 years (renewable)", "Working illegally = fines + deportation", "EU Blue Card available in most countries. After 5 years → permanent residency.", "Job offer, employer sponsorship, degree certificate, skills matching occupation list"],
    retirement:    ["Long-Stay Visa (varies)", "1 year (renewable)", "Loss of visa + deportation", "Varies by country. Most require proof of income/pension. No work allowed.", "Pension/income proof, health insurance, accommodation proof. Requirements vary by country."],
    digital_nomad: ["Varies by country", "Varies", "Standard overstay penalties", "Many EU countries now offer DN visas: Spain, Portugal, Greece, Croatia, Czech Republic, Estonia, etc.", "Income min. 2,000-3,500 EUR/month depending on country, remote work proof, health insurance"]
  };

  // Apply Schengen defaults to countries without specific data
  var schengenCountries = ["austria","belgium","croatia","czech-republic","denmark","hungary","ireland","italy",
    "liechtenstein","luxembourg","netherlands","norway","poland","romania","slovakia","slovenia","sweden","switzerland"];
  schengenCountries.forEach(function(c) { if (!D[c]) D[c] = schengenData; });

  // Non-Schengen specific
  if (!D["united-kingdom"]) D["united-kingdom"] = {
    tourism:       ["Visa-Free / Standard Visitor Visa", "6 months (visa-free for many) / 6 months (SVV)", "Fine + removal + re-entry ban (1-10 years)", "No extension for visa-free. SVV can be extended in exceptional cases. No border runs.", "Passport, return ticket, proof of funds (~75 GBP/day), accommodation proof"],
    student:       ["Student Visa (Tier 4)", "Duration of course + wrap-up", "Removal + study ban + re-entry ban", "Student Route visa. Can work 20h/week. Graduate Route: 2 years post-study work.", "CAS from licensed sponsor, English proficiency (IELTS 5.5-7), financial proof (~11,502 GBP/year London)"],
    work:          ["Skilled Worker Visa", "Up to 5 years", "Removal + employer sanctions", "Skilled Worker visa. After 5 years → ILR (permanent). After 6 years → citizenship.", "Job offer from licensed sponsor, salary min. 38,700 GBP/year, English B1, certificate of sponsorship"],
    retirement:    ["No Retirement Visa", "N/A", "N/A", "UK has no retirement visa. Options: Innovator Founder visa, Global Talent, or family route.", "No direct retirement pathway. Ancestor visa for Commonwealth citizens with UK grandparent."],
    digital_nomad: ["No DN Visa (Standard Visitor)", "6 months", "Standard removal procedures", "No formal DN visa. Standard Visitor allows remote work for overseas employer. Cannot do UK-source work.", "Enter as visitor. Remote work for non-UK employer tolerated. No formal requirements."]
  };

  // Remaining Asian
  if (!D["singapore"]) D["singapore"] = {
    tourism:       ["Visa-Free / SG Arrival Card", "30-90 days", "Fine up to $4,000 SGD + jail up to 6 months + caning + deportation", "No extension for short visits. Must leave Singapore. SG Arrival Card online before arrival.", "Passport 6+ months, return ticket, proof of funds, SG Arrival Card (free)"],
    student:       ["Student Pass", "Duration of course", "Heavy penalties + deportation + ban", "Apply via ICA. Can work 16h/week during term. Internship during breaks allowed.", "IPA from ICA, university acceptance, financial proof, medical exam"],
    work:          ["Employment Pass (EP)", "2 years (renewable)", "Heavy fines + jail + deportation", "EP for professionals earning $5,000+ SGD/month. S Pass for mid-skilled. After 2+ years → PR possible.", "Job offer, salary min. $5,000 SGD/month, degree, employer sponsorship via MOM"],
    retirement:    ["No Retirement Visa", "N/A", "N/A", "Singapore has no retirement visa. Options: Employment Pass, Entrepass, or Global Investor Programme ($10M SGD).", "No direct pathway. GIP requires $10M SGD investment."],
    digital_nomad: ["Overseas Networks & Expertise Pass", "5 years", "Standard penalties", "ONE Pass for top talent ($30,000+ SGD/month). Tech@SG for tech companies. No standard DN visa.", "ONE Pass: salary $30,000+ SGD/month or exceptional achievements. Very selective."]
  };

  if (!D["new-zealand"]) D["new-zealand"] = {
    tourism:       ["NZeTA / Visitor Visa", "90 days (eTA) / 9 months (Visitor)", "Removal + 5-year re-entry ban", "NZeTA for visa-waiver countries ($12-$23 NZD). Visitor visa extendable up to 9 months total.", "NZeTA or Visitor Visa, IVL levy $35 NZD, proof of funds ($1,000 NZD/month)"],
    student:       ["Student Visa", "Duration of course + 3 months", "Removal + study ban", "Can work 20h/week during term. Post-Study Work Visa 1-3 years. Points system for PR.", "Offer of place, proof of funds ($20,000 NZD/year), health insurance, English proficiency"],
    work:          ["Essential Skills Work Visa", "Up to 3 years", "Removal + ban", "AEWV (Accredited Employer Work Visa). Employer must be accredited. Points for PR.", "Job offer from accredited employer, relevant skills/experience, median wage or above"],
    retirement:    ["Retirement Category Visa", "2 years (renewable)", "Standard penalties", "Invest $750,000 NZD + settle funds $500,000 + income $60,000 NZD/year. Small annual allocation.", "Age 66+, $750,000 NZD investment, $500,000 settlement funds, $60,000/year income. Very limited places."],
    digital_nomad: ["No DN Visa (Visitor)", "90 days (NZeTA)", "Standard penalties", "No formal DN visa. Working Holiday Visa for ages 18-30/35 from eligible countries (1-2 years).", "Working Holiday: 1 year, employer limit 3-6 months. Ages 18-30 (some 35). Eligible countries only."]
  };

  // Simple countries with less detailed data
  ["jordan","maldives","nepal","philippines","qatar","sri-lanka","taiwan","turkey"].forEach(function(c) {
    if (!D[c]) D[c] = {
      tourism:       ["Tourist Visa / Visa on Arrival / e-Visa", "30-90 days (varies)", "Fine + deportation + possible ban", "Check specific country requirements. Extensions usually available at immigration office.", "Passport 6+ months, return ticket, proof of funds, visa fee varies"],
      student:       ["Student Visa", "Duration of course", "Deportation + study ban", "Renew via educational institution. Requirements vary by country.", "University acceptance, proof of funds, health insurance"],
      work:          ["Work Visa + Permit", "1-2 years (renewable)", "Working without permit = fines + deportation", "Employer sponsors work permit. Requirements vary by country.", "Job offer, employer sponsorship, relevant qualifications"],
      retirement:    ["Varies / May not exist", "Varies", "Varies", "Check if country offers retirement visa. Many countries in this region have limited retirement options.", "Requirements vary. Check country-specific visa page for details."],
      digital_nomad: ["No specific DN Visa", "N/A", "Varies", "Use tourist visa for short stays. Few countries in this group offer formal DN programs.", "Check country-specific visa page for current options."]
    };
  });

  // ── Valid nationality combos (pre-built from file system) ──
  // Format: "destination|nationality" → true
  var COMBOS = {"argentina|argentinian":1,"argentina|australian":1,"argentina|brazilian":1,"argentina|canadian":1,"argentina|chinese":1,"argentina|french":1,"argentina|german":1,"argentina|indian":1,"argentina|indonesian":1,"argentina|japanese":1,"argentina|korean":1,"argentina|mexican":1,"argentina|nigerian":1,"argentina|philippine":1,"argentina|russian":1,"argentina|singaporean":1,"argentina|south-african":1,"argentina|turkish":1,"argentina|uk":1,"argentina|us":1,"australia|argentinian":1,"australia|brazilian":1,"australia|canadian":1,"australia|chinese":1,"australia|french":1,"australia|german":1,"australia|indian":1,"australia|indonesian":1,"australia|japanese":1,"australia|korean":1,"australia|mexican":1,"australia|new-zealand":1,"australia|nigerian":1,"australia|philippine":1,"australia|russian":1,"australia|singaporean":1,"australia|south-african":1,"australia|turkish":1,"australia|uk":1,"australia|us":1,"austria|argentinian":1,"austria|australian":1,"austria|brazilian":1,"austria|canadian":1,"austria|chinese":1,"austria|french":1,"austria|german":1,"austria|indian":1,"austria|indonesian":1,"austria|japanese":1,"austria|korean":1,"austria|mexican":1,"austria|nigerian":1,"austria|philippine":1,"austria|russian":1,"austria|singaporean":1,"austria|south-african":1,"austria|turkish":1,"austria|uk":1,"austria|us":1,"belgium|argentinian":1,"belgium|australian":1,"belgium|brazilian":1,"belgium|canadian":1,"belgium|chinese":1,"belgium|french":1,"belgium|german":1,"belgium|indian":1,"belgium|indonesian":1,"belgium|japanese":1,"belgium|korean":1,"belgium|mexican":1,"belgium|nigerian":1,"belgium|philippine":1,"belgium|russian":1,"belgium|singaporean":1,"belgium|south-african":1,"belgium|turkish":1,"belgium|uk":1,"belgium|us":1,"brazil|argentinian":1,"brazil|australian":1,"brazil|brazilian":1,"brazil|canadian":1,"brazil|chinese":1,"brazil|french":1,"brazil|german":1,"brazil|indian":1,"brazil|indonesian":1,"brazil|japanese":1,"brazil|korean":1,"brazil|mexican":1,"brazil|nigerian":1,"brazil|philippine":1,"brazil|russian":1,"brazil|singaporean":1,"brazil|south-african":1,"brazil|turkish":1,"brazil|uk":1,"brazil|us":1,"cambodia|argentinian":1,"cambodia|australian":1,"cambodia|brazilian":1,"cambodia|canadian":1,"cambodia|chinese":1,"cambodia|french":1,"cambodia|german":1,"cambodia|indian":1,"cambodia|indonesian":1,"cambodia|japanese":1,"cambodia|korean":1,"cambodia|mexican":1,"cambodia|nigerian":1,"cambodia|philippine":1,"cambodia|russian":1,"cambodia|singaporean":1,"cambodia|south-african":1,"cambodia|turkish":1,"cambodia|uk":1,"cambodia|us":1,"canada|argentinian":1,"canada|australian":1,"canada|brazilian":1,"canada|canadian":1,"canada|chinese":1,"canada|french":1,"canada|german":1,"canada|indian":1,"canada|indonesian":1,"canada|japanese":1,"canada|korean":1,"canada|mexican":1,"canada|nigerian":1,"canada|philippine":1,"canada|russian":1,"canada|singaporean":1,"canada|south-african":1,"canada|turkish":1,"canada|uk":1,"canada|us":1,"china|argentinian":1,"china|australian":1,"china|brazilian":1,"china|canadian":1,"china|chinese":1,"china|french":1,"china|german":1,"china|indian":1,"china|indonesian":1,"china|japanese":1,"china|korean":1,"china|mexican":1,"china|nigerian":1,"china|philippine":1,"china|russian":1,"china|singaporean":1,"china|south-african":1,"china|turkish":1,"china|uk":1,"china|us":1,"colombia|argentinian":1,"colombia|australian":1,"colombia|brazilian":1,"colombia|canadian":1,"colombia|chinese":1,"colombia|french":1,"colombia|german":1,"colombia|indian":1,"colombia|indonesian":1,"colombia|japanese":1,"colombia|korean":1,"colombia|mexican":1,"colombia|nigerian":1,"colombia|philippine":1,"colombia|russian":1,"colombia|singaporean":1,"colombia|south-african":1,"colombia|turkish":1,"colombia|uk":1,"colombia|us":1,"costa-rica|argentinian":1,"costa-rica|australian":1,"costa-rica|brazilian":1,"costa-rica|canadian":1,"costa-rica|chinese":1,"costa-rica|french":1,"costa-rica|german":1,"costa-rica|indian":1,"costa-rica|indonesian":1,"costa-rica|japanese":1,"costa-rica|korean":1,"costa-rica|mexican":1,"costa-rica|nigerian":1,"costa-rica|philippine":1,"costa-rica|russian":1,"costa-rica|singaporean":1,"costa-rica|south-african":1,"costa-rica|turkish":1,"costa-rica|uk":1,"costa-rica|us":1,"croatia|argentinian":1,"croatia|australian":1,"croatia|brazilian":1,"croatia|canadian":1,"croatia|chinese":1,"croatia|french":1,"croatia|german":1,"croatia|indian":1,"croatia|indonesian":1,"croatia|japanese":1,"croatia|korean":1,"croatia|mexican":1,"croatia|nigerian":1,"croatia|philippine":1,"croatia|russian":1,"croatia|singaporean":1,"croatia|south-african":1,"croatia|turkish":1,"croatia|uk":1,"croatia|us":1,"czech-republic|argentinian":1,"czech-republic|australian":1,"czech-republic|brazilian":1,"czech-republic|canadian":1,"czech-republic|chinese":1,"czech-republic|french":1,"czech-republic|german":1,"czech-republic|indian":1,"czech-republic|indonesian":1,"czech-republic|japanese":1,"czech-republic|korean":1,"czech-republic|mexican":1,"czech-republic|nigerian":1,"czech-republic|philippine":1,"czech-republic|russian":1,"czech-republic|singaporean":1,"czech-republic|south-african":1,"czech-republic|turkish":1,"czech-republic|uk":1,"czech-republic|us":1,"denmark|argentinian":1,"denmark|australian":1,"denmark|brazilian":1,"denmark|canadian":1,"denmark|chinese":1,"denmark|french":1,"denmark|german":1,"denmark|indian":1,"denmark|indonesian":1,"denmark|japanese":1,"denmark|korean":1,"denmark|mexican":1,"denmark|nigerian":1,"denmark|philippine":1,"denmark|russian":1,"denmark|singaporean":1,"denmark|south-african":1,"denmark|turkish":1,"denmark|uk":1,"denmark|us":1,"france|argentinian":1,"france|australian":1,"france|bangladeshi":1,"france|brazilian":1,"france|canadian":1,"france|chinese":1,"france|indian":1,"france|indonesian":1,"france|japanese":1,"france|korean":1,"france|mexican":1,"france|nigerian":1,"france|pakistani":1,"france|philippine":1,"france|russian":1,"france|singaporean":1,"france|south-african":1,"france|turkish":1,"france|uk":1,"france|us":1,"germany|argentinian":1,"germany|australian":1,"germany|brazilian":1,"germany|canadian":1,"germany|chinese":1,"germany|french":1,"germany|german":1,"germany|indian":1,"germany|indonesian":1,"germany|japanese":1,"germany|korean":1,"germany|mexican":1,"germany|nigerian":1,"germany|philippine":1,"germany|russian":1,"germany|singaporean":1,"germany|south-african":1,"germany|turkish":1,"germany|uk":1,"germany|us":1,"greece|argentinian":1,"greece|australian":1,"greece|brazilian":1,"greece|canadian":1,"greece|chinese":1,"greece|french":1,"greece|german":1,"greece|indian":1,"greece|indonesian":1,"greece|japanese":1,"greece|korean":1,"greece|mexican":1,"greece|nigerian":1,"greece|philippine":1,"greece|russian":1,"greece|singaporean":1,"greece|south-african":1,"greece|turkish":1,"greece|uk":1,"greece|us":1,"hong-kong|argentinian":1,"hong-kong|australian":1,"hong-kong|brazilian":1,"hong-kong|canadian":1,"hong-kong|chinese":1,"hong-kong|french":1,"hong-kong|german":1,"hong-kong|indian":1,"hong-kong|indonesian":1,"hong-kong|japanese":1,"hong-kong|korean":1,"hong-kong|mexican":1,"hong-kong|nigerian":1,"hong-kong|philippine":1,"hong-kong|russian":1,"hong-kong|singaporean":1,"hong-kong|south-african":1,"hong-kong|turkish":1,"hong-kong|uk":1,"hong-kong|us":1,"hungary|argentinian":1,"hungary|australian":1,"hungary|brazilian":1,"hungary|canadian":1,"hungary|chinese":1,"hungary|french":1,"hungary|german":1,"hungary|indian":1,"hungary|indonesian":1,"hungary|japanese":1,"hungary|korean":1,"hungary|mexican":1,"hungary|nigerian":1,"hungary|philippine":1,"hungary|russian":1,"hungary|singaporean":1,"hungary|south-african":1,"hungary|turkish":1,"hungary|uk":1,"hungary|us":1,"india|argentinian":1,"india|australian":1,"india|brazilian":1,"india|canadian":1,"india|chinese":1,"india|french":1,"india|german":1,"india|indian":1,"india|indonesian":1,"india|japanese":1,"india|korean":1,"india|mexican":1,"india|nigerian":1,"india|philippine":1,"india|russian":1,"india|singaporean":1,"india|south-african":1,"india|turkish":1,"india|uk":1,"india|us":1,"indonesia|argentinian":1,"indonesia|australian":1,"indonesia|brazilian":1,"indonesia|canadian":1,"indonesia|chinese":1,"indonesia|french":1,"indonesia|german":1,"indonesia|indian":1,"indonesia|indonesian":1,"indonesia|japanese":1,"indonesia|korean":1,"indonesia|mexican":1,"indonesia|nigerian":1,"indonesia|philippine":1,"indonesia|russian":1,"indonesia|singaporean":1,"indonesia|south-african":1,"indonesia|turkish":1,"indonesia|uk":1,"indonesia|us":1,"ireland|argentinian":1,"ireland|australian":1,"ireland|brazilian":1,"ireland|canadian":1,"ireland|chinese":1,"ireland|french":1,"ireland|german":1,"ireland|indian":1,"ireland|indonesian":1,"ireland|japanese":1,"ireland|korean":1,"ireland|mexican":1,"ireland|nigerian":1,"ireland|philippine":1,"ireland|russian":1,"ireland|singaporean":1,"ireland|south-african":1,"ireland|turkish":1,"ireland|uk":1,"ireland|us":1,"italy|argentinian":1,"italy|australian":1,"italy|brazilian":1,"italy|canadian":1,"italy|chinese":1,"italy|french":1,"italy|german":1,"italy|indian":1,"italy|indonesian":1,"italy|japanese":1,"italy|korean":1,"italy|mexican":1,"italy|nigerian":1,"italy|philippine":1,"italy|russian":1,"italy|singaporean":1,"italy|south-african":1,"italy|turkish":1,"italy|uk":1,"italy|us":1,"japan|argentinian":1,"japan|australian":1,"japan|brazilian":1,"japan|canadian":1,"japan|chinese":1,"japan|french":1,"japan|german":1,"japan|indian":1,"japan|indonesian":1,"japan|japanese":1,"japan|korean":1,"japan|mexican":1,"japan|nigerian":1,"japan|philippine":1,"japan|russian":1,"japan|singaporean":1,"japan|south-african":1,"japan|turkish":1,"japan|uk":1,"japan|us":1,"jordan|argentinian":1,"jordan|australian":1,"jordan|brazilian":1,"jordan|canadian":1,"jordan|chinese":1,"jordan|french":1,"jordan|german":1,"jordan|indian":1,"jordan|indonesian":1,"jordan|japanese":1,"jordan|korean":1,"jordan|mexican":1,"jordan|nigerian":1,"jordan|philippine":1,"jordan|russian":1,"jordan|singaporean":1,"jordan|south-african":1,"jordan|turkish":1,"jordan|uk":1,"jordan|us":1,"malaysia|argentinian":1,"malaysia|australian":1,"malaysia|brazilian":1,"malaysia|canadian":1,"malaysia|chinese":1,"malaysia|french":1,"malaysia|german":1,"malaysia|indian":1,"malaysia|indonesian":1,"malaysia|japanese":1,"malaysia|korean":1,"malaysia|mexican":1,"malaysia|nigerian":1,"malaysia|philippine":1,"malaysia|russian":1,"malaysia|singaporean":1,"malaysia|south-african":1,"malaysia|turkish":1,"malaysia|uk":1,"malaysia|us":1,"maldives|argentinian":1,"maldives|australian":1,"maldives|brazilian":1,"maldives|canadian":1,"maldives|chinese":1,"maldives|french":1,"maldives|german":1,"maldives|indian":1,"maldives|indonesian":1,"maldives|japanese":1,"maldives|korean":1,"maldives|mexican":1,"maldives|nigerian":1,"maldives|philippine":1,"maldives|russian":1,"maldives|singaporean":1,"maldives|south-african":1,"maldives|turkish":1,"maldives|uk":1,"maldives|us":1,"mexico|argentinian":1,"mexico|australian":1,"mexico|brazilian":1,"mexico|canadian":1,"mexico|chinese":1,"mexico|french":1,"mexico|german":1,"mexico|indian":1,"mexico|indonesian":1,"mexico|japanese":1,"mexico|korean":1,"mexico|mexican":1,"mexico|nigerian":1,"mexico|philippine":1,"mexico|russian":1,"mexico|singaporean":1,"mexico|south-african":1,"mexico|turkish":1,"mexico|uk":1,"mexico|us":1,"nepal|argentinian":1,"nepal|australian":1,"nepal|brazilian":1,"nepal|canadian":1,"nepal|chinese":1,"nepal|french":1,"nepal|german":1,"nepal|indian":1,"nepal|indonesian":1,"nepal|japanese":1,"nepal|korean":1,"nepal|mexican":1,"nepal|nigerian":1,"nepal|philippine":1,"nepal|russian":1,"nepal|singaporean":1,"nepal|south-african":1,"nepal|turkish":1,"nepal|uk":1,"nepal|us":1,"netherlands|argentinian":1,"netherlands|australian":1,"netherlands|brazilian":1,"netherlands|canadian":1,"netherlands|chinese":1,"netherlands|french":1,"netherlands|german":1,"netherlands|indian":1,"netherlands|indonesian":1,"netherlands|japanese":1,"netherlands|korean":1,"netherlands|mexican":1,"netherlands|nigerian":1,"netherlands|philippine":1,"netherlands|russian":1,"netherlands|singaporean":1,"netherlands|south-african":1,"netherlands|turkish":1,"netherlands|uk":1,"netherlands|us":1,"new-zealand|argentinian":1,"new-zealand|australian":1,"new-zealand|brazilian":1,"new-zealand|canadian":1,"new-zealand|chinese":1,"new-zealand|french":1,"new-zealand|german":1,"new-zealand|indian":1,"new-zealand|indonesian":1,"new-zealand|japanese":1,"new-zealand|korean":1,"new-zealand|mexican":1,"new-zealand|nigerian":1,"new-zealand|philippine":1,"new-zealand|russian":1,"new-zealand|singaporean":1,"new-zealand|south-african":1,"new-zealand|turkish":1,"new-zealand|uk":1,"new-zealand|us":1,"norway|argentinian":1,"norway|australian":1,"norway|brazilian":1,"norway|canadian":1,"norway|chinese":1,"norway|french":1,"norway|german":1,"norway|indian":1,"norway|indonesian":1,"norway|japanese":1,"norway|korean":1,"norway|mexican":1,"norway|nigerian":1,"norway|philippine":1,"norway|russian":1,"norway|singaporean":1,"norway|south-african":1,"norway|turkish":1,"norway|uk":1,"norway|us":1,"philippines|argentinian":1,"philippines|australian":1,"philippines|brazilian":1,"philippines|canadian":1,"philippines|chinese":1,"philippines|french":1,"philippines|german":1,"philippines|indian":1,"philippines|indonesian":1,"philippines|japanese":1,"philippines|korean":1,"philippines|mexican":1,"philippines|nigerian":1,"philippines|philippine":1,"philippines|russian":1,"philippines|singaporean":1,"philippines|south-african":1,"philippines|turkish":1,"philippines|uk":1,"philippines|us":1,"poland|argentinian":1,"poland|australian":1,"poland|brazilian":1,"poland|canadian":1,"poland|chinese":1,"poland|french":1,"poland|german":1,"poland|indian":1,"poland|indonesian":1,"poland|japanese":1,"poland|korean":1,"poland|mexican":1,"poland|nigerian":1,"poland|philippine":1,"poland|russian":1,"poland|singaporean":1,"poland|south-african":1,"poland|turkish":1,"poland|uk":1,"poland|us":1,"portugal|argentinian":1,"portugal|australian":1,"portugal|brazilian":1,"portugal|canadian":1,"portugal|chinese":1,"portugal|french":1,"portugal|german":1,"portugal|indian":1,"portugal|indonesian":1,"portugal|japanese":1,"portugal|korean":1,"portugal|mexican":1,"portugal|nigerian":1,"portugal|philippine":1,"portugal|russian":1,"portugal|singaporean":1,"portugal|south-african":1,"portugal|turkish":1,"portugal|uk":1,"portugal|us":1,"qatar|argentinian":1,"qatar|australian":1,"qatar|brazilian":1,"qatar|canadian":1,"qatar|chinese":1,"qatar|french":1,"qatar|german":1,"qatar|indian":1,"qatar|indonesian":1,"qatar|japanese":1,"qatar|korean":1,"qatar|mexican":1,"qatar|nigerian":1,"qatar|philippine":1,"qatar|russian":1,"qatar|singaporean":1,"qatar|south-african":1,"qatar|turkish":1,"qatar|uk":1,"qatar|us":1,"romania|argentinian":1,"romania|australian":1,"romania|brazilian":1,"romania|canadian":1,"romania|chinese":1,"romania|french":1,"romania|german":1,"romania|indian":1,"romania|indonesian":1,"romania|japanese":1,"romania|korean":1,"romania|mexican":1,"romania|nigerian":1,"romania|philippine":1,"romania|russian":1,"romania|singaporean":1,"romania|south-african":1,"romania|turkish":1,"romania|uk":1,"romania|us":1,"schengen|chinese":1,"schengen|indian":1,"schengen|indonesian":1,"schengen|nigerian":1,"schengen|philippine":1,"schengen|russian":1,"schengen|south-african":1,"schengen|turkish":1,"singapore|argentinian":1,"singapore|australian":1,"singapore|brazilian":1,"singapore|canadian":1,"singapore|chinese":1,"singapore|french":1,"singapore|german":1,"singapore|indian":1,"singapore|indonesian":1,"singapore|japanese":1,"singapore|korean":1,"singapore|mexican":1,"singapore|nigerian":1,"singapore|philippine":1,"singapore|russian":1,"singapore|singaporean":1,"singapore|south-african":1,"singapore|turkish":1,"singapore|uk":1,"singapore|us":1,"spain|argentinian":1,"spain|australian":1,"spain|brazilian":1,"spain|canadian":1,"spain|chinese":1,"spain|french":1,"spain|german":1,"spain|indian":1,"spain|indonesian":1,"spain|japanese":1,"spain|korean":1,"spain|mexican":1,"spain|nigerian":1,"spain|philippine":1,"spain|russian":1,"spain|singaporean":1,"spain|south-african":1,"spain|turkish":1,"spain|uk":1,"spain|us":1,"sri-lanka|argentinian":1,"sri-lanka|australian":1,"sri-lanka|brazilian":1,"sri-lanka|canadian":1,"sri-lanka|chinese":1,"sri-lanka|french":1,"sri-lanka|german":1,"sri-lanka|indian":1,"sri-lanka|indonesian":1,"sri-lanka|japanese":1,"sri-lanka|korean":1,"sri-lanka|mexican":1,"sri-lanka|nigerian":1,"sri-lanka|philippine":1,"sri-lanka|russian":1,"sri-lanka|singaporean":1,"sri-lanka|south-african":1,"sri-lanka|turkish":1,"sri-lanka|uk":1,"sri-lanka|us":1,"sweden|argentinian":1,"sweden|australian":1,"sweden|brazilian":1,"sweden|canadian":1,"sweden|chinese":1,"sweden|french":1,"sweden|german":1,"sweden|indian":1,"sweden|indonesian":1,"sweden|japanese":1,"sweden|korean":1,"sweden|mexican":1,"sweden|nigerian":1,"sweden|philippine":1,"sweden|russian":1,"sweden|singaporean":1,"sweden|south-african":1,"sweden|turkish":1,"sweden|uk":1,"sweden|us":1,"switzerland|argentinian":1,"switzerland|australian":1,"switzerland|brazilian":1,"switzerland|canadian":1,"switzerland|chinese":1,"switzerland|french":1,"switzerland|german":1,"switzerland|indian":1,"switzerland|indonesian":1,"switzerland|japanese":1,"switzerland|korean":1,"switzerland|mexican":1,"switzerland|nigerian":1,"switzerland|philippine":1,"switzerland|russian":1,"switzerland|singaporean":1,"switzerland|south-african":1,"switzerland|turkish":1,"switzerland|uk":1,"switzerland|us":1,"taiwan|argentinian":1,"taiwan|australian":1,"taiwan|brazilian":1,"taiwan|canadian":1,"taiwan|chinese":1,"taiwan|french":1,"taiwan|german":1,"taiwan|indian":1,"taiwan|indonesian":1,"taiwan|japanese":1,"taiwan|korean":1,"taiwan|mexican":1,"taiwan|nigerian":1,"taiwan|philippine":1,"taiwan|russian":1,"taiwan|singaporean":1,"taiwan|south-african":1,"taiwan|turkish":1,"taiwan|uk":1,"taiwan|us":1,"thailand|australian":1,"thailand|bangladeshi":1,"thailand|brazilian":1,"thailand|canadian":1,"thailand|chinese":1,"thailand|french":1,"thailand|german":1,"thailand|indian":1,"thailand|indonesian":1,"thailand|japanese":1,"thailand|korean":1,"thailand|mexican":1,"thailand|nigerian":1,"thailand|pakistani":1,"thailand|philippine":1,"thailand|russian":1,"thailand|singaporean":1,"thailand|south-african":1,"thailand|uk":1,"thailand|us":1,"turkey|argentinian":1,"turkey|australian":1,"turkey|brazilian":1,"turkey|canadian":1,"turkey|chinese":1,"turkey|french":1,"turkey|german":1,"turkey|indian":1,"turkey|indonesian":1,"turkey|japanese":1,"turkey|korean":1,"turkey|mexican":1,"turkey|nigerian":1,"turkey|philippine":1,"turkey|russian":1,"turkey|singaporean":1,"turkey|south-african":1,"turkey|turkish":1,"turkey|uk":1,"turkey|us":1,"uae|argentinian":1,"uae|australian":1,"uae|brazilian":1,"uae|canadian":1,"uae|chinese":1,"uae|french":1,"uae|german":1,"uae|indian":1,"uae|indonesian":1,"uae|japanese":1,"uae|korean":1,"uae|mexican":1,"uae|nigerian":1,"uae|philippine":1,"uae|russian":1,"uae|singaporean":1,"uae|south-african":1,"uae|turkish":1,"uae|uk":1,"uae|us":1,"united-kingdom|argentinian":1,"united-kingdom|australian":1,"united-kingdom|brazilian":1,"united-kingdom|canadian":1,"united-kingdom|chinese":1,"united-kingdom|french":1,"united-kingdom|german":1,"united-kingdom|indian":1,"united-kingdom|indonesian":1,"united-kingdom|japanese":1,"united-kingdom|korean":1,"united-kingdom|mexican":1,"united-kingdom|new-zealand":1,"united-kingdom|nigerian":1,"united-kingdom|philippine":1,"united-kingdom|russian":1,"united-kingdom|singaporean":1,"united-kingdom|south-african":1,"united-kingdom|turkish":1,"united-kingdom|us":1,"usa|argentinian":1,"usa|australian":1,"usa|brazilian":1,"usa|canadian":1,"usa|chinese":1,"usa|french":1,"usa|german":1,"usa|indian":1,"usa|indonesian":1,"usa|japanese":1,"usa|korean":1,"usa|mexican":1,"usa|nigerian":1,"usa|philippine":1,"usa|russian":1,"usa|singaporean":1,"usa|south-african":1,"usa|turkish":1,"usa|uk":1,"usa|us":1,"vietnam|argentinian":1,"vietnam|australian":1,"vietnam|brazilian":1,"vietnam|canadian":1,"vietnam|chinese":1,"vietnam|french":1,"vietnam|german":1,"vietnam|indian":1,"vietnam|indonesian":1,"vietnam|japanese":1,"vietnam|korean":1,"vietnam|mexican":1,"vietnam|nigerian":1,"vietnam|philippine":1,"vietnam|russian":1,"vietnam|singaporean":1,"vietnam|south-african":1,"vietnam|turkish":1,"vietnam|uk":1,"vietnam|us":1};
  // Labels per language
  var LABELS = {
    en: { nat: "YOUR NATIONALITY", dest: "DESTINATION COUNTRY", purpose: "PURPOSE OF TRAVEL", btn: "Find Visa Info", duration: "Maximum Stay", overstay: "Overstay Penalty", strategy: "Entry / Exit Strategy", requirements: "Key Requirements", details: "Full Visa Details", guide: "Expat Guide", tourism: "Tourism / Vacation", student: "Student / Study", work: "Work / Employment", retirement: "Retirement", digital_nomad: "Digital Nomad", fee: "Visa Fee", processing: "Processing Time", steps_title: "Step-by-Step Process", docs_title: "Required Documents", penalty_title: "Overstay Penalties", strategy_title: "Extension & Strategy", search_again: "Search Again", no_data: "No data available for this combination.", select_all: "Please select all three fields.", visa_for: "Visa" },
    fr: { nat: "VOTRE NATIONALITE", dest: "PAYS DE DESTINATION", purpose: "MOTIF DU VOYAGE", btn: "Trouver les Infos Visa", duration: "Sejour Maximum", overstay: "Penalite de Depassement", strategy: "Strategie Entree / Sortie", requirements: "Conditions Requises", details: "Details Complets du Visa", guide: "Guide Expatriation", tourism: "Tourisme / Vacances", student: "Etudiant / Etudes", work: "Travail / Emploi", retirement: "Retraite", digital_nomad: "Nomade Numerique", fee: "Frais de Visa", processing: "Delai de Traitement", steps_title: "Processus Etape par Etape", docs_title: "Documents Requis", penalty_title: "Penalites de Depassement", strategy_title: "Extension & Strategie", search_again: "Nouvelle Recherche", no_data: "Aucune donnee disponible pour cette combinaison.", select_all: "Veuillez selectionner les trois champs.", visa_for: "Visa" },
    es: { nat: "SU NACIONALIDAD", dest: "PAIS DE DESTINO", purpose: "MOTIVO DEL VIAJE", btn: "Buscar Info de Visa", duration: "Estancia Maxima", overstay: "Penalizacion por Exceso", strategy: "Estrategia Entrada / Salida", requirements: "Requisitos Clave", details: "Detalles Completos del Visa", guide: "Guia Expatriacion", tourism: "Turismo / Vacaciones", student: "Estudiante / Estudios", work: "Trabajo / Empleo", retirement: "Jubilacion", digital_nomad: "Nomada Digital", fee: "Tarifa de Visa", processing: "Tiempo de Procesamiento", steps_title: "Proceso Paso a Paso", docs_title: "Documentos Requeridos", penalty_title: "Penalizaciones por Exceso", strategy_title: "Extension y Estrategia", search_again: "Buscar de Nuevo", no_data: "No hay datos disponibles para esta combinacion.", select_all: "Por favor seleccione los tres campos.", visa_for: "Visa" },
    pt: { nat: "SUA NACIONALIDADE", dest: "PAIS DE DESTINO", purpose: "MOTIVO DA VIAGEM", btn: "Encontrar Info do Visto", duration: "Estadia Maxima", overstay: "Penalidade por Excesso", strategy: "Estrategia Entrada / Saida", requirements: "Requisitos Principais", details: "Detalhes Completos do Visto", guide: "Guia Expatriacao", tourism: "Turismo / Ferias", student: "Estudante / Estudos", work: "Trabalho / Emprego", retirement: "Aposentadoria", digital_nomad: "Nomade Digital", fee: "Taxa do Visto", processing: "Tempo de Processamento", steps_title: "Processo Passo a Passo", docs_title: "Documentos Necessarios", penalty_title: "Penalidades por Excesso", strategy_title: "Extensao e Estrategia", search_again: "Pesquisar Novamente", no_data: "Nenhum dado disponivel para esta combinacao.", select_all: "Por favor selecione os tres campos.", visa_for: "Visto" },
    zh: { nat: "\u60a8\u7684\u56fd\u7c4d", dest: "\u76ee\u7684\u5730\u56fd\u5bb6", purpose: "\u65c5\u884c\u76ee\u7684", btn: "\u67e5\u627e\u7b7e\u8bc1\u4fe1\u606f", duration: "\u6700\u957f\u505c\u7559", overstay: "\u903e\u671f\u7f5a\u6b3e", strategy: "\u5165\u5883/\u51fa\u5883\u7b56\u7565", requirements: "\u5173\u952e\u8981\u6c42", details: "\u5b8c\u6574\u7b7e\u8bc1\u8be6\u60c5", guide: "\u5916\u7c4d\u4eba\u58eb\u6307\u5357", tourism: "\u65c5\u6e38/\u5ea6\u5047", student: "\u5b66\u751f/\u7559\u5b66", work: "\u5de5\u4f5c/\u5c31\u4e1a", retirement: "\u9000\u4f11", digital_nomad: "\u6570\u5b57\u6e38\u6c11", fee: "\u7b7e\u8bc1\u8d39\u7528", processing: "\u5904\u7406\u65f6\u95f4", steps_title: "\u7533\u8bf7\u6b65\u9aa4", docs_title: "\u6240\u9700\u6587\u4ef6", penalty_title: "\u903e\u671f\u7f5a\u6b3e", strategy_title: "\u5ef6\u671f\u4e0e\u7b56\u7565", search_again: "\u91cd\u65b0\u641c\u7d22", no_data: "\u6682\u65e0\u6b64\u7ec4\u5408\u7684\u6570\u636e\u3002", select_all: "\u8bf7\u9009\u62e9\u6240\u6709\u4e09\u4e2a\u5b57\u6bb5\u3002", visa_for: "\u7b7e\u8bc1" },
    th: { nat: "\u0e2a\u0e31\u0e0d\u0e0a\u0e32\u0e15\u0e34\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13", dest: "\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e1b\u0e25\u0e32\u0e22\u0e17\u0e32\u0e07", purpose: "\u0e27\u0e31\u0e15\u0e16\u0e38\u0e1b\u0e23\u0e30\u0e2a\u0e07\u0e04\u0e4c", btn: "\u0e04\u0e49\u0e19\u0e2b\u0e32\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e27\u0e35\u0e0b\u0e48\u0e32", duration: "\u0e1e\u0e31\u0e01\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14", overstay: "\u0e04\u0e48\u0e32\u0e1b\u0e23\u0e31\u0e1a\u0e2d\u0e22\u0e39\u0e48\u0e40\u0e01\u0e34\u0e19", strategy: "\u0e01\u0e25\u0e22\u0e38\u0e17\u0e18\u0e4c\u0e40\u0e02\u0e49\u0e32/\u0e2d\u0e2d\u0e01", requirements: "\u0e02\u0e49\u0e2d\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e2b\u0e25\u0e31\u0e01", details: "\u0e23\u0e32\u0e22\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e27\u0e35\u0e0b\u0e48\u0e32\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", guide: "\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e1c\u0e39\u0e49\u0e1e\u0e33\u0e19\u0e31\u0e01", tourism: "\u0e17\u0e48\u0e2d\u0e07\u0e40\u0e17\u0e35\u0e48\u0e22\u0e27/\u0e1e\u0e31\u0e01\u0e1c\u0e48\u0e2d\u0e19", student: "\u0e19\u0e31\u0e01\u0e40\u0e23\u0e35\u0e22\u0e19/\u0e28\u0e36\u0e01\u0e29\u0e32", work: "\u0e17\u0e33\u0e07\u0e32\u0e19/\u0e08\u0e49\u0e32\u0e07\u0e07\u0e32\u0e19", retirement: "\u0e40\u0e01\u0e29\u0e35\u0e22\u0e13\u0e2d\u0e32\u0e22\u0e38", digital_nomad: "\u0e14\u0e34\u0e08\u0e34\u0e17\u0e31\u0e25\u0e42\u0e19\u0e41\u0e21\u0e14", fee: "\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e27\u0e35\u0e0b\u0e48\u0e32", processing: "\u0e23\u0e30\u0e22\u0e30\u0e40\u0e27\u0e25\u0e32\u0e14\u0e33\u0e40\u0e19\u0e34\u0e19\u0e01\u0e32\u0e23", steps_title: "\u0e02\u0e31\u0e49\u0e19\u0e15\u0e2d\u0e19\u0e01\u0e32\u0e23\u0e2a\u0e21\u0e31\u0e04\u0e23", docs_title: "\u0e40\u0e2d\u0e01\u0e2a\u0e32\u0e23\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e43\u0e0a\u0e49", penalty_title: "\u0e04\u0e48\u0e32\u0e1b\u0e23\u0e31\u0e1a\u0e2d\u0e22\u0e39\u0e48\u0e40\u0e01\u0e34\u0e19\u0e01\u0e33\u0e2b\u0e19\u0e14", strategy_title: "\u0e01\u0e32\u0e23\u0e15\u0e48\u0e2d\u0e2d\u0e32\u0e22\u0e38\u0e41\u0e25\u0e30\u0e01\u0e25\u0e22\u0e38\u0e17\u0e18\u0e4c", search_again: "\u0e04\u0e49\u0e19\u0e2b\u0e32\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07", no_data: "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e04\u0e49\u0e19\u0e2b\u0e32\u0e19\u0e35\u0e49", select_all: "\u0e01\u0e23\u0e38\u0e13\u0e32\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e32\u0e21\u0e0a\u0e48\u0e2d\u0e07", visa_for: "\u0e27\u0e35\u0e0b\u0e48\u0e32" },
    ru: { nat: "\u0412\u0410\u0428\u0415 \u0413\u0420\u0410\u0416\u0414\u0410\u041d\u0421\u0422\u0412\u041e", dest: "\u0421\u0422\u0420\u0410\u041d\u0410 \u041d\u0410\u0417\u041d\u0410\u0427\u0415\u041d\u0418\u042f", purpose: "\u0426\u0415\u041b\u042c \u041f\u041e\u0415\u0417\u0414\u041a\u0418", btn: "\u041d\u0430\u0439\u0442\u0438 \u0438\u043d\u0444\u043e \u043e \u0432\u0438\u0437\u0435", duration: "\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u0435\u0431\u044b\u0432\u0430\u043d\u0438\u0435", overstay: "\u0428\u0442\u0440\u0430\u0444 \u0437\u0430 \u043f\u0440\u043e\u0441\u0440\u043e\u0447\u043a\u0443", strategy: "\u0421\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u044f \u0432\u044a\u0435\u0437\u0434\u0430/\u0432\u044b\u0435\u0437\u0434\u0430", requirements: "\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u044f", details: "\u041f\u043e\u043b\u043d\u044b\u0435 \u0434\u0435\u0442\u0430\u043b\u0438 \u0432\u0438\u0437\u044b", guide: "\u0413\u0438\u0434 \u044d\u043a\u0441\u043f\u0430\u0442\u0430", tourism: "\u0422\u0443\u0440\u0438\u0437\u043c/\u041e\u0442\u0434\u044b\u0445", student: "\u0421\u0442\u0443\u0434\u0435\u043d\u0442/\u0423\u0447\u0435\u0431\u0430", work: "\u0420\u0430\u0431\u043e\u0442\u0430/\u0422\u0440\u0443\u0434\u043e\u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", retirement: "\u041f\u0435\u043d\u0441\u0438\u044f", digital_nomad: "\u0426\u0438\u0444\u0440\u043e\u0432\u043e\u0439 \u043a\u043e\u0447\u0435\u0432\u043d\u0438\u043a", fee: "\u0412\u0438\u0437\u043e\u0432\u044b\u0439 \u0441\u0431\u043e\u0440", processing: "\u0421\u0440\u043e\u043a \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", steps_title: "\u041f\u043e\u0448\u0430\u0433\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0446\u0435\u0441\u0441", docs_title: "\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", penalty_title: "\u0428\u0442\u0440\u0430\u0444\u044b \u0437\u0430 \u043f\u0440\u043e\u0441\u0440\u043e\u0447\u043a\u0443", strategy_title: "\u041f\u0440\u043e\u0434\u043b\u0435\u043d\u0438\u0435 \u0438 \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u044f", search_again: "\u041d\u043e\u0432\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", no_data: "\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u044d\u0442\u043e\u0439 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438.", select_all: "\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0441\u0435 \u0442\u0440\u0438 \u043f\u043e\u043b\u044f.", visa_for: "\u0412\u0438\u0437\u0430" },
    ar: { nat: "\u062c\u0646\u0633\u064a\u062a\u0643", dest: "\u0628\u0644\u062f \u0627\u0644\u0648\u062c\u0647\u0629", purpose: "\u063a\u0631\u0636 \u0627\u0644\u0633\u0641\u0631", btn: "\u0628\u062d\u062b \u0639\u0646 \u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0629", duration: "\u0623\u0642\u0635\u0649 \u0625\u0642\u0627\u0645\u0629", overstay: "\u063a\u0631\u0627\u0645\u0629 \u062a\u062c\u0627\u0648\u0632 \u0627\u0644\u0645\u062f\u0629", strategy: "\u0627\u0633\u062a\u0631\u0627\u062a\u064a\u062c\u064a\u0629 \u0627\u0644\u062f\u062e\u0648\u0644/\u0627\u0644\u062e\u0631\u0648\u062c", requirements: "\u0627\u0644\u0645\u062a\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629", details: "\u062a\u0641\u0627\u0635\u064a\u0644 \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0629 \u0627\u0644\u0643\u0627\u0645\u0644\u0629", guide: "\u062f\u0644\u064a\u0644 \u0627\u0644\u0645\u063a\u062a\u0631\u0628\u064a\u0646", tourism: "\u0633\u064a\u0627\u062d\u0629/\u0625\u062c\u0627\u0632\u0629", student: "\u0637\u0627\u0644\u0628/\u062f\u0631\u0627\u0633\u0629", work: "\u0639\u0645\u0644/\u062a\u0648\u0638\u064a\u0641", retirement: "\u062a\u0642\u0627\u0639\u062f", digital_nomad: "\u0631\u062d\u0627\u0644\u0629 \u0631\u0642\u0645\u064a\u0629", fee: "\u0631\u0633\u0648\u0645 \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0629", processing: "\u0648\u0642\u062a \u0627\u0644\u0645\u0639\u0627\u0644\u062c\u0629", steps_title: "\u0627\u0644\u062e\u0637\u0648\u0627\u062a", docs_title: "\u0627\u0644\u0645\u0633\u062a\u0646\u062f\u0627\u062a \u0627\u0644\u0645\u0637\u0644\u0648\u0628\u0629", penalty_title: "\u063a\u0631\u0627\u0645\u0627\u062a \u062a\u062c\u0627\u0648\u0632 \u0627\u0644\u0645\u062f\u0629", strategy_title: "\u0627\u0644\u062a\u0645\u062f\u064a\u062f \u0648\u0627\u0644\u0627\u0633\u062a\u0631\u0627\u062a\u064a\u062c\u064a\u0629", search_again: "\u0628\u062d\u062b \u062c\u062f\u064a\u062f", no_data: "\u0644\u0627 \u062a\u0648\u062c\u062f \u0628\u064a\u0627\u0646\u0627\u062a \u0644\u0647\u0630\u0627 \u0627\u0644\u0627\u062e\u062a\u064a\u0627\u0631.", select_all: "\u064a\u0631\u062c\u0649 \u0627\u062e\u062a\u064a\u0627\u0631 \u062c\u0645\u064a\u0639 \u0627\u0644\u062d\u0642\u0648\u0644 \u0627\u0644\u062b\u0644\u0627\u062b\u0629.", visa_for: "\u062a\u0623\u0634\u064a\u0631\u0629" },
    ja: { nat: "\u56fd\u7c4d", dest: "\u76ee\u7684\u5730", purpose: "\u6e21\u822a\u76ee\u7684", btn: "\u30d3\u30b6\u60c5\u5831\u3092\u691c\u7d22", duration: "\u6700\u5927\u6ede\u5728\u671f\u9593", overstay: "\u30aa\u30fc\u30d0\u30fc\u30b9\u30c6\u30a4\u7f70\u5247", strategy: "\u5165\u51fa\u56fd\u6226\u7565", requirements: "\u4e3b\u306a\u8981\u4ef6", details: "\u30d3\u30b6\u8a73\u7d30", guide: "\u99d0\u5728\u30ac\u30a4\u30c9", tourism: "\u89b3\u5149/\u4f11\u6687", student: "\u5b66\u751f/\u7559\u5b66", work: "\u5c31\u52b4/\u96c7\u7528", retirement: "\u9000\u8077", digital_nomad: "\u30c7\u30b8\u30bf\u30eb\u30ce\u30de\u30c9", fee: "\u30d3\u30b6\u6599\u91d1", processing: "\u51e6\u7406\u6642\u9593", steps_title: "\u7533\u8acb\u30b9\u30c6\u30c3\u30d7", docs_title: "\u5fc5\u8981\u66f8\u985e", penalty_title: "\u30aa\u30fc\u30d0\u30fc\u30b9\u30c6\u30a4\u7f70\u5247", strategy_title: "\u5ef6\u9577\u3068\u6226\u7565", search_again: "\u518d\u691c\u7d22", no_data: "\u3053\u306e\u7d44\u307f\u5408\u308f\u305b\u306e\u30c7\u30fc\u30bf\u306f\u3042\u308a\u307e\u305b\u3093\u3002", select_all: "3\u3064\u306e\u30d5\u30a3\u30fc\u30eb\u30c9\u3092\u3059\u3079\u3066\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\u3002", visa_for: "\u30d3\u30b6" },
    ko: { nat: "\uad6d\uc801", dest: "\ubaa9\uc801\uc9c0 \uad6d\uac00", purpose: "\uc5ec\ud589 \ubaa9\uc801", btn: "\ube44\uc790 \uc815\ubcf4 \uac80\uc0c9", duration: "\ucd5c\ub300 \uccb4\ub958", overstay: "\ubd88\ubc95\uccb4\ub958 \ubc8c\uae08", strategy: "\uc785\ucd9c\uad6d \uc804\ub7b5", requirements: "\uc8fc\uc694 \uc694\uac74", details: "\ube44\uc790 \uc0c1\uc138", guide: "\uc8fc\uc7ac\uc6d0 \uac00\uc774\ub4dc", tourism: "\uad00\uad11/\ud734\uac00", student: "\ud559\uc0dd/\uc720\ud559", work: "\ucde8\uc5c5/\uace0\uc6a9", retirement: "\uc740\ud1f4", digital_nomad: "\ub514\uc9c0\ud138\ub178\ub9c8\ub4dc", fee: "\ube44\uc790 \uc218\uc218\ub8cc", processing: "\ucc98\ub9ac \uc2dc\uac04", steps_title: "\uc2e0\uccad \ub2e8\uacc4", docs_title: "\ud544\uc694 \uc11c\ub958", penalty_title: "\ubd88\ubc95\uccb4\ub958 \ubc8c\uae08", strategy_title: "\uc5f0\uc7a5 \ubc0f \uc804\ub7b5", search_again: "\ub2e4\uc2dc \uac80\uc0c9", no_data: "\uc774 \uc870\ud569\uc5d0 \ub300\ud55c \ub370\uc774\ud130\uac00 \uc5c6\uc2b5\ub2c8\ub2e4.", select_all: "\uc138 \uac00\uc9c0 \ud544\ub4dc\ub97c \ubaa8\ub450 \uc120\ud0dd\ud574 \uc8fc\uc138\uc694.", visa_for: "\ube44\uc790" }
  };

  // ── Translated country names per language ──
  var COUNTRY_NAMES = {
    fr: {"argentina":"Argentine","australia":"Australie","austria":"Autriche","belgium":"Belgique","brazil":"Bresil","cambodia":"Cambodge","canada":"Canada","china":"Chine","colombia":"Colombie","costa-rica":"Costa Rica","croatia":"Croatie","czech-republic":"Republique tcheque","denmark":"Danemark","france":"France","germany":"Allemagne","greece":"Grece","hong-kong":"Hong Kong","hungary":"Hongrie","india":"Inde","indonesia":"Indonesie","ireland":"Irlande","italy":"Italie","japan":"Japon","jordan":"Jordanie","liechtenstein":"Liechtenstein","luxembourg":"Luxembourg","malaysia":"Malaisie","maldives":"Maldives","mexico":"Mexique","nepal":"Nepal","netherlands":"Pays-Bas","new-zealand":"Nouvelle-Zelande","norway":"Norvege","panama":"Panama","paraguay":"Paraguay","philippines":"Philippines","poland":"Pologne","portugal":"Portugal","qatar":"Qatar","romania":"Roumanie","singapore":"Singapour","slovakia":"Slovaquie","slovenia":"Slovenie","spain":"Espagne","sri-lanka":"Sri Lanka","sweden":"Suede","switzerland":"Suisse","taiwan":"Taiwan","thailand":"Thailande","turkey":"Turquie","uae":"Emirats arabes unis","united-kingdom":"Royaume-Uni","usa":"Etats-Unis","vietnam":"Vietnam"},
    es: {"argentina":"Argentina","australia":"Australia","austria":"Austria","belgium":"Belgica","brazil":"Brasil","cambodia":"Camboya","canada":"Canada","china":"China","colombia":"Colombia","costa-rica":"Costa Rica","croatia":"Croacia","czech-republic":"Republica Checa","denmark":"Dinamarca","france":"Francia","germany":"Alemania","greece":"Grecia","hong-kong":"Hong Kong","hungary":"Hungria","india":"India","indonesia":"Indonesia","ireland":"Irlanda","italy":"Italia","japan":"Japon","jordan":"Jordania","liechtenstein":"Liechtenstein","luxembourg":"Luxemburgo","malaysia":"Malasia","maldives":"Maldivas","mexico":"Mexico","nepal":"Nepal","netherlands":"Paises Bajos","new-zealand":"Nueva Zelanda","norway":"Noruega","panama":"Panama","paraguay":"Paraguay","philippines":"Filipinas","poland":"Polonia","portugal":"Portugal","qatar":"Catar","romania":"Rumania","singapore":"Singapur","slovakia":"Eslovaquia","slovenia":"Eslovenia","spain":"Espana","sri-lanka":"Sri Lanka","sweden":"Suecia","switzerland":"Suiza","taiwan":"Taiwan","thailand":"Tailandia","turkey":"Turquia","uae":"Emiratos Arabes Unidos","united-kingdom":"Reino Unido","usa":"Estados Unidos","vietnam":"Vietnam"},
    pt: {"argentina":"Argentina","australia":"Australia","austria":"Austria","belgium":"Belgica","brazil":"Brasil","cambodia":"Camboja","canada":"Canada","china":"China","colombia":"Colombia","costa-rica":"Costa Rica","croatia":"Croacia","czech-republic":"Republica Checa","denmark":"Dinamarca","france":"Franca","germany":"Alemanha","greece":"Grecia","hong-kong":"Hong Kong","hungary":"Hungria","india":"India","indonesia":"Indonesia","ireland":"Irlanda","italy":"Italia","japan":"Japao","jordan":"Jordania","liechtenstein":"Liechtenstein","luxembourg":"Luxemburgo","malaysia":"Malasia","maldives":"Maldivas","mexico":"Mexico","nepal":"Nepal","netherlands":"Paises Baixos","new-zealand":"Nova Zelandia","norway":"Noruega","panama":"Panama","paraguay":"Paraguai","philippines":"Filipinas","poland":"Polonia","portugal":"Portugal","qatar":"Catar","romania":"Romenia","singapore":"Singapura","slovakia":"Eslovaquia","slovenia":"Eslovenia","spain":"Espanha","sri-lanka":"Sri Lanka","sweden":"Suecia","switzerland":"Suica","taiwan":"Taiwan","thailand":"Tailandia","turkey":"Turquia","uae":"Emirados Arabes Unidos","united-kingdom":"Reino Unido","usa":"Estados Unidos","vietnam":"Vietna"}
  };
  // Also translate nationalities
  var NAT_NAMES = {
    fr: {"argentinian":"Argentin","australian":"Australien","bangladeshi":"Bangladais","brazilian":"Bresilien","canadian":"Canadien","chinese":"Chinois","french":"Francais","german":"Allemand","indian":"Indien","indonesian":"Indonesien","japanese":"Japonais","korean":"Coreen","mexican":"Mexicain","new-zealand":"Neo-Zelandais","nigerian":"Nigerian","pakistani":"Pakistanais","philippine":"Philippin","russian":"Russe","singaporean":"Singapourien","south-african":"Sud-Africain","turkish":"Turc","uk":"Britannique","us":"Americain"},
    es: {"argentinian":"Argentino","australian":"Australiano","bangladeshi":"Bangladesi","brazilian":"Brasileno","canadian":"Canadiense","chinese":"Chino","french":"Frances","german":"Aleman","indian":"Indio","indonesian":"Indonesio","japanese":"Japones","korean":"Coreano","mexican":"Mexicano","new-zealand":"Neozelandes","nigerian":"Nigeriano","pakistani":"Paquistani","philippine":"Filipino","russian":"Ruso","singaporean":"Singapurense","south-african":"Sudafricano","turkish":"Turco","uk":"Britanico","us":"Estadounidense"},
    pt: {"argentinian":"Argentino","australian":"Australiano","bangladeshi":"Bengali","brazilian":"Brasileiro","canadian":"Canadense","chinese":"Chines","french":"Frances","german":"Alemao","indian":"Indiano","indonesian":"Indonesio","japanese":"Japones","korean":"Coreano","mexican":"Mexicano","new-zealand":"Neozelandes","nigerian":"Nigeriano","pakistani":"Paquistanes","philippine":"Filipino","russian":"Russo","singaporean":"Singapuriano","south-african":"Sul-Africano","turkish":"Turco","uk":"Britanico","us":"Americano"}
  };

  function getLang() {
    var path = window.location.pathname;
    var m = path.match(/^\/(fr|es|pt|zh|th|ru|ar|ja|ko)\//);
    return m ? m[1] : "en";
  }

  function init() {
    var container = document.getElementById("visa-search-container");
    if (!container) return;
    var lang = getLang();
    var L = LABELS[lang] || LABELS.en;

    var cn = COUNTRY_NAMES[lang] || {};
    var nn = NAT_NAMES[lang] || {};
    var natOpts = '<option value="">-- Select --</option>';
    NATIONALITIES.forEach(function(n) {
      natOpts += '<option value="' + n.s + '">' + (nn[n.s] || n.n) + '</option>';
    });
    var destOpts = '<option value="">-- Select --</option>';
    DESTINATIONS.forEach(function(d) {
      destOpts += '<option value="' + d.s + '">' + (cn[d.s] || d.n) + '</option>';
    });
    var purposeOpts = '<option value="">-- Select --</option>';
    PURPOSES.forEach(function(p) {
      purposeOpts += '<option value="' + p.s + '">' + (L[p.s] || p.n) + '</option>';
    });

    container.innerHTML =
      '<div class="visa-search-form">' +
        '<div class="visa-search-field">' +
          '<label for="vs-nat">' + L.nat + '</label>' +
          '<select id="vs-nat">' + natOpts + '</select>' +
        '</div>' +
        '<div class="visa-search-field">' +
          '<label for="vs-dest">' + L.dest + '</label>' +
          '<select id="vs-dest">' + destOpts + '</select>' +
        '</div>' +
        '<div class="visa-search-field">' +
          '<label for="vs-purpose">' + L.purpose + '</label>' +
          '<select id="vs-purpose">' + purposeOpts + '</select>' +
        '</div>' +
        '<div class="visa-search-field visa-search-btn-wrap">' +
          '<button id="vs-btn" type="button" class="btn btn-primary">' + L.btn + ' &rarr;</button>' +
        '</div>' +
      '</div>' +
      '<div id="visa-result-panel" style="display:none;"></div>';

    document.getElementById("vs-btn").addEventListener("click", function() { showResult(lang); });
  }

  function showResult(lang) {
    var nat = document.getElementById("vs-nat").value;
    var dest = document.getElementById("vs-dest").value;
    var purpose = document.getElementById("vs-purpose").value;
    var panel = document.getElementById("visa-result-panel");
    var L = LABELS[lang] || LABELS.en;

    if (!nat || !dest || !purpose) {
      panel.style.display = "block";
      panel.innerHTML = '<div class="visa-result-error">' + (L.select_all || "Please select all three fields.") + '</div>';
      return;
    }

    var countryData = D[dest];
    if (!countryData || !countryData[purpose]) {
      panel.style.display = "block";
      panel.innerHTML = '<div class="visa-result-error">' + (L.no_data || "No data available for this combination.") + '</div>';
      return;
    }

    // Redirect to dedicated result page
    var resultUrl = "/" + lang + "/visa-result.html?nat=" + encodeURIComponent(nat) + "&dest=" + encodeURIComponent(dest) + "&purpose=" + encodeURIComponent(purpose);
    window.location.href = resultUrl;
  }

  // ── Enhanced data: fee, processing_time, steps, documents per destination×purpose ──
  var EXTRA = {
    "thailand": {
      tourism: { fee: "Free (visa-exempt) / THB 2,000 (~$55)", processing: "Instant (visa-free) / 3-5 business days", steps: ["Check if your nationality is visa-exempt (93 countries qualify for 30-60 day stays)","Complete Thailand Digital Arrival Card (TDAC) at tdac.immigration.go.th before travel","Prepare documents: passport valid 6+ months, return ticket, proof of accommodation, proof of funds","At immigration, present your passport and TDAC QR code to the officer","Receive your 30 or 60-day stamp in your passport upon entry"], documents: ["Passport valid at least 6 months beyond entry date","Return or onward flight ticket","Proof of accommodation (hotel booking or invitation letter)","Proof of funds (20,000 THB per person or equivalent)","TDAC QR code (completed online before arrival)"] },
      student: { fee: "THB 2,000 (~$55)", processing: "5-10 business days", steps: ["Obtain acceptance letter from a Thai school or university","Apply for Non-Immigrant ED Visa at Thai embassy or consulate in your home country","Prepare documents: acceptance letter, financial proof, medical certificate, passport photos","Attend visa interview if required and pay the visa fee","Upon approval, enter Thailand and report to Immigration within 90 days"], documents: ["Acceptance letter from Thai educational institution","Passport valid at least 6 months","Financial proof showing sufficient funds","Medical certificate from approved clinic","Passport-sized photos (4x6 cm)","Completed visa application form"] },
      work: { fee: "THB 2,000 (~$55) + Work Permit fees", processing: "5-15 business days", steps: ["Secure a job offer from a Thai company willing to sponsor your work permit","Employer applies for work permit at Ministry of Labour","Apply for Non-Immigrant B Visa at Thai embassy with work permit notification","Enter Thailand and complete work permit process at the Labour Office","Register your address with Immigration and set up 90-day reporting"], documents: ["Valid passport with at least 6 months validity","Job offer letter from Thai employer","Work permit application and notification letter","Degree certificate (apostilled or legalized)","Medical certificate","Passport-sized photos","Company registration documents from employer"] },
      retirement: { fee: "THB 2,000 (~$55)", processing: "5-10 business days", steps: ["Open a Thai bank account and deposit 800,000 THB (or show 65,000 THB/month income)","Obtain health insurance meeting Thai requirements (40k outpatient / 400k inpatient)","Apply for Non-Immigrant O-A visa at Thai embassy in your home country","Enter Thailand and report to Immigration within 90 days","Set up 90-day reporting and obtain re-entry permit if planning to travel"], documents: ["Passport valid at least 18 months","Proof of age (50 years or older)","Thai bank statement showing 800,000 THB or income proof of 65,000 THB/month","Health insurance policy meeting Thai government requirements","Medical certificate","Police clearance certificate from home country"] },
      digital_nomad: { fee: "$10,000 application fee", processing: "20-30 business days", steps: ["Verify you meet income requirements ($80,000+/year or $250,000+ in assets)","Prepare application documents including income proof and employment contracts","Submit LTR visa application online through the BOI website","Wait for approval notification from the Board of Investment","Collect your 10-year LTR visa and enter Thailand"], documents: ["Proof of income $80,000+/year from foreign employer","Employment contract or business ownership proof","Health insurance with minimum $50,000 coverage","Passport valid for the duration of the visa","Criminal background check from home country","Passport-sized photos"] }
    },
    "portugal": {
      tourism: { fee: "Free (EU/US/UK) / EUR 80 (Schengen visa)", processing: "Instant (visa-free) / 15 business days", steps: ["Check if your nationality qualifies for Schengen visa-free entry (90 days)","If visa required, apply at Portuguese embassy or VFS Global center","Prepare proof of accommodation, travel insurance (30k EUR), and financial means","Enter Portugal through any Schengen border checkpoint","Keep all proof of funds and accommodation for potential border checks"], documents: ["Passport valid 3+ months beyond intended stay","Travel insurance with 30,000 EUR minimum coverage","Proof of accommodation (hotel booking or host letter)","Proof of sufficient funds (approx. 75 EUR/day)","Return or onward flight ticket"] },
      student: { fee: "EUR 75 (visa) + EUR 83 (residence permit)", processing: "30-60 business days", steps: ["Obtain acceptance letter from a Portuguese university","Apply for D4 Student Visa at the Portuguese consulate in your country","Prepare financial proof showing at least 705 EUR/month available","Enter Portugal and schedule appointment at AIMA for residence permit","Obtain your residence permit within 4 months of arrival"], documents: ["University acceptance letter","Passport valid for duration of studies","Proof of funds (705 EUR/month minimum)","Health insurance coverage","Clean criminal record certificate (apostilled)","Proof of accommodation in Portugal"] },
      work: { fee: "EUR 75 (visa) + EUR 83 (residence permit)", processing: "30-60 business days", steps: ["Obtain a job contract from a Portuguese employer","Employer proves no EU candidate available for the position","Apply for D1 Work Visa at Portuguese consulate","Enter Portugal and schedule AIMA appointment for residence permit","Collect your residence permit and register for NIF tax number"], documents: ["Employment contract with Portuguese company","Passport valid for duration of contract","Proof of accommodation","Criminal record certificate (apostilled)","Health insurance","Employer declaration and company documents"] },
      retirement: { fee: "EUR 75 (visa) + EUR 83 (residence permit)", processing: "30-60 business days", steps: ["Obtain a Portuguese NIF tax number (can be done remotely via representative)","Open a Portuguese bank account","Apply for D7 Passive Income Visa at Portuguese consulate","Demonstrate passive income of at least 760 EUR/month","Enter Portugal and apply for residence permit at AIMA"], documents: ["Proof of passive income (760 EUR/month minimum) - pension, dividends, rental","Portuguese NIF tax number","Portuguese bank account statement","Health insurance valid in Portugal","Criminal record certificate (apostilled)","Proof of accommodation in Portugal"] },
      digital_nomad: { fee: "EUR 75 (visa) + EUR 83 (residence permit)", processing: "30-60 business days", steps: ["Verify your remote income meets 3,040 EUR/month minimum","Gather proof of employment with non-Portuguese company","Apply for D8 Digital Nomad Visa at Portuguese consulate","Enter Portugal and apply for residence permit at AIMA","Register for NIF and set up Portuguese banking"], documents: ["Proof of remote income minimum 3,040 EUR/month","Employment contract or freelance contracts with foreign clients","Health insurance valid in Portugal","Criminal record certificate (apostilled)","Proof of accommodation in Portugal","Passport valid for visa duration"] }
    },
    "japan": {
      tourism: { fee: "Free (visa-free for most Western nations)", processing: "Instant (visa-free)", steps: ["Check if your nationality qualifies for visa-free entry to Japan (90 days for most Western nations)","Complete Visit Japan Web registration online before travel","Book return or onward flight - this is strictly checked at entry","Prepare proof of accommodation and sufficient funds","Present passport and completed forms at immigration on arrival"], documents: ["Passport valid for duration of stay","Return or onward flight ticket","Proof of accommodation","Proof of sufficient funds","Visit Japan Web QR code (completed online)"] },
      student: { fee: "JPY 3,000 (~$20)", processing: "1-3 months (COE processing)", steps: ["Apply to a Japanese school and receive acceptance","School applies for Certificate of Eligibility (COE) at Immigration Bureau","Once COE is issued, apply for Student Visa at Japanese embassy","Enter Japan and complete residence registration at your local ward office","Apply for work permission (28h/week) if needed"], documents: ["Certificate of Eligibility (COE)","Passport valid for duration of studies","Financial proof (~200,000 JPY/month)","University acceptance letter","Passport-sized photos (4.5x3.5 cm)","Health insurance enrollment"] },
      work: { fee: "JPY 3,000 (~$20)", processing: "1-3 months (COE processing)", steps: ["Receive job offer from Japanese company","Employer applies for Certificate of Eligibility (COE) at Immigration Bureau","Apply for work visa at Japanese embassy with COE","Enter Japan and complete residence registration","Obtain residence card and register at local ward office"], documents: ["Certificate of Eligibility (COE)","Job offer or employment contract","Degree certificate matching job category","Passport valid for duration of employment","Passport-sized photos","Resume/CV"] },
      retirement: { fee: "N/A", processing: "N/A", steps: ["Japan has no retirement visa - research alternative visa categories","Consider Investor visa (5 million yen investment in business)","Explore Spouse visa if married to a Japanese national","Consider Designated Activities visa for specific circumstances","Consult with an immigration lawyer for best pathway"], documents: ["Varies by visa category chosen","No specific retirement visa documents"] },
      digital_nomad: { fee: "JPY 3,000 (~$20)", processing: "1-2 months", steps: ["Verify your income meets 10 million yen/year minimum (~$70,000)","Obtain private health insurance with coverage in Japan","Apply for Digital Nomad Visa at Japanese embassy in your country","Enter Japan with your 6-month visa (single entry, non-renewable)","Register your address at local ward office within 14 days"], documents: ["Proof of income minimum 10 million yen/year","Private health insurance valid in Japan","Employment contract with non-Japanese company","Passport valid for at least 6 months","Passport-sized photos","Tax payment certificate from home country"] }
    },
    "usa": {
      tourism: { fee: "$21 (ESTA) / $185 (B1/B2 visa)", processing: "Instant-72h (ESTA) / 2-8 weeks (B visa)", steps: ["Determine if you qualify for ESTA (Visa Waiver Program) or need a B1/B2 visa","For ESTA: apply online at esta.cbp.dhs.gov at least 72 hours before travel","For B visa: complete DS-160 form online and schedule embassy interview","Attend visa interview with all required documents","Upon approval, enter the US and go through CBP inspection"], documents: ["Passport valid for 6 months beyond intended stay","ESTA approval or B1/B2 visa","Proof of ties to home country (job, property, family)","Proof of sufficient funds","Return flight ticket","Hotel or accommodation booking"] },
      student: { fee: "$185 (visa) + $350 (SEVIS fee)", processing: "3-8 weeks", steps: ["Receive acceptance and Form I-20 from SEVP-certified school","Pay SEVIS fee ($350) at fmjfee.com","Complete DS-160 visa application online","Schedule and attend visa interview at US embassy","Arrive in US no more than 30 days before program start date"], documents: ["Form I-20 from SEVP-certified institution","SEVIS fee payment receipt ($350)","Passport valid for 6 months beyond stay","Financial proof for at least 1 year of expenses","Academic transcripts and test scores","Passport-sized photo (2x2 inches)"] },
      work: { fee: "$460-$780 (filing) + $190 (visa)", processing: "2-6 months (H-1B lottery in April)", steps: ["Employer submits H-1B petition to USCIS (April lottery)","If selected, USCIS processes the petition","Upon approval, apply for H-1B visa at US embassy","Attend visa interview with petition approval notice","Enter the US with H-1B status valid for 3 years"], documents: ["H-1B petition approval notice (I-797)","Passport valid for 6 months beyond stay","Bachelor's degree or higher in specialty occupation","Employer's Labor Condition Application","Completed DS-160 form","Passport-sized photos"] },
      retirement: { fee: "N/A", processing: "N/A", steps: ["USA has no retirement visa - research alternative pathways","Consider EB-5 Investor visa ($800,000+ investment in targeted employment area)","Explore Green Card Diversity Lottery if from eligible country","Consider family-based sponsorship if you have US citizen relatives","Consult immigration attorney for best available option"], documents: ["Varies by visa category chosen","No specific retirement visa documents"] },
      digital_nomad: { fee: "N/A", processing: "N/A", steps: ["USA has no digital nomad visa program","Use ESTA (90 days) or B1/B2 tourist visa (up to 6 months)","Note: you cannot earn US-source income without work authorization","Consider O-1 visa if you have extraordinary ability in your field","Remote work for foreign employer while on tourist status is a grey area"], documents: ["Standard tourist visa documents apply","No specific digital nomad visa documents"] }
    },
    "mexico": {
      tourism: { fee: "Free (FMM at entry) / $575 MXN (air arrival)", processing: "Instant at entry", steps: ["Check if your nationality is visa-exempt for Mexico","FMM tourist card is auto-issued at entry for exempt nationalities","Complete immigration form on arrival or online via INM","Present passport and FMM at immigration checkpoint","Receive up to 180-day entry stamp"], documents: ["Passport valid for duration of stay","Return or onward flight ticket","Proof of funds (~$1,620/month or hotel booking)","Completed FMM form (provided at entry or online)"] },
      student: { fee: "$50-$100 USD", processing: "10-15 business days", steps: ["Obtain acceptance from a Mexican university or school","Apply for Temporary Resident visa (student) at Mexican consulate","Prepare financial proof and other required documents","Attend consulate appointment and pay visa fee","Enter Mexico and exchange visa for Temporary Resident Card at INM within 30 days"], documents: ["University acceptance letter","Passport valid for duration of studies","Proof of financial means","Health insurance","Background check certificate","Passport-sized photos"] },
      work: { fee: "$50-$100 USD (visa) + employer fees", processing: "15-30 business days", steps: ["Secure job offer from Mexican employer","Employer applies for work authorization at INM in Mexico","Once approved, apply for Temporary Resident visa at Mexican consulate","Enter Mexico and exchange visa for Temporary Resident Card within 30 days","Register for RFC tax number at SAT"], documents: ["Job offer letter from Mexican company","Employer's INM authorization","Passport valid for duration of contract","Proof of qualifications","Passport-sized photos","Background check certificate"] },
      retirement: { fee: "$50-$100 USD", processing: "10-15 business days", steps: ["Verify you meet income requirements ($3,000/month or $100,000 savings)","Apply for Temporary Resident visa at Mexican consulate","Provide 12 months of bank statements showing income or savings","Enter Mexico and exchange visa for Temporary Resident Card at INM","After 4 years, apply for Permanent Residency (no income proof needed)"], documents: ["12 months bank statements showing $3,000+/month income or $100,000+ savings","Passport valid for duration of stay","Background check certificate","Passport-sized photos","Proof of accommodation in Mexico"] },
      digital_nomad: { fee: "Free (tourist FMM)", processing: "Instant at entry", steps: ["Enter Mexico as a tourist with FMM card (180 days)","No formal digital nomad visa exists - use tourist entry","Remote work for foreign companies is tolerated","Leave and re-enter for a new 180-day period if needed","Consider Temporary Resident visa for stays beyond 180 days"], documents: ["Passport valid for duration of stay","Return or onward flight ticket","Proof of funds","No specific digital nomad documentation required"] }
    }
  };

  // Apply generic extra data for countries without specific EXTRA entries
  function getExtra(dest, purpose) {
    if (EXTRA[dest] && EXTRA[dest][purpose]) return EXTRA[dest][purpose];
    // Generate reasonable defaults from the base data
    var info = D[dest] && D[dest][purpose];
    if (!info) return null;
    var isVisaFree = /visa.?free|visa.?exempt|visa on arrival|eVisa|ESTA|eTA|FMM/i.test(info[0]);
    return {
      fee: isVisaFree ? "Free / Low cost" : "Varies by nationality",
      processing: isVisaFree ? "Instant to 72 hours" : "5-15 business days",
      steps: [
        "Check visa requirements for your nationality on the official immigration website",
        "Prepare all required documents including valid passport and supporting materials",
        "Apply for visa at embassy/consulate or online if e-visa is available",
        "Wait for processing and approval",
        "Enter the country and comply with visa conditions"
      ],
      documents: info[4] ? info[4].split(", ").map(function(d) { return d.trim(); }) : ["Valid passport", "Proof of funds", "Return ticket"]
    };
  }

  // ── Render result page ──
  var guideCountries = ["thailand","portugal","spain","mexico","vietnam","malaysia","japan","uae","colombia","panama","costa-rica","greece","georgia","paraguay","laos","cambodia"];

  function renderResultPage() {
    var container = document.getElementById("visa-result-container");
    if (!container) return;
    // Only run on visa-result.html
    if (window.location.pathname.indexOf("visa-result") === -1) return;

    var lang = getLang();
    var L = LABELS[lang] || LABELS.en;
    var cn = COUNTRY_NAMES[lang] || {};

    var params = new URLSearchParams(window.location.search);
    var nat = params.get("nat");
    var dest = params.get("dest");
    var purpose = params.get("purpose");

    if (!nat || !dest || !purpose) {
      container.innerHTML = '<div class="vr-container"><div class="vr-error"><h2>' + (L.select_all || "Please select all three fields.") + '</h2><p><a href="/" class="btn btn-primary">' + (L.search_again || "Search Again") + '</a></p></div></div>';
      return;
    }

    var countryData = D[dest];
    if (!countryData || !countryData[purpose]) {
      container.innerHTML = '<div class="vr-container"><div class="vr-error"><h2>' + (L.no_data || "No data available.") + '</h2><p><a href="/" class="btn btn-primary">' + (L.search_again || "Search Again") + '</a></p></div></div>';
      return;
    }

    var info = countryData[purpose];
    var extra = getExtra(dest, purpose);
    var destObj = DESTINATIONS.find(function(d) { return d.s === dest; });
    var destName = cn[dest] || (destObj ? destObj.n : dest);
    var destFlag = destObj ? destObj.f : "";

    var purposeLabel = L[purpose] || purpose;

    var hasCombo = COMBOS[dest + "|" + nat];
    var visaLink = hasCombo
      ? "/" + lang + "/" + dest + "-visa-for-" + nat + "-citizens.html"
      : "/" + lang + "/visa-" + dest + ".html";

    var hasGuide = guideCountries.indexOf(dest) !== -1;
    var guideLink = "/" + lang + "/expat-guide-" + dest + ".html";

    // Build steps HTML
    var stepsHtml = "";
    if (extra && extra.steps) {
      stepsHtml = '<ol class="vr-steps">';
      extra.steps.forEach(function(step) {
        stepsHtml += '<li>' + step + '</li>';
      });
      stepsHtml += '</ol>';
    }

    // Build documents HTML
    var docsHtml = "";
    if (extra && extra.documents) {
      docsHtml = '<ul class="vr-docs">';
      extra.documents.forEach(function(doc) {
        docsHtml += '<li>' + doc + '</li>';
      });
      docsHtml += '</ul>';
    }

    var html = '<div class="vr-container">' +
      '<div class="vr-header">' +
        '<span class="fi fi-' + destFlag + ' vr-flag"></span>' +
        '<div style="flex:1;">' +
          '<h1 class="vr-title">' + destName + ' \u2014 ' + purposeLabel + ' ' + L.visa_for + '</h1>' +
          '<p class="vr-subtitle">' + info[0] + '</p>' +
        '</div>' +
        '<div class="vr-badge-row">' +
          '<div class="vr-badge">' +
            '<div class="vr-badge-label">' + L.duration + '</div>' +
            '<div class="vr-badge-value">' + info[1] + '</div>' +
          '</div>' +
          (extra ? '<div class="vr-badge">' +
            '<div class="vr-badge-label">' + L.fee + '</div>' +
            '<div class="vr-badge-value" style="font-size:16px;">' + extra.fee + '</div>' +
          '</div>' : '') +
        '</div>' +
      '</div>' +
      '<div class="vr-body">' +
        (extra && extra.processing ? '<div class="vr-section"><div class="vr-fee-row">' +
          '<div class="vr-fee-item"><div class="vr-fee-label">' + L.processing + '</div><div class="vr-fee-value">' + extra.processing + '</div></div>' +
          '<div class="vr-fee-item"><div class="vr-fee-label">' + L.fee + '</div><div class="vr-fee-value">' + extra.fee + '</div></div>' +
        '</div></div>' : '') +
        (stepsHtml ? '<div class="vr-section"><div class="vr-section-title"><span class="vr-section-icon">&#9989;</span> ' + L.steps_title + '</div>' + stepsHtml + '</div>' : '') +
        (docsHtml ? '<div class="vr-section"><div class="vr-section-title"><span class="vr-section-icon">&#128203;</span> ' + L.docs_title + '</div>' + docsHtml + '</div>' : '') +
        '<div class="vr-section vr-warning"><div class="vr-section-title"><span class="vr-section-icon">&#9888;&#65039;</span> ' + L.penalty_title + '</div><p>' + info[2] + '</p></div>' +
        '<div class="vr-section vr-info"><div class="vr-section-title"><span class="vr-section-icon">&#128260;</span> ' + L.strategy_title + '</div><p>' + info[3] + '</p></div>' +
        '<div class="vr-section"><div class="vr-section-title"><span class="vr-section-icon">&#128196;</span> ' + L.requirements + '</div><p style="color:#374151;font-size:14px;line-height:1.6;margin:0;">' + info[4] + '</p></div>' +
        '<div class="vr-actions">' +
          '<a href="' + visaLink + '" class="btn btn-primary">' + L.details + ' &rarr;</a>' +
          (hasGuide ? '<a href="' + guideLink + '" class="btn btn-secondary">' + L.guide + ' &rarr;</a>' : '') +
          '<a href="/" class="btn btn-outline">' + L.search_again + '</a>' +
        '</div>' +
      '</div>' +
    '</div>';

    container.innerHTML = html;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function() { init(); renderResultPage(); });
  } else {
    init();
    renderResultPage();
  }
})();
