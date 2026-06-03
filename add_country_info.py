# -*- coding: utf-8 -*-
"""Action-visas-style enrichment of country hub pages (visa-{country}.html, EN).

Inserts, immediately BEFORE the main Key-Facts table
(table.table.table-bordered.table-sm.mt-3.mb-4):
  1. An SEO intro paragraph for the country.
  2. A "Country information" box: capital, main airports (with IATA codes),
     currency, official language.
And appends a "How to get the {Country} visa?" step section near the end of
the article (before the editorial/related block) if not already present.

Idempotent via <!-- country-info-v1 -->. PROD ONLY (www, absolute paths).
"""
import re, os, glob

WWW = r'C:\Users\chemi\Documents\evisa\pacific-main\www'
MARK = '<!-- country-info-v1 -->'

# country slug -> (Display name, capital, [(airport, IATA), ...], currency, language)
C = {
 'andorra':('Andorra','Andorra la Vella',[('via Barcelona-El Prat','BCN'),('Andorra-La Seu','LEU')],'Euro (EUR)','Catalan'),
 'angola':('Angola','Luanda',[('Luanda Quatro de Fevereiro','LAD')],'Kwanza (AOA)','Portuguese'),
 'argentina':('Argentina','Buenos Aires',[('Ezeiza Intl','EZE'),('Aeroparque','AEP'),('Córdoba','COR')],'Argentine Peso (ARS)','Spanish'),
 'australia':('Australia','Canberra',[('Sydney','SYD'),('Melbourne','MEL'),('Brisbane','BNE')],'Australian Dollar (AUD)','English'),
 'austria':('Austria','Vienna',[('Vienna Intl','VIE'),('Salzburg','SZG')],'Euro (EUR)','German'),
 'bahamas':('Bahamas','Nassau',[('Lynden Pindling Intl','NAS'),('Grand Bahama','FPO')],'Bahamian Dollar (BSD)','English'),
 'bahrain':('Bahrain','Manama',[('Bahrain Intl','BAH')],'Bahraini Dinar (BHD)','Arabic'),
 'belgium':('Belgium','Brussels',[('Brussels','BRU'),('Charleroi','CRL'),('Antwerp','ANR')],'Euro (EUR)','Dutch, French, German'),
 'belize':('Belize','Belmopan',[('Philip Goldson Intl','BZE')],'Belize Dollar (BZD)','English'),
 'bermuda':('Bermuda','Hamilton',[('L.F. Wade Intl','BDA')],'Bermudian Dollar (BMD)','English'),
 'bhutan':('Bhutan','Thimphu',[('Paro Intl','PBH')],'Ngultrum (BTN)','Dzongkha'),
 'brazil':('Brazil','Brasília',[('São Paulo Guarulhos','GRU'),('Rio Galeão','GIG'),('Brasília','BSB')],'Brazilian Real (BRL)','Portuguese'),
 'brunei':('Brunei','Bandar Seri Begawan',[('Brunei Intl','BWN')],'Brunei Dollar (BND)','Malay'),
 'bulgaria':('Bulgaria','Sofia',[('Sofia','SOF'),('Burgas','BOJ'),('Varna','VAR')],'Bulgarian Lev (BGN)','Bulgarian'),
 'cambodia':('Cambodia','Phnom Penh',[('Phnom Penh','PNH'),('Siem Reap-Angkor','SAI')],'Riel (KHR)','Khmer'),
 'canada':('Canada','Ottawa',[('Toronto Pearson','YYZ'),('Vancouver','YVR'),('Montréal','YUL')],'Canadian Dollar (CAD)','English, French'),
 'chile':('Chile','Santiago',[('Santiago Arturo Merino Benítez','SCL')],'Chilean Peso (CLP)','Spanish'),
 'china':('China','Beijing',[('Beijing Capital','PEK'),('Shanghai Pudong','PVG'),('Guangzhou','CAN')],'Renminbi (CNY)','Mandarin Chinese'),
 'colombia':('Colombia','Bogotá',[('Bogotá El Dorado','BOG'),('Medellín','MDE'),('Cartagena','CTG')],'Colombian Peso (COP)','Spanish'),
 'costa-rica':('Costa Rica','San José',[('Juan Santamaría','SJO'),('Liberia','LIR')],'Costa Rican Colón (CRC)','Spanish'),
 'croatia':('Croatia','Zagreb',[('Zagreb','ZAG'),('Split','SPU'),('Dubrovnik','DBV')],'Euro (EUR)','Croatian'),
 'cyprus':('Cyprus','Nicosia',[('Larnaca','LCA'),('Paphos','PFO')],'Euro (EUR)','Greek, Turkish'),
 'czech-republic':('Czech Republic','Prague',[('Prague Václav Havel','PRG')],'Czech Koruna (CZK)','Czech'),
 'denmark':('Denmark','Copenhagen',[('Copenhagen','CPH'),('Billund','BLL')],'Danish Krone (DKK)','Danish'),
 'ecuador':('Ecuador','Quito',[('Quito Mariscal Sucre','UIO'),('Guayaquil','GYE')],'US Dollar (USD)','Spanish'),
 'egypt':('Egypt','Cairo',[('Cairo Intl','CAI'),('Hurghada','HRG'),('Sharm El Sheikh','SSH')],'Egyptian Pound (EGP)','Arabic'),
 'fiji':('Fiji','Suva',[('Nadi Intl','NAN'),('Nausori','SUV')],'Fijian Dollar (FJD)','English, Fijian'),
 'finland':('Finland','Helsinki',[('Helsinki-Vantaa','HEL')],'Euro (EUR)','Finnish, Swedish'),
 'france':('France','Paris',[('Paris Charles de Gaulle','CDG'),('Paris Orly','ORY'),('Nice','NCE')],'Euro (EUR)','French'),
 'georgia':('Georgia','Tbilisi',[('Tbilisi','TBS'),('Batumi','BUS'),('Kutaisi','KUT')],'Lari (GEL)','Georgian'),
 'germany':('Germany','Berlin',[('Frankfurt','FRA'),('Munich','MUC'),('Berlin Brandenburg','BER')],'Euro (EUR)','German'),
 'greece':('Greece','Athens',[('Athens Eleftherios Venizelos','ATH'),('Thessaloniki','SKG'),('Heraklion','HER')],'Euro (EUR)','Greek'),
 'guatemala':('Guatemala','Guatemala City',[('La Aurora','GUA')],'Quetzal (GTQ)','Spanish'),
 'hong-kong':('Hong Kong','Hong Kong (SAR)',[('Hong Kong Intl','HKG')],'Hong Kong Dollar (HKD)','Chinese, English'),
 'hungary':('Hungary','Budapest',[('Budapest Ferenc Liszt','BUD')],'Forint (HUF)','Hungarian'),
 'iceland':('Iceland','Reykjavík',[('Keflavík Intl','KEF')],'Icelandic Króna (ISK)','Icelandic'),
 'india':('India','New Delhi',[('Delhi Indira Gandhi','DEL'),('Mumbai','BOM'),('Bengaluru','BLR')],'Indian Rupee (INR)','Hindi, English'),
 'indonesia':('Indonesia','Jakarta',[('Jakarta Soekarno-Hatta','CGK'),('Bali Ngurah Rai','DPS')],'Rupiah (IDR)','Indonesian'),
 'iran':('Iran','Tehran',[('Tehran Imam Khomeini','IKA')],'Iranian Rial (IRR)','Persian'),
 'iraq':('Iraq','Baghdad',[('Baghdad Intl','BGW'),('Erbil','EBL')],'Iraqi Dinar (IQD)','Arabic, Kurdish'),
 'ireland':('Ireland','Dublin',[('Dublin','DUB'),('Cork','ORK'),('Shannon','SNN')],'Euro (EUR)','English, Irish'),
 'israel':('Israel','Jerusalem',[('Tel Aviv Ben Gurion','TLV')],'Israeli New Shekel (ILS)','Hebrew, Arabic'),
 'italy':('Italy','Rome',[('Rome Fiumicino','FCO'),('Milan Malpensa','MXP'),('Venice','VCE')],'Euro (EUR)','Italian'),
 'japan':('Japan','Tokyo',[('Tokyo Narita','NRT'),('Tokyo Haneda','HND'),('Osaka Kansai','KIX')],'Japanese Yen (JPY)','Japanese'),
 'jordan':('Jordan','Amman',[('Amman Queen Alia','AMM'),('Aqaba King Hussein','AQJ')],'Jordanian Dinar (JOD)','Arabic'),
 'kuwait':('Kuwait','Kuwait City',[('Kuwait Intl','KWI')],'Kuwaiti Dinar (KWD)','Arabic'),
 'laos':('Laos','Vientiane',[('Wattay Intl','VTE'),('Luang Prabang','LPQ')],'Kip (LAK)','Lao'),
 'liechtenstein':('Liechtenstein','Vaduz',[('via Zurich','ZRH')],'Swiss Franc (CHF)','German'),
 'luxembourg':('Luxembourg','Luxembourg City',[('Luxembourg-Findel','LUX')],'Euro (EUR)','Luxembourgish, French, German'),
 'macau':('Macau','Macau (SAR)',[('Macau Intl','MFM')],'Pataca (MOP)','Chinese, Portuguese'),
 'malaysia':('Malaysia','Kuala Lumpur',[('Kuala Lumpur Intl','KUL'),('Kota Kinabalu','BKI'),('Penang','PEN')],'Ringgit (MYR)','Malay'),
 'maldives':('Maldives','Malé',[('Velana Intl','MLE')],'Rufiyaa (MVR)','Dhivehi'),
 'mexico':('Mexico','Mexico City',[('Mexico City Intl','MEX'),('Cancún','CUN'),('Guadalajara','GDL')],'Mexican Peso (MXN)','Spanish'),
 'moldova':('Moldova','Chișinău',[('Chișinău Intl','KIV')],'Moldovan Leu (MDL)','Romanian'),
 'myanmar':('Myanmar','Naypyidaw',[('Yangon Intl','RGN'),('Mandalay','MDL')],'Kyat (MMK)','Burmese'),
 'nepal':('Nepal','Kathmandu',[('Kathmandu Tribhuvan','KTM'),('Pokhara','PKR')],'Nepalese Rupee (NPR)','Nepali'),
 'netherlands':('Netherlands','Amsterdam',[('Amsterdam Schiphol','AMS'),('Rotterdam','RTM'),('Eindhoven','EIN')],'Euro (EUR)','Dutch'),
 'new-zealand':('New Zealand','Wellington',[('Auckland','AKL'),('Christchurch','CHC'),('Wellington','WLG')],'New Zealand Dollar (NZD)','English, Māori'),
 'nicaragua':('Nicaragua','Managua',[('Managua Augusto C. Sandino','MGA')],'Córdoba (NIO)','Spanish'),
 'norway':('Norway','Oslo',[('Oslo Gardermoen','OSL'),('Bergen','BGO')],'Norwegian Krone (NOK)','Norwegian'),
 'oman':('Oman','Muscat',[('Muscat Intl','MCT'),('Salalah','SLL')],'Omani Rial (OMR)','Arabic'),
 'panama':('Panama','Panama City',[('Tocumen Intl','PTY')],'Balboa (PAB) / US Dollar','Spanish'),
 'peru':('Peru','Lima',[('Lima Jorge Chávez','LIM'),('Cusco','CUZ')],'Sol (PEN)','Spanish'),
 'philippines':('Philippines','Manila',[('Manila Ninoy Aquino','MNL'),('Cebu','CEB'),('Clark','CRK')],'Philippine Peso (PHP)','Filipino, English'),
 'poland':('Poland','Warsaw',[('Warsaw Chopin','WAW'),('Kraków','KRK')],'Złoty (PLN)','Polish'),
 'portugal':('Portugal','Lisbon',[('Lisbon Humberto Delgado','LIS'),('Porto','OPO'),('Faro','FAO')],'Euro (EUR)','Portuguese'),
 'qatar':('Qatar','Doha',[('Hamad Intl','DOH')],'Qatari Riyal (QAR)','Arabic'),
 'romania':('Romania','Bucharest',[('Bucharest Henri Coandă','OTP'),('Cluj-Napoca','CLJ')],'Romanian Leu (RON)','Romanian'),
 'samoa':('Samoa','Apia',[('Faleolo Intl','APW')],'Tālā (WST)','Samoan, English'),
 'singapore':('Singapore','Singapore',[('Changi','SIN')],'Singapore Dollar (SGD)','English, Malay, Mandarin, Tamil'),
 'slovakia':('Slovakia','Bratislava',[('Bratislava','BTS'),('Košice','KSC')],'Euro (EUR)','Slovak'),
 'slovenia':('Slovenia','Ljubljana',[('Ljubljana Jože Pučnik','LJU')],'Euro (EUR)','Slovenian'),
 'south-korea':('South Korea','Seoul',[('Incheon Intl','ICN'),('Gimpo','GMP'),('Busan','PUS')],'South Korean Won (KRW)','Korean'),
 'spain':('Spain','Madrid',[('Madrid Barajas','MAD'),('Barcelona El Prat','BCN'),('Palma','PMI')],'Euro (EUR)','Spanish'),
 'sri-lanka':('Sri Lanka','Colombo (Sri Jayawardenepura Kotte)',[('Bandaranaike Intl','CMB')],'Sri Lankan Rupee (LKR)','Sinhala, Tamil'),
 'sweden':('Sweden','Stockholm',[('Stockholm Arlanda','ARN'),('Gothenburg','GOT')],'Swedish Krona (SEK)','Swedish'),
 'switzerland':('Switzerland','Bern',[('Zurich','ZRH'),('Geneva','GVA'),('Basel','BSL')],'Swiss Franc (CHF)','German, French, Italian'),
 'taiwan':('Taiwan','Taipei',[('Taoyuan Intl','TPE'),('Taipei Songshan','TSA'),('Kaohsiung','KHH')],'New Taiwan Dollar (TWD)','Mandarin Chinese'),
 'thailand':('Thailand','Bangkok',[('Suvarnabhumi','BKK'),('Don Mueang','DMK'),('Phuket','HKT')],'Thai Baht (THB)','Thai'),
 'tonga':('Tonga','Nukuʻalofa',[('Fuaʻamotu Intl','TBU')],'Paʻanga (TOP)','Tongan, English'),
 'turkey':('Turkey','Ankara',[('Istanbul Airport','IST'),('Istanbul Sabiha Gökçen','SAW'),('Antalya','AYT')],'Turkish Lira (TRY)','Turkish'),
 'uae':('United Arab Emirates','Abu Dhabi',[('Dubai Intl','DXB'),('Abu Dhabi','AUH'),('Sharjah','SHJ')],'UAE Dirham (AED)','Arabic'),
 'uk':('United Kingdom','London',[('London Heathrow','LHR'),('London Gatwick','LGW'),('Manchester','MAN')],'Pound Sterling (GBP)','English'),
 'united-kingdom':('United Kingdom','London',[('London Heathrow','LHR'),('London Gatwick','LGW'),('Manchester','MAN')],'Pound Sterling (GBP)','English'),
 'ukraine':('Ukraine','Kyiv',[('Kyiv Boryspil','KBP'),('Lviv','LWO')],'Hryvnia (UAH)','Ukrainian'),
 'uruguay':('Uruguay','Montevideo',[('Montevideo Carrasco','MVD')],'Uruguayan Peso (UYU)','Spanish'),
 'usa':('United States','Washington, D.C.',[('New York JFK','JFK'),('Los Angeles','LAX'),('Miami','MIA')],'US Dollar (USD)','English'),
 'venezuela':('Venezuela','Caracas',[('Caracas Simón Bolívar','CCS')],'Bolívar (VES)','Spanish'),
 'vietnam':('Vietnam','Hanoi',[('Hanoi Noi Bai','HAN'),('Ho Chi Minh Tan Son Nhat','SGN'),('Da Nang','DAD')],'Vietnamese Dong (VND)','Vietnamese'),
}


def info_box(name, cap, airports, cur, lang):
    air = ', '.join(f'{a} ({code})' for a, code in airports)
    intro = (f'<p>Planning a trip to <strong>{name}</strong>? This 2026 guide explains the '
             f'visa rules, costs and entry requirements for {name}, plus the practical '
             f'travel details you need before you go. Below you will find the key facts at a '
             f'glance, followed by visa categories, required documents and a step-by-step '
             f'application guide.</p>')
    box = (f'<div class="country-info-box" style="background:#f8f9fc;border:1px solid #e5e7eb;'
           f'border-radius:8px;padding:16px 20px;margin:0 0 20px;">'
           f'<h2 class="h5" style="margin-top:0;">{name} — Country Information</h2>'
           f'<ul class="mb-0" style="columns:2;-webkit-columns:2;list-style:none;padding-left:0;">'
           f'<li><strong>Capital:</strong> {cap}</li>'
           f'<li><strong>Currency:</strong> {cur}</li>'
           f'<li><strong>Official language:</strong> {lang}</li>'
           f'<li><strong>Main airports:</strong> {air}</li>'
           f'</ul></div>')
    return MARK + '\n' + intro + '\n' + box + '\n'


def how_to(name):
    return (f'\n<h2 id="how-to-get-{re.sub(r"[^a-z]+","-",name.lower()).strip("-")}-visa">'
            f'How to get the {name} visa?</h2>\n'
            f'<ol>'
            f'<li><strong>Check whether you need a visa.</strong> Confirm your nationality\'s '
            f'requirement for {name} in the table above (visa-free, eVisa, visa on arrival or consular visa).</li>'
            f'<li><strong>Choose the right visa type</strong> for your trip — tourism, business, transit, work or study.</li>'
            f'<li><strong>Prepare your documents:</strong> a passport valid at least 6 months, a recent photo, '
            f'proof of accommodation and onward travel, and sufficient funds.</li>'
            f'<li><strong>Apply</strong> online (eVisa) or at the nearest {name} embassy/consulate, and pay the visa fee.</li>'
            f'<li><strong>Receive your visa</strong> and print or save the approval before you travel to {name}.</li>'
            f'</ol>'
            f'<p>For the exact fee, processing time and document list for your nationality, see the dedicated '
            f'requirements and fees guides linked on this page.</p>\n')


TABLE_RE = re.compile(r'<table class="table table-bordered table-sm[^"]*">')


def process(slug):
    if slug not in C:
        return 'no-data'
    name, cap, airports, cur, lang = C[slug]
    path = os.path.join(WWW, 'en', f'visa-{slug}.html')
    if not os.path.exists(path):
        return 'missing'
    h = open(path, encoding='utf-8', errors='replace').read()
    if MARK in h:
        return 'already'
    m = TABLE_RE.search(h)
    if not m:
        return 'no-table'
    block = info_box(name, cap, airports, cur, lang)
    h2 = h[:m.start()] + block + h[m.start():]
    # add How-to before the editorial/related block or before </article>
    if f'How to get the {name} visa' not in h2:
        anchor = None
        for a in ('<div class="eeat-section', '<div class="related-guides', '</article>'):
            if a in h2:
                anchor = a; break
        if anchor:
            h2 = h2.replace(anchor, how_to(name) + anchor, 1)
    open(path, 'w', encoding='utf-8').write(h2)
    return 'ok'


def main():
    import sys
    only = sys.argv[1:] if len(sys.argv) > 1 else sorted(C.keys())
    res = {}
    for slug in only:
        r = process(slug)
        res[r] = res.get(r, 0) + 1
    print(res)


if __name__ == '__main__':
    main()
