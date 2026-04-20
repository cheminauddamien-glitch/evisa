#!/usr/bin/env python3
"""
update_visa_changes_2025_2026.py
Inject 2025-2026 regulatory update banners into visa country pages (EN/FR/ES/PT).

Countries: Brazil, Japan, UK, Thailand, Sri Lanka, China, USA, Canada, + 17 Schengen
"""

import os
import re

WWW = os.path.join(os.path.dirname(__file__), '..', 'www')

# ── Alert HTML template ─────────────────────────────────────────────────────

def make_alert(emoji, label, text, bg='#fff3cd', border='#ffc107', text_color='#856404'):
    return (
        f'<div class="visa-update-alert" style="background:{bg};border-left:4px solid {border};'
        f'padding:14px 18px;border-radius:8px;margin:0 0 18px;color:{text_color};">\n'
        f'  <strong style="font-size:15px;">{emoji} {label}</strong>\n'
        f'  <p style="margin:6px 0 0;font-size:14px;">{text}</p>\n'
        f'</div>'
    )

# ── Per-country update data ─────────────────────────────────────────────────

UPDATES = {

    # Brazil – visa reinstated for USA/Canada/Australia from April 2025
    'visa-brazil': {
        'en': make_alert('⚠️', 'Important Update (April 2025)',
            'Brazil has <strong>reinstated visa requirements</strong> for US, Canadian, and '
            'Australian citizens as of April 2025. Travellers holding those passports now '
            'need a valid visa or eVisa before boarding. Apply at '
            '<a href="https://www.gov.br/mre" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">gov.br/mre</a>.',
        ),
        'fr': make_alert('⚠️', 'Mise à jour importante (avril 2025)',
            'Le Brésil a <strong>réinstauré l\'obligation de visa</strong> pour les citoyens '
            'américains, canadiens et australiens depuis avril 2025. Ces passeports exigent '
            'désormais un visa ou eVisa valide avant l\'embarquement. Demande sur '
            '<a href="https://www.gov.br/mre" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">gov.br/mre</a>.',
        ),
        'es': make_alert('⚠️', 'Actualización importante (abril 2025)',
            'Brasil ha <strong>restablecido el requisito de visa</strong> para ciudadanos de '
            'EE.UU., Canadá y Australia desde abril de 2025. Estos pasaportes requieren ahora '
            'visa o eVisa válida antes del embarque. Solicitud en '
            '<a href="https://www.gov.br/mre" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">gov.br/mre</a>.',
        ),
        'pt': make_alert('⚠️', 'Atualização importante (abril de 2025)',
            'O Brasil <strong>reinstaurou a exigência de visto</strong> para cidadãos '
            'americanos, canadenses e australianos desde abril de 2025. Esses passaportes '
            'agora exigem visto ou eVisa válido antes do embarque. Solicite em '
            '<a href="https://www.gov.br/mre" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">gov.br/mre</a>.',
        ),
    },

    # Japan – visa fees ×5 + departure tax
    'visa-japan': {
        'en': make_alert('⚠️', 'Fee Update (2025)',
            'Japan has significantly increased visa fees. Single-entry tourist/business visa: '
            '<strong>¥15,000</strong> (previously ¥3,000). A <strong>departure tax of '
            '¥3,000</strong> per person is also levied on exit.',
        ),
        'fr': make_alert('⚠️', 'Mise à jour des frais (2025)',
            'Le Japon a considérablement augmenté ses frais de visa. Visa entrée simple '
            'touriste/affaires : <strong>15 000 ¥</strong> (contre 3 000 ¥ auparavant). '
            'Une <strong>taxe de départ de 3 000 ¥</strong> par personne est également '
            'prélevée à la sortie du territoire.',
        ),
        'es': make_alert('⚠️', 'Actualización de tarifas (2025)',
            'Japón ha aumentado significativamente las tarifas de visado. Visado turístico/'
            'negocios de entrada simple: <strong>¥15,000</strong> (antes ¥3,000). '
            'También se cobra un <strong>impuesto de salida de ¥3,000</strong> por persona.',
        ),
        'pt': make_alert('⚠️', 'Atualização de taxas (2025)',
            'O Japão aumentou significativamente as taxas de visto. Visto turístico/negócios '
            'entrada simples: <strong>¥15.000</strong> (antes ¥3.000). '
            'Uma <strong>taxa de saída de ¥3.000</strong> por pessoa também é cobrada.',
        ),
    },

    # UK – eVisa digital mandatory from February 2026
    'visa-united-kingdom': {
        'en': make_alert('⚠️', 'Important Change (February 2026)',
            'Physical visa vignette stickers have been <strong>abolished</strong>. All UK visas '
            'are now fully digital (eVisa). Travellers must create a UK Visas and Immigration '
            '(UKVI) account at '
            '<a href="https://www.gov.uk/get-access-evisa" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">gov.uk/get-access-evisa</a> '
            'and present their eVisa digitally at check-in and the border.',
        ),
        'fr': make_alert('⚠️', 'Changement important (février 2026)',
            'Les vignettes visa physiques ont été <strong>supprimées</strong>. Tous les visas '
            'britanniques sont désormais entièrement numériques (eVisa). Les voyageurs doivent '
            'créer un compte UKVI sur '
            '<a href="https://www.gov.uk/get-access-evisa" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">gov.uk/get-access-evisa</a> '
            'et présenter leur eVisa numériquement à l\'embarquement et à la frontière.',
        ),
        'es': make_alert('⚠️', 'Cambio importante (febrero de 2026)',
            'Las pegatinas de visado físico han sido <strong>abolidas</strong>. Todos los '
            'visados del Reino Unido son ahora completamente digitales (eVisa). Los viajeros '
            'deben crear una cuenta UKVI en '
            '<a href="https://www.gov.uk/get-access-evisa" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">gov.uk/get-access-evisa</a> '
            'y presentar su eVisa digitalmente al embarcar y en la frontera.',
        ),
        'pt': make_alert('⚠️', 'Mudança importante (fevereiro de 2026)',
            'As vinhetas de visto físico foram <strong>abolidas</strong>. Todos os vistos do '
            'Reino Unido são agora totalmente digitais (eVisa). Os viajantes devem criar uma '
            'conta UKVI em '
            '<a href="https://www.gov.uk/get-access-evisa" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">gov.uk/get-access-evisa</a> '
            'e apresentar seu eVisa digitalmente no check-in e na fronteira.',
        ),
    },

    # Thailand – TDAC mandatory since May 2025
    'visa-thailand': {
        'en': make_alert('⚠️', 'Important Update (May 2025)',
            'Thailand now requires <strong>all foreign travellers</strong> to complete the '
            '<strong>Thailand Digital Arrival Card (TDAC)</strong> before arrival. This is '
            'a mandatory online declaration form — not a visa. Complete it at '
            '<a href="https://tdac.immigration.go.th" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">tdac.immigration.go.th</a>.',
        ),
        'fr': make_alert('⚠️', 'Mise à jour importante (mai 2025)',
            'La Thaïlande exige désormais de <strong>tous les voyageurs étrangers</strong> '
            'qu\'ils remplissent la <strong>Carte d\'Arrivée Numérique Thaïlandaise (TDAC)</strong> '
            'avant leur arrivée. Il s\'agit d\'un formulaire de déclaration en ligne obligatoire '
            '— pas d\'un visa. À compléter sur '
            '<a href="https://tdac.immigration.go.th" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">tdac.immigration.go.th</a>.',
        ),
        'es': make_alert('⚠️', 'Actualización importante (mayo de 2025)',
            'Tailandia exige ahora que <strong>todos los viajeros extranjeros</strong> '
            'completen la <strong>Tarjeta de Llegada Digital de Tailandia (TDAC)</strong> '
            'antes de llegar. Es un formulario de declaración en línea obligatorio — no un '
            'visado. Complétalo en '
            '<a href="https://tdac.immigration.go.th" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">tdac.immigration.go.th</a>.',
        ),
        'pt': make_alert('⚠️', 'Atualização importante (maio de 2025)',
            'A Tailândia agora exige que <strong>todos os viajantes estrangeiros</strong> '
            'preencham o <strong>Cartão de Chegada Digital da Tailândia (TDAC)</strong> '
            'antes da chegada. É um formulário de declaração online obrigatório — não um '
            'visto. Preencha em '
            '<a href="https://tdac.immigration.go.th" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">tdac.immigration.go.th</a>.',
        ),
    },

    # Sri Lanka – ETA mandatory before arrival since Oct 2025
    'visa-sri-lanka': {
        'en': make_alert('⚠️', 'Important Update (October 2025)',
            'Sri Lanka now requires <strong>all visitors to obtain an ETA</strong> (Electronic '
            'Travel Authorization) <strong>before arrival</strong> — including previously '
            'visa-free nationalities. Apply at '
            '<a href="https://eta.gov.lk" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">eta.gov.lk</a>. '
            'Approx. 40 nationalities may obtain a visa on arrival if the ETA is unavailable.',
        ),
        'fr': make_alert('⚠️', 'Mise à jour importante (octobre 2025)',
            'Le Sri Lanka exige désormais que <strong>tous les visiteurs obtiennent un ETA</strong> '
            '(autorisation de voyage électronique) <strong>avant leur arrivée</strong> — y '
            'compris les nationalités précédemment exemptées de visa. Demande sur '
            '<a href="https://eta.gov.lk" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">eta.gov.lk</a>. '
            'Environ 40 nationalités peuvent obtenir un visa à l\'arrivée si l\'ETA est indisponible.',
        ),
        'es': make_alert('⚠️', 'Actualización importante (octubre de 2025)',
            'Sri Lanka exige ahora que <strong>todos los visitantes obtengan un ETA</strong> '
            '(Autorización Electrónica de Viaje) <strong>antes de llegar</strong> — incluidas '
            'las nacionalidades antes exentas de visado. Solicitud en '
            '<a href="https://eta.gov.lk" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">eta.gov.lk</a>. '
            'Aprox. 40 nacionalidades pueden obtener visa a la llegada si el ETA no está disponible.',
        ),
        'pt': make_alert('⚠️', 'Atualização importante (outubro de 2025)',
            'O Sri Lanka agora exige que <strong>todos os visitantes obtenham um ETA</strong> '
            '(Autorização Eletrônica de Viagem) <strong>antes da chegada</strong> — incluindo '
            'nacionalidades anteriormente isentas de visto. Solicite em '
            '<a href="https://eta.gov.lk" target="_blank" rel="noopener" '
            'style="color:#856404;font-weight:600;">eta.gov.lk</a>. '
            'Aprox. 40 nacionalidades podem obter visto na chegada se o ETA não estiver disponível.',
        ),
    },

    # China – 30-day visa-free extended to 79 countries
    'visa-china': {
        'en': make_alert('✅', 'Visa-Free Update (February 2026)',
            'China extended its <strong>30-day visa-free programme to 79 countries</strong>, '
            'adding the United Kingdom and Canada in February 2026. Eligible nationals can '
            'stay up to 30 days for tourism, transit, or business without a visa.',
            bg='#d1e7dd', border='#198754', text_color='#0a3622',
        ),
        'fr': make_alert('✅', 'Mise à jour sans visa (février 2026)',
            'La Chine a étendu son <strong>programme sans visa de 30 jours à 79 pays</strong>, '
            'ajoutant le Royaume-Uni et le Canada en février 2026. Les ressortissants éligibles '
            'peuvent séjourner jusqu\'à 30 jours pour le tourisme, le transit ou les affaires '
            'sans visa.',
            bg='#d1e7dd', border='#198754', text_color='#0a3622',
        ),
        'es': make_alert('✅', 'Actualización sin visa (febrero de 2026)',
            'China amplió su <strong>programa sin visa de 30 días a 79 países</strong>, '
            'añadiendo el Reino Unido y Canadá en febrero de 2026. Los nacionales elegibles '
            'pueden permanecer hasta 30 días para turismo, tránsito o negocios sin visa.',
            bg='#d1e7dd', border='#198754', text_color='#0a3622',
        ),
        'pt': make_alert('✅', 'Atualização de isenção de visto (fevereiro de 2026)',
            'A China estendeu seu <strong>programa de isenção de visto de 30 dias para '
            '79 países</strong>, adicionando o Reino Unido e o Canadá em fevereiro de 2026. '
            'Os nacionais elegíveis podem permanecer até 30 dias para turismo, trânsito ou '
            'negócios sem visto.',
            bg='#d1e7dd', border='#198754', text_color='#0a3622',
        ),
    },

    # USA – ESTA fee $21 → $40 since September 2025
    'visa-usa': {
        'en': make_alert('⚠️', 'ESTA Fee Update (September 2025)',
            'The ESTA (Electronic System for Travel Authorization) application fee increased '
            'from <strong>USD 21 to USD 40</strong> as of September 2025. This applies to '
            'all Visa Waiver Program (VWP) eligible travellers to the United States.',
        ),
        'fr': make_alert('⚠️', 'Mise à jour des frais ESTA (septembre 2025)',
            'Le frais de demande d\'ESTA (Système Électronique d\'Autorisation de Voyage) '
            'est passé de <strong>21 $ à 40 $</strong> depuis septembre 2025. Cela s\'applique '
            'à tous les voyageurs des nationalités éligibles au programme VWP se rendant '
            'aux États-Unis.',
        ),
        'es': make_alert('⚠️', 'Actualización de tarifas ESTA (septiembre de 2025)',
            'La tarifa de solicitud del ESTA (Sistema Electrónico de Autorización de Viaje) '
            'aumentó de <strong>USD 21 a USD 40</strong> desde septiembre de 2025. Esto aplica '
            'a todos los viajeros de nacionalidades elegibles para el programa VWP que viajan '
            'a Estados Unidos.',
        ),
        'pt': make_alert('⚠️', 'Atualização da taxa ESTA (setembro de 2025)',
            'A taxa de solicitação do ESTA (Sistema Eletrônico de Autorização de Viagem) '
            'aumentou de <strong>USD 21 para USD 40</strong> desde setembro de 2025. Isso '
            'se aplica a todos os viajantes de nacionalidades elegíveis para o programa VWP '
            'viajando para os Estados Unidos.',
        ),
    },

    # Canada – 13 new eTA countries December 2025
    'visa-canada': {
        'en': make_alert('✅', 'eTA Update (December 2025)',
            'Canada added <strong>13 new countries</strong> to its Electronic Travel '
            'Authorization (eTA) programme in December 2025, including Argentina, Philippines, '
            'and Thailand. Citizens of these countries can now apply for an eTA '
            '(CAD 7, valid 5 years) instead of a full visa for short stays.',
            bg='#d1e7dd', border='#198754', text_color='#0a3622',
        ),
        'fr': make_alert('✅', 'Mise à jour eTA (décembre 2025)',
            'Le Canada a ajouté <strong>13 nouveaux pays</strong> à son programme '
            'd\'Autorisation de Voyage Électronique (eTA) en décembre 2025, dont l\'Argentine, '
            'les Philippines et la Thaïlande. Les citoyens de ces pays peuvent désormais '
            'demander un eTA (7 CAD, valable 5 ans) au lieu d\'un visa complet pour les '
            'courts séjours.',
            bg='#d1e7dd', border='#198754', text_color='#0a3622',
        ),
        'es': make_alert('✅', 'Actualización eTA (diciembre de 2025)',
            'Canadá agregó <strong>13 nuevos países</strong> a su programa de Autorización '
            'Electrónica de Viaje (eTA) en diciembre de 2025, incluidos Argentina, Filipinas '
            'y Tailandia. Los ciudadanos de estos países ahora pueden solicitar eTA '
            '(7 CAD, válido 5 años) en lugar de una visa completa para estancias cortas.',
            bg='#d1e7dd', border='#198754', text_color='#0a3622',
        ),
        'pt': make_alert('✅', 'Atualização eTA (dezembro de 2025)',
            'O Canadá adicionou <strong>13 novos países</strong> ao seu programa de '
            'Autorização Eletrônica de Viagem (eTA) em dezembro de 2025, incluindo Argentina, '
            'Filipinas e Tailândia. Os cidadãos desses países agora podem solicitar eTA '
            '(CAD 7, válido 5 anos) em vez de visto completo para estadias curtas.',
            bg='#d1e7dd', border='#198754', text_color='#0a3622',
        ),
    },
}

# ── Schengen countries: EES + ETIAS ────────────────────────────────────────

SCHENGEN_PAGES = [
    'visa-austria', 'visa-belgium', 'visa-croatia', 'visa-czech-republic',
    'visa-denmark', 'visa-estonia', 'visa-finland', 'visa-france',
    'visa-germany', 'visa-greece', 'visa-hungary', 'visa-italy',
    'visa-latvia', 'visa-lithuania', 'visa-luxembourg', 'visa-malta',
    'visa-netherlands', 'visa-norway', 'visa-poland', 'visa-portugal',
    'visa-slovakia', 'visa-slovenia', 'visa-spain', 'visa-sweden',
    'visa-switzerland',
]

SCHENGEN_ALERTS = {
    'en': make_alert('⚠️', 'Important Updates 2026',
        '<strong>(1) EES (Entry/Exit System)</strong> is now operational across 18 Schengen '
        'states as of <strong>10 April 2026</strong> — all non-EU travellers have biometrics '
        '(fingerprints + photo) registered at the border on first entry. '
        '<strong>(2) ETIAS</strong> (European Travel Information and Authorisation System) '
        'at <strong>€20</strong>, valid 3 years, is announced for <strong>Q4 2026</strong> '
        'and will be mandatory for all Visa Waiver nationals entering the Schengen area.',
    ),
    'fr': make_alert('⚠️', 'Mises à jour importantes 2026',
        '<strong>(1) EES (Système d\'Entrée/Sortie)</strong> est opérationnel dans 18 États '
        'Schengen depuis le <strong>10 avril 2026</strong> — tous les voyageurs non-UE font '
        'enregistrer leurs données biométriques (empreintes + photo) à la frontière à la '
        'première entrée. <strong>(2) L\'ETIAS</strong> (Système Européen d\'Information et '
        'd\'Autorisation de Voyage) à <strong>20 €</strong>, valable 3 ans, est annoncé '
        'pour le <strong>T4 2026</strong> et sera obligatoire pour tous les ressortissants '
        'exemptés de visa entrant dans l\'espace Schengen.',
    ),
    'es': make_alert('⚠️', 'Actualizaciones importantes 2026',
        '<strong>(1) EES (Sistema de Entrada/Salida)</strong> está operativo en 18 estados '
        'Schengen desde el <strong>10 de abril de 2026</strong> — todos los viajeros no-UE '
        'tienen sus datos biométricos (huellas + foto) registrados en la frontera en la '
        'primera entrada. <strong>(2) El ETIAS</strong> (Sistema Europeo de Información y '
        'Autorización de Viajes) a <strong>€20</strong>, válido 3 años, está anunciado '
        'para el <strong>T4 de 2026</strong> y será obligatorio para todos los nacionales '
        'exentos de visado que entren al espacio Schengen.',
    ),
    'pt': make_alert('⚠️', 'Atualizações importantes 2026',
        '<strong>(1) EES (Sistema de Entrada/Saída)</strong> está operacional em 18 estados '
        'Schengen desde <strong>10 de abril de 2026</strong> — todos os viajantes não-UE '
        'têm dados biométricos (impressões digitais + foto) registrados na fronteira na '
        'primeira entrada. <strong>(2) O ETIAS</strong> (Sistema Europeu de Informação e '
        'Autorização de Viagem) a <strong>€20</strong>, válido 3 anos, está anunciado '
        'para o <strong>4T de 2026</strong> e será obrigatório para todos os nacionais '
        'isentos de visto que entrem no espaço Schengen.',
    ),
}

for page in SCHENGEN_PAGES:
    UPDATES[page] = SCHENGEN_ALERTS.copy()

# ── Injection logic ─────────────────────────────────────────────────────────

LANGS = ['en', 'fr', 'es', 'pt']

updated = 0
skipped = 0
errors = 0

for slug, lang_alerts in UPDATES.items():
    for lang in LANGS:
        if lang not in lang_alerts:
            continue
        path = os.path.join(WWW, lang, f'{slug}.html')
        if not os.path.exists(path):
            skipped += 1
            continue
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()

        alert_html = lang_alerts[lang]

        # Skip if already injected
        if 'visa-update-alert' in html:
            skipped += 1
            continue

        # Inject right after </h1> (first occurrence in body)
        new_html = re.sub(
            r'(<h1[^>]*>.*?</h1>)',
            r'\1\n' + alert_html,
            html, count=1, flags=re.DOTALL
        )

        if new_html == html:
            # Fallback: inject before the first <table class="table
            new_html = html.replace(
                '<table class="table table-bordered',
                alert_html + '\n<table class="table table-bordered',
                1,
            )

        if new_html == html:
            print(f'  WARN: no injection point found for {lang}/{slug}.html')
            errors += 1
            continue

        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f'\n✅ Done: {updated} pages updated, {skipped} skipped, {errors} errors')
