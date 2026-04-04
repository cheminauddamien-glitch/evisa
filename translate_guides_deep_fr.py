#!/usr/bin/env python3
"""Deep translation of ALL remaining English content in FR expat guide pages."""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\fr"

# All English→French replacements (ordered from longest to shortest to avoid partial matches)
REPLACEMENTS = [
    # INTRO PARAGRAPHS (country-specific intros that were left in English)
    ("Thailand remains one of the world's most popular expat destinations, offering warm weather, affordable living, world-class cuisine and welcoming visa options for retirees, remote workers and families.",
     "La Thaïlande reste l'une des destinations les plus populaires au monde pour les expatriés, offrant un climat chaud, un coût de la vie abordable, une cuisine de renommée mondiale et des options de visa accueillantes pour les retraités, les travailleurs à distance et les familles."),

    # VISA TABLE CONTENT
    ("Requires proof of 800,000 THB in a Thai bank account OR 65,000 THB/month income. Valid 1 year, renewable. Allows multiple entries.",
     "Nécessite la preuve de 800 000 THB sur un compte bancaire thaïlandais OU 65 000 THB/mois de revenus. Valable 1 an, renouvelable. Entrées multiples."),
    ("Valid 10 years. Allows working for overseas employers without a Thai work permit. Fast-track immigration.",
     "Valable 10 ans. Permet de travailler pour des employeurs étrangers sans permis de travail thaïlandais. Immigration accélérée."),
    ("5–20 year stay, VIP airport service. No income requirement. Purely residence-based.",
     "Séjour de 5 à 20 ans, service VIP aéroport. Aucune condition de revenus. Purement résidentiel."),
    ("Must be accompanied by a Thai Work Permit. Annual renewal.",
     "Doit être accompagné d'un permis de travail thaïlandais. Renouvellement annuel."),
    ("60 days (Tourist) or 30 days (visa-exempt). Can extend once at immigration. Many expats use border runs — now strictly monitored.",
     "60 jours (touristique) ou 30 jours (exemption). Extension unique possible à l'immigration. Les sorties de territoire sont désormais strictement contrôlées."),

    # STEP-BY-STEP (partial translations)
    ("retirement, LTR, Elite or business", "retraite, LTR, Elite ou affaires"),
    ("passport (6+ months), photos, bank statements, health insurance, medical certificate",
     "passeport (6+ mois de validité), photos, relevés bancaires, assurance santé, certificat médical"),
    ("Thai embassy or consulate in your home country", "l'ambassade ou le consulat thaïlandais dans votre pays d'origine"),
    ("TM.30 address notification within 24 hours", "la notification d'adresse TM.30 dans les 24 heures"),
    ("required for retirement visa deposit", "requis pour le dépôt du visa retraite"),
    ("at the Immigration Bureau (online, by post or in person)", "au Bureau de l'Immigration (en ligne, par courrier ou en personne)"),
    ("at your local Immigration office", "à votre bureau local de l'Immigration"),

    # HEALTHCARE SECTION
    ("Thailand's public healthcare system (30-Baht Scheme) is available to Thai nationals and permanent residents only. As a non-resident expat, you cannot access public healthcare at subsidised rates.",
     "Le système de santé public thaïlandais (régime à 30 Bahts) est réservé aux ressortissants thaïlandais et aux résidents permanents. En tant qu'expatrié non-résident, vous ne pouvez pas accéder aux soins publics à tarif subventionné."),
    ("Private hospitals in Thailand (Bangkok Hospital, Bumrungrad, Samitivej) are world-class and significantly cheaper than Western equivalents. A consultation costs 500–1,500 THB (~$14–42). Major surgery is 60–80% cheaper than in the US or Europe.",
     "Les hôpitaux privés en Thaïlande (Bangkok Hospital, Bumrungrad, Samitivej) sont de classe mondiale et considérablement moins chers que leurs équivalents occidentaux. Une consultation coûte 500–1 500 THB (~14–42 $). La chirurgie majeure est 60–80 % moins chère qu'aux États-Unis ou en Europe."),
    ("Most visa types (including LTR and Retirement OA) require proof of health insurance with minimum 40,000 THB outpatient / 400,000 THB inpatient coverage.",
     "La plupart des types de visa (y compris LTR et Retraite OA) exigent une preuve d'assurance santé avec une couverture minimale de 40 000 THB en ambulatoire / 400 000 THB en hospitalisation."),

    # INSURANCE SECTION
    ("for retirement and LTR visas. Even on other visas, it is strongly recommended. Thai private hospitals can be expensive for major procedures, and repatriation costs without insurance can exceed $50,000.",
     "pour les visas de retraite et LTR. Même avec d'autres types de visa, elle est fortement recommandée. Les hôpitaux privés thaïlandais peuvent être coûteux pour les interventions majeures, et les frais de rapatriement sans assurance peuvent dépasser 50 000 $."),
    ("Local insurer specialising in expats in Southeast Asia. Plans from ~$800/year. Good network of Thai private hospitals.",
     "Assureur local spécialisé dans les expatriés en Asie du Sud-Est. Plans à partir de ~800 $/an. Bon réseau d'hôpitaux privés thaïlandais."),
    ("Strong regional network. Plans from ~$1,000/year. Well-regarded for cancer coverage.",
     "Solide réseau régional. Plans à partir de ~1 000 $/an. Reconnu pour la couverture cancer."),
    ("International coverage, ideal if you travel frequently or split time between countries. From ~$1,500/year.",
     "Couverture internationale, idéale si vous voyagez fréquemment ou partagez votre temps entre plusieurs pays. À partir de ~1 500 $/an."),
    ("Comprehensive plans with worldwide coverage. Particularly suited for high earners on LTR visas. From ~$1,800/year.",
     "Plans complets avec couverture mondiale. Particulièrement adapté aux hauts revenus avec visa LTR. À partir de ~1 800 $/an."),
    ("Flexible modular plans. Can add dental, optical and maternity. From ~$1,200/year.",
     "Plans modulaires flexibles. Possibilité d'ajouter dentaire, optique et maternité. À partir de ~1 200 $/an."),
    ("For the Retirement OA visa, your policy must be issued by a Thai-licensed insurer and must specifically state 40,000 / 400,000 THB minimum coverage. Pacific Cross and BUPA are the easiest to use for this purpose.",
     "Pour le visa Retraite OA, votre police doit être émise par un assureur agréé en Thaïlande et doit spécifiquement indiquer une couverture minimale de 40 000 / 400 000 THB. Pacific Cross et BUPA sont les plus faciles à utiliser à cet effet."),

    # BANK ACCOUNT SECTION
    ("it's required for the retirement visa deposit (800,000 THB), utility payments, rent transfers and daily transactions.",
     "il est requis pour le dépôt du visa retraite (800 000 THB), le paiement des factures, les virements de loyer et les transactions quotidiennes."),
    ("Most expat-friendly bank. English-language app and staff in main branches. Fixed deposit accounts accepted for visa purposes.",
     "Banque la plus accueillante pour les expatriés. Application et personnel anglophones dans les agences principales. Comptes à terme acceptés pour les formalités de visa."),
    ("Largest bank in Thailand. Strong international wire support. Commonly used for pension/income transfers.",
     "Plus grande banque de Thaïlande. Excellent support pour les virements internationaux. Couramment utilisée pour les transferts de pension/revenus."),
    ("Good English-language online banking. Competitive FX rates.",
     "Bonne banque en ligne anglophone. Taux de change compétitifs."),
    ("Easier account opening in some provinces. Partners with Mitsubishi UFJ.",
     "Ouverture de compte plus facile dans certaines provinces. Partenaire de Mitsubishi UFJ."),
    ("online opening not available for foreigners", "ouverture en ligne non disponible pour les étrangers"),
    ("to the bank officer", "à l'agent bancaire"),
    ("same day or within 5 business days", "le jour même ou dans les 5 jours ouvrables"),
    ("may require Thai phone number", "peut nécessiter un numéro de téléphone thaïlandais"),

    # REAL ESTATE SECTION
    ("Foreigners cannot own land in Thailand, but they can own condominium units freehold (up to 49% of a building's total floor area may be foreign-owned). Houses and land must be held through a Thai company, a 30-year leasehold or a Thai spouse.",
     "Les étrangers ne peuvent pas posséder de terrain en Thaïlande, mais ils peuvent posséder des appartements en copropriété en pleine propriété (jusqu'à 49 % de la superficie totale d'un immeuble peut être détenue par des étrangers). Les maisons et terrains doivent être détenus via une société thaïlandaise, un bail de 30 ans ou un conjoint thaïlandais."),
    ("Full ownership permitted for foreigners. Must be paid from overseas in foreign currency (proof required). Most popular option.",
     "Pleine propriété autorisée pour les étrangers. Paiement obligatoire depuis l'étranger en devise étrangère (justificatif requis). Option la plus populaire."),
    ("for 30 years, renewable twice (total 90 years in practice). Common for villas and townhouses.",
     "pour 30 ans, renouvelable deux fois (90 ans en pratique). Courant pour les villas et maisons de ville."),
    ("A Thai limited company (min. 51% Thai shareholders) can hold land. Complex, legal fees $2,000–5,000. Requires ongoing compliance.",
     "Une société thaïlandaise à responsabilité limitée (min. 51 % d'actionnaires thaïlandais) peut détenir des terrains. Complexe, frais juridiques 2 000–5 000 $. Nécessite une conformité continue."),
    ("a Thai spouse's name. No legal protection in case of divorce. Not recommended.",
     "un conjoint thaïlandais. Aucune protection juridique en cas de divorce. Non recommandé."),

    # PURCHASE PROCESS
    ("Hire a reputable real estate lawyer (budget 30,000–80,000 THB)",
     "Engagez un avocat immobilier réputé (budget 30 000–80 000 THB)"),
    ("Verify the title deed (Chanote / Nor Sor 4 — the only fully secure title)",
     "Vérifiez le titre de propriété (Chanote / Nor Sor 4 — le seul titre pleinement sécurisé)"),
    ("Sign a Reservation Agreement and pay deposit (50,000–100,000 THB)",
     "Signez un contrat de réservation et payez l'acompte (50 000–100 000 THB)"),
    ("Due diligence: check no liens, correct zoning, building permits",
     "Vérifications préalables : absence de charges, zonage correct, permis de construire"),
    ("Transfer funds from overseas bank to Thailand (keep FET form for proof)",
     "Transférez les fonds depuis une banque étrangère vers la Thaïlande (conservez le formulaire FET comme justificatif)"),
    ("Sign Sale & Purchase Agreement (SPA)",
     "Signez le contrat de vente (SPA)"),
    ("Transfer at the Land Office — both parties must attend",
     "Transfert au Bureau foncier — les deux parties doivent être présentes"),
    ("Pay transfer fees (typically 2–3% of assessed value)",
     "Payez les frais de transfert (généralement 2–3 % de la valeur estimée)"),

    # COST TABLE
    ("Transfer fee", "Frais de transfert"),
    ("Stamp duty or specific business tax", "Droit de timbre ou taxe commerciale spécifique"),
    ("Withholding tax", "Retenue à la source"),
    ("Lawyer fees", "Frais d'avocat"),
    ("Agent commission", "Commission d'agent"),
    ("2% of the appraised value (split buyer/seller)", "2 % de la valeur estimée (partagé acheteur/vendeur)"),
    ("0.5% stamp duty OR 3.3% SBT if sold within 5 years", "0,5 % droit de timbre OU 3,3 % SBT si vendu dans les 5 ans"),
    ("1–3% (paid by seller)", "1–3 % (payé par le vendeur)"),
    ("3–5% (paid by seller)", "3–5 % (payé par le vendeur)"),

    # PRO TIPS
    ("Always use a Chanote (NS4J) title deed. Avoid Nor Sor 3 or Sor Kor 1 titles — they offer less legal protection and cannot be mortgaged.",
     "Utilisez toujours un titre Chanote (NS4J). Évitez les titres Nor Sor 3 ou Sor Kor 1 — ils offrent moins de protection juridique et ne peuvent pas être hypothéqués."),
    ("The LTR Visa is the best option for remote workers — 10 years, no 90-day reports, and it exempts certain income from Thai tax.",
     "Le visa LTR est la meilleure option pour les travailleurs à distance — 10 ans, pas de signalement tous les 90 jours, et il exonère certains revenus de l'impôt thaïlandais."),
    ("Kasikorn Bank's Asoke (Bangkok) or Nimman (Chiang Mai) branches are known for being particularly helpful to expats. Arrive early — queues can be long.",
     "Les agences Kasikorn Bank d'Asoke (Bangkok) ou Nimman (Chiang Mai) sont réputées pour être particulièrement accueillantes envers les expatriés. Arrivez tôt — les files d'attente peuvent être longues."),

    # E-E-A-T SECTION
    ("We strive to keep all information current but visa rules, healthcare costs and property regulations change frequently. Always verify current requirements with official government sources and consult a licensed professional before making major decisions.",
     "Nous nous efforçons de maintenir toutes les informations à jour, mais les règles de visa, les coûts de santé et les réglementations immobilières changent fréquemment. Vérifiez toujours les exigences actuelles auprès des sources gouvernementales officielles et consultez un professionnel agréé avant de prendre des décisions importantes."),
    ("This guide is researched and maintained by the editorial team at eVisa-Card.com.",
     "Ce guide est recherché et maintenu par l'équipe éditoriale d'eVisa-Card.com."),

    # GENERIC COMMON PATTERNS (apply across all country guides)
    ("Valid passport", "Passeport valide"),
    ("Proof of address in Thailand (rental contract or TM.30 confirmation)",
     "Justificatif de domicile en Thaïlande (contrat de location ou confirmation TM.30)"),
    ("Thai SIM card or phone number", "Carte SIM ou numéro de téléphone thaïlandais"),
    ("Initial deposit (typically 500–2,000 THB)", "Dépôt initial (généralement 500–2 000 THB)"),
    ("Non-Immigrant visa (tourist visa may be refused at some branches)",
     "Visa Non-Immigrant (le visa touristique peut être refusé dans certaines agences)"),
    ("GP consultation (private)", "Consultation médecin généraliste (privé)"),
    ("Specialist consultation", "Consultation spécialiste"),
    ("Emergency room visit", "Visite aux urgences"),
    ("Hospitalisation (per night)", "Hospitalisation (par nuit)"),
    ("Dental cleaning", "Détartrage dentaire"),
    ("Eye exam + glasses", "Examen oculaire + lunettes"),

    # FOOTER / MISC
    ("Global eVisa & Travel Information Platform", "Plateforme mondiale d'information eVisa et voyages"),
    ("Follow eVisa-Card.com", "Suivez eVisa-Card.com"),
    ("March 2026", "Mars 2026"),
]

def main():
    total_replacements = 0
    files_updated = 0

    for fname in sorted(os.listdir(BASE)):
        if not fname.startswith("expat-guide-") or not fname.endswith(".html"):
            continue

        fpath = os.path.join(BASE, fname)
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()

        original = html
        file_replacements = 0

        for eng, fra in REPLACEMENTS:
            count = html.count(eng)
            if count > 0:
                html = html.replace(eng, fra)
                file_replacements += count

        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            files_updated += 1
            total_replacements += file_replacements
            print(f"  OK {fname}: {file_replacements} replacements")

    print(f"\nDone: {files_updated} files, {total_replacements} total replacements.")

if __name__ == "__main__":
    main()
