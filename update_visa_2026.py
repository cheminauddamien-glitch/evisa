#!/usr/bin/env python3
"""
update_visa_2026.py — Inject 2026 visa update banner + Important Update alert
into expat guide pages across 10 languages.

Source of truth: VISA_AUDIT_2026.md
Date: 2026-05-20
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent / "www"
UPDATE_DATE_ISO = "2026-05-20"

# ---- 16 countries with their 2026 update info ----
# status: 'major' (alert box), 'minor' (short note), 'current' (banner only)
COUNTRIES = {
    "thailand": {
        "status": "major",
        "effective": "Cabinet decision 19 May 2026 — rollout mid-2026",
        "title": "Thailand visa exemption reform — May 2026",
        "summary": (
            "The Thai Cabinet decided on 19 May 2026 to cancel the 60-day visa-free scheme. "
            "The new policy introduces a <strong>30-day visa exemption for 54 countries</strong> "
            "(Australia, Austria, Canada, France, Germany, Japan, New Zealand, Singapore, UK, US, "
            "etc.) and a <strong>15-day exemption for 3 countries</strong> (Maldives, Mauritius, "
            "Seychelles). The <strong>Thailand Digital Arrival Card (TDAC)</strong> remains "
            "mandatory and replaces the paper TM6."
        ),
        "source_label": "Thai MFA / Royal Gazette",
        "source_url": "https://www.nationthailand.com/news/policy/40066405",
    },
    "vietnam": {
        "status": "major",
        "effective": "1 March 2026 (passport rule) — 15 April 2026 (DAC HCMC)",
        "title": "Vietnam: 90-day e-Visa, passport validity & Digital Arrival Card",
        "summary": (
            "The Vietnam e-Visa is now <strong>90 days, multi-entry</strong> and open to all "
            "nationalities through 83 ports of entry. From <strong>1 March 2026</strong> the "
            "<strong>6-month passport validity</strong> rule is strictly enforced (boarding refused "
            "if passport expires before 1 September 2026). From <strong>15 April 2026</strong> the "
            "<strong>Digital Arrival Card</strong> is mandatory at Tan Son Nhat (HCMC), to be "
            "completed within 72 hours before arrival."
        ),
        "source_label": "Vietnam Immigration Department",
        "source_url": "https://evisa.gov.vn",
    },
    "cambodia": {
        "status": "major",
        "effective": "Already in force; China trial exemption 15 Jun – 15 Oct 2026",
        "title": "Cambodia: mandatory e-Arrival Card, end of paper stamps",
        "summary": (
            "The <strong>Cambodia e-Arrival Card</strong> must be submitted online within 7 days "
            "before the flight, in addition to the e-Visa. Air arrivals no longer receive a "
            "physical passport stamp (email confirmation only). A trial <strong>14-day visa "
            "exemption for Chinese citizens</strong> runs from 15 June to 15 October 2026."
        ),
        "source_label": "Cambodia e-Visa & e-Arrival portals",
        "source_url": "https://www.evisa.gov.kh",
    },
    "uae": {
        "status": "major",
        "effective": "April 2026 (grace period) — health insurance throughout 2026",
        "title": "UAE: mandatory health insurance & end of overstay grace period",
        "summary": (
            "From 2026, <strong>health insurance covering the full stay is mandatory</strong>. A "
            "<strong>colour scan of the passport cover</strong> (in addition to the data page) is "
            "required. From <strong>April 2026</strong>, the grace period after visa expiry is "
            "removed: an automatic <strong>AED 50/day fine</strong> applies immediately. A 30-day "
            "minimum gap is enforced before re-entry on a new 30-day tourist visa."
        ),
        "source_label": "ICP / u.ae",
        "source_url": "https://icp.gov.ae",
    },
    "mexico": {
        "status": "major",
        "effective": "Generalised 2024-2025 (paper FMM phase-out)",
        "title": "Mexico: paper FMM phased out, 180 days no longer guaranteed",
        "summary": (
            "The <strong>paper FMM is being phased out</strong> at major airports (CUN, MEX). "
            "Officers now stamp the passport with a <strong>manually-written number of days</strong> "
            "— the 180-day maximum is no longer automatic. A digital FMM (FMMd) is downloadable "
            "after arrival. The paper FMM is still required at land borders. The 2026 fee is "
            "<strong>MXN 983 (~USD 54)</strong>."
        ),
        "source_label": "INM (Instituto Nacional de Migración)",
        "source_url": "https://www.inm.gob.mx/fmme/publico/en/solicitud.html",
    },
    "panama": {
        "status": "major",
        "effective": "28 October 2024",
        "title": "Panama: Executive Decree 196 — visa exemption expanded",
        "summary": (
            "<strong>Executive Decree 196 (28 October 2024)</strong> expanded visa exemption to "
            "nationals of 'visa-required' countries who hold a valid <strong>multi-entry visa or "
            "residence</strong> from the US, Canada, UK, EU, Japan, South Korea, Singapore or "
            "Australia. Only validity on the day of entry is required. Maximum stay under this "
            "regime is <strong>30 days</strong>. Proof of USD 500 and a return ticket remain "
            "mandatory."
        ),
        "source_label": "Panama Migración",
        "source_url": "https://www.migracion.gob.pa",
    },
    "paraguay": {
        "status": "major",
        "effective": "30 December 2025 + 10 January 2026",
        "title": "Paraguay: Venezuela exemption removed, new exemptions added",
        "summary": (
            "From <strong>10 January 2026</strong>, the visa exemption for <strong>Venezuelan "
            "citizens is abolished</strong> (1996 decree repealed on national security grounds). "
            "From <strong>30 December 2025</strong>, new 30-day exemptions are granted to "
            "<strong>Malaysia and the Philippines</strong>. Trinidad &amp; Tobago and the Bahamas "
            "(90 days) are pending entry into force. Visa-on-arrival is removed except for Oman and "
            "Qatar."
        ),
        "source_label": "Paraguay MRE",
        "source_url": "https://www.mre.gov.py",
    },
    "spain": {
        "status": "major",
        "effective": "3 April 2025 (Golden Visa) — EES fully active since 10 April 2026",
        "title": "Spain: Golden Visa abolished, ETIAS coming Q4 2026",
        "summary": (
            "The <strong>Golden Visa was abolished on 3 April 2025</strong> (Organic Law 1/2025) — "
            "the €500,000 real-estate route is permanently closed. Alternatives include the "
            "<strong>Digital Nomad Visa</strong> (income ≥ 200% SMI ≈ €2,850/month in 2026), the "
            "Non-Lucrative Visa, and the EU Blue Card. The European <strong>EES</strong> has been "
            "fully operational since 10 April 2026 (biometric entry/exit); <strong>ETIAS</strong> "
            "launches in Q4 2026 and is NOT yet required as of May 2026."
        ),
        "source_label": "Spanish Ministry of Foreign Affairs",
        "source_url": "https://www.exteriores.gob.es",
    },
    "georgia": {
        "status": "major",
        "effective": "1 January 2026",
        "title": "Georgia: mandatory travel medical insurance from 1 January 2026",
        "summary": (
            "Since <strong>1 January 2026</strong>, all foreign visitors must hold a <strong>travel "
            "medical insurance policy</strong> with minimum coverage of <strong>30,000 GEL "
            "(~USD 11,000)</strong>, valid for the full duration of the stay, issued in English or "
            "Georgian. Border officers may request proof on entry. Visa-free stay of 365 "
            "consecutive days remains unchanged for the 90+ eligible nationalities."
        ),
        "source_label": "MFA Georgia",
        "source_url": "https://mfa.gov.ge",
    },
    "portugal": {
        "status": "major",
        "effective": "Law 61/2025 promulgated May 2026",
        "title": "Portugal: citizenship now requires 10 years of residence",
        "summary": (
            "<strong>Law 61/2025 (May 2026)</strong> raised the residence requirement for "
            "citizenship to <strong>10 years</strong> (7 years for EU/CPLP nationals) from 5 years "
            "previously. Family reunification is now possible only after 2 years of residence. The "
            "<strong>D8 Digital Nomad Visa</strong> minimum income is <strong>€3,680/month</strong>. "
            "The D7 visa is now reserved for retirees and passive-income holders; freelance "
            "applications are being rejected. The European <strong>EES</strong> is fully active "
            "since 10 April 2026."
        ),
        "source_label": "AIMA (former SEF)",
        "source_url": "https://aima.gov.pt",
    },
    "greece": {
        "status": "major",
        "effective": "Thresholds in force; backdating rule changed in 2026",
        "title": "Greece: Golden Visa thresholds restructured, ETIAS coming Q4 2026",
        "summary": (
            "The Greek <strong>Golden Visa thresholds were restructured</strong>: <strong>€800,000"
            "</strong> in Athens, Thessaloniki, Mykonos, Santorini, Corfu, Rhodes, Crete and "
            "Zakynthos; <strong>€400,000</strong> elsewhere (minimum 120 m²); <strong>€250,000"
            "</strong> only for renovation/conversion projects or the new Start-Up Investment "
            "route. The 5-year permit now runs from issuance, not application date. The European "
            "<strong>EES</strong> is fully operational since 10 April 2026."
        ),
        "source_label": "MFA Greece / Enterprise Greece",
        "source_url": "https://www.mfa.gr",
    },
    "laos": {
        "status": "minor",
        "effective": "Progressive rollout since 1 September 2025",
        "title": "Laos: new Lao Digital Immigration Form (LDIF)",
        "summary": (
            "The <strong>Lao Digital Immigration Form (LDIF)</strong> has been rolled out since "
            "<strong>1 September 2025</strong> at major airports and selected land crossings, with "
            "national deployment progressing throughout 2026. The LDIF is separate from the visa — "
            "visa rules (e-Visa USD 30-50, VoA 30 days, extension +30 days) remain unchanged."
        ),
        "source_label": "Lao Immigration Department",
        "source_url": "https://laoevisa.gov.la",
    },
    "colombia": {
        "status": "minor",
        "effective": "1 January 2026 (annual SMMLV indexation)",
        "title": "Colombia: long-stay visa financial thresholds raised +22.7%",
        "summary": (
            "From <strong>1 January 2026</strong>, the financial thresholds for long-stay visas "
            "(Digital Nomad, Retirement, M and R categories) were <strong>raised by 22.7%</strong>, "
            "tracking the annual revaluation of the Colombian minimum wage. <strong>Travel health "
            "insurance is now mandatory</strong> for all visa categories. The Check-Mig form "
            "remains mandatory (72h–1h before flight). Tourist extension fee: USD 27."
        ),
        "source_label": "Cancillería de Colombia",
        "source_url": "https://www.cancilleria.gov.co",
    },
    "costa-rica": {
        "status": "minor",
        "effective": "Resolution in force since 1 July 2024; perpetual-tourism bill pending",
        "title": "Costa Rica: tighter exemption rules, perpetual-tourism bill in discussion",
        "summary": (
            "A DGME resolution effective <strong>1 July 2024</strong> clarified visa-exemption "
            "rules for travellers holding Schengen C/D or US/Canada multi-entry visas (multi-entry "
            "is now required; stay limited to residual validity). A draft <strong>'perpetual "
            "tourism' bill</strong> is in discussion: overstay fine would rise from USD 100 to "
            "<strong>USD 300/month</strong>, with a 90-day cooling-off period after using the "
            "180-day allowance. Not yet voted as of May 2026."
        ),
        "source_label": "Costa Rica DGME",
        "source_url": "https://www.migracion.go.cr",
    },
    "malaysia": {
        "status": "current",
        "effective": "MDAC mandatory since 1 January 2024",
        "title": "Malaysia: MDAC mandatory, visa-free for China & India extended through 2026",
        "summary": (
            "The <strong>Malaysia Digital Arrival Card (MDAC)</strong> is mandatory for all "
            "foreigners (except Singaporeans, PRs and diplomatic passports) — free, to be filed "
            "within 72 hours before arrival. The 30-day <strong>visa-free regime for China and "
            "India</strong> is extended through the end of 2026. Autogate is open to citizens of "
            "63 countries since June 2024."
        ),
        "source_label": "Malaysia Immigration",
        "source_url": "https://imi.gov.my",
    },
    "japan": {
        "status": "current",
        "effective": "JESTA launch: fiscal year 2028 (April 2028 – March 2029)",
        "title": "Japan: JESTA travel authorisation arriving in 2028",
        "summary": (
            "<strong>JESTA</strong> (Japan Electronic System for Travel Authorization) — the "
            "Japanese ESTA/ETIAS equivalent — has been officially confirmed for launch in "
            "<strong>fiscal year 2028</strong> (April 2028 – March 2029), NOT 2026 despite some "
            "misleading headlines. Estimated fee ¥2,000–6,000. <strong>No operational change in "
            "2026</strong>: the current 90-day visa exemption for 71 nationalities remains in "
            "force."
        ),
        "source_label": "Ministry of Justice / MOFA",
        "source_url": "https://www.mofa.go.jp/j_info/visit/visa/short/novisa.html",
    },
}

# ---- Localized labels for the banner and alert box ----
LANG = {
    "en": {
        "updated": "Updated",
        "date_label": "20 May 2026",
        "effective": "Effective",
        "important": "Important 2026 update",
        "source": "Source",
        "team": "Editorial Team, eVisa-Card.com",
        # regex to find the "Last updated:" paragraph at the top of each guide
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">Last updated:[^<]*?<em>[^<]*?</em></p>'
        ),
        # bottom paragraph still references "March 2026" — replace too
        "pattern_bottom": re.compile(r"Last updated:\s*<strong>March 2026</strong>"),
        "bottom_replace": "Last updated: <strong>20 May 2026</strong>",
    },
    "fr": {
        "updated": "Mis à jour",
        "date_label": "20 mai 2026",
        "effective": "Entrée en vigueur",
        "important": "Mise à jour importante 2026",
        "source": "Source",
        "team": "Équipe éditoriale, eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">Dernière mise à jour[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(Dernière mise à jour|Last updated)[^<]*?<strong>[^<]*2026</strong>"),
        "bottom_replace": "Dernière mise à jour: <strong>20 mai 2026</strong>",
    },
    "es": {
        "updated": "Actualizado",
        "date_label": "20 de mayo de 2026",
        "effective": "Entrada en vigor",
        "important": "Actualización importante 2026",
        "source": "Fuente",
        "team": "Equipo Editorial, eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">Última actualización[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(Última actualización|Last updated)[^<]*?<strong>[^<]*2026</strong>"),
        "bottom_replace": "Última actualización: <strong>20 de mayo de 2026</strong>",
    },
    "pt": {
        "updated": "Atualizado",
        "date_label": "20 de maio de 2026",
        "effective": "Em vigor",
        "important": "Atualização importante 2026",
        "source": "Fonte",
        "team": "Equipe Editorial, eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">(Última atualização|Última actualização|Last updated)[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(Última atualização|Última actualização|Last updated)[^<]*?<strong>[^<]*2026</strong>"),
        "bottom_replace": "Última atualização: <strong>20 de maio de 2026</strong>",
    },
    "zh": {
        "updated": "更新",
        "date_label": "2026年5月20日",
        "effective": "生效",
        "important": "2026年重要更新",
        "source": "来源",
        "team": "编辑小组, eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">最后更新[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(最后更新|Last updated)[^<]*?<strong>[^<]*</strong>"),
        "bottom_replace": "最后更新: <strong>2026年5月20日</strong>",
    },
    "th": {
        "updated": "อัปเดต",
        "date_label": "20 พฤษภาคม 2026",
        "effective": "มีผลบังคับใช้",
        "important": "การอัปเดตที่สำคัญ 2026",
        "source": "ที่มา",
        "team": "ทีมบรรณาธิการ eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">(อัปเดตล่าสุด|ปรับปรุงล่าสุด|Last updated)[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(อัปเดตล่าสุด|ปรับปรุงล่าสุด|Last updated)[^<]*?<strong>[^<]*</strong>"),
        "bottom_replace": "อัปเดตล่าสุด: <strong>20 พฤษภาคม 2026</strong>",
    },
    "ru": {
        "updated": "Обновлено",
        "date_label": "20 мая 2026",
        "effective": "Вступает в силу",
        "important": "Важное обновление 2026",
        "source": "Источник",
        "team": "Редакционная команда, eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">Последнее обновление[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(Последнее обновление|Last updated)[^<]*?<strong>[^<]*</strong>"),
        "bottom_replace": "Последнее обновление: <strong>20 мая 2026</strong>",
    },
    "ar": {
        "updated": "تم التحديث",
        "date_label": "20 مايو 2026",
        "effective": "ساري المفعول",
        "important": "تحديث مهم 2026",
        "source": "المصدر",
        "team": "فريق التحرير، eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">آخر تحديث[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(آخر تحديث|Last updated)[^<]*?<strong>[^<]*</strong>"),
        "bottom_replace": "آخر تحديث: <strong>20 مايو 2026</strong>",
    },
    "ja": {
        "updated": "更新",
        "date_label": "2026年5月20日",
        "effective": "施行",
        "important": "2026年の重要な更新",
        "source": "出典",
        "team": "編集チーム、eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">最終更新[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(最終更新|Last updated)[^<]*?<strong>[^<]*</strong>"),
        "bottom_replace": "最終更新日: <strong>2026年5月20日</strong>",
    },
    "ko": {
        "updated": "업데이트",
        "date_label": "2026년 5월 20일",
        "effective": "시행",
        "important": "2026년 중요 업데이트",
        "source": "출처",
        "team": "편집팀, eVisa-Card.com",
        "pattern_top": re.compile(
            r'<p style="font-size:13px;color:#999;">(마지막 업데이트|최근 업데이트|Last updated)[^<]*?<em>[^<]*?</em></p>'
        ),
        "pattern_bottom": re.compile(r"(마지막 업데이트|최근 업데이트|Last updated)[^<]*?<strong>[^<]*</strong>"),
        "bottom_replace": "마지막 업데이트: <strong>2026년 5월 20일</strong>",
    },
}


def build_banner(lang_code):
    L = LANG[lang_code]
    return (
        f'<p style="font-size:13px;color:#999;">{L["updated"]}: {L["date_label"]} '
        f'— <em>{L["team"]}</em></p>'
    )


def build_alert(lang_code, country):
    """Build the 'Important 2026 update' alert box.
    Title and labels are localized; the factual body stays in English
    (consistent with existing partial-EN state of non-EN guides per project status)."""
    L = LANG[lang_code]
    c = COUNTRIES[country]
    status = c["status"]
    if status == "current":
        return ""  # no alert box for "current" countries — banner only

    # Color and icon by status
    if status == "major":
        bg = "#fff5f0"
        border = "#f15d30"
        icon = "⚠️"
        label = L["important"]
    else:  # minor
        bg = "#f0f6ff"
        border = "#1d2d50"
        icon = "ℹ️"
        label = L["important"]

    src_html = (
        f'<p style="margin:8px 0 0;font-size:.85rem;color:#666;">'
        f'<strong>{L["source"]}:</strong> '
        f'<a href="{c["source_url"]}" rel="nofollow noopener" target="_blank" '
        f'style="color:#1d2d50;">{c["source_label"]}</a></p>'
    )

    return (
        f'\n    <div style="background:{bg};border-left:4px solid {border};'
        f'padding:16px 20px;border-radius:4px;margin:0 0 28px;">\n'
        f'        <p style="margin:0 0 6px;font-weight:600;color:#1d2d50;font-size:1rem;">'
        f'{icon} {label} — {c["title"]}</p>\n'
        f'        <p style="margin:0 0 6px;font-size:.92rem;color:#444;line-height:1.6;">'
        f'{c["summary"]}</p>\n'
        f'        <p style="margin:6px 0 0;font-size:.88rem;color:#444;">'
        f'<strong>{L["effective"]}:</strong> {c["effective"]}</p>\n'
        f'        {src_html}\n'
        f'    </div>'
    )


def update_file(path: Path, lang_code: str, country: str):
    L = LANG[lang_code]
    html = path.read_text(encoding="utf-8")

    new_banner = build_banner(lang_code)
    alert = build_alert(lang_code, country)

    # Replace top "Last updated" paragraph + insert alert immediately after
    def top_repl(m):
        return new_banner + alert

    new_html, n_top = L["pattern_top"].subn(top_repl, html, count=1)

    # Update bottom-of-page "Last updated: March 2026"
    new_html, n_bot = L["pattern_bottom"].subn(L["bottom_replace"], new_html, count=1)

    if n_top == 0:
        return f"  [FAIL] {lang_code}/{country} - top banner NOT FOUND"
    path.write_text(new_html, encoding="utf-8")
    return f"  [OK]   {lang_code}/{country} - alert={'yes' if alert else 'no'}, bottom={n_bot}"


def main():
    print(f"=== eVisa update injection — {UPDATE_DATE_ISO} ===\n")
    total_ok = 0
    total_skip = 0
    for lang_code in LANG:
        print(f"[{lang_code}]")
        for country in COUNTRIES:
            path = ROOT / lang_code / f"expat-guide-{country}.html"
            if not path.exists():
                print(f"  - {country} — file missing")
                total_skip += 1
                continue
            msg = update_file(path, lang_code, country)
            print(msg)
            if "[OK]" in msg:
                total_ok += 1
            else:
                total_skip += 1
        print()
    print(f"=== Done: {total_ok} updated, {total_skip} skipped/failed ===")


if __name__ == "__main__":
    main()
