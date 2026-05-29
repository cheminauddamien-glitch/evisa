"""Enrich thin BUT trafficked nationality pages with genuinely useful,
data-driven sections derived from each page's own Key Facts table. Content
branches by real visa status (visa-free / eVisa / VOA / visa-required) and
weaves in the real fee/stay/processing/portal values, so pages differ
meaningfully rather than sharing boilerplate.

Idempotent: marked with <!-- enriched-v1 -->, skipped if already present.
Inserts before </article>, after the existing sections.
"""
import re, os, sys

ROOT = r'C:\Users\chemi\Documents\evisa\pacific-main'
MARK = '<!-- enriched-v1 -->'


def parse_keyfacts(article):
    d = {}
    for k, v in re.findall(r'<tr><th>(.*?)</th><td>(.*?)</td></tr>', article, re.S):
        key = re.sub(r'<[^>]+>', '', k).strip().lower()
        val = re.sub(r'<[^>]+>', '', v).strip()
        d[key] = val
    return d


def status_of(kf):
    blob = (kf.get('visa required', '') + ' ' + kf.get('visa type', '')).lower()
    if 'visa-free' in blob or 'visa free' in blob or 'no visa' in blob or blob.startswith('no'):
        return 'visa_free'
    if 'voa' in blob or 'on arrival' in blob or 'arrival' in blob:
        return 'voa'
    if 'evisa' in blob or 'e-visa' in blob or 'eta' in blob or 'electronic' in blob:
        return 'evisa'
    return 'visa_required'


def enrich(country, nat, kf):
    """Return HTML of new sections + list of (q,a) for FAQ."""
    st = status_of(kf)
    fee = kf.get('fee', '—')
    stay = kf.get('max stay', kf.get('stay', '—'))
    proc = kf.get('processing', '—')
    portal = kf.get('apply at', '').strip()
    secs = []
    faq = []

    # --- Cost & validity ---
    if st == 'visa_free':
        secs.append((f'Cost & Validity for {nat} Travellers',
            f'<p>{nat} citizens pay <strong>no visa fee</strong> to enter {country} for tourism. '
            f'The permitted stay is <strong>{stay}</strong>, granted automatically on arrival with a '
            f'valid passport. Because entry is visa-free, there is no application form, no embassy '
            f'appointment and no processing wait — {proc.lower() if proc and proc!="—" else "entry is granted at the border"}.</p>'))
        faq.append((f'Is entry to {country} really free for {nat} citizens?',
            f'Yes. {nat} passport holders enter {country} without a visa and without paying a visa fee, '
            f'for stays of {stay}. You only need a passport valid for the duration of your trip and, in some cases, proof of onward travel.'))
    elif st in ('evisa', 'voa'):
        label = 'eVisa' if st == 'evisa' else 'visa on arrival'
        label_title = 'eVisa' if st == 'evisa' else 'Visa on Arrival'
        secs.append((f'{country} {label_title} Cost for {nat} Citizens',
            f'<p>The {label} for {nat} travellers costs <strong>{fee}</strong> and authorises a stay of '
            f'<strong>{stay}</strong>. {("Apply online at <strong>"+portal+"</strong> before you travel." if (st=="evisa" and portal) else "It is issued at the port of entry, so no advance application is required.")} '
            f'Typical processing is <strong>{proc}</strong>, so apply with a comfortable margin before departure.</p>'))
        faq.append((f'How much does the {country} {label} cost for {nat} citizens?',
            f'The {label} fee for {nat} passport holders is {fee}. It covers a stay of {stay}. '
            f'{("Payment is made online during the "+("eVisa") +" application." ) if st=="evisa" else "Payment is collected at the border on arrival."}'))
    else:
        secs.append((f'{country} Visa Cost & Validity for {nat} Citizens',
            f'<p>{nat} citizens must obtain a visa before travelling to {country}. The fee is '
            f'<strong>{fee}</strong> and the visa permits a stay of <strong>{stay}</strong>. '
            f'Applications are filed {("at <strong>"+portal+"</strong>" if portal else "at the nearest consulate")} '
            f'and take <strong>{proc}</strong> to process, so begin the procedure several weeks before departure.</p>'))
        faq.append((f'Do {nat} citizens need a visa to visit {country}?',
            f'Yes. {nat} passport holders must apply for a visa before arrival. The fee is {fee} and processing takes {proc}. '
            f'Apply {("via "+portal) if portal else "through the nearest consulate"} well ahead of your trip.'))

    # --- Stay & overstay (universal but country-named, useful) ---
    secs.append((f'Length of Stay & Overstaying {country}',
        f'<p>The standard tourist stay for {nat} citizens is <strong>{stay}</strong>. Overstaying this '
        f'limit in {country} can lead to fines, deportation and a temporary re-entry ban, so track your '
        f'permitted days carefully. If you need longer, enquire about an extension or a different visa '
        f'category with {country}&rsquo;s immigration authority before your authorised stay expires.</p>'))
    faq.append((f'What happens if a {nat} traveller overstays in {country}?',
        f'Overstaying the {stay} limit can result in fines, removal and a re-entry ban. Always leave or '
        f'regularise your status before your permitted stay ends.'))

    html = f'\n{MARK}\n'
    for title, body in secs:
        hid = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        html += f'<h2 id="{hid}">{title}</h2>\n{body}\n'
    return html, faq


def inject_faq(html, new_faq):
    """Append Q&A to the first FAQPage JSON-LD block."""
    m = re.search(r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)', html, re.S | re.I)
    if not m:
        return html
    # find the FAQPage block specifically
    for sm in re.finditer(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html, re.S | re.I):
        import json
        try:
            data = json.loads(sm.group(1).strip())
        except Exception:
            continue
        if isinstance(data, dict) and data.get('@type') == 'FAQPage':
            for q, a in new_faq:
                data['mainEntity'].append({'@type': 'Question', 'name': q,
                    'acceptedAnswer': {'@type': 'Answer', 'text': a}})
            newblock = sm.group(0)[:sm.group(0).index('>')+1] + '\n    ' + json.dumps(data, ensure_ascii=False) + '\n    </script>'
            return html.replace(sm.group(0), newblock, 1)
    return html


def process(path):
    bn = os.path.basename(path).replace('.html', '')
    m = re.match(r'([a-z-]+)-visa-for-([a-z-]+)-citizens', bn)
    if not m:
        return 0
    country = m.group(1).replace('-', ' ').title()
    nat_map = {'us': 'US', 'uk': 'UK', 'uae': 'UAE'}
    nat = nat_map.get(m.group(2), m.group(2).replace('-', ' ').title())
    h = open(path, encoding='utf-8', errors='replace').read()
    if MARK in h:
        return 0
    am = re.search(r'(<article[^>]*>)(.*?)(</article>)', h, re.S | re.I)
    if not am:
        return 0
    kf = parse_keyfacts(am.group(2))
    if not kf:
        return 0
    new_html, new_faq = enrich(country, nat, kf)
    new_article = am.group(1) + am.group(2) + new_html + am.group(3)
    h2 = h.replace(am.group(0), new_article, 1)
    h2 = inject_faq(h2, new_faq)
    open(path, 'w', encoding='utf-8').write(h2)
    return 1


def main():
    args = sys.argv[1:]
    if args:
        for a in args:
            print(a, '->', process(a))
    else:
        print('pass file paths')


if __name__ == '__main__':
    main()
