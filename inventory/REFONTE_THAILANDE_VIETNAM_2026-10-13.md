# Refonte Thaïlande / Vietnam — 13 octobre 2026

Brief appliqué : `Downloads/brief_claude_corrections_thailande_vietnam.txt`.
Faits revérifiés le 13/10/2026 sur les sources officielles : ambassade royale de Thaïlande en France (thaiembassy.fr), gouvernement thaïlandais, TAT, France Diplomatie (mise à jour du 07/10), thaievisa.go.th, ministère vietnamien de la Sécurité publique, evisa.gov.vn, baochinhphu.vn, ambassade de Singapour au Vietnam et gov.uk.

## Fichiers modifiés dans `www2/` : 135

| Pages | Langues | Contenu |
|---|---|---|
| `visa-thailand`, `visa-vietnam` | 10 | Réécriture complète : bandeau sourcé et daté, tableaux par nationalité, séparation entre frais officiels, formalités d'arrivée (TDAC, PAI) et conseils, FAQ visible et JSON-LD régénéré, encadré « site indépendant, non gouvernemental » |
| `thailand-evisa`, `vietnam-evisa` | 10 | Réécriture : portail officiel, frais officiels distincts des frais de service, délais indicatifs ; `</section>` orphelin du gabarit retiré hors anglais |
| `thailand-visa-extension`, `vietnam-visa-extension` | 10 | Réécriture : prolongation du visa TR (1 mois, 1 900 THB) ; exemption thaïlandaise « à vérifier » ; aucune prolongation automatique au Vietnam |
| `index`, `destination` (accueils) | 10 | Cartes Thaïlande et Vietnam : badge, ligne de faits, description |
| `expat-guide-thailand`, `expat-guide-vietnam`, `thailand-visa-processing-time` (en, es, ja), `th/vietnam-visa-fees` | 10 | Ancien bandeau remplacé par le nouveau ; ancien portail `evisa.xuatnhapcanh.gov.vn` remplacé par `evisa.gov.vn` |
| `en/vietnam-visa-for-*-citizens` | 20 pages | Portail, frais 25/50 USD, durée « jusqu'à 90 jours », délai indicatif, visa à l'arrivée ; og/twitter:description réalignés sur la description (Russie, Philippines et Indonésie disaient encore « e-Visa obligatoire ») |
| `en/thailand-visa-for-pakistani-citizens` | 1 | Frais 2 000 THB, délai 5–10 jours et séjour de 30 jours non sourcés retirés ; 20 000 THB ; prolongation du visa TR |
| `visa-processing-times` | 10 | Lignes Thaïlande (ancienne exemption de 60 jours) et Vietnam (traductions cassées en thaï, arabe, japonais et coréen) |

Contrôles : `validate.py` avant et après donne 0 JSON-LD invalide, 0 défaut de structure, 0 lien mort, 0 hreflang cassé et 0 titre dupliqué. Les titres de plus de 65 caractères passent de 332 à 320. Les comptes de balises et les href de chaque traduction sont identiques à la source française, les chiffres aussi, sauf dans la question de FAQ volontairement rendue générique hors français (« Ai-je besoin d'un visa… », toutes nationalités). Aucun texte injecté en arabe ou en thaï ne contient de chiffres non occidentaux. Les tableaux restent défilables sur mobile (`.table-wrap`).

## Points encore « à vérifier » (affichés comme tels sur les pages)

1. **Thaïlande, prolongation de l'exemption de 30 jours** : aucune source officielle ne confirme une prolongation de 30 jours à 1 900 THB pour l'exemption. Seule la prolongation du visa TR (1 mois, 1 900 THB) est confirmée.
2. **Thaïlande, accords bilatéraux** (90, 30 et 14 jours) : les exemples restent « à confirmer » pays par pays.
3. **Thaïlande, assurance santé** : les montants exigés pour certains visas de long séjour sont à vérifier.
4. **Thaïlande, frais et délais hors de France** : ils dépendent du lieu de dépôt (affichés sur thaievisa.go.th). Les 35 € et le délai d'environ 4 semaines valent pour une demande déposée depuis la France.
5. **Vietnam, PAI** : déclaration volontaire pendant le pilote (Tân Sơn Nhất, puis Nội Bài, Đà Nẵng, Nha Trang et Phú Quốc). Son caractère obligatoire après le pilote et son périmètre exact sont à suivre.
6. **Vietnam, délai de l'e-Visa** : « environ 3 jours ouvrables » est indicatif, aucun texte officiel ne le garantit.
7. **Vietnam, exemptions ASEAN et bilatérales** (30 jours ; Philippines 21 jours ; Chili 90 jours) : marquées « à confirmer ».
8. **Vietnam, amendes de dépassement** : aucun montant publié retenu, la page parle d'« amende administrative ».

## Hors périmètre, non corrigé

- `visa-processing-times` (ar, th, ja, ko) : les autres pays du tableau gardent des traductions automatiques fautives, par exemple « ขนาด N/ A » ou des chiffres arabo-indiens.
