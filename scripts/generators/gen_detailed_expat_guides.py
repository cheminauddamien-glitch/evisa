#!/usr/bin/env python3
"""
Generate detailed expat guide pages per country.
Sections: Visa/Residency, Healthcare, Supplementary Insurance, Bank Account, Real Estate
"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"
BASE = "https://www.evisa-card.com"

COUNTRIES = {
    "thailand": {
        "name": "Thailand",
        "flag_code": "th",
        "flag_emoji": "🇹🇭",
        "hero_bg": "https://flagcdn.com/w1280/th.png",
        "capital": "Bangkok",
        "currency": "Thai Baht (THB)",
        "language": "Thai",
        "cost": "~$800–1,500/month",
        "title": "Complete Expat Guide Thailand 2026 — Live, Work & Retire in Thailand",
        "meta": "Complete guide to living in Thailand as an expat in 2026. Visa options, residency, healthcare, supplementary insurance, bank accounts and property buying for foreigners.",
        "intro": "Thailand remains one of the world's most popular expat destinations, offering warm weather, affordable living, world-class cuisine and welcoming visa options for retirees, remote workers and families.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Retirement Visa (Non-OA)", "For expats 50+. Requires proof of 800,000 THB in a Thai bank account OR 65,000 THB/month income. Valid 1 year, renewable. Allows multiple entries."),
                ("LTR Visa (Long-Term Resident)", "For remote workers earning $80,000+/year. Valid 10 years. Allows working for overseas employers without a Thai work permit. Fast-track immigration."),
                ("Thailand Elite Visa", "Membership programme (500,000–2,000,000 THB). 5–20 year stay, VIP airport service. No income requirement. Purely residence-based."),
                ("Non-Immigrant B (Business)", "Required if working for a Thai company. Must be accompanied by a Thai Work Permit. Annual renewal."),
                ("Tourist Visa / Visa Exempt", "60 days (Tourist) or 30 days (visa-exempt). Can extend once at immigration. Many expats use border runs — now strictly monitored."),
            ],
            "steps": [
                "Determine your visa category (retirement, LTR, Elite or business)",
                "Gather documents: passport (6+ months), photos, bank statements, health insurance, medical certificate",
                "Apply at the nearest Thai embassy or consulate in your home country",
                "Upon arrival, file TM.30 address notification within 24 hours",
                "Open a Thai bank account (required for retirement visa deposit)",
                "Report every 90 days at the Immigration Bureau (online, by post or in person)",
                "Renew annually at your local Immigration office",
            ],
            "tip": "The LTR Visa is the best option for remote workers — 10 years, no 90-day reports, and it exempts certain income from Thai tax.",
        },
        "health": {
            "heading": "Healthcare in Thailand",
            "public": "Thailand's public healthcare system (30-Baht Scheme) is available to Thai nationals and permanent residents only. As a non-resident expat, you cannot access public healthcare at subsidised rates.",
            "private": "Private hospitals in Thailand (Bangkok Hospital, Bumrungrad, Samitivej) are world-class and significantly cheaper than Western equivalents. A consultation costs 500–1,500 THB (~$14–42). Major surgery is 60–80% cheaper than in the US or Europe.",
            "costs": [
                ("GP consultation (private)", "500–1,200 THB (~$14–34)"),
                ("Specialist consultation", "1,200–3,000 THB (~$34–85)"),
                ("Emergency room visit", "2,000–8,000 THB (~$57–228)"),
                ("Hospitalisation (per night)", "5,000–25,000 THB (~$143–714)"),
                ("Dental cleaning", "800–1,500 THB (~$23–43)"),
                ("Eye exam + glasses", "2,000–5,000 THB (~$57–143)"),
            ],
            "recommended": "Most visa types (including LTR and Retirement OA) require proof of health insurance with minimum 40,000 THB outpatient / 400,000 THB inpatient coverage.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "International health insurance is mandatory for retirement and LTR visas. Even on other visas, it is strongly recommended. Thai private hospitals can be expensive for major procedures, and repatriation costs without insurance can exceed $50,000.",
            "providers": [
                ("Pacific Cross Thailand", "Local insurer specialising in expats in Southeast Asia. Plans from ~$800/year. Good network of Thai private hospitals."),
                ("BUPA Thailand", "Strong regional network. Plans from ~$1,000/year. Well-regarded for cancer coverage."),
                ("AXA / AXA Global Healthcare", "International coverage, ideal if you travel frequently or split time between countries. From ~$1,500/year."),
                ("Cigna Global", "Comprehensive plans with worldwide coverage. Particularly suited for high earners on LTR visas. From ~$1,800/year."),
                ("Allianz Care", "Flexible modular plans. Can add dental, optical and maternity. From ~$1,200/year."),
            ],
            "tip": "For the Retirement OA visa, your policy must be issued by a Thai-licensed insurer and must specifically state 40,000 / 400,000 THB minimum coverage. Pacific Cross and BUPA are the easiest to use for this purpose.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Thailand",
            "intro": "A Thai bank account is practically essential for expats — it's required for the retirement visa deposit (800,000 THB), utility payments, rent transfers and daily transactions.",
            "banks": [
                ("Kasikorn Bank (KBank)", "Most expat-friendly bank. English-language app and staff in main branches. Fixed deposit accounts accepted for visa purposes."),
                ("Bangkok Bank", "Largest bank in Thailand. Strong international wire support. Commonly used for pension/income transfers."),
                ("SCB (Siam Commercial Bank)", "Good English-language online banking. Competitive FX rates."),
                ("Krungsri (Bank of Ayudhya)", "Easier account opening in some provinces. Partners with Mitsubishi UFJ."),
            ],
            "requirements": [
                "Valid passport",
                "Non-Immigrant visa (tourist visa may be refused at some branches)",
                "Proof of address in Thailand (rental contract or TM.30 confirmation)",
                "Thai SIM card or phone number",
                "Initial deposit (typically 500–2,000 THB)",
            ],
            "process": [
                "Visit the bank branch in person (online opening not available for foreigners)",
                "Request a savings account (บัญชีออมทรัพย์)",
                "Present all documents to the bank officer",
                "Receive debit card same day or within 5 business days",
                "Activate online/mobile banking (may require Thai phone number)",
            ],
            "tip": "Kasikorn Bank's Asoke (Bangkok) or Nimman (Chiang Mai) branches are known for being particularly helpful to expats. Arrive early — queues can be long.",
        },
        "realestate": {
            "heading": "Buying Property in Thailand",
            "intro": "Foreigners cannot own land in Thailand, but they can own condominium units freehold (up to 49% of a building's total floor area may be foreign-owned). Houses and land must be held through a Thai company, a 30-year leasehold or a Thai spouse.",
            "options": [
                ("Condominium (freehold)", "Full ownership permitted for foreigners. Must be paid from overseas in foreign currency (proof required). Most popular option."),
                ("30-year Leasehold", "Land and houses can be leased for 30 years, renewable twice (total 90 years in practice). Common for villas and townhouses."),
                ("Thai Company Structure", "A Thai limited company (min. 51% Thai shareholders) can hold land. Complex, legal fees $2,000–5,000. Requires ongoing compliance."),
                ("Thai Spouse", "Land can be registered in a Thai spouse's name. No legal protection in case of divorce. Not recommended."),
            ],
            "process": [
                "Hire a reputable real estate lawyer (budget 30,000–80,000 THB)",
                "Verify the title deed (Chanote / Nor Sor 4 — the only fully secure title)",
                "Sign a Reservation Agreement and pay deposit (50,000–100,000 THB)",
                "Due diligence: check no liens, correct zoning, building permits",
                "Transfer funds from overseas bank to Thailand (keep FET form for proof)",
                "Sign Sale & Purchase Agreement (SPA)",
                "Transfer at the Land Office — both parties must attend",
                "Pay transfer fees (typically 2–3% of assessed value)",
            ],
            "costs": [
                ("Transfer fee", "2% of the appraised value (split buyer/seller)"),
                ("Stamp duty or specific business tax", "0.5% stamp duty OR 3.3% SBT if sold within 5 years"),
                ("Withholding tax", "1–3% (paid by seller)"),
                ("Lawyer fees", "30,000–80,000 THB"),
                ("Agent commission", "3–5% (paid by seller)"),
            ],
            "tip": "Always use a Chanote (NS4J) title deed. Avoid Nor Sor 3 or Sor Kor 1 titles — they offer less legal protection and cannot be mortgaged.",
        },
    },
    "portugal": {
        "name": "Portugal",
        "flag_code": "pt",
        "flag_emoji": "🇵🇹",
        "hero_bg": "https://flagcdn.com/w1280/pt.png",
        "capital": "Lisbon",
        "currency": "Euro (€)",
        "language": "Portuguese",
        "cost": "~$1,500–2,500/month",
        "title": "Complete Expat Guide Portugal 2026 — Live, Work & Retire in Portugal",
        "meta": "Complete guide to living in Portugal as an expat in 2026. D7 visa, Golden Visa, NHR tax status, healthcare, health insurance, bank accounts and property buying for foreigners.",
        "intro": "Portugal consistently ranks as one of the best countries for expats — EU membership, mild climate, low crime, excellent healthcare and a growing expat community make it a top destination for retirees, remote workers and families.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("D7 Passive Income Visa", "For retirees and people with passive income (pension, rental, investments). Minimum income ~€760/month (minimum wage). Apply at Portuguese consulate. 2-year initial residence permit, renewable."),
                ("Digital Nomad Visa (D8)", "For remote workers with foreign employers. Minimum income 4× Portuguese minimum wage (~€3,040/month). 1-year initial stay, renewable."),
                ("Golden Visa (ARI)", "Investment-based residency. Currently: funds investment €500,000+, cultural donation €250,000+. Real estate routes closed since 2023. 2-year permit with path to citizenship in 5 years."),
                ("D2 Entrepreneur Visa", "For business owners and entrepreneurs. Requires business plan and proof of funds. Path to permanent residency."),
                ("EU Citizen", "EU/EEA/Swiss citizens register at the local Câmara Municipal within 3 months. Free, no investment required."),
            ],
            "steps": [
                "Apply for the appropriate visa at your local Portuguese consulate",
                "Obtain a NIF (tax number) — can be done remotely via a fiscal representative",
                "Open a Portuguese bank account (required for visa purposes)",
                "Arrive in Portugal and register your address",
                "Schedule appointment at AIMA (Immigration Authority, formerly SEF) for residence permit",
                "Obtain your residence card (Título de Residência) — valid 2 years",
                "Apply for NHR tax status within the first year (if applicable)",
                "Renew permit every 2 years; apply for permanent residency after 5 years",
            ],
            "tip": "Apply for NHR (Non-Habitual Resident) tax status in your first year — it provides a flat 20% income tax rate on Portuguese-source income and 0% on most foreign-source income for 10 years.",
        },
        "health": {
            "heading": "Healthcare in Portugal",
            "public": "Portugal has the SNS (Serviço Nacional de Saúde) — a universal public health system. Legal residents with a SNS number can access public healthcare for free or at very low cost (€5–20 co-payment per consultation).",
            "private": "Private clinics and hospitals (CUF, Luz Saúde, HPA Health Group in the Algarve) offer shorter waiting times and English-speaking doctors. Consultations cost €60–150.",
            "costs": [
                ("SNS GP consultation (residents)", "Free (with SNS user number)"),
                ("SNS specialist consultation", "€7.50 co-payment"),
                ("Private GP consultation", "€60–100"),
                ("Private specialist", "€80–200"),
                ("Emergency (SNS)", "€20.60 co-payment"),
                ("Prescription medicines", "Partially subsidised (15–95% depending on medication)"),
            ],
            "recommended": "Register at your local health centre (Centro de Saúde) within the first months to get a SNS user number. This gives access to the full public health system.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "While public healthcare is excellent for residents, wait times can be long for non-urgent care. A supplementary private health insurance plan gives faster access to private hospitals and specialists, and is required for D7/D8 visa applications.",
            "providers": [
                ("Médis (BCP Group)", "Portugal's largest private health insurer. Strong network of private hospitals and clinics. Plans from ~€80/month."),
                ("Fidelidade Saúde", "Comprehensive plans with dental included. Partners with CUF network. From ~€70/month."),
                ("Multicare (Fidelidade)", "Popular expat-friendly plans with English support. From ~€60/month."),
                ("Cigna Global", "International plan ideal for new arrivals awaiting SNS registration. Worldwide coverage. From ~€130/month."),
                ("AXA Global Healthcare", "Flexible international plans. Useful if you travel frequently outside Portugal. From ~€120/month."),
            ],
            "tip": "For D7 visa applications, you need proof of health insurance before arriving. Cigna or AXA Global Healthcare are easiest to obtain from abroad. Once resident, you can switch to a Portuguese plan like Médis which offers better value.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Portugal",
            "intro": "A Portuguese bank account is required for the D7 and D8 visa applications, and essential for receiving transfers, paying rent, utilities and taxes.",
            "banks": [
                ("Millennium BCP", "Largest private bank. Good English support, strong online banking. Popular with expats."),
                ("Novo Banco", "Strong international transfer capabilities. English-speaking staff in Lisbon/Porto/Algarve."),
                ("Caixa Geral de Depósitos", "State-owned bank. Extensive branch network, competitive fees."),
                ("N26 / Revolut (non-resident)", "Digital banks accepted for day-to-day use but NOT accepted for visa applications. Use as secondary accounts only."),
                ("Activobank", "Online bank by Millennium BCP. Easy account opening, low fees. Good for tech-savvy expats."),
            ],
            "requirements": [
                "Valid passport",
                "NIF (Portuguese tax number) — mandatory",
                "Proof of address (utility bill, rental contract)",
                "Proof of income or funds",
                "Portuguese phone number (for 2FA)",
            ],
            "process": [
                "Obtain your NIF first — visit a Finanças office or use an online fiscal representative service (~€150–300)",
                "Book an appointment at the bank branch",
                "Present all documents and complete the bank's KYC form",
                "Account opened same day in most cases",
                "Online/mobile banking activated within 2–5 days",
            ],
            "tip": "You can obtain a NIF remotely before arriving in Portugal by appointing a fiscal representative (costs ~€150–300). This allows you to open a bank account and apply for your visa while still abroad.",
        },
        "realestate": {
            "heading": "Buying Property in Portugal",
            "intro": "Portugal has no restrictions on foreigners buying property. The process is transparent and well-regulated. The real estate market has grown significantly, with Lisbon and Porto being the most expensive markets.",
            "options": [
                ("Freehold Purchase", "Full ownership. No restrictions for foreigners. Most common method."),
                ("Golden Visa (Funds route)", "Investment in qualified funds ≥€500,000 or cultural heritage ≥€250,000. Real estate routes closed since Oct 2023."),
                ("Usufruct", "Right to use a property for life while another person holds the bare ownership. Common in inheritance situations."),
            ],
            "process": [
                "Obtain a NIF (tax number) — mandatory for property purchase",
                "Hire a Portuguese solicitor (advogado) — budget €2,000–5,000",
                "Sign the Promissory Purchase Contract (CPCV) and pay 10–30% deposit",
                "Solicitor conducts due diligence: title search, encumbrances, planning permissions",
                "Arrange finance (Portuguese mortgage or international transfer)",
                "Sign the final Deed (Escritura) at a Notary — both parties attend",
                "Register property at the Land Registry (Conservatória do Registo Predial)",
                "Register at the Tax Authority (Autoridade Tributária)",
            ],
            "costs": [
                ("IMT (property transfer tax)", "0–8% depending on value (graduated scale; primary residence exempt up to €97,064)"),
                ("Stamp duty (IS)", "0.8% of purchase price"),
                ("Notary and registration", "€1,000–2,500"),
                ("Solicitor fees", "1–2% of purchase price"),
                ("Estate agent commission", "3–5% (paid by seller)"),
                ("Annual property tax (IMI)", "0.3–0.45% of taxable value per year"),
            ],
            "tip": "For properties over €1M, stamp duty increases to 6%. Always use a local solicitor — they will check the Caderneta Predial, the Certidão de Teor and all encumbrances before you commit.",
        },
    },
    "spain": {
        "name": "Spain",
        "flag_code": "es",
        "flag_emoji": "🇪🇸",
        "hero_bg": "https://flagcdn.com/w1280/es.png",
        "capital": "Madrid",
        "currency": "Euro (€)",
        "language": "Spanish",
        "cost": "~$1,500–2,800/month",
        "title": "Complete Expat Guide Spain 2026 — Live, Work & Retire in Spain",
        "meta": "Complete guide to living in Spain as an expat in 2026. Non-lucrative visa, digital nomad visa, healthcare, health insurance, bank accounts and property buying for foreigners.",
        "intro": "Spain offers year-round sunshine, rich culture, excellent food and one of Europe's best healthcare systems. With the Non-Lucrative Visa, Digital Nomad Visa and Golden Visa, Spain has become a top destination for expats from around the world.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Non-Lucrative Visa (NLV)", "For retirees and those with passive income. Must prove €2,400/month (€600 per additional family member). Cannot work in Spain. 1-year permit, renewable for 2-year periods."),
                ("Digital Nomad Visa (DNV)", "For remote workers with non-Spanish clients. Minimum income €2,646/month. Work permit included. 1-year permit renewable for 3 years, then long-term residence."),
                ("Golden Visa", "Investment residency: real estate €500,000+, business investment €1M+, government bonds €2M+. No minimum stay requirement. 2-year renewable permit."),
                ("Beckham Law (Impatriate Regime)", "Flat 24% income tax on Spanish-source income for 6 years. For employees relocated to Spain or DNV holders. Apply within 6 months of arrival."),
                ("EU Citizen", "Register at the local Town Hall (Padrón) and obtain a NIE (foreigners tax number). Free, immediate residence rights."),
            ],
            "steps": [
                "Apply for your visa at the Spanish consulate in your country",
                "Obtain a NIE (Número de Identificación de Extranjero) — required for all legal and financial transactions",
                "Register on the Padrón (municipal census) at your local Town Hall",
                "Obtain private health insurance (required for NLV)",
                "Apply for TIE (Tarjeta de Identidad de Extranjero) residence card at the Oficina de Extranjería",
                "Register with the Seguridad Social if working",
                "Consider applying for Beckham Law within 6 months if eligible",
            ],
            "tip": "The Non-Lucrative Visa requires you NOT to work in Spain, but you can receive income from foreign sources (pensions, investments, remote work for non-Spanish companies if done discreetly — grey area). The Digital Nomad Visa is cleaner if you're working remotely.",
        },
        "health": {
            "heading": "Healthcare in Spain",
            "public": "Spain's public healthcare system (Sistema Nacional de Salud, SNS) is one of the best in the world. Legal residents registered on the Padrón and contributing to Social Security can access it for free. Retired expats with an S1 form from their home country (EU citizens) also qualify.",
            "private": "Private healthcare is excellent and affordable by international standards. Major networks: Sanitas, Adeslas, Asisa, HM Hospitales. Consultations cost €40–100.",
            "costs": [
                ("Public healthcare (residents)", "Free (with Social Security or S1 form)"),
                ("Private GP", "€40–80"),
                ("Private specialist", "€80–150"),
                ("Dental cleaning (private)", "€50–80"),
                ("Prescription medicines", "Subsidised for residents (0–40% co-payment)"),
                ("Private hospital (per night)", "€300–800"),
            ],
            "recommended": "For NLV applicants: private health insurance with at least €30,000 coverage is required for the visa. Even after obtaining residency, many expats keep private insurance for faster service.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "Private health insurance is compulsory for Non-Lucrative and Digital Nomad visa applications. Even for residents with access to the public system, private coverage provides faster appointments and English-speaking doctors.",
            "providers": [
                ("Sanitas", "Spain's largest private insurer (owned by Bupa). Excellent network, English-language service, strong app. Accepted for NLV. From ~€70/month."),
                ("Adeslas (SegurCaixa)", "Broad network across Spain. Dental plans available. Popular with expats. From ~€65/month."),
                ("Asisa", "Strong in Madrid and Catalonia. Good value plans. From ~€60/month."),
                ("Cigna Global", "International plan, ideal for new arrivals. Worldwide coverage. From ~€130/month."),
                ("AXA Spain", "Local AXA plans with solid network. Dental add-on available. From ~€75/month."),
            ],
            "tip": "For visa purposes, Sanitas and Adeslas are most commonly accepted by Spanish consulates. Make sure your policy is comprehensive (no exclusions for pre-existing conditions at the consulate stage) and has no co-payments (some consulates require this).",
        },
        "bank": {
            "heading": "Opening a Bank Account in Spain",
            "intro": "A Spanish bank account is needed to pay rent, utilities, taxes and to meet visa financial proof requirements. Most banks require a NIE (tax number) and proof of address.",
            "banks": [
                ("Sabadell", "Expat-friendly with English service. Branches in Alicante, Barcelona, Málaga. No-fee accounts available."),
                ("BBVA", "Major bank, strong digital platform. Easy account opening with NIE. Competitive FX rates."),
                ("Santander", "Largest bank, extensive branch network. Good for international transfers."),
                ("CaixaBank", "Largest bank by customers. Good mobile app. Some branches have dedicated expat advisors."),
                ("N26 / Wise (non-resident)", "Usable while awaiting NIE but not accepted for visa applications. Good for initial period."),
            ],
            "requirements": [
                "Valid passport",
                "NIE (mandatory) or EU ID",
                "Padrón certificate (proof of address registration)",
                "Spanish phone number",
                "Proof of income or funds",
            ],
            "process": [
                "Obtain your NIE first — at the Oficina de Extranjería or at your Spanish consulate abroad",
                "Register on the Padrón at your Town Hall",
                "Book a bank appointment online",
                "Present all documents; open account same day",
                "Activate online banking (requires Spanish phone number)",
            ],
            "tip": "Sabadell in coastal areas (Alicante, Costa del Sol) has dedicated expat services in English. If you're moving to Madrid or Barcelona, BBVA and CaixaBank have the best digital banking experience.",
        },
        "realestate": {
            "heading": "Buying Property in Spain",
            "intro": "Foreigners can freely buy property in Spain with no restrictions. Spain is one of the most transparent real estate markets in the EU. Prices vary enormously: from €1,000/m² in rural areas to €6,000+/m² in prime Madrid and Barcelona.",
            "options": [
                ("Freehold Purchase", "Full ownership, no restrictions for foreigners. Most common."),
                ("Golden Visa", "Purchase property ≥€500,000 to qualify for Golden Visa residency."),
                ("Off-Plan Purchase", "Buying directly from developers before completion. Lower prices but construction risk."),
            ],
            "process": [
                "Obtain a NIE (mandatory for property purchase)",
                "Hire a Spanish solicitor (abogado) — non-negotiable recommendation",
                "Sign a Reservation Contract (Contrato de Reserva) and pay €3,000–10,000 deposit",
                "Sign the Private Purchase Contract (Contrato de Arras) and pay 10% deposit",
                "Solicitor conducts due diligence: nota simple, building permits, community debts",
                "Arrange finance or international transfer",
                "Sign the Deed (Escritura) before a Notary",
                "Register property at the Property Registry (Registro de la Propiedad)",
            ],
            "costs": [
                ("Transfer tax (ITP) or VAT", "6–10% ITP (resale) OR 10% VAT (new build) + 1.5% stamp duty"),
                ("Notary fees", "0.5–1% of purchase price"),
                ("Land Registry fees", "0.2–0.5%"),
                ("Solicitor fees", "1–2% of purchase price"),
                ("Annual property tax (IBI)", "0.3–1.3% of cadastral value"),
                ("Community fees", "€50–500/month depending on urbanisation"),
            ],
            "tip": "Always obtain a Nota Simple from the Property Registry before signing anything — it confirms ownership, any mortgages and encumbrances on the property. Cost: ~€10.",
        },
    },
    "mexico": {
        "name": "Mexico",
        "flag_code": "mx",
        "flag_emoji": "🇲🇽",
        "hero_bg": "https://flagcdn.com/w1280/mx.png",
        "capital": "Mexico City",
        "currency": "Mexican Peso (MXN)",
        "language": "Spanish",
        "cost": "~$1,000–2,000/month",
        "title": "Complete Expat Guide Mexico 2026 — Live, Work & Retire in Mexico",
        "meta": "Complete guide to living in Mexico as an expat in 2026. Temporary and permanent residency, IMSS healthcare, health insurance, bank accounts and property for foreigners.",
        "intro": "Mexico offers stunning diversity — from the cosmopolitan energy of Mexico City to the beaches of Tulum and the colonial charm of Oaxaca. Affordable living, warm weather and straightforward residency make it a top expat destination in Latin America.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Temporary Resident Visa (Residente Temporal)", "For stays of 1–4 years. Income requirement: ~$1,620/month average over the past 6 months (or ~$27,000 in savings). Issued initially for 1 year, renewable up to 4 years. Allows work with appropriate permit."),
                ("Permanent Resident Visa (Residente Permanente)", "For long-term stays. Requires higher income (~$2,700/month) or 4 years as Temporary Resident. No renewal — permanent. Best option for retirees."),
                ("Digital Nomad Visa (Residente Temporal)", "Mexico doesn't have a specific DNV but Temporary Resident with income proof from abroad is widely used. Many nomads also use tourist entry (180 days) repeatedly."),
                ("Retiree / Pensionado", "Via Temporary or Permanent Resident route with pension income proof. No special retiree visa category exists but income threshold is achievable with most pensions."),
                ("Tourist Entry", "180 days. No income requirement. Not renewable without leaving. Widely used by short-term expats and nomads."),
            ],
            "steps": [
                "Apply at the Mexican consulate in your home country with income/savings proof",
                "Receive entry visa (valid 180 days to complete the process in Mexico)",
                "Travel to Mexico and within 30 days visit the INM (Instituto Nacional de Migración) office",
                "Submit biometrics and complete the application",
                "Receive your Tarjeta de Residente (residence card) within 10–15 business days",
                "Obtain a CURP (unique population code) — free, done at the INM or online",
                "Obtain an RFC (tax ID) at the SAT (tax authority) if working or renting",
            ],
            "tip": "Mexico City's Condesa/Roma Norte, San Miguel de Allende, Puerto Vallarta and Tulum have large expat communities with established support networks for the residency process.",
        },
        "health": {
            "heading": "Healthcare in Mexico",
            "public": "The IMSS (Mexican Social Security) is available to Temporary and Permanent Residents who are employed in Mexico or pay voluntary contributions (~$400–600/year). Quality varies significantly by region — strong in Mexico City, weaker in rural areas.",
            "private": "Private healthcare in Mexico is significantly cheaper than in the US, with high quality in major cities. Hospitals like ABC Medical Center (CDMX), Hospital San Javier (Guadalajara) and CMQ (Puerto Vallarta) serve the expat community well.",
            "costs": [
                ("IMSS voluntary membership (annual)", "~$430/year (for permanent residents)"),
                ("Private GP consultation", "400–1,200 MXN (~$24–71)"),
                ("Private specialist", "800–3,000 MXN (~$47–177)"),
                ("Emergency room (private)", "3,000–12,000 MXN (~$177–710)"),
                ("Hospitalisation (private, per night)", "5,000–20,000 MXN (~$295–1,180)"),
                ("Dental cleaning", "300–700 MXN (~$18–41)"),
            ],
            "recommended": "Most expats opt for private international health insurance rather than IMSS. IMSS is a good supplement for routine care, but private insurance is essential for hospitalisation.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "Private health insurance is not legally required in Mexico but is strongly recommended. Emergency medical costs and hospitalisation at private facilities can be very high without coverage. US expats especially should never rely on tourist status without insurance.",
            "providers": [
                ("GNP Seguros", "Mexico's largest insurer. Extensive private hospital network across Mexico. Plans from ~$800/year."),
                ("MetLife Mexico", "Good international coverage. Popular with US and Canadian expats. From ~$1,000/year."),
                ("BUPA Global / Cigna Global", "International plans with worldwide coverage including the US — essential if you travel north frequently. From ~$1,500/year."),
                ("Allianz Care", "Flexible plans, good for frequent travellers. From ~$1,200/year."),
                ("Pacific Cross", "Good value plans for Southeast Asia–Mexico corridor expats. From ~$800/year."),
            ],
            "tip": "If you plan to visit the US for medical care, make sure your plan includes US coverage — this typically doubles the premium but is essential for serious conditions.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Mexico",
            "intro": "A Mexican bank account is required for paying rent, utilities and receiving local salary. It also helps avoid currency conversion fees. The process has become stricter due to anti-money-laundering regulations.",
            "banks": [
                ("BBVA Mexico (Bancomer)", "Largest bank. English-language app, extensive ATM network. Expat-friendly in large cities."),
                ("Santander Mexico", "Good international wire capabilities. English support available."),
                ("Banamex (Citigroup)", "Strong digital platform. Good for US citizens due to Citigroup connection."),
                ("HSBC Mexico", "Best option for international transfers, particularly to/from Europe and Asia."),
                ("Nu (Nubank)", "Digital bank. Easy to open, no fees. Good for daily use. Limited to residents."),
            ],
            "requirements": [
                "Valid passport",
                "Proof of address in Mexico (utility bill or rental contract)",
                "CURP (population registry number)",
                "RFC (tax ID — required by some banks)",
                "Temporary or Permanent Resident card",
                "Initial deposit (varies by bank)",
            ],
            "process": [
                "Obtain your CURP first (free, online or at INM)",
                "Obtain RFC at the SAT office or via the SAT website",
                "Schedule appointment at bank (walk-in possible but often refused for foreigners)",
                "Present all documents",
                "Account opened within 1–3 business days",
            ],
            "tip": "BBVA Mexico and HSBC are the most expat-friendly. Avoid trying to open an account with only a tourist visa — most banks require at least a Temporary Resident card.",
        },
        "realestate": {
            "heading": "Buying Property in Mexico",
            "intro": "Foreigners can own property in Mexico, but with important restrictions in coastal and border zones (within 50km of the coast and 100km of a border). These 'restricted zones' require a bank trust (Fideicomiso) or a Mexican corporation to hold the property.",
            "options": [
                ("Freehold (unrestricted zones)", "Full foreign ownership possible in non-coastal/border areas like Mexico City, Guadalajara, San Miguel de Allende."),
                ("Fideicomiso (Bank Trust)", "Required in restricted zones (coastal/border). A Mexican bank holds the title for you as beneficiary. Cost: ~$600–800/year in bank fees. 50-year trust, renewable."),
                ("Mexican Corporation (SRL/SA)", "Alternative to Fideicomiso. Cheaper for large portfolios. Requires proper legal structuring. Not recommended for single properties."),
            ],
            "process": [
                "Obtain a RFC (tax ID)",
                "Hire a Notario Público (notary — has a specific legal role in Mexico)",
                "Hire an independent real estate lawyer (separate from the notary)",
                "Make an offer and sign a preliminary sale agreement",
                "If coastal: apply for Fideicomiso at a Mexican bank (4–6 weeks)",
                "Notary conducts title search and tax clearance",
                "Sign the Deed (Escritura) before the Notary",
                "Register at the Public Registry of Property (RPP)",
            ],
            "costs": [
                ("Acquisition tax (ISAI)", "2–4% depending on state"),
                ("Notary fees", "1–3% of purchase price"),
                ("Fideicomiso set-up", "~$1,500–2,500 one-time"),
                ("Annual Fideicomiso fee", "~$600–800/year"),
                ("Lawyer fees", "1–2%"),
                ("Annual property tax (Predial)", "Very low — typically 0.1–0.3% of assessed value"),
            ],
            "tip": "The Notario Público in Mexico is NOT the same as a notary in other countries — they are senior lawyers with quasi-judicial powers who certify the transaction. Use a reputable one. Budget 10–15% of the purchase price for all closing costs.",
        },
    },
    "vietnam": {
        "name": "Vietnam",
        "flag_code": "vn",
        "flag_emoji": "🇻🇳",
        "hero_bg": "https://flagcdn.com/w1280/vn.png",
        "capital": "Hanoi",
        "currency": "Vietnamese Dong (VND)",
        "language": "Vietnamese",
        "cost": "~$700–1,400/month",
        "title": "Complete Expat Guide Vietnam 2026 — Live, Work & Retire in Vietnam",
        "meta": "Complete guide to living in Vietnam as an expat in 2026. E-visa, residency, TRC, healthcare, health insurance, bank accounts and property for foreigners.",
        "intro": "Vietnam offers an unbeatable combination of ultra-low cost of living, delicious cuisine, dynamic cities and stunning natural scenery. Hanoi and Ho Chi Minh City have thriving expat communities, with fast internet and a growing remote worker scene.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("E-Visa (90 days)", "Available online for citizens of 80+ countries. Single or multiple entry. Maximum 90 days, not renewable without leaving. Cost: $25."),
                ("Temporary Residence Card (TRC)", "For longer stays. Requires a sponsor (employer, Vietnamese spouse or an approved organisation). 1–2 year TRC, renewable. No specific income threshold."),
                ("Business Visa (DN)", "For business activities. 3–12 months, multiple entry. Requires invitation from a Vietnamese company."),
                ("Investor / Company Director", "Foreigners who invest in or direct a Vietnamese company can obtain a TRC through the company. Minimum investment ~$130,000."),
                ("Retirement / Long-Term Stay", "Vietnam has no formal retirement visa. Most long-term expats use repeated e-visas, business visas or obtain a TRC through employment/marriage."),
            ],
            "steps": [
                "Apply for an e-visa online at the official Vietnam Immigration Portal (evisa.xuatnhapcanh.gov.vn)",
                "Upon arrival, register your stay at the local police station or your accommodation does it",
                "For long-term stay: find a sponsor (employer, school or Vietnamese partner)",
                "Apply for a Temporary Residence Card (TRC) at the Immigration Department",
                "Obtain a tax code at the local Tax Department if working",
            ],
            "tip": "As of 2023, Vietnam e-visas allow 90 days multiple entry for most nationalities. This is sufficient for many long-term nomads who do a short trip to a neighbouring country every 3 months.",
        },
        "health": {
            "heading": "Healthcare in Vietnam",
            "public": "Public hospitals in Vietnam are overcrowded and language-challenged. Expats generally avoid them for all but emergencies. Foreigners registered with a Vietnamese employer can access the public health insurance system (BHYT).",
            "private": "International private hospitals serve the expat community well in Hanoi and HCMC: Family Medical Practice, Vinmec International, Columbia Asia, FV Hospital (HCMC). Quality is good; costs are moderate.",
            "costs": [
                ("GP consultation (private expat clinic)", "$40–80"),
                ("Specialist consultation", "$60–150"),
                ("Emergency room", "$100–300"),
                ("Hospitalisation (international hospital, per night)", "$300–800"),
                ("Dental cleaning", "$20–50"),
                ("Prescription medicines", "Very cheap — 30–80% cheaper than Western prices"),
            ],
            "recommended": "Always use international hospitals if available. While local hospitals handle emergencies, language barriers and differing standards make private care preferable for expats.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "Health insurance is not legally required for most expat visa categories in Vietnam, but it is essential. Medical evacuation from Vietnam to Singapore or Thailand for serious cases can cost $20,000–50,000 without coverage.",
            "providers": [
                ("Bao Viet Insurance", "Vietnam's largest insurer. Affordable local plans from ~$400/year. Limited English support."),
                ("Baoviet Health + PVI Insurance", "Popular among locally employed expats. From ~$500/year."),
                ("Cigna Global", "International plan, widely accepted at expat clinics. From ~$1,000/year."),
                ("AXA Global Healthcare", "Comprehensive worldwide coverage. Good for frequent travellers. From ~$1,200/year."),
                ("BUPA Global", "Premium plan, includes medical evacuation and repatriation. From ~$1,500/year."),
            ],
            "tip": "Make sure your plan explicitly covers medical evacuation and repatriation — these are the most expensive emergencies for expats in Vietnam and are often excluded from basic plans.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Vietnam",
            "intro": "A Vietnamese bank account simplifies daily life — cheaper rent payments, utility bills, local transfers and receiving salary. The process has become easier for foreigners holding TRCs.",
            "banks": [
                ("Vietcombank", "Vietnam's largest and most internationally connected bank. Good SWIFT network. English app available."),
                ("HSBC Vietnam", "Best option for international wire transfers. English-language service. Requires minimum balance."),
                ("Techcombank", "Strong digital banking. Popular with younger expats and tech workers."),
                ("VIB (Vietnam International Bank)", "Good mobile app, quick account opening. Accepts TRC holders easily."),
                ("Standard Chartered Vietnam", "Good for high-income expats. Full international banking services."),
            ],
            "requirements": [
                "Valid passport",
                "Temporary Residence Card (TRC) — tourist visa usually not accepted",
                "Proof of local address (rental contract)",
                "Vietnamese phone number",
            ],
            "process": [
                "Obtain a TRC or work permit first",
                "Visit bank branch with all documents",
                "Complete KYC form and biometrics",
                "Account opened same day in most banks",
                "Receive ATM/debit card within 3–5 business days",
            ],
            "tip": "Without a TRC, most Vietnamese banks will refuse to open an account. Vietcombank and HSBC Vietnam are the most foreigner-friendly. HSBC requires a higher minimum balance (~$500) but offers the best international wire service.",
        },
        "realestate": {
            "heading": "Buying Property in Vietnam",
            "intro": "Foreigners can buy property in Vietnam under the 2014 Housing Law, but with significant restrictions: maximum 30% of apartments in a building, no more than 250 houses in a ward, and ownership is limited to 50 years (renewable). Foreigners cannot own land — they lease it from the state.",
            "options": [
                ("Apartment ownership (50-year)", "Foreigners can buy apartments in approved developments. Ownership certificate valid 50 years, renewable once. Most common option."),
                ("Villa / House (50-year lease)", "50-year term on the land, with ownership of the structure. Renewable."),
                ("Through a Vietnamese company", "If you own a Vietnamese company with a local partner, the company can hold land long-term. Risky unless you trust your partner."),
            ],
            "process": [
                "Verify the project is open to foreign ownership (check with developer and local authority)",
                "Hire a Vietnamese lawyer who speaks English",
                "Sign a Sale and Purchase Agreement (SPA)",
                "Pay deposits in tranches as specified in the contract",
                "Receive the Pink Book (ownership certificate) — usually 3–6 months after completion",
                "Register at the local Land Registration Office",
            ],
            "costs": [
                ("Registration tax", "0.5% of property value"),
                ("Notarisation fees", "0.06–0.3% of transaction value"),
                ("Lawyer fees", "$1,000–3,000"),
                ("Agent commission", "1–3% (sometimes paid by developer)"),
                ("Annual land use fee", "Very low — typically $50–200/year"),
            ],
            "tip": "The 30% cap on foreign ownership in apartment buildings can affect resale — once the cap is hit, only Vietnamese buyers can purchase remaining units. Check the current foreign ownership ratio before buying.",
        },
    },
    "malaysia": {
        "name": "Malaysia",
        "flag_code": "my",
        "flag_emoji": "🇲🇾",
        "hero_bg": "https://flagcdn.com/w1280/my.png",
        "capital": "Kuala Lumpur",
        "currency": "Malaysian Ringgit (MYR)",
        "language": "Malay, English",
        "cost": "~$1,000–2,000/month",
        "title": "Complete Expat Guide Malaysia 2026 — Live, Work & Retire in Malaysia",
        "meta": "Complete guide to living in Malaysia as an expat in 2026. MM2H visa, DE Rantau nomad pass, healthcare, health insurance, bank accounts and property for foreigners.",
        "intro": "Malaysia is one of Asia's most underrated expat destinations — English is widely spoken, infrastructure is excellent, the food is extraordinary and the cost of living is among the lowest in the region for the quality on offer.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("MM2H (Malaysia My Second Home)", "Long-term residence programme for foreigners. Requirements since 2021: minimum 3-month fixed deposit of MYR 1,000,000, monthly offshore income of MYR 40,000, Malaysian health insurance. 5-year renewable visa. 60 days/year minimum stay."),
                ("DE Rantau (Digital Nomad Pass)", "For digital nomads earning USD 24,000+/year. 3–12 month pass, renewable. Single or family options available. Fast online application."),
                ("Employment Pass", "For foreign workers employed by Malaysian companies. Issued for 1–3 years. Requires employment contract with minimum salary MYR 5,000/month."),
                ("Resident Pass-Talent (RP-T)", "For highly skilled professionals. 10-year multiple-entry pass. No sponsorship needed. Requires degree and job offer or self-employment."),
                ("Professional Visit Pass", "Short-term professional activities, up to 12 months. Sponsored by a Malaysian company."),
            ],
            "steps": [
                "Determine visa category (MM2H for retirees, DE Rantau for nomads, Employment Pass for workers)",
                "Prepare documents: passport, income proof, health certificate, police clearance",
                "For MM2H: apply via an approved MM2H agent (mandatory)",
                "For DE Rantau: apply online via mdec.com.my",
                "For Employment Pass: employer applies on your behalf via EzXpat system",
                "Upon approval, enter Malaysia and activate the visa",
                "Register with LHDN (tax authority) if earning Malaysian-source income",
            ],
            "tip": "The new MM2H requirements (2021) are significantly stricter than before. The DE Rantau Nomad Pass at USD 24,000/year is a much more accessible option for remote workers and is processed within 2–4 weeks.",
        },
        "health": {
            "heading": "Healthcare in Malaysia",
            "public": "Malaysia has an excellent public healthcare system. Government hospitals charge a nominal fee for foreigners (RM 10–50 per consultation) but waiting times can be long. Non-residents pay more.  Emergency treatment is available to all.",
            "private": "Private hospitals in Malaysia are among the best in Southeast Asia and significantly cheaper than Singapore equivalents. KPJ Healthcare, Pantai Hospitals, Sunway Medical Centre and Prince Court (KL) are highly rated.",
            "costs": [
                ("Private GP consultation", "RM 50–120 (~$11–27)"),
                ("Private specialist", "RM 150–500 (~$34–113)"),
                ("Emergency (private)", "RM 300–1,000 (~$68–225)"),
                ("Hospitalisation (private, per night)", "RM 400–1,500 (~$90–338)"),
                ("Dental cleaning", "RM 100–200 (~$23–45)"),
                ("Eye exam + glasses", "RM 200–500 (~$45–113)"),
            ],
            "recommended": "MM2H requires proof of Malaysian health insurance. Even without this requirement, private health insurance is strongly recommended for expats due to the high cost of hospitalisation at private hospitals.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "MM2H requires Malaysian health insurance coverage. Beyond the visa requirement, private insurance is strongly recommended to cover hospitalisation, specialist care and medical evacuation.",
            "providers": [
                ("Great Eastern Life Malaysia", "Malaysia's largest life insurer. Comprehensive health riders available. From ~RM 200/month."),
                ("AIA Malaysia", "Strong private hospital network. International coverage option available. From ~RM 180/month."),
                ("Prudential Malaysia", "Good range of health plans. Widely accepted at private hospitals. From ~RM 190/month."),
                ("Cigna Global", "International plan accepted for MM2H. Good for those who split time between countries. From ~$100/month."),
                ("Pacific Cross Malaysia", "Specialist expat insurer. Good value for SE Asia-based expats. From ~RM 150/month."),
            ],
            "tip": "For MM2H specifically, the insurance must be issued by a Malaysian-licensed insurer and must be valid for the full duration of your stay. Great Eastern and AIA are the most commonly approved.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Malaysia",
            "intro": "A Malaysian bank account is needed for the MM2H fixed deposit requirement and for daily expenses. The process is straightforward for visa holders.",
            "banks": [
                ("Maybank", "Malaysia's largest bank. Most expat-friendly with English service. Required for MM2H fixed deposit. Extensive ATM network."),
                ("CIMB Bank", "Strong digital banking. International wire capabilities. Popular with younger expats."),
                ("HSBC Malaysia", "Best for international transfers. Higher minimum balance required."),
                ("Public Bank", "Conservative but reliable. Good for fixed deposits (required for MM2H)."),
                ("RHB Bank", "Good digital platform, competitive rates. Easy account opening."),
            ],
            "requirements": [
                "Valid passport",
                "Employment Pass, MM2H or DE Rantau Pass",
                "Proof of address in Malaysia (utility bill or rental contract)",
                "Malaysian phone number",
                "Initial deposit (RM 200–1,000 depending on account type)",
            ],
            "process": [
                "Visit the bank branch in person (online opening not available for foreigners)",
                "Present all required documents",
                "Account typically opened same day",
                "Receive debit card within 3–5 business days",
                "Activate online banking — usually requires Malaysian mobile number",
            ],
            "tip": "For MM2H, Maybank is the preferred bank for the fixed deposit requirement — it's the most familiar to the MM2H agents and immigration officers. Open a savings account first, then convert to a fixed deposit.",
        },
        "realestate": {
            "heading": "Buying Property in Malaysia",
            "intro": "Foreigners can buy property in Malaysia but with a minimum purchase price restriction. Since 2020, the national minimum for foreign buyers is MYR 1,000,000 (~$225,000), though some states have higher thresholds (e.g., Selangor: MYR 2,000,000).",
            "options": [
                ("Freehold Title", "Full ownership, no time restriction. Available to foreigners above the minimum threshold."),
                ("Leasehold Title", "99-year lease on the land. Common for high-rise condominiums. After 99 years, the land reverts to the state."),
                ("MM2H Property", "MM2H holders have access to slightly lower minimum purchase thresholds in some states."),
            ],
            "process": [
                "Obtain a Consent to Purchase from the State Authority (required for foreigners in some states)",
                "Hire a Malaysian property lawyer (solicitor)",
                "Sign the Letter of Offer / Booking Form and pay 2–3% deposit",
                "Lawyer conducts title search and property due diligence",
                "Sign the Sale and Purchase Agreement (SPA) — pay 10% deposit within 14 days",
                "Pay balance within 90 days (or as per SPA)",
                "Register title transfer at the Land Office",
            ],
            "costs": [
                ("Stamp duty", "1–4% on the purchase price (graduated)"),
                ("Real Property Gains Tax (RPGT)", "0–30% on profits when selling (exemptions apply after 5 years)"),
                ("Lawyer fees", "0.5–1% of purchase price"),
                ("Agent commission", "2–3% (paid by seller)"),
                ("Annual quit rent (Cukai Tanah)", "Very low — typically RM 50–500/year"),
                ("Annual assessment tax", "~RM 100–500/year depending on local council"),
            ],
            "tip": "Check the minimum price threshold in your specific state — it varies from MYR 1,000,000 in most states to MYR 2,000,000 in Selangor. KL properties are generally freehold; many suburban properties are leasehold.",
        },
    },
    "japan": {
        "name": "Japan",
        "flag_code": "jp",
        "flag_emoji": "🇯🇵",
        "hero_bg": "https://flagcdn.com/w1280/jp.png",
        "capital": "Tokyo",
        "currency": "Japanese Yen (JPY)",
        "language": "Japanese",
        "cost": "~$1,500–3,000/month",
        "title": "Complete Expat Guide Japan 2026 — Live, Work & Retire in Japan",
        "meta": "Complete guide to living in Japan as an expat in 2026. Highly skilled professional visa, digital nomad visa, national health insurance, bank accounts and property for foreigners.",
        "intro": "Japan combines extraordinary safety, efficient infrastructure, unique culture and excellent healthcare. The 2024 Digital Nomad Visa and the Highly Skilled Professional (HSP) point system have made Japan more accessible than ever for skilled foreign workers.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Digital Nomad Visa (2024)", "New 6-month visa for remote workers earning ¥10,000,000/year (~$65,000+). Single-entry, extendable for 6 months. Must have health insurance. Cannot work for Japanese companies."),
                ("Highly Skilled Professional (HSP)", "Points-based system (70+ points). Points for education, income, age, Japanese ability. Allows fast-track to permanent residence (1–3 years vs standard 10)."),
                ("Engineer/Specialist Visa", "For IT, engineering and scientific professionals. Requires job offer from Japanese employer. 1–5 year renewable permit."),
                ("Specified Skilled Worker (SSW)", "For specified industries (hospitality, food service, care, construction). No degree required. Up to 5 years."),
                ("Spouse/Dependent Visa", "For spouses and dependent children of work visa holders or permanent residents. Allows certain types of employment."),
                ("Permanent Resident (PR)", "After 10 years continuous residence (or 1–3 years on HSP visa). No work restrictions. Highly desirable."),
            ],
            "steps": [
                "Secure a job offer from a Japanese employer OR qualify for the Digital Nomad Visa",
                "Employer applies for Certificate of Eligibility (CoE) from the Japan Immigration Services Agency",
                "Apply for the visa at the Japanese embassy in your country using the CoE",
                "Arrive in Japan and register at your ward/municipal office within 14 days",
                "Obtain your Residence Card (在留カード) at the airport or municipal office",
                "Enrol in National Health Insurance (国民健康保険) at the municipal office",
                "Obtain a My Number Card (マイナンバーカード) — Japan's national ID",
                "Open a bank account (requires Residence Card)",
            ],
            "tip": "The My Number Card has become increasingly important in Japan — it's needed for taxes, bank accounts, health insurance and government services. Apply for it at your local ward office as soon as possible.",
        },
        "health": {
            "heading": "Healthcare in Japan",
            "public": "Japan has a universal health insurance system. All residents (including foreigners with a Residence Card) must enrol in either National Health Insurance (国民健康保険, Kokumin Kenkou Hoken) for self-employed/unemployed, or company health insurance (社会保険) for employees. Patients pay 30% of medical costs; the insurance covers 70%.",
            "private": "Japan's public hospitals are excellent — among the best in the world. Private clinics are common for routine care. International clinics in Tokyo (JICA, St. Luke's International, Tokyo Midtown Medical Center) offer English-language services.",
            "costs": [
                ("NHI monthly premium (employee, 30%)", "~¥15,000–35,000/month depending on income"),
                ("GP consultation (30% co-pay)", "¥1,000–3,000 (~$7–20)"),
                ("Specialist consultation (30% co-pay)", "¥2,000–6,000 (~$13–40)"),
                ("Hospitalisation (30% co-pay, per day)", "¥5,000–20,000 (~$33–133)"),
                ("Dental (partial coverage)", "¥2,000–5,000 per visit"),
                ("Prescription medicines (30% co-pay)", "¥200–2,000"),
            ],
            "recommended": "Enrol in the public health insurance system immediately upon registering your residence — it is mandatory and provides excellent value. You will also need a high-limit cost cap — Japan's system caps out-of-pocket costs at ¥80,100/month for average earners.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "Because Japan's National Health Insurance already covers 70% of medical costs, supplementary insurance is less critical than in other countries. However, international health insurance is useful for the period before NHI enrolment, for English-language hospitals, and for coverage during international travel.",
            "providers": [
                ("Tokio Marine Nichido", "Japan's largest private insurer. Cancer and hospitalisation riders. For Japanese-speakers primarily."),
                ("Aflac Japan", "Popular cancer and medical indemnity plans. Useful as a supplement to NHI. English support available."),
                ("AIG Japan / Fuji Life", "International plans for expats. Good English support. From ~¥15,000/month."),
                ("Cigna Global", "International plan for pre-arrival period and for coverage outside Japan. From ~$100/month."),
                ("AXA Global Healthcare", "Good for expats who travel frequently. Worldwide coverage including Japan. From ~$120/month."),
            ],
            "tip": "For most working expats in Japan, the mandatory NHI or company health insurance + a supplementary cancer/hospitalisation plan from a local insurer like Aflac is the most cost-effective setup.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Japan",
            "intro": "A Japanese bank account is essential for receiving salary, paying rent, utilities and taxes. It has historically been difficult for new arrivals, but the process has improved significantly.",
            "banks": [
                ("Japan Post Bank (ゆうちょ銀行)", "Easiest bank to open for foreigners. Accepts residence cards from 6 months after arrival. No minimum balance. Largest ATM network in Japan."),
                ("MUFG (Mitsubishi UFJ)", "Largest megabank. Good international wire capabilities. English online banking available."),
                ("Sony Bank", "Online bank with the best FX rates in Japan. Excellent English interface. Requires Residence Card. Popular with expats."),
                ("Shinsei Bank (SBI Shinsei)", "English-language internet banking. No ATM fees at 7-Eleven. Good for international transfers."),
                ("Wise (Multi-currency)", "Not a full bank but widely used by expats for international transfers and multi-currency transactions."),
            ],
            "requirements": [
                "Residence Card (在留カード) — mandatory",
                "My Number Card or My Number notification slip",
                "Japanese phone number or smartphone",
                "Proof of address (or residence card address is sufficient)",
                "Some banks require 6 months of residence before opening",
            ],
            "process": [
                "Register your address at the ward office and obtain your Residence Card",
                "Obtain My Number Card (apply at ward office, takes ~1 month)",
                "Visit Japan Post Bank or apply online at Sony Bank / Shinsei",
                "Present Residence Card and My Number",
                "Receive bankbook and/or debit card within 1–2 weeks",
            ],
            "tip": "Japan Post Bank is the easiest to open immediately. Sony Bank has the best FX rates and English interface — open it once you've been resident for a few months.",
        },
        "realestate": {
            "heading": "Buying Property in Japan",
            "intro": "Japan has no restrictions on foreigners buying property — freehold ownership is fully permitted. Japan is unique in that properties (especially houses) can depreciate significantly over time, while land values are more stable. Prices outside Tokyo and major cities are remarkably low.",
            "options": [
                ("Condominium (Mansion)", "Full freehold ownership. Most expats buy condos in Tokyo, Osaka or Kyoto. Popular in international communities."),
                ("Single-family house (Kodate)", "Full ownership of land and structure. Houses depreciate to near-zero after 20–30 years in Japan — land is the main value."),
                ("Akiya (Abandoned house)", "Vacant properties in rural areas, sometimes available for ¥1 (~$0.01) or very low prices. Renovation costs can be high."),
            ],
            "process": [
                "Obtain a long-term residence visa (tourist visa insufficient for mortgage)",
                "Hire a licensed real estate agent (宅地建物取引業者) — usually no buyer fee",
                "Identify properties via SUUMO, AtHome or an expat-specialist agency",
                "Make an offer and receive the Property Information Document (重要事項説明書)",
                "Sign the Purchase Agreement (売買契約書) — pay 10% deposit",
                "Arrange mortgage (if applicable) or wire full payment",
                "Transfer at the notary / legal scrivener (司法書士) — title registered in land registry",
            ],
            "costs": [
                ("Real estate agent fee", "3% + ¥60,000 + tax (paid by buyer and seller)"),
                ("Registration and license tax", "0.1–2% of assessed value"),
                ("Property acquisition tax", "3–4% of assessed value (one-time, 3–6 months after purchase)"),
                ("Judicial scrivener (registration)", "¥100,000–300,000"),
                ("Annual fixed asset tax", "1.4% of assessed value (about 70% of market value)"),
                ("Building inspection", "¥50,000–100,000 recommended"),
            ],
            "tip": "In rural Japan, you can buy a fully habitable house for ¥2,000,000–5,000,000 (~$13,000–33,000). The Akiya Banks (空き家バンク) run by municipalities list vacant properties. The main cost is renovation, not purchase.",
        },
    },
    "uae": {
        "name": "UAE",
        "flag_code": "ae",
        "flag_emoji": "🇦🇪",
        "hero_bg": "https://flagcdn.com/w1280/ae.png",
        "capital": "Abu Dhabi (Dubai most popular for expats)",
        "currency": "UAE Dirham (AED)",
        "language": "Arabic, English",
        "cost": "~$2,500–5,000/month",
        "title": "Complete Expat Guide UAE 2026 — Live, Work & Retire in Dubai & Abu Dhabi",
        "meta": "Complete guide to living in the UAE as an expat in 2026. Golden Visa, green visa, freelance permit, healthcare, health insurance, bank accounts and property for foreigners.",
        "intro": "The UAE — particularly Dubai — has positioned itself as the world's leading destination for high-net-worth expats and remote workers. Zero income tax, world-class infrastructure, modern healthcare and a cosmopolitan lifestyle make it uniquely attractive.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Golden Visa (10 years)", "For investors, entrepreneurs, specialised talents and outstanding students. Property investment ≥AED 2,000,000. No employer sponsorship needed. Renewable. Includes family members."),
                ("Green Visa (5 years)", "For skilled workers, freelancers and investors. Self-sponsored. Income ≥AED 15,000/month for skilled employees. No employer sponsorship needed."),
                ("Employment Visa (2–3 years)", "Sponsored by employer. Most common route. Employer handles the application. Includes Emirates ID and health card."),
                ("Freelance/Remote Work Visa", "1-year renewable remote work visa. Income ≥$3,500/month. Allows residing in the UAE while working for a foreign company."),
                ("Retirement Visa (5 years)", "For retirees 55+. Must meet one of: real estate worth AED 2M+, financial savings AED 1M+, or AED 20,000/month income."),
            ],
            "steps": [
                "Determine your visa category based on your situation",
                "For employment visa: employer initiates the process via Ministry of Human Resources",
                "Medical fitness test at an approved centre",
                "Emirates ID registration (biometrics)",
                "Obtain residence visa stamp in passport",
                "Register tenancy contract on Ejari (Dubai) or Tawtheeq (Abu Dhabi)",
                "Open a UAE bank account",
                "Obtain Dubai Health Authority (DHA) or HAAD (Abu Dhabi) health card",
            ],
            "tip": "The Green Visa is the most flexible option for independent professionals — it allows you to sponsor yourself without a local employer, and you can stay 180 days outside the UAE without losing residency.",
        },
        "health": {
            "heading": "Healthcare in the UAE",
            "public": "Government hospitals (Dubai Health Authority, Abu Dhabi DOH) are available to UAE residents. Emiratis get free care; expats pay reduced rates. However, most expats prefer private hospitals due to better English service and shorter waiting times.",
            "private": "The UAE has world-class private healthcare. Dubai: Mediclinic, Cleveland Clinic Abu Dhabi, American Hospital Dubai. Abu Dhabi: Cleveland Clinic, Burjeel, Aster Hospitals. English is the working language in all major facilities.",
            "costs": [
                ("Private GP consultation", "AED 300–600 (~$82–163)"),
                ("Specialist consultation", "AED 500–1,500 (~$136–408)"),
                ("Emergency room", "AED 500–2,000 (~$136–545)"),
                ("Hospitalisation (per night)", "AED 2,000–8,000 (~$545–2,178)"),
                ("Dental cleaning", "AED 300–600 (~$82–163)"),
                ("Dental (major work)", "AED 1,500–8,000 (~$408–2,178)"),
            ],
            "recommended": "Health insurance is MANDATORY in Dubai (all residents and employers must have coverage) and in Abu Dhabi. Employer-sponsored health insurance is standard. Self-employed residents must arrange their own.",
        },
        "insurance": {
            "heading": "Health Insurance in the UAE",
            "intro": "Health insurance is legally mandatory for all residents in Dubai and Abu Dhabi. In Dubai, employers with 100+ employees must provide Essential Benefits Plan (EBP) or above. Self-employed residents must purchase their own. The minimum plan (Essential Benefits Plan) costs ~AED 600–750/year.",
            "providers": [
                ("Daman (National Health Insurance Company)", "Abu Dhabi's official mandatory insurer. All Abu Dhabi residents must be covered by Daman as primary insurer."),
                ("AXA Gulf", "Wide network, strong in Dubai. Good for employer group plans. Premium plans from AED 5,000/year."),
                ("Cigna Global", "Popular with multinational employees. International coverage. From AED 7,000/year."),
                ("Bupa Arabia / Bupa Global", "Regional leader. Strong hospital network. From AED 6,000/year."),
                ("MetLife Gulf", "Good for families and dental coverage. From AED 4,500/year."),
            ],
            "tip": "In Dubai, even the minimum Essential Benefits Plan (EBP) covers emergency care, maternity and pre-existing conditions. For comprehensive private hospital access and international coverage, upgrade to an enhanced plan.",
        },
        "bank": {
            "heading": "Opening a Bank Account in the UAE",
            "intro": "A UAE bank account is essential for receiving salary, paying rent (often via post-dated cheques in Dubai), utility bills and daily transactions. The process requires Emirates ID.",
            "banks": [
                ("Emirates NBD", "UAE's largest bank. Good English service, strong online banking, extensive ATM network."),
                ("ADCB (Abu Dhabi Commercial Bank)", "Best for Abu Dhabi residents. Good international transfer rates."),
                ("HSBC UAE", "Best for international wire transfers and expats with global banking needs. High minimum balance (AED 25,000 for some accounts)."),
                ("Mashreq Bank", "Fastest account opening (sometimes same day). Strong digital banking. Neo account with no minimum balance."),
                ("Wio Bank (digital)", "New digital bank. Instant account opening with Emirates ID. No fees. Popular with freelancers and nomads."),
            ],
            "requirements": [
                "Emirates ID (mandatory)",
                "Valid passport with UAE visa",
                "Salary certificate or proof of income",
                "Employment contract or trade licence (for freelancers)",
                "UAE phone number",
                "Minimum salary may apply (AED 5,000–10,000/month for some banks)",
            ],
            "process": [
                "Obtain your Emirates ID first (issued after residence visa is stamped)",
                "Book appointment at the bank or apply digitally",
                "Submit all documents",
                "Account activated within 1–5 business days",
                "Receive debit card and online banking access",
            ],
            "tip": "Mashreq Neo and Wio Bank offer the fastest account opening — sometimes within 24 hours — with no minimum balance. Ideal for new arrivals while waiting for Emirates NBD or HSBC approval.",
        },
        "realestate": {
            "heading": "Buying Property in the UAE",
            "intro": "Foreigners can buy property in the UAE in designated freehold zones (Dubai has over 60 freehold areas). Abu Dhabi has more restricted zones. Property purchase can qualify for a Golden Visa (≥AED 2,000,000).",
            "options": [
                ("Freehold Ownership", "Full ownership in designated freehold zones. Available to all nationalities. Most condos and many villas are freehold."),
                ("Leasehold (up to 99 years)", "Available outside freehold zones. Long-term lease but no land ownership."),
                ("Off-Plan Purchase", "Buying from developers before or during construction. Typically 10–40% cheaper than ready units. Developer payment plans common (20/80, 40/60)."),
            ],
            "process": [
                "Identify property and sign a Memorandum of Understanding (MOU) — pay 10% deposit",
                "Get a No Objection Certificate (NOC) from the developer (if resale)",
                "Both parties attend the Dubai Land Department (DLD) for transfer",
                "Pay Transfer Fee (4%) and obtain new title deed",
                "Register with Ejari if renting out the property",
            ],
            "costs": [
                ("Dubai Land Department (DLD) transfer fee", "4% of purchase price"),
                ("Agent commission", "2% (buyer) + 2% (seller) = 4% total"),
                ("NOC fee", "AED 500–5,000"),
                ("Registration fee", "AED 2,000–4,000"),
                ("Annual service charges", "AED 10–30/sq ft depending on development"),
                ("No annual property tax in the UAE", "—"),
            ],
            "tip": "Dubai has no annual property tax and no capital gains tax on property — only the 4% transfer fee on purchase. Off-plan properties from developers like Emaar, Damac and Nakheel often come with 0% payment plans stretching 5–8 years.",
        },
    },
    "colombia": {
        "name": "Colombia",
        "flag_code": "co",
        "flag_emoji": "🇨🇴",
        "hero_bg": "https://flagcdn.com/w1280/co.png",
        "capital": "Bogotá",
        "currency": "Colombian Peso (COP)",
        "language": "Spanish",
        "cost": "~$1,000–2,000/month",
        "title": "Complete Expat Guide Colombia 2026 — Live, Work & Retire in Colombia",
        "meta": "Complete guide to living in Colombia as an expat in 2026. Digital nomad visa, pensionado visa, healthcare, health insurance, bank accounts and property for foreigners.",
        "intro": "Colombia has transformed dramatically over the past decade — Medellín was named the world's most innovative city, and cities like Bogotá, Cartagena and Santa Marta offer a rich mix of culture, climate and affordability. Colombia's digital nomad visa and affordable EPS health system make it increasingly popular with expats.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Digital Nomad Visa (V Nómada Digital)", "For remote workers. Must prove $684/month income (3× minimum wage). 2-year visa with multiple-entry. Does not allow working for Colombian companies."),
                ("Pensionado Visa (M Pensionado)", "For retirees with proven pension of at least $684/month. 2-year visa, renewable. Includes right to work."),
                ("Migrant Visa (M Visa)", "For various categories: employee, investor, real estate owner (property ≥350 SMMLV ~$100,000). 2-year renewable."),
                ("Resident Visa (R Visa)", "Permanent residency after 5 continuous years on M Visa, or via marriage to Colombian national. Renewable every 5 years."),
                ("Visitor Visa / Visa-Free", "Citizens of most Western countries can enter visa-free for 90 days, extendable to 180 days/year. No work permitted."),
            ],
            "steps": [
                "Apply online via the Colombian Foreign Ministry visa portal (cancilleria.gov.co)",
                "Upload all required documents (passport, photos, income proof, criminal record)",
                "Pay the visa fee (~$52 application, ~$232 issuance)",
                "Receive visa within 15–30 business days",
                "Arrive in Colombia and within 15 days register the visa at a Migración Colombia office",
                "Obtain a Cédula de Extranjería (foreigner ID card) at Migración Colombia",
                "Register with the DIAN (tax authority) to get an RUT (tax ID) if working",
            ],
            "tip": "The Digital Nomad Visa is valid for 2 years and is the most popular new route for remote workers. The income requirement of ~$684/month (3× Colombian minimum wage) is very accessible.",
        },
        "health": {
            "heading": "Healthcare in Colombia",
            "public": "Colombia has a unique dual healthcare system. The EPS (Entidad Promotora de Salud) system provides universal coverage to all legal residents. Foreigners with a Cédula de Extranjería can enrol in EPS for ~$50–200/month (based on income). Quality varies enormously by city and provider.",
            "private": "Colombia also has excellent private hospitals that are much cheaper than US/European equivalents. Medellín is a world-renowned medical tourism destination: Clínica El Rosario, Clínica del Country (Bogotá), Hospital Pablo Tobón (Medellín). Dental and cosmetic surgery are 60–80% cheaper than in the US.",
            "costs": [
                ("EPS monthly premium (foreigner)", "~$50–200/month (income-based)"),
                ("EPS GP consultation (co-payment)", "~$0–5 (nearly free)"),
                ("Private specialist consultation", "COP 80,000–200,000 (~$20–50)"),
                ("Private emergency room", "COP 200,000–800,000 (~$50–200)"),
                ("Dental cleaning (private)", "COP 60,000–120,000 (~$15–30)"),
                ("Major private surgery", "60–80% cheaper than US equivalent"),
            ],
            "recommended": "Enrol in EPS for routine and emergency care. Add a supplementary private plan or use top private hospitals (prepago plan) for specialist care and English-language service.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "While EPS provides solid basic coverage, wait times for specialists and certain services can be long. A supplementary private plan (medicina prepagada) gives immediate access to private hospitals and specialists.",
            "providers": [
                ("Colsanitas", "Colombia's most prestigious private health insurer. Full access to Clínica del Country and Clínica de La Sabana. From ~$200/month."),
                ("Compensar", "EPS + private plan combined. Strong in Bogotá. From ~$150/month."),
                ("Sura (EPS + Prepagada)", "Large network, good app, strong emergency coverage. From ~$160/month."),
                ("Cigna Global", "International plan for expats needing US or European coverage. From ~$100/month."),
                ("AXA Colombia", "International plan with Latin America coverage. Good for frequent travellers. From ~$120/month."),
            ],
            "tip": "Colsanitas is considered the gold standard of Colombian private health insurance among expats. The combination of EPS (for routine/emergency) + Colsanitas prepago (for specialists and surgery) offers excellent coverage at a fraction of US costs.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Colombia",
            "intro": "A Colombian bank account simplifies daily life — rent payments, utility bills, salary receipt and online shopping. The process requires a Cédula de Extranjería (foreigner ID).",
            "banks": [
                ("Bancolombia", "Colombia's largest bank. Most expat-friendly with English app. Extensive ATM network. Good online banking."),
                ("Banco de Bogotá", "Second-largest bank. Strong in Bogotá, Medellín and main cities. Competitive rates."),
                ("Davivienda", "Good mobile app. Popular with young expats and digital nomads."),
                ("Nequi (Bancolombia digital)", "Digital wallet/account. Instant opening with cédula. No fees. Good for daily transactions but not full banking."),
                ("Nubank (Nu Colombia)", "Digital bank. Very easy to open. No fees, great app. Growing rapidly in Colombia."),
            ],
            "requirements": [
                "Cédula de Extranjería (foreigner ID card) — mandatory",
                "Proof of address (rental contract or utility bill)",
                "Colombian phone number",
                "RUT (tax ID) for some account types",
                "Minimum initial deposit (varies by bank and account type)",
            ],
            "process": [
                "Obtain your Cédula de Extranjería at Migración Colombia first",
                "Visit bank branch or apply digitally (Nubank, Nequi)",
                "Present Cédula and proof of address",
                "Account opened same day in most cases",
                "Receive debit card within 5–7 business days",
            ],
            "tip": "Start with Nequi or Nu Colombia (fully digital, instant account) while waiting for your Cédula. Once you have your Cédula, open a Bancolombia account for more complete banking services.",
        },
        "realestate": {
            "heading": "Buying Property in Colombia",
            "intro": "Foreigners can freely buy property in Colombia with no restrictions. Colombia is one of the most accessible property markets in Latin America for foreigners. Medellín has become a hotspot, with Bogotá, Cartagena and Santa Marta also very popular.",
            "options": [
                ("Freehold Purchase", "Full ownership, no restrictions for foreigners. Standard method for all property types."),
                ("M Visa via Property", "Owning property worth ≥350 SMMLV (~$100,000) qualifies you for a Migrant Visa (2 years, renewable)."),
                ("Off-Plan Purchase", "Common in Medellín and Bogotá. Typically 15–30% cheaper than finished properties. Developers offer payment plans during construction."),
            ],
            "process": [
                "Obtain a RUT (Colombian tax ID) at the DIAN — required for property purchase",
                "Hire a Colombian real estate lawyer (abogado)",
                "Sign a Promesa de Compraventa (preliminary agreement) — pay 10–30% deposit",
                "Lawyer conducts title search at the Public Instruments Registry",
                "Sign the Escritura Pública (deed) before a Notario",
                "Register at the Public Instruments Registry (Registro de Instrumentos Públicos)",
                "Pay transfer taxes",
            ],
            "costs": [
                ("Property transfer tax (Impuesto de Registro)", "0.5–1% of transaction value"),
                ("Notary fees", "~0.3–0.5% of transaction value (split buyer/seller)"),
                ("Registration fee", "0.5–1%"),
                ("Lawyer fees", "1–2%"),
                ("Annual property tax (Predial)", "0.5–1.2% of assessed value"),
                ("Agent commission", "3–5% (paid by seller)"),
            ],
            "tip": "Medellín's El Poblado and Laureles neighbourhoods offer the highest concentration of expat-friendly properties and services. Cartagena's Getsemaní is an up-and-coming area with strong rental yields. Always verify the Certificado de Tradición y Libertad (title certificate) at the Registry before any payment.",
        },
    },
}

# ─── HTML generation ─────────────────────────────────────────────────────────

def make_page(slug, data):
    name = data["name"]
    flag = data["flag_code"]
    bg = data["hero_bg"]
    title = data["title"]
    meta = data["meta"]
    intro = data["intro"]
    v = data["visa"]
    h = data["health"]
    ins = data["insurance"]
    b = data["bank"]
    r = data["realestate"]

    # Build visa types table
    visa_rows = "".join(
        f'<tr><td style="font-weight:600;width:35%;padding:8px 12px;border-bottom:1px solid #eee;">{t}</td>'
        f'<td style="padding:8px 12px;border-bottom:1px solid #eee;">{desc}</td></tr>'
        for t, desc in v["types"]
    )

    # Build visa steps
    visa_steps = "".join(
        f'<li style="margin-bottom:8px;">{step}</li>'
        for i, step in enumerate(v["steps"], 1)
    )

    # Build health costs table
    health_rows = "".join(
        f'<tr><td style="padding:6px 12px;border-bottom:1px solid #eee;">{item}</td>'
        f'<td style="padding:6px 12px;border-bottom:1px solid #eee;font-weight:600;">{cost}</td></tr>'
        for item, cost in h["costs"]
    )

    # Build insurance providers
    ins_providers = "".join(
        f'<div style="background:#f8f9fc;border-radius:6px;padding:14px 18px;margin-bottom:10px;">'
        f'<strong style="color:#1d2d50;">{prov}</strong><br/>'
        f'<span style="font-size:.9rem;color:#555;">{desc}</span></div>'
        for prov, desc in ins["providers"]
    )

    # Build bank accounts
    bank_list = "".join(
        f'<div style="border-left:3px solid #f15d30;padding:8px 14px;margin-bottom:8px;">'
        f'<strong>{bank}</strong> — <span style="color:#555;font-size:.9rem;">{desc}</span></div>'
        for bank, desc in b["banks"]
    )
    bank_req = "".join(f'<li>{req}</li>' for req in b["requirements"])
    bank_steps = "".join(f'<li style="margin-bottom:6px;">{step}</li>' for step in b["process"])

    # Build RE options
    re_options = "".join(
        f'<div style="background:#f8f9fc;border-radius:6px;padding:12px 16px;margin-bottom:8px;">'
        f'<strong style="color:#1d2d50;">{opt}</strong><br/>'
        f'<span style="font-size:.9rem;color:#555;">{desc}</span></div>'
        for opt, desc in r["options"]
    )
    re_steps = "".join(f'<li style="margin-bottom:8px;">{step}</li>' for step in r["process"])
    re_costs = "".join(
        f'<tr><td style="padding:6px 12px;border-bottom:1px solid #eee;">{item}</td>'
        f'<td style="padding:6px 12px;border-bottom:1px solid #eee;font-weight:600;">{cost}</td></tr>'
        for item, cost in r["costs"]
    )

    hreflang_block = "\n".join([
        f'    <link rel="alternate" hreflang="en" href="{BASE}/en/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="fr" href="{BASE}/fr/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="es" href="{BASE}/es/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="pt" href="{BASE}/pt/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="zh" href="{BASE}/zh/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="th" href="{BASE}/th/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="ru" href="{BASE}/ru/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="ar" href="{BASE}/ar/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="ja" href="{BASE}/ja/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="ko" href="{BASE}/ko/expat-guide-{slug}.html"/>',
        f'    <link rel="alternate" hreflang="x-default" href="{BASE}/en/expat-guide-{slug}.html"/>',
    ])

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="description" content="{meta}"/>
    <link rel="canonical" href="{BASE}/en/expat-guide-{slug}.html"/>
{hreflang_block}
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@graph":[
    {{"@type":"FAQPage","mainEntity":[
    {{"@type":"Question","name":"Can foreigners buy property in {name}?","acceptedAnswer":{{"@type":"Answer","text":"{r["intro"][:200]}"}} }},
    {{"@type":"Question","name":"What health insurance do I need in {name}?","acceptedAnswer":{{"@type":"Answer","text":"{ins["intro"][:200]}"}} }},
    {{"@type":"Question","name":"How do I open a bank account in {name}?","acceptedAnswer":{{"@type":"Answer","text":"{b["intro"][:200]}"}} }}
    ]}}
    ]}}
    </script>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light" id="ftco-navbar" style="background-color:#0d2461 !important;position:relative;z-index:10;">
    <div class="container">
        <a class="navbar-brand" href="../index.html" style="padding:0;"><img src="../images/logo.png" alt="eVisa-Card.com" style="height:120px;width:auto;display:block;"></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse justify-content-center" id="ftco-nav">
            <ul class="navbar-nav align-items-center">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link active" href="/en/expat-guides.html">Guides</a></li>
                <li class="nav-item dropdown ml-3">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi fi-gb"></span> English</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item active" href="/en/expat-guide-{slug}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/fr/expat-guide-{slug}.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/es/expat-guide-{slug}.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/pt/expat-guide-{slug}.html"><span class="fi fi-br"></span> Português</a>
                        <a class="dropdown-item" href="/zh/expat-guide-{slug}.html"><span class="fi fi-cn"></span> 中文</a>
                        <a class="dropdown-item" href="/th/expat-guide-{slug}.html"><span class="fi fi-th"></span> ไทย</a>
                        <a class="dropdown-item" href="/ru/expat-guide-{slug}.html"><span class="fi fi-ru"></span> Русский</a>
                        <a class="dropdown-item" href="/ar/expat-guide-{slug}.html"><span class="fi fi-sa"></span> العربية</a>
                        <a class="dropdown-item" href="/ja/expat-guide-{slug}.html"><span class="fi fi-jp"></span> 日本語</a>
                        <a class="dropdown-item" href="/ko/expat-guide-{slug}.html"><span class="fi fi-kr"></span> 한국어</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="hero-wrap hero-wrap-2" style="background-image:url('{bg}');background-size:cover;background-position:center;" data-stellar-background-ratio="0.5">
    <div class="overlay"></div>
    <div class="container">
        <div class="row no-gutters slider-text align-items-end justify-content-center">
            <div class="col-md-9 ftco-animate text-center pb-5">
                <p class="breadcrumbs"><span class="mr-2"><a href="../index.html">Home <i class="fa fa-chevron-right"></i></a></span> <span class="mr-2"><a href="/en/expat-guides.html">Expat Guides <i class="fa fa-chevron-right"></i></a></span> <span>{name}</span></p>
                <h1 class="mb-0 bread">Expat Guide: Living in {name} 2026</h1>
            </div>
        </div>
    </div>
</section>

<section class="ftco-section">
<div class="container" style="max-width:960px;">

    <!-- Intro + Key Facts -->
    <div class="row mb-5">
        <div class="col-md-8">
            <p style="font-size:17px;color:#444;line-height:1.8;">{intro}</p>
            <p style="font-size:13px;color:#999;">Last updated: March 2026 — <em>Editorial Team, eVisa-Card.com</em></p>
        </div>
        <div class="col-md-4">
            <div style="background:#f8f9fc;border-left:4px solid #f15d30;padding:18px 20px;border-radius:4px;">
                <h3 style="font-size:16px;margin-bottom:12px;color:#1d2d50;"><span class="fi fi-{flag}" style="margin-right:6px;"></span> {name} at a Glance</h3>
                <table style="width:100%;font-size:.88rem;">
                    <tr><td style="padding:3px 0;color:#888;">Capital</td><td style="font-weight:600;">{data["capital"]}</td></tr>
                    <tr><td style="padding:3px 0;color:#888;">Currency</td><td style="font-weight:600;">{data["currency"]}</td></tr>
                    <tr><td style="padding:3px 0;color:#888;">Language</td><td style="font-weight:600;">{data["language"]}</td></tr>
                    <tr><td style="padding:3px 0;color:#888;">Monthly cost</td><td style="font-weight:600;">{data["cost"]}</td></tr>
                </table>
            </div>
        </div>
    </div>

    <!-- Table of Contents -->
    <div class="row mb-5">
        <div class="col-md-12">
            <div style="background:#fff;border:1px solid #e0e4f0;border-radius:6px;padding:20px 24px;">
                <h2 style="font-size:16px;margin-bottom:12px;color:#1d2d50;">📋 Table of Contents</h2>
                <ol style="margin:0;padding-left:20px;font-size:.95rem;">
                    <li><a href="#visa" style="color:#f15d30;">Visa &amp; Residency Options</a></li>
                    <li><a href="#health" style="color:#f15d30;">Healthcare System</a></li>
                    <li><a href="#insurance" style="color:#f15d30;">Health Insurance</a></li>
                    <li><a href="#bank" style="color:#f15d30;">Opening a Bank Account</a></li>
                    <li><a href="#realestate" style="color:#f15d30;">Buying Property</a></li>
                </ol>
            </div>
        </div>
    </div>

    <!-- Section 1: Visa -->
    <div class="row mb-5" id="visa">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">
                🛂 {v["heading"]}
            </h2>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Available Visa Types</h3>
            <div style="overflow-x:auto;">
            <table style="width:100%;border-collapse:collapse;font-size:.92rem;margin-bottom:24px;">
                <thead>
                    <tr style="background:#1d2d50;color:#fff;">
                        <th style="padding:10px 12px;text-align:left;">Visa Type</th>
                        <th style="padding:10px 12px;text-align:left;">Details</th>
                    </tr>
                </thead>
                <tbody>{visa_rows}</tbody>
            </table>
            </div>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Step-by-Step Residency Process</h3>
            <ol style="font-size:.95rem;line-height:1.8;padding-left:20px;">{visa_steps}</ol>
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:14px 18px;border-radius:4px;margin-top:16px;">
                <strong>💡 Pro Tip:</strong> {v["tip"]}
            </div>
        </div>
    </div>

    <!-- Section 2: Health -->
    <div class="row mb-5" id="health">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">
                🏥 {h["heading"]}
            </h2>
            <div class="row mb-4">
                <div class="col-md-6">
                    <div style="background:#f0f7ff;border-radius:6px;padding:18px;height:100%;">
                        <h3 style="font-size:16px;color:#1d2d50;margin-bottom:10px;">Public Healthcare</h3>
                        <p style="font-size:.92rem;color:#555;margin:0;">{h["public"]}</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div style="background:#f0fff4;border-radius:6px;padding:18px;height:100%;">
                        <h3 style="font-size:16px;color:#1d2d50;margin-bottom:10px;">Private Healthcare</h3>
                        <p style="font-size:.92rem;color:#555;margin:0;">{h["private"]}</p>
                    </div>
                </div>
            </div>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Typical Healthcare Costs</h3>
            <div style="overflow-x:auto;">
            <table style="width:100%;border-collapse:collapse;font-size:.92rem;margin-bottom:16px;">
                <thead>
                    <tr style="background:#1d2d50;color:#fff;">
                        <th style="padding:8px 12px;text-align:left;">Service</th>
                        <th style="padding:8px 12px;text-align:left;">Estimated Cost</th>
                    </tr>
                </thead>
                <tbody>{health_rows}</tbody>
            </table>
            </div>
            <div style="background:#e8f4e8;border-left:4px solid #4caf50;padding:14px 18px;border-radius:4px;">
                <strong>ℹ️ Recommended:</strong> {h["recommended"]}
            </div>
        </div>
    </div>

    <!-- Section 3: Insurance -->
    <div class="row mb-5" id="insurance">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">
                🛡️ {ins["heading"]}
            </h2>
            <p style="font-size:.95rem;color:#444;margin-bottom:20px;">{ins["intro"]}</p>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Top Providers for Expats</h3>
            {ins_providers}
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:14px 18px;border-radius:4px;margin-top:8px;">
                <strong>💡 Pro Tip:</strong> {ins["tip"]}
            </div>
        </div>
    </div>

    <!-- Section 4: Bank Account -->
    <div class="row mb-5" id="bank">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">
                🏦 {b["heading"]}
            </h2>
            <p style="font-size:.95rem;color:#444;margin-bottom:20px;">{b["intro"]}</p>
            <div class="row">
                <div class="col-md-6">
                    <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Recommended Banks</h3>
                    {bank_list}
                </div>
                <div class="col-md-6">
                    <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Required Documents</h3>
                    <ul style="font-size:.92rem;line-height:1.9;padding-left:20px;">{bank_req}</ul>
                </div>
            </div>
            <h3 style="font-size:17px;color:#1d2d50;margin:20px 0 12px;">Step-by-Step Process</h3>
            <ol style="font-size:.95rem;line-height:1.8;padding-left:20px;">{bank_steps}</ol>
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:14px 18px;border-radius:4px;margin-top:16px;">
                <strong>💡 Pro Tip:</strong> {b["tip"]}
            </div>
        </div>
    </div>

    <!-- Section 5: Real Estate -->
    <div class="row mb-5" id="realestate">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">
                🏠 {r["heading"]}
            </h2>
            <p style="font-size:.95rem;color:#444;margin-bottom:20px;">{r["intro"]}</p>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Ownership Options for Foreigners</h3>
            {re_options}
            <div class="row mt-4">
                <div class="col-md-6">
                    <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Purchase Process</h3>
                    <ol style="font-size:.92rem;line-height:1.8;padding-left:20px;">{re_steps}</ol>
                </div>
                <div class="col-md-6">
                    <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Typical Purchase Costs</h3>
                    <div style="overflow-x:auto;">
                    <table style="width:100%;border-collapse:collapse;font-size:.88rem;">
                        <thead>
                            <tr style="background:#1d2d50;color:#fff;">
                                <th style="padding:7px 10px;">Item</th>
                                <th style="padding:7px 10px;">Cost</th>
                            </tr>
                        </thead>
                        <tbody>{re_costs}</tbody>
                    </table>
                    </div>
                </div>
            </div>
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:14px 18px;border-radius:4px;margin-top:20px;">
                <strong>💡 Pro Tip:</strong> {r["tip"]}
            </div>
        </div>
    </div>

    <!-- E-E-A-T -->
    <div class="row mb-5">
        <div class="col-md-12">
            <div style="background:#f8f9fc;border:1px solid #e0e4f0;border-radius:6px;padding:20px 24px;">
                <h3 style="font-size:15px;color:#1d2d50;margin-bottom:8px;"><i class="fa fa-shield" style="color:#f15d30;margin-right:6px;"></i> About This Guide</h3>
                <p style="font-size:.88rem;color:#666;margin:0;">This guide is researched and maintained by the editorial team at eVisa-Card.com. Last updated: <strong>March 2026</strong>. We strive to keep all information current but visa rules, healthcare costs and property regulations change frequently. Always verify current requirements with official government sources and consult a licensed professional before making major decisions.</p>
            </div>
        </div>
    </div>

    <!-- Related Guides -->
    <div class="row mb-4">
        <div class="col-md-12">
            <h3 style="font-size:18px;color:#1d2d50;margin-bottom:16px;">Related Expat Guides</h3>
            <div class="row">
                <div class="col-md-4 mb-3"><a href="/en/expat-guides.html" class="btn btn-outline-primary btn-block">All Expat Guides</a></div>
                <div class="col-md-4 mb-3"><a href="/en/retirement-visa-guide.html" class="btn btn-outline-primary btn-block">Retirement Visa Guide</a></div>
                <div class="col-md-4 mb-3"><a href="/en/digital-nomad-visas-guide.html" class="btn btn-outline-primary btn-block">Digital Nomad Visas</a></div>
            </div>
        </div>
    </div>

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
                <p class="mt-4">© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="/en/legal-notice.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">Legal Notice</a>
                    &nbsp;|&nbsp;
                    <a href="/en/disclaimer.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">Disclaimer</a>
                </p>
            </div>
        </div>
    </div>
</footer>
<script src="../js/jquery.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>'''
    return html


# ─── Write pages ─────────────────────────────────────────────────────────────

created = 0
for slug, data in COUNTRIES.items():
    html = make_page(slug, data)
    out = os.path.join(WWW, "en", f"expat-guide-{slug}.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  WROTE: en/expat-guide-{slug}.html ({len(html)//1024}KB)")
    created += 1

print(f"\nDONE — {created} detailed EN guide pages written")
