#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Final fix script for remaining English text and corrupted words in FR guides.
"""
import os
import re
import glob

FR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "fr")
PATTERN = os.path.join(FR_DIR, "expat-guide-*.html")

# Fix remaining corrupted words from substring damage
CORRUPTION_FIXES = [
    ("tetis que", "tandis que"),
    ("Metatouy", "Mandatory"),
    ("metatouy", "mandatory"),
    ("straightfouward", "straightforward"),
    ("Straightfouward", "Straightforward"),
    ("significativement.", "considérablement."),
    ("Untitled let.", "Terrain sans titre."),
    ("Untitled let ", "Terrain sans titre "),
    ("Let can be leased", "Land can be leased"),  # Will be translated below
    # Fix remaining instances of damaged words
]

# Remaining English text -> French translations
FINAL_TRANSLATIONS = [
    # --- Remaining sentences/phrases found across files ---

    # Cambodia
    ("No specific retirement visa, but those 55+ can apply for a 1-year 'retirement' extension of their ordinary visa.",
     "Pas de visa retraite spécifique, mais les personnes de 55 ans et plus peuvent demander une extension de 1 an de leur visa ordinaire pour « retraite »."),
    ("Requires proof of $1,500/month income or $50,000 in bank.",
     "Nécessite une preuve de revenus de 1 500 $/mois ou 50 000 $ en banque."),
    ("Dépôt initial ($100–500 for most account types)", "Dépôt initial (100–500 $ pour la plupart des types de comptes)"),
    ("Dépôt initial ($100-500 for most account types)", "Dépôt initial (100-500 $ pour la plupart des types de comptes)"),

    # Colombia
    ("Start with Nequi or Nu Colombia (fully digital, instant account) while waiting for your Cédula. Once you have your Cédula, open a Bancolombia account for more complete banking services.",
     "Commencez avec Nequi ou Nu Colombia (entièrement numérique, compte instantané) en attendant votre Cédula. Une fois que vous avez votre Cédula, ouvrez un compte Bancolombia pour des services bancaires plus complets."),
    ("Start with Nequi or Nu Colombia (fully digital, instant account) tandis que waiting for your Cédula. Once you have your Cédula, ouvrez un Bancolombia account for more complete banking services.",
     "Commencez avec Nequi ou Nu Colombia (entièrement numérique, compte instantané) en attendant votre Cédula. Une fois que vous avez votre Cédula, ouvrez un compte Bancolombia pour des services bancaires plus complets."),

    # Costa Rica
    ("State insurer. Mandatory for car insurance; also offers health plans.",
     "Assureur d'État. Obligatoire pour l'assurance auto ; offre également des plans santé."),
    ("Combine mandatory CAJA (~$100/month) with a private complementary plan ($100–150/month) for the best of both worlds — comprehensive public coverage plus fast-track private access for specialist care.",
     "Combinez la CAJA obligatoire (~100 $/mois) avec un plan privé complémentaire (100-150 $/mois) pour le meilleur des deux mondes — couverture publique complète plus accès privé rapide pour les soins spécialisés."),
    ("Combine obligatoire CAJA (~$100/mois) with a private complémentaire plan ($100–150/mois) for the best of both worlds — comprehensive public coverage plus fast-track private access for soins spécialisés.",
     "Combinez la CAJA obligatoire (~100 $/mois) avec un plan privé complémentaire (100-150 $/mois) pour le meilleur des deux mondes — couverture publique complète plus accès privé rapide pour les soins spécialisés."),
    ("Untitled land. Very risky for foreigners — avoid unless you have expert legal advice.",
     "Terrain sans titre. Très risqué pour les étrangers — à éviter sauf si vous avez des conseils juridiques d'expert."),
    ("Crypto gains from foreign platforms are tax-free", "Les plus-values crypto provenant de plateformes étrangères sont exonérées d'impôt"),
    ("Crypto gains from foreign exchanges are tax-free", "Les plus-values crypto provenant de plateformes étrangères sont exonérées d'impôt"),

    # Georgia
    ("For residency: apply at the Civil Registry Agency with investment proof",
     "Pour la résidence : faites votre demande à l'Agence du Registre Civil avec preuve d'investissement"),
    ("Emergency (private hospital)", "Urgences (hôpital privé)"),
    ("Health insurance is not required for visa-free stays in Georgia. However, it is strongly recommended given the limitations of the public health system and the need for medical evacuation coverage.",
     "L'assurance santé n'est pas requise pour les séjours sans visa en Géorgie. Cependant, elle est fortement recommandée compte tenu des limites du système de santé public et du besoin de couverture d'évacuation médicale."),
    ("Assurance santé n'est pas requise for visa-free stays in Georgia. Cependant, it est fortement recommended given the limitations of the public health system et the need for évacuation médicale coverage",
     "L'assurance santé n'est pas requise pour les séjours sans visa en Géorgie. Cependant, elle est fortement recommandée compte tenu des limites du système de santé public et du besoin de couverture d'évacuation médicale"),
    ("Not Georgian banks but widely used for international transfers. Complement your local TBC or Bank of Georgia account.",
     "Pas des banques géorgiennes mais largement utilisées pour les transferts internationaux. Complétez votre compte local TBC ou Bank of Georgia."),
    ("Not Georgian banks but largement utilisé for transferts internationaux. Complement your local TBC or Bank of Georgia account.",
     "Pas des banques géorgiennes mais largement utilisées pour les transferts internationaux. Complétez votre compte local TBC ou Bank of Georgia."),
    ("Visit any TBC Bank or Bank of Georgia branch",
     "Rendez-vous dans n'importe quelle agence TBC Bank ou Bank of Georgia"),
    ("No lawyer strictly required (system is very simple) but highly recommended for foreigners",
     "Pas d'avocat strictement requis (le système est très simple) mais fortement recommandé pour les étrangers"),
    ("No lawyer strictly required (system is very simple) but highly recommend",
     "Pas d'avocat strictement requis (le système est très simple) mais fortement recommandé"),

    # Greece
    ("Open a Greek bank account (required for most visa types)",
     "Ouvrez un compte bancaire grec (requis pour la plupart des types de visa)"),
    ("Ouvrez un Greek bank account (requis pour most visa types)",
     "Ouvrez un compte bancaire grec (requis pour la plupart des types de visa)"),
    ("Apply for the appropriate visa at your local Greek consulate",
     "Postulez pour le visa approprié à votre consulat grec local"),
    ("Postulez pour the appropriate visa at your local Greek consulate",
     "Postulez pour le visa approprié à votre consulat grec local"),

    # Japan
    ("Apply for the visa at the Japanese embassy in your country using the CoE",
     "Postulez pour le visa à l'ambassade du Japon dans votre pays en utilisant le CoE"),
    ("Postulez pour the visa at the Japanese embassy in your country using the CoE",
     "Postulez pour le visa à l'ambassade du Japon dans votre pays en utilisant le CoE"),
    ("A Japanese bank account is essential for receiving salary, paying rent, utilities and taxes. It has historically been difficult for new arrivals, but the process has improved significantly.",
     "Un compte bancaire japonais est indispensable pour recevoir son salaire, payer le loyer, les services publics et les impôts. Cela a historiquement été difficile pour les nouveaux arrivants, mais le processus s'est considérablement amélioré."),
    ("A Japanese bank account est indispensable for receiving salary, paying rent, utilities et taxes. It has historically been difficult for new arrivals, but the process has improved",
     "Un compte bancaire japonais est indispensable pour recevoir son salaire, payer le loyer, les services publics et les impôts. Cela a historiquement été difficile pour les nouveaux arrivants, mais le processus s'est considérablement amélioré"),

    # Laos
    ("Land can be leased to foreigners for up to 50 years, renewable. This is the main option for property use. Common for villas, guesthouses and commercial properties.",
     "Les terrains peuvent être loués aux étrangers pour une durée allant jusqu'à 50 ans, renouvelable. C'est l'option principale pour l'usage de la propriété. Courant pour les villas, maisons d'hôtes et propriétés commerciales."),
    ("Hire a Lao lawyer familiar with foreign investment law",
     "Engagez un avocat laotien familier du droit des investissements étrangers"),

    # Malaysia
    ("Strong private hospital network. International coverage option available.",
     "Solide réseau d'hôpitaux privés. Option de couverture internationale disponible."),
    ("A Malaysian bank account is needed for the MM2H fixed deposit requirement and for daily expenses. The process is straightforward for visa holders.",
     "Un compte bancaire malaisien est nécessaire pour l'exigence de dépôt fixe MM2H et pour les dépenses quotidiennes. Le processus est simple pour les titulaires de visa."),
    ("Territorial tax system: foreign income not taxed",
     "Système fiscal territorial : revenus étrangers non imposés"),

    # Mexico
    ("Via Temporary or Permanent Resident route with pension income proof. No special retiree visa category exists but income threshold is achievable with most pensions.",
     "Via la voie du Résident Temporaire ou Permanent avec preuve de revenus de pension. Pas de catégorie de visa retraité spécifique mais le seuil de revenus est atteignable avec la plupart des pensions."),
    ("Apply at the Mexican consulate in your home country with income/savings proof",
     "Postulez au consulat mexicain dans votre pays d'origine avec une preuve de revenus/épargne"),
    ("Postulez à the Mexican consulate in your home country with income/savings proof",
     "Postulez au consulat mexicain dans votre pays d'origine avec une preuve de revenus/épargne"),
    ("Most expats opt for private international health insurance rather than IMSS. IMSS is a good supplement for routine care, but private insurance is essential for hospitalisation.",
     "La plupart des expatriés optent pour une assurance santé internationale privée plutôt que l'IMSS. L'IMSS est un bon complément pour les soins courants, mais l'assurance privée est indispensable pour l'hospitalisation."),
    ("Most expats opt for private international assurance santé rather than IMSS. IMSS is a good supplement for soins courants, but private insurance est indispensable for hospitalisation.",
     "La plupart des expatriés optent pour une assurance santé internationale privée plutôt que l'IMSS. L'IMSS est un bon complément pour les soins courants, mais l'assurance privée est indispensable pour l'hospitalisation."),
    ("If you plan to visit the US for medical care, make sure your plan includes US coverage — this generally doubles the premium but is essential for serious conditions.",
     "Si vous prévoyez de vous rendre aux États-Unis pour des soins médicaux, assurez-vous que votre plan inclut la couverture américaine — cela double généralement la prime mais est indispensable pour les conditions graves."),
    ("this généralement doubles the premium but est indispensable for serious conditions.",
     "cela double généralement la prime mais est indispensable pour les conditions graves."),
    ("Best option for international transfers, particularly to/from Europe and Asia.",
     "Meilleure option pour les transferts internationaux, particulièrement vers/depuis l'Europe et l'Asie."),
    ("Best option for transferts internationaux, particulièrement to/from Europe et Asia.",
     "Meilleure option pour les transferts internationaux, particulièrement vers/depuis l'Europe et l'Asie."),
    ("Mexico doesn't have a specific DNV but Temporary Resident with income proof from abroad is widely used. Many nomads also use tourist entry (180 days) repeatedly.",
     "Le Mexique n'a pas de visa nomade numérique spécifique mais le statut de Résident Temporaire avec preuve de revenus de l'étranger est largement utilisé. Beaucoup de nomades utilisent également l'entrée touristique (180 jours) de manière répétée."),
    ("Obtain RFC at the SAT office or via the SAT website",
     "Obtenez votre RFC au bureau du SAT ou via le site web du SAT"),

    # Paraguay
    ("Open a Paraguayan bank account and make the $5,500 deposit",
     "Ouvrez un compte bancaire paraguayen et effectuez le dépôt de 5 500 $"),
    ("Ouvrez un Paraguayan bank account et make the $5,500 deposit",
     "Ouvrez un compte bancaire paraguayen et effectuez le dépôt de 5 500 $"),
    ("Receive account number and access for wire transfers",
     "Recevez votre numéro de compte et l'accès pour les virements"),
    ("Receive account number et access for wire transfers",
     "Recevez votre numéro de compte et l'accès pour les virements"),
    ("Full ownership. No restrictions for foreigners. Standard for all property types.",
     "Pleine propriété. Aucune restriction pour les étrangers. Standard pour tous les types de biens."),

    # Portugal
    ("Open a Portuguese bank account (required for visa purposes)",
     "Ouvrez un compte bancaire portugais (requis pour les demandes de visa)"),
    ("Ouvrez un Portuguese bank account (requis pour visa purposes)",
     "Ouvrez un compte bancaire portugais (requis pour les demandes de visa)"),
    ("Register at your local health centre (Centro de Saúde) within the first months to get a SNS user number.",
     "Inscrivez-vous à votre centre de santé local (Centro de Saúde) dans les premiers mois pour obtenir un numéro d'utilisateur SNS."),
    ("within the first months", "dans les premiers mois"),

    # Spain
    ("Apply for your visa at the Spanish consulate in your country",
     "Postulez pour votre visa au consulat d'Espagne dans votre pays"),
    ("Postulez pour your visa at the Spanish consulate in your country",
     "Postulez pour votre visa au consulat d'Espagne dans votre pays"),
    ("The Non-Lucrative Visa requires you NOT to work in Spain, but you can receive income from foreign sources (pensions, investments, remote work for non-Spanish companies if done discreetly — grey area). The Digital Nomad Visa is cleaner if you're working remotely.",
     "Le visa Non Lucratif vous interdit de travailler en Espagne, mais vous pouvez recevoir des revenus de sources étrangères (pensions, investissements, travail à distance pour des entreprises non espagnoles si fait discrètement — zone grise). Le visa Nomade Numérique est plus clair si vous travaillez à distance."),
    ("The Non-Lucrative Visa nécessite you NOT to work in Spain, but you can receive income from foreign sources (pensions, investments, remote work for non-Spanish companies if done discreetly",
     "Le visa Non Lucratif vous interdit de travailler en Espagne, mais vous pouvez recevoir des revenus de sources étrangères (pensions, investissements, travail à distance pour des entreprises non espagnoles si fait discrètement"),
    ("The Digital Nomad Visa is cleaner if you're working remotely.", "Le visa Nomade Numérique est plus clair si vous travaillez à distance."),
    ("grey area).", "zone grise)."),
    ("For NLV applicants: private health insurance with at least", "Pour les candidats au NLV : une assurance santé privée d'au moins"),
    ("For NLV applicants: private assurance santé with at least", "Pour les candidats au NLV : une assurance santé privée d'au moins"),
    ("coverage is required for the visa. Even after obtaining residency, many expats keep private insurance for faster service.",
     "de couverture est requise pour le visa. Même après l'obtention de la résidence, de nombreux expatriés conservent une assurance privée pour un service plus rapide."),
    ("coverage est requis(e) for the visa. Even après obtaining residency, many expats keep private insurance for faster service.",
     "de couverture est requise pour le visa. Même après l'obtention de la résidence, de nombreux expatriés conservent une assurance privée pour un service plus rapide."),
    ("Register on the Padrón at your Town Hall", "Inscrivez-vous au Padrón à votre mairie"),
    ("Register property at the Property Registry (Registro de la Propiedad)",
     "Enregistrez le bien au Registre de la Propriété (Registro de la Propiedad)"),
    ("Major bank, strong digital platform. Easy account opening with NIE.",
     "Grande banque, solide plateforme numérique. Ouverture de compte facile avec NIE."),

    # UAE
    ("Regional leader. Strong hospital network.", "Leader régional. Solide réseau hospitalier."),
    ("Book appointment at the bank or apply digitally", "Prenez rendez-vous à la banque ou postulez en ligne"),
    ("Prenez rendez-vous at the bank or apply digitally", "Prenez rendez-vous à la banque ou postulez en ligne"),
    ("Golden Visa: 10-year residency with property or investment",
     "Golden Visa : résidence de 10 ans avec propriété ou investissement"),

    # Vietnam
    ("Public hospitals in Vietnam are overcrowded and language-challenged. Expats generally avoid them for all but emergencies. Foreigners registered with a Vietnamese employer can access the public health insurance system.",
     "Les hôpitaux publics au Vietnam sont surpeuplés et présentent des difficultés linguistiques. Les expatriés les évitent généralement sauf pour les urgences. Les étrangers inscrits auprès d'un employeur vietnamien peuvent accéder au système d'assurance santé publique."),
    ("Public hospitals in Vietnam are overcrowded et language-challenged. Expats généralement avoid them for all but emergencies. Foreigners registered with a Vietnamese employer can access the public assur",
     "Les hôpitaux publics au Vietnam sont surpeuplés et présentent des difficultés linguistiques. Les expatriés les évitent généralement sauf pour les urgences. Les étrangers inscrits auprès d'un employeur vietnamien peuvent accéder au système d'assur"),
    ("Income tax up to 35% could theoretically apply", "L'impôt sur le revenu jusqu'à 35 % pourrait théoriquement s'appliquer"),

    # Generic cleanup
    ("requis pour most visa types", "requis pour la plupart des types de visa"),
    ("requis pour visa purposes", "requis pour les demandes de visa"),
    ("at your Town Hall", "à votre mairie"),
    ("for visa purposes", "pour les demandes de visa"),
]


def process_file(filepath):
    fname = os.path.basename(filepath)
    print(f"Final fix: {fname}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    main_start = content.find('<section class="ftco-section">')
    footer_start = content.find('<footer')
    if main_start < 0:
        print("  WARNING: No ftco-section found")
        return 0
    if footer_start < 0:
        footer_start = len(content)

    head = content[:main_start]
    body = content[main_start:footer_start]
    tail = content[footer_start:]

    changes = 0

    # Fix corrupted words
    for wrong, right in CORRUPTION_FIXES:
        if wrong in body:
            body = body.replace(wrong, right)
            changes += 1

    # Apply translations
    for eng, fra in FINAL_TRANSLATIONS:
        if eng in body:
            body = body.replace(eng, fra)
            changes += 1

    result = head + body + tail

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"  -> {changes} fixes applied")
    return changes


def main():
    files = sorted(glob.glob(PATTERN))
    print(f"Final fixes for {len(files)} files...")
    total = 0
    for f in files:
        total += process_file(f)
    print(f"\nDone. Total fixes: {total}")


if __name__ == '__main__':
    main()
