#!/usr/bin/env python3
"""
gen_subpages_batch_b.py
Generates 3 sub-pages per country for 10 countries:
  {country}-visa-requirements.html
  {country}-visa-fees.html
  {country}-visa-processing-time.html
Output dir: www/en/
"""

import os
import textwrap

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ── Country data ──────────────────────────────────────────────────────────────
COUNTRIES = {
    "vietnam": {
        "label": "Vietnam",
        "flag": "vn",
        "visa_page": "visa-vietnam.html",
        "fee": "USD 25",
        "stay": "90 days",
        "processing": "3 business days",
        "portal": "evisa.xuatnhapcanh.gov.vn",
        "portal_url": "https://evisa.xuatnhapcanh.gov.vn",
        "visa_type": "eVisa",
        "free_note": "45-day visa-free for France, Germany, UK and 10 other nationalities",
        "eligibility": "All nationalities",
        "entry": "Single or multiple entry",
        "currency": "VND (Vietnamese Dong)",
        "region": "Southeast Asia",
        "schengen": False,
        "extra_fees": [
            ("90-day eVisa (single or multiple entry)", "USD 25"),
            ("Consular visa (varies by type)", "USD 25–135"),
            ("Overstay fine (per day)", "USD 5–10"),
            ("Emergency processing (expedited)", "Not available"),
            ("Work permit (employer applied)", "Variable"),
            ("Temporary Residence Card", "USD 20–100"),
        ],
        "req_rows": [
            ("Valid passport", "Minimum 6 months validity beyond entry; at least 1 blank page"),
            ("Digital passport photo", "Recent, plain background, 4×6 cm"),
            ("Passport bio-data scan", "Clear colour scan, all corners visible"),
            ("Entry & exit dates", "Planned travel dates within 90-day validity"),
            ("Accommodation details", "Hotel booking or host address"),
            ("Payment card", "Visa/MasterCard for USD 25 fee"),
            ("Return/onward ticket", "Recommended; may be checked at border"),
        ],
        "processing_rows": [
            ("Standard eVisa (online)", "3 business days"),
            ("Consular visa (embassy)", "5–10 business days"),
            ("Peak season (Tet, summer)", "Up to 5 business days"),
            ("Visa-free entry (13 nationalities)", "Instant — no application needed"),
            ("Work permit (employer-applied)", "15–30 working days"),
            ("Temporary Residence Card", "7–14 working days after work permit"),
        ],
        "faq_req": [
            ("What documents are required for a Vietnam eVisa in 2026?",
             "You need a valid passport (6+ months validity), a recent digital passport photo, a scan of your passport bio-data page, planned entry/exit dates, accommodation details, and a credit or debit card to pay the USD 25 fee online at evisa.xuatnhapcanh.gov.vn."),
            ("Is there a minimum passport validity for Vietnam?",
             "Yes. Your passport must be valid for at least 6 months beyond your intended entry date and have at least one blank page for the entry stamp. Renew your passport before applying if it does not meet these requirements."),
            ("Do children need a separate Vietnam eVisa?",
             "Yes. Each traveller, including children, requires their own eVisa. Children should be listed on the application with their own passport details. The fee is the same USD 25 regardless of age."),
            ("Can I extend my Vietnam eVisa inside the country?",
             "eVisa extensions are possible inside Vietnam at an Immigration Department office, but are not guaranteed. A simpler option is to do a border run and re-enter with a new eVisa. Citizens of visa-free countries can extend their 45-day stay once for an additional 45 days."),
        ],
        "faq_fee": [
            ("How much does a Vietnam eVisa cost in 2026?",
             "The Vietnam eVisa fee is USD 25 for both single-entry and multiple-entry options. Payment is made online by credit or debit card (Visa/MasterCard) during the application at evisa.xuatnhapcanh.gov.vn. The fee is non-refundable even if the application is refused."),
            ("Are there any additional fees when entering Vietnam?",
             "No airport tax is separately charged to tourists as it is included in the airfare. There is no visa-on-arrival counter fee for eVisa holders. However, overstaying your visa incurs a fine of approximately USD 5–10 per day and may result in a ban from re-entry."),
            ("Is the Vietnam eVisa fee the same for all nationalities?",
             "Yes. Vietnam charges a flat USD 25 fee for all nationalities applying online for the 90-day eVisa. Citizens of 13 visa-free countries (UK, France, Germany etc.) pay nothing because they do not need to apply at all."),
            ("Can I get a refund if my Vietnam eVisa is denied?",
             "No. The USD 25 Vietnam eVisa fee is non-refundable regardless of the outcome. To minimise the risk of refusal, ensure your passport is valid, your photo meets specifications, and all information matches your travel document exactly."),
        ],
        "faq_proc": [
            ("How long does it take to get a Vietnam eVisa?",
             "The standard processing time for a Vietnam eVisa is 3 business days. Applications submitted on weekdays before noon (Vietnam time) often receive a decision within 72 hours. During peak holidays such as Tet (Lunar New Year) processing may take up to 5 business days."),
            ("Can I get a Vietnam eVisa faster than 3 days?",
             "Vietnam does not currently offer an official expedited eVisa service. If you need to travel urgently, contact the nearest Vietnamese embassy or consulate for a same-day or next-day consular visa, which may be available at higher cost."),
            ("What happens if my Vietnam eVisa is not approved in time?",
             "If your eVisa has not been approved and your departure is imminent, you should contact the Vietnamese embassy. Alternatively, citizens of the 13 visa-free countries (France, Germany, UK, Japan, etc.) can enter without a visa for 45 days with no advance application required."),
            ("Does the 3-day processing include weekends?",
             "No. Processing time is counted in business days, excluding Vietnamese public holidays and weekends. Apply at least 5 calendar days before travel to account for weekends and any unexpected delays. The eVisa portal shows the estimated approval date when you submit."),
        ],
        "howto_req": [
            ("Check eligibility", "Visit evisa.xuatnhapcanh.gov.vn and verify whether your nationality qualifies for visa-free entry or must apply for a 90-day eVisa."),
            ("Prepare your documents", "Gather a valid passport (6+ months validity), a recent digital passport photo with plain background, and a clear scan of your passport bio-data page."),
            ("Complete the online application", "Fill in the eVisa form with your personal details, travel dates, and accommodation address. Double-check all information matches your passport exactly."),
            ("Pay the fee", "Pay the USD 25 non-refundable fee using Visa or MasterCard. Save your application receipt number for tracking."),
            ("Download and print your eVisa", "Within 3 business days you will receive an approval email. Download the PDF eVisa and print a copy to present at the Vietnamese port of entry alongside your passport."),
        ],
        "howto_fee": [
            ("Determine your visa category", "Check whether you qualify for visa-free entry (45 days for 13 nationalities) or need to purchase a 90-day eVisa for USD 25 at evisa.xuatnhapcanh.gov.vn."),
            ("Choose entry type", "Select single-entry or multiple-entry on the application form. Both cost the same USD 25, so multiple-entry is usually the better choice if you plan to visit nearby countries."),
            ("Prepare a valid payment card", "Use a Visa or MasterCard credit or debit card. Ensure international payments are enabled on your card before starting the application to avoid payment failures."),
            ("Pay online securely", "Enter your card details on the official government portal. You will receive an email receipt. Never pay through third-party agents who charge additional service fees."),
            ("Keep proof of payment", "Save the payment confirmation and application reference number. You will need this to check the status of your eVisa and to resolve any payment disputes."),
        ],
        "howto_proc": [
            ("Apply early", "Submit your Vietnam eVisa application at least 5 calendar days before your travel date to allow for the 3-business-day processing period plus weekends."),
            ("Track your application", "Use your application reference number on the official portal to check the real-time status of your eVisa. You will also receive an email notification when approved."),
            ("Check your email spam folder", "The eVisa approval is sent by email. If you do not see it within 3 business days, check your spam or junk folder before contacting the immigration department."),
            ("Download and verify your eVisa", "When approved, download the PDF and verify that all details (name, passport number, travel dates) match your passport. Errors must be corrected before travel."),
            ("Present your eVisa at the border", "Print your eVisa PDF and present it alongside your valid passport at the Vietnamese port of entry. Immigration officers will stamp your passport for the approved stay duration."),
        ],
    },

    "indonesia": {
        "label": "Indonesia",
        "flag": "id",
        "visa_page": "visa-indonesia.html",
        "fee": "IDR 500,000 (~USD 32)",
        "stay": "30 days (extendable once)",
        "processing": "1–2 business days",
        "portal": "molina.imigrasi.go.id",
        "portal_url": "https://molina.imigrasi.go.id",
        "visa_type": "eVOA (electronic Visa on Arrival)",
        "free_note": "Visa-free for ASEAN nationals; eVOA for most other nationalities",
        "eligibility": "86+ nationalities eligible for eVOA",
        "entry": "Single entry",
        "currency": "IDR (Indonesian Rupiah)",
        "region": "Southeast Asia",
        "schengen": False,
        "extra_fees": [
            ("eVOA (30-day single entry)", "IDR 500,000 (~USD 32)"),
            ("Extension fee (30 more days)", "IDR 500,000 (~USD 32)"),
            ("Visa on Arrival at airport", "IDR 500,000 (~USD 32)"),
            ("Social/cultural visa (B211)", "USD 50–100 (varies by consulate)"),
            ("Work permit (RPTKA)", "Variable (employer-sponsored)"),
            ("KITAS (limited stay permit)", "USD 100–200 government fee"),
        ],
        "req_rows": [
            ("Valid passport", "Minimum 6 months validity; at least 1 blank page"),
            ("Passport-style photo", "Recent, white background, 3.5×4.5 cm"),
            ("Return/onward ticket", "Proof of departure from Indonesia"),
            ("Accommodation proof", "Hotel booking or host invitation"),
            ("Payment card", "Visa/MasterCard for IDR 500,000 (~USD 32)"),
            ("Travel insurance", "Recommended; required for some visa types"),
            ("Sufficient funds", "Bank statement or credit card showing adequate funds"),
        ],
        "processing_rows": [
            ("eVOA online (molina.imigrasi.go.id)", "1–2 business days"),
            ("Visa on Arrival (at airport)", "15–30 minutes upon arrival"),
            ("Social/cultural visa B211 (consulate)", "3–5 business days"),
            ("Work permit / KITAS", "30–60 working days"),
            ("Extension of stay (imigrasi office)", "3–5 working days"),
            ("Peak season (Christmas, Bali high season)", "Up to 3 business days"),
        ],
        "faq_req": [
            ("What documents do I need for Indonesia eVOA in 2026?",
             "You need a valid passport (6+ months validity), a recent passport-style photo, a confirmed return or onward ticket showing you will leave Indonesia within 30 days, proof of accommodation, and a Visa or MasterCard to pay IDR 500,000 (~USD 32) online at molina.imigrasi.go.id."),
            ("Do I need travel insurance for Indonesia?",
             "Travel insurance is strongly recommended and may be required for certain visa categories such as the social/cultural visa (B211A). For the eVOA, it is not mandatory but advisable given the cost of medical care in remote Indonesian islands."),
            ("Can I extend my Indonesia eVOA?",
             "Yes. The 30-day eVOA can be extended once for an additional 30 days at a local immigration office (Kantor Imigrasi) in Indonesia. The extension fee is also IDR 500,000. You must apply before your current permit expires."),
            ("Is the Indonesia eVOA the same as a Visa on Arrival?",
             "They are similar but different. The eVOA is applied online before travel at molina.imigrasi.go.id and avoids airport queues. The traditional Visa on Arrival (VOA) is purchased at designated airport counters upon arrival and costs the same IDR 500,000. Both allow 30 days extendable once."),
        ],
        "faq_fee": [
            ("How much does the Indonesia eVOA cost in 2026?",
             "The Indonesia eVOA costs IDR 500,000 (approximately USD 32) for a 30-day single-entry stay. If you need to extend your stay for another 30 days, a further IDR 500,000 extension fee applies at a local immigration office. Payment is by credit or debit card online."),
            ("Are there extra fees for the Indonesia eVOA?",
             "The government fee is IDR 500,000. Third-party visa agencies may charge an additional service fee of USD 10–30. To avoid extra costs, always apply directly through the official government portal at molina.imigrasi.go.id. There are no hidden airport fees for eVOA holders."),
            ("Is the Indonesia eVOA fee refundable?",
             "No. The IDR 500,000 eVOA fee is non-refundable. If your application is rejected or you cancel your trip, you will not receive a refund. Ensure all details match your passport and your nationality is eligible before paying."),
            ("Do ASEAN nationals pay any visa fee for Indonesia?",
             "No. Citizens of ASEAN member states (Thailand, Malaysia, Singapore, Philippines, Brunei, Vietnam, Myanmar, Laos, Cambodia) enjoy visa-free access to Indonesia and do not pay any visa fee. They can typically stay 30 days without a visa."),
        ],
        "faq_proc": [
            ("How long does Indonesia eVOA processing take in 2026?",
             "The Indonesia eVOA is processed within 1–2 business days when applied online at molina.imigrasi.go.id. Most applicants receive approval within 24 hours on business days. During peak travel seasons (Christmas, Bali holidays) allow 3 business days to be safe."),
            ("Can I get the Indonesia eVOA on the same day?",
             "Same-day approval is not guaranteed through the online portal. If you need to travel urgently, purchase the Visa on Arrival (VOA) at designated immigration counters at Ngurah Rai (Bali), Soekarno-Hatta (Jakarta), or other major airports. The VOA takes 15–30 minutes."),
            ("What is the difference in processing time between eVOA and VOA?",
             "The eVOA requires 1–2 business days advance processing online but saves time at the airport. The traditional Visa on Arrival takes 15–30 minutes at the airport counter. For a stress-free arrival, the eVOA is recommended especially during busy periods."),
            ("How do I track my Indonesia eVOA application?",
             "After submitting your application at molina.imigrasi.go.id you will receive an application reference number. Log back into the portal to check status. You will also receive an email notification when your eVOA is approved. Check your spam folder if you do not receive it within 2 days."),
        ],
        "howto_req": [
            ("Check eVOA eligibility", "Visit molina.imigrasi.go.id and confirm your nationality is among the 86+ countries eligible for the Indonesia eVOA."),
            ("Gather required documents", "Prepare a valid passport (6+ months validity), a passport-style photo, and proof of return/onward travel out of Indonesia within 30 days."),
            ("Complete the online application", "Fill in the eVOA application form with personal details, travel dates, and Indonesian accommodation address."),
            ("Pay the fee", "Pay IDR 500,000 (~USD 32) using a Visa or MasterCard. Save your payment receipt and application reference number."),
            ("Print your eVOA QR code", "Within 1–2 business days you will receive an approval email with a QR code. Print it or save it to your phone and present it at Indonesian immigration alongside your passport."),
        ],
        "howto_fee": [
            ("Verify your nationality is eligible", "Check the official list of 86+ eligible nationalities on molina.imigrasi.go.id before starting the payment process."),
            ("Prepare your credit or debit card", "Ensure your Visa or MasterCard is enabled for international online transactions. Check your card limit covers IDR 500,000 (~USD 32)."),
            ("Apply on the official government portal only", "Always pay through molina.imigrasi.go.id to avoid third-party surcharges of USD 10–30 common on unofficial visa agency sites."),
            ("Complete payment and save confirmation", "After paying, download and save your payment confirmation email. Note your application reference number for tracking purposes."),
            ("Budget for possible extension", "If you may stay longer than 30 days, budget an additional IDR 500,000 for a one-time extension applied for at a local immigration office inside Indonesia."),
        ],
        "howto_proc": [
            ("Apply at least 3 days before travel", "Submit your eVOA application at molina.imigrasi.go.id at least 3 calendar days before departure to allow 1–2 business days processing plus time for any corrections."),
            ("Monitor your email and portal status", "Log into the portal with your reference number and check your registered email including spam folder for the approval notification."),
            ("Verify approval details", "When approved, confirm that your name, passport number, and travel dates on the eVOA exactly match your passport. Contact immigration immediately if any errors are found."),
            ("Download and save your eVOA", "Download the eVOA QR code document. Print a physical copy and also save it to your smartphone in case of internet connectivity issues at the border."),
            ("Present at Indonesian immigration", "At the Indonesian port of entry, present your passport and eVOA QR code to the immigration officer. They will scan the code and stamp your passport for a 30-day stay."),
        ],
    },

    "turkey": {
        "label": "Turkey",
        "flag": "tr",
        "visa_page": "visa-turkey.html",
        "fee": "USD 50–90 (varies by nationality)",
        "stay": "30 days",
        "processing": "Instant to 5 minutes",
        "portal": "evisa.gov.tr",
        "portal_url": "https://www.evisa.gov.tr",
        "visa_type": "eVisa",
        "free_note": "Visa-free for EU citizens and many others; eVisa required for ~100 nationalities",
        "eligibility": "~100 nationalities eligible for eVisa",
        "entry": "Single or double entry",
        "currency": "TRY (Turkish Lira)",
        "region": "Europe / Middle East",
        "schengen": False,
        "extra_fees": [
            ("eVisa – US citizens", "USD 90"),
            ("eVisa – Australian citizens", "USD 90"),
            ("eVisa – Canadian citizens", "USD 90"),
            ("eVisa – most other eligible nationalities", "USD 50"),
            ("Consular visa (sticker)", "USD 50–110 (varies by nationality)"),
            ("Overstay fine (per day)", "Variable; may result in ban"),
        ],
        "req_rows": [
            ("Valid passport", "Minimum 6 months validity beyond visa expiry date"),
            ("Return/onward ticket", "Proof of departure from Turkey within stay period"),
            ("Credit/debit card", "Visa or MasterCard for USD 50–90 fee payment"),
            ("Accommodation details", "Hotel booking or host address in Turkey"),
            ("Email address", "Valid email to receive eVisa confirmation"),
            ("Travel history (optional)", "Prior Schengen/US/UK visa may allow cheaper fee"),
            ("Sufficient funds", "Bank statement or credit card evidence"),
        ],
        "processing_rows": [
            ("eVisa (evisa.gov.tr)", "Instant to 5 minutes"),
            ("Consular visa (embassy)", "3–5 business days"),
            ("Work visa (employer-sponsored)", "15–30 working days"),
            ("Student visa (education institution)", "10–20 working days"),
            ("Residence permit", "20–30 working days (applied in Turkey)"),
            ("Peak season (summer holidays)", "eVisa still instant; consular may take 5–7 days"),
        ],
        "faq_req": [
            ("What do I need to apply for a Turkey eVisa in 2026?",
             "You need a valid passport (6+ months validity), a confirmed return or onward ticket, a valid email address to receive the eVisa, and a Visa or MasterCard to pay the fee of USD 50–90 depending on your nationality. The entire application takes about 5 minutes at evisa.gov.tr."),
            ("Do I need a confirmed flight to apply for a Turkey eVisa?",
             "You should have at least a planned travel date and evidence of onward travel, although a confirmed booking is not technically required for the eVisa application itself. Turkish immigration at the border may ask for proof of return travel, so a booked flight or bus ticket is strongly recommended."),
            ("Does a Schengen visa help with Turkey eVisa eligibility?",
             "Some nationalities with a valid Schengen, US, or UK visa may be eligible for a cheaper or extended Turkey eVisa. Check the latest eligibility rules at evisa.gov.tr. A valid multi-entry Schengen visa does not replace the need for a Turkey eVisa."),
            ("Can I extend my Turkey eVisa inside Turkey?",
             "The 30-day eVisa cannot be extended online. To stay longer, you must either leave Turkey and re-enter (if eligible), apply for a tourist residence permit at the Provincial Directorate of Migration Management (PDMM) inside Turkey, or obtain a different visa category from a Turkish consulate."),
        ],
        "faq_fee": [
            ("How much does a Turkey eVisa cost in 2026?",
             "The Turkey eVisa fee is USD 90 for US, Australian, and Canadian citizens, and USD 50 for most other eligible nationalities. Fees are non-refundable and paid online at evisa.gov.tr using Visa or MasterCard. Check the official site for your nationality's exact fee as rates are subject to change."),
            ("Why is the Turkey eVisa more expensive for some nationalities?",
             "Turkey sets eVisa fees based on bilateral agreements and reciprocity principles. US, Australian, and Canadian citizens pay USD 90 because Turkey applies reciprocal fee matching for these nationalities. Other nationalities typically pay USD 50. The fee includes a single or double-entry 30-day permit."),
            ("Is the Turkey eVisa fee refundable if I cancel my trip?",
             "No. The Turkey eVisa fee is non-refundable. If you cancel your trip or your visa is denied, you will not receive a refund. The eVisa is also non-transferable. Apply only when you are certain of your travel plans."),
            ("Are there additional taxes or fees when visiting Turkey?",
             "There is no separate tourism tax levied at the border. However, some Turkish hotels charge a small nightly accommodation tax. International flights from Turkish airports may include airport fees in the ticket price. Always check your ticket's full fee breakdown before purchasing."),
        ],
        "faq_proc": [
            ("How quickly is the Turkey eVisa processed in 2026?",
             "The Turkey eVisa is processed instantly or within 5 minutes at evisa.gov.tr. You will receive the approved eVisa PDF to your email address almost immediately after payment. This makes Turkey one of the fastest eVisa systems in the world."),
            ("Do I need to print my Turkey eVisa?",
             "Yes. You must print your Turkey eVisa and present it alongside your valid passport at Turkish immigration. Some airports may accept a digital version on your smartphone, but a printed copy is the safest option. Save the PDF immediately after receiving it."),
            ("What if I do not receive my Turkey eVisa email immediately?",
             "Check your spam or junk email folder first. If the email has not arrived within 30 minutes, log back into evisa.gov.tr with your application reference number to download the eVisa directly. Contact the support email on the portal if issues persist."),
            ("Can I apply for a Turkey eVisa on the same day as my flight?",
             "Yes. Since processing is instant, you can technically apply on the day of travel. However, it is strongly recommended to apply at least 24–48 hours before your flight to allow time to resolve any payment issues or application errors without missing your departure."),
        ],
        "howto_req": [
            ("Check your nationality's eligibility", "Visit evisa.gov.tr to confirm your passport is among the ~100 nationalities eligible for a Turkey eVisa and note your specific fee (USD 50 or USD 90)."),
            ("Prepare your travel documents", "Have your valid passport (6+ months validity), a confirmed return or onward ticket, and your accommodation address in Turkey ready before starting the application."),
            ("Complete the application form", "Enter your personal details, passport information, travel dates, and accommodation at evisa.gov.tr. The form takes approximately 3–5 minutes to complete."),
            ("Pay the visa fee online", "Pay USD 50 or USD 90 using Visa or MasterCard. Your eVisa will be issued within seconds to minutes after successful payment."),
            ("Print and carry your eVisa", "Download the eVisa PDF from the confirmation email and print it. Present the printed eVisa alongside your passport at Turkish immigration upon arrival."),
        ],
        "howto_fee": [
            ("Identify your nationality's fee", "Check evisa.gov.tr for your country's exact eVisa fee: USD 90 for US/Australia/Canada citizens, USD 50 for most others."),
            ("Prepare an internationally enabled card", "Ensure your Visa or MasterCard is authorised for online international transactions and has sufficient funds for the fee."),
            ("Pay directly on the official portal", "Always pay at evisa.gov.tr. Third-party visa services charge an additional USD 20–50 service fee on top of the official government fee."),
            ("Save your payment receipt", "Download and store your payment confirmation email and eVisa PDF. These serve as proof of fee payment if any discrepancy arises at the border."),
            ("Budget for incidentals", "There are no hidden entry fees for eVisa holders, but carry some Turkish Lira for local transportation or small purchases upon arrival."),
        ],
        "howto_proc": [
            ("Apply at least 24–48 hours before travel", "Although processing is instant, apply at least a day early to resolve any unexpected technical or payment issues without missing your flight."),
            ("Use the official evisa.gov.tr portal", "Only apply at the official government website. Third-party sites cause delays and charge extra fees without providing any faster service."),
            ("Check your email immediately after payment", "Your eVisa should arrive within 5 minutes. Check inbox and spam. If not received in 30 minutes, use your reference number to retrieve it at evisa.gov.tr."),
            ("Verify all eVisa details", "Confirm that your name, passport number, nationality, and travel dates on the eVisa exactly match your passport to avoid being denied boarding."),
            ("Present at Turkish immigration", "Hand your printed eVisa and passport to the Turkish immigration officer. They will verify the document and stamp your passport for a 30-day stay."),
        ],
    },

    "uae": {
        "label": "UAE",
        "flag": "ae",
        "visa_page": "visa-uae.html",
        "fee": "AED 250–350 (~USD 68–95) for non-EU; 90-day visa-free for EU",
        "stay": "90 days (EU visa-free); 30/60 days (eVisa)",
        "processing": "3–5 business days",
        "portal": "icp.gov.ae",
        "portal_url": "https://icp.gov.ae",
        "visa_type": "eVisa / Tourist Visa",
        "free_note": "90 days visa-free for EU, UK, US, Australia and many other nationalities",
        "eligibility": "Visa-free for 50+ nationalities; eVisa for others",
        "entry": "Single or multiple entry",
        "currency": "AED (UAE Dirham)",
        "region": "Middle East",
        "schengen": False,
        "extra_fees": [
            ("30-day single-entry tourist visa", "AED 250–300 (~USD 68–82)"),
            ("60-day single-entry tourist visa", "AED 350–400 (~USD 95–109)"),
            ("90-day multiple-entry visa", "AED 650+ (~USD 177+)"),
            ("Transit visa (48–96 hours)", "AED 50–100 (~USD 14–27)"),
            ("Visa extension (inside UAE)", "AED 600–1,500 (~USD 163–408)"),
            ("Work visa (employer-sponsored)", "Variable, employer pays"),
        ],
        "req_rows": [
            ("Valid passport", "Minimum 6 months validity; at least 2 blank pages"),
            ("Passport-size photo", "White background, recent, 3.5×4.5 cm"),
            ("Return/onward ticket", "Proof of departure from UAE"),
            ("Hotel booking or host NOC", "Confirmed accommodation in the UAE"),
            ("Bank statement", "3 months showing sufficient funds for stay"),
            ("Travel insurance", "Minimum USD 30,000 medical coverage recommended"),
            ("Payment card", "Visa/MasterCard for AED 250–650 fee"),
        ],
        "processing_rows": [
            ("Tourist eVisa (icp.gov.ae)", "3–5 business days"),
            ("Visa-free entry (50+ nationalities)", "Instant — no pre-approval needed"),
            ("Transit visa (48 hours)", "1–2 business days"),
            ("Employment visa (employer-sponsored)", "7–14 working days"),
            ("Residence visa (family/investor)", "10–20 working days"),
            ("Golden Visa (10-year)", "20–30 working days"),
        ],
        "faq_req": [
            ("What documents are needed for a UAE tourist visa in 2026?",
             "You need a valid passport (6+ months validity, 2+ blank pages), a white-background passport photo, confirmed return ticket, hotel booking or host's No Objection Certificate (NOC), 3 months of bank statements, and a Visa or MasterCard for the AED 250–650 fee. EU, UK, US, and Australian citizens need no visa."),
            ("Do EU citizens need a visa for the UAE?",
             "No. Citizens of EU member states, along with UK, US, Australian, Canadian, Japanese, and many other passport holders, receive 90 days visa-free entry to the UAE. They do not need to apply in advance or pay any fee. Just ensure your passport has 6+ months validity."),
            ("Do I need travel insurance for a UAE tourist visa?",
             "Travel insurance is not mandatory for tourist visa applications but is strongly recommended given the high cost of medical treatment in the UAE. Some visa agents require it. Ensure your policy covers at least USD 30,000 in medical expenses."),
            ("Can I work in the UAE on a tourist visa?",
             "No. Working in the UAE on a tourist or visit visa is illegal and can result in deportation and a ban. You must have an employment visa sponsored by a UAE employer and obtain a UAE residence visa to work legally."),
        ],
        "faq_fee": [
            ("How much does a UAE tourist visa cost in 2026?",
             "UAE tourist visas cost AED 250–300 (~USD 68–82) for a 30-day single-entry, AED 350–400 (~USD 95–109) for 60 days, and AED 650+ for a 90-day multiple-entry visa. EU, UK, US, Australian, and many other nationals enter visa-free for 90 days at no cost. Apply at icp.gov.ae or through Emirates/Etihad airlines."),
            ("Can I apply for a UAE visa through the airline?",
             "Yes. If you are flying with Emirates or Etihad Airways, you can apply for a UAE tourist visa directly through the airline's website. Fees are similar to the government portal at icp.gov.ae. This is a convenient option as the airline can access your booking details automatically."),
            ("Are there additional fees when entering the UAE?",
             "There is no separate airport entry tax for tourists. However, some UAE hotels charge a municipal fee (AED 7–20 per night) and a tourism fee (AED 10–15 per night). These are added to your hotel bill, not collected at the border."),
            ("Is the UAE tourist visa fee refundable if denied?",
             "Government fees for UAE visa applications are generally non-refundable if the application is denied or withdrawn. Service fees charged by visa agencies are also typically non-refundable. Ensure all documents are correct before submission to minimise refusal risk."),
        ],
        "faq_proc": [
            ("How long does UAE visa processing take in 2026?",
             "UAE tourist visa applications submitted through icp.gov.ae are processed in 3–5 business days. Applications via Emirates or Etihad airlines may be faster (2–3 days). Visa-free nationals (EU, UK, US etc.) require no advance processing and enter immediately upon arrival."),
            ("Can I get a UAE visa faster than 3 days?",
             "Express processing is available through some airline visa services and authorised travel agents, potentially reducing processing to 24–48 hours for an additional fee. The standard government portal does not currently offer an official expedited option."),
            ("What happens if my UAE visa application is delayed?",
             "If your application exceeds 5 business days without a decision, contact icp.gov.ae customer support or the travel agent through whom you applied. Keep your application reference number. If you have flexible travel dates, consider delaying your flight until the visa is confirmed."),
            ("Can I check my UAE visa application status online?",
             "Yes. You can track your UAE visa application status on the icp.gov.ae portal using your application reference number and passport details. You will also receive email and SMS updates when the visa is approved or if additional documents are required."),
        ],
        "howto_req": [
            ("Determine if you need a visa", "Check the UAE Federal Authority for Identity and Citizenship (icp.gov.ae) to confirm whether your nationality requires a visa. EU, UK, US, and Australian citizens can enter visa-free for 90 days."),
            ("Prepare required documents", "Gather a passport valid for 6+ months with 2 blank pages, a recent passport photo, confirmed return ticket, hotel booking, 3 months bank statements, and optional travel insurance."),
            ("Submit your application", "Apply online at icp.gov.ae, through the UAE embassy in your country, or via Emirates/Etihad airline if you are flying with them."),
            ("Pay the visa fee", "Pay AED 250–650 (~USD 68–177) depending on the visa type using Visa or MasterCard. Some agents accept local payment methods."),
            ("Receive and review your visa", "Within 3–5 business days you will receive your UAE visa by email. Print it and check all details match your passport before travel."),
        ],
        "howto_fee": [
            ("Check if you qualify for visa-free entry", "EU, UK, US, Canadian, Australian, and Japanese citizens get 90 days visa-free — no payment required. Verify at icp.gov.ae."),
            ("Select the right visa duration", "Choose 30-day (AED 250–300), 60-day (AED 350–400), or 90-day multiple-entry (AED 650+) based on your travel plans. Longer durations offer better value for extended stays."),
            ("Apply through official channels", "Use icp.gov.ae or a licensed UAE visa agent. Airlines Emirates and Etihad also offer visa services with competitive fees."),
            ("Pay securely online", "Complete payment with Visa or MasterCard. Save your payment confirmation email and application reference number."),
            ("Keep fee receipt for records", "Store your fee receipt; some UAE hotels and tour operators may request proof of visa status upon check-in."),
        ],
        "howto_proc": [
            ("Apply 7 business days before travel", "Submit your UAE visa application at icp.gov.ae at least 7 business days before departure to allow 3–5 days processing plus buffer time."),
            ("Track via icp.gov.ae portal", "Use your application reference number and passport details on the portal to monitor real-time status updates."),
            ("Check email and SMS notifications", "UAE immigration sends status updates by email and SMS. Keep your phone nearby and ensure your registered email is correct."),
            ("Download and print your visa", "Once approved, download the UAE visa PDF and print a copy. Present it at the UAE port of entry alongside your valid passport."),
            ("Present at UAE immigration", "Hand your printed visa and passport to UAE border control. They will verify your visa and stamp your passport. You may be asked to confirm your hotel booking and sufficient funds."),
        ],
    },

    "singapore": {
        "label": "Singapore",
        "flag": "sg",
        "visa_page": "visa-singapore.html",
        "fee": "SGD 30 (~USD 22) for tourist visa; visa-free for most",
        "stay": "30 days visa-free (most nationalities)",
        "processing": "3–8 weeks (Employment Pass)",
        "portal": "mom.gov.sg",
        "portal_url": "https://www.mom.gov.sg",
        "visa_type": "Visa-free / Tourist Visa / Employment Pass",
        "free_note": "Visa-free for 160+ nationalities including EU, UK, US, Australia",
        "eligibility": "Visa-free for 160+ countries; visa required for ~30 nationalities",
        "entry": "Multiple entry (visa-free)",
        "currency": "SGD (Singapore Dollar)",
        "region": "Southeast Asia",
        "schengen": False,
        "extra_fees": [
            ("Tourist visa (for nationalities that need it)", "SGD 30 (~USD 22)"),
            ("Employment Pass (EP) application", "SGD 105 (~USD 78)"),
            ("S Pass application", "SGD 60 (~USD 44)"),
            ("Work Permit", "SGD 35 (~USD 26) per foreign worker levy exempt"),
            ("Dependent Pass", "SGD 105 (~USD 78)"),
            ("Long-Term Visit Pass", "SGD 30–105 (~USD 22–78)"),
        ],
        "req_rows": [
            ("Valid passport", "Minimum 6 months validity; at least 2 blank pages"),
            ("Return/onward ticket", "Proof of departure from Singapore"),
            ("Accommodation proof", "Hotel booking or host details"),
            ("Sufficient funds", "Approx SGD 100/day recommended"),
            ("Employment Pass (for workers)", "SGD 5,000/month minimum salary for EP"),
            ("Educational certificates", "Required for Employment Pass applications"),
            ("Company sponsorship letter", "Required for work visa applicants"),
        ],
        "processing_rows": [
            ("Visa-free entry (160+ nationalities)", "Instant on arrival, no application"),
            ("Tourist visa (e-service ICA)", "1–3 business days"),
            ("Employment Pass (EP)", "3–8 weeks"),
            ("S Pass (mid-skilled workers)", "3–8 weeks"),
            ("Work Permit (unskilled/semi-skilled)", "1–7 days online"),
            ("Dependent Pass / LTVP", "3–6 weeks"),
        ],
        "faq_req": [
            ("Do I need a visa for Singapore in 2026?",
             "Most nationalities including EU, UK, US, Australian, Canadian, Indian (with prior Singapore stay), and many ASEAN citizens do not need a visa for Singapore. Over 160 nationalities can enter visa-free for 30–90 days. Citizens of about 30 countries still require a visa obtainable from the Singapore Immigration and Checkpoints Authority (ICA)."),
            ("What is the minimum salary for a Singapore Employment Pass?",
             "As of 2026, the minimum qualifying salary for a Singapore Employment Pass (EP) is SGD 5,000 per month for most sectors (higher for financial services at SGD 5,500). The EP targets professionals, managers, executives, and specialists. Candidates must also pass the COMPASS scoring framework."),
            ("What documents are needed for a Singapore tourist visa?",
             "For nationalities requiring a visa, you need a valid passport (6+ months), passport photo, confirmed return ticket, hotel booking, bank statements (3 months), and a completed application form. Applications are submitted through a Singapore embassy, accredited travel agent, or the ICA e-service."),
            ("Can I work in Singapore on a tourist visa?",
             "No. Working in Singapore without a valid work pass is illegal under the Employment of Foreign Manpower Act and can result in fines, imprisonment, and a ban from Singapore. You must apply for an Employment Pass, S Pass, or Work Permit through your Singapore employer before starting work."),
        ],
        "faq_fee": [
            ("How much does a Singapore visa cost in 2026?",
             "Singapore tourist visa costs SGD 30 (~USD 22) for nationalities that require it; the majority of travellers enter visa-free at no cost. An Employment Pass application costs SGD 105 (~USD 78). An S Pass application costs SGD 60 (~USD 44). Fees are paid online to the Immigration and Checkpoints Authority (ICA) at ica.gov.sg."),
            ("Is there a fee for Singapore visa-free entry?",
             "No. Citizens of 160+ nationalities including all EU countries, UK, US, Australia, Canada, Japan, and South Korea enter Singapore visa-free for 30–90 days without any fee. Upon arrival, immigration officers may ask about accommodation and funds but no payment is required."),
            ("What is the Employment Pass fee for Singapore?",
             "The Singapore Employment Pass application fee is SGD 105 (~USD 78) per application, paid online by the sponsoring employer through mom.gov.sg. This is a government processing fee and does not guarantee approval. A separate issuance fee may apply once the EP is approved."),
            ("Are there any hidden costs when entering Singapore?",
             "There are no hidden entry fees. However, all visitors must complete a Singapore Arrival Card (SGAC) online free of charge within 3 days before arrival. Do this at ica.gov.sg/arrival. Avoid third-party services that charge for completing this free government form."),
        ],
        "faq_proc": [
            ("How long does Singapore Employment Pass processing take?",
             "The Singapore Employment Pass (EP) takes 3–8 weeks to process. Applications are submitted online by the sponsoring employer through mom.gov.sg using the EP Online system. The Ministry of Manpower also evaluates applications against the COMPASS points framework before approving."),
            ("Is Singapore visa processing instant for visa-free nationals?",
             "Yes. Citizens of 160+ nationalities receive instant clearance upon arrival at Singapore's Changi Airport or land/sea borders. No advance application is needed. Simply present your passport and completed Singapore Arrival Card (SGAC) at the immigration counter."),
            ("How do I track my Singapore Employment Pass application?",
             "Employers can track EP application status through the EP Online portal at mom.gov.sg. The ministry also sends email updates. The average processing time is 3–8 weeks. If additional information is needed, MOM will contact the employer directly via the portal."),
            ("Can I speed up Singapore Employment Pass processing?",
             "There is no official expedited processing for Singapore Employment Pass applications. Ensure the application is complete and accurate to avoid delays from requests for additional information. Submitting during off-peak periods (not January or after public holidays) may result in faster processing."),
        ],
        "howto_req": [
            ("Check your visa-free status", "Visit ica.gov.sg to confirm whether your nationality enjoys visa-free access to Singapore for 30–90 days. Over 160 nationalities qualify."),
            ("Complete the Singapore Arrival Card", "All visitors must complete the Singapore Arrival Card (SGAC) free at ica.gov.sg/arrival within 3 days before arrival, regardless of visa status."),
            ("Prepare required documents", "Have a valid passport (6+ months), return ticket, hotel booking, and bank statements or credit card showing sufficient funds (SGD 100/day recommended)."),
            ("Apply for a visa if required", "If your nationality requires a visa, apply through the ICA e-service, Singapore embassy, or accredited travel agent, paying SGD 30 (~USD 22)."),
            ("Present at Singapore immigration", "At the border, present your passport and SGAC confirmation to the immigration officer for instant clearance (visa-free) or visa stamp."),
        ],
        "howto_fee": [
            ("Determine your visa status", "Check ica.gov.sg to see if your nationality requires a fee-bearing tourist visa (SGD 30) or qualifies for free visa-free entry."),
            ("Apply through official ICA channels", "Visa-required nationals should apply at the ICA e-service or Singapore embassy. Avoid third-party services that overcharge."),
            ("Pay SGD 30 by credit card", "The tourist visa fee is paid online. Use a Visa, MasterCard, or NETS card. Ensure your card supports international online transactions."),
            ("Budget for your stay", "Singapore recommends having at least SGD 100 per day of your stay available (approx USD 74). Border officers may ask about your funds."),
            ("No fee for arrival card", "The Singapore Arrival Card (SGAC) at ica.gov.sg/arrival is free. Ignore any website charging for this mandatory free government form."),
        ],
        "howto_proc": [
            ("Check if advance application is needed", "160+ nationalities need no advance application. If you need a tourist visa, apply at least 5 business days before travel for the 1–3 day processing time."),
            ("Submit SGAC before arrival", "Complete your Singapore Arrival Card online at ica.gov.sg/arrival within 3 days before entering Singapore. This is mandatory and free."),
            ("Monitor application status", "If you applied for a tourist visa, track status via ICA's e-service. You will receive an email notification upon approval."),
            ("Receive and print your visa", "Tourist visa is emailed to you as a PDF. Print it and carry it to the airport, though digital copies are generally accepted."),
            ("Clear immigration at Changi Airport", "Present your passport (and visa if required) at the automated or staffed immigration lanes. Processing is typically under 5 minutes for most nationalities."),
        ],
    },

    "netherlands": {
        "label": "Netherlands",
        "flag": "nl",
        "visa_page": "visa-netherlands.html",
        "fee": "EUR 80",
        "stay": "90 days within 180-day period (Schengen)",
        "processing": "15 working days",
        "portal": "netherlandsandyou.nl",
        "portal_url": "https://www.netherlandsandyou.nl",
        "visa_type": "Schengen Visa (type C)",
        "free_note": "Visa-free for EU/EEA, UK, US, Canada, Australia, Japan and many others",
        "eligibility": "Non-EU nationals may require Schengen visa; varies by nationality",
        "entry": "Single, double or multiple entry",
        "currency": "EUR (Euro)",
        "region": "Western Europe",
        "schengen": True,
        "extra_fees": [
            ("Schengen short-stay visa (adult)", "EUR 80"),
            ("Schengen visa (child 6–11)", "EUR 40"),
            ("Schengen visa (child under 6)", "Free"),
            ("VFS Global service fee", "EUR 15–30 (varies by country)"),
            ("National (D) visa – long stay", "EUR 192"),
            ("MVV (entry visa for residence permit)", "EUR 192"),
        ],
        "req_rows": [
            ("Valid passport", "Issued within last 10 years; valid 3+ months after return date; 2 blank pages"),
            ("Completed Schengen application form", "Signed application form (DS-160 equivalent for Schengen)"),
            ("Passport-style photos", "2 photos meeting ICAO standards, 35×45 mm, plain background"),
            ("Travel insurance", "Minimum EUR 30,000 coverage, valid for all Schengen area"),
            ("Flight itinerary", "Round-trip booking or confirmed reservation"),
            ("Accommodation proof", "Hotel bookings or host invitation letter"),
            ("Bank statements", "3–6 months, minimum EUR 50/day of stay"),
            ("Employment letter / payslips", "Proof of leave approval and stable employment/income"),
        ],
        "processing_rows": [
            ("Schengen visa – standard", "15 working days"),
            ("Schengen visa – early submission", "Up to 6 months before travel"),
            ("Schengen visa – peak season (summer)", "Up to 30 working days"),
            ("National (D) long-stay visa", "3–6 months"),
            ("Residence permit (MVV)", "3–6 months from abroad"),
            ("Dutch highly skilled migrant permit", "2–4 weeks (with IND approval)"),
        ],
        "faq_req": [
            ("What documents do I need for a Netherlands Schengen visa in 2026?",
             "You need a valid passport (issued within 10 years, valid 3+ months after return, 2 blank pages), 2 ICAO-compliant passport photos, completed Schengen application form, travel insurance (EUR 30,000 minimum), round-trip flight itinerary, accommodation proof, 3–6 months bank statements (EUR 50/day minimum), and employment letter with pay slips."),
            ("Do I need travel insurance for a Netherlands Schengen visa?",
             "Yes. Travel insurance is mandatory for a Schengen visa. It must cover the entire Schengen zone, your full travel period, and provide at least EUR 30,000 in medical emergency and repatriation coverage. The insurance certificate must show your name, travel dates, and coverage amounts."),
            ("How far in advance can I apply for a Netherlands Schengen visa?",
             "You can apply up to 6 months before your travel date. The earliest recommended submission is 3 months in advance. Applications must be submitted at least 15 working days before travel. During summer or school holiday periods, submit even earlier due to higher appointment demand at VFS Global."),
            ("Can I visit other Schengen countries on a Netherlands Schengen visa?",
             "Yes. A Netherlands-issued Schengen visa permits travel throughout all 27 Schengen member states for up to 90 days in any 180-day period. Apply to the Netherlands consulate if the Netherlands is your main destination or longest stay country."),
        ],
        "faq_fee": [
            ("How much does a Netherlands Schengen visa cost in 2026?",
             "The official Netherlands Schengen visa fee is EUR 80 for adults and EUR 40 for children aged 6–11. Children under 6 are exempt. VFS Global service centres charge an additional EUR 15–30 service fee depending on the country. A national (long-stay D) visa costs EUR 192."),
            ("Is the Netherlands Schengen visa fee refundable?",
             "No. The EUR 80 Schengen visa fee is non-refundable regardless of the outcome. Even if your visa is refused, the fee is retained to cover administrative processing costs. Some VFS Global service fees may be refundable if the appointment is cancelled well in advance; check local VFS terms."),
            ("Does the Netherlands Schengen visa fee include VFS service charges?",
             "No. The EUR 80 is the government (Dutch IND/Embassy) fee only. VFS Global, which processes applications on behalf of the Dutch embassy in many countries, charges an additional service fee of EUR 15–30 per application. This brings the total cost to approximately EUR 95–110."),
            ("Are there reduced fees for any nationalities for the Netherlands Schengen visa?",
             "Citizens of some countries with bilateral agreements (e.g., Georgia, Ukraine, Moldova, Kosovo, Bosnia and Herzegovina, North Macedonia, Albania, Serbia, Armenia, Cape Verde) benefit from a reduced EUR 35 Schengen visa fee under the EU visa facilitation agreements."),
        ],
        "faq_proc": [
            ("How long does Netherlands Schengen visa processing take in 2026?",
             "The standard Netherlands Schengen visa processing time is 15 working days (approximately 3 calendar weeks). During peak summer season (June–August) and around Christmas, processing can extend to 30 working days. Always apply at least 6 weeks before travel during busy periods."),
            ("Can I expedite my Netherlands Schengen visa application?",
             "The Netherlands does not offer a guaranteed expedited Schengen visa service. If you have urgent travel (medical emergency, family death), contact the Dutch embassy directly with supporting documentation. They may prioritise urgent cases, but this is not a standard paid service."),
            ("When should I submit my Netherlands Schengen visa application?",
             "Apply between 3 months and 15 working days before your departure. Earlier submission (2–3 months ahead) is recommended during summer. The application cannot be submitted more than 6 months before the intended travel date."),
            ("How do I track my Netherlands Schengen visa application?",
             "You can track your application status through the VFS Global portal using your application reference number. Some Dutch embassies also provide direct tracking. You will receive email/SMS updates when the passport is ready for collection or when a decision is made."),
        ],
        "howto_req": [
            ("Check visa requirement for your nationality", "Verify at netherlandsandyou.nl whether your passport requires a Schengen visa. EU, EEA, UK, US, Canada, and Australian citizens enter visa-free."),
            ("Gather all required documents", "Prepare passport, ICAO photos, travel insurance (EUR 30,000 min), flight itinerary, accommodation proof, 3–6 months bank statements, and employment letter."),
            ("Book VFS appointment or embassy appointment", "Schedule an appointment at the nearest VFS Global centre or Dutch embassy/consulate with your completed application form and all documents."),
            ("Attend appointment and submit biometrics", "Attend in person to submit documents and provide fingerprint biometrics. Bring all original documents plus photocopies."),
            ("Pay EUR 80 visa fee plus VFS service charge", "Pay the government fee and VFS service fee at the application centre. Keep your receipt for tracking and collection."),
        ],
        "howto_fee": [
            ("Confirm the official fee is EUR 80", "The Schengen short-stay visa fee for adults is EUR 80. Check netherlandsandyou.nl for any fee updates or nationality-specific reduced rates."),
            ("Identify if you qualify for a reduced fee", "Citizens of certain countries with EU visa facilitation agreements pay EUR 35. Check if your country is among them before budgeting."),
            ("Budget for VFS service fee", "Add EUR 15–30 VFS service fee on top of the EUR 80 government fee. Total cost is approximately EUR 95–110."),
            ("Pay at the VFS application centre", "Fees are paid at the appointment, typically by cash or local debit card. Check your local VFS accepted payment methods in advance."),
            ("Retain payment receipts", "Keep all fee receipts. If your passport is not returned within the expected period, your receipt number will help VFS track your application."),
        ],
        "howto_proc": [
            ("Apply 15+ working days before travel", "Submit your application at least 15 working days (3 calendar weeks) before departure. During summer, apply 6–8 weeks early."),
            ("Submit complete documentation at first attempt", "Incomplete applications cause delays. Use the VFS checklist from netherlandsandyou.nl to verify every document before your appointment."),
            ("Track via VFS portal", "After submission, track your application status using the VFS reference number at vfsglobal.com. Email/SMS notifications will alert you when ready."),
            ("Collect your passport", "Collect your passport from the VFS centre after notification, or opt for courier delivery if offered. Verify the visa details immediately upon receipt."),
            ("Verify Schengen visa validity", "Check the visa validity dates, number of entries, and duration of stay. Correct any errors immediately before travel by contacting the Dutch embassy."),
        ],
    },

    "portugal": {
        "label": "Portugal",
        "flag": "pt",
        "visa_page": "visa-portugal.html",
        "fee": "EUR 80 (Schengen); EUR 90 D7 passive income visa",
        "stay": "90 days (Schengen); long-stay on D7",
        "processing": "15 working days (Schengen); 2–3 months (D7)",
        "portal": "sef.pt",
        "portal_url": "https://www.sef.pt",
        "visa_type": "Schengen / D7 Passive Income / NHR",
        "free_note": "Visa-free for EU, UK, US, Canada, Australia; D7 requires EUR 760/month income",
        "eligibility": "Non-EU nationals with income/savings may qualify for D7 visa",
        "entry": "Multiple entry (D7); single/multiple (Schengen)",
        "currency": "EUR (Euro)",
        "region": "Western Europe",
        "schengen": True,
        "extra_fees": [
            ("Schengen short-stay visa (adult)", "EUR 80"),
            ("D7 passive income visa (type D)", "EUR 90"),
            ("Residence permit (SEF/AIMA)", "EUR 83 (initial) + EUR 54 renewal"),
            ("NIF (tax number registration)", "Free at Finanças"),
            ("NHR tax regime application", "EUR 200 approx (lawyer recommended)"),
            ("Golden Visa – real estate", "EUR 250,000 fund/capital transfer minimum"),
        ],
        "req_rows": [
            ("Valid passport", "Minimum 6 months validity; 2 blank pages"),
            ("Completed visa application form", "Signed and dated"),
            ("Passport-style photos", "2 ICAO-compliant photos, 35×45 mm"),
            ("Travel insurance", "EUR 30,000 minimum for Schengen; higher recommended for D7"),
            ("Proof of income / passive income", "EUR 760/month minimum for D7 (pension, rental, dividends)"),
            ("Bank statements", "3–6 months showing regular income for D7"),
            ("Accommodation proof", "Hotel bookings or rental contract in Portugal"),
            ("Criminal background check", "Required for D7 and long-stay visas"),
        ],
        "processing_rows": [
            ("Schengen C visa – standard", "15 working days"),
            ("D7 passive income visa", "2–3 months"),
            ("Golden Visa", "4–6 months (includes investment verification)"),
            ("Digital Nomad Visa (D8)", "2–3 months"),
            ("D6 family reunification visa", "2–3 months"),
            ("Residence permit renewal (AIMA)", "3–6 months"),
        ],
        "faq_req": [
            ("What documents do I need for a Portugal D7 visa in 2026?",
             "For a Portugal D7 passive income visa you need a valid passport (6+ months), ICAO passport photos, proof of passive income of at least EUR 760/month (pension, rental, investments, dividends), 3–6 months bank statements, Portugal accommodation proof (rental contract or purchase deed), travel insurance, and a criminal background check from your home country."),
            ("What is the minimum income for a Portugal D7 visa?",
             "The Portugal D7 visa requires proof of passive income of at least EUR 760/month (equivalent to the Portuguese minimum wage as of 2026). Acceptable income sources include pensions, rental income, dividends, royalties, and interest. For a family, additional income is required for each dependent."),
            ("What is the Portugal NHR tax regime?",
             "The Non-Habitual Resident (NHR) tax regime historically offered a flat 20% tax rate on Portuguese-source income and tax exemptions on most foreign-source income for 10 years. Note that NHR was reformed in 2024; check with a Portuguese tax adviser for the current IFICI (Non-Habitual Tax Status for Scientific and Innovation) regime applicable in 2026."),
            ("Do I need a Portuguese NIF before applying for the D7 visa?",
             "Yes. You need a Portuguese NIF (tax identification number) before completing your D7 visa application. You can obtain a NIF at a Portuguese consulate abroad or at a local Finanças office in Portugal. It is free and takes 1–5 days. Some lawyers can obtain it remotely for a service fee."),
        ],
        "faq_fee": [
            ("How much does a Portugal D7 visa cost in 2026?",
             "The Portugal D7 passive income visa costs EUR 90 in government fees. The Schengen short-stay visa costs EUR 80. Additional costs include translation and notarisation of documents (EUR 200–500), legal adviser fees (EUR 500–2,000), and travel insurance. The total D7 process typically costs EUR 800–3,000 including professional support."),
            ("What does the Portugal Golden Visa cost in 2026?",
             "Portugal's Golden Visa requires a minimum qualifying investment of EUR 250,000 in authorised investment funds or cultural sponsorship (real estate purchases no longer qualify in most areas as of 2023). Government fees include EUR 5,000 analysis fee and EUR 5,000 issuance fee per person. Legal and setup costs add EUR 3,000–10,000 typically."),
            ("Is the Portugal Schengen visa fee refundable?",
             "No. The EUR 80 Schengen visa fee is non-refundable even if the application is refused. The EUR 90 D7 application fee is also non-refundable. Ensure all documents are correct and income thresholds are met before submission."),
            ("Are there any additional fees for the Portugal NHR tax registration?",
             "The NIF registration is free at a Portuguese Finanças office. Applying for NHR (now IFICI) status is done online at the Portuguese Tax Authority (AT) portal and does not require a government fee, but most applicants hire a tax lawyer at EUR 200–500 to ensure the application is filed correctly."),
        ],
        "faq_proc": [
            ("How long does a Portugal D7 visa take to process in 2026?",
             "The Portugal D7 passive income visa typically takes 2–3 months from the date of your consulate appointment to visa issuance. Processing times vary by consulate location; high-demand consulates (USA, UK, Brazil) may have longer wait times. Book your consulate appointment well in advance as slots fill quickly."),
            ("How long does the Portugal Schengen visa take?",
             "The Portugal Schengen short-stay visa (type C) is processed within 15 working days. During peak summer season (June–August), processing may extend to 30 working days. Apply at least 6 weeks before travel in summer and 3–4 weeks at other times."),
            ("How do I track my Portugal visa application at SEF/AIMA?",
             "You can check the status of your Portugal visa or residence permit application online through the SEF/AIMA portal at aima.gov.pt using your application reference number. You will also receive email notifications at key stages. Note that SEF was renamed AIMA (Agency for Integration, Migration and Asylum) in 2023."),
            ("Can I speed up my Portugal D7 visa application?",
             "There is no official expedited service for the D7 visa. To avoid delays: submit a complete application with all certified translations, book the earliest available consulate appointment, and hire a qualified immigration lawyer familiar with Portuguese consulate requirements."),
        ],
        "howto_req": [
            ("Check your visa requirement", "EU, UK, US, and Australian citizens can enter Portugal visa-free. Non-EU citizens seeking to stay longer than 90 days should explore the D7 passive income visa at sef.pt (now aima.gov.pt)."),
            ("Gather documents for D7 visa", "Prepare passport, ICAO photos, proof of passive income (EUR 760/month minimum), 6 months bank statements, Portugal accommodation proof, criminal record certificate, and travel insurance."),
            ("Obtain Portuguese NIF", "Apply for a NIF (tax number) at a Portuguese consulate abroad or Finanças office in Portugal. Required before submitting the D7 visa application."),
            ("Book and attend consulate appointment", "Schedule an appointment at the Portuguese consulate or VFS Global in your country. Submit all original documents and certified translations."),
            ("Wait for visa decision", "D7 visa processing takes 2–3 months. You will receive a notification when approved and can collect your visa sticker from the consulate."),
        ],
        "howto_fee": [
            ("Confirm the D7 visa government fee (EUR 90)", "The D7 application fee is EUR 90. The Schengen C visa is EUR 80. Budget an additional EUR 200–500 for document translations and notarisation."),
            ("Budget for legal support", "Hiring an immigration lawyer for the D7 application is strongly recommended (EUR 500–2,000) to ensure the application is complete and correctly submitted."),
            ("Pay at the consulate appointment", "Fees are paid at the consulate appointment, usually in local currency. Check the Portuguese consulate website for accepted payment methods in your country."),
            ("Budget for residence permit fees post-arrival", "Once in Portugal, the initial residence permit issued by AIMA costs EUR 83 plus a renewal fee of EUR 54 per year. Budget for these ongoing costs."),
            ("Keep all receipts", "Retain all fee receipts and bank transfer confirmations related to your visa application. These may be requested by AIMA during residence permit processing."),
        ],
        "howto_proc": [
            ("Apply 3 months before intended move date", "Submit your D7 visa application at least 3 months before you plan to move to Portugal, accounting for 2–3 months processing plus time to book consulate appointments."),
            ("Submit a complete application package", "Use the official checklist from aima.gov.pt. Incomplete submissions are a leading cause of delays. Certify all translations and have documents notarised where required."),
            ("Track via AIMA portal", "Monitor your application at aima.gov.pt with your application reference. Email notifications are sent at key stages. You can also contact the consulate directly for updates."),
            ("Collect visa and travel to Portugal", "Once approved, collect your D visa sticker from the consulate. Travel to Portugal within the visa validity period (usually 4 months from issue)."),
            ("Apply for residence permit within 4 months", "After arriving in Portugal on your D7 visa, apply for a residence permit at AIMA within the first 4 months. This converts your D7 visa into a 2-year renewable residence permit."),
        ],
    },

    "greece": {
        "label": "Greece",
        "flag": "gr",
        "visa_page": "visa-greece.html",
        "fee": "EUR 80 (Schengen); EUR 250,000+ Golden Visa",
        "stay": "90 days within 180-day period (Schengen)",
        "processing": "15 working days",
        "portal": "mfa.gr",
        "portal_url": "https://www.mfa.gr",
        "visa_type": "Schengen Visa (type C) / Golden Visa",
        "free_note": "Visa-free for EU, UK, US, Canada, Australia and many others",
        "eligibility": "Non-EU nationals may need Schengen visa; Golden Visa for investors EUR 250,000+",
        "entry": "Single, double or multiple entry",
        "currency": "EUR (Euro)",
        "region": "Southern Europe",
        "schengen": True,
        "extra_fees": [
            ("Schengen short-stay visa (adult)", "EUR 80"),
            ("Schengen visa (child 6–11)", "EUR 40"),
            ("Schengen visa (child under 6)", "Free"),
            ("VFS Global service fee", "EUR 15–30"),
            ("Golden Visa – real estate or fund", "EUR 250,000–800,000 (varies by zone)"),
            ("National (D) long-stay visa", "EUR 150–192"),
        ],
        "req_rows": [
            ("Valid passport", "Issued within last 10 years; 3+ months validity after departure; 2 blank pages"),
            ("Completed Schengen application form", "Signed; downloaded from mfa.gr"),
            ("Passport-style photos", "2 ICAO-standard photos, 35×45 mm"),
            ("Travel insurance", "EUR 30,000 minimum; valid for Schengen area"),
            ("Flight itinerary", "Round-trip flight booking or confirmed reservation"),
            ("Accommodation proof", "Hotel bookings or host invitation letter"),
            ("Bank statements", "3–6 months; min EUR 50 per day of stay"),
            ("Employment / income proof", "Payslips, employment contract, or business registration"),
        ],
        "processing_rows": [
            ("Schengen C visa – standard", "15 working days"),
            ("Schengen C visa – peak season", "Up to 30 working days"),
            ("Golden Visa – application", "60–90 working days"),
            ("National D visa – long stay", "2–3 months"),
            ("Residence permit (first)", "3–6 months"),
            ("Greek citizenship (naturalisation)", "2–5 years (after 7 years legal residence)"),
        ],
        "faq_req": [
            ("What documents are needed for a Greece Schengen visa in 2026?",
             "You need a valid passport (10 years or less old, 3+ months validity after departure, 2 blank pages), 2 ICAO passport photos, completed Schengen application form from mfa.gr, travel insurance (EUR 30,000 min for full Schengen zone), round-trip flight booking, hotel bookings or invitation letter, 3–6 months bank statements, and employment or income proof."),
            ("What is the Greece Golden Visa in 2026?",
             "The Greece Golden Visa grants a 5-year renewable residence permit in exchange for qualifying investments. As of 2026 the minimum investment thresholds are EUR 800,000 for real estate in Athens, Thessaloniki, Mykonos, and Santorini, and EUR 400,000 in other areas. Alternative qualifying investments in business, bonds, or funds start at EUR 250,000."),
            ("Do I need travel insurance for a Greece Schengen visa?",
             "Yes. Travel insurance is mandatory. It must cover medical emergencies and repatriation, be valid for the entire Schengen area, and provide at least EUR 30,000 coverage. The policy must cover your full travel period. Present the original insurance certificate with your visa application."),
            ("Can I visit other Schengen countries on a Greece Schengen visa?",
             "Yes. A Greek-issued Schengen visa is valid for all 27 Schengen member states. You can travel freely throughout the Schengen zone for up to 90 days in any 180-day period. Apply to the Greek consulate if Greece is your main or longest-stay destination."),
        ],
        "faq_fee": [
            ("How much does a Greece Schengen visa cost in 2026?",
             "The Greece Schengen visa costs EUR 80 for adults, EUR 40 for children aged 6–11, and is free for children under 6. VFS Global service centres add EUR 15–30. The total cost is approximately EUR 95–110 per adult application. Long-stay national (D) visas cost EUR 150–192."),
            ("What is the minimum investment for the Greece Golden Visa?",
             "In 2026 the Greece Golden Visa minimum investment is EUR 800,000 for real estate in high-demand areas (Athens, Thessaloniki, Mykonos, Santorini, and other Aegean islands over 3,100 km²) and EUR 400,000 elsewhere. Investment fund options start at EUR 250,000. All amounts exclude transaction costs and legal fees."),
            ("Is the Greece Schengen visa fee refundable?",
             "No. The EUR 80 Schengen visa fee is non-refundable even if the application is refused or the applicant cancels travel. The VFS service fee may be partially refundable if you cancel your appointment before it is processed; check with your local VFS centre."),
            ("Are there extra fees when entering Greece?",
             "There are no separate border entry fees for Greece. However, some Greek islands charge a small passenger port tax (EUR 1–3) on ferry travel. This is included in ferry tickets. Tourist accommodation in Greece charges a nightly accommodation tax of EUR 0.50–4.00 depending on hotel category."),
        ],
        "faq_proc": [
            ("How long does Greece Schengen visa processing take in 2026?",
             "Standard Greece Schengen visa processing is 15 working days. During peak summer season (May–August), this can extend to 30 working days. Apply at least 6–8 weeks before summer travel and 4 weeks before off-peak travel. Applications can be submitted up to 6 months in advance."),
            ("How do I track my Greece Schengen visa application?",
             "You can track your application status through the VFS Global portal using your application reference number, or directly with the Greek consulate. Some consulates send SMS and email updates. Contact VFS customer support if no update is received after 15 working days."),
            ("Can I get an expedited Greece Schengen visa?",
             "Greece does not offer a standard expedited Schengen visa service. For genuine emergencies (medical, bereavement), contact the Greek consulate directly with supporting documents. Priority processing may be arranged at the consulate's discretion."),
            ("What happens if my Greece Schengen visa is refused?",
             "You will receive a refusal notice stating the reason. You can reapply after addressing the deficiency (usually insufficient financial proof or incomplete documentation). You can also appeal the decision to the Greek authorities within the timeframe stated in the refusal notice."),
        ],
        "howto_req": [
            ("Check visa requirements at mfa.gr", "Verify whether your nationality needs a Schengen visa for Greece. EU, EEA, UK, US, Canadian, and Australian citizens enter visa-free."),
            ("Prepare all required documents", "Gather passport (10 years or less, 3+ months validity), ICAO photos, travel insurance, flight bookings, hotel reservations, bank statements, and employment proof."),
            ("Book your VFS appointment", "Schedule an in-person appointment at the nearest VFS Global centre or Greek consulate. Bring all original documents plus photocopies."),
            ("Attend appointment and submit biometrics", "Submit your application in person. Biometrics (fingerprints) are collected at the VFS centre. First-time Schengen applicants must always apply in person."),
            ("Pay EUR 80 fee at appointment", "Pay the government visa fee and VFS service charge at the appointment. Collect your receipt and application tracking number."),
        ],
        "howto_fee": [
            ("Confirm EUR 80 as the standard adult fee", "Check mfa.gr for the latest fee schedule, including any reductions for EU-facilitation agreement countries (EUR 35 reduced fee)."),
            ("Add VFS service fee to your budget", "Total cost is EUR 95–110 per adult (EUR 80 government fee + EUR 15–30 VFS fee). Check your local VFS centre for their exact service charge."),
            ("Check if you qualify for a fee waiver", "Children under 6, and certain humanitarian cases, may be exempt from the EUR 80 fee. Verify eligibility criteria at the Greek consulate."),
            ("Pay at the VFS centre", "Accepted payment methods vary by country. Check your local VFS centre website. Most accept cash and local debit card. Some also accept credit cards."),
            ("Request and keep a fee receipt", "Always request a written receipt for your fee payment. You will need it if there is any dispute about your application status or to claim a refund in the rare event of an error."),
        ],
        "howto_proc": [
            ("Apply at least 15 working days before travel", "Submit your application a minimum of 15 working days before departure. In summer months (June–August) apply 6–8 weeks early due to high demand."),
            ("Submit a complete and accurate application", "Use the official document checklist from mfa.gr. Missing or incorrect documents are the main cause of delays and refusals."),
            ("Track your application status", "Use your VFS reference number to track status online or sign up for SMS/email alerts from the VFS portal."),
            ("Collect passport from VFS", "After approval notification, collect your passport from the VFS centre or opt for courier delivery. Verify the visa sticker for accuracy before leaving the counter."),
            ("Respect visa conditions on entry", "Present your passport and printed visa at Greek border control. Stay within the 90-day limit in any 180-day period and respect single/double/multiple entry conditions on your visa sticker."),
        ],
    },

    "switzerland": {
        "label": "Switzerland",
        "flag": "ch",
        "visa_page": "visa-switzerland.html",
        "fee": "EUR 80 (embassy fee for Schengen)",
        "stay": "90 days within 180-day period (Schengen)",
        "processing": "15 working days",
        "portal": "eda.admin.ch",
        "portal_url": "https://www.eda.admin.ch",
        "visa_type": "Schengen Visa (type C)",
        "free_note": "Visa-free for EU/EEA, UK, US, Canada, Australia, Japan and many others",
        "eligibility": "Non-EU/EEA nationals may need Schengen visa via Swiss embassy",
        "entry": "Single, double or multiple entry",
        "currency": "CHF (Swiss Franc)",
        "region": "Central Europe",
        "schengen": True,
        "extra_fees": [
            ("Schengen short-stay visa (adult)", "EUR 80 (~CHF 86)"),
            ("Schengen visa (child 6–11)", "EUR 40 (~CHF 43)"),
            ("Schengen visa (child under 6)", "Free"),
            ("VFS Global or TLScontact service fee", "EUR 15–30"),
            ("National C permit (long stay)", "CHF 65–100"),
            ("Swiss work permit (employer quota)", "CHF 100–200"),
        ],
        "req_rows": [
            ("Valid passport", "Issued within 10 years; valid 3+ months after return; 2 blank pages"),
            ("Completed Schengen application form", "Signed and dated; downloaded from eda.admin.ch"),
            ("Passport-style photos", "2 ICAO-standard photos, 35×45 mm"),
            ("Travel insurance", "EUR 30,000 minimum; valid for Switzerland and full Schengen area"),
            ("Round-trip flight itinerary", "Confirmed booking or reservation showing entry/exit"),
            ("Accommodation proof", "Hotel bookings or host invitation letter with Swiss residence proof"),
            ("Bank statements", "3–6 months; min EUR 100/day for Switzerland"),
            ("Employment or income proof", "Payslips, employer letter, business registration, or pension award"),
        ],
        "processing_rows": [
            ("Schengen C visa – standard", "15 working days"),
            ("Schengen C visa – peak season (summer/winter)", "Up to 30 working days"),
            ("Swiss national (D) long-stay visa", "1–3 months"),
            ("Work permit (employer-sponsored)", "1–3 months"),
            ("Family reunification permit", "2–4 months"),
            ("Swiss passport (naturalisation)", "2–5 years residency requirement"),
        ],
        "faq_req": [
            ("What documents do I need for a Switzerland Schengen visa in 2026?",
             "You need a valid passport (issued within 10 years, 3+ months validity after return, 2 blank pages), 2 ICAO passport photos, completed Schengen application form, travel insurance with EUR 30,000 minimum coverage, confirmed round-trip flight booking, accommodation proof (hotel or host letter), 3–6 months bank statements, and employment or income proof."),
            ("Is the Switzerland Schengen visa different from other Schengen visas?",
             "Switzerland is part of the Schengen area but is not an EU member state. The Schengen visa issued by Switzerland follows the same rules as other Schengen visas: valid for 90 days in 180-day period, multiple-entry option available. The application process goes through Swiss embassies or VFS Global/TLScontact centres."),
            ("How much money do I need for a Switzerland Schengen visa?",
             "Switzerland is one of Europe's most expensive countries. Bank statements should show a minimum of EUR 100 (approx CHF 100) per day of your intended stay, plus evidence of return flight and accommodation. More funds are recommended for Switzerland compared to other Schengen destinations."),
            ("Can I visit other Schengen countries on a Switzerland Schengen visa?",
             "Yes. A Swiss-issued Schengen visa is valid throughout all 27 Schengen member states. However, Switzerland is your main destination, so your visa is issued for your stay in Switzerland. You can make short side trips to other Schengen countries within your 90-day allowance."),
        ],
        "faq_fee": [
            ("How much does a Switzerland Schengen visa cost in 2026?",
             "The Switzerland Schengen visa fee is EUR 80 (~CHF 86) for adults and EUR 40 for children aged 6–11. Children under 6 are free. VFS Global or TLScontact service fees add EUR 15–30 per application. Total cost per adult application is approximately EUR 95–110."),
            ("Are Switzerland Schengen visa fees refundable?",
             "No. The EUR 80 fee is non-refundable even if the visa is refused or you cancel your trip. VFS service fees are also generally non-refundable once your appointment has been processed. Ensure all documents are correct and meeting financial requirements before submitting."),
            ("Does Switzerland charge more because it is more expensive than other Schengen countries?",
             "No. The Schengen visa application fee is standardised across all Schengen member states at EUR 80 for adults. Switzerland cannot charge a higher application fee than other Schengen states. The difference is that Swiss immigration expects higher financial proof (EUR 100/day vs EUR 50/day in some other countries)."),
            ("Are there reduced fees for Switzerland Schengen visa?",
             "Citizens of countries with EU visa facilitation agreements (such as Ukraine, Georgia, Moldova, Kosovo, Western Balkans) benefit from a reduced EUR 35 Schengen fee that also applies to Switzerland as a Schengen member. Children under 6 are always exempt regardless of nationality."),
        ],
        "faq_proc": [
            ("How long does Switzerland Schengen visa processing take in 2026?",
             "Standard processing for a Switzerland Schengen visa is 15 working days. During peak ski season (December–March) and summer (June–August), processing may extend to 30 working days. Apply at least 6–8 weeks before peak season travel and 3–4 weeks before off-peak travel."),
            ("Can I get an expedited Switzerland Schengen visa?",
             "Switzerland does not offer a guaranteed expedited Schengen visa service. In case of genuine emergency travel (medical, family bereavement), contact the Swiss embassy directly with supporting documentation to request priority consideration."),
            ("How do I track my Switzerland Schengen visa application?",
             "You can track your application at the VFS Global or TLScontact portal using your application reference number. The Swiss embassy may also send email/SMS updates. Contact VFS customer service if you have received no update after 15 working days."),
            ("Do I need to re-apply at a Swiss embassy even if I already have a Schengen visa?",
             "If your existing Schengen visa was issued by another Schengen country and is still valid, you can enter Switzerland without a new application. However, if you need a new Schengen visa specifically for Switzerland, apply to the Swiss embassy or consulate in your country through eda.admin.ch."),
        ],
        "howto_req": [
            ("Check visa requirements at eda.admin.ch", "Confirm whether your nationality needs a Schengen visa for Switzerland. EU, EEA, UK, US, Canadian, and Australian citizens enter visa-free."),
            ("Gather all required documents", "Prepare passport (10 years max age, 3+ months validity), 2 ICAO photos, insurance (EUR 30,000+), flight booking, hotel confirmation, bank statements (EUR 100/day minimum), and employment proof."),
            ("Book your appointment", "Schedule at the nearest Swiss embassy, VFS Global or TLScontact centre. First-time Schengen applicants must apply in person for biometrics."),
            ("Attend appointment and submit application", "Arrive on time with all original documents and photocopies. Submit biometrics and pay the EUR 80 fee plus service charges."),
            ("Await decision and collect passport", "Wait 15 working days (longer in peak seasons). Collect your passport from the application centre when notified."),
        ],
        "howto_fee": [
            ("Confirm EUR 80 government fee", "The Schengen adult visa fee is EUR 80 for all nationalities (or EUR 35 for facilitation agreement countries). Check eda.admin.ch for any recent changes."),
            ("Add VFS or TLScontact service fee", "Budget EUR 15–30 for the application centre service fee on top of the EUR 80 government fee, making total approximately EUR 95–110."),
            ("Prepare payment for the appointment", "Check whether your local VFS/TLScontact centre accepts cash, debit card, or credit card. Bring the correct amount in the accepted local currency."),
            ("Keep all receipts", "Request and store fee receipts as proof of payment. You will need them if there is any dispute about your application or to track your passport collection."),
            ("Budget for higher cost of stay", "Switzerland is expensive. Ensure your bank statements show EUR 100/day of stay. Immigration officers at the border may ask about your financial means."),
        ],
        "howto_proc": [
            ("Apply 15+ working days before travel", "Submit your application at least 15 working days before travel. For ski season (December–February) or summer (June–August), apply 6–8 weeks early."),
            ("Use official checklist from eda.admin.ch", "Download and follow the official document checklist for your nationality. Missing documents are the primary cause of delays and refusals."),
            ("Track via VFS or embassy portal", "Use your application reference number to monitor status online. Sign up for email/SMS alerts where available."),
            ("Collect and inspect your passport", "Collect your passport from the application centre after notification. Immediately verify the visa sticker dates, entries, and duration of stay."),
            ("Enter Switzerland within visa validity", "Present your passport and visa at Swiss immigration. Stay within the 90-day Schengen limit. Switzerland operates 24/7 border controls; always carry your passport."),
        ],
    },

    "mexico": {
        "label": "Mexico",
        "flag": "mx",
        "visa_page": "visa-mexico.html",
        "fee": "Visa-free for 100+ countries; FMM card USD 30; consular visa USD 36",
        "stay": "180 days (visa-free / tourist card)",
        "processing": "Instant (visa-free + FMM); 3–5 days (consular visa)",
        "portal": "inm.gob.mx",
        "portal_url": "https://www.inm.gob.mx",
        "visa_type": "Visa-free / FMM Tourist Card / Consular Visa",
        "free_note": "Visa-free for 100+ nationalities including EU, UK, US, Canada, Japan, Australia",
        "eligibility": "Visa-free for 100+ nationalities; consular visa for others",
        "entry": "Multiple entry (visa-free); single entry (consular visa typical)",
        "currency": "MXN (Mexican Peso)",
        "region": "North America / Latin America",
        "schengen": False,
        "extra_fees": [
            ("FMM tourist card (air arrival)", "USD 30 (approx MXN 510); included in airfare from many origins"),
            ("FMM tourist card (land border)", "USD 30 (~MXN 510); paid at INM border booth"),
            ("Consular tourist visa (US applicants exempt)", "USD 36 (~MXN 612)"),
            ("Temporary resident visa", "USD 36 (~MXN 612) at consulate + INM card fee"),
            ("Permanent resident visa", "USD 36 (~MXN 612) + INM permanent card fee"),
            ("Work permit / FMM de trabajo", "Variable; employer-sponsored"),
        ],
        "req_rows": [
            ("Valid passport", "Minimum 6 months validity beyond intended stay"),
            ("Return or onward ticket", "Proof of departure from Mexico"),
            ("Sufficient funds", "Approx USD 1,000 per month of stay (informal guideline)"),
            ("FMM tourist card", "Completed at airport or border; free or USD 30 depending on origin"),
            ("Accommodation proof", "Hotel booking or host invitation (sometimes requested)"),
            ("Travel insurance", "Strongly recommended; not mandatory for most nationalities"),
            ("No prior immigration violation", "Clean Mexico immigration record required"),
        ],
        "processing_rows": [
            ("Visa-free entry + FMM card", "Instant on arrival"),
            ("FMM card (land border)", "15–30 minutes at INM booth"),
            ("Consular tourist visa", "3–5 business days"),
            ("Temporary resident visa", "10–15 business days"),
            ("Permanent resident visa", "10–15 business days"),
            ("Naturalization (citizenship)", "5 years legal residence minimum"),
        ],
        "faq_req": [
            ("What documents do I need to enter Mexico in 2026?",
             "Citizens of 100+ countries including EU, UK, US, Canada, Japan, and Australia can enter Mexico visa-free. You need a valid passport (6+ months), a completed FMM tourist card (given on the plane or at land borders), and proof of a return or onward ticket. Some airlines and border officers may ask for accommodation details and proof of sufficient funds."),
            ("What is the Mexico FMM tourist card?",
             "The Forma Migratoria Múltiple (FMM) is a tourist entry card required for all visitors to Mexico. For air arrivals, the fee is typically included in your airfare and the form is completed on the plane. For land border crossings, you complete the FMM at an INM booth and pay approximately USD 30 in cash. Keep the bottom portion of the FMM — you must return it when you leave Mexico."),
            ("How long can I stay in Mexico without a visa?",
             "Visa-free nationals can stay in Mexico for up to 180 days per visit. The immigration officer at the border writes the number of permitted days on your FMM card (up to 180). If you plan a short trip, you may receive fewer days; you can politely request 180 days when entering."),
            ("Do I need to keep my Mexico FMM tourist card?",
             "Yes. Keep the bottom tear-off portion of your FMM throughout your stay in Mexico. You must present it to the immigration officer when departing. Losing your FMM requires obtaining a replacement at an INM office (Instituto Nacional de Migración) and paying a replacement fee of approximately MXN 700 (~USD 40)."),
        ],
        "faq_fee": [
            ("How much does it cost to visit Mexico in 2026?",
             "Mexico is free to enter for 100+ nationalities with no visa required. The FMM tourist card costs approximately USD 30 (~MXN 510) at land borders and is usually included in your airfare. If your nationality requires a consular visa, the fee is USD 36 (~MXN 612). There are no additional airport entry taxes for tourists."),
            ("Is the FMM fee included in my airline ticket?",
             "For most international air routes into Mexico, the FMM fee is included in the airline ticket price as an airport fee or tourism charge. Check your flight booking details. If you are crossing a land border from the US, Guatemala, or Belize, you pay the FMM fee in cash at the INM border booth."),
            ("Is there an airport departure tax for Mexico?",
             "International departure taxes are typically included in the price of international airline tickets departing Mexico. If you purchased your ticket from within Mexico, check whether TUA (Tarifa de Uso de Aeropuerto, the airport use fee) is included. Most modern airline tickets include this automatically."),
            ("Do I pay the FMM fee on a day trip to Mexico from the US?",
             "If you are making a short day trip or crossing the border briefly (less than 20–25 km from the border, e.g., to Tijuana or Juarez), you may be exempt from the FMM fee. However, for anything beyond the border zone or overnight stays, the USD 30 FMM applies. Ask at the INM booth when crossing."),
        ],
        "faq_proc": [
            ("How quickly can I enter Mexico for visa-free nationals?",
             "Citizens of 100+ countries enter Mexico instantly upon arrival. The FMM tourist card is completed on the plane (for air arrivals) or at the INM booth (land border, 15–30 minutes). There is no advance application or processing time required. Simply present your passport and completed FMM at the immigration counter."),
            ("How long does a Mexico consular visa take to process?",
             "A Mexico consular tourist visa is processed in 3–5 business days at a Mexican consulate or embassy. Some consulates may process faster; check with your local consulate. Temporary and permanent resident visas take 10–15 business days."),
            ("Can I extend my stay in Mexico beyond the permitted days?",
             "You can request an extension of your FMM stay at an INM office before your permitted period expires. Extensions are discretionary and not guaranteed for tourism purposes. The more common approach is to do a border run (leave and re-enter Mexico) to obtain a new 180-day FMM."),
            ("What happens if I overstay my Mexico tourist card?",
             "Overstaying your FMM is a migration violation. You will be required to pay a fine at the airport or border before departure (approximately MXN 2,670–6,000 per day depending on length of overstay). Significant overstays may result in a ban from re-entry to Mexico."),
        ],
        "howto_req": [
            ("Check if you need a visa for Mexico", "Visit inm.gob.mx to check your nationality's status. Over 100 nationalities including EU, UK, US, Canada, Japan, and Australia are visa-exempt."),
            ("Prepare your travel documents", "Bring a valid passport (6+ months validity), return or onward ticket, and accommodation details. The FMM tourist card will be issued at the airport or border."),
            ("Complete the FMM tourist card", "For air arrivals: fill in the form on the plane or at immigration. For land border crossings: complete the FMM at the INM booth and pay approximately USD 30 in cash."),
            ("Pass Mexico immigration", "Present your passport, FMM, and any supporting documents to the immigration officer. They will stamp your passport and write your permitted days (up to 180) on the FMM."),
            ("Keep your FMM throughout your stay", "Store the bottom portion of the FMM in your passport. You must return it when you leave Mexico. Losing it requires a replacement from INM at extra cost."),
        ],
        "howto_fee": [
            ("Confirm your visa-free status", "Check inm.gob.mx — 100+ nationalities enter Mexico free. No visa application fee applies for eligible passport holders."),
            ("Understand the FMM card cost", "The FMM tourist card costs USD 30 at land borders (cash only at most INM booths). For air arrivals, this fee is typically included in your ticket."),
            ("Check if FMM is included in your airline ticket", "Review your flight booking for 'tourist card', 'FMM', or 'Mexico entry fee' in the fee breakdown. If not mentioned, budget USD 30 for the land border payment."),
            ("Carry USD or MXN cash for land crossing", "INM border booths accept US dollars and Mexican pesos but may not accept credit cards. Carry sufficient small denomination bills for the USD 30 FMM fee."),
            ("Budget for potential replacement FMM", "Losing your FMM requires a replacement at an INM office at a cost of approximately MXN 700 (~USD 40). Keep your FMM safe throughout your stay."),
        ],
        "howto_proc": [
            ("No advance application needed (visa-free)", "Citizens of 100+ nationalities can book their Mexico trip without any advance visa application. Just ensure your passport is valid for 6+ months."),
            ("Complete FMM on the plane or at the border", "For air arrivals, complete the paper or electronic FMM form provided on the aircraft or at the airport kiosk before reaching immigration."),
            ("Approach Mexico immigration counter", "Present your passport and completed FMM to the immigration officer. They will stamp your passport and authorise your stay (up to 180 days)."),
            ("Retain FMM bottom portion", "The immigration officer keeps the top of the FMM; you keep the bottom. Store it inside your passport throughout your time in Mexico."),
            ("Surrender FMM on departure", "Present your FMM to the departure immigration officer when leaving Mexico. For air departures, airline check-in staff or departure immigration will collect it."),
        ],
    },
}

# ── HTML template ──────────────────────────────────────────────────────────────

def head_block(title, description, slug, country_key, flag_code, lang_slug):
    """Return the <head> section."""
    canonical = f"https://www.evisa-card.com/en/{slug}"
    keywords = f"{lang_slug.replace('-', ' ')}, {country_key} visa 2026, {country_key} evisa, {country_key} visa requirements, {country_key} visa fees, {country_key} visa processing time"
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
    <meta content="{keywords}" name="keywords"/>
    <meta content="index, follow" name="robots" />
    <link href="{canonical}" rel="canonical" />
    <!-- Open Graph -->
    <meta content="{title}" property="og:title" />
    <meta content="{description}" property="og:description" />
    <meta content="website" property="og:type" />
    <meta content="{canonical}" property="og:url" />
    <meta content="https://www.evisa-card.com/images/og-image.jpg" property="og:image" />
    <!-- Fonts & CSS -->
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&amp;display=swap" rel="stylesheet" />
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


def navbar_block(country_key, slug, flag_code):
    return f"""<body>
    <!-- ======== HEADER ========= -->
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
                            <a class="dropdown-item" href="/fr/{slug}"><span class="fi fi-fr"></span> Français</a>
                            <a class="dropdown-item" href="/es/{slug}"><span class="fi fi-es"></span> Español</a>
                            <a class="dropdown-item" href="/pt/{slug}"><span class="fi fi-br"></span> Português</a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>"""


def footer_js_block():
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
    <script src="../js/main.js"></script>"""


def faq_jsonld(faq_items):
    import json
    entities = []
    for q, a in faq_items:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'


def howto_jsonld(name, steps):
    import json
    step_objs = [{"@type": "HowToStep", "name": f"Step {i+1}", "text": text}
                 for i, (name_s, text) in enumerate(steps)]
    data = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "description": f"Step-by-step guide: {name} in 2026.",
        "step": step_objs
    }
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'


def internal_links(d, country_key):
    vp = d["visa_page"]
    label = d["label"]
    return f"""<div class="mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Guides</h3>
    <div>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{vp}">{label} Visa Overview</a>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="how-to-apply-evisa.html">How to Apply for an eVisa</a>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-documents-checklist.html">Visa Documents Checklist</a>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-processing-times.html">Global Processing Times</a>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-photo-requirements.html">Visa Photo Requirements</a>
        <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
    </div>
</div>"""


def eeat_block():
    return """<div class="alert alert-info small mt-4"><strong>Editorial note:</strong> Verified by our immigration team. Last updated: March 2026. Sources: official embassy websites.</div>"""


def table_rows(rows):
    html = ""
    for label, value in rows:
        html += f"<tr><th>{label}</th><td>{value}</td></tr>\n"
    return html


# ── Page 1: Requirements ──────────────────────────────────────────────────────

def gen_requirements(country_key, d):
    label = d["label"]
    flag = d["flag"]
    slug = f"{country_key}-visa-requirements.html"
    title = f"{label} eVisa Requirements 2026 — Documents, Eligibility &amp; How to Apply"
    raw_title = f"{label} eVisa Requirements 2026 — Documents, Eligibility & How to Apply"
    desc_raw = (
        f"{label} visa requirements 2026: documents checklist, eligibility, passport validity, photos & step-by-step application. Official {d['portal']}."
    )
    desc = desc_raw[:155]

    h1 = f'<span class="fi fi-{flag} mr-2"></span>{label} eVisa Requirements 2026: Documents, Eligibility &amp; How to Apply'

    faq_ld = faq_jsonld(d["faq_req"])
    howto_ld = howto_jsonld(f"How to Meet {label} eVisa Requirements", d["howto_req"])
    intro_schengen = ""
    if d["schengen"]:
        intro_schengen = f"As a Schengen member, {label} issues Type C short-stay visas valid throughout all 27 Schengen states. Non-EU nationals should apply through the {label} embassy or an authorised VFS Global application centre in their country of residence. EU, EEA, UK, US, Canadian, and Australian citizens enjoy visa-free access."
    else:
        intro_schengen = f"{d['free_note']}. The {d['visa_type']} system makes {label} highly accessible — apply online at <a href='{d['portal_url']}' target='_blank' rel='noopener'>{d['portal']}</a>."

    rows_html = table_rows(d["req_rows"])

    content = f"""
<section class="ftco-section"><div class="container"><article class="country-page">

<h1>{h1}</h1>

<p class="lead">Planning to visit {label} in 2026? This guide covers every document you need, who is eligible, and the exact steps to apply for a {label} {d['visa_type']}.</p>

<h2 id="overview">Overview: {label} Visa &amp; Entry Requirements 2026</h2>
<p>{intro_schengen}</p>
<p>The official fee is <strong>{d['fee']}</strong> with a standard processing time of <strong>{d['processing']}</strong>. The permitted stay is up to <strong>{d['stay']}</strong>. Entry is {d['entry']}. Currency in use: {d['currency']}.</p>

<h2 id="documents">Required Documents for {label} {d['visa_type']} 2026</h2>
<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Document Requirements — {label}</th></tr></thead>
<tbody>
{rows_html}
</tbody>
</table>
<p>All documents must be originals or certified copies unless stated otherwise. Translations into the official language(s) of {label} or English must be certified by an accredited translator.</p>

<h2 id="eligibility">Who Is Eligible for a {label} Visa?</h2>
<p><strong>Eligibility:</strong> {d['eligibility']}.</p>
<p>Special note: {d['free_note']}.</p>
<p>Children under 18 must travel with a valid passport of their own. Minors travelling without both parents may need a notarised parental consent letter. Always verify current rules at the official {label} immigration authority before travel.</p>

<h2 id="how-to-apply">How to Apply: Step-by-Step for {label} in 2026</h2>
<ol>
{"".join(f"<li><strong>{sn}</strong> — {st}</li>" for sn, st in d["howto_req"])}
</ol>
<p>Apply via the official portal: <a href="{d['portal_url']}" target="_blank" rel="noopener">{d['portal']}</a>. Avoid third-party agents who charge unnecessary service fees on top of the official government fee.</p>

{eeat_block()}

{internal_links(d, country_key)}

</article></div></section>
"""

    return assemble(raw_title, title, desc, slug, country_key, flag, content, faq_ld, howto_ld, slug)


# ── Page 2: Fees ──────────────────────────────────────────────────────────────

def gen_fees(country_key, d):
    label = d["label"]
    flag = d["flag"]
    slug = f"{country_key}-visa-fees.html"
    title = f"{label} Visa Fees 2026 — Official Costs, Payment Methods &amp; Refund Policy"
    raw_title = f"{label} Visa Fees 2026 — Official Costs, Payment Methods & Refund Policy"
    desc_raw = (
        f"{label} visa fees 2026: official {d['visa_type']} costs {d['fee']}, payment methods, children fees, refund policy. Verified {d['portal']}."
    )
    desc = desc_raw[:155]

    h1 = f'<span class="fi fi-{flag} mr-2"></span>{label} Visa Fees 2026: Full Cost Breakdown &amp; Payment Guide'

    faq_ld = faq_jsonld(d["faq_fee"])
    howto_ld = howto_jsonld(f"How to Pay {label} Visa Fees", d["howto_fee"])

    rows_html = table_rows(d["extra_fees"])

    content = f"""
<section class="ftco-section"><div class="container"><article class="country-page">

<h1>{h1}</h1>

<p class="lead">Understand every cost involved in applying for a {label} visa in 2026 — from the official government fee to service charges, children's discounts, and refund policies.</p>

<h2 id="official-fees">Official {label} Visa Fee Schedule 2026</h2>
<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Fee Schedule — {label} {d['visa_type']}</th></tr></thead>
<tbody>
{rows_html}
</tbody>
</table>
<p>All fees listed are official government charges. Additional service fees may apply at VFS Global or other authorised application centres. Fees are subject to change; always verify at <a href="{d['portal_url']}" target="_blank" rel="noopener">{d['portal']}</a>.</p>

<h2 id="payment-methods">Accepted Payment Methods</h2>
<p>Most {label} visa applications accept payment by Visa and MasterCard credit or debit cards through the official online portal. Some embassies and consulates also accept bank transfers, money orders, or cash in local currency at the application centre. Check your local consulate or VFS Global website for the accepted payment options in your country.</p>
<p>Important: never pay visa fees to unofficial third-party agents who claim to offer "faster processing." The official fee at the government portal is always the same regardless of who submits it.</p>

<h2 id="refund-policy">Refund Policy</h2>
<p>The {label} visa application fee is <strong>non-refundable</strong> regardless of outcome. This applies even if:</p>
<ul>
  <li>Your visa application is refused</li>
  <li>You cancel your trip after applying</li>
  <li>You withdraw your application before a decision is made</li>
</ul>
<p>To minimise the risk of losing your fee, ensure all documents are complete and correct before submitting. Review the official checklist at <a href="{d['portal_url']}" target="_blank" rel="noopener">{d['portal']}</a>.</p>

<h2 id="tips">Money-Saving Tips for {label} Visa Fees 2026</h2>
<p>Apply directly on the official government portal to avoid third-party surcharges. Check whether your nationality qualifies for a reduced-fee or visa-free arrangement with {label}. For families, confirm children&apos;s fee exemptions or reductions before applying. If applying for multiple {label} visas in the same year, a multiple-entry visa may offer better value than several single-entry fees.</p>

{eeat_block()}

{internal_links(d, country_key)}

</article></div></section>
"""

    return assemble(raw_title, title, desc, slug, country_key, flag, content, faq_ld, howto_ld, slug)


# ── Page 3: Processing Time ───────────────────────────────────────────────────

def gen_processing(country_key, d):
    label = d["label"]
    flag = d["flag"]
    slug = f"{country_key}-visa-processing-time.html"
    title = f"{label} Visa Processing Time 2026 — How Long &amp; How to Track Your Application"
    raw_title = f"{label} Visa Processing Time 2026 — How Long & How to Track Your Application"
    desc_raw = (
        f"{label} visa processing time 2026: {d['processing']} standard. Learn how to apply early, track status & avoid delays. Source: {d['portal']}."
    )
    desc = desc_raw[:155]

    h1 = f'<span class="fi fi-{flag} mr-2"></span>{label} Visa Processing Time 2026: Timelines, Tracking &amp; Tips'

    faq_ld = faq_jsonld(d["faq_proc"])
    howto_ld = howto_jsonld(f"How to Track Your {label} Visa Application", d["howto_proc"])

    rows_html = table_rows(d["processing_rows"])

    content = f"""
<section class="ftco-section"><div class="container"><article class="country-page">

<h1>{h1}</h1>

<p class="lead">How long does a {label} visa take in 2026? Standard processing is <strong>{d['processing']}</strong>. This guide covers all visa types, peak-season delays, tracking methods, and tips to avoid common hold-ups.</p>

<h2 id="processing-times">Processing Times by Visa Type — {label} 2026</h2>
<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Processing Times — {label}</th></tr></thead>
<tbody>
{rows_html}
</tbody>
</table>
<p>Processing times are estimates and may vary. Always apply with adequate lead time to account for unexpected delays. Official tracking: <a href="{d['portal_url']}" target="_blank" rel="noopener">{d['portal']}</a>.</p>

<h2 id="apply-early">When to Apply for a {label} Visa</h2>
<p>Apply as early as possible — most {label} visa applications can be submitted up to <strong>3–6 months before travel</strong>. The minimum lead time is the standard processing period of {d['processing']}, but applying earlier gives you time to correct any document errors, request missing records, or re-apply if necessary.</p>
<p>Peak travel periods (summer holidays, national festivals, Christmas/New Year) can double processing times at consulates and application centres. If you are travelling during these periods, submit your application at least 6–8 weeks in advance.</p>

<h2 id="tracking">How to Track Your {label} Visa Application</h2>
<p>Most {label} visa applications can be tracked online using your application reference number. After submitting, you should receive:</p>
<ul>
  <li>An email confirmation with your reference number</li>
  <li>A link to the online tracking portal at <a href="{d['portal_url']}" target="_blank" rel="noopener">{d['portal']}</a></li>
  <li>Email and/or SMS updates at key stages (receipt, decision, collection)</li>
</ul>
<p>If no update is received within the expected processing period, contact the processing centre using your reference number. Do not book non-refundable flights or accommodation until your visa is confirmed.</p>

<h2 id="delays">Common Causes of Processing Delays</h2>
<p>The most common reasons for {label} visa processing delays are: incomplete documentation, passport photos not meeting official specifications, insufficient financial proof, failure to provide certified translations, high application volumes during peak season, and discrepancies between the application form and supporting documents. Use the official checklist from <a href="{d['portal_url']}" target="_blank" rel="noopener">{d['portal']}</a> and double-check all details before submission.</p>

{eeat_block()}

{internal_links(d, country_key)}

</article></div></section>
"""

    return assemble(raw_title, title, desc, slug, country_key, flag, content, faq_ld, howto_ld, slug)


# ── Assemble full page ─────────────────────────────────────────────────────────

def assemble(raw_title, title_html, desc, slug, country_key, flag, body_content, faq_ld, howto_ld, page_slug):
    d = COUNTRIES[country_key]
    head = head_block(raw_title, desc, page_slug, country_key, flag, slug)
    nav = navbar_block(country_key, page_slug, flag)
    foot = footer_js_block()
    return f"""{head}
{nav}
{body_content}
{faq_ld}
{howto_ld}
{foot}
</body>
</html>"""


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []
    for country_key, d in COUNTRIES.items():
        pages = [
            (f"{country_key}-visa-requirements.html", gen_requirements(country_key, d)),
            (f"{country_key}-visa-fees.html", gen_fees(country_key, d)),
            (f"{country_key}-visa-processing-time.html", gen_processing(country_key, d)),
        ]
        for filename, html in pages:
            path = os.path.join(OUT_DIR, filename)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(filename)
            print(f"  Created: {filename}")

    print(f"\nTotal files created: {len(created)}")
    assert len(created) == 30, f"Expected 30 files, got {len(created)}"
    print("All 30 files generated successfully.")


if __name__ == "__main__":
    main()
