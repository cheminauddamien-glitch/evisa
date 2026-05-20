# Visa Conditions Audit — May 2026

**Audit date**: 2026-05-20
**Scope**: 16 country expat guides on eVisa-Card.com
**Method**: WebSearch + WebFetch across official MFAs, immigration portals, and cross-referenced tertiary sources

This document is the source of truth for the `update_visa_2026.py` script that injects update banners and "Important 2026 Update" alert boxes into expat guides across 10 languages.

---

## Per-country findings

### Thailand — MAJ MAJEURE
- **Change**: Thai Cabinet decided on 19 May 2026 to cancel the 60-day visa-free scheme. New regime: **30-day visa exemption for 54 countries** (AU, AT, CA, FR, DE, JP, NZ, SG, UK, US, etc.) + **15-day exemption for 3 countries** (Maldives, Mauritius, Seychelles).
- **TDAC** (Thailand Digital Arrival Card) mandatory for all foreign nationals, replaces TM6.
- **Effective**: Cabinet decision 19 May 2026; MFA finalising implementation timeline (rollout expected mid-2026).
- **Sources**: nationthailand.com/news/policy/40066405 · thailandinsiderguide.com/en/travel-essentials/visas-and-entry-requirements

### Vietnam — MAJ MAJEURE
- **Change**: e-Visa now **90 days, multi-entry** (since Aug 2023, often missed in older guides). **6-month passport validity** strictly enforced from **1 March 2026**. **Digital Arrival Card** mandatory at Tan Son Nhat (HCMC) from **15 April 2026**, 72h pre-arrival.
- **Effective**: 1 Mar 2026 (passport rule) + 15 Apr 2026 (DAC HCMC).
- **Sources**: evisa.gov.vn · vietnam.travel

### Cambodia — MAJ MAJEURE
- **Change**: **Cambodia e-Arrival Card** mandatory within 7 days before flight (separate from e-Visa). Digital entry — no more physical passport stamps for air arrivals. Trial visa exemption for Chinese citizens (14 days) from **15 June to 15 October 2026**.
- **Effective**: e-Arrival Card already in force.
- **Sources**: evisa.gov.kh · arrival.gov.kh

### UAE — MAJ MAJEURE
- **Change**: **Mandatory health insurance** for entire stay duration from 2026. Colour scan of passport cover (in addition to data page) required. End of grace period: **automatic AED 50/day fine from visa expiry** (April 2026). 30-day minimum gap before re-entry after a 30-day tourist visa. 4 new visa categories: AI Specialist, Entertainment, Events, Job Exploration.
- **Effective**: April 2026 (grace period); health insurance throughout 2026.
- **Sources**: icp.gov.ae · u.ae

### Mexico — MAJ MAJEURE
- **Change**: **Paper FMM eliminated at major airports** (CUN, MEX). Passport now stamped with manually-written number of days (no longer guaranteed 180). Digital FMM (FMMd) downloadable post-arrival. FMM still required at land borders. **Fee 2026: MXN 983 (~USD 54)**.
- **Effective**: Pilot since 2023, generalised 2024-2025.
- **Sources**: inm.gob.mx · mx.usembassy.gov

### Panama — MAJ MAJEURE
- **Change**: **Executive Decree 196 (28 Oct 2024)**: visa exemption expanded to nationals of "visa-required" countries holding a valid multi-entry visa or residence from US/CA/UK/EU/JP/KR/SG/AU. Only validity on entry day required. 30-day max stay under this regime. USD 500 proof + return ticket.
- **Effective**: 28 October 2024.
- **Sources**: fragomen.com Panama insights · bal.com immigration-news

### Paraguay — MAJ MAJEURE
- **Change**: **Visa exemption for Venezuelans abolished** (Decree 14.609/1996 repealed) — effective **10 January 2026**. New exemptions: Malaysia (30d) and Philippines (30d) from **30 December 2025**. Trinidad & Tobago + Bahamas (90d) pending. Visa on arrival removed except Oman/Qatar.
- **Effective**: 30 Dec 2025 + 10 Jan 2026.
- **Sources**: mre.gov.py · en.wikipedia.org/wiki/Visa_policy_of_Paraguay

### Spain — MAJ MAJEURE
- **Change**: **Golden Visa ABOLISHED on 3 April 2025** (Organic Law 1/2025) — €500k real estate route closed permanently. Alternatives: Digital Nomad Visa (income ≥ 200% SMI ≈ €2,850/month in 2026), Non-Lucrative Visa, EU Blue Card.
- **Effective**: 3 April 2025.
- **Sources**: exteriores.gob.es · wise.com/us/blog/spain-golden-visa

### Georgia — MAJ MAJEURE
- **Change**: **Mandatory travel medical insurance from 1 January 2026** — minimum coverage **30,000 GEL (~USD 11,000)**, valid full stay duration, English or Georgian.
- **Effective**: 1 January 2026.
- **Sources**: mfa.gov.ge · en.wikipedia.org/wiki/Visa_policy_of_Georgia

### Portugal — MAJ MAJEURE
- **Change**: **Law 61/2025 (May 2026)**: citizenship now requires **10 years** of residence (7 years for EU/CPLP) vs 5 years before. Family reunification after 2 years. D8 Nomad Visa income min **€3,680/month**. D7 reserved for retirees/passive income (rejected for freelancers).
- **Effective**: Law 61/2025 promulgated May 2026.
- **Sources**: aima.gov.pt · getgoldenvisa.com/portugal-digital-nomad-visa

### Greece — MAJ MAJEURE
- **Change**: **Golden Visa restructured**: thresholds raised to **€800k** (Athens, Thessaloniki, Mykonos, Santorini, Corfu, Rhodes, Crete, Zakynthos), **€400k** elsewhere (min 120 m²), **€250k** only for renovation/conversion or new Start-Up Investment route. End of backdating: 5-year permit starts from issuance, not application.
- **Effective**: Thresholds in force; backdating rule changed in 2026.
- **Sources**: mfa.gr · globalcitizensolutions.com/greece-golden-visa-new-rules

### Laos — MAJ MINEURE
- **Change**: **Lao Digital Immigration Form (LDIF)** rollout since 1 Sep 2025, national deployment progressing in 2026. Separate from visa (visa rules unchanged).
- **Effective**: From 1 September 2025, ongoing rollout.
- **Sources**: laoevisa.gov.la · immigration.gov.la

### Colombia — MAJ MINEURE
- **Change**: **Financial thresholds raised +22.7%** for long visas (Digital Nomad, Retirement, M, R) — indexed to minimum wage revaluation. Mandatory health insurance for all visas. Check-Mig form still required (72h-1h pre-flight).
- **Effective**: 1 January 2026 (annual SMMLV indexation).
- **Sources**: cancilleria.gov.co · visaverge.com/travel/colombian-visa-your-complete-guide

### Costa Rica — MAJ MINEURE
- **Change**: DGME Resolution effective 1 July 2024: clarifications on Schengen C/D and US/CA multi-entry exemptions. **Anti-"perpetual tourism" bill in discussion**: overstay fine would rise from USD 100 to USD 300/month + 90-day cooling-off after using 180 days. Not yet voted.
- **Effective**: 1 July 2024 (resolution); bill pending.
- **Sources**: fragomen.com Costa Rica · costaricalaw.com

### Malaysia — À JOUR (verify)
- **Status**: Already current. **MDAC** mandatory for all foreigners since 1 Jan 2024 (verify mention in guide). Visa-free 30d extension for China + India through end 2026. Autogate open to 63 nationalities since June 2024.
- **Sources**: imi.gov.my

### Japan — À JOUR (anticipate)
- **Status**: Current. **JESTA** announced — launch postponed to **fiscal year 2028 (April 2028 – March 2029)**, NOT 2026. Estimated fee ¥2,000-6,000. No operational change in 2026. Add a short "JESTA arriving 2028" note for SEO anticipation.
- **Sources**: moj.go.jp · mofa.go.jp/j_info/visit/visa/short/novisa.html

---

## Schengen common block (Greece, Portugal, Spain)
- **EES (Entry/Exit System)**: progressive start 12 October 2025, **fully operational since 10 April 2026**. Replaces passport stamping with biometric registration (fingerprints + photo) for non-EU short stays.
- **ETIAS (travel authorisation)**: launch postponed to **Q4 2026** (€20 fee, 3-year validity, multi-entry 90/180). Mandatory ~2027 after 6-month transition.
- **As of May 2026**: ETIAS NOT yet required — do not display as mandatory in guides.
- **Sources**: home-affairs.ec.europa.eu/news/entryexit-system-will-become-fully-operational-10-april-2026-2026-03-30_en · travel-europe.europa.eu/en/etias

---

## Update strategy

For each guide we inject:
1. **Date banner** (always, all 16 × 10 = 160 files): replace "Last updated: March 2026" with "Updated: 20 May 2026 — Effective: [date]" in the local language.
2. **Important Update alert box** (11 MAJ MAJEURE countries × 10 languages = 110 files): short alert with key change, effective date, and link to official source.
3. **Minor note** (3 MAJ MINEURE × 10 = 30 files): single sentence inline note.
4. **À jour** (2 countries × 10 = 20 files): date banner only.

Implementation: `update_visa_2026.py`.
