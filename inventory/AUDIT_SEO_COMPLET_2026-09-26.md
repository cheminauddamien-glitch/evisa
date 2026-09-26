# Audit SEO complet — evisa-card.com — 26 septembre 2026

Sources : Search Console (compte connecté, données au 21-23/09), scan local d'une passe sur les 10 954 pages de `www2/`, tests HTTP en ligne, recherche concurrentielle (SERP US, lecture directe des pages concurrentes). Pas d'outil Ahrefs/Semrush connecté : volumes et difficultés sont estimés d'après la composition réelle des SERP. Détails bruts : `scratchpad/audit/technique.md`, `marche.md`, `pages.csv` (10 954 lignes).

---

## 1. Résumé exécutif

Le site est techniquement propre (0 title dupliqué, 0 H1 manquant, 0 lien cassé, sitemap = disque, canonicals et 301 corrects) et **quasi invisible** : 15 clics et 2 640 impressions sur 28 jours, position moyenne 51,8, contre 7 320 clics / 2 M d'impressions / position 14,7 sur 16 mois. Le problème n'est pas l'hygiène, c'est le modèle : **78 % du site (8 573 pages « citizens ») ne porte que 37 mots uniques par page** ; les pages sœurs d'une même destination sont identiques à 89 % au nom de nationalité près. Google l'a tranché page par page : « autre canonique » (3 516) + « explorée, non indexée » (5 064) = 8 580, soit exactement le volume de la matrice citizens.

Le déploiement de consolidation du 11-13 septembre a en outre **divisé l'index par deux** (15 k → 8,7 k pages indexées) : au-delà des 3 528 redirections voulues, ~3 000 pages supplémentaires ont été recrawlées et rejetées, et le site est resté incohérent (16 797 liens internes vers des 301, 652 traductions conservées sans original anglais, 387 hubs orphelins).

Point fort : les hubs `visa-<pays>` (1 544 mots, 67 % de contenu unique) et les guides expat (2 257 mots, 94 % unique) sont de vraies pages — mais 37 % des hubs n'ont **aucun lien entrant** et les guides n'en ont que 4.

**Trois priorités** : (1) décider du sort de la matrice citizens par cluster complet (réduire ou enrichir, pas laisser en l'état) ; (2) réparer l'architecture post-consolidation (Related blocks, hubs orphelins, x-default) ; (3) créer les signaux de valeur originale que les concurrents qui rankent possèdent (actualité datée, sources liées, auteur, outils).

Verdict : **problèmes critiques**, d'ordre éditorial et architectural, pas technique.

---

## 2. Données Search Console

| Indicateur | 16 mois | 28 derniers jours |
|---|---|---|
| Clics | 7 320 | **15** |
| Impressions | 2 M | 2 640 |
| CTR | 0,4 % | 0,6 % |
| Position moyenne | 14,7 | **51,8** |

Pays (16 mois) : France 626 clics, États-Unis 518 (556 k impressions), UK 362, Nigéria 326, Japon 323, Canada 315, Corée 275. Sur 28 jours : Nigéria 3 clics, Thaïlande 2, le reste ≤ 1.

Pages historiquement performantes (16 mois) : `en/malaysia-visa-for-nigerian-citizens` 83, `en/cambodia-visa-extension` 48, `en/belgium-visa-processing-time` 47, `en/romania-visa-for-nigerian-citizens` 45, `en/visa-jordan` 42, `en/colombia-visa-for-nigerian-citizens` 41, `en/malaysia-visa-extension` 39, `en/sri-lanka-visa-extension` 39, `en/china-visa-for-nigerian-citizens` 36, `en/visa-turkey` 35. Requêtes : « frro visa extension fees » 13, « do south africans need a visa for taiwan » 6, « sri lanka visa extension fee » 6, « visa fee to vietnam » 5 (669 imp.), « malaysia visa extension » 4. **Ce qui rankait = pages extension/processing-time + citizens nigérians/sud-africains**, pas la masse.

Indexation (21/09) : 8 720 indexées, 13 000 non indexées. Sitemap : 10 940 URL, statut OK, lu le 22/09.

| Motif | Pages | Lecture |
|---|---|---|
| Explorée, actuellement non indexée | 5 064 | Passé de ~2 k à 5 k entre le 13 et le 15/09. Exemples : citizens dans toutes les langues + `ko/singapore-visa-requirements`. Verdict qualité. |
| Page en double, canonique choisie par Google | 3 516 | Citizens et fees. Google fusionne les sœurs. |
| Page avec redirection | 3 528 | Attendu (lots B/C1). |
| Autre page avec canonique correcte | 406 | Attendu. |
| Détectée, non indexée | 260 | File d'attente. |
| Exclue par noindex | 249 | **Artefact** : exemples crawlés en juin (avant migration), aujourd'hui `index, follow` en ligne. Seules les 10 `visa-result` + 404 sont noindex. Rien à faire. |
| Erreur de redirection | 1 | À identifier (export GSC). |

Core Web Vitals : pas assez de données (trafic trop faible). PageSpeed API : quota du jour épuisé, à relancer demain.

Vérifications en ligne : `.html` → 301 vers URL sans extension, canonicals corrects, `/en/` → `/`, `/visa-france` → `/en/visa-france`, `/en/visa-uk` → `/en/visa-united-kingdom`, `/fr/disclaimer` → `/fr/mentions-legales`, `/visa/india/` → `/en/visa-india`. **Toutes les règles `.htaccess` avec `/?` fonctionnent** — la note projet du 09/09 disant le contraire est fausse. Corrections Thaïlande du 21/09 bien servies.

Backlinks : aucune mention du domaine trouvée en recherche (`"evisa-card.com"` ne remonte que le site lui-même). Profil de liens quasi nul.

---

## 3. Duplication et contenu (cause racine)

### 3.1 Inventaire (www2, 10 954 pages)
citizens **8 573 (78 %)**, hubs 1 060, extension 480, expat-guide 330, autres 186, evisa 100, processing-time 90, requirements 77, fees 48, index 10. Après lots B/C1, `en` garde 824 citizens mais `ja` 897, `ko` 889, `zh`/`ar` 885 : **les langues sans trafic ont conservé plus de pages programmatiques que l'anglais.**

### 3.2 Mesure de similarité (Jaccard, shingles 8 mots)

| Citizens, sœurs d'une même destination | en (7 306 paires) | fr |
|---|---|---|
| Médiane | 0,158 | 0,158 |
| p90 | 0,805 | 0,800 |
| Paires > 80 % identiques | **11,4 %** | 9,8 % |
| Paires > 50 % | 37,1 % | 34,1 % |

`en/sweden-visa-for-south-african-citizens` vs `-turkish-` : 0,89, seules différences = 10 occurrences du gentilé + URLs JSON-LD. Même nationalité / destinations différentes : médiane 0,018 (pas de duplication inter-destination).

### 3.3 Contenu unique par gabarit (en)

| Gabarit | Pages | Mots | Mots uniques | Ratio |
|---|---|---|---|---|
| citizens | 824 | 358 | **37** | **0,08** |
| processing-time | 18 | 476 | 160 | 0,31 |
| extension | 48 | 525 | 323 | 0,50 |
| hub | 106 | 1 263 | 873 | 0,67 |
| requirements | 16 | 844 | 730 | 0,94 |
| expat-guide | 33 | 1 911 | 1 765 | 0,94 |
| evisa | 10 | 533 | 476 | 0,96 |

### 3.4 Thin content
1 851 pages < 300 mots (17 %) : ar 327, ru 313, zh 278, en 228, ko 177, pt 160, es 150, fr 146, ja 64 ; 1 808 sont des citizens. Pages légales zh/ru/ar/ja/ko/th quasi vides (6-23 mots) et indexables.

---

## 4. Problèmes on-page et architecture

| Page / périmètre | Problème | Sévérité | Correction |
|---|---|---|---|
| 8 573 citizens | 37 mots uniques, sœurs identiques à 89 % | **Critique** | Voir plan §8 : réduire par cluster ou enrichir par nationalité |
| 9 116 pages (83 %) | < 5 liens entrants ; citizens = **exactement 1** entrant (le hub) | **Élevée** | Maillage transversal (sœurs, même nationalité, extension/evisa) |
| 387 hubs (37 %) | **0 lien entrant** (`en/visa-andorra`, `visa-saudi-arabia`, `visa-israel`, `visa-finland`, `visa-panama`…) : `destination.html` figé à 50 pays, footer 18 | **Élevée** | Lister les 106 hubs sur `destination` × 10 langues |
| 6 658 pages (61 %) | **16 797 liens internes vers des 301** (blocs Related vers fees/requirements/processing supprimés par lot B) | **Élevée** | Régénérer les blocs Related |
| 652 pages (ja 104, ko 97, zh 92, th 84…) | Traduction conservée, original EN supprimé → **x-default perdu** | **Élevée** | Décision par cluster : supprimer ou recréer l'EN |
| 1 172 pages | Clusters hreflang partiels (75 à 1 seule langue, ex. `en/argentina-visa-processing-time`) | Élevée | Idem |
| Footer 9 langues | `/en/privacy-policy` et `/en/terms-of-use` reçoivent **9 942 entrants** : le PageRank du châssis fuit vers 2 pages EN | Moyenne | Pages légales localisées + nofollow inutile, juste lier la bonne langue |
| 4 816 pages (44 %) | Titles > 65 car. (médiane fr 90, es 87, pt 79, en 73), suffixe « 2026 : Requirements, Cost & How to Apply » traduit | Moyenne | Raccourcir le suffixe par langue |
| 2 519 pages | Meta description > 160 car. | Moyenne | Idem |
| 81 pages (zh 49, th 10, ar 6, ko 6…) | Meta descriptions = débris de traduction (« 完整指南2026年3月更新. ») | Moyenne | Régénérer |
| 10 645 pages | FAQPage partout ; 1 376 questions réutilisées ; « What is ETIAS… » sur 60 pages/langue ; plus de rich result FAQ depuis 2023 | Moyenne | Retirer le FAQPage des citizens, garder sur hubs avec FAQ propres |
| 10 879 pages (99 %) | Aucune image de contenu ; 0 schéma `Organization` autonome ; breadcrumbs plats (Home › Destinations › page) | Moyenne | Organization + breadcrumb hub › citizens ; visuels sur hubs |
| 428 pages du 21/09 | Sitemap non régénéré (lastmod 03-07/09) | Moyenne | Régénérer, et scinder par gabarit pour lire GSC |
| Home | Meta « Updated August 2026 » | Faible | Date sincère ou retirer |
| 12 pages | Légales zh/ru/ar/ja/ko/th vides | Moyenne | Traduire ou noindex |
| 1 page | `th/visa-france` JSON-LD invalide | Faible | Corriger |
| `.html` consolidées | Chaîne 2 sauts (`.html` → sans ext → hub) | Faible | Règle directe |
| css/js | Assets Colorlib morts (`style.css` 292 Ko, `jquery` 262 Ko, `bootstrap` 157 Ko non référencés) ; héros JPEG 900 Ko | Faible | Supprimer / compresser |

Sain : titles uniques, H1, alt, `lang`/`dir`, viewport, robots.txt, canonicals www, sitemap sans 301/noindex.

---

## 5. Checklist technique

| Contrôle | Statut | Détail |
|---|---|---|
| HTTPS, www, canonicals | Pass | Cohérents sur 10 953 pages |
| robots.txt | Pass | Bloque seulement admin/tmp/logs ; Ahrefs/Semrush bloqués (choix assumé, empêche les outils tiers de mesurer les backlinks) |
| Sitemap | Warning | 10 940 URL = disque, 0 URL en 301, mais lastmod périmé pour 428 pages ; un seul fichier de 2,2 Mo |
| Redirections .htaccess | Pass | 27 règles, toutes testées OK en ligne ; 1 chaîne à 2 sauts |
| Liens internes cassés | Pass | 0 |
| Liens internes vers 301 | **Fail** | 16 797 |
| hreflang | **Fail** | 652 sans x-default, 1 172 clusters partiels |
| Noindex | Pass | 11 (404 + visa-result) ; GSC 249 = périmé |
| Données structurées | Warning | 1 invalide ; FAQPage sur-utilisé ; pas d'Organization |
| Mobile | Pass | viewport 100 %, CSS unique 67 Ko |
| Vitesse | Non mesuré | CWV sans données, PSI quota épuisé — à relancer |
| Poids HTML | Pass | médiane 22,8 Ko |
| Images | Warning | 0 image de contenu ; héros 900 Ko |
| Indexation | **Fail** | 8,7 k indexées / 21,7 k connues |

---

## 6. Concurrents

Sur 8 requêtes tests, **iVisa, VisaHQ, Atlys, VisaGuide n'apparaissent presque jamais en tête** sur l'informationnel. Ce qui ranke : sites officiels (7/9 sur « schengen visa requirements »), cabinets d'immigration (Fragomen, Envoy, Newland Chase) sur l'actualité, **micro-éditeurs de niche** (VisasNews, ISSA Compass, ThaiLawOnline, myvietnamvisa, schengentraveler, hellosafe, opaige) sur le long-tail, marques du pays d'origine (GoDigit, MakeMyTrip, Vanguard NG) par nationalité. evisa-card est en **position 9** sur « schengen visa for nigerian citizens requirements 2026 ».

| Dimension | evisa-card | Atlys | VisaGuide.World | VisasNews | Officiels |
|---|---|---|---|---|---|
| Pages | ~11 k, 10 langues | matrice + hubs + outil | très grand, news | moyen, dense | — |
| Contenu unique | 8 % sur 78 % des pages | outil + hubs rédigés | news quotidienne, passport pages | brèves datées | factsheets |
| Fraîcheur affichée | « March 2026 » sur pages Schengen | « Last Updated May 2026 » + note de source | date dans le title | date par article | datées |
| Auteur / E-E-A-T | byline « Editorial Team, reviewed by D. Cheminaud », **0 source liée** | « Research Team », sources citées, disclaimer | editorial policy, about | rédaction | — |
| Outils | sélecteur visa-search | passeport→destination 200 pays | passport ranking | — | portails |
| Backlinks | ~0 | fort (Série C, presse) | fort | moyen | — |
| SERP features | aucune | snippets sur outils | passport lists | **3 places sur un même top 10** | snippets head |
| **Gagnant** | — | outils + fraîcheur | autorité | fraîcheur | tête de requête |

Règle constatée : plus la requête est générique, plus les officiels saturent ; dès qu'on ajoute nationalité, durée ou action (« extend », « rejected », « transit »), la SERP est tenue par des petits éditeurs battables avec contenu **daté, chiffré, sourcé**.

---

## 7. Opportunités mots-clés (25, triées par opportunité)

| # | Mot-clé | Intention | Difficulté | Opportunité | Position actuelle | Contenu |
|---|---|---|---|---|---|---|
| 1 | thailand visa exemption 30 days new rules september 2026 | Info | Moyen | **Haut** | — | Actu datée + avant/après + 60 pays |
| 2 | can I extend my thailand visa exemption (1900 baht) | Info | Facile | **Haut** | — | Guide TM.7, bureaux |
| 3 | thailand land border entries 2 per year / border run | Info | Facile | **Haut** | — | Explainer air vs terre |
| 4 | vietnam evisa how long does it take | Info | Facile | **Haut** | — | Réponse chiffrée + pics |
| 5 | vietnam digital arrival card | Info | Facile | **Haut** | — | Guide 72 h, aéroports couverts |
| 6 | vietnam evisa rejected what to do | Info | Facile | Haut | — | 12 causes, re-soumission |
| 7 | do south africans / nigerians need ETIAS | Info | Facile | **Haut** | — | Page « ne vous concerne pas » |
| 8 | schengen visa rejection rate nigeria / appeal | Info | Moyen | **Haut** | p.9 (page NG) | Data page + lettre type |
| 9 | schengen visa appointment wait time VFS (IN/NG/ZA) | Info | Moyen | Haut | — | Page vivante par pays |
| 10 | schengen visa for south african citizens requirements | Info | Moyen | Haut | existe | Checklist + coûts ZAR |
| 11 | uk eta transit heathrow airside | Info | Facile | Haut | — | Réponse binaire |
| 12 | vietnam visa exemption 45 days countries list | Info | Moyen | Haut | hub | Liste 24 pays, validité 2028 |
| 13 | vietnam visa for nigerian citizens / phu quoc 30 days | Info | Facile | Haut | existe | Astuce Phu Quoc |
| 14 | how many times can I enter thailand visa exempt | Info | Facile | Haut | — | FAQ longue |
| 15 | thailand DTV visa requirements 2026 | Info | Moyen | Moyen | hub | Casier judiciaire depuis 31/08 |
| 16 | thailand digital arrival card how to fill | Info/Nav | Moyen | Moyen | — | Walkthrough + mise en garde faux sites |
| 17 | thailand overstay fine per day / blacklist | Info | Facile | Moyen | — | Tableau 500 THB/j |
| 18 | vietnam evisa cost 25 usd 50 usd | Info | Facile | Moyen | pages evisa | Officiel vs agence |
| 19 | etias start date / delayed 2027 | Info | Dur | Moyen | — | Page statut horodatée |
| 20 | etias vs ees difference | Info | Moyen | Moyen | — | Tableau comparatif |
| 21 | uk eta cost £20 / eta or visa by nationality | Info | Moyen | Moyen | — | ETA vs visa (85 pays) |
| 22 | thailand visa for filipino citizens 30 days | Info | Facile | Moyen | existe | MAJ 15/09 + « twice by land » |
| 23 | visa free countries for nigerian passport 2026 | Info | Dur | Moyen | — | Liste sourcée Henley |
| 24 | esta for nigerian citizens (not eligible) | Info | Facile | Moyen | — | Alternative B1/B2 |
| 25 | esta cost 2026 $40.27 | Info | Dur | Bas | pages ESTA | Encart chiffré |

Lots prioritaires : #1-3 + #14 (Thaïlande post-15/09), #4-6 + #12-13 (Vietnam), #7-10 (Schengen × NG/ZA/IN), #11 (ETA transit).

---

## 8. Content gaps

| Gap | Pourquoi | Format | Priorité | Effort |
|---|---|---|---|---|
| Flux actualités visa datées + bloc « Latest changes » sur les hubs | VisasNews tient 3 places d'un même top 10 sur la seule fraîcheur | `/xx/news/<slug>` | P1 | Moyen, récurrent |
| Bandeau « dernière vérification » + changelog par page, `dateModified` sincère | Atlys l'affiche ; le site montre « March 2026 » sur des règles changées en avril/sept. | Template | P1 | Faible |
| Vérificateur passeport → destination | Cœur d'Atlys/Sherpa ; les 8 573 pages existent, il manque l'entrée | Étendre `visa-search.js` | P1 | Faible |
| Pages « refus & recours » (Schengen, Vietnam eVisa, UK) | 45,9 % de refus NG ; forte intention ; officiels absents | Guide + lettre type | P1 | Moyen |
| Frais officiels vs frais d'agence par destination | Différenciateur d'un éditeur non vendeur | Tableau sourcé | P1 | Faible |
| Pages « ne vous concerne pas » (ETIAS×ZA/NG/IN, ESTA×NG, ETA×NG/IN/PK) | Capte la confusion des segments forts | Page courte | P1 | Faible |
| Calculateur 90/180 Schengen | Outil le plus recherché de la thématique | JS autonome | P1 | Faible-Moyen |
| Compteur séjour Thaïlande (30+30, 2 entrées terrestres/an) | Règle neuve et complexe | Mini-outil hub | P2 | Faible |
| Pages aéroport / point d'entrée | « ETA Heathrow transit », « arrival card Noi Bai » | `/airport/<code>` | P2 | Moyen |
| Pages visa run / border run | Forte demande post-15/09, blogs expat seulement | Guide | P2 | Moyen |
| Page statistiques (refus par consulat, visas délivrés) | Data pages = backlinks | Annuelle | P2 | Moyen |
| Comparateur ETA/ESTA/ETIAS/eVisa | Confusion passeports faibles | Matrice | P2 | Faible |
| Checklists imprimables, retours lecteurs, screencasts TDAC | Signaux d'utilité/expérience | — | P3 | Faible-Moyen |

E-E-A-T (YMYL voyage) : page auteur réelle + `Person`/`sameAs` ; page méthodologie et sources ; disclaimer « site privé, non affilié » au-dessus de la ligne de flottaison ; **une source officielle liée par fait chiffré** (aujourd'hui 0 lien externe sur la page test) ; `Organization` JSON-LD ; ne jamais rafraîchir une date sans changement.

---

## 9. Plan d'action priorisé

### Décision structurante (avant tout le reste)
**Sort des 8 573 pages citizens.** Google en a déjà rejeté ~8 580. Deux voies :
- **A. Réduction** : garder 1 page par destination × régime (visa-free / eVisa / ambassade) avec tableau des nationalités, rediriger 301 le reste vers elle. Divise le site par ~4, concentre le maillage, cohérent avec les lots B/C1. Coût : perte des rares citizens qui rankaient (nigérian, sud-africain) — à conserver explicitement (~200 pages avec clics sur 16 mois).
- **B. Enrichissement** : ajouter par page un contenu réellement spécifique (frais en devise locale, centre VFS du pays d'origine, taux de refus de la nationalité, exemptions particulières). Réaliste sur ~500 couples à trafic, pas sur 8 573 × 10 langues.
- Recommandation : **A pour les 9 langues non anglaises et pour les couples EN sans impression ; B pour les ~200-500 couples EN qui ont eu des clics** (extraction GSC 16 mois, pages breakdown, 1 000 lignes). Traiter **par cluster hreflang complet**, jamais page par page.

### Quick wins (cette semaine)
| Action | Impact | Effort | Dépend de |
|---|---|---|---|
| Régénérer les blocs Related (16 797 liens vers 301) | Élevé | 2 h script | — |
| Lister les 106 hubs sur `destination.html` × 10 langues (387 hubs orphelins) | Élevé | 2 h | — |
| Régénérer `sitemap.xml` (lastmod) et le scinder par gabarit (citizens / hubs / guides / autres) | Moyen | 1 h | — |
| Footer : lier privacy/terms de la bonne langue (créer les 8 versions manquantes ou pointer vers legal-notice localisé) | Moyen | 2 h | — |
| 81 meta descriptions débris + 12 pages légales vides (traduire ou noindex) + 1 JSON-LD th | Faible | 1 h | — |
| Home : retirer « Updated August 2026 » ; `dateModified` sincère sur les 428 pages TH/VN | Faible | 30 min | — |
| Relancer PSI (quota) sur 3 gabarits | Diagnostic | 10 min | demain |
| Exporter de GSC : 1 000 pages 16 mois avec clics (base de la décision A/B) ; 1 erreur de redirection | Diagnostic | 20 min | — |

### Court terme (2-4 semaines)
| Action | Impact | Effort | Dépend de |
|---|---|---|---|
| Exécuter la décision citizens (A/B), par cluster, avec 301 et sitemap | **Critique** | 2-3 j | export GSC |
| Résoudre les 652 orphelines d'original EN et 1 172 clusters partiels (dans le même passage) | Élevé | inclus | idem |
| Maillage transversal : sur chaque page conservée, liens vers sœurs (même destination), même nationalité, extension/evisa du pays ; breadcrumb hub › page | Élevé | 1 j script | décision A/B |
| Titles > 65 car. : suffixe court par langue (4 816 p.) ; metas > 160 (2 519 p.) | Moyen | 0,5 j | — |
| FAQPage : retirer des citizens, garder sur hubs avec questions propres | Moyen | 0,5 j | — |
| E-E-A-T template : page auteur + méthodologie + disclaimer haut de page + `Organization` + 1 source officielle liée par fait sur hubs TH/VN/Schengen/UK/US | Élevé | 2 j | — |
| Pages « ne vous concerne pas » (6 pages EN) + « frais officiels vs agence » (tableau) | Moyen | 1 j | — |

### Investissements (trimestre)
| Action | Impact | Effort |
|---|---|---|
| Flux news (2-4 brèves/semaine, EN puis FR) + bloc « Latest changes » sur hubs | Élevé | continu |
| 10 pages long-tail des lots #1-13 | Élevé | 3-4 j |
| Vérificateur passeport→destination + calculateur 90/180 + compteur Thaïlande | Moyen-Élevé | 2-3 j |
| Pages refus & recours, statistiques, aéroports | Moyen | 4-5 j |
| Backlinks : publier des données originales (délais VFS relevés, frais toutes destinations) ; débloquer AhrefsBot pour mesurer | Moyen | continu |
| Supprimer assets morts, compresser héros JPEG | Faible | 1 h |

Mesure : attendre 4-6 semaines après la réduction pour lire « explorée non indexée » ; les sitemaps par gabarit rendront la lecture possible.

---

## 10. Corrections à apporter aux notes projet
- La note du 09/09 « ce serveur ignore le quantificateur `/?` dans .htaccess » est **trop générale** : les 10 règles 301 concernées répondent correctement en ligne, et `/blog/` → 301 `/blog` → 410. Le seul échec observé concernait une règle 410 ; cause probable = ordre des règles. Rien à réécrire.
- Le motif « 249 noindex » de GSC n'est pas un défaut du site : état périmé antérieur au 8 juillet.

---

## 11. Corrections appliquées le 26/09/2026 (lots 1 et 2, non commitées)

10 892 fichiers modifiés + 20 créés dans `www2/`. Validation finale sur tout le site : 0 JSON-LD invalide, 0 défaut de structure (main/footer/body), 0 lien interne mort, 0 lien interne vers une 301, 0 hreflang vers un fichier absent, 0 titre dupliqué.

| # | Correction | Volume |
|---|---|---|
| 1a | Blocs Related : liens vers pages consolidées supprimés quand la cible finale (hub) était déjà liée dans le bloc, sinon réécrits vers le hub ; lien « Avertissement » fr/es/pt (301) retiré du footer | 18 941 supprimés, 1 035 réécrits, 7 877 pages |
| 1b | Section « Toutes les destinations A–Z » (noms CLDR localisés) sur les 10 pages `destination` : les 91 hubs pays ont désormais un lien entrant ; cartes Thaïlande (Visa-free 30 days) et Vietnam (USD 25–50) mises à jour | 10 pages |
| 1c | Politique de confidentialité et conditions d'utilisation créées en es, pt, zh, th, ru, ar, ja, ko ; footer de ces 8 langues pointe vers sa propre langue ; clusters hreflang complets (10 langues + x-default) | 16 pages créées, 8 872 footers |
| 1d | `sitemap.xml` devenu un index de 4 sitemaps (hubs 1 070, guides 1 125, citizens 8 573, pages 188 = 10 956 URL, dont les 16 nouvelles pages légales) ; lastmod tiré de git | 5 fichiers |
| 1e | Fil d'Ariane Accueil › Destinations › **Pays** › page (HTML + JSON-LD) | 9 225 pages |
| 2a | Titres > 65 car. : suffixe remplacé par un mot-clé court (citizens, extension) ou supprimé ; 12 titres espagnols restés en anglais traduits | 4 677 + 12 pages |
| 2b | Meta descriptions > 160 car. coupées à la dernière phrase entière | 2 517 pages |
| 2c | Meta descriptions « débris de traduction » réécrites à partir du H1 | 71 pages |
| 2d | Mentions légales et avertissement traduits en zh, th, ru, ar, ja, ko (étaient vides) | 12 pages |
| 2e | JSON-LD FAQ tronqué de `th/visa-france` refermé ; accueil : « official eVisa guides » → « independent », date « Updated August 2026 » retirée | 2 pages |
| 2f | 10 images les plus lourdes recompressées (5,1 Mo → 2,6 Mo) | 10 fichiers |

Non fait, volontairement : suppression des CSS/JS Colorlib (encore utilisés par `contact.html`, ancien gabarit) ; 597 titres > 65 car. sans séparateur exploitable ; libellés des pastilles réécrites vers le hub (ex. « Denmark Requirements » → hub Danemark). Corrigé aussi : le fil d’Ariane de `th/visa-thailand` affichait « จีน » (Chine) au lieu de Thaïlande.
