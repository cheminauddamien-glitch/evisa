#!/usr/bin/env python3
"""
gen_visa_extension.py
Generates 15 visa-extension guide pages for the top tourist-destination countries.
Output: www/en/{country}-visa-extension.html
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Per-country data
# ---------------------------------------------------------------------------
COUNTRIES = [
    {
        "slug": "thailand",
        "name": "Thailand",
        "flag": "th",
        "title": "Thailand Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Thailand visa extension 2026: extend your tourist visa 30 days at immigration for THB 1,900. Deadlines, documents, border run tips and overstay penalties.",
        "keywords": "thailand visa extension 2026, extend thailand tourist visa, thailand immigration extension, thailand overstay penalty",
        "h1": "How to Extend Your Thailand Visa in 2026",
        "intro": (
            "Thailand is one of the world's most-visited destinations, and many tourists find themselves wanting to stay longer than originally planned. "
            "The good news is that Thailand allows visa extensions at local immigration offices, making it relatively straightforward to add extra time to your stay."
        ),
        "can_extend": (
            "Yes — Thailand allows tourist visa holders and most visa-exempt visitors to extend their stay at any of the country's immigration offices. "
            "The standard extension grants an additional <strong>30 days</strong> on top of your current permitted stay. "
            "If you entered on a 60-day tourist visa (TR), you can extend for 30 more days, giving you a maximum of 90 days in total. "
            "Visa-exempt visitors who received 30 or 60 days at the border may also apply for the same 30-day extension. "
            "An alternative to an in-country extension is a <em>border run</em> — leaving Thailand and re-entering to receive a fresh entry stamp — though authorities have been known to question travellers who do this repeatedly. "
            "For longer stays, a multiple-entry tourist visa (METV) or a Non-Immigrant visa is a better long-term solution."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport with at least one blank page</li>"
            "<li>Completed TM.7 extension application form (available at immigration offices)</li>"
            "<li>1 recent passport-sized photo (4 × 6 cm, white background)</li>"
            "<li>Photocopy of passport bio page, current visa/entry stamp, and departure card (TM.6)</li>"
            "<li>Proof of onward travel (flight booking or confirmed itinerary)</li>"
            "<li>Proof of accommodation (hotel booking or lease agreement)</li>"
            "<li>Extension fee: <strong>THB 1,900</strong> (cash)</li>"
            "</ul>"
        ),
        "steps": [
            ("Locate your nearest immigration office", "Find the closest immigration office — major ones are in Bangkok (Chaeng Watthana), Phuket Town, Chiang Mai, and Pattaya. Check the Immigration Bureau website for a full list."),
            ("Prepare your documents", "Complete the TM.7 form (free at the office). Gather your passport, photocopies, a passport photo, proof of accommodation, and the THB 1,900 cash fee."),
            ("Arrive early", "Immigration offices are open Mon–Fri 08:30–16:30 (excluding public holidays). Queues can be long; arriving before 08:00 is advisable, especially in tourist areas."),
            ("Submit your application", "Hand your documents to the officer at the extension counter. They will review everything and may ask brief questions about your travel plans."),
            ("Receive your new stamp", "If approved (same-day in most cases), your passport is stamped with the new permitted-to-stay date. Double-check the date before leaving the counter."),
        ],
        "overstay": (
            "Overstaying in Thailand is taken seriously. The fine is <strong>THB 500 per day</strong> (maximum THB 20,000 if you turn yourself in; potentially more if caught at the border). "
            "An overstay of more than 90 days triggers a ban from re-entering Thailand: 90 days to 1 year overstay = 1-year ban; 1–3 years overstay = 3-year ban; 3–5 years = 5-year ban; over 5 years = 10-year ban. "
            "If detained for overstay you may also face immigration detention before deportation. Always ensure you extend your visa or depart before your permitted-stay date expires."
        ),
        "table_rows": [
            ("Visa-exempt extension (30 days)", "30 days", "THB 1,900", "Any Immigration Office", "Same day"),
            ("Tourist Visa TR extension (30 days)", "30 days", "THB 1,900", "Any Immigration Office", "Same day"),
            ("Border Run (re-entry)", "New 30–60 days", "Free (travel costs)", "Border crossing", "Immediate"),
            ("Multiple-Entry Tourist Visa (METV)", "Up to 6 months / 60 days per entry", "THB 5,000", "Thai Embassy / Consulate", "Varies"),
        ],
        "apply_deadline": "Apply at least <strong>7 days before</strong> your current permitted-stay date expires.",
        "official_link": "https://www.immigration.go.th",
        "official_link_text": "Thailand Immigration Bureau",
    },
    {
        "slug": "india",
        "name": "India",
        "flag": "in",
        "title": "India Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "India visa extension 2026: extend a regular tourist visa at FRRO for USD 30. e-Tourist visa cannot be extended. Documents, steps and overstay penalties.",
        "keywords": "india visa extension 2026, extend india tourist visa, india FRRO extension, india visa overstay",
        "h1": "How to Extend Your India Visa in 2026",
        "intro": (
            "India is one of the world's most diverse travel destinations, attracting millions of visitors each year. "
            "If you need more time to explore its heritage sites, mountains, and coastlines, understanding the visa extension process is essential — "
            "the rules differ significantly between the popular e-Tourist Visa and a regular sticker visa."
        ),
        "can_extend": (
            "Whether you can extend depends on the type of visa you hold. "
            "<strong>e-Tourist Visa (eTV)</strong> — India's electronic tourist visa is <em>not extendable</em>. You must exit India before your eTV expires and, if eligible, apply for a fresh eTV from outside the country. "
            "<strong>Regular Tourist Visa (sticker visa)</strong> — a conventional tourist visa issued at an Indian embassy or consulate <em>can</em> be extended. "
            "Extensions are processed by the Foreigners Regional Registration Office (FRRO) or Foreigners Registration Office (FRO) in the city where you are staying. "
            "Extensions are typically granted in increments of up to 6 months, subject to the officer's discretion, and the total stay including extension usually cannot exceed 6 months in a calendar year."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport with blank pages</li>"
            "<li>Completed online registration on the FRRO e-FRRO portal (indianfrro.gov.in)</li>"
            "<li>Original visa and all photocopies of passport pages bearing stamps</li>"
            "<li>Proof of residential address in India (hotel registration certificate / rent agreement)</li>"
            "<li>Recent passport-sized photographs</li>"
            "<li>Proof of sufficient funds (bank statement or traveller's cheques)</li>"
            "<li>Extension fee: approx. <strong>USD 30</strong> (equivalent in INR)</li>"
            "<li>Valid reason for extension (tourism, medical, family)</li>"
            "</ul>"
        ),
        "steps": [
            ("Register on the e-FRRO portal", "Visit indianfrro.gov.in and create an account. Complete the online application form for a visa extension and upload the required documents."),
            ("Book an appointment", "After submitting the form, book an in-person appointment at your nearest FRRO/FRO office. Walk-in visits are generally not accepted."),
            ("Attend your appointment", "Arrive at the FRRO with all original documents and photocopies. The officer will review your case and may ask questions about your purpose of stay."),
            ("Pay the fee", "Pay the extension fee (approx. USD 30 equivalent in INR) as directed by the FRRO officer, usually via demand draft or online payment."),
            ("Receive the extension endorsement", "If approved, your passport will be endorsed with the new validity period. Processing typically takes a few days to a couple of weeks."),
        ],
        "overstay": (
            "Overstaying an Indian visa is a serious offence. Penalties include a fine, potential deportation, and a blacklisting ban that can prevent future entry to India for several years. "
            "The e-Tourist Visa specifically states that overstay will result in deportation and future visa refusals. "
            "Always apply for an extension at least <strong>15 days before</strong> your visa expires to give sufficient processing time. "
            "If you overstay inadvertently, report to the FRRO immediately rather than waiting to be caught at the airport."
        ),
        "table_rows": [
            ("e-Tourist Visa (eTV)", "NOT extendable", "N/A — must exit", "Apply new eTV from abroad", "N/A"),
            ("Regular Tourist Visa — extension", "Up to 6 months total", "~USD 30 (INR equivalent)", "FRRO / FRO office", "Days to weeks"),
        ],
        "apply_deadline": "Apply at least <strong>15 days before</strong> your current visa expires.",
        "official_link": "https://indianfrro.gov.in",
        "official_link_text": "India e-FRRO Portal",
    },
    {
        "slug": "indonesia",
        "name": "Indonesia",
        "flag": "id",
        "title": "Indonesia Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Indonesia visa extension 2026: extend your eVOA or social visa 30 days at immigration for IDR 350,000. Max 60 days total, one extension only. Full guide.",
        "keywords": "indonesia visa extension 2026, extend indonesia evoa, indonesia immigration extension, indonesia overstay fine",
        "h1": "How to Extend Your Indonesia Visa in 2026",
        "intro": (
            "Indonesia — home to Bali, Lombok, Raja Ampat, and hundreds of other stunning islands — regularly tops traveller bucket lists. "
            "If your initial 30-day stay isn't long enough, Indonesia offers a straightforward extension process for eligible visa holders. "
            "This guide covers the eVisa on Arrival (eVOA) extension and other relevant options."
        ),
        "can_extend": (
            "Indonesia's <strong>eVisa on Arrival (eVOA)</strong> can be extended <em>once</em> for an additional 30 days, bringing your maximum stay to 60 days. "
            "The extension must be applied for at a local Immigration Office (Kantor Imigrasi) before your current 30-day permit expires. "
            "The standard social/tourist visit visa obtained at embassies may also be extendable in country (up to 60 days additional, depending on visa class). "
            "Certain business or social visas allow multiple 30-day extensions for longer stays."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (6+ months validity, at least 1 blank page)</li>"
            "<li>Completed extension application form (available at the Immigration Office)</li>"
            "<li>Copy of passport bio page and existing visa/entry stamp</li>"
            "<li>Proof of accommodation in Indonesia</li>"
            "<li>Onward flight ticket</li>"
            "<li>Extension fee: <strong>IDR 350,000</strong> (approx. USD 22) — cash or bank transfer depending on office</li>"
            "</ul>"
        ),
        "steps": [
            ("Locate your nearest Immigration Office (Kantor Imigrasi)", "Indonesia has immigration offices in every major city and tourist area, including Denpasar (Bali), Jakarta, Surabaya, Yogyakarta, and Lombok."),
            ("Prepare your documents", "Fill in the extension application form and gather your passport, a copy of your visa/entry stamp, proof of accommodation, and your onward ticket."),
            ("Submit your application before expiry", "Visit the immigration office during business hours (Mon–Thu 08:00–16:00, Fri 08:00–16:30). Submit your documents at the front desk."),
            ("Pay the extension fee", "Pay IDR 350,000 (eVOA extension fee) as directed. Keep your receipt as proof of payment."),
            ("Collect your passport with new stamp", "Processing is usually same-day or next-day. Your passport will be stamped with the new expiry date of your extended stay."),
        ],
        "overstay": (
            "Indonesia imposes a fine of <strong>IDR 1,000,000 per day</strong> (approx. USD 63/day) for overstaying, up to a maximum of 60 days overdue. "
            "If you overstay more than 60 days you may be subject to immigration detention and deportation, and a re-entry ban can be imposed. "
            "The Bali immigration office in particular is known to enforce these rules strictly at Ngurah Rai Airport during departure. "
            "Always extend before your stamp expires or book your departure flight accordingly."
        ),
        "table_rows": [
            ("eVOA extension (30 days)", "30 days (max 60 days total)", "IDR 350,000 (~USD 22)", "Local Immigration Office", "Same day / next day"),
            ("Social/Tourist Visa extension", "Up to 60 days additional", "Varies by visa class", "Local Immigration Office", "1–3 days"),
        ],
        "apply_deadline": "Apply before your current 30-day eVOA or visa expires. Extensions are NOT available after expiry.",
        "official_link": "https://molina.imigrasi.go.id",
        "official_link_text": "Indonesia Immigration Portal",
    },
    {
        "slug": "vietnam",
        "name": "Vietnam",
        "flag": "vn",
        "title": "Vietnam Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Vietnam visa extension 2026: extend 30–90 days online via xuatnhapcanh.gov.vn for USD 25. Apply 3 days before expiry. Documents, steps and overstay rules.",
        "keywords": "vietnam visa extension 2026, extend vietnam e-visa, vietnam immigration extension online, vietnam overstay penalty",
        "h1": "How to Extend Your Vietnam Visa in 2026",
        "intro": (
            "Vietnam's scenic landscapes, UNESCO heritage sites, and world-famous cuisine keep travellers coming back for more. "
            "The country has streamlined its visa extension process — most tourists can now apply for extensions online, making it one of the more convenient options in Southeast Asia."
        ),
        "can_extend": (
            "Vietnam allows tourist visa holders to extend their stay for a further <strong>30 to 90 days</strong> depending on the visa type. "
            "Since 2023, Vietnam's e-Visa (single or multiple entry, 90 days) is also extendable. "
            "Extensions can be applied for online via the official immigration portal at <a href='https://xuatnhapcanh.gov.vn' target='_blank' rel='noopener'>xuatnhapcanh.gov.vn</a>. "
            "Alternatively, you can apply in person at the Immigration Department in major cities (Hanoi, Ho Chi Minh City, Da Nang). "
            "Travel agencies in Vietnam also offer assistance with extensions, but it is safest to use the official portal."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (6+ months validity)</li>"
            "<li>Current Vietnam visa or e-Visa (not yet expired)</li>"
            "<li>Online application via xuatnhapcanh.gov.vn (create account and complete form)</li>"
            "<li>Digital copy of passport bio page</li>"
            "<li>Proof of accommodation in Vietnam (hotel booking or rental contract)</li>"
            "<li>Extension fee: <strong>USD 25</strong> (paid online by card or via bank transfer)</li>"
            "</ul>"
        ),
        "steps": [
            ("Visit the official portal", "Go to xuatnhapcanh.gov.vn and create a user account if you do not already have one."),
            ("Select 'Extend Visa' and fill in the form", "Choose the extension option, enter your current visa number, passport details, and the new duration requested (30, 60, or 90 days)."),
            ("Upload documents", "Upload a scan of your passport bio page and your current visa. Attach proof of accommodation."),
            ("Pay the USD 25 fee", "Pay online by international credit/debit card or via the designated bank transfer method."),
            ("Wait for confirmation", "Processing typically takes 2–5 business days. You will receive an email or portal notification once approved. Apply at least 3 days before your current visa expires."),
        ],
        "overstay": (
            "Overstaying in Vietnam results in a fine of <strong>VND 500,000–1,500,000</strong> (approx. USD 20–60) depending on the length of overstay. "
            "Repeated or long overstays can lead to deportation and a multi-year entry ban. "
            "The Vietnamese government has increased enforcement at airports in recent years. "
            "Apply for your extension at least <strong>3 days before</strong> your current visa expires to ensure approval before the deadline."
        ),
        "table_rows": [
            ("e-Visa extension (30–90 days)", "30, 60, or 90 days", "USD 25", "xuatnhapcanh.gov.vn (online)", "2–5 business days"),
            ("In-person extension (Immigration Dept.)", "30–90 days", "USD 25 + service fee", "Hanoi / HCMC / Da Nang Immigration", "2–5 business days"),
        ],
        "apply_deadline": "Apply at least <strong>3 days before</strong> your current visa expires.",
        "official_link": "https://xuatnhapcanh.gov.vn",
        "official_link_text": "Vietnam Immigration Portal",
    },
    {
        "slug": "malaysia",
        "name": "Malaysia",
        "flag": "my",
        "title": "Malaysia Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Malaysia visa extension 2026: extend your social visit pass free of charge at Immigration. Usually granted 30–60 extra days. Process, documents and overstay fines.",
        "keywords": "malaysia visa extension 2026, extend malaysia social visit pass, malaysia immigration department, malaysia overstay fine",
        "h1": "How to Extend Your Malaysia Visa in 2026",
        "intro": (
            "Malaysia offers a welcoming entry experience for tourists, with many nationalities able to visit visa-free. "
            "If you need extra time to explore Kuala Lumpur, Penang, the Borneo rainforests, or the stunning islands, "
            "you may be eligible to extend your Social Visit Pass through the Malaysian Immigration Department."
        ),
        "can_extend": (
            "Visitors holding a <strong>Social Visit Pass</strong> (the entry pass issued on arrival to visa-exempt nationals) can apply for an extension at any Immigration Department office in Malaysia. "
            "Extensions are granted at the discretion of the immigration officer and are typically <strong>30 to 60 days</strong>, depending on nationality and circumstances. "
            "There is <strong>no fee</strong> for the extension itself under most standard tourist categories. "
            "eVisa holders may also apply for extensions, subject to visa conditions. "
            "The extension must be applied for <em>before</em> the current pass expires — applications after expiry are not accepted."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (6+ months validity)</li>"
            "<li>Completed extension application form (IM.12 or equivalent — available at the Immigration office)</li>"
            "<li>Copy of passport bio page and existing entry stamp</li>"
            "<li>Proof of accommodation (hotel booking or host's identification)</li>"
            "<li>Onward or return flight booking</li>"
            "<li>Sufficient funds for the extended stay (bank statement or cash)</li>"
            "<li>No extension fee charged for standard tourist categories</li>"
            "</ul>"
        ),
        "steps": [
            ("Find the nearest Immigration Department office", "Major offices are in Kuala Lumpur (Putrajaya HQ), Penang, Johor Bahru, Kota Kinabalu (Sabah), and Kuching (Sarawak)."),
            ("Prepare your documents", "Complete the required form and gather your passport, copies of all stamped pages, proof of accommodation, and onward ticket."),
            ("Submit before your pass expires", "Visit the immigration office during opening hours (Mon–Thu and Sat 08:00–17:00; Fri 08:00–17:15; closed Sunday and public holidays)."),
            ("Attend the counter", "Hand your documents to the immigration officer. Be polite and clear about your reason for extending — tourism, family visit, etc."),
            ("Receive new pass", "If approved, your passport will be stamped with the new permitted-stay date on the same day. Extensions are not guaranteed; officers may decline if documentation is incomplete."),
        ],
        "overstay": (
            "Malaysia takes overstay offences very seriously. A fine of <strong>RM 1,000–10,000</strong> can be imposed, and in serious cases imprisonment of up to 5 years. "
            "Deportation may also apply, along with a re-entry ban. Malaysian immigration authorities conduct regular checks in popular tourist areas. "
            "There is a specific 'overstay' stamp placed in the passport at departure which can cause complications for future visa applications worldwide. "
            "Never overstay — apply for an extension well before your current pass expires."
        ),
        "table_rows": [
            ("Social Visit Pass extension", "30–60 days (officer's discretion)", "Free", "Immigration Department office", "Same day"),
            ("eVisa extension (if applicable)", "Subject to visa terms", "Subject to visa type", "Immigration Department office", "1–3 days"),
        ],
        "apply_deadline": "Apply <strong>before your current pass expires</strong>. Applications after expiry are not accepted.",
        "official_link": "https://www.imi.gov.my",
        "official_link_text": "Malaysia Immigration Department",
    },
    {
        "slug": "philippines",
        "name": "Philippines",
        "flag": "ph",
        "title": "Philippines Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Philippines visa extension 2026: extend monthly at Bureau of Immigration for PHP 3,030. Extend multiple times up to 2 years. Documents, steps and overstay fees.",
        "keywords": "philippines visa extension 2026, extend philippines tourist visa, bureau of immigration philippines, philippines overstay fee",
        "h1": "How to Extend Your Philippines Visa in 2026",
        "intro": (
            "The Philippines — with its 7,000+ islands, world-class diving, and tropical beauty — is a destination many visitors want to enjoy for as long as possible. "
            "The good news is that the Philippines has one of the most flexible tourist visa extension systems in Asia, "
            "allowing travellers to extend their stay multiple times through the Bureau of Immigration (BI)."
        ),
        "can_extend": (
            "Most foreign nationals may extend their tourist visa (or visa-free entry) at the <strong>Bureau of Immigration</strong>. "
            "Extensions are issued in <strong>monthly increments</strong> and the process can be repeated multiple times, with a theoretical maximum cumulative stay of up to <strong>2 years</strong> (subject to BI discretion and immigration rules). "
            "Some nationalities are restricted to shorter maximum stays. "
            "After the initial 30-day visa-free entry, the first extension covers an additional 29 days. Subsequent extensions are for 59 days each. "
            "Online extensions are also available via the BI online appointment system for certain types."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (6+ months validity, blank pages)</li>"
            "<li>Accomplished BI extension application form</li>"
            "<li>Recent passport-sized photograph</li>"
            "<li>Copy of all stamped passport pages</li>"
            "<li>Proof of sufficient funds</li>"
            "<li>Onward or return ticket</li>"
            "<li>Extension fee: <strong>PHP 3,030</strong> per monthly extension (includes express fee — walk-in)</li>"
            "</ul>"
        ),
        "steps": [
            ("Go to the Bureau of Immigration", "The main BI office is in Intramuros, Manila. Regional offices are in Cebu, Davao, Iloilo, and other cities. Arrive early — queues can be very long."),
            ("Get a queue number and fill in the form", "Pick up the application form at the counter, fill it in, and attach your photograph and passport copies."),
            ("Submit at the main counter", "Hand your complete application package to the processing officer. They will review your documents and issue a receipt."),
            ("Pay the fee", "Pay PHP 3,030 at the cashier. Keep your official receipt — you will need it to collect your passport."),
            ("Collect your passport", "Return on the date specified on your receipt (usually same day or next day) to collect your passport with the new extension stamp."),
        ],
        "overstay": (
            "Overstaying in the Philippines is subject to a fine of <strong>PHP 500 per month</strong> of overstay (plus associated administrative fees), but enforcement at departure includes a thorough review of your stamp history. "
            "Long overstays (over 6 months) can lead to being placed on an Immigration watchlist and potential deportation proceedings. "
            "Repeated offenders may face a re-entry blacklist. "
            "The Bureau of Immigration is known to impose additional penalties at the discretion of the immigration officer at the airport. "
            "Always extend before your current authorised stay expires."
        ),
        "table_rows": [
            ("First extension (29 days)", "29 days", "PHP 3,030", "Bureau of Immigration office", "Same day"),
            ("Subsequent extensions (59 days each)", "59 days per extension", "PHP 3,030+", "Bureau of Immigration office", "Same day"),
            ("Maximum cumulative stay", "Up to 2 years (BI discretion)", "Per extension fee", "Bureau of Immigration", "Ongoing"),
        ],
        "apply_deadline": "Apply before your current authorised stay expires. There is no fixed minimum lead time but allow at least <strong>1 week</strong>.",
        "official_link": "https://www.immigration.gov.ph",
        "official_link_text": "Bureau of Immigration Philippines",
    },
    {
        "slug": "cambodia",
        "name": "Cambodia",
        "flag": "kh",
        "title": "Cambodia Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Cambodia visa extension 2026: extend an E visa (business/ordinary) for USD 30–45 at immigration. Tourist visa extension is limited. Full guide with penalties.",
        "keywords": "cambodia visa extension 2026, extend cambodia e-visa, cambodia immigration extension, cambodia overstay fine",
        "h1": "How to Extend Your Cambodia Visa in 2026",
        "intro": (
            "Cambodia — home to the ancient temples of Angkor Wat and a rapidly growing tourism scene — has a two-tier visa system: "
            "a Tourist (T) visa for short visits and an Ordinary (E) visa for longer stays or business. "
            "Understanding which visa type you hold is critical to determining whether an extension is possible."
        ),
        "can_extend": (
            "Extension rules in Cambodia differ by visa type. "
            "<strong>Ordinary (E) Visa</strong> — this is the more flexible visa and can be extended multiple times in Cambodia: "
            "an E-visa extension for a further 30 days costs USD 30; an ordinary stay extension for 1 month costs USD 45. "
            "Long-stay ordinary visas can be extended for up to 1 year increments at the Department of Immigration. "
            "<strong>Tourist (T) Visa</strong> — the standard tourist visa is much more limited. It can be extended once for an additional 30 days at a cost of USD 30 at the immigration office. "
            "After that single extension, tourists must exit Cambodia. "
            "The popular eVisa (available at evisa.gov.kh) is a Tourist-category visa and falls under the same one-extension limit."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (6+ months validity)</li>"
            "<li>Completed extension application form (from the Department of Immigration)</li>"
            "<li>Copy of passport bio page and current visa</li>"
            "<li>Recent passport-sized photograph</li>"
            "<li>Extension fee: <strong>USD 30</strong> (tourist extension) or <strong>USD 45</strong> (ordinary/business extension)</li>"
            "<li>Proof of purpose (business letter for E-visa extensions, accommodation proof for tourist)</li>"
            "</ul>"
        ),
        "steps": [
            ("Determine your visa type", "Check whether you hold a Tourist (T) or Ordinary (E) visa — this determines how many extensions are available to you."),
            ("Visit the Department of Immigration", "The main office is in Phnom Penh. In Siem Reap and other tourist cities, local immigration offices also process extensions."),
            ("Submit your application and documents", "Hand in the completed form, passport, photo, and copies of your visa page. Officers will review your application."),
            ("Pay the extension fee", "Pay USD 30 (tourist) or USD 45 (ordinary) in cash. US dollars are widely accepted at Cambodian government offices."),
            ("Receive your extension stamp", "Extensions are usually processed same-day or within 1–2 business days. Your passport will be returned with the new validity stamp."),
        ],
        "overstay": (
            "Cambodia charges a flat fine of <strong>USD 10 per day</strong> of overstay, payable at the border or airport on departure. "
            "This is well-enforced at all official exit points. "
            "Longer overstays (over 30 days) may also attract additional scrutiny and potential deportation. "
            "Overstay is noted in the immigration system and may affect future visa applications to Cambodia. "
            "Always confirm your extension date and depart or re-extend before it expires."
        ),
        "table_rows": [
            ("Tourist (T) visa extension — once only", "30 days (one time only)", "USD 30", "Department of Immigration", "Same day / 1–2 days"),
            ("Ordinary (E) visa extension", "30 days (renewable)", "USD 30–45", "Department of Immigration", "Same day / 1–2 days"),
            ("Long-stay Ordinary visa (1 year)", "1 year", "Varies (~USD 285+)", "Department of Immigration, Phnom Penh", "Several days"),
        ],
        "apply_deadline": "Apply before your current visa expires. Overstay fines begin the day after expiry.",
        "official_link": "https://www.evisa.gov.kh",
        "official_link_text": "Cambodia eVisa Official Portal",
    },
    {
        "slug": "japan",
        "name": "Japan",
        "flag": "jp",
        "title": "Japan Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Japan visa extension 2026: extend at Regional Immigration Bureau for ¥4,000. Strong reason required — medical or family emergency. Tourist extensions are rare.",
        "keywords": "japan visa extension 2026, extend japan tourist visa, japan immigration bureau extension, japan overstay consequences",
        "h1": "How to Extend Your Japan Visa in 2026",
        "intro": (
            "Japan is one of the world's most sought-after travel destinations, famed for its cherry blossoms, cuisine, and ancient culture. "
            "However, Japan takes immigration rules very seriously, and tourist visa extensions are not easily granted. "
            "This guide explains when extensions are possible, what is required, and what the strict overstay consequences are."
        ),
        "can_extend": (
            "Japan is strict about tourist visa extensions. Extensions are processed by the <strong>Regional Immigration Services Bureau</strong> (出入国在留管理局) and are typically only approved for <em>compelling reasons</em> such as a medical emergency, serious illness, or death of a family member in Japan. "
            "Simply wanting to stay longer for tourism is generally <em>not</em> considered sufficient grounds. "
            "If approved, the extension is usually for 15 to 90 days depending on the circumstances. "
            "Visa-exempt short-term visitors (e.g., 90 days for many nationalities) must have a strong justification. "
            "For travellers planning a longer stay in Japan, it is strongly advised to obtain the correct visa (e.g., a Cultural Activities visa or Working Holiday Visa) before arriving."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport with current residence/stay permit</li>"
            "<li>Completed Application for Extension of Period of Stay (様式第30号 — available at the Immigration Bureau)</li>"
            "<li>Passport-sized photograph (4 × 3 cm)</li>"
            "<li>Documentation supporting the reason for extension (medical certificate, death certificate, etc.)</li>"
            "<li>Proof of financial support for the extended period</li>"
            "<li>Application fee: <strong>¥4,000</strong> (revenue stamps —収入印紙)</li>"
            "</ul>"
        ),
        "steps": [
            ("Assess your reason for extension", "Only apply if you have a compelling and documentable reason (medical, family emergency). Gather supporting documentation."),
            ("Find your Regional Immigration Bureau", "Major bureaus are in Tokyo (Shinagawa), Osaka, Nagoya, Sapporo, and Fukuoka. Check immi-moj.go.jp for the nearest office."),
            ("Complete the application form", "Download and complete the 'Application for Extension of Period of Stay' form. Have it stamped and signed."),
            ("Submit all documents", "Visit the Immigration Bureau in person during office hours (Mon–Fri 09:00–16:00). Submit your complete document package."),
            ("Pay ¥4,000 in revenue stamps", "Purchase revenue stamps (収入印紙) at the post office or convenience store. Attach them to the application form and hand in at the counter."),
        ],
        "overstay": (
            "Overstaying in Japan is treated as a criminal offence. Penalties include <strong>imprisonment for up to 3 years and/or a fine of up to ¥3,000,000</strong>. "
            "Deportation is standard for overstayers, followed by a re-entry ban of 5 to 10 years (or permanently for serious cases). "
            "Japan's immigration system is highly data-driven and overstay records are permanently linked to your passport biometrics. "
            "Japanese authorities conduct active enforcement. Never overstay under any circumstances — contact the Immigration Bureau proactively if you face an unexpected situation."
        ),
        "table_rows": [
            ("Tourist / Short-term stay extension (exceptional)", "15–90 days (exceptional only)", "¥4,000", "Regional Immigration Services Bureau", "Days to weeks (variable)"),
        ],
        "apply_deadline": "Apply well before your current permitted stay expires. Processing is not guaranteed and can take several weeks.",
        "official_link": "https://www.moj.go.jp/isa/",
        "official_link_text": "Japan Immigration Services Agency",
    },
    {
        "slug": "singapore",
        "name": "Singapore",
        "flag": "sg",
        "title": "Singapore Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Singapore visa extension 2026: apply via ICA online portal. Extensions rare for tourists — exiting and re-entering is usually easier. Process and overstay rules.",
        "keywords": "singapore visa extension 2026, extend singapore visit pass, ICA singapore extension, singapore overstay consequences",
        "h1": "How to Extend Your Singapore Visa in 2026",
        "intro": (
            "Singapore is a compact, vibrant city-state with world-class food, architecture, and culture — but its small size means most tourists complete their visit within the standard allowed period. "
            "For those who need extra time, understanding the extension process and its limitations is important."
        ),
        "can_extend": (
            "Singapore's <strong>Immigration & Checkpoints Authority (ICA)</strong> does allow short-term visit pass extensions, but approvals for tourists are rare and typically only granted under exceptional circumstances. "
            "Extensions can be applied for online via the ICA e-Service portal. "
            "However, given Singapore's relatively small geographic footprint and the ease of exiting and re-entering from Johor Bahru (Malaysia) or Batam/Bintan (Indonesia) and returning, "
            "most travellers find it simpler and more reliable to exit and re-enter for a fresh visit pass (usually 30 days). "
            "Note that Singapore immigration officers may question travellers who make very frequent short trips in and out."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (6+ months validity)</li>"
            "<li>Existing Short-Term Visit Pass (STVP) still valid</li>"
            "<li>Online application via ICA e-Service (eservices.ica.gov.sg)</li>"
            "<li>Strong documented reason for extension (medical, family, business obligation)</li>"
            "<li>Supporting documents (medical letter, employer letter, etc.)</li>"
            "<li>Application processed online — no extension fee for tourist STVP extensions</li>"
            "</ul>"
        ),
        "steps": [
            ("Visit ICA e-Service portal", "Go to eservices.ica.gov.sg and log in with your SingPass or use the foreign visitor extension option."),
            ("Submit extension request", "Complete the online form, stating your reason for extension and uploading supporting documents."),
            ("Await ICA decision", "ICA will process your application and notify you by email. Processing can take several working days."),
            ("If declined, plan your departure", "If ICA declines the extension, you must depart before your current STVP expires. Consider crossing to Johor Bahru and re-entering for a fresh pass."),
            ("Collect approval (if granted)", "If approved, an updated STVP will be issued. Confirm the new expiry date via the ICA portal."),
        ],
        "overstay": (
            "Singapore has <strong>zero tolerance</strong> for immigration overstays. Overstaying is a criminal offence punishable by up to 6 months' imprisonment and/or a fine. "
            "In addition, those who overstay will be banned from re-entering Singapore. "
            "Given Singapore's small size and highly digital immigration infrastructure, overstays are almost always detected at the airport on departure. "
            "ICA is known for strict enforcement. There are no exceptions — always depart or obtain an approved extension before your STVP expires."
        ),
        "table_rows": [
            ("Short-Term Visit Pass (STVP) extension", "Varies (exceptional cases only)", "No fee for tourist STVP", "ICA e-Service (online)", "Several working days"),
        ],
        "apply_deadline": "Apply via ICA e-Service before your current STVP expires. Extensions are not guaranteed.",
        "official_link": "https://www.ica.gov.sg",
        "official_link_text": "ICA Singapore Official Website",
    },
    {
        "slug": "turkey",
        "name": "Turkey",
        "flag": "tr",
        "title": "Turkey Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Turkey visa extension 2026: e-Visa cannot be extended — exit and re-enter for a new 90-day window. Or apply for a residence permit. Overstay fines explained.",
        "keywords": "turkey visa extension 2026, extend turkey e-visa, turkey residence permit, turkey overstay fine",
        "h1": "How to Extend Your Turkey Visa in 2026",
        "intro": (
            "Turkey straddles Europe and Asia and offers a rich mix of history, coastline, and culture. "
            "Many travellers arrive on Turkey's popular e-Visa, but it is important to understand its limitations: "
            "the e-Visa cannot be extended in-country, which means long-stay visitors need an alternative strategy."
        ),
        "can_extend": (
            "Turkey's <strong>e-Visa</strong> — the most common visa for tourists — <em>cannot be extended</em> once you are in Turkey. "
            "The e-Visa allows a maximum stay of 90 days within any 180-day period. "
            "To 'reset' your 90-day clock you must <strong>exit Turkey</strong> (e.g., cross into Greece, Bulgaria, or Georgia) and re-enter, whereupon a new 90-day window begins — provided you have not exceeded the 90/180-day rule. "
            "An important caveat: Turkey also enforces a <em>Schengen-style 90/180 rule</em> for many nationalities, so you cannot simply keep re-entering every 91 days indefinitely. "
            "For those wishing to remain in Turkey for longer than 90 days continuously, the correct option is a <strong>Short-Term Residence Permit</strong>, "
            "applied for at the Provincial Directorate of Migration Management (İl Göç İdaresi Müdürlüğü)."
        ),
        "requirements": (
            "<ul>"
            "<li>For a Short-Term Residence Permit application:</li>"
            "<li>Valid passport (6+ months validity beyond the permit duration requested)</li>"
            "<li>Completed online pre-application at e-ikamet.goc.gov.tr</li>"
            "<li>4 biometric photos</li>"
            "<li>Proof of address in Turkey (rental contract, title deed, or notarised address declaration)</li>"
            "<li>Health insurance valid in Turkey for the full permit period</li>"
            "<li>Bank statement showing sufficient funds (approx. USD 500/month)</li>"
            "<li>Permit fee: approx. TRY 1,800–3,600 (varies by permit duration)</li>"
            "</ul>"
        ),
        "steps": [
            ("Exit Turkey for an e-Visa reset (short stays)", "If you only need a brief additional period, exit Turkey and re-enter. Ensure you respect the 90/180-day rule for your nationality."),
            ("Apply online for a Short-Term Residence Permit", "For stays over 90 days, apply at e-ikamet.goc.gov.tr before your current visa expires. Complete the online form and book an appointment."),
            ("Attend your appointment at the Migration Management office", "Bring all original documents to your provincial Immigration Directorate appointment. Biometrics will be taken."),
            ("Pay the permit fee", "Fees are paid at the tax office (vergi dairesi) or specific banks designated by the Directorate. Keep all receipts."),
            ("Receive your residence permit card", "If approved, a residence permit card (ikamet tezkeresi) is mailed to your Turkish address within a few weeks."),
        ],
        "overstay": (
            "Overstaying Turkey's e-Visa or visa-free period results in a fine calculated at a daily rate — typically equivalent to <strong>around USD 10–30 per day</strong> depending on the year's tariff, payable in Turkish Lira at the border on departure. "
            "More significant overstays (over 90 days) can lead to deportation and a re-entry ban. "
            "Turkish border police review entry/exit stamps and immigration records carefully at major airports. "
            "If you approach the end of your allowed stay, apply for a residence permit or exit Turkey before the deadline."
        ),
        "table_rows": [
            ("e-Visa — in-country extension", "NOT possible", "N/A — must exit Turkey", "No in-country process", "N/A"),
            ("Re-entry after exit (new 90-day window)", "Up to 90 days", "New e-Visa fee (~USD 65)", "evisa.gov.tr (online)", "Immediate"),
            ("Short-Term Residence Permit", "6 months – 2 years (renewable)", "~TRY 1,800–3,600", "e-ikamet.goc.gov.tr + in-person appt.", "Weeks"),
        ],
        "apply_deadline": "Apply for a residence permit before your visa or current authorised stay expires.",
        "official_link": "https://www.evisa.gov.tr",
        "official_link_text": "Turkey e-Visa Official Portal",
    },
    {
        "slug": "uae",
        "name": "UAE",
        "flag": "ae",
        "title": "UAE Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "UAE visa extension 2026: extend 30 days via GDRFA app for AED 600. Apply 2 weeks before expiry. Dubai and Abu Dhabi process, documents and overstay fines.",
        "keywords": "uae visa extension 2026, extend uae tourist visa, GDRFA dubai visa extension, uae overstay fine 2026",
        "h1": "How to Extend Your UAE Visa in 2026",
        "intro": (
            "The UAE — encompassing Dubai, Abu Dhabi, and the other Emirates — is a global travel hub attracting tens of millions of visitors annually. "
            "Tourist visas can be extended online through official channels, making the process accessible and efficient for most visitors."
        ),
        "can_extend": (
            "UAE tourist visa holders can apply for a <strong>30-day extension</strong> online via the <strong>GDRFA (General Directorate of Residency and Foreigners Affairs)</strong> app or website, "
            "or through the ICP (Federal Authority for Identity, Citizenship, Customs & Port Security) portal. "
            "The extension fee is <strong>AED 600</strong> (approx. USD 163). "
            "Most tourist visas are either 30-day or 60-day on arrival, and a single 30-day extension is usually available for each. "
            "In Dubai specifically, the GDRFA app is the recommended tool; in Abu Dhabi and other Emirates, ICP's TAMM or TAMM Abu Dhabi portals are used. "
            "Multiple extensions may be possible but are subject to approval — check the specific visa terms."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid UAE tourist visa (not yet expired)</li>"
            "<li>Emirates ID (if applicable) or passport copy</li>"
            "<li>UAE mobile number for OTP verification</li>"
            "<li>Online application via GDRFA Smart app (Dubai) or ICP portal</li>"
            "<li>Valid email address for confirmation</li>"
            "<li>Extension fee: <strong>AED 600</strong> (payable by credit/debit card online)</li>"
            "</ul>"
        ),
        "steps": [
            ("Download the GDRFA Smart app or visit the portal", "For Dubai: download GDRFA Smart on iOS/Android. For other Emirates: visit icp.gov.ae."),
            ("Create an account or log in", "Register with your Emirates number and passport details. Verify via OTP."),
            ("Select 'Visa Extension'", "Navigate to the visa services section and select 'Extend Tourist Visa'. Enter your current visa number."),
            ("Upload documents and pay AED 600", "Upload a copy of your passport and pay AED 600 by card. A service fee of AED 28 may also apply."),
            ("Receive confirmation email", "Once processed (usually within 24–48 hours), you will receive a confirmation email with your new visa validity date. Apply at least 2 weeks before your visa expires."),
        ],
        "overstay": (
            "UAE overstay fines are significant. The penalty is <strong>AED 200 per day</strong> for the first day of overstay, then AED 100 per day thereafter, with no maximum cap for standard tourist overstays. "
            "In addition to the daily fine, there is a standard AED 100 overstay fee. "
            "Overstayers may also be placed on a deportation order and banned from re-entering the UAE. "
            "The UAE's immigration system is highly efficient — overstays are always detected at border control on departure. "
            "Always extend your visa at least 14 days before it expires to avoid complications."
        ),
        "table_rows": [
            ("Tourist visa extension (30 days)", "30 days", "AED 600 (~USD 163)", "GDRFA app (Dubai) / ICP portal (other Emirates)", "24–48 hours (online)"),
        ],
        "apply_deadline": "Apply at least <strong>2 weeks (14 days) before</strong> your visa expires.",
        "official_link": "https://gdrfad.gov.ae",
        "official_link_text": "GDRFA Dubai Official Portal",
    },
    {
        "slug": "usa",
        "name": "USA",
        "flag": "us",
        "title": "USA Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "USA visa extension 2026: file I-539 with USCIS for USD 370, at least 45 days before I-94 expiry. Processing 3–6 months, approval not guaranteed. Full guide.",
        "keywords": "usa visa extension 2026, extend usa tourist visa B1 B2, I-539 form USCIS, usa visa overstay consequences",
        "h1": "How to Extend Your USA Visa in 2026",
        "intro": (
            "Extending a tourist (B-1/B-2) visa stay in the United States is possible but involves a bureaucratic process with USCIS, "
            "a long processing time, and significant risk if the application is denied. "
            "This guide explains who can apply, how to do it, and the serious consequences of overstaying without an approved extension."
        ),
        "can_extend": (
            "Visitors in B-1 (business) or B-2 (tourist) status may apply to extend their stay by filing <strong>Form I-539</strong> with U.S. Citizenship and Immigration Services (USCIS). "
            "Extensions are generally granted in 6-month increments and the total stay typically cannot exceed 1 year from date of entry. "
            "USCIS has broad discretion to approve or deny extension requests. Approval is not guaranteed. "
            "Critically, you must file Form I-539 at least <strong>45 days before your I-94 Arrival/Departure Record expires</strong>. "
            "If approved, you are authorised to stay and USCIS will issue an I-797 notice. "
            "If denied, you may be required to leave immediately and the denial can affect future US visa applications. "
            "Visa Waiver Program (ESTA) travellers <em>cannot</em> extend their stay — they must exit after 90 days."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (valid for the duration of the requested extension)</li>"
            "<li>Completed Form I-539 'Application to Extend/Change Nonimmigrant Status'</li>"
            "<li>Copy of your I-94 Arrival/Departure Record (printout from i94.cbp.dhs.gov)</li>"
            "<li>Copy of your current US visa stamp and passport bio page</li>"
            "<li>Evidence of strong ties to your home country (employment, property, family)</li>"
            "<li>Explanation of why extension is needed and travel plans</li>"
            "<li>Bank statements showing sufficient funds</li>"
            "<li>Filing fee: <strong>USD 370</strong></li>"
            "</ul>"
        ),
        "steps": [
            ("Check your I-94 expiry date", "Log in to i94.cbp.dhs.gov to confirm your authorized period of admission. This date — not your visa stamp — is the deadline."),
            ("Complete Form I-539", "Download Form I-539 from uscis.gov. Fill it in carefully. Errors or omissions can cause denial."),
            ("Gather supporting documents", "Compile all required documents including your I-94, passport copies, financial evidence, and a cover letter explaining your request."),
            ("File online or by mail at least 45 days before I-94 expiry", "File via the USCIS online portal (for most I-539 applications) or mail to the appropriate USCIS Service Centre. Pay the USD 370 fee."),
            ("Wait for the USCIS decision", "Processing currently takes 3–6 months. If your I-94 expires during processing and you filed timely, you are in 'maintained status' and may stay lawfully while awaiting a decision."),
        ],
        "overstay": (
            "Overstaying a US visa is extremely serious. Even a single day of unlawful presence can trigger immigration consequences. "
            "<strong>180 days to 1 year of unlawful presence</strong> triggers a 3-year bar from re-entering the US. "
            "<strong>Over 1 year of unlawful presence</strong> triggers a 10-year bar. "
            "Overstay is permanently recorded in US immigration databases and will be flagged on every future visa application. "
            "In some cases it can also affect eligibility for immigration benefits for family members in the US. "
            "ESTA/Visa Waiver Programme travellers who overstay become permanently ineligible for ESTA and must always apply for a visa in future. "
            "Never overstay — if you cannot leave on time, consult an immigration attorney immediately."
        ),
        "table_rows": [
            ("B-1/B-2 Extension via I-539", "Up to 6 months (per approval)", "USD 370 filing fee", "USCIS (online or by mail)", "3–6 months processing"),
            ("Visa Waiver Program (ESTA)", "NOT extendable — 90 days maximum", "N/A", "Must exit after 90 days", "N/A"),
        ],
        "apply_deadline": "File Form I-539 at least <strong>45 days before your I-94 expiry date</strong>.",
        "official_link": "https://www.uscis.gov/i-539",
        "official_link_text": "USCIS Form I-539 Page",
    },
    {
        "slug": "canada",
        "name": "Canada",
        "flag": "ca",
        "title": "Canada Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Canada visa extension 2026: apply online before expiry for CAD 100. Maintained-status rule lets you stay during processing. Documents, steps and overstay rules.",
        "keywords": "canada visa extension 2026, extend canada visitor visa, IRCC canada extension, canada maintained status rule",
        "h1": "How to Extend Your Canada Visa in 2026",
        "intro": (
            "Canada — with its vast wilderness, multicultural cities, and friendly people — attracts millions of visitors each year. "
            "If you need more time to explore, Canada's visitor record extension process is handled entirely online through Immigration, Refugees and Citizenship Canada (IRCC), "
            "and a useful 'maintained status' rule protects you while your application is being processed."
        ),
        "can_extend": (
            "Visitors to Canada on a temporary resident visa (visitor visa) or those admitted as visitors (including some Electronic Travel Authorization / eTA holders) can apply online to extend their visitor record. "
            "The standard initial authorised stay is 6 months from entry. Extensions are typically granted in further 6-month increments. "
            "The key advantage of Canada's system is the <strong>maintained status rule</strong>: if you apply for an extension <em>before</em> your current status expires, "
            "you are legally authorised to remain in Canada while IRCC processes your application — even if that takes longer than expected. "
            "Applications must be submitted via the IRCC online portal (IRCC Secure Account / MyAccount). "
            "The application fee is <strong>CAD 100</strong>."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (valid for the full period of the requested extension)</li>"
            "<li>Current visitor record or entry authorisation</li>"
            "<li>Online application via IRCC secure account (www.canada.ca/en/immigration-refugees-citizenship)</li>"
            "<li>Digital copies of passport bio page and all Canadian entry/exit stamps</li>"
            "<li>Proof of sufficient funds (bank statements for the extension period)</li>"
            "<li>Explanation of purpose of extended visit (travel, family, tourism)</li>"
            "<li>Proof of ties to home country (employment, property, family)</li>"
            "<li>Application fee: <strong>CAD 100</strong></li>"
            "</ul>"
        ),
        "steps": [
            ("Log in to your IRCC Secure Account", "Create or log into your account at www.canada.ca. Go to 'Apply to extend your stay in Canada'."),
            ("Complete the application form", "Fill in the online form accurately, including your current status, purpose of stay, and the duration you are requesting."),
            ("Upload all required documents", "Attach your passport scans, financial statements, and supporting documents. Ensure files are legible and complete."),
            ("Pay CAD 100 and submit", "Pay the application fee of CAD 100 by credit card. Submit the application before your current authorised stay expires."),
            ("Benefit from maintained status", "Once you submit before expiry, you have maintained status — you can legally remain in Canada while IRCC reviews your application. Processing times vary (typically weeks to a few months)."),
        ],
        "overstay": (
            "If you do not apply for an extension before your status expires, you become an <strong>overstayer</strong> in Canada. "
            "This is an immigration violation that can result in a removal order, deportation, and a bar on re-entering Canada. "
            "Overstay is recorded in IRCC's systems and will negatively affect future visa applications. "
            "Unlike the US, Canada does not have an official exit tracking system at land borders (as of 2026), but Canada and the US share traveller data under the Entry/Exit Initiative, "
            "so overstays are generally detected. Always apply for an extension before your current status expires."
        ),
        "table_rows": [
            ("Visitor Record extension", "Usually 6 months per extension", "CAD 100", "IRCC Secure Account (online)", "Weeks to a few months"),
        ],
        "apply_deadline": "Apply <strong>before your current authorised stay expires</strong> to benefit from maintained status.",
        "official_link": "https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/extend-stay.html",
        "official_link_text": "IRCC — Extend Your Stay in Canada",
    },
    {
        "slug": "australia",
        "name": "Australia",
        "flag": "au",
        "title": "Australia Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "Australia visa extension 2026: apply for Visitor visa subclass 600 before expiry. Fee AUD 365, processing 6–12 weeks. Documents, steps and overstay consequences.",
        "keywords": "australia visa extension 2026, extend australia visitor visa subclass 600, DIBP australia extension, australia overstay consequences",
        "h1": "How to Extend Your Australia Visa in 2026",
        "intro": (
            "Australia's vast landscapes, unique wildlife, and vibrant cities make it a destination many visitors want to linger in longer than originally planned. "
            "Extending your stay in Australia requires applying for a new Visitor Visa (subclass 600) — Australia does not technically 'extend' visas; instead, you apply for a new one from within the country."
        ),
        "can_extend": (
            "Australia does not use a traditional extension system. Instead, tourists who want to stay longer must apply for a new <strong>Visitor Visa (subclass 600)</strong> before their current visa expires. "
            "This can be done online via the Australian Government's ImmiAccount portal. "
            "The application fee is <strong>AUD 365</strong> (Tourist stream). "
            "Processing takes approximately <strong>6–12 weeks</strong>, though it can vary. "
            "If you apply before your current visa expires, you are generally granted a 'bridging visa A' (BVA), which allows you to remain in Australia lawfully while your application is being processed. "
            "The subclass 600 Visitor Visa is usually granted for up to 3, 6, or 12 months. "
            "Note: holders of the Electronic Travel Authority (ETA, subclass 601) or eVisitor (subclass 651) cannot extend in-country — they must leave and re-apply from outside Australia."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (ideally 6+ months validity beyond the requested stay)</li>"
            "<li>Current Australian visa (not yet expired)</li>"
            "<li>ImmiAccount registration (immi.homeaffairs.gov.au)</li>"
            "<li>Completed online Visitor Visa subclass 600 application</li>"
            "<li>Evidence of ongoing genuine tourist activities</li>"
            "<li>Bank statements showing sufficient funds</li>"
            "<li>Proof of strong home-country ties (employment, family, assets)</li>"
            "<li>Application fee: <strong>AUD 365</strong></li>"
            "</ul>"
        ),
        "steps": [
            ("Create an ImmiAccount", "Register or log in at immi.homeaffairs.gov.au. This is the Department of Home Affairs' official portal."),
            ("Start a new Visitor Visa (subclass 600) application", "Select 'Apply for a visa', choose Visitor Visa subclass 600 (Tourist stream), and complete the online form."),
            ("Upload supporting documents", "Attach your bank statements, proof of accommodation, return flight (if booked), and evidence of home-country ties."),
            ("Pay AUD 365 and submit", "Pay the application fee online. Submit well before your current visa expires."),
            ("Bridging Visa A is automatically granted", "Once you submit in-time, a Bridging Visa A (BVA) is automatically granted, allowing you to remain in Australia while your subclass 600 is processed."),
        ],
        "overstay": (
            "Overstaying in Australia has severe and long-lasting consequences. "
            "If your visa expires before you lodge a new application, you become unlawful. "
            "Unlawful non-citizens in Australia may be detained and deported. "
            "An <strong>Unlawful Non-Citizen (UNC)</strong> flag is permanently placed on your immigration record, which can result in a <strong>3-year exclusion period</strong> from being granted certain Australian visas. "
            "For ETA or eVisitor holders, departing with an overstay record may result in cancellation of future ETA eligibility. "
            "Always apply for your subclass 600 before your current visa expires to secure a Bridging Visa A."
        ),
        "table_rows": [
            ("Visitor Visa subclass 600 (in-country)", "3, 6, or 12 months (subject to grant)", "AUD 365", "ImmiAccount (online)", "6–12 weeks"),
            ("ETA (subclass 601) / eVisitor (651)", "NOT extendable in-country", "N/A — must leave Australia", "Apply from outside Australia", "Minutes to days"),
        ],
        "apply_deadline": "Apply <strong>before your current visa expires</strong> to receive a Bridging Visa A and lawful status.",
        "official_link": "https://immi.homeaffairs.gov.au",
        "official_link_text": "Australian Department of Home Affairs ImmiAccount",
    },
    {
        "slug": "new-zealand",
        "name": "New Zealand",
        "flag": "nz",
        "title": "New Zealand Visa Extension 2026 — How to Extend, Cost & Requirements",
        "meta_desc": "New Zealand visa extension 2026: apply online for NZD 200 before expiry, 4–6 weeks processing. Documents, steps, bridging visa rules and overstay penalties.",
        "keywords": "new zealand visa extension 2026, extend new zealand visitor visa, immigration new zealand extension, new zealand overstay consequences",
        "h1": "How to Extend Your New Zealand Visa in 2026",
        "intro": (
            "New Zealand's stunning fjords, Maori culture, adventure activities, and Lord of the Rings landscapes inspire many visitors to stay longer than planned. "
            "New Zealand's immigration system allows visitor visa extensions, and the online application process is straightforward — "
            "but you must apply before your current visa expires."
        ),
        "can_extend": (
            "Visitor visa holders in New Zealand can apply to extend their stay online via <strong>Immigration New Zealand (INZ)</strong>. "
            "The extension is applied for as a new visitor visa from within New Zealand. "
            "The fee is <strong>NZD 200</strong> and the processing time is typically <strong>4–6 weeks</strong>. "
            "Visitors who apply before their current visa expires are usually granted a <em>visitor visa with interim visa</em> conditions allowing them to remain lawfully while the application is processed. "
            "The maximum total tourist stay in New Zealand in any 18-month period is generally 9 months for most nationalities. "
            "Holders of the NZeTA (New Zealand Electronic Travel Authority) cannot extend in-country — they must leave and return."
        ),
        "requirements": (
            "<ul>"
            "<li>Valid passport (6+ months validity recommended)</li>"
            "<li>Current visitor visa (not yet expired)</li>"
            "<li>Online application via myvisa.immigration.govt.nz</li>"
            "<li>Evidence of genuine visitor activities (itinerary, tour bookings)</li>"
            "<li>Bank statements showing sufficient funds for the extended stay</li>"
            "<li>Proof of strong home-country ties (employment letter, property, family)</li>"
            "<li>Medical and character requirements (may need health insurance evidence)</li>"
            "<li>Application fee: <strong>NZD 200</strong></li>"
            "</ul>"
        ),
        "steps": [
            ("Log in to New Zealand's online visa portal", "Go to myvisa.immigration.govt.nz and log in with your RealMe account or create one."),
            ("Start a Visitor Visa (extension) application", "Select 'Extend your stay in New Zealand' and choose the Visitor Visa category."),
            ("Complete the form and upload documents", "Fill in all sections, including travel plans and funding. Upload bank statements, itinerary, and home-country tie documents."),
            ("Pay NZD 200 and submit", "Pay the application fee online by credit/debit card. Submit before your current visa expires."),
            ("Interim visa is granted automatically", "Once submitted, an interim visa is issued, allowing you to remain lawfully in New Zealand while INZ processes your application (4–6 weeks)."),
        ],
        "overstay": (
            "New Zealand takes overstays seriously. Overstaying makes you an 'unlawful immigrant' under NZ law. "
            "Consequences include <strong>deportation at your own expense</strong>, a liability order for those costs, and a re-entry ban (typically 5 years, up to indefinitely for serious cases). "
            "New Zealand's immigration database tracks entry and exit, and overstays are flagged at departure from any NZ airport. "
            "If you are in New Zealand and discover your visa is about to expire, apply for an extension immediately via myvisa.immigration.govt.nz or contact Immigration New Zealand directly at 0508 558 855 (within NZ)."
        ),
        "table_rows": [
            ("Visitor Visa extension (in-country)", "Up to 9 months total in 18 months", "NZD 200", "myvisa.immigration.govt.nz (online)", "4–6 weeks"),
            ("NZeTA", "NOT extendable in-country", "N/A — must depart", "Apply fresh NZeTA from outside NZ", "Minutes"),
        ],
        "apply_deadline": "Apply <strong>before your current visitor visa expires</strong> to receive an interim visa for lawful continued stay.",
        "official_link": "https://www.immigration.govt.nz",
        "official_link_text": "Immigration New Zealand Official Website",
    },
]

# ---------------------------------------------------------------------------
# FAQ / HowTo generators
# ---------------------------------------------------------------------------

def faq_json(c):
    slug = c["slug"]
    name = c["name"]
    first_row = c["table_rows"][0]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"Can I extend my {name} visa while inside the country?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": c["can_extend"].replace("<strong>", "").replace("</strong>", "").replace("<em>", "").replace("</em>", "").replace("<a href='https://xuatnhapcanh.gov.vn' target='_blank' rel='noopener'>xuatnhapcanh.gov.vn</a>", "xuatnhapcanh.gov.vn")[:400]
                }
            },
            {
                "@type": "Question",
                "name": f"How long does a {name} visa extension take?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Processing time for a {name} visa extension is: {first_row[4]}. Always apply well before your current visa or permitted stay expires to avoid any lapse in status."
                }
            },
            {
                "@type": "Question",
                "name": f"What is the fee for a {name} visa extension?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"The standard extension fee for a {name} tourist visa is {first_row[2]}. Additional service fees may apply in some cases. Fees are subject to change — always confirm current rates with the official immigration authority."
                }
            },
            {
                "@type": "Question",
                "name": f"What happens if I overstay my {name} visa?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": c["overstay"].replace("<strong>", "").replace("</strong>", "").replace("<em>", "").replace("</em>", "")[:400]
                }
            },
        ]
    }


def howto_json(c):
    name = c["name"]
    steps_ld = []
    for i, (step_name, step_text) in enumerate(c["steps"], 1):
        steps_ld.append({
            "@type": "HowToStep",
            "name": f"Step {i}: {step_name}",
            "text": step_text
        })
    return {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": f"How to Apply for a {name} Visa Extension",
        "description": f"Step-by-step guide to extending your {name} tourist visa in 2026.",
        "step": steps_ld
    }


# ---------------------------------------------------------------------------
# HTML builder
# ---------------------------------------------------------------------------

def build_html(c):
    import json as _json

    slug = c["slug"]
    name = c["name"]
    flag = c["flag"]
    title = c["title"]
    meta_desc = c["meta_desc"]
    keywords = c["keywords"]
    h1 = c["h1"]
    canonical = f"https://www.evisa-card.com/en/{slug}-visa-extension.html"

    # Table rows
    table_body = ""
    for row in c["table_rows"]:
        ext_type, duration, fee, where, processing = row
        table_body += f"""
        <tr>
          <td>{ext_type}</td>
          <td>{duration}</td>
          <td>{fee}</td>
          <td>{where}</td>
          <td>{processing}</td>
        </tr>"""

    # Steps list for HTML
    steps_html = ""
    for i, (step_name, step_text) in enumerate(c["steps"], 1):
        steps_html += f"""
        <li class="mb-2"><strong>{step_name}</strong><br>{step_text}</li>"""

    faq_ld = _json.dumps(faq_json(c), indent=2, ensure_ascii=False)
    howto_ld = _json.dumps(howto_json(c), indent=2, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
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
    <!-- SEO -->
    <meta content="{meta_desc}" name="description"/>
    <meta content="{keywords}" name="keywords"/>
    <meta content="index, follow" name="robots" />
    <link href="{canonical}" rel="canonical" />
    <!-- Open Graph -->
    <meta content="{title}" property="og:title" />
    <meta content="{meta_desc}" property="og:description" />
    <meta content="website" property="og:type" />
    <meta content="{canonical}" property="og:url" />
    <meta content="https://www.evisa-card.com/images/og-image.jpg" property="og:image" />
    <!-- Hreflang -->
    <link rel="alternate" hreflang="en" href="{canonical}"/>
    <link rel="alternate" hreflang="x-default" href="{canonical}"/>
    <!-- Fonts & CSS -->
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&amp;display=swap" rel="stylesheet" />
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet" />
    <link href="../css/owl.carousel.min.css" rel="stylesheet" />
    <link href="../css/owl.theme.default.min.css" rel="stylesheet" />
    <link href="../css/magnific-popup.css" rel="stylesheet" />
    <link href="../css/bootstrap-datepicker.css" rel="stylesheet" />
    <link href="../css/jquery.timepicker.css" rel="stylesheet" />
    <link href="../css/flaticon.css" rel="stylesheet" />
    <link href="../css/style.css" rel="stylesheet" />
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
</head>
<body>
    <!-- ======== HEADER ========= -->
    <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
        <div class="container">
            <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
            <button aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation"
                    class="navbar-toggler" data-target="#ftco-nav" data-toggle="collapse" type="button">
                <span class="oi oi-menu"></span> Menu
            </button>
            <div class="collapse navbar-collapse" id="ftco-nav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                    <li class="nav-item active"><a class="nav-link" href="visa-{slug}.html">{name} Visa</a></li>
                    <li class="nav-item dropdown ml-2">
                        <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button"
                           data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"
                           style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                           <span class="fi fi-gb"></span> English
                        </a>
                        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                            <a class="dropdown-item active" href="/en/{slug}-visa-extension.html"><span class="fi fi-gb"></span> English</a>
                            <a class="dropdown-item" href="/fr/{slug}-visa-extension.html"><span class="fi fi-fr"></span> Fran&#231;ais</a>
                            <a class="dropdown-item" href="/es/{slug}-visa-extension.html"><span class="fi fi-es"></span> Espa&#241;ol</a>
                            <a class="dropdown-item" href="/pt/{slug}-visa-extension.html"><span class="fi fi-br"></span> Portugu&#234;s</a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <section class="ftco-section">
        <div class="container">
            <article class="country-page">

                <h1><span class="fi fi-{flag} mr-2"></span>{h1}</h1>
                <p class="lead">{c["intro"]}</p>

                <!-- Extension Overview Table -->
                <h2 id="overview">Visa Extension at a Glance</h2>
                <p>{c["apply_deadline"]}</p>
                <div class="table-responsive">
                    <table class="table table-bordered table-sm mt-3 mb-4">
                        <thead class="thead-dark">
                            <tr>
                                <th>Extension Type</th>
                                <th>Duration</th>
                                <th>Fee</th>
                                <th>Where to Apply</th>
                                <th>Processing Time</th>
                            </tr>
                        </thead>
                        <tbody>{table_body}
                        </tbody>
                    </table>
                </div>

                <!-- Section 1 -->
                <h2 id="can-extend">Can You Extend Your {name} Visa?</h2>
                <p>{c["can_extend"]}</p>

                <!-- Section 2 -->
                <h2 id="requirements">Extension Requirements and Documents</h2>
                {c["requirements"]}

                <!-- Section 3 -->
                <h2 id="steps">Step-by-Step Extension Process</h2>
                <ol>{steps_html}
                </ol>

                <!-- Section 4 -->
                <h2 id="overstay">Overstay Penalties — Important!</h2>
                <div class="alert alert-danger">
                    <span class="fa fa-exclamation-triangle mr-1"></span>
                    <strong>Warning:</strong> Overstaying your visa can have serious and long-lasting consequences.
                </div>
                <p>{c["overstay"]}</p>

                <!-- E-E-A-T block -->
                <div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
                    <div class="d-flex align-items-start">
                        <div class="mr-3"><span class="fa fa-shield fa-2x text-info"></span></div>
                        <div>
                            <strong>Editorial Team — eVisa-Card.com</strong>
                            <p class="mb-1 small text-muted">This guide is maintained by our visa research team. Last updated: <strong>March 2026</strong>.</p>
                            <p class="mb-0 small"><strong>Important:</strong> Visa extension rules change frequently. Always verify current requirements at the
                            <a href="{c['official_link']}" target="_blank" rel="noopener">{c['official_link_text']}</a>
                            before making travel plans. This page is for informational purposes only.</p>
                        </div>
                    </div>
                </div>

                <!-- Internal links -->
                <div class="related-guides mt-5 pt-4 border-top">
                    <h3 class="h5 mb-3">Related {name} Visa Guides</h3>
                    <div>
                        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{slug}.html">{name} Visa Overview</a>
                        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{slug}-visa-requirements.html">{name} Visa Requirements</a>
                        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{slug}-visa-fees.html">{name} Visa Fees</a>
                        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="how-to-apply-evisa.html">How to Apply for an eVisa</a>
                        <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
                    </div>
                </div>

            </article>
        </div>
    </section>

    <!-- FAQPage JSON-LD -->
    <script type="application/ld+json">
{faq_ld}
    </script>

    <!-- HowTo JSON-LD -->
    <script type="application/ld+json">
{howto_ld}
    </script>

    <footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
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

    <!-- Loader + JS -->
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
</html>
"""
    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []
    for c in COUNTRIES:
        filename = f"{c['slug']}-visa-extension.html"
        filepath = os.path.join(OUT_DIR, filename)
        html = build_html(c)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        created.append(filename)
        print(f"  Created: {filename}")
    print(f"\nDone — {len(created)} files generated in {OUT_DIR}")


if __name__ == "__main__":
    main()
