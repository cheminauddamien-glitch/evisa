#!/usr/bin/env python3
"""
1. Fix navbar alignment: language selector inline with nav items
2. Translate + complete all 48 card descriptions in fr/es/pt destination.html
"""
import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

# ── 1. Navbar alignment fix ───────────────────────────────────────────────────
# Change: collapse div gets justify-content-center, ul loses mx-auto → align-items-center
# Result: all nav items + language selector are one centered inline group

fixed_nav = errors_nav = 0

all_html = (
    glob.glob(os.path.join(WWW, "*.html")) +
    glob.glob(os.path.join(WWW, "en", "*.html")) +
    glob.glob(os.path.join(WWW, "fr", "*.html")) +
    glob.glob(os.path.join(WWW, "es", "*.html")) +
    glob.glob(os.path.join(WWW, "pt", "*.html"))
)

for fpath in all_html:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        orig = html
        # Fix collapse div — add justify-content-center
        html = html.replace(
            'class="collapse navbar-collapse" id="ftco-nav"',
            'class="collapse navbar-collapse justify-content-center" id="ftco-nav"'
        )
        # Fix ul — replace mx-auto with align-items-center
        html = html.replace(
            'class="navbar-nav mx-auto"',
            'class="navbar-nav align-items-center"'
        )
        # Remove ml-2 from language dropdown (no extra gap)
        html = html.replace(
            'class="nav-item dropdown ml-2"',
            'class="nav-item dropdown ml-3"'
        )
        if html != orig:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            fixed_nav += 1
    except Exception as e:
        print(f"ERR {fpath}: {e}")
        errors_nav += 1

print(f"Navbar alignment fixed: {fixed_nav} pages | Errors: {errors_nav}")


# ── 2. Translate + complete 48 card descriptions in destination.html ──────────

# Full (non-truncated) descriptions per country
DESCS = {
    "en": {
        "<p>Apply online for India e-Visa for tourism or business. Valid up to one year with…</p>":
            "<p>Apply online for India e-Visa for tourism or business. Valid up to 1 year with multiple entries. Processing 3–5 days.</p>",
        "<p>Thailand eVisa or visa exemption for many nationalities. Typical tourist stays up to…</p>":
            "<p>Thailand offers 60-day visa exemption for 60+ nationalities. eVisa available for others. Extendable on arrival.</p>",
        "<p>Japan generally requires visitor visas for certain nationalities. Check electronic…</p>":
            "<p>Japan requires visitor visas for some nationalities. eVisa available. Visa-free for 70+ countries for 90 days.</p>",
        "<p>China visitor visas vary by purpose and nationality. Use official consular portals for…</p>":
            "<p>China visitor visas vary by purpose and nationality. 144-hour transit visa-free program available in major cities.</p>",
        "<p>Indonesia eVisa for tourism allows short stays (commonly 30 days). Apply via the…</p>":
            "<p>Indonesia eVisa allows 30-day stays, extendable to 60 days. Apply via the official immigration portal.</p>",
        "<p>Malaysia often offers visa-free entry for many countries; eVisas available for others.…</p>":
            "<p>Malaysia offers visa-free entry for 60+ nationalities. eVisa available for others. MM2H program for long stays.</p>",
        "<p>Singapore grants visa-free travel to many nationalities. When required, apply via…</p>":
            "<p>Singapore grants visa-free travel to 160+ nationalities. When required, apply via the ICA e-Service portal.</p>",
        "<p>Many nationalities enter Philippines visa-free; eVisas and VOAs exist for others. Fees…</p>":
            "<p>190+ nationalities enter Philippines visa-free for 30 days. eVisa and Visa on Arrival available for others.</p>",
        "<p>Vietnam eVisa allows stays typically 30 or 90 days. Use official immigration portals…</p>":
            "<p>Vietnam eVisa allows 90-day stays (single or multiple entry). Apply online via the official immigration portal.</p>",
        "<p>Cambodia eVisa is commonly used for tourism (30 days). Apply via the official website…</p>":
            "<p>Cambodia eVisa (30 days, single entry) is available online. Visa on arrival also available at major border points.</p>",
        "<p>Sri Lanka ETA is required for many visitors; apply online and check processing times,…</p>":
            "<p>Sri Lanka ETA required for most visitors. Apply online for 30-day stay, extendable to 90 days. Processing 1–2 days.</p>",
        "<p>Maldives offers visa on arrival for tourists. Ensure passport validity and note any…</p>":
            "<p>Maldives offers free 30-day visa on arrival for all nationalities. Passport must be valid for 6+ months.</p>",
        "<p>Nepal issues tourist visas on arrival and via embassy; confirm fees, passport photo…</p>":
            "<p>Nepal tourist visa available on arrival and online. 15, 30 or 90-day options. Multiple entry permits available.</p>",
        "<p>Turkey eVisa is available to many travelers online; check nationality rules, single vs…</p>":
            "<p>Turkey eVisa available online for 50+ nationalities. Single or multiple entry, up to 90 days within 180 days.</p>",
        "<p>UAE offers visa-free access or eVisas for many nationalities; check transit vs tourist…</p>":
            "<p>UAE offers visa-free entry for 50+ nationalities (30–180 days). eVisa and visa on arrival available for others.</p>",
        "<p>UK Standard Visitor visa covers tourism, business and short studies. Application…</p>":
            "<p>UK Standard Visitor visa covers tourism, business and short studies (up to 6 months). Apply via UK Visas & Immigration.</p>",
        "<p>France follows Schengen rules for short stays (90 days). Apply through consular…</p>":
            "<p>France follows Schengen rules: 90 days within 180 days. Apply via French consulate. Standard Schengen documents required.</p>",
        "<p>Spain requires Schengen visas for many nationals. Prepare travel itinerary, proof of…</p>":
            "<p>Spain requires Schengen visa for many nationalities. Prepare travel itinerary, proof of funds and travel insurance.</p>",
        "<p>Italy issues Schengen short-stay visas; typical requirements include itinerary,…</p>":
            "<p>Italy issues Schengen visas for stays up to 90 days. Requirements include itinerary, hotel booking and travel insurance.</p>",
        "<p>Germany follows Schengen procedures for visitors. Applications require documentation,…</p>":
            "<p>Germany follows Schengen procedures. Applications require full documentation and a consulate appointment.</p>",
        "<p>Netherlands requires Schengen visas for many visitors. Check consulate-specific…</p>":
            "<p>Netherlands requires Schengen visa for many nationalities. Check Dutch consulate requirements in your country.</p>",
        "<p>Belgium issues Schengen visas; travellers should prepare standard documents, proof of…</p>":
            "<p>Belgium issues Schengen visas. Prepare standard documents, proof of funds and accommodation booking.</p>",
        "<p>Portugal follows Schengen rules for short stays. Ensure documents, travel insurance…</p>":
            "<p>Portugal follows Schengen rules for stays up to 90 days. Ensure valid documents, travel insurance and proof of funds.</p>",
        "<p>Greece follows Schengen visa rules; tourist applications should include proof of…</p>":
            "<p>Greece follows Schengen visa rules. Tourist applications must include proof of accommodation and sufficient funds.</p>",
        "<p>Switzerland is part of Schengen for visa purposes. Apply for short-stay visas via…</p>":
            "<p>Switzerland is part of Schengen. Apply for short-stay visas via the Swiss embassy or VFS Global in your country.</p>",
        "<p>Austrian Schengen visas require booking appointments and document submission. Check…</p>":
            "<p>Austrian Schengen visas require appointment booking and full document submission at the consulate.</p>",
        "<p>Croatia now aligns with Schengen rules for many travellers; check whether you need a…</p>":
            "<p>Croatia now aligns with Schengen rules. Check if you need a national visa or if Schengen visa applies.</p>",
        "<p>Czech Schengen visa applications require standard documents and consular appointments;…</p>":
            "<p>Czech Schengen visa applications require standard documents and a consulate appointment. Processing 10–15 days.</p>",
        "<p>Poland issues Schengen visas for short stays. Ensure you follow the local consulate…</p>":
            "<p>Poland issues Schengen visas for short stays (90 days). Follow local consulate requirements and book in advance.</p>",
        "<p>Hungary processes Schengen visas through their consulates; be aware of required…</p>":
            "<p>Hungary processes Schengen visas through its consulates. Prepare required documents and allow 10–15 days processing.</p>",
        "<p>Sweden requires Schengen visas for many visitors; check the Swedish consulate…</p>":
            "<p>Sweden requires Schengen visas for many nationalities. Check the Swedish consulate or VFS Global in your country.</p>",
        "<p>Norway applies Schengen rules; applicants must provide proof of travel plans,…</p>":
            "<p>Norway applies Schengen rules. Provide proof of travel plans, accommodation, travel insurance and sufficient funds.</p>",
        "<p>Denmark requires Schengen visas for eligible travellers; check specific embassy…</p>":
            "<p>Denmark requires Schengen visas for eligible travellers. Check specific embassy requirements for your nationality.</p>",
        "<p>Ireland has its own visitor visa rules outside Schengen. Check Irish immigration for…</p>":
            "<p>Ireland has its own visitor visa rules outside Schengen. Check Irish Immigration Service for your nationality requirements.</p>",
        "<p>Romania has specific national visa rules and is in transition regarding Schengen;…</p>":
            "<p>Romania has specific national visa rules. Now fully part of Schengen for air and sea travel since 2024.</p>",
        "<p>ESTA required for visa-waiver countries. Apply online at esta.cbp.dhs.gov before travel.</p>":
            "<p>ESTA required for 40+ visa-waiver countries. Apply online at esta.cbp.dhs.gov. Valid 2 years, multiple trips.</p>",
        "<p>Electronic Travel Authorization required for visa-exempt nationals. Apply online before fl</p>":
            "<p>Canada eTA required for visa-exempt nationals flying in. Apply online at ircc.canada.ca. Valid 5 years.</p>",
        "<p>Most nationalities enter visa-free for up to 180 days. FMM tourist card required on arriva</p>":
            "<p>Most nationalities enter Mexico visa-free for up to 180 days. FMM tourist card required on arrival (free at border).</p>",
        "<p>Brazil eVisa available online for many nationalities. US citizens can enter visa-free sinc</p>":
            "<p>Brazil eVisa available online for many nationalities. US, Canadian and Australian citizens enter visa-free since 2024.</p>",
        "<p>Most Western passport holders enter visa-free for 90 days. Reciprocity fee abolished.</p>":
            "<p>Most Western passport holders enter Argentina visa-free for 90 days. Reciprocity fee abolished since 2016.</p>",
        "<p>No visa required for most nationalities for stays up to 90 days, extendable to 180 days.</p>":
            "<p>Colombia: no visa required for most nationalities for stays up to 90 days, extendable to 180 days per year.</p>",
        "<p>Visa-free access for most nationalities. A-1 immigration form required on arrival.</p>":
            "<p>Peru: visa-free for most nationalities for up to 183 days. Migration form required on arrival.</p>",
        "<p>Visa on arrival available for most nationalities at Amman airport. Jordan Pass includes entry fee.</p>":
            "<p>Jordan visa on arrival at Amman airport for most nationalities (JOD 40). Jordan Pass includes the entry fee.</p>",
        "<p>100+ nationalities enter visa-free. eVisa available via MOI portal for others.</p>":
            "<p>Oman: 100+ nationalities enter visa-free for 14 days. eVisa available via MOI portal for others (up to 30 days).</p>",
        "<p>eVisitor (subclass 651) free for EU/UK/US. ETA (subclass 601) for others. Apply online via</p>":
            "<p>Australia: free eVisitor (651) for EU/UK/US. ETA (601) for other eligible nationals. Apply via ImmiAccount.</p>",
        "<p>New Zealand Electronic Travel Authority required for visa-waiver nationals. Apply online b</p>":
            "<p>New Zealand NZeTA required for visa-waiver nationals. Apply online via Immigration NZ app or website. NZD 23.</p>",
        "<p>Most nationalities enter visa-free. British nationals get 180 days. No eVisa system curren</p>":
            "<p>South Africa: most nationalities enter visa-free for 30–90 days. British nationals get 180 days. No eVisa currently.</p>",
        "<p>Visa-free for 60+ nationalities. eVisa available for others via BOCA Taiwan portal.</p>":
            "<p>Taiwan: visa-free for 60+ nationalities (30–90 days). eVisa available for others via BOCA Taiwan portal.</p>",
    }
}

# Build FR/ES/PT translations from the completed EN descriptions
DEST_CARD_TRANS = {
    "fr": {
        "<p>Apply online for India e-Visa for tourism or business. Valid up to 1 year with multiple entries. Processing 3–5 days.</p>": "<p>Demandez l'e-Visa indien en ligne pour tourisme ou affaires. Valide 1 an avec entrées multiples. Traitement 3–5 jours.</p>",
        "<p>Thailand offers 60-day visa exemption for 60+ nationalities. eVisa available for others. Extendable on arrival.</p>": "<p>La Thaïlande offre une exemption de visa de 60 jours pour 60+ nationalités. eVisa disponible pour les autres. Prolongeable.</p>",
        "<p>Japan requires visitor visas for some nationalities. eVisa available. Visa-free for 70+ countries for 90 days.</p>": "<p>Le Japon exige un visa pour certaines nationalités. eVisa disponible. Exemption pour 70+ pays (90 jours).</p>",
        "<p>China visitor visas vary by purpose and nationality. 144-hour transit visa-free program available in major cities.</p>": "<p>Visas visiteurs variables selon le motif et la nationalité. Programme transit sans visa 144h disponible dans les grandes villes.</p>",
        "<p>Indonesia eVisa allows 30-day stays, extendable to 60 days. Apply via the official immigration portal.</p>": "<p>L'eVisa indonésien permet des séjours de 30 jours, extensibles à 60. Demandez via le portail officiel d'immigration.</p>",
        "<p>Malaysia offers visa-free entry for 60+ nationalities. eVisa available for others. MM2H program for long stays.</p>": "<p>Malaisie : entrée sans visa pour 60+ nationalités. eVisa pour les autres. Programme MM2H pour les longs séjours.</p>",
        "<p>Singapore grants visa-free travel to 160+ nationalities. When required, apply via the ICA e-Service portal.</p>": "<p>Singapour : voyage sans visa pour 160+ nationalités. Si requis, demandez via le portail e-Service ICA.</p>",
        "<p>190+ nationalities enter Philippines visa-free for 30 days. eVisa and Visa on Arrival available for others.</p>": "<p>190+ nationalités entrent aux Philippines sans visa (30 jours). eVisa et VOA disponibles pour les autres.</p>",
        "<p>Vietnam eVisa allows 90-day stays (single or multiple entry). Apply online via the official immigration portal.</p>": "<p>L'eVisa vietnamien permet des séjours de 90 jours (entrée simple ou multiple). Demandez sur le portail officiel.</p>",
        "<p>Cambodia eVisa (30 days, single entry) is available online. Visa on arrival also available at major border points.</p>": "<p>L'eVisa cambodgien (30 jours, entrée unique) est disponible en ligne. VOA aussi aux principaux postes-frontières.</p>",
        "<p>Sri Lanka ETA required for most visitors. Apply online for 30-day stay, extendable to 90 days. Processing 1–2 days.</p>": "<p>L'ETA du Sri Lanka est requise pour la plupart des visiteurs. Séjour 30 jours, extensible à 90. Traitement 1–2 jours.</p>",
        "<p>Maldives offers free 30-day visa on arrival for all nationalities. Passport must be valid for 6+ months.</p>": "<p>Les Maldives offrent un visa gratuit à l'arrivée (30 jours) pour toutes les nationalités. Passeport valide 6+ mois requis.</p>",
        "<p>Nepal tourist visa available on arrival and online. 15, 30 or 90-day options. Multiple entry permits available.</p>": "<p>Visa touristique Népal disponible à l'arrivée et en ligne. Options 15, 30 ou 90 jours. Permis multi-entrées disponibles.</p>",
        "<p>Turkey eVisa available online for 50+ nationalities. Single or multiple entry, up to 90 days within 180 days.</p>": "<p>L'eVisa turc est disponible en ligne pour 50+ nationalités. Entrée simple ou multiple, jusqu'à 90 jours sur 180.</p>",
        "<p>UAE offers visa-free entry for 50+ nationalities (30–180 days). eVisa and visa on arrival available for others.</p>": "<p>EAU : entrée sans visa pour 50+ nationalités (30–180 jours). eVisa et visa à l'arrivée disponibles pour les autres.</p>",
        "<p>UK Standard Visitor visa covers tourism, business and short studies (up to 6 months). Apply via UK Visas & Immigration.</p>": "<p>Le visa Standard Visitor UK couvre tourisme, affaires et études courtes (6 mois). Demandez via UK Visas & Immigration.</p>",
        "<p>France follows Schengen rules: 90 days within 180 days. Apply via French consulate. Standard Schengen documents required.</p>": "<p>La France suit les règles Schengen : 90 jours sur 180. Demandez au consulat français avec les documents Schengen standards.</p>",
        "<p>Spain requires Schengen visa for many nationalities. Prepare travel itinerary, proof of funds and travel insurance.</p>": "<p>L'Espagne exige un visa Schengen pour de nombreuses nationalités. Préparez l'itinéraire, les justificatifs financiers et l'assurance.</p>",
        "<p>Italy issues Schengen visas for stays up to 90 days. Requirements include itinerary, hotel booking and travel insurance.</p>": "<p>L'Italie délivre des visas Schengen jusqu'à 90 jours. Exigences : itinéraire, hébergement et assurance voyage.</p>",
        "<p>Germany follows Schengen procedures. Applications require full documentation and a consulate appointment.</p>": "<p>L'Allemagne suit les procédures Schengen. Les demandes nécessitent une documentation complète et un rendez-vous consulaire.</p>",
        "<p>Netherlands requires Schengen visa for many nationalities. Check Dutch consulate requirements in your country.</p>": "<p>Les Pays-Bas exigent un visa Schengen pour de nombreuses nationalités. Vérifiez les exigences du consulat néerlandais.</p>",
        "<p>Belgium issues Schengen visas. Prepare standard documents, proof of funds and accommodation booking.</p>": "<p>La Belgique délivre des visas Schengen. Préparez documents standards, justificatifs financiers et réservation d'hébergement.</p>",
        "<p>Portugal follows Schengen rules for stays up to 90 days. Ensure valid documents, travel insurance and proof of funds.</p>": "<p>Le Portugal suit les règles Schengen (90 jours). Assurez-vous d'avoir documents valides, assurance voyage et fonds suffisants.</p>",
        "<p>Greece follows Schengen visa rules. Tourist applications must include proof of accommodation and sufficient funds.</p>": "<p>La Grèce suit les règles Schengen. Les demandes touristiques incluent preuve d'hébergement et fonds suffisants.</p>",
        "<p>Switzerland is part of Schengen. Apply for short-stay visas via the Swiss embassy or VFS Global in your country.</p>": "<p>La Suisse fait partie de Schengen. Demandez les visas de court séjour via l'ambassade suisse ou VFS Global.</p>",
        "<p>Austrian Schengen visas require appointment booking and full document submission at the consulate.</p>": "<p>Les visas Schengen autrichiens nécessitent une prise de rendez-vous et le dépôt complet des documents au consulat.</p>",
        "<p>Croatia now aligns with Schengen rules. Check if you need a national visa or if Schengen visa applies.</p>": "<p>La Croatie applique désormais les règles Schengen. Vérifiez si vous avez besoin d'un visa national ou Schengen.</p>",
        "<p>Czech Schengen visa applications require standard documents and a consulate appointment. Processing 10–15 days.</p>": "<p>Les visas Schengen tchèques nécessitent documents standards et rendez-vous consulaire. Traitement 10–15 jours.</p>",
        "<p>Poland issues Schengen visas for short stays (90 days). Follow local consulate requirements and book in advance.</p>": "<p>La Pologne délivre des visas Schengen (90 jours). Respectez les exigences du consulat local et réservez à l'avance.</p>",
        "<p>Hungary processes Schengen visas through its consulates. Prepare required documents and allow 10–15 days processing.</p>": "<p>La Hongrie traite les visas Schengen via ses consulats. Préparez les documents et comptez 10–15 jours de traitement.</p>",
        "<p>Sweden requires Schengen visas for many nationalities. Check the Swedish consulate or VFS Global in your country.</p>": "<p>La Suède exige un visa Schengen pour de nombreuses nationalités. Consultez le consulat suédois ou VFS Global.</p>",
        "<p>Norway applies Schengen rules. Provide proof of travel plans, accommodation, travel insurance and sufficient funds.</p>": "<p>La Norvège applique les règles Schengen. Fournissez preuve de voyage, hébergement, assurance et fonds suffisants.</p>",
        "<p>Denmark requires Schengen visas for eligible travellers. Check specific embassy requirements for your nationality.</p>": "<p>Le Danemark exige un visa Schengen pour les voyageurs éligibles. Vérifiez les exigences spécifiques à votre nationalité.</p>",
        "<p>Ireland has its own visitor visa rules outside Schengen. Check Irish Immigration Service for your nationality requirements.</p>": "<p>L'Irlande a ses propres règles de visa visiteur hors Schengen. Vérifiez l'Irish Immigration Service pour votre nationalité.</p>",
        "<p>Romania has specific national visa rules. Now fully part of Schengen for air and sea travel since 2024.</p>": "<p>La Roumanie a ses propres règles de visa. Membre à part entière de Schengen pour les voyages aériens et maritimes depuis 2024.</p>",
        "<p>ESTA required for 40+ visa-waiver countries. Apply online at esta.cbp.dhs.gov. Valid 2 years, multiple trips.</p>": "<p>ESTA requise pour 40+ pays exemptés de visa. Demandez sur esta.cbp.dhs.gov. Valide 2 ans, voyages multiples.</p>",
        "<p>Canada eTA required for visa-exempt nationals flying in. Apply online at ircc.canada.ca. Valid 5 years.</p>": "<p>L'AVE canadienne est requise pour les ressortissants exemptés de visa voyageant par avion. Valide 5 ans.</p>",
        "<p>Most nationalities enter Mexico visa-free for up to 180 days. FMM tourist card required on arrival (free at border).</p>": "<p>La plupart des nationalités entrent au Mexique sans visa (180 jours). Carte FMM requise à l'arrivée (gratuite aux frontières).</p>",
        "<p>Brazil eVisa available online for many nationalities. US, Canadian and Australian citizens enter visa-free since 2024.</p>": "<p>L'eVisa brésilien est disponible en ligne. Les citoyens américains, canadiens et australiens entrent sans visa depuis 2024.</p>",
        "<p>Most Western passport holders enter Argentina visa-free for 90 days. Reciprocity fee abolished since 2016.</p>": "<p>La plupart des passeports occidentaux entrent en Argentine sans visa (90 jours). Taxe de réciprocité supprimée depuis 2016.</p>",
        "<p>Colombia: no visa required for most nationalities for stays up to 90 days, extendable to 180 days per year.</p>": "<p>Colombie : pas de visa requis pour la plupart des nationalités jusqu'à 90 jours, extensible à 180 jours par an.</p>",
        "<p>Peru: visa-free for most nationalities for up to 183 days. Migration form required on arrival.</p>": "<p>Pérou : sans visa pour la plupart des nationalités jusqu'à 183 jours. Formulaire de migration requis à l'arrivée.</p>",
        "<p>Jordan visa on arrival at Amman airport for most nationalities (JOD 40). Jordan Pass includes the entry fee.</p>": "<p>Visa à l'arrivée à l'aéroport d'Amman pour la plupart des nationalités (40 JOD). Jordan Pass inclut les frais d'entrée.</p>",
        "<p>Oman: 100+ nationalities enter visa-free for 14 days. eVisa available via MOI portal for others (up to 30 days).</p>": "<p>Oman : 100+ nationalités entrent sans visa (14 jours). eVisa disponible via le portail MOI pour les autres (30 jours).</p>",
        "<p>Australia: free eVisitor (651) for EU/UK/US. ETA (601) for other eligible nationals. Apply via ImmiAccount.</p>": "<p>Australie : eVisitor gratuit (651) pour UE/UK/US. ETA (601) pour d'autres nationals éligibles. Demandez via ImmiAccount.</p>",
        "<p>New Zealand NZeTA required for visa-waiver nationals. Apply online via Immigration NZ app or website. NZD 23.</p>": "<p>NZeTA requise pour les ressortissants exemptés de visa. Demandez via l'app Immigration NZ. 23 NZD.</p>",
        "<p>South Africa: most nationalities enter visa-free for 30–90 days. British nationals get 180 days. No eVisa currently.</p>": "<p>Afrique du Sud : sans visa pour la plupart (30–90 jours). Les Britanniques obtiennent 180 jours. Pas d'eVisa actuellement.</p>",
        "<p>Taiwan: visa-free for 60+ nationalities (30–90 days). eVisa available for others via BOCA Taiwan portal.</p>": "<p>Taïwan : sans visa pour 60+ nationalités (30–90 jours). eVisa disponible pour les autres via le portail BOCA.</p>",
    },
    "es": {
        "<p>Apply online for India e-Visa for tourism or business. Valid up to 1 year with multiple entries. Processing 3–5 days.</p>": "<p>Solicita el e-Visa de India en línea para turismo o negocios. Válido 1 año con entradas múltiples. Procesamiento 3–5 días.</p>",
        "<p>Thailand offers 60-day visa exemption for 60+ nationalities. eVisa available for others. Extendable on arrival.</p>": "<p>Tailandia ofrece exención de visa de 60 días para 60+ nacionalidades. eVisa disponible para otras. Extensible a la llegada.</p>",
        "<p>Japan requires visitor visas for some nationalities. eVisa available. Visa-free for 70+ countries for 90 days.</p>": "<p>Japón requiere visa para algunas nacionalidades. eVisa disponible. Sin visa para 70+ países (90 días).</p>",
        "<p>China visitor visas vary by purpose and nationality. 144-hour transit visa-free program available in major cities.</p>": "<p>Las visas chinas varían según propósito y nacionalidad. Programa tránsito sin visa 144 horas en las principales ciudades.</p>",
        "<p>Indonesia eVisa allows 30-day stays, extendable to 60 days. Apply via the official immigration portal.</p>": "<p>El eVisa de Indonesia permite estadías de 30 días, extensibles a 60. Solicita en el portal oficial de inmigración.</p>",
        "<p>Malaysia offers visa-free entry for 60+ nationalities. eVisa available for others. MM2H program for long stays.</p>": "<p>Malasia: entrada sin visa para 60+ nacionalidades. eVisa para otras. Programa MM2H para estancias largas.</p>",
        "<p>Singapore grants visa-free travel to 160+ nationalities. When required, apply via the ICA e-Service portal.</p>": "<p>Singapur: viaje sin visa para 160+ nacionalidades. Si se requiere, solicita en el portal e-Service de ICA.</p>",
        "<p>190+ nationalities enter Philippines visa-free for 30 days. eVisa and Visa on Arrival available for others.</p>": "<p>190+ nacionalidades entran a Filipinas sin visa (30 días). eVisa y visa a la llegada disponibles para otras.</p>",
        "<p>Vietnam eVisa allows 90-day stays (single or multiple entry). Apply online via the official immigration portal.</p>": "<p>El eVisa de Vietnam permite 90 días (entrada simple o múltiple). Solicita en el portal oficial de inmigración.</p>",
        "<p>Cambodia eVisa (30 days, single entry) is available online. Visa on arrival also available at major border points.</p>": "<p>eVisa de Camboya (30 días, entrada única) disponible en línea. Visa a la llegada en los principales puestos fronterizos.</p>",
        "<p>Sri Lanka ETA required for most visitors. Apply online for 30-day stay, extendable to 90 days. Processing 1–2 days.</p>": "<p>ETA de Sri Lanka requerida para la mayoría de visitantes. 30 días, extensibles a 90. Procesamiento 1–2 días.</p>",
        "<p>Maldives offers free 30-day visa on arrival for all nationalities. Passport must be valid for 6+ months.</p>": "<p>Maldivas ofrece visa gratuita a la llegada (30 días) para todas las nacionalidades. Pasaporte válido 6+ meses.</p>",
        "<p>Nepal tourist visa available on arrival and online. 15, 30 or 90-day options. Multiple entry permits available.</p>": "<p>Visa turístico de Nepal disponible a la llegada y en línea. Opciones 15, 30 o 90 días. Permisos de entrada múltiple disponibles.</p>",
        "<p>Turkey eVisa available online for 50+ nationalities. Single or multiple entry, up to 90 days within 180 days.</p>": "<p>eVisa de Turquía disponible en línea para 50+ nacionalidades. Entrada simple o múltiple, hasta 90 días en 180.</p>",
        "<p>UAE offers visa-free entry for 50+ nationalities (30–180 days). eVisa and visa on arrival available for others.</p>": "<p>EAU: entrada sin visa para 50+ nacionalidades (30–180 días). eVisa y visa a la llegada para las demás.</p>",
        "<p>UK Standard Visitor visa covers tourism, business and short studies (up to 6 months). Apply via UK Visas & Immigration.</p>": "<p>La visa Standard Visitor UK cubre turismo, negocios y estudios cortos (6 meses). Solicita en UK Visas & Immigration.</p>",
        "<p>France follows Schengen rules: 90 days within 180 days. Apply via French consulate. Standard Schengen documents required.</p>": "<p>Francia sigue reglas Schengen: 90 días en 180. Solicita en el consulado francés con documentos Schengen estándar.</p>",
        "<p>Spain requires Schengen visa for many nationalities. Prepare travel itinerary, proof of funds and travel insurance.</p>": "<p>España requiere visa Schengen para muchas nacionalidades. Prepara itinerario, justificante de fondos y seguro de viaje.</p>",
        "<p>Italy issues Schengen visas for stays up to 90 days. Requirements include itinerary, hotel booking and travel insurance.</p>": "<p>Italia expide visas Schengen hasta 90 días. Requisitos: itinerario, reserva de hotel y seguro de viaje.</p>",
        "<p>Germany follows Schengen procedures. Applications require full documentation and a consulate appointment.</p>": "<p>Alemania sigue procedimientos Schengen. Las solicitudes requieren documentación completa y cita en el consulado.</p>",
        "<p>Netherlands requires Schengen visa for many nationalities. Check Dutch consulate requirements in your country.</p>": "<p>Países Bajos: visa Schengen requerida para muchas nacionalidades. Consulta los requisitos del consulado neerlandés.</p>",
        "<p>Belgium issues Schengen visas. Prepare standard documents, proof of funds and accommodation booking.</p>": "<p>Bélgica expide visas Schengen. Prepara documentos estándar, justificante de fondos y reserva de alojamiento.</p>",
        "<p>Portugal follows Schengen rules for stays up to 90 days. Ensure valid documents, travel insurance and proof of funds.</p>": "<p>Portugal sigue reglas Schengen (90 días). Asegúrate de tener documentos válidos, seguro de viaje y fondos suficientes.</p>",
        "<p>Greece follows Schengen visa rules. Tourist applications must include proof of accommodation and sufficient funds.</p>": "<p>Grecia sigue las reglas Schengen. Las solicitudes turísticas incluyen prueba de alojamiento y fondos suficientes.</p>",
        "<p>Switzerland is part of Schengen. Apply for short-stay visas via the Swiss embassy or VFS Global in your country.</p>": "<p>Suiza forma parte de Schengen. Solicita visas de corta estancia en la embajada suiza o VFS Global en tu país.</p>",
        "<p>Austrian Schengen visas require appointment booking and full document submission at the consulate.</p>": "<p>Las visas Schengen austriacas requieren cita previa y entrega completa de documentos en el consulado.</p>",
        "<p>Croatia now aligns with Schengen rules. Check if you need a national visa or if Schengen visa applies.</p>": "<p>Croacia aplica ahora las reglas Schengen. Verifica si necesitas visa nacional o si aplica la visa Schengen.</p>",
        "<p>Czech Schengen visa applications require standard documents and a consulate appointment. Processing 10–15 days.</p>": "<p>Las visas Schengen checas requieren documentos estándar y cita en el consulado. Procesamiento 10–15 días.</p>",
        "<p>Poland issues Schengen visas for short stays (90 days). Follow local consulate requirements and book in advance.</p>": "<p>Polonia expide visas Schengen (90 días). Sigue los requisitos del consulado local y reserva con antelación.</p>",
        "<p>Hungary processes Schengen visas through its consulates. Prepare required documents and allow 10–15 days processing.</p>": "<p>Hungría tramita visas Schengen en sus consulados. Prepara los documentos y cuenta con 10–15 días de procesamiento.</p>",
        "<p>Sweden requires Schengen visas for many nationalities. Check the Swedish consulate or VFS Global in your country.</p>": "<p>Suecia requiere visa Schengen para muchas nacionalidades. Consulta el consulado sueco o VFS Global en tu país.</p>",
        "<p>Norway applies Schengen rules. Provide proof of travel plans, accommodation, travel insurance and sufficient funds.</p>": "<p>Noruega aplica reglas Schengen. Proporciona prueba de itinerario, alojamiento, seguro de viaje y fondos suficientes.</p>",
        "<p>Denmark requires Schengen visas for eligible travellers. Check specific embassy requirements for your nationality.</p>": "<p>Dinamarca requiere visa Schengen para viajeros elegibles. Consulta los requisitos específicos para tu nacionalidad.</p>",
        "<p>Ireland has its own visitor visa rules outside Schengen. Check Irish Immigration Service for your nationality requirements.</p>": "<p>Irlanda tiene sus propias reglas de visa fuera de Schengen. Consulta el Servicio de Inmigración Irlandés para tu nacionalidad.</p>",
        "<p>Romania has specific national visa rules. Now fully part of Schengen for air and sea travel since 2024.</p>": "<p>Rumanía tiene reglas propias de visa. Miembro pleno de Schengen para viajes aéreos y marítimos desde 2024.</p>",
        "<p>ESTA required for 40+ visa-waiver countries. Apply online at esta.cbp.dhs.gov. Valid 2 years, multiple trips.</p>": "<p>ESTA requerida para 40+ países exentos de visa. Solicita en esta.cbp.dhs.gov. Válida 2 años, múltiples viajes.</p>",
        "<p>Canada eTA required for visa-exempt nationals flying in. Apply online at ircc.canada.ca. Valid 5 years.</p>": "<p>AVE de Canadá requerida para nacionales exentos de visa que viajan en avión. Válida 5 años.</p>",
        "<p>Most nationalities enter Mexico visa-free for up to 180 days. FMM tourist card required on arrival (free at border).</p>": "<p>La mayoría de las nacionalidades entran a México sin visa (180 días). Tarjeta FMM requerida a la llegada (gratuita en frontera).</p>",
        "<p>Brazil eVisa available online for many nationalities. US, Canadian and Australian citizens enter visa-free since 2024.</p>": "<p>eVisa brasileño disponible en línea. Ciudadanos de EE.UU., Canadá y Australia entran sin visa desde 2024.</p>",
        "<p>Most Western passport holders enter Argentina visa-free for 90 days. Reciprocity fee abolished since 2016.</p>": "<p>La mayoría de pasaportes occidentales entran a Argentina sin visa (90 días). Tasa de reciprocidad eliminada en 2016.</p>",
        "<p>Colombia: no visa required for most nationalities for stays up to 90 days, extendable to 180 days per year.</p>": "<p>Colombia: sin visa para la mayoría de nacionalidades hasta 90 días, extensibles a 180 días por año.</p>",
        "<p>Peru: visa-free for most nationalities for up to 183 days. Migration form required on arrival.</p>": "<p>Perú: sin visa para la mayoría de nacionalidades hasta 183 días. Formulario de migración requerido a la llegada.</p>",
        "<p>Jordan visa on arrival at Amman airport for most nationalities (JOD 40). Jordan Pass includes the entry fee.</p>": "<p>Visa a la llegada en el aeropuerto de Amman para la mayoría (40 JOD). Jordan Pass incluye la tarifa de entrada.</p>",
        "<p>Oman: 100+ nationalities enter visa-free for 14 days. eVisa available via MOI portal for others (up to 30 days).</p>": "<p>Omán: 100+ nacionalidades entran sin visa (14 días). eVisa disponible vía portal MOI para otras (30 días).</p>",
        "<p>Australia: free eVisitor (651) for EU/UK/US. ETA (601) for other eligible nationals. Apply via ImmiAccount.</p>": "<p>Australia: eVisitor gratuito (651) para UE/UK/US. ETA (601) para otros nacionales elegibles. Solicita en ImmiAccount.</p>",
        "<p>New Zealand NZeTA required for visa-waiver nationals. Apply online via Immigration NZ app or website. NZD 23.</p>": "<p>NZeTA requerida para nacionales exentos de visa en Nueva Zelanda. Solicita vía app Immigration NZ. NZD 23.</p>",
        "<p>South Africa: most nationalities enter visa-free for 30–90 days. British nationals get 180 days. No eVisa currently.</p>": "<p>Sudáfrica: sin visa para la mayoría (30–90 días). Nacionales británicos obtienen 180 días. Sin eVisa actualmente.</p>",
        "<p>Taiwan: visa-free for 60+ nationalities (30–90 days). eVisa available for others via BOCA Taiwan portal.</p>": "<p>Taiwán: sin visa para 60+ nacionalidades (30–90 días). eVisa disponible para otros vía portal BOCA Taiwán.</p>",
    },
    "pt": {
        "<p>Apply online for India e-Visa for tourism or business. Valid up to 1 year with multiple entries. Processing 3–5 days.</p>": "<p>Solicite o e-Visa da Índia online para turismo ou negócios. Válido 1 ano com entradas múltiplas. Processamento 3–5 dias.</p>",
        "<p>Thailand offers 60-day visa exemption for 60+ nationalities. eVisa available for others. Extendable on arrival.</p>": "<p>A Tailândia oferece isenção de visto de 60 dias para 60+ nacionalidades. eVisa disponível para outras. Prorrogável.</p>",
        "<p>Japan requires visitor visas for some nationalities. eVisa available. Visa-free for 70+ countries for 90 days.</p>": "<p>O Japão exige visto para algumas nacionalidades. eVisa disponível. Isenção para 70+ países (90 dias).</p>",
        "<p>China visitor visas vary by purpose and nationality. 144-hour transit visa-free program available in major cities.</p>": "<p>Vistos da China variam por propósito e nacionalidade. Programa de trânsito sem visto de 144h nas principais cidades.</p>",
        "<p>Indonesia eVisa allows 30-day stays, extendable to 60 days. Apply via the official immigration portal.</p>": "<p>O eVisa da Indonésia permite estadias de 30 dias, prorrogáveis a 60. Solicite no portal oficial de imigração.</p>",
        "<p>Malaysia offers visa-free entry for 60+ nationalities. eVisa available for others. MM2H program for long stays.</p>": "<p>Malásia: entrada sem visto para 60+ nacionalidades. eVisa para outras. Programa MM2H para longas estadias.</p>",
        "<p>Singapore grants visa-free travel to 160+ nationalities. When required, apply via the ICA e-Service portal.</p>": "<p>Singapura: viagem sem visto para 160+ nacionalidades. Se necessário, solicite via portal e-Service da ICA.</p>",
        "<p>190+ nationalities enter Philippines visa-free for 30 days. eVisa and Visa on Arrival available for others.</p>": "<p>190+ nacionalidades entram nas Filipinas sem visto (30 dias). eVisa e visto na chegada disponíveis para outras.</p>",
        "<p>Vietnam eVisa allows 90-day stays (single or multiple entry). Apply online via the official immigration portal.</p>": "<p>O eVisa do Vietnã permite 90 dias (entrada simples ou múltipla). Solicite no portal oficial de imigração.</p>",
        "<p>Cambodia eVisa (30 days, single entry) is available online. Visa on arrival also available at major border points.</p>": "<p>eVisa do Camboja (30 dias, entrada única) disponível online. Visto na chegada nos principais postos de fronteira.</p>",
        "<p>Sri Lanka ETA required for most visitors. Apply online for 30-day stay, extendable to 90 days. Processing 1–2 days.</p>": "<p>ETA do Sri Lanka obrigatória para a maioria. 30 dias, prorrogáveis a 90. Processamento 1–2 dias.</p>",
        "<p>Maldives offers free 30-day visa on arrival for all nationalities. Passport must be valid for 6+ months.</p>": "<p>Maldivas oferece visto gratuito na chegada (30 dias) para todas as nacionalidades. Passaporte válido por 6+ meses.</p>",
        "<p>Nepal tourist visa available on arrival and online. 15, 30 or 90-day options. Multiple entry permits available.</p>": "<p>Visto turístico do Nepal disponível na chegada e online. Opções de 15, 30 ou 90 dias. Permissões de múltiplas entradas.</p>",
        "<p>Turkey eVisa available online for 50+ nationalities. Single or multiple entry, up to 90 days within 180 days.</p>": "<p>eVisa da Turquia disponível online para 50+ nacionalidades. Entrada simples ou múltipla, até 90 dias em 180.</p>",
        "<p>UAE offers visa-free entry for 50+ nationalities (30–180 days). eVisa and visa on arrival available for others.</p>": "<p>EAU: entrada sem visto para 50+ nacionalidades (30–180 dias). eVisa e visto na chegada para as demais.</p>",
        "<p>UK Standard Visitor visa covers tourism, business and short studies (up to 6 months). Apply via UK Visas & Immigration.</p>": "<p>O visto Standard Visitor do Reino Unido cobre turismo, negócios e estudos curtos (6 meses). Solicite via UK Visas & Immigration.</p>",
        "<p>France follows Schengen rules: 90 days within 180 days. Apply via French consulate. Standard Schengen documents required.</p>": "<p>A França segue regras Schengen: 90 dias em 180. Solicite no consulado francês com documentos Schengen padrão.</p>",
        "<p>Spain requires Schengen visa for many nationalities. Prepare travel itinerary, proof of funds and travel insurance.</p>": "<p>A Espanha exige visto Schengen para muitas nacionalidades. Prepare itinerário, comprovante de fundos e seguro viagem.</p>",
        "<p>Italy issues Schengen visas for stays up to 90 days. Requirements include itinerary, hotel booking and travel insurance.</p>": "<p>A Itália emite vistos Schengen até 90 dias. Requisitos: itinerário, reserva de hotel e seguro viagem.</p>",
        "<p>Germany follows Schengen procedures. Applications require full documentation and a consulate appointment.</p>": "<p>A Alemanha segue procedimentos Schengen. Solicitações exigem documentação completa e agendamento consular.</p>",
        "<p>Netherlands requires Schengen visa for many nationalities. Check Dutch consulate requirements in your country.</p>": "<p>Países Baixos: visto Schengen exigido para muitas nacionalidades. Verifique os requisitos do consulado holandês.</p>",
        "<p>Belgium issues Schengen visas. Prepare standard documents, proof of funds and accommodation booking.</p>": "<p>A Bélgica emite vistos Schengen. Prepare documentos padrão, comprovante de fundos e reserva de hospedagem.</p>",
        "<p>Portugal follows Schengen rules for stays up to 90 days. Ensure valid documents, travel insurance and proof of funds.</p>": "<p>Portugal segue regras Schengen (90 dias). Certifique-se de ter documentos válidos, seguro viagem e fundos suficientes.</p>",
        "<p>Greece follows Schengen visa rules. Tourist applications must include proof of accommodation and sufficient funds.</p>": "<p>A Grécia segue regras Schengen. Solicitações turísticas incluem prova de hospedagem e fundos suficientes.</p>",
        "<p>Switzerland is part of Schengen. Apply for short-stay visas via the Swiss embassy or VFS Global in your country.</p>": "<p>A Suíça faz parte do Schengen. Solicite vistos de curta duração na embaixada suíça ou VFS Global no seu país.</p>",
        "<p>Austrian Schengen visas require appointment booking and full document submission at the consulate.</p>": "<p>Vistos Schengen austríacos exigem agendamento e entrega completa de documentos no consulado.</p>",
        "<p>Croatia now aligns with Schengen rules. Check if you need a national visa or if Schengen visa applies.</p>": "<p>A Croácia segue as regras Schengen. Verifique se precisa de visto nacional ou se o visto Schengen se aplica.</p>",
        "<p>Czech Schengen visa applications require standard documents and a consulate appointment. Processing 10–15 days.</p>": "<p>Vistos Schengen tchecos exigem documentos padrão e consulado agendado. Processamento 10–15 dias.</p>",
        "<p>Poland issues Schengen visas for short stays (90 days). Follow local consulate requirements and book in advance.</p>": "<p>A Polônia emite vistos Schengen (90 dias). Siga os requisitos do consulado local e agende com antecedência.</p>",
        "<p>Hungary processes Schengen visas through its consulates. Prepare required documents and allow 10–15 days processing.</p>": "<p>A Hungria processa vistos Schengen nos consulados. Prepare documentos e aguarde 10–15 dias de processamento.</p>",
        "<p>Sweden requires Schengen visas for many nationalities. Check the Swedish consulate or VFS Global in your country.</p>": "<p>A Suécia exige visto Schengen para muitas nacionalidades. Consulte o consulado sueco ou VFS Global no seu país.</p>",
        "<p>Norway applies Schengen rules. Provide proof of travel plans, accommodation, travel insurance and sufficient funds.</p>": "<p>A Noruega aplica regras Schengen. Forneça prova de itinerário, hospedagem, seguro viagem e fundos suficientes.</p>",
        "<p>Denmark requires Schengen visas for eligible travellers. Check specific embassy requirements for your nationality.</p>": "<p>A Dinamarca exige visto Schengen para viajantes elegíveis. Verifique os requisitos específicos para sua nacionalidade.</p>",
        "<p>Ireland has its own visitor visa rules outside Schengen. Check Irish Immigration Service for your nationality requirements.</p>": "<p>A Irlanda tem regras próprias fora de Schengen. Consulte o Serviço de Imigração Irlandês para sua nacionalidade.</p>",
        "<p>Romania has specific national visa rules. Now fully part of Schengen for air and sea travel since 2024.</p>": "<p>A Romênia tem regras específicas de visto. Membro pleno de Schengen para viagens aéreas e marítimas desde 2024.</p>",
        "<p>ESTA required for 40+ visa-waiver countries. Apply online at esta.cbp.dhs.gov. Valid 2 years, multiple trips.</p>": "<p>ESTA exigida para 40+ países isentos de visto. Solicite em esta.cbp.dhs.gov. Válida 2 anos, múltiplas viagens.</p>",
        "<p>Canada eTA required for visa-exempt nationals flying in. Apply online at ircc.canada.ca. Valid 5 years.</p>": "<p>AVE do Canadá exigida para nacionais isentos de visto que viajam de avião. Solicite em ircc.canada.ca. Válida 5 anos.</p>",
        "<p>Most nationalities enter Mexico visa-free for up to 180 days. FMM tourist card required on arrival (free at border).</p>": "<p>A maioria das nacionalidades entra no México sem visto (180 dias). Cartão FMM exigido na chegada (gratuito na fronteira).</p>",
        "<p>Brazil eVisa available online for many nationalities. US, Canadian and Australian citizens enter visa-free since 2024.</p>": "<p>eVisa do Brasil disponível online. Cidadãos dos EUA, Canadá e Austrália entram sem visto desde 2024.</p>",
        "<p>Most Western passport holders enter Argentina visa-free for 90 days. Reciprocity fee abolished since 2016.</p>": "<p>A maioria dos passaportes ocidentais entra na Argentina sem visto (90 dias). Taxa de reciprocidade abolida em 2016.</p>",
        "<p>Colombia: no visa required for most nationalities for stays up to 90 days, extendable to 180 days per year.</p>": "<p>Colômbia: sem visto para a maioria das nacionalidades até 90 dias, prorrogáveis a 180 dias por ano.</p>",
        "<p>Peru: visa-free for most nationalities for up to 183 days. Migration form required on arrival.</p>": "<p>Peru: sem visto para a maioria das nacionalidades até 183 dias. Formulário de migração exigido na chegada.</p>",
        "<p>Jordan visa on arrival at Amman airport for most nationalities (JOD 40). Jordan Pass includes the entry fee.</p>": "<p>Visto na chegada no aeroporto de Amã para a maioria (40 JOD). Jordan Pass inclui a taxa de entrada.</p>",
        "<p>Oman: 100+ nationalities enter visa-free for 14 days. eVisa available via MOI portal for others (up to 30 days).</p>": "<p>Omã: 100+ nacionalidades entram sem visto (14 dias). eVisa disponível via portal MOI para outras (30 dias).</p>",
        "<p>Australia: free eVisitor (651) for EU/UK/US. ETA (601) for other eligible nationals. Apply via ImmiAccount.</p>": "<p>Austrália: eVisitor gratuito (651) para UE/UK/US. ETA (601) para outros nacionais elegíveis. Solicite via ImmiAccount.</p>",
        "<p>New Zealand NZeTA required for visa-waiver nationals. Apply online via Immigration NZ app or website. NZD 23.</p>": "<p>NZeTA exigida para nacionais isentos de visto na Nova Zelândia. Solicite via app Immigration NZ. NZD 23.</p>",
        "<p>South Africa: most nationalities enter visa-free for 30–90 days. British nationals get 180 days. No eVisa currently.</p>": "<p>África do Sul: sem visto para a maioria (30–90 dias). Britânicos obtêm 180 dias. Sem eVisa atualmente.</p>",
        "<p>Taiwan: visa-free for 60+ nationalities (30–90 days). eVisa available for others via BOCA Taiwan portal.</p>": "<p>Taiwan: sem visto para 60+ nacionalidades (30–90 dias). eVisa disponível para outras via portal BOCA Taiwan.</p>",
    },
}

# First fix EN destination.html (complete truncated descriptions)
en_dest = os.path.join(WWW, "destination.html")
try:
    with open(en_dest, "r", encoding="utf-8") as f:
        html = f.read()
    for old, new in DESCS["en"].items():
        html = html.replace(old, new)
    with open(en_dest, "w", encoding="utf-8") as f:
        f.write(html)
    print("destination.html (EN root) fixed")
except Exception as e:
    print(f"ERR destination.html: {e}")

# Then fix EN subdir destination.html
en_dest2 = os.path.join(WWW, "en", "destination.html")
if os.path.exists(en_dest2):
    try:
        with open(en_dest2, "r", encoding="utf-8") as f:
            html = f.read()
        for old, new in DESCS["en"].items():
            html = html.replace(old, new)
        with open(en_dest2, "w", encoding="utf-8") as f:
            f.write(html)
        print("en/destination.html fixed")
    except Exception as e:
        print(f"ERR en/destination.html: {e}")

# Now apply to FR/ES/PT: first apply EN fixes, then translate
for lang in ["fr", "es", "pt"]:
    fpath = os.path.join(WWW, lang, "destination.html")
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        # First complete truncated EN versions
        for old, new in DESCS["en"].items():
            html = html.replace(old, new)
        # Then translate to target language
        for en_completed, translated in DEST_CARD_TRANS[lang].items():
            html = html.replace(en_completed, translated)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"{lang}/destination.html: descriptions translated")
    except Exception as e:
        print(f"ERR {lang}/destination.html: {e}")

print("\nDONE")
