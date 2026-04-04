#!/usr/bin/env python3
"""Generate new detailed expat guide pages: Panama, Costa Rica, Greece, Georgia, Paraguay, Laos, Cambodia"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"
BASE = "https://www.evisa-card.com"

COUNTRIES = {
    "panama": {
        "name": "Panama",
        "flag_code": "pa",
        "hero_bg": "https://flagcdn.com/w1280/pa.png",
        "capital": "Panama City",
        "currency": "Balboa / USD",
        "language": "Spanish",
        "cost": "~$1,200–2,500/month",
        "title": "Complete Expat Guide Panama 2026 — Live & Retire in Panama",
        "meta": "Complete guide to living in Panama as an expat in 2026. Pensionado visa, residency, healthcare, health insurance, bank accounts and property buying for foreigners.",
        "intro": "Panama offers a unique combination: a dollarised economy, excellent healthcare, zero taxes on foreign-source income, a tropical climate and one of the world's most famous retirement visa programmes — the Pensionado. It is consistently ranked as a top retirement destination in the Americas.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Pensionado Visa", "Panama's flagship retirement visa. Requires a guaranteed lifetime pension of $1,000/month from a government or private pension. No age minimum. Permanent residency from day one. No stay requirement. Includes a long list of discounts (20–50%) on healthcare, restaurants, entertainment."),
                ("Friendly Nations Visa", "For citizens of 50+ 'friendly nations' (including USA, EU, UK, Canada, Australia). Requires $200,000 in a Panama bank account OR employment with a Panamanian company OR business ownership. Permanent residency."),
                ("Self-Employed / Business Visa", "For investors or business owners. Capital investment of $40,000+ (with at least 3 Panamanian employees). 2-year permit, path to permanent residency."),
                ("Digital Nomad Visa (Short-Stay Permit)", "Panama introduced a Remote Worker Permit in 2021. Monthly income proof $36,000+/year. 9-month renewable permit. Not full residency."),
                ("Tourist Visa / Stamp", "US, EU, UK, Canadian citizens: 180 days visa-free. Many nomads use Panama as a hub and renew easily with a short border run."),
            ],
            "steps": [
                "Choose your visa category (Pensionado for retirees, Friendly Nations for qualified nationals)",
                "Hire a Panamanian immigration lawyer (~$1,500–3,000 in legal fees)",
                "Gather documents: passport, pension letter, police clearance, health certificate, bank statements",
                "Apostille and translate all foreign documents to Spanish",
                "Submit application to the National Immigration Service (SNM)",
                "Initial temporary residency issued (~3–6 months processing)",
                "Permanent residency card (Carnet) issued — usually within 6 months",
                "Apply for cedula (national ID) at the Civil Registry",
                "Obtain RUC (tax ID) at the DGI if conducting business",
            ],
            "tip": "The Pensionado Visa is one of the world's best retirement programmes — permanent residency with a modest $1,000/month pension, no age limit, and remarkable discounts on healthcare and daily expenses. It can be obtained with a pension as small as a US Social Security benefit.",
        },
        "health": {
            "heading": "Healthcare in Panama",
            "public": "Panama has a two-tier public system: Social Security (CSS) for formal workers and public hospitals (MINSA) for the general population. Pensionado visa holders can access CSS at discounted rates. Quality in Panama City is good; rural areas are underserved.",
            "private": "Panama City has excellent private hospitals: Hospital Nacional, Hospital Punta Pacifica (affiliated with Johns Hopkins), Clínica Hospital San Fernando, Hospital Chiriquí (David). English-speaking doctors are common. Costs are significantly lower than the US.",
            "costs": [
                ("Private GP consultation", "$40–80"),
                ("Specialist consultation", "$80–200"),
                ("Emergency room (private)", "$200–800"),
                ("Hospitalisation (private, per night)", "$400–1,500"),
                ("Dental cleaning", "$40–80"),
                ("Major dental work", "50–70% cheaper than US"),
            ],
            "recommended": "Most expats use a combination of private health insurance and occasional CSS access (if eligible via Pensionado). Panama City's private hospitals offer US-quality care at 30–50% of US prices.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "Health insurance is not legally required for residency in Panama but is strongly recommended. Hospitalisation and specialist care at private hospitals can be expensive without coverage. Pensionado holders receive a 20% discount on private medical services.",
            "providers": [
                ("Pan-American Life Insurance (PALIC)", "Major regional insurer with strong Panama network. Widely accepted at private hospitals. From ~$150/month."),
                ("BlueCross BlueShield (Panama)", "Popular with US expats. Good network of hospitals. From ~$180/month."),
                ("ASSA Compañía de Seguros", "Panama-based insurer. Comprehensive plans, dental included. From ~$120/month."),
                ("Cigna Global", "International plan covering Panama and worldwide, including US. From ~$150/month."),
                ("Aetna International", "Good for US citizens who need US coverage too. From ~$200/month."),
            ],
            "tip": "Pensionado visa holders receive a 20% discount on private healthcare services — keep this in mind when comparing insurance plans. Even with insurance, you'll pay a fraction of US costs for the same procedures.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Panama",
            "intro": "Panama is a major banking hub in Latin America. However, post-FATCA compliance has made account opening stricter, especially for US citizens. A Panamanian bank account is essential for visa purposes (Friendly Nations) and daily life.",
            "banks": [
                ("Banco Nacional de Panamá", "State-owned bank. Most accessible for new residents. Competitive rates. Good for retirement pension deposits."),
                ("BAC Credomatic", "Largest private bank in Central America. English service, good digital banking. Popular with expats."),
                ("Banistmo (HSBC affiliate)", "Good for international transfers, especially to/from Europe. English support available."),
                ("Multibank", "Expat-friendly, good for Friendly Nations visa applicants (requires bank balance proof). Good English service."),
                ("Global Bank", "Relatively easy account opening. Good for Pensionado applicants."),
            ],
            "requirements": [
                "Valid passport",
                "Panamanian residency card (Carnet) or tourist visa",
                "Proof of address (rental contract or utility bill)",
                "Proof of income (pension letter, employment contract or investment proof)",
                "Personal and professional reference letters (2 each, some banks)",
                "Initial deposit ($500–5,000 depending on bank)",
            ],
            "process": [
                "Obtain your residency card or at minimum a tourist entry stamp",
                "Visit bank branch in person (no online opening for non-residents)",
                "Present all documents including reference letters",
                "Compliance interview (standard KYC process)",
                "Account opened within 1–4 weeks (compliance checks take time)",
            ],
            "tip": "US citizens face the most scrutiny due to FATCA reporting requirements — some banks decline US applicants entirely. Multibank and Global Bank are more open to US expats. Non-US expats typically have a smoother experience.",
        },
        "realestate": {
            "heading": "Buying Property in Panama",
            "intro": "Panama has among the most foreigner-friendly property laws in Latin America. Foreigners have the same property rights as Panamanian citizens. No restrictions on type of property, location or amount owned. The property market is dollarised.",
            "options": [
                ("Freehold (Titled Property)", "Full ownership, same rights as citizens. Most condos, houses and commercial properties. Registered at the Public Registry."),
                ("Rights of Possession (ROP)", "Untitled land where occupants have use rights but not formal title. Common in rural and coastal areas. Higher risk — verify carefully."),
                ("Pensionado Property Exemption", "First purchase of primary residence by a Pensionado is exempt from certain taxes. Confirm with your lawyer."),
            ],
            "process": [
                "Hire a Panamanian real estate lawyer (abogado)",
                "Obtain your RUC (tax ID) from the DGI",
                "Sign a Promise to Purchase contract (Promesa de Compraventa) — pay 10% deposit",
                "Lawyer conducts title search at the Public Registry",
                "Verify no liens, encumbrances or property tax debts",
                "Sign the final Purchase Deed (Escritura de Compraventa) before a Notary",
                "Register at the Public Registry (Registro Público) — takes 2–8 weeks",
            ],
            "costs": [
                ("Transfer tax (ITBMS)", "2% of higher of sale price or registered value"),
                ("Notary and legal fees", "1–2% of purchase price"),
                ("Public Registry fee", "~$500–1,500"),
                ("Annual property tax", "0% up to $120,000 value (primary residence exempt to $300,000 for new construction)"),
                ("Agent commission", "3–5% (paid by seller)"),
            ],
            "tip": "Panama's primary residence tax exemption is excellent — new properties up to $300,000 are exempt from property tax for 20 years. Always verify titled property (vs Rights of Possession) before purchase. Coastal property near the beach requires additional due diligence on concession rights.",
        },
    },
    "costa-rica": {
        "name": "Costa Rica",
        "flag_code": "cr",
        "hero_bg": "https://flagcdn.com/w1280/cr.png",
        "capital": "San José",
        "currency": "Costa Rican Colón (CRC) / USD",
        "language": "Spanish",
        "cost": "~$1,500–2,800/month",
        "title": "Complete Expat Guide Costa Rica 2026 — Live & Retire in Costa Rica",
        "meta": "Complete guide to living in Costa Rica as an expat in 2026. Pensionado visa, rentista visa, healthcare, CAJA insurance, bank accounts and property for foreigners.",
        "intro": "Costa Rica — Pura Vida — is a long-standing favourite of North American and European expats. Stable democracy, no standing army, excellent healthcare, lush biodiversity and a well-developed expat infrastructure make it one of the easiest countries in Latin America to settle in.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Pensionado (Retiree Visa)", "Requires a guaranteed lifetime pension of $1,000/month from a government or private source. Permanent residency. Must spend 183 days/year in Costa Rica to maintain status. Popular with US and Canadian retirees."),
                ("Rentista (Passive Income Visa)", "For those with passive income (not pension): $2,500/month OR one-time bank deposit of $60,000. 2-year permit, renewable. Must reside 183 days/year."),
                ("Inversionista (Investor Visa)", "Investment of $150,000+ in Costa Rican property, business or government bonds. Permanent residency. No minimum stay requirement."),
                ("Digital Nomad Visa", "For remote workers. Income $3,000/month (individual) or $4,000/month (family). 1-year permit, renewable once. No local work allowed."),
                ("Temporary Resident (Work)", "Sponsored by a Costa Rican employer. For skilled professionals. 2-year permit."),
            ],
            "steps": [
                "Hire a Costa Rican immigration lawyer (budget $1,500–3,000)",
                "Gather documents: passport, pension/income proof, police clearance, birth certificate, marriage certificate if applicable",
                "Apostille and notarise all foreign documents; translate to Spanish",
                "Submit to DGME (Dirección General de Migración y Extranjería)",
                "Receive initial conditional residency within 3–12 months",
                "Enrol in the CAJA (public health system) — mandatory for all residents",
                "Obtain your DIMEX card (Documento de Identidad Migratoria para Extranjeros)",
                "After 3 years of temporary residency, apply for permanent residency",
            ],
            "tip": "The Pensionado visa requires $1,000/month — even a modest US Social Security benefit often qualifies. The mandatory CAJA enrolment (~$50–150/month) gives access to Costa Rica's excellent public health system.",
        },
        "health": {
            "heading": "Healthcare in Costa Rica",
            "public": "Costa Rica's CAJA (Caja Costarricense de Seguro Social) is widely regarded as one of the best public healthcare systems in Latin America. All legal residents must enrol and pay monthly contributions (~$50–150/month based on income). Covers doctor visits, hospitalisation, surgery, maternity and prescription medicines.",
            "private": "Private clinics and hospitals operate alongside the public system. CIMA Hospital (San José), Clínica Bíblica, Clínica Católica and Hospital Clínica Bíblica offer English-speaking doctors and US-comparable standards at 40–60% lower costs.",
            "costs": [
                ("CAJA monthly contribution (resident)", "~$50–150/month (income-based)"),
                ("CAJA consultation (covered)", "Free or nominal co-pay"),
                ("Private GP consultation", "$60–100"),
                ("Private specialist", "$80–200"),
                ("Private hospitalisation (per night)", "$400–1,200"),
                ("Dental cleaning (private)", "$60–100"),
            ],
            "recommended": "Enrol in CAJA immediately — it's mandatory and provides comprehensive coverage for a modest monthly fee. Add a private supplementary plan for faster access to specialists and English-speaking doctors.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "While the CAJA public system is comprehensive, wait times for non-emergency specialist care and some procedures can be long. Supplementary private insurance provides immediate access to private hospitals and is also useful for the period before CAJA enrolment is active.",
            "providers": [
                ("INS (Instituto Nacional de Seguros)", "State insurer. Mandatory for car insurance; also offers health plans. From ~$80/month."),
                ("Aseguradora del Istmo (ADISA)", "Private supplementary plans. Strong hospital network. From ~$100/month."),
                ("Cigna Global", "International plan for new arrivals and frequent travellers. From ~$120/month."),
                ("AXA Global Healthcare", "Comprehensive worldwide coverage. Good for those splitting time between CR and home country. From ~$130/month."),
                ("BUPA International", "Premium plan with repatriation coverage. Good for US citizens. From ~$150/month."),
            ],
            "tip": "Combine mandatory CAJA (~$100/month) with a private supplementary plan ($100–150/month) for the best of both worlds — comprehensive public coverage plus fast-track private access for specialist care.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Costa Rica",
            "intro": "A Costa Rican bank account is needed to pay rent, utilities and CAJA contributions, and to receive local salary or pension transfers. The process has become more regulated but remains manageable.",
            "banks": [
                ("Banco de Costa Rica (BCR)", "State bank. Most expat-friendly, good English service in Escazú/San José. Accepts tourist visas for basic accounts."),
                ("Banco Nacional de Costa Rica", "Largest state bank. Lowest fees. Extensive branch network throughout the country."),
                ("BAC San José (BAC Credomatic)", "Best digital banking. Popular with younger expats and digital nomads. Requires DIMEX card."),
                ("Scotiabank Costa Rica", "Canadian bank, familiar to North American expats. International wire capabilities."),
                ("Prival Bank", "Good for higher-net-worth expats and investors. English-speaking staff."),
            ],
            "requirements": [
                "Valid passport",
                "DIMEX card (for residents) — OR tourist entry for basic account at state banks",
                "Proof of address (rental contract or utility bill)",
                "Proof of income (pension letter, employment contract, bank statements)",
                "Costa Rican phone number",
            ],
            "process": [
                "Visit bank branch in person",
                "For state banks: some accept tourist status for a basic account",
                "Present all documents and complete KYC form",
                "Account typically opened within 1–5 business days",
                "Receive debit card and online banking access",
            ],
            "tip": "Banco de Costa Rica in Escazú and Los Yoses (San José) have dedicated expat advisors with strong English skills. State banks (BCR, Banco Nacional) are the most accessible for new arrivals without a DIMEX card.",
        },
        "realestate": {
            "heading": "Buying Property in Costa Rica",
            "intro": "Costa Rica has no restrictions on foreign property ownership — foreigners have the same rights as citizens. The property market is well-established, with a large inventory of expat-friendly properties particularly in the Central Valley, Guanacaste, Manuel Antonio and the Southern Zone.",
            "options": [
                ("Titled (Freehold) Property", "Full ownership registered at the National Registry. Standard for most urban and suburban properties. Most secure form of ownership."),
                ("Concession Land (Maritime Zone)", "Land within 200m of the ocean. The first 50m from the high tide line is public and inalienable. The next 150m requires a concession from the municipality. Foreigners can hold concessions but must have 5 years legal residency or go through a Costa Rican company."),
                ("Rights of Way / Possession Rights", "Untitled land. Very risky for foreigners — avoid unless you have expert legal advice."),
            ],
            "process": [
                "Hire a Costa Rican real estate lawyer (not optional)",
                "Obtain an RNPN (National Property Registry) title search",
                "Check for liens, easements, back taxes, survey maps",
                "Sign a Purchase Option contract (Opción de Compra) — pay $5,000–20,000 deposit",
                "Complete due diligence: survey, environmental restrictions, zoning",
                "Sign Escritura de Compraventa (Purchase Deed) before a Notary Public",
                "Register at the National Registry (Registro Nacional)",
                "Pay transfer taxes and notary fees at closing",
            ],
            "costs": [
                ("Property transfer tax", "1.5% of registered value"),
                ("Notary fees", "1.25–1.5% of sale price"),
                ("National Registry recording fee", "~0.5%"),
                ("Lawyer fees", "1–2% of purchase price"),
                ("Annual property tax (Impuesto sobre Bienes Inmuebles)", "0.25% of appraised value"),
                ("Annual municipality luxury tax (if applicable)", "0.25–0.55% on values over ¢133M (~$245,000)"),
            ],
            "tip": "Always verify the title at the National Registry (Registro Nacional) yourself or via your lawyer before signing anything. Maritime zone properties near the beach require special legal expertise — do not purchase without understanding the concession terms.",
        },
    },
    "greece": {
        "name": "Greece",
        "flag_code": "gr",
        "hero_bg": "https://flagcdn.com/w1280/gr.png",
        "capital": "Athens",
        "currency": "Euro (€)",
        "language": "Greek",
        "cost": "~$1,500–3,000/month",
        "title": "Complete Expat Guide Greece 2026 — Live & Retire in Greece",
        "meta": "Complete guide to living in Greece as an expat in 2026. Financially independent person visa, Golden Visa, Greek Non-Dom tax, healthcare, bank accounts and property for foreigners.",
        "intro": "Greece offers a compelling combination: Mediterranean lifestyle, ancient culture, excellent climate, affordable cost of living by EU standards, world-class cuisine and a strong expat community. The Financially Independent Person visa and a generous non-dom tax regime make it increasingly attractive to retirees and remote workers.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Financially Independent Person Visa (FIP)", "For non-EU citizens with passive income. Requires €2,000/month (€250 per additional adult, €150 per child). No work in Greece allowed. 2-year renewable permit. Must spend 183 days/year in Greece."),
                ("Digital Nomad Visa (DNV)", "For remote workers with non-Greek employers/clients. Income ≥€3,500/month. 1-year permit, renewable once. Fast processing."),
                ("Golden Visa", "Investment residency: real estate ≥€250,000 (higher in Athens, Thessaloniki: ≥€800,000 since Aug 2023). No stay requirement. 5-year renewable. Includes family."),
                ("Non-Dom Tax Regime", "Flat €100,000/year tax on all foreign-source income (regardless of actual income amount). Ideal for high-income individuals. Apply in the first year of residency. Valid 15 years."),
                ("EU/EEA Citizen", "Free movement rights. Register at the local municipality. No investment or income requirement."),
            ],
            "steps": [
                "Apply for the appropriate visa at your local Greek consulate",
                "Upon arriving in Greece: obtain an AFM (Greek tax number) at the local Tax Office (Εφορία)",
                "Open a Greek bank account (required for most visa types)",
                "Register at the local Municipality (Δήμος)",
                "Apply for residence permit at the Aliens and Immigration Division (Υπηρεσία Αλλοδαπών)",
                "Apply for AMKA (social security number) at a KEP service centre",
                "Enrol in EOPYY (public health insurance) if eligible",
                "Apply for Non-Dom tax status if applicable (within the first year)",
            ],
            "tip": "Greece's Non-Dom tax regime (flat €100,000/year on all foreign income) is one of Europe's most attractive for wealthy individuals. If your foreign income exceeds ~€400,000/year, this regime saves significantly compared to standard Greek income tax rates.",
        },
        "health": {
            "heading": "Healthcare in Greece",
            "public": "Greece has a universal public health system (ESY — Ethniko Systima Ygeias). Legal residents with an AMKA social security number can access public hospitals and health centres (Κέντρα Υγείας). The system has faced austerity-related challenges but has improved significantly. Wait times can be long.",
            "private": "Private clinics and hospitals in Athens and Thessaloniki (Hygeia, MITERA, Metropolitan Hospital, Henry Dunant) offer high-quality English-language care. Quality in major cities is excellent; rural areas rely more on the public system.",
            "costs": [
                ("Public hospital consultation (with AMKA)", "€5–20 co-payment"),
                ("Private GP consultation", "€60–100"),
                ("Private specialist", "€80–200"),
                ("Private hospitalisation (per night)", "€300–1,000"),
                ("Dental cleaning (private)", "€60–100"),
                ("Prescription medicines", "Partially subsidised for AMKA holders"),
            ],
            "recommended": "Obtain your AMKA number as soon as possible — this gives access to the public system. Add private health insurance for faster specialist access and English-speaking doctors.",
        },
        "insurance": {
            "heading": "Supplementary Health Insurance",
            "intro": "Private health insurance is not legally required for FIP or DNV visa holders (but you must demonstrate coverage for the visa application). Even after obtaining residency and AMKA access, private insurance is recommended for faster service and English-speaking doctors.",
            "providers": [
                ("Interamerican (Achmea Greece)", "Greece's largest private health insurer. Comprehensive hospital networks. From ~€80/month."),
                ("Allianz Hellas", "Strong network, good international coverage for travellers. From ~€90/month."),
                ("AXA Greece", "Solid plans with dental options. From ~€75/month."),
                ("Cigna Global", "International plan for new arrivals and frequent travellers. From ~€120/month."),
                ("AXA Global Healthcare", "Worldwide coverage, ideal for those not yet resident. From ~€130/month."),
            ],
            "tip": "For visa application purposes, you need proof of health insurance before arriving. Cigna Global or AXA Global Healthcare are easy to obtain internationally. Once resident with AMKA, consider switching to a local plan (Interamerican, Allianz Hellas) for better value.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Greece",
            "intro": "A Greek bank account is required for paying rent, utilities, taxes and visa-related financial proof. An AFM (Greek tax number) is mandatory before account opening.",
            "banks": [
                ("National Bank of Greece (NBG)", "Largest bank. Good English service in Athens and tourist areas. Strong online banking."),
                ("Alpha Bank", "Modern digital platform. English-speaking branches in Athens. Popular with expats."),
                ("Piraeus Bank", "Widespread branch network. Good for property-related transactions. Online banking in English."),
                ("Eurobank", "Strong digital banking. Good for investment and savings products. English support."),
                ("Revolut / Wise", "Not Greek banks but widely used by expats for daily transactions and international transfers. Cannot be used for visa applications."),
            ],
            "requirements": [
                "Valid passport or EU ID",
                "AFM (Greek tax number) — mandatory",
                "Proof of address in Greece (rental contract or utility bill)",
                "Proof of income or funds",
                "Greek phone number or SIM",
            ],
            "process": [
                "Obtain your AFM first at the local Tax Office (Εφορία) — bring passport and proof of address",
                "Visit bank branch in person",
                "Present passport, AFM and proof of address",
                "Account opened same day in most cases",
                "Online banking activated within 2–5 days",
            ],
            "tip": "Alpha Bank's Kolonaki (Athens) and Thessaloniki city centre branches have dedicated English-speaking staff for expats and investors. Always get your AFM before visiting the bank — account opening is refused without it.",
        },
        "realestate": {
            "heading": "Buying Property in Greece",
            "intro": "EU/EEA citizens can freely buy property in Greece. Non-EU citizens can also buy (with some restrictions in border regions requiring special permits). Greece's Golden Visa requires minimum property investment of €250,000 (€800,000 in Athens, Thessaloniki and certain islands since August 2023).",
            "options": [
                ("Freehold Purchase", "Full ownership. Standard for all residential and commercial property. No restrictions for most nationalities."),
                ("Golden Visa Property", "Minimum €250,000 (€800,000 in prime zones) qualifies for Golden Visa. Can be one property or multiple smaller ones totalling the threshold."),
                ("Off-Plan Purchase", "Buying from developers. Lower prices but construction risk. Growing market in Athens, Crete and the islands."),
            ],
            "process": [
                "Obtain an AFM (Greek tax number)",
                "Hire a Greek real estate lawyer (αδικηγόρος)",
                "Sign a Preliminary Contract (Προσύμφωνο) and pay 10% deposit",
                "Lawyer checks title at the Land Registry (Κτηματολόγιο) for encumbrances",
                "Arrange finance or international bank transfer",
                "Sign the Final Notarial Deed (Συμβολαιογραφική Πράξη) before a Notary",
                "Register the transfer at the Land Registry",
            ],
            "costs": [
                ("Property transfer tax", "3.09% of objective (tax) value"),
                ("Notary fees", "0.8–1% of property value"),
                ("Land Registry fee", "0.475–0.575%"),
                ("Lawyer fees", "1–2%"),
                ("ENFIA (annual property tax)", "Variable — typically €200–2,000/year depending on location and size"),
                ("Agent commission", "2% + VAT (paid by buyer in most cases)"),
            ],
            "tip": "Golden Visa threshold changes (Aug 2023) raised the minimum to €800,000 in Athens, Thessaloniki, Mykonos and Santorini. Other regions remain at €250,000. Verify which threshold applies to your target location before negotiating.",
        },
    },
    "georgia": {
        "name": "Georgia",
        "flag_code": "ge",
        "hero_bg": "https://flagcdn.com/w1280/ge.png",
        "capital": "Tbilisi",
        "currency": "Georgian Lari (GEL)",
        "language": "Georgian, Russian, English",
        "cost": "~$700–1,500/month",
        "title": "Complete Expat Guide Georgia 2026 — Live & Work in Georgia (Caucasus)",
        "meta": "Complete guide to living in Georgia (Caucasus) as an expat in 2026. Visa-free 365 days, residency by investment, flat 20% tax, healthcare, bank accounts and property for foreigners.",
        "intro": "Georgia (the Caucasus country) has emerged as one of the most popular destinations for digital nomads, entrepreneurs and expats worldwide. The reasons: 365-day visa-free entry for 95+ nationalities, a flat 20% income tax (1% for small businesses), ultra-low cost of living, fast internet and a young, cosmopolitan capital in Tbilisi.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Visa-Free Stay (365 days)", "Citizens of 95+ countries (including USA, EU, UK, Canada, Australia) can stay 365 consecutive days without a visa. No income or investment requirement. The simplest option for digital nomads."),
                ("Residency by Investment", "Investment in Georgian real estate or business. Minimum $100,000 in real estate OR $300,000 in business. Temporary residency for 6 years, then permanent."),
                ("Employment Residency", "For those employed by a Georgian company. Employer applies on your behalf. Temporary residency."),
                ("Permanent Residency", "After 6 years of continuous legal residence. Or by marriage to a Georgian citizen (3 years)."),
                ("Citizenship by Investment", "Exceptional status granted by Presidential decree. Requires significant economic contribution. Rare but possible."),
            ],
            "steps": [
                "Citizens of 95+ countries: simply enter Georgia with a valid passport — no pre-arrival visa needed",
                "Register your stay at the House of Justice (სამართლის სახლი) if staying 30+ days",
                "Obtain a Personal Identification Number (personal ID) at the Public Service Hall",
                "Open a Georgian bank account (requires passport + Georgian phone number)",
                "Register for tax purposes at the Revenue Service (rs.ge) if earning Georgian income",
                "For residency: apply at the Civil Registry Agency with investment proof",
            ],
            "tip": "Georgia's 1% flat tax on annual revenue up to 500,000 GEL (~$180,000) for small status businesses makes it extraordinarily attractive for freelancers and entrepreneurs. Register as a 'Small Business' (მცირე ბიზნესი) or 'Virtual Zone Company' for IT businesses (0% corporate tax, 5% dividend tax).",
        },
        "health": {
            "heading": "Healthcare in Georgia",
            "public": "Georgia has a Universal Healthcare programme (UHC) that provides basic coverage to all Georgian citizens and legal residents. Foreigners without residency are not covered. Emergency treatment is available to all, but costs must be paid privately.",
            "private": "Private hospitals in Tbilisi are modern and affordable: Mediclub Georgia, Todua Medical Centre, Acad. O. Gudushauri Hospital, American Medical Center. Quality varies — major hospitals in Tbilisi are good; rural areas have limited facilities.",
            "costs": [
                ("Private GP consultation", "30–80 GEL (~$11–29)"),
                ("Specialist consultation", "50–150 GEL (~$18–55)"),
                ("Emergency (private hospital)", "100–500 GEL (~$36–182)"),
                ("Hospitalisation (private, per night)", "150–600 GEL (~$55–218)"),
                ("Dental cleaning", "30–70 GEL (~$11–25)"),
                ("Basic blood tests", "20–50 GEL (~$7–18)"),
            ],
            "recommended": "Healthcare is very cheap in Georgia. Even without insurance, paying out of pocket for routine care is affordable. International health insurance is recommended primarily for serious illness, surgery or medical evacuation.",
        },
        "insurance": {
            "heading": "Health Insurance in Georgia",
            "intro": "Health insurance is not required for visa-free stays in Georgia. However, it is strongly recommended given the limitations of the public health system and the need for medical evacuation coverage for serious conditions.",
            "providers": [
                ("GPI Insurance (Georgia)", "Georgia's largest local insurer. Affordable plans from ~80 GEL/month. Good network of local hospitals."),
                ("Aldagi (Vienna Insurance Group)", "Strong local insurer. Comprehensive plans with dental. From ~100 GEL/month."),
                ("Imedi L (local)", "Good value for routine care. Popular with local expat community. From ~70 GEL/month."),
                ("Cigna Global", "International plan for worldwide coverage including medical evacuation. From ~$80/month."),
                ("SafetyWing", "Nomad-focused insurance. Affordable, flexible. Good for short-to-medium stays. From ~$45/month."),
            ],
            "tip": "SafetyWing is popular with the large digital nomad community in Tbilisi — very affordable and easy to sign up for. For longer-term residents, a local Georgian plan (GPI, Aldagi) provides better coverage at lower cost.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Georgia",
            "intro": "Georgia has one of the most foreigner-friendly banking environments in the world. Bank accounts can be opened quickly, often same-day, with just a passport — no residency required.",
            "banks": [
                ("TBC Bank", "Georgia's largest bank. Excellent English app. Fastest account opening (sometimes 15 minutes in-branch). Multi-currency accounts. Highly recommended."),
                ("Bank of Georgia", "Second-largest bank. Good digital banking. English-speaking staff. Multi-currency (GEL, USD, EUR)."),
                ("Credo Bank", "Good for small businesses and entrepreneurs. Competitive FX rates."),
                ("Liberty Bank", "Widespread branches. Good for everyday transactions."),
                ("Wise / Revolut", "Not Georgian banks but widely used for international transfers. Complement your local TBC or Bank of Georgia account."),
            ],
            "requirements": [
                "Valid passport (that's it — no residency required for basic accounts)",
                "Georgian phone number (for 2FA — buy a SIM at the airport for ~$5)",
                "In some cases: proof of address (rental contract)",
            ],
            "process": [
                "Buy a Georgian SIM card (Magti or Geocell) at the airport",
                "Visit any TBC Bank or Bank of Georgia branch",
                "Present passport and phone number",
                "Account opened same day — typically within 30–60 minutes",
                "Receive debit card immediately or within 1–2 days",
                "Activate mobile banking via the app",
            ],
            "tip": "TBC Bank is the clear expat favourite in Georgia — the app is in English, account opening takes 15–30 minutes with just your passport, and you get a multi-currency account (GEL + USD + EUR) from day one. No other country in the world makes banking this easy for foreigners.",
        },
        "realestate": {
            "heading": "Buying Property in Georgia",
            "intro": "Georgia has no restrictions on foreign property ownership. Foreigners can buy any type of property — apartments, houses, commercial — with the same rights as Georgian citizens. The market is transparent, prices are low, and the process is quick. Investment ≥$100,000 qualifies for residency.",
            "options": [
                ("Freehold Purchase", "Full ownership. No restrictions. Registered at the National Agency of Public Registry (NAPR). Most secure and straightforward."),
                ("Residency Qualification", "Property investment ≥$100,000 qualifies for a 6-year temporary residency permit."),
                ("Off-Plan / New Development", "Popular in Tbilisi, Batumi and Gudauri. Developers offer flexible payment plans. Batumi (Black Sea) is a popular short-term rental market."),
            ],
            "process": [
                "No lawyer strictly required (system is very simple) but highly recommended for foreigners",
                "Agree price with seller — a real estate agent is optional",
                "Visit the House of Justice (სამართლის სახლი) together",
                "Present passports of buyer and seller",
                "Sign the purchase agreement and pay",
                "Registration completed on-the-spot or within 1–4 business days",
                "Receive new ownership certificate",
            ],
            "costs": [
                ("Property registration fee", "~50–200 GEL (~$18–73) — extremely low"),
                ("Notarisation (if applicable)", "~100–300 GEL"),
                ("Agent commission", "2–5% (if applicable)"),
                ("Annual property tax", "0.05–1% depending on owner income and property value"),
                ("No real estate transfer tax", "—"),
            ],
            "tip": "Georgia has one of the world's simplest property purchase systems. Two people walk into a House of Justice, sign a document and walk out with a new ownership certificate — sometimes in under an hour. No lawyers, no notaries, no complex due diligence required (though still recommended). Batumi has a booming short-term rental market with yields of 8–12%.",
        },
    },
    "paraguay": {
        "name": "Paraguay",
        "flag_code": "py",
        "hero_bg": "https://flagcdn.com/w1280/py.png",
        "capital": "Asunción",
        "currency": "Paraguayan Guaraní (PYG) / USD",
        "language": "Spanish, Guaraní",
        "cost": "~$700–1,400/month",
        "title": "Complete Expat Guide Paraguay 2026 — Live & Retire in Paraguay",
        "meta": "Complete guide to living in Paraguay as an expat in 2026. Permanent residency, tax residency, territorial tax system, healthcare, bank accounts and property for foreigners.",
        "intro": "Paraguay is Latin America's best-kept secret for expats seeking a low-tax, low-cost destination. The country operates on a territorial tax system (only local income is taxed), permanent residency is obtainable in 3 months, and the cost of living is among the lowest in South America. Asunción is a modern, safe capital with a growing expat community.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("Permanent Residency (Residencia Permanente)", "Paraguay's flagship path: deposit $5,500 in a Paraguayan bank + monthly income proof of $1,250 (or pension). Permanent residency issued within 60–90 days. No minimum stay requirement once obtained."),
                ("Simple Residency (Residencia Simple)", "Temporary residency via employment, business or investment. Path to permanent residency."),
                ("Jubilado (Retiree)", "For retirees with a pension of $1,250/month. Permanent residency. Popular with North American and European retirees."),
                ("Investor Visa", "Investment in Paraguayan business or real estate. No strict minimum but typically $70,000+ demonstrated."),
                ("Visa-Free Entry", "US, EU, UK and many other nationalities: 90 days visa-free. Renewable with a short border run."),
            ],
            "steps": [
                "Hire a Paraguayan immigration lawyer (budget $500–2,000 total)",
                "Open a Paraguayan bank account and make the $5,500 deposit",
                "Gather documents: passport, police clearance, birth certificate, proof of income",
                "Apostille all foreign documents and translate to Spanish",
                "Submit application to MIGRACIONES (Immigration Department)",
                "Receive temporary certificate within 2–4 weeks",
                "Obtain permanent residency cedula within 60–90 days",
                "Apply for tax residency certificate (for international tax purposes) — optional but valuable",
            ],
            "tip": "Paraguay's permanent residency is one of the fastest and cheapest in the world ($5,500 deposit + lawyer fees). Combined with the territorial tax system (no tax on foreign-source income), it's a powerful tax residency option for international entrepreneurs and investors.",
        },
        "health": {
            "heading": "Healthcare in Paraguay",
            "public": "Paraguay's public health system (IPS — Instituto de Previsión Social) covers registered workers and their families. Quality is inconsistent — good in Asunción, very limited in rural areas. Emergency hospitals are available but often overcrowded.",
            "private": "Private hospitals in Asunción provide the best care: Hospital Bautista, Centro Médico La Costa, Hospital Adventista. Quality is acceptable for routine and moderate care, but complex procedures may require travel to Brazil or Argentina. Costs are very low by international standards.",
            "costs": [
                ("Private GP consultation", "$30–60"),
                ("Specialist consultation", "$50–120"),
                ("Emergency room (private)", "$100–400"),
                ("Hospitalisation (private, per night)", "$200–600"),
                ("Dental cleaning", "$30–60"),
                ("Major dental work", "40–60% cheaper than US"),
            ],
            "recommended": "Most expats use private healthcare in Asunción and maintain international health insurance for serious conditions requiring treatment in Brazil, Argentina or the US.",
        },
        "insurance": {
            "heading": "Health Insurance in Paraguay",
            "intro": "Private health insurance is not required for residency in Paraguay. However, given the limitations of the local healthcare system for serious conditions, international health insurance is strongly recommended.",
            "providers": [
                ("La Consolidada", "Paraguay-based insurer. Affordable local plans. Good for routine care in Asunción. From ~$100/month."),
                ("Mapfre Paraguay", "Regional insurer with local hospital network. From ~$120/month."),
                ("Cigna Global", "International plan covering Paraguay plus worldwide. Essential for serious conditions requiring travel. From ~$100/month."),
                ("SafetyWing", "Nomad insurance. Affordable and flexible. Good for shorter stays. From ~$45/month."),
                ("AXA Global Healthcare", "Comprehensive international plan. Good for high-net-worth expats. From ~$130/month."),
            ],
            "tip": "Given that complex medical cases in Paraguay often require travel to São Paulo (Brazil) or Buenos Aires (Argentina), make sure your international health insurance covers treatment in neighbouring countries, not just Paraguay.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Paraguay",
            "intro": "A Paraguayan bank account is required for the residency deposit ($5,500) and for daily transactions. The process is relatively straightforward compared to other Latin American countries.",
            "banks": [
                ("Banco Continental", "Paraguay's largest private bank. Good English support. Recommended for residency applications."),
                ("Banco Itaú Paraguay", "Brazilian-owned. Strong digital banking, international connections. Popular with Brazilian expats."),
                ("Banco GNB Paraguay", "Good for account opening. Accepts foreigners with passport only at some branches."),
                ("BBVA Paraguay", "International bank. Good for wire transfers to/from Spain and Latin America."),
                ("Banco Nacional de Fomento", "State bank. Most accessible but limited digital services."),
            ],
            "requirements": [
                "Valid passport",
                "Proof of address in Paraguay (rental contract or hotel bill)",
                "Police clearance certificate (some banks)",
                "Proof of income or purpose of account",
                "Initial deposit ($100–$5,500 depending on account type)",
            ],
            "process": [
                "Visit bank branch in person",
                "For residency deposit: open a fixed-term savings account with $5,500",
                "Standard account opening takes 1–3 business days",
                "Receive account number and access for wire transfers",
                "Mobile banking available after account activation",
            ],
            "tip": "Banco Continental is the most popular bank for residency purposes among expats. The $5,500 deposit must remain in the account until residency is approved — it earns a small amount of interest in the meantime.",
        },
        "realestate": {
            "heading": "Buying Property in Paraguay",
            "intro": "Paraguay has no restrictions on foreign property ownership. The market is extremely affordable — land and properties in Asunción cost a fraction of comparable Latin American cities. The legal process is straightforward.",
            "options": [
                ("Freehold Purchase", "Full ownership. No restrictions for foreigners. Standard for all property types."),
                ("Agricultural Land", "Foreigners can own agricultural land. Paraguay has become a major soy and cattle farming country, with expat farmers from Brazil, Germany and Mennonite communities owning large tracts."),
                ("Off-Plan / Development", "Growing in Asunción's Villa Morra and Carmelitas neighbourhoods. Lower prices with developer payment plans."),
            ],
            "process": [
                "Obtain a RUC (tax ID) at the SET (tax authority)",
                "Hire a Paraguayan notary (escribano) — manages the whole process",
                "Conduct a title search at the General Directorate of Public Registries",
                "Verify property is free of liens and back taxes (IBI)",
                "Sign the Escritura Pública (purchase deed) before the notary",
                "Register at the Property Registry",
            ],
            "costs": [
                ("Property transfer tax", "1.5% of sale price"),
                ("Notary fees", "1.5–2% of sale price"),
                ("Property Registry fee", "~$200–500"),
                ("Annual property tax (IBI)", "Very low — typically $100–500/year"),
                ("Agent commission", "3–5% (paid by seller)"),
            ],
            "tip": "Paraguay is one of South America's most affordable property markets. A 2-bedroom apartment in Asunción's Carmelitas neighbourhood costs $80,000–150,000 — comparable areas in Buenos Aires or Santiago are 3–5× more expensive. Land prices in the countryside start at $500/hectare.",
        },
    },
    "laos": {
        "name": "Laos",
        "flag_code": "la",
        "hero_bg": "https://flagcdn.com/w1280/la.png",
        "capital": "Vientiane",
        "currency": "Lao Kip (LAK) / Thai Baht / USD",
        "language": "Lao",
        "cost": "~$600–1,200/month",
        "title": "Complete Expat Guide Laos 2026 — Live & Work in Laos",
        "meta": "Complete guide to living in Laos as an expat in 2026. Laos visa, business visa, temporary residence, healthcare, bank accounts and property for foreigners.",
        "intro": "Laos is Southeast Asia's most peaceful and unhurried country. Luang Prabang, Vang Vieng and Vientiane attract expats seeking a quiet lifestyle, stunning natural landscapes and ultra-low cost of living. Infrastructure is limited compared to Thailand or Vietnam, but for those seeking tranquillity, Laos is incomparable.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("E-Visa / Visa on Arrival (30 days)", "Available for most nationalities. Cost $35–42. Extendable once for 30 days at the Immigration Department in Vientiane or Luang Prabang. Most common entry for short-term stays."),
                ("Business Visa (B3)", "For those working or investing in Laos. Sponsored by a Lao company or organisation. 1-year multiple-entry. Renewable. Most common for working expats."),
                ("Temporary Residence Permit (TRC)", "For employees of registered companies or organisations. 1–5 years. Requires sponsor. Work permit must be obtained alongside."),
                ("NGO / UN / Embassy Staff", "Specific visa categories for humanitarian, diplomatic and international organisation staff."),
                ("Retirement / Long-Term Stay", "Laos has no formal retirement visa. Most retired expats use repeated business visas (B3) or stay on 30-day tourist entries renewed by short trips to Thailand."),
            ],
            "steps": [
                "Apply for e-visa online at laoevisa.gov.la OR obtain visa on arrival at major airports/border crossings",
                "For long-term stay: secure employment or business sponsorship in Laos",
                "Employer applies for work permit at the Ministry of Labour",
                "Apply for Temporary Residence Card (TRC) at the Department of Immigration",
                "Register your residence at the local Police station within 24 hours of arrival (your hotel/guesthouse does this automatically)",
                "Obtain a Lao tax code if earning Lao-source income",
            ],
            "tip": "Many long-term expats in Laos use a 'border run' to Thailand every 30–60 days to renew their tourist entry. This is a grey area — immigration officers increasingly notice multiple entries. A Business Visa (B3) with a sponsoring organisation provides much more stability.",
        },
        "health": {
            "heading": "Healthcare in Laos",
            "public": "Laos's public healthcare system is among the least developed in Southeast Asia. Public hospitals are severely underfunded and understaffed. Expats should avoid them for anything beyond basic first aid. Emergency cases are routinely evacuated to Thailand.",
            "private": "Private medical care in Vientiane (Mahosot International, Australian Embassy Clinic, Lao-French Hospital, Mittaphab Hospital) is adequate for routine care and minor emergencies. For anything serious, medical evacuation to Khon Kaen or Bangkok (Thailand) is standard.",
            "costs": [
                ("Private GP consultation (Vientiane)", "$30–60"),
                ("Private specialist", "$50–100"),
                ("Emergency treatment", "$100–500"),
                ("Medical evacuation to Bangkok", "$5,000–25,000 (without insurance)"),
                ("Dental cleaning (local private)", "$20–50"),
                ("Prescription medicines", "Very cheap locally; limited availability"),
            ],
            "recommended": "Medical evacuation insurance is ESSENTIAL in Laos. Even a serious accident in Vientiane will likely require evacuation to Thailand. This is non-negotiable for expats in Laos.",
        },
        "insurance": {
            "heading": "Health Insurance in Laos",
            "intro": "Given the very limited local healthcare infrastructure, international health insurance with medical evacuation coverage is not optional — it is a necessity for any expat in Laos. Evacuation to Thailand costs $5,000–25,000 without coverage.",
            "providers": [
                ("BUPA International / BUPA Global", "Highly recommended for Laos. Strong medical evacuation coverage. From ~$150/month."),
                ("Cigna Global", "International plan with excellent evacuation and Thailand coverage. From ~$100/month."),
                ("AXA Global Healthcare", "Good worldwide plan with medical evacuation. From ~$120/month."),
                ("AIG Travel Guard", "Good for short-term stays. Strong emergency and evacuation coverage. From ~$60/month."),
                ("SafetyWing", "Budget nomad insurance. Covers medical evacuation. Most affordable option. From ~$45/month."),
            ],
            "tip": "Your policy MUST include medical evacuation to Thailand. This is the single most important coverage for expats in Laos — verify explicitly that your policy covers helicopter and air ambulance evacuation across the Thai border.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Laos",
            "intro": "A Lao bank account is useful for receiving salary in Laos and paying local expenses. The process is straightforward but limited digital banking is available. Many expats use Thai bank accounts for international transfers.",
            "banks": [
                ("Banque pour le Commerce Extérieur Lao (BCEL)", "Largest bank. Most foreigner-friendly. English service in Vientiane. Good for USD accounts."),
                ("Lao Development Bank", "State bank. Good interest rates on LAK deposits. Limited English service."),
                ("Joint Development Bank (JDB)", "Good for business banking. Partners with Chinese banks."),
                ("Bangkok Bank (Laos branch)", "Thai bank with branches in Vientiane. Excellent for transfers to Thailand."),
                ("ANZ Laos (via BCEL)", "Good for Australian expats needing international connections."),
            ],
            "requirements": [
                "Valid passport",
                "Visa or TRC (tourist visa may be accepted at BCEL)",
                "Proof of address (rental contract)",
                "Purpose of account statement (some banks)",
                "Initial deposit ($100–500)",
            ],
            "process": [
                "Visit BCEL or Bangkok Bank in Vientiane",
                "Present passport and visa",
                "Complete account opening form",
                "Account opened within 1–3 business days",
                "Online banking is basic — primarily used for ATM withdrawals and local transfers",
            ],
            "tip": "BCEL is the clear choice for expats in Laos — it has the broadest ATM network and the most foreigner-friendly service. Open both a LAK account and a USD account to handle both local and international transactions.",
        },
        "realestate": {
            "heading": "Property in Laos for Foreigners",
            "intro": "Foreigners CANNOT own land in Laos. This is constitutionally prohibited. However, foreigners can lease land for up to 50 years (with possible renewal), hold ownership of structures (not land), and invest through a Lao company with local partners.",
            "options": [
                ("Long-term Lease (50 years)", "Land can be leased to foreigners for up to 50 years, renewable. This is the main option for property use. Common for villas, guesthouses and commercial properties."),
                ("Lao Company Structure", "A Lao company (with at least 1 Lao partner) can hold land. Common for investors and business owners. Requires a trusted local partner."),
                ("Condominium (limited)", "A small number of approved condominium developments allow foreign ownership of individual units. Verify with the developer and Ministry of Land."),
            ],
            "process": [
                "Identify a suitable property through a local agent",
                "Hire a Lao lawyer familiar with foreign investment law",
                "Negotiate lease terms with the landowner",
                "Draft a Land Use Lease Agreement (50 years, 2× renewable = 150 years in practice)",
                "Register the lease at the National Land Management Authority (NLMA)",
                "Obtain a Construction Permit if building on the land",
            ],
            "costs": [
                ("Lease registration fee", "1–2% of lease value"),
                ("Lawyer fees", "$500–2,000"),
                ("Annual land use tax", "Very low — typically $100–500/year for residential"),
                ("Construction costs", "Very low — $200–400/m² for basic construction"),
            ],
            "tip": "Long-term leases in Laos are common and legally well-established for foreigners. The key risk is title — ensure the land has a proper Title Certificate (not just occupancy rights) before signing any lease agreement. Always work with a reputable Lao lawyer.",
        },
    },
    "cambodia": {
        "name": "Cambodia",
        "flag_code": "kh",
        "hero_bg": "https://flagcdn.com/w1280/kh.png",
        "capital": "Phnom Penh",
        "currency": "Cambodian Riel (KHR) / USD",
        "language": "Khmer",
        "cost": "~$700–1,400/month",
        "title": "Complete Expat Guide Cambodia 2026 — Live & Retire in Cambodia",
        "meta": "Complete guide to living in Cambodia as an expat in 2026. E-visa, ordinary residence visa, business visa, healthcare, bank accounts and property for foreigners.",
        "intro": "Cambodia is one of Southeast Asia's most accessible expat destinations — ultra-low cost of living, a fully dollarised economy (USD used everywhere), relatively straightforward residency via business or ordinary visa, and Phnom Penh and Siem Reap offer surprisingly vibrant expat communities.",
        "visa": {
            "heading": "Visa & Residency Options",
            "types": [
                ("E-Visa (T class / Tourist)", "Available online at evisa.gov.kh. 30 days, single entry, extendable once for 30 days. Cost: $30 + $6 processing fee."),
                ("Ordinary Visa (E class)", "Available on arrival or online. 30 days, can be extended multiple times. The 'E' visa is the basis for most long-term stays. Extensions: 1 month, 3 months, 6 months, 1 year (multiple entry possible on 1-year extension)."),
                ("Business Visa (EB class)", "For those conducting business. Extendable for 1 year multiple entry. Popular with expat business owners and remote workers."),
                ("Retirement Extension", "No specific retirement visa, but those 55+ can apply for a 1-year 'retirement' extension of their ordinary visa. Requires proof of $1,500/month income or $50,000 in bank."),
                ("CAMKIDS Visa (for families)", "Specific category for foreign family members of Cambodian nationals."),
            ],
            "steps": [
                "Apply for E-Visa online before travel OR obtain visa on arrival at Phnom Penh / Siem Reap airports",
                "For long-term stay: extend your E-class visa at an immigration agent or the Department of Immigration",
                "Most expats use an immigration agent (~$200–350/year for 1-year multiple-entry EB extension)",
                "Register your address at the local sangkat (commune) office",
                "Obtain a Tax Identification Number (TIN) at the General Department of Taxation if working",
            ],
            "tip": "Cambodia's visa system is very foreigner-friendly. A 1-year multiple-entry business extension (~$300 via an agent) is the de facto 'digital nomad visa'. No minimum stay requirement, no income proof needed at most immigration offices.",
        },
        "health": {
            "heading": "Healthcare in Cambodia",
            "public": "Cambodia's public healthcare system is very limited. Most public hospitals lack basic equipment and medicines. Expats should use private hospitals for all care beyond minor issues.",
            "private": "Private hospitals in Phnom Penh (Royal Rattanak Hospital, Sen Sok International University Hospital, Naga Clinic, Sunrise Japan Hospital) provide adequate to good care. Siem Reap has Royal Angkor International Hospital. For serious conditions, Bangkok is the standard evacuation destination (~1 hour by plane).",
            "costs": [
                ("Private GP consultation", "$25–60"),
                ("Specialist consultation", "$50–100"),
                ("Emergency room (private Phnom Penh)", "$100–500"),
                ("Hospitalisation (private, per night)", "$200–600"),
                ("Dental cleaning", "$25–50"),
                ("Medical evacuation to Bangkok", "$5,000–20,000 (without insurance)"),
            ],
            "recommended": "As with Laos, medical evacuation insurance is essential in Cambodia. For anything beyond routine care, Bangkok's Bumrungrad or Samitivej hospitals are the standard destination.",
        },
        "insurance": {
            "heading": "Health Insurance in Cambodia",
            "intro": "International health insurance is not required for any visa category in Cambodia but is essential for safety. The combination of limited local facilities and proximity to excellent Thai hospitals makes evacuation coverage critical.",
            "providers": [
                ("Pacific Cross Cambodia", "Local expat-focused insurer. Good network of Phnom Penh private hospitals. From ~$600/year."),
                ("BUPA Global", "Strong medical evacuation and Thailand coverage. From ~$1,500/year."),
                ("Cigna Global", "International plan with broad coverage. Good for frequent travellers. From ~$1,000/year."),
                ("AXA Global Healthcare", "Comprehensive worldwide plan with repatriation. From ~$1,200/year."),
                ("SafetyWing", "Budget nomad insurance. Covers evacuation. Popular in the expat community. From ~$45/month."),
            ],
            "tip": "Ensure your plan explicitly covers medical evacuation to Thailand. Pacific Cross Cambodia is a good local option and is widely accepted at Phnom Penh's private hospitals.",
        },
        "bank": {
            "heading": "Opening a Bank Account in Cambodia",
            "intro": "Cambodia's fully dollarised economy makes banking straightforward — USD accounts are the norm. Account opening is relatively easy for foreigners, even on tourist visa at some banks.",
            "banks": [
                ("ABA Bank", "Cambodia's most popular bank among expats. Excellent English app, ABA PAY digital payments, easy account opening. Most recommended."),
                ("Canadia Bank", "Good for business accounts and larger transactions. English service available."),
                ("ACLEDA Bank", "Largest bank by branches. Good for transfers within Cambodia and to Vietnam/Laos."),
                ("FTB Bank (Foreign Trade Bank)", "State bank. Good for USD transfers. Strong relationship with Chinese banks."),
                ("Wing Money", "Mobile money service (not a full bank) used for daily transactions. Very popular."),
            ],
            "requirements": [
                "Valid passport",
                "Cambodian visa (tourist may be accepted at ABA Bank)",
                "Proof of address (guesthouse or rental contract)",
                "Cambodian phone number (for app)",
                "Initial deposit ($100–500 for most account types)",
            ],
            "process": [
                "Visit ABA Bank branch in Phnom Penh or Siem Reap",
                "Present passport and visa",
                "Complete account opening form",
                "Account opened same day in most cases",
                "Download ABA Mobile app — one of the best banking apps in Southeast Asia",
            ],
            "tip": "ABA Bank is the unanimous favourite among Phnom Penh expats — the app is excellent, account opening is fast (sometimes with just a tourist visa), and the service is in English. Open a USD account as the primary account for daily use.",
        },
        "realestate": {
            "heading": "Buying Property in Cambodia",
            "intro": "Foreigners CANNOT own land in Cambodia, but the law was amended in 2010 to allow foreigners to own condominium units on the 2nd floor and above (not ground floor or land). Workarounds include 50-year long-term leases and Cambodian company structures.",
            "options": [
                ("Condominium Ownership (freehold)", "Foreign ownership permitted from the 2nd floor upward in approved condominium buildings. Growing inventory in Phnom Penh. Sihanoukville and Siem Reap also have options."),
                ("Long-term Lease (50 years, renewable)", "Land and houses can be leased for 50 years, renewable for another 50. Common for villas and townhouses."),
                ("Cambodian Company (99% practical)", "Many foreigners form a Cambodian company (with a Cambodian nominee director holding 51% of shares on paper). Legal but carries risk if done improperly."),
                ("LMAP-Titled Land via Cambodian spouse", "Land held in a Cambodian spouse's name. Common but risky without legal protections."),
            ],
            "process": [
                "Hire a reputable Cambodian real estate lawyer",
                "Verify the title (LMAP Title — the most secure type; avoid Soft Title)",
                "For condos: check building is registered with MLMUPC as foreigner-eligible",
                "Sign a Memorandum of Understanding (MOU) and pay deposit",
                "Lawyer conducts due diligence: title, permits, developer reputation",
                "Sign the Sale and Purchase Agreement (SPA)",
                "Transfer at the relevant authority and receive your ownership certificate",
            ],
            "costs": [
                ("Transfer tax (registration fee)", "4% of property value"),
                ("Stamp duty", "0.1% of registered value"),
                ("Notarisation", "~$200–500"),
                ("Lawyer fees", "$1,000–3,000"),
                ("Annual property tax", "0.1% of assessed value above $25,000"),
                ("Annual rental income tax (if renting out)", "14% withholding tax"),
            ],
            "tip": "Only buy condos in Cambodia — they are the only truly secure form of foreign property ownership under Cambodian law. Leasehold villas and company-held land carry significant legal risk. In Phnom Penh, Boeung Keng Kang (BKK1) and Tonle Bassac are the most expat-friendly neighbourhoods.",
        },
    },
}

# ─── Reuse the make_page function from gen_detailed_expat_guides.py ──────────

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

    visa_rows = "".join(
        f'<tr><td style="font-weight:600;width:35%;padding:8px 12px;border-bottom:1px solid #eee;">{t}</td>'
        f'<td style="padding:8px 12px;border-bottom:1px solid #eee;">{desc}</td></tr>'
        for t, desc in v["types"]
    )
    visa_steps = "".join(f'<li style="margin-bottom:8px;">{step}</li>' for step in v["steps"])
    health_rows = "".join(
        f'<tr><td style="padding:6px 12px;border-bottom:1px solid #eee;">{item}</td>'
        f'<td style="padding:6px 12px;border-bottom:1px solid #eee;font-weight:600;">{cost}</td></tr>'
        for item, cost in h["costs"]
    )
    ins_providers = "".join(
        f'<div style="background:#f8f9fc;border-radius:6px;padding:14px 18px;margin-bottom:10px;">'
        f'<strong style="color:#1d2d50;">{prov}</strong><br/>'
        f'<span style="font-size:.9rem;color:#555;">{desc}</span></div>'
        for prov, desc in ins["providers"]
    )
    bank_list = "".join(
        f'<div style="border-left:3px solid #f15d30;padding:8px 14px;margin-bottom:8px;">'
        f'<strong>{bank}</strong> — <span style="color:#555;font-size:.9rem;">{desc}</span></div>'
        for bank, desc in b["banks"]
    )
    bank_req = "".join(f'<li>{req}</li>' for req in b["requirements"])
    bank_steps = "".join(f'<li style="margin-bottom:6px;">{step}</li>' for step in b["process"])
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

    return f'''<!DOCTYPE html>
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
    <div class="row mb-5">
        <div class="col-md-12">
            <div style="background:#fff;border:1px solid #e0e4f0;border-radius:6px;padding:20px 24px;">
                <h2 style="font-size:16px;margin-bottom:12px;color:#1d2d50;">📋 Table of Contents</h2>
                <ol style="margin:0;padding-left:20px;font-size:.95rem;">
                    <li><a href="#visa" style="color:#f15d30;">Visa &amp; Residency</a></li>
                    <li><a href="#health" style="color:#f15d30;">Healthcare</a></li>
                    <li><a href="#insurance" style="color:#f15d30;">Health Insurance</a></li>
                    <li><a href="#bank" style="color:#f15d30;">Bank Account</a></li>
                    <li><a href="#realestate" style="color:#f15d30;">Buying Property</a></li>
                </ol>
            </div>
        </div>
    </div>
    <div class="row mb-5" id="visa">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">🛂 {v["heading"]}</h2>
            <div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:.92rem;margin-bottom:24px;"><thead><tr style="background:#1d2d50;color:#fff;"><th style="padding:10px 12px;text-align:left;">Visa Type</th><th style="padding:10px 12px;text-align:left;">Details</th></tr></thead><tbody>{visa_rows}</tbody></table></div>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Step-by-Step Process</h3>
            <ol style="font-size:.95rem;line-height:1.8;padding-left:20px;">{visa_steps}</ol>
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:14px 18px;border-radius:4px;margin-top:16px;"><strong>💡 Pro Tip:</strong> {v["tip"]}</div>
        </div>
    </div>
    <div class="row mb-5" id="health">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">🏥 {h["heading"]}</h2>
            <div class="row mb-4">
                <div class="col-md-6"><div style="background:#f0f7ff;border-radius:6px;padding:18px;height:100%;"><h3 style="font-size:16px;color:#1d2d50;margin-bottom:10px;">Public Healthcare</h3><p style="font-size:.92rem;color:#555;margin:0;">{h["public"]}</p></div></div>
                <div class="col-md-6"><div style="background:#f0fff4;border-radius:6px;padding:18px;height:100%;"><h3 style="font-size:16px;color:#1d2d50;margin-bottom:10px;">Private Healthcare</h3><p style="font-size:.92rem;color:#555;margin:0;">{h["private"]}</p></div></div>
            </div>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Typical Costs</h3>
            <div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:.92rem;margin-bottom:16px;"><thead><tr style="background:#1d2d50;color:#fff;"><th style="padding:8px 12px;text-align:left;">Service</th><th style="padding:8px 12px;text-align:left;">Cost</th></tr></thead><tbody>{health_rows}</tbody></table></div>
            <div style="background:#e8f4e8;border-left:4px solid #4caf50;padding:14px 18px;border-radius:4px;"><strong>ℹ️ Recommended:</strong> {h["recommended"]}</div>
        </div>
    </div>
    <div class="row mb-5" id="insurance">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">🛡️ {ins["heading"]}</h2>
            <p style="font-size:.95rem;color:#444;margin-bottom:20px;">{ins["intro"]}</p>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Top Providers for Expats</h3>
            {ins_providers}
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:14px 18px;border-radius:4px;margin-top:8px;"><strong>💡 Pro Tip:</strong> {ins["tip"]}</div>
        </div>
    </div>
    <div class="row mb-5" id="bank">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">🏦 {b["heading"]}</h2>
            <p style="font-size:.95rem;color:#444;margin-bottom:20px;">{b["intro"]}</p>
            <div class="row">
                <div class="col-md-6"><h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Recommended Banks</h3>{bank_list}</div>
                <div class="col-md-6"><h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Required Documents</h3><ul style="font-size:.92rem;line-height:1.9;padding-left:20px;">{bank_req}</ul></div>
            </div>
            <h3 style="font-size:17px;color:#1d2d50;margin:20px 0 12px;">Step-by-Step Process</h3>
            <ol style="font-size:.95rem;line-height:1.8;padding-left:20px;">{bank_steps}</ol>
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:14px 18px;border-radius:4px;margin-top:16px;"><strong>💡 Pro Tip:</strong> {b["tip"]}</div>
        </div>
    </div>
    <div class="row mb-5" id="realestate">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">🏠 {r["heading"]}</h2>
            <p style="font-size:.95rem;color:#444;margin-bottom:20px;">{r["intro"]}</p>
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Options for Foreigners</h3>
            {re_options}
            <div class="row mt-4">
                <div class="col-md-6"><h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Purchase Process</h3><ol style="font-size:.92rem;line-height:1.8;padding-left:20px;">{re_steps}</ol></div>
                <div class="col-md-6"><h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">Typical Costs</h3><div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:.88rem;"><thead><tr style="background:#1d2d50;color:#fff;"><th style="padding:7px 10px;">Item</th><th style="padding:7px 10px;">Cost</th></tr></thead><tbody>{re_costs}</tbody></table></div></div>
            </div>
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:14px 18px;border-radius:4px;margin-top:20px;"><strong>💡 Pro Tip:</strong> {r["tip"]}</div>
        </div>
    </div>
    <div class="row mb-5">
        <div class="col-md-12">
            <div style="background:#f8f9fc;border:1px solid #e0e4f0;border-radius:6px;padding:20px 24px;">
                <h3 style="font-size:15px;color:#1d2d50;margin-bottom:8px;"><i class="fa fa-shield" style="color:#f15d30;margin-right:6px;"></i> About This Guide</h3>
                <p style="font-size:.88rem;color:#666;margin:0;">This guide is researched and maintained by the editorial team at eVisa-Card.com. Last updated: <strong>March 2026</strong>. Always verify current requirements with official government sources and consult a licensed professional before making major decisions.</p>
            </div>
        </div>
    </div>
    <div class="row mb-4">
        <div class="col-md-12">
            <h3 style="font-size:18px;color:#1d2d50;margin-bottom:16px;">Related Expat Guides</h3>
            <div class="row">
                <div class="col-md-4 mb-3"><a href="/en/expat-guides.html" class="btn btn-outline-primary btn-block">All Expat Guides</a></div>
                <div class="col-md-4 mb-3"><a href="/en/retirement-visa-guide.html" class="btn btn-outline-primary btn-block">Retirement Visa Guide</a></div>
                <div class="col-md-4 mb-3"><a href="/en/cheapest-countries-to-retire-abroad-2026.html" class="btn btn-outline-primary btn-block">Cheapest Countries to Retire</a></div>
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


created = 0
for slug, data in COUNTRIES.items():
    html = make_page(slug, data)
    out = os.path.join(WWW, "en", f"expat-guide-{slug}.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  WROTE: en/expat-guide-{slug}.html ({len(html)//1024}KB)")
    created += 1

print(f"\nDONE — {created} new detailed EN guide pages written")
