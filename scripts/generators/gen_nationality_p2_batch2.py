#!/usr/bin/env python3
"""
gen_nationality_p2_batch2.py
Generates 40 HTML nationality pages for USA and Canada
(20 nationalities × 2 destination countries)
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ── nationality metadata ──────────────────────────────────────────────────────
NATIONALITIES = [
    # (slug,         display,          flag-code)
    ("french",       "French",         "fr"),
    ("german",       "German",         "de"),
    ("japanese",     "Japanese",       "jp"),
    ("australian",   "Australian",     "au"),
    ("indian",       "Indian",         "in"),
    ("chinese",      "Chinese",        "cn"),
    ("russian",      "Russian",        "ru"),
    ("brazilian",    "Brazilian",      "br"),
    ("mexican",      "Mexican",        "mx"),
    ("south-african","South African",  "za"),
    ("nigerian",     "Nigerian",       "ng"),
    ("korean",       "Korean",         "kr"),
    ("singaporean",  "Singaporean",    "sg"),
    ("indonesian",   "Indonesian",     "id"),
    ("philippine",   "Philippine",     "ph"),
    ("turkish",      "Turkish",        "tr"),
    ("argentinian",  "Argentinian",    "ar"),
    ("canadian",     "Canadian",       "ca"),
    ("uk",           "UK",             "gb"),
    ("us",           "US",             "us"),
]

# ── USA visa data ─────────────────────────────────────────────────────────────
USA_VISA = {
    # ESTA-eligible
    "uk":           {"type":"ESTA",     "fee":"USD 21", "stay":"90 days", "processing":"Instant (online)", "apply_at":"esta.cbp.dhs.gov"},
    "french":       {"type":"ESTA",     "fee":"USD 21", "stay":"90 days", "processing":"Instant (online)", "apply_at":"esta.cbp.dhs.gov"},
    "german":       {"type":"ESTA",     "fee":"USD 21", "stay":"90 days", "processing":"Instant (online)", "apply_at":"esta.cbp.dhs.gov"},
    "japanese":     {"type":"ESTA",     "fee":"USD 21", "stay":"90 days", "processing":"Instant (online)", "apply_at":"esta.cbp.dhs.gov"},
    "australian":   {"type":"ESTA",     "fee":"USD 21", "stay":"90 days", "processing":"Instant (online)", "apply_at":"esta.cbp.dhs.gov"},
    "korean":       {"type":"ESTA",     "fee":"USD 21", "stay":"90 days", "processing":"Instant (online)", "apply_at":"esta.cbp.dhs.gov"},
    "singaporean":  {"type":"ESTA",     "fee":"USD 21", "stay":"90 days", "processing":"Instant (online)", "apply_at":"esta.cbp.dhs.gov"},
    # Visa-free special cases
    "canadian":     {"type":"Visa-Free (USMCA)", "fee":"None", "stay":"180 days", "processing":"N/A", "apply_at":"N/A — passport only"},
    "brazilian":    {"type":"Visa-Free (since Oct 2024)", "fee":"None", "stay":"90 days", "processing":"N/A", "apply_at":"N/A — passport only"},
    "mexican":      {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"6–18 months (interview)", "apply_at":"ustraveldocs.com"},
    # B1/B2 required
    "indian":       {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "chinese":      {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 10 years (multiple-entry)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "russian":      {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "south-african":{"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "nigerian":     {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "indonesian":   {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "philippine":   {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "turkish":      {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "argentinian":  {"type":"B1/B2 Visa", "fee":"USD 185", "stay":"Up to 6 months (per officer)", "processing":"3–8 weeks", "apply_at":"ustraveldocs.com"},
    "us":           {"type":"Visa-Free (US Citizens)",  "fee":"None",   "stay":"N/A (US residents)", "processing":"N/A", "apply_at":"N/A — US citizens reside in the USA"},
}

# ── Canada visa data ──────────────────────────────────────────────────────────
CANADA_VISA = {
    # Visa-free
    "us":           {"type":"Visa-Free", "fee":"None", "stay":"6 months", "processing":"N/A", "apply_at":"N/A — passport only"},
    # eTA
    "uk":           {"type":"eTA",       "fee":"CAD 7", "stay":"6 months", "processing":"Instant (online)", "apply_at":"canada.ca/eTA"},
    "french":       {"type":"eTA",       "fee":"CAD 7", "stay":"6 months", "processing":"Instant (online)", "apply_at":"canada.ca/eTA"},
    "german":       {"type":"eTA",       "fee":"CAD 7", "stay":"6 months", "processing":"Instant (online)", "apply_at":"canada.ca/eTA"},
    "japanese":     {"type":"eTA",       "fee":"CAD 7", "stay":"6 months", "processing":"Instant (online)", "apply_at":"canada.ca/eTA"},
    "australian":   {"type":"eTA",       "fee":"CAD 7", "stay":"6 months", "processing":"Instant (online)", "apply_at":"canada.ca/eTA"},
    "korean":       {"type":"eTA",       "fee":"CAD 7", "stay":"6 months", "processing":"Instant (online)", "apply_at":"canada.ca/eTA"},
    "singaporean":  {"type":"eTA",       "fee":"CAD 7", "stay":"6 months", "processing":"Instant (online)", "apply_at":"canada.ca/eTA"},
    "brazilian":    {"type":"eTA",       "fee":"CAD 7", "stay":"6 months", "processing":"Instant (online)", "apply_at":"canada.ca/eTA"},
    "mexican":      {"type":"Visitor Visa", "fee":"CAD 100", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    # Visitor Visa required
    "indian":       {"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "chinese":      {"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "russian":      {"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "south-african":{"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "nigerian":     {"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "indonesian":   {"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "philippine":   {"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "turkish":      {"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "argentinian":  {"type":"Visitor Visa", "fee":"CAD 100 + biometrics CAD 85", "stay":"6 months", "processing":"4–12 weeks", "apply_at":"ircc.canada.ca"},
    "canadian":     {"type":"Visa-Free (Canadian Citizens)",  "fee":"None",   "stay":"N/A (Canadian residents)", "processing":"N/A", "apply_at":"N/A — Canadian citizens reside in Canada"},
}

# ── helpers ───────────────────────────────────────────────────────────────────

def nationality_display(slug, display):
    """Return display name for use in headings/sentences."""
    return display

def visa_status_badge(vtype):
    if "Visa-Free" in vtype or "USMCA" in vtype:
        return f'<span style="color:green;font-weight:600;">Visa-Free</span>'
    if vtype in ("ESTA", "eTA"):
        return f'<span style="color:#0069d9;font-weight:600;">{vtype} Required</span>'
    if "B1/B2" in vtype or "Visitor Visa" in vtype:
        return f'<span style="color:#c0392b;font-weight:600;">Visa Required ({vtype})</span>'
    return vtype

# ── USA page content builder ──────────────────────────────────────────────────

def usa_body(nat_slug, nat_display, nat_flag, vdata):
    vtype   = vdata["type"]
    fee     = vdata["fee"]
    stay    = vdata["stay"]
    proc    = vdata["processing"]
    apply   = vdata["apply_at"]
    badge   = visa_status_badge(vtype)

    # ── related links (defined early so early-return branches can use it) ──
    related = [
        ("visa-usa.html",            "USA Visa Overview"),
        ("usa-visa-for-french-citizens.html",   "USA for French Citizens"),
        ("usa-visa-for-german-citizens.html",   "USA for German Citizens"),
        ("usa-visa-for-indian-citizens.html",   "USA for Indian Citizens"),
    ]
    related_links = "\n".join(
        f'    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{href}">{label}</a>'
        for href, label in related if href != f"usa-visa-for-{nat_slug}-citizens.html"
    )

    # ── FAQ (3 Q&A) ──
    if nat_slug == "us":
        # US citizens don't need a visa for the USA — redirect/informational page
        faq = [
            {"q": "Do US citizens need a visa to enter the USA?",
             "a": "No. US citizens are nationals of the United States and require no visa to enter or live in their own country. A valid US passport is only required for international re-entry."},
            {"q": "What travel documents do US citizens need when returning to the USA?",
             "a": "US citizens must present a valid US passport (or US passport card for land/sea border crossings) when returning from abroad. US citizens cannot be denied entry to their own country."},
            {"q": "Can US citizens be required to show proof of onward travel at the US border?",
             "a": "No. US citizens have an unconditional right to enter the United States. CBP officers may not deny entry to a US citizen regardless of onward travel plans or length of stay."},
        ]
        h2_sections = """
<h2>US Citizens and US Entry — No Visa Required</h2>
<p>As a US citizen, you have an <strong>absolute right to enter the United States</strong>. No visa, ESTA, or other travel authorisation is required. You are only required to present a valid US passport (or other accepted document) when returning from a trip abroad.</p>

<h2>Returning to the USA from Abroad</h2>
<p>When returning to the USA after international travel, US citizens must present their US passport at the port of entry. US passport cards are accepted at land and sea crossings but are <em>not</em> valid for international air travel. If your passport has expired abroad, the US Embassy can issue an emergency travel document.</p>

<h2>Living and Working in the USA as a US Citizen</h2>
<p>US citizens have unrestricted rights to live, work, and study anywhere in the United States. If you are interested in becoming a US citizen through naturalisation, contact <a href="https://www.uscis.gov" target="_blank" rel="noopener">USCIS (uscis.gov)</a>.</p>

<h2>Travelling to Other Countries from the USA</h2>
<p>The US passport is one of the world's most powerful travel documents, granting <strong>visa-free or visa-on-arrival access to over 180 countries</strong>. See our <a href="visa-free-countries-us-passport.html">US passport visa-free countries guide</a> for a complete list.</p>
"""
        return faq, h2_sections, badge, related_links
    elif "ESTA" in vtype:
        faq = [
            {"q": f"Do {nat_display} citizens need a visa for the USA?",
             "a": f"No. {nat_display} passport holders are part of the US Visa Waiver Program (VWP). They must obtain an ESTA authorisation before travel — it costs USD 21 and is valid for 2 years or until passport expiry."},
            {"q": "How do I apply for ESTA as a {nat_display} citizen?".replace("{nat_display}", nat_display),
             "a": "Apply online at esta.cbp.dhs.gov at least 72 hours before departure. Fill in the form, pay USD 21 by card, and receive approval usually within minutes. Carry the authorisation number when you travel."},
            {"q": f"How long can {nat_display} citizens stay in the USA on ESTA?",
             "a": "Up to 90 days per visit. ESTA does not allow extension or change of status. For longer stays, a B1/B2 visa is required."},
        ]
        h2_sections = _esta_sections(nat_display)
    elif "USMCA" in vtype or ("Visa-Free" in vtype and "canadian" == nat_slug):
        faq = [
            {"q": "Do Canadian citizens need a visa to enter the USA?",
             "a": "No. Canadian passport holders are exempt from US visa requirements under USMCA (formerly NAFTA). A valid Canadian passport is all that is needed."},
            {"q": "How long can Canadians stay in the USA?",
             "a": "Typically up to 6 months per visit, at the discretion of the Customs and Border Protection (CBP) officer at the port of entry."},
            {"q": "Do Canadians need ESTA for the USA?",
             "a": "No. ESTA is only for Visa Waiver Program countries. Canadians are automatically visa-exempt and do not need ESTA."},
        ]
        h2_sections = _canadian_usa_sections()
    elif "Oct 2024" in vtype or ("Visa-Free" in vtype and "brazilian" == nat_slug):
        faq = [
            {"q": "Do Brazilian citizens need a visa for the USA?",
             "a": "No. Brazil joined the US Visa Waiver Program (VWP) in October 2024. Brazilian passport holders can enter the USA visa-free for up to 90 days for tourism or business."},
            {"q": "Do Brazilians need ESTA for the USA?",
             "a": "Brazil's VWP admission came with a transitional period. An eTA-style system is expected; travellers should check esta.cbp.dhs.gov for the latest requirements before departure."},
            {"q": "How long can Brazilian citizens stay in the USA without a visa?",
             "a": "Up to 90 days per visit under the Visa Waiver Program."},
        ]
        h2_sections = _brazil_usa_sections()
    elif nat_slug == "mexican":
        faq = [
            {"q": "Do Mexican citizens need a visa for the USA?",
             "a": "Yes. Mexican passport holders must obtain a B1/B2 non-immigrant visa at the US Embassy or Consulate. The visa application fee is USD 185. Processing may take 6–18 months depending on the consulate and season."},
            {"q": "How long does it take to get a US visa for Mexican citizens?",
             "a": "Wait times at US consulates in Mexico can range from 6 to 18 months for a B1/B2 interview slot. Applicants should apply well in advance. Some emergency appointments may be available."},
            {"q": "Can Mexican dual passport holders (Mexico + EU) enter the USA visa-free?",
             "a": "Yes. Mexican nationals who also hold a passport from an EU Visa Waiver Program country (e.g., Germany, France, Spain) may use that passport with ESTA to enter the USA without a B1/B2 visa."},
        ]
        h2_sections = _b1b2_sections(nat_display, "Mexico", wait="6–18 months")
    else:
        faq = [
            {"q": f"Do {nat_display} citizens need a visa for the USA?",
             "a": f"Yes. {nat_display} passport holders must apply for a B1/B2 non-immigrant visitor visa. The application fee is USD 185 and requires completing form DS-160, paying the fee, and attending an in-person interview at the US Embassy or Consulate."},
            {"q": f"How long does it take to get a US B1/B2 visa for {nat_display} citizens?",
             "a": f"Processing typically takes 3–8 weeks after the visa interview, though interview wait times vary by consulate. Applicants should apply at least 3–6 months before planned travel."},
            {"q": f"How long can {nat_display} citizens stay in the USA on a B1/B2 visa?",
             "a": "A B1/B2 visa is usually issued for multiple entries and valid for up to 10 years, but each stay is limited by the duration granted by the CBP officer at entry — typically up to 6 months."},
        ]
        h2_sections = _b1b2_sections(nat_display, nat_display.replace(" ",""), wait="3–8 weeks")

    return faq, h2_sections, badge, related_links


def _esta_sections(nd):
    return f"""
<h2>ESTA — Visa Waiver for {nd} Citizens</h2>
<p>{nd} passport holders are enrolled in the US <strong>Visa Waiver Program (VWP)</strong>, allowing stays of up to <strong>90 days</strong> for tourism, transit, or business. An <strong>Electronic System for Travel Authorization (ESTA)</strong> is required before boarding a US-bound flight or ship.</p>
<p>ESTA is not a visa but an automated security screening. It costs <strong>USD 21</strong>, is approved within minutes in most cases, and remains valid for <strong>2 years</strong> (or until passport expiry).</p>

<h2>How to Apply for ESTA in 2026</h2>
<ol>
<li>Visit the official website <a href="https://esta.cbp.dhs.gov" target="_blank" rel="noopener">esta.cbp.dhs.gov</a>.</li>
<li>Complete the online form (passport details, travel information, background questions).</li>
<li>Pay USD 21 by credit or debit card.</li>
<li>Receive authorisation — usually within minutes, sometimes up to 72 hours.</li>
<li>No need to print; your ESTA is linked to your passport electronically.</li>
</ol>

<h2>Documents Required at US Customs</h2>
<ul>
<li>Valid {nd} passport (min. 6 months validity recommended)</li>
<li>Approved ESTA authorisation</li>
<li>Return or onward ticket</li>
<li>Proof of accommodation in the USA</li>
<li>Sufficient funds for your stay</li>
</ul>

<h2>Extending Your Stay or Changing Status</h2>
<p>ESTA does <strong>not</strong> allow extensions or changes of immigration status inside the USA. If you need to stay longer than 90 days or wish to work or study, you must apply for the appropriate US visa (e.g., B1/B2, F-1) from your home country <em>before</em> travelling.</p>
"""


def _canadian_usa_sections():
    return """
<h2>Do Canadians Need a Visa or ESTA for the USA?</h2>
<p>No. Canadian citizens are <strong>visa-exempt</strong> from US entry requirements under the <strong>USMCA</strong> (formerly NAFTA) agreement. A valid Canadian passport is sufficient for entry at all land, air, and sea ports of entry. No ESTA is needed.</p>

<h2>How Long Can Canadians Stay in the USA?</h2>
<p>The CBP officer at the port of entry determines the length of each stay. For tourism and short business visits, up to <strong>6 months</strong> is typical. Always have proof of ties to Canada (employment, property, family) if asked.</p>

<h2>Permanent Residents and Nexus</h2>
<p>Canadian <strong>permanent residents</strong> who are not Canadian citizens are subject to different rules and may require a US visa. The <strong>NEXUS</strong> trusted-traveller programme expedites land and air crossings for pre-approved Canadian citizens between both countries.</p>

<h2>Working or Studying in the USA as a Canadian</h2>
<p>Tourism and short business visits are visa-free, but <strong>working or studying in the USA requires appropriate non-immigrant visas</strong> (TN visa for USMCA professionals, H-1B for skilled workers, F-1 for students, etc.).</p>
"""


def _brazil_usa_sections():
    return """
<h2>Visa-Free USA Entry for Brazilian Citizens</h2>
<p>Brazil was admitted to the US <strong>Visa Waiver Program (VWP)</strong> in October 2024. Brazilian passport holders may now visit the USA for tourism or business for up to <strong>90 days</strong> without a B1/B2 visa.</p>

<h2>ESTA / Pre-Travel Authorisation</h2>
<p>As part of VWP membership, Brazilian travellers are expected to register with the <strong>Electronic System for Travel Authorization (ESTA)</strong> before travel. Check <a href="https://esta.cbp.dhs.gov" target="_blank" rel="noopener">esta.cbp.dhs.gov</a> for current requirements and fees. The standard fee is USD 21.</p>

<h2>Documents Needed at the US Border</h2>
<ul>
<li>Valid Brazilian passport</li>
<li>ESTA / pre-travel authorisation (check current requirements)</li>
<li>Return or onward ticket</li>
<li>Proof of accommodation</li>
<li>Sufficient funds for the duration of stay</li>
</ul>

<h2>Working or Studying in the USA</h2>
<p>Visa Waiver Program entry does <strong>not</strong> allow work, study, or employment. Brazilians planning to work or study in the USA must apply for the correct visa (H-1B, L-1, F-1, etc.) at the US Embassy before travelling.</p>
"""


def _b1b2_sections(nd, country_id, wait):
    return f"""
<h2>US B1/B2 Visa for {nd} Citizens</h2>
<p>{nd} passport holders require a <strong>B1/B2 non-immigrant visitor visa</strong> to enter the United States for tourism, medical treatment, or business. The application fee is <strong>USD 185</strong> (MRV fee), paid online before scheduling an interview at the US Embassy or Consulate.</p>

<h2>How to Apply for a US B1/B2 Visa in 2026</h2>
<ol>
<li>Complete <strong>DS-160</strong> (Online Nonimmigrant Visa Application) at ceac.state.gov.</li>
<li>Pay the USD 185 MRV fee via <a href="https://www.ustraveldocs.com" target="_blank" rel="noopener">ustraveldocs.com</a>.</li>
<li>Schedule an interview at the nearest US Embassy or Consulate.</li>
<li>Attend the interview with all required documents.</li>
<li>If approved, your passport will be returned with the visa within 3–10 business days.</li>
</ol>
<p>Current interview wait times for {nd} citizens: approximately <strong>{wait}</strong> — apply well in advance.</p>

<h2>Required Documents for the Visa Interview</h2>
<ul>
<li>Valid {nd} passport (min. 6 months validity beyond intended stay)</li>
<li>DS-160 confirmation page</li>
<li>USD 185 MRV fee receipt</li>
<li>One passport-sized photo (5 cm × 5 cm, white background)</li>
<li>Proof of ties to home country (employment letter, property deeds, family evidence)</li>
<li>Bank statements / financial evidence</li>
<li>Travel itinerary and accommodation bookings</li>
</ul>

<h2>Tips to Strengthen Your US Visa Application</h2>
<p>The consular officer will assess your <em>non-immigrant intent</em> — your intention to return home after your US visit. Strong evidence of ties to your home country (stable employment, family, property ownership) significantly improves approval chances. Provide honest, consistent answers and bring comprehensive financial documentation.</p>
"""


# ── Canada page content builder ───────────────────────────────────────────────

def canada_body(nat_slug, nat_display, nat_flag, vdata):
    vtype   = vdata["type"]
    fee     = vdata["fee"]
    stay    = vdata["stay"]
    proc    = vdata["processing"]
    apply   = vdata["apply_at"]
    badge   = visa_status_badge(vtype)

    # ── related links (defined early so early-return branches can use it) ──
    related = [
        ("visa-canada.html",                      "Canada Visa Overview"),
        ("canada-visa-for-uk-citizens.html",       "Canada for UK Citizens"),
        ("canada-visa-for-indian-citizens.html",   "Canada for Indian Citizens"),
        ("canada-visa-for-french-citizens.html",   "Canada for French Citizens"),
    ]
    related_links = "\n".join(
        f'    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{href}">{label}</a>'
        for href, label in related if href != f"canada-visa-for-{nat_slug}-citizens.html"
    )

    if nat_slug == "canadian":
        faq = [
            {"q": "Do Canadian citizens need a visa for Canada?",
             "a": "No. Canadian citizens are nationals of Canada and have an absolute right to enter and live in their own country. No visa, eTA, or other travel authorisation is required."},
            {"q": "What travel document do Canadians need when returning to Canada?",
             "a": "Canadian citizens must present a valid Canadian passport when returning from abroad by air. A Canadian passport or enhanced driver's licence may be used at land and sea border crossings."},
            {"q": "Can a Canadian citizen be denied entry to Canada?",
             "a": "No. Canadian citizens cannot be denied entry to Canada under any circumstances. If your passport has expired abroad, the Canadian Embassy or Consulate can issue an emergency travel document."},
        ]
        h2_sections = """
<h2>Canadian Citizens and Canadian Entry — No Visa Required</h2>
<p>As a Canadian citizen, you have an <strong>absolute right to enter Canada</strong>. No visa, eTA, or other travel authorisation is needed. You simply present your valid Canadian passport at the port of entry when returning from abroad.</p>

<h2>Returning to Canada from Abroad</h2>
<p>Canadian citizens arriving by air must present a valid Canadian passport. At land and sea crossings, other documents such as a Canadian passport card or enhanced driver's licence may also be accepted under the Western Hemisphere Travel Initiative (WHTI) for entry from the US.</p>

<h2>Living and Working in Canada as a Canadian Citizen</h2>
<p>Canadian citizens have unrestricted rights to live, work, and study anywhere in Canada. If you are applying for Canadian citizenship through naturalisation, visit <a href="https://www.canada.ca/en/immigration-refugees-citizenship" target="_blank" rel="noopener">IRCC (canada.ca/ircc)</a>.</p>

<h2>Travelling to Other Countries from Canada</h2>
<p>The Canadian passport provides <strong>visa-free or visa-on-arrival access to over 180 countries</strong>. See our <a href="visa-free-countries-canada-passport.html">Canadian passport visa-free countries guide</a> for a full list of destinations.</p>
"""
        return faq, h2_sections, badge, related_links

    if "Visa-Free" in vtype and nat_slug == "us":
        faq = [
            {"q": "Do US citizens need a visa for Canada?",
             "a": "No. US citizens are completely visa-exempt for Canada and do not require an eTA. A valid US passport is sufficient for entry at all ports of entry."},
            {"q": "How long can US citizens stay in Canada?",
             "a": "Up to 6 months per visit, as determined by the Canada Border Services Agency (CBSA) officer at the port of entry."},
            {"q": "Can US citizens live and work in Canada?",
             "a": "Short visits are visa-free, but working, studying, or staying beyond 6 months requires the appropriate permit or visa through Immigration, Refugees and Citizenship Canada (IRCC)."},
        ]
        h2_sections = _us_canada_sections()
    elif vtype == "eTA":
        faq = [
            {"q": f"Do {nat_display} citizens need a visa for Canada?",
             "a": f"No. {nat_display} passport holders need an <strong>eTA (Electronic Travel Authorisation)</strong> but not a full visa. The eTA costs CAD 7 and is typically approved within minutes online."},
            {"q": f"How do {nat_display} citizens apply for a Canadian eTA?",
             "a": "Apply at canada.ca/eTA. Fill in your passport details, pay CAD 7 by credit card, and receive email approval — usually instantly, sometimes within 72 hours. The eTA is linked electronically to your passport."},
            {"q": f"How long can {nat_display} citizens stay in Canada on an eTA?",
             "a": "Each visit can be up to 6 months, as authorised by the CBSA officer. The eTA itself is valid for 5 years or until passport expiry, allowing multiple entries."},
        ]
        h2_sections = _eta_sections(nat_display)
    elif nat_slug == "mexican":
        faq = [
            {"q": "Do Mexican citizens need a visa for Canada?",
             "a": "Yes. Canada reinstated a visitor visa requirement for Mexican nationals in February 2009. Mexican passport holders must apply for a Temporary Resident Visa (TRV) at a Canadian visa office."},
            {"q": "Can Mexican citizens use an eTA for Canada instead of a visa?",
             "a": "Mexican nationals who currently hold or have previously held a valid Canadian or US visa may be eligible for an eTA instead of a full visitor visa. Check canada.ca for the current eligibility rules."},
            {"q": "How much does the Canadian visitor visa cost for Mexican citizens?",
             "a": "The application fee is CAD 100 per person. Additional biometric fees of CAD 85 may apply. Processing typically takes 4–12 weeks."},
        ]
        h2_sections = _canada_visa_sections(nat_display, "Mexico", biometrics=False)
    else:
        faq = [
            {"q": f"Do {nat_display} citizens need a visa for Canada?",
             "a": f"Yes. {nat_display} passport holders require a Canadian Visitor Visa (Temporary Resident Visa, TRV). The fee is CAD 100, plus CAD 85 for biometrics. Apply online at ircc.canada.ca."},
            {"q": f"How long does the Canadian visa take for {nat_display} citizens?",
             "a": "Processing typically takes 4–12 weeks, depending on the volume of applications and the specific visa office handling the case. Biometrics (fingerprints and photo) are also required."},
            {"q": f"Can {nat_display} citizens work in Canada on a visitor visa?",
             "a": "No. A visitor visa only allows tourism, family visits, and short business meetings. Working, studying, or staying longer than 6 months requires a separate work or study permit from IRCC."},
        ]
        h2_sections = _canada_visa_sections(nat_display, nat_display, biometrics=True)

    return faq, h2_sections, badge, related_links


def _us_canada_sections():
    return """
<h2>Do Americans Need a Visa or eTA for Canada?</h2>
<p>No. US citizens are fully <strong>visa-exempt</strong> for Canada and do <em>not</em> need an eTA (Electronic Travel Authorisation). A valid US passport is sufficient at all air, land, and sea borders. US Lawful Permanent Residents (green card holders) who are not US citizens must check their own nationality's requirements.</p>

<h2>How Long Can US Citizens Stay in Canada?</h2>
<p>The CBSA officer at the port of entry determines the length of stay — typically up to <strong>6 months</strong> for tourism or short business visits. If you intend to stay longer, you must apply for an extension from inside Canada (via IRCC) before your authorised period expires.</p>

<h2>NEXUS and Trusted Traveller Programmes</h2>
<p>US citizens who frequently cross the border can apply for <strong>NEXUS</strong>, a joint US-Canadian trusted traveller programme that allows expedited processing at dedicated lanes at airports and land borders. NEXUS costs USD/CAD 50 and is valid for 5 years.</p>

<h2>Working or Studying in Canada as a US Citizen</h2>
<p>Tourism and short visits are visa-free, but <strong>employment or study in Canada requires a work or study permit</strong>. Under USMCA, certain US professionals may qualify for a TN work permit, available directly at the port of entry. Apply through Immigration, Refugees and Citizenship Canada (IRCC) at <a href="https://www.canada.ca/en/immigration-refugees-citizenship" target="_blank" rel="noopener">canada.ca/ircc</a>.</p>
"""


def _eta_sections(nd):
    return f"""
<h2>Canada eTA for {nd} Citizens — What You Need to Know</h2>
<p>{nd} passport holders are <strong>visa-exempt for Canada</strong> but must obtain an <strong>Electronic Travel Authorisation (eTA)</strong> before flying to Canada. The eTA is a simple online process, costs <strong>CAD 7</strong>, and is typically approved within <strong>minutes</strong>. It is valid for <strong>5 years</strong> or until passport expiry (whichever comes first) and allows multiple trips.</p>
<p>Note: An eTA is only required for air travel. {nd} citizens arriving by land or sea do <em>not</em> need an eTA (a valid passport is sufficient).</p>

<h2>How to Apply for a Canadian eTA in 2026</h2>
<ol>
<li>Visit the official site: <a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/eta.html" target="_blank" rel="noopener">canada.ca/eTA</a>.</li>
<li>Have your valid {nd} passport, email address, and a credit/debit card ready.</li>
<li>Fill in the online form and pay CAD 7.</li>
<li>Receive your eTA approval email — usually within minutes.</li>
<li>Your eTA is linked electronically to your passport; no need to print anything.</li>
</ol>

<h2>What to Bring When Entering Canada</h2>
<ul>
<li>Valid {nd} passport (with approved eTA linked)</li>
<li>Return or onward ticket</li>
<li>Proof of accommodation in Canada</li>
<li>Sufficient funds for your stay</li>
<li>Travel/health insurance (recommended)</li>
</ul>

<h2>Staying Longer or Moving to Canada</h2>
<p>The eTA allows visits of up to 6 months at a time. For longer stays, study, or work, you must apply for the appropriate Canadian permit or visa through <a href="https://www.canada.ca/en/immigration-refugees-citizenship" target="_blank" rel="noopener">IRCC (Immigration, Refugees and Citizenship Canada)</a> before or during your stay.</p>
"""


def _canada_visa_sections(nd, country_label, biometrics=True):
    bio_note = " Biometrics (fingerprints and photo) are also required (CAD 85)." if biometrics else ""
    bio_docs = "<li>Biometrics appointment confirmation</li>" if biometrics else ""
    return f"""
<h2>Canadian Visitor Visa for {nd} Citizens</h2>
<p>{nd} passport holders require a <strong>Temporary Resident Visa (TRV)</strong> — commonly called a Canadian visitor visa — to enter Canada. The application fee is <strong>CAD 100</strong>.{bio_note} Processing typically takes <strong>4–12 weeks</strong> via the IRCC online portal.</p>

<h2>How to Apply for a Canadian Visa in 2026</h2>
<ol>
<li>Create an account on <a href="https://www.canada.ca/en/immigration-refugees-citizenship" target="_blank" rel="noopener">ircc.canada.ca</a>.</li>
<li>Complete the online application form (IMM 5257).</li>
<li>Pay the CAD 100 visa fee (and CAD 85 biometrics fee if applicable).</li>
<li>Submit documents electronically.</li>
{"<li>Attend a biometrics appointment at a Visa Application Centre (VAC).</li>" if biometrics else ""}
<li>Await a decision — typically 4–12 weeks.</li>
<li>If approved, your passport will be returned with the visa sticker.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid {nd} passport</li>
<li>Completed IMM 5257 application form</li>
<li>Two recent passport photos</li>
<li>Proof of financial support (bank statements, last 3–6 months)</li>
<li>Travel itinerary and accommodation bookings</li>
<li>Letter of invitation (if visiting family/friends)</li>
<li>Proof of employment or enrolment (employment letter, pay stubs)</li>
{bio_docs}
</ul>

<h2>Tips for a Successful Application</h2>
<p>IRCC assesses applications based on your ties to your home country (employment, family, property) and the purpose of your visit. Provide complete, honest, and well-organised documentation. Gaps in information or inconsistencies are the leading cause of refusals. Consider using a certified immigration consultant if your case is complex.</p>
"""


# ── HTML template ─────────────────────────────────────────────────────────────

def build_html(dest_slug, dest_display, dest_flag, nat_slug, nat_display, nat_flag,
               vdata, faq, h2_sections, badge, related_links):
    slug = f"{dest_slug}-visa-for-{nat_slug}-citizens"
    canonical = f"https://www.evisa-card.com/en/{slug}"
    title = f"{dest_display} Visa for {nat_display} Citizens 2026 — ESTA, B1/B2 & Requirements"

    if dest_slug == "usa":
        meta_desc = (
            f"{nat_display} citizens visiting the USA in 2026: visa requirements, "
            f"ESTA eligibility, fees, processing times and how to apply. Complete guide."
        )
    else:
        meta_desc = (
            f"{nat_display} citizens visiting Canada in 2026: visa requirements, "
            f"eTA eligibility, fees, processing times and how to apply. Complete guide."
        )
    # Ensure 150-155 chars — pad / trim
    while len(meta_desc) < 150:
        meta_desc = meta_desc.rstrip(".") + " Updated March 2026."
    meta_desc = meta_desc[:155]

    # Build FAQ JSON-LD
    faq_items = ",\n      ".join(
        '{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'.format(
            q=f["q"].replace('"', '\\"'), a=f["a"].replace('"', '\\"')
        )
        for f in faq
    )
    faq_jsonld = (
        '{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n      '
        + faq_items
        + "\n    ]}}"
    )

    key_facts_header = f"Key Facts — {dest_display} for {nat_display} Citizens"
    h1 = f"{dest_display} Visa for {nat_display} Citizens 2026"

    official_link = (
        "https://esta.cbp.dhs.gov" if dest_slug == "usa"
        else "https://www.canada.ca/en/immigration-refugees-citizenship"
    )
    official_label = "esta.cbp.dhs.gov" if dest_slug == "usa" else "IRCC — canada.ca"

    dest_overview_link = f"visa-{dest_slug}.html"
    dest_overview_label = f"{dest_display} Visa Overview"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{canonical}"/>
    <link rel="alternate" hreflang="en" href="{canonical}"/>
    <link rel="alternate" hreflang="x-default" href="{canonical}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {faq_jsonld}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#ftco-nav" data-toggle="collapse" type="button"><span class="oi oi-menu"></span> Menu</button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;"><span class="fi fi-gb"></span> English</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item active" href="/en/{slug}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/fr/{slug}.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/es/{slug}.html"><span class="fi fi-es"></span> Español</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{nat_flag}" style="margin-right:6px;"></span>{h1}<span class="fi fi-{dest_flag}" style="margin-left:8px;"></span></h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{key_facts_header}</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{badge}</td></tr>
<tr><th>Max Stay</th><td>{vdata["stay"]}</td></tr>
<tr><th>Visa Fee</th><td>{vdata["fee"]}</td></tr>
<tr><th>Processing Time</th><td>{vdata["processing"]}</td></tr>
<tr><th>Apply At</th><td>{vdata["apply_at"]}</td></tr>
</tbody>
</table>

{h2_sections}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{official_link}" target="_blank" rel="noopener">{official_label}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{dest_overview_link}">{dest_overview_label}</a>
{related_links}
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations →</a>
</div>

</article>
</div>
</section>

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
                <p class="mt-4">&copy; 2026 eVisa-Card.com &mdash; Global eVisa &amp; Travel Information Platform</p>
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
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []

    # ── USA pages (all 20 nationalities) ──
    for nat_slug, nat_display, nat_flag in NATIONALITIES:
        vdata = USA_VISA[nat_slug]
        faq, h2_sections, badge, related_links = usa_body(nat_slug, nat_display, nat_flag, vdata)
        html = build_html(
            dest_slug="usa", dest_display="USA", dest_flag="us",
            nat_slug=nat_slug, nat_display=nat_display, nat_flag=nat_flag,
            vdata=vdata, faq=faq, h2_sections=h2_sections, badge=badge,
            related_links=related_links,
        )
        fname = f"usa-visa-for-{nat_slug}-citizens.html"
        fpath = os.path.join(OUTPUT_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        created.append(fname)
        print(f"  Created: {fname}")

    # ── Canada pages (all 20 nationalities) ──
    for nat_slug, nat_display, nat_flag in NATIONALITIES:
        vdata = CANADA_VISA[nat_slug]
        faq, h2_sections, badge, related_links = canada_body(nat_slug, nat_display, nat_flag, vdata)
        html = build_html(
            dest_slug="canada", dest_display="Canada", dest_flag="ca",
            nat_slug=nat_slug, nat_display=nat_display, nat_flag=nat_flag,
            vdata=vdata, faq=faq, h2_sections=h2_sections, badge=badge,
            related_links=related_links,
        )
        fname = f"canada-visa-for-{nat_slug}-citizens.html"
        fpath = os.path.join(OUTPUT_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        created.append(fname)
        print(f"  Created: {fname}")

    print(f"\nTotal files created: {len(created)}")
    assert len(created) == 40, f"Expected 40 files, got {len(created)}"
    print("All 40 files confirmed.")


if __name__ == "__main__":
    main()
