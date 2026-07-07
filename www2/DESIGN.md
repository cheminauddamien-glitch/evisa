# DESIGN SYSTEM — evisa-card.com v2026

> Style : **"Autorité calme" / GovTech-Fintech moderne**  
> Épuré, aéré, beaucoup de blanc, profondeur subtile, iconographie trait fin.  
> Aucun Bootstrap, aucun jQuery, aucun framework. CSS pur, zéro dépendance.

---

## 1. Philosophie

- **Confiance avant tout** : sujet sensible (frontières, gouvernement). Chaque composant doit projeter sérieux et crédibilité.
- **Clarté de données** : densité d'info élevée → hiérarchie typographique forte, tableaux lisibles, résumés scannables.
- **Performance** : LCP < 2,5 s sur mobile bas de gamme. Images `loading="lazy"` + `width/height` obligatoires. Polices `font-display:swap`.
- **Accessibilité** : WCAG AA minimum, un seul `<h1>` par page, landmarks ARIA, skip-link, focus visible.
- **Internationalisation** : 10 langues. RTL géré par `dir="rtl"` + propriétés CSS logiques sans feuille séparée.

---

## 2. Tokens couleurs

```css
/* ── Brand — Bleu passeport ── */
--brand-900: #0B1F3A   /* fonds sombres hero, footer */
--brand-800: #0F2E54   /* header snapshot, header footer */
--brand-700: #173A6B   /* CTA secondaire border, steps, liens */
--brand-600: #1E4D8C   /* couleur de lien par défaut */
--brand-500: #2D6CB8   /* icônes info, focus ring */
--brand-300: #8FB4DD   /* texte sur fond sombre, séparateurs */
--brand-100: #E7EFFA   /* fonds badge, TOC, hover nav */
--brand-050: #F4F8FD   /* fonds de section hero-country, trust bar */

/* ── Action — Vert "approuvé / go" ── */
--action-700: #0B7A53  /* hover CTA primaire */
--action-600: #0E9F6E  /* CTA primaire : bg, border */
--action-500: #15B981  /* icônes success */
--action-100: #DCF6EC  /* badge success bg, row highlight tables */

/* ── Accent — Or "tampon officiel" (usage rare) ── */
--accent-600: #C9871F  /* texte badge officiel, icône alerte officielle */
--accent-500: #E8A33D  /* warning icon */
--accent-100: #FCF1DE  /* bg alerte officielle/warning */

/* ── Sémantique ── */
--success: #0E9F6E
--warning: #E8A33D
--danger:  #D64545
--info:    #2D6CB8

/* ── Neutres slate ── */
--ink-900: #0B1220   /* titres principaux */
--ink-700: #27313F   /* texte courant */
--ink-500: #5A6675   /* texte secondaire, captions */
--ink-400: #8A94A3   /* placeholders, labels */
--line:    #E3E8EF   /* séparateurs, bordures */
--surface-2: #F6F8FB /* sections alternées, sidebar, fonds subtils */
--surface:   #FFFFFF /* fond principal */
```

### Règles d'usage couleur

| Contexte | Couleur |
|---|---|
| CTA primaire (bg) | `--action-600` |
| CTA secondaire (border) | `--brand-700` |
| Liens dans le texte | `--brand-600` |
| Badge "Officiel" / sceau | `--accent-*` |
| Badge "Mis à jour / approuvé" | `--action-*` |
| Section alternée | `--surface-2` |
| Fond hero principal | `--brand-900` → `--brand-700` |

---

## 3. Typographie

### Polices

| Usage | Police | Fallback |
|---|---|---|
| Titres + UI (latin/cyrillique) | Plus Jakarta Sans | system-ui, -apple-system |
| Corps (latin/cyrillique) | Inter | system-ui, -apple-system |
| CJK Simplifié | Noto Sans SC | PingFang SC, Microsoft YaHei |
| CJK Japonais | Noto Sans JP | Hiragino Sans, Yu Gothic |
| CJK Coréen | Noto Sans KR | Apple SD Gothic Neo |
| Thaï | Noto Sans Thai | Leelawadee UI |
| Arabe | IBM Plex Sans Arabic | Noto Sans Arabic, Segoe UI |

**Chargement :** `<link rel="preconnect" href="https://fonts.googleapis.com">` + `<link rel="stylesheet" href="...&display=swap">` dans `<head>`. Pas d'`@import` CSS (render-blocking).

**Script par langue :**
```html
<!-- CJK Simplifié -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap">
<!-- Arabe -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">
```

Le CSS applique automatiquement la police via `:lang(zh)`, `:lang(ar)` etc.

### Échelle typographique

```
--fs-xs:   .800rem  (12.8 px) — labels, captions, breadcrumb
--fs-sm:   .900rem  (14.4 px) — texte secondaire, nav, badges
--fs-base: 1.000rem (16 px)   — texte courant, body
--fs-md:   1.125rem (18 px)   — intro, lead, step title
--fs-lg:   1.375rem (22 px)   — h3, sous-sections
--fs-xl:   1.750rem (28 px)   — h2, titres de sections
--fs-2xl:  2.250rem (36 px)   — h1 pages internes
--fs-3xl:  3.000rem (48 px)   — h1 homepage (clampé)
```

**Règles texte corps :** longueur de ligne 65–75 ch (`max-width: 70ch` sur `<p>`), interligne 1.65–1.75, `text-wrap: balance` sur les titres.

---

## 4. Espacement (base 4 px)

```
--sp-1:  .25rem  ( 4 px)
--sp-2:  .5rem   ( 8 px)
--sp-3:  .75rem  (12 px)
--sp-4:  1rem    (16 px)
--sp-6:  1.5rem  (24 px)
--sp-8:  2rem    (32 px)
--sp-12: 3rem    (48 px)
--sp-16: 4rem    (64 px)
--sp-24: 6rem    (96 px)
```

---

## 5. Rayons, Ombres, Transitions

```css
/* Rayons */
--r-sm:   8px
--r-md:   12px
--r-lg:   16px
--r-pill: 999px

/* Ombres (3 niveaux, tintées brand) */
--sh-1: 0 1px 3px rgba(11,31,58,.06), 0 1px 2px rgba(11,31,58,.04)
--sh-2: 0 4px 12px rgba(11,31,58,.08), 0 2px 6px rgba(11,31,58,.05)
--sh-3: 0 8px 24px rgba(11,31,58,.10), 0 4px 12px rgba(11,31,58,.06)

/* Transitions */
--tr:      160ms ease   /* hover léger */
--tr-slow: 280ms ease   /* open/close panels */
```

---

## 6. Grille & Layout

- **Container max :** 1200 px (`--container-max`)
- **Article max :** 740 px (`--article-max`) — texte long centré
- **Gouttière :** 24 px (`--gutter` = `1.5rem`)
- **Header height :** 64 px (`--header-h`)
- **Breakpoints :**
  - `≤ 480 px` — mobile
  - `481–768 px` — grand mobile / tablette portrait
  - `769–1024 px` — tablette / petit desktop
  - `≥ 1025 px` — desktop

---

## 7. Inventaire des composants CSS

| Classe racine | Description |
|---|---|
| `.site-header` | Header sticky |
| `.site-nav` | Navigation principale |
| `.nav-toggle` | Hamburger mobile |
| `.lang-selector` | Sélecteur de langue dropdown |
| `.breadcrumb` | Fil d'Ariane microdata |
| `.hero-home` | Hero homepage (fond brand sombre) |
| `.hero-country` | Hero hub pays (fond clair) |
| `.hero-article` | Hero page article (compact) |
| `.dest-search` | Barre de recherche destination |
| `.trust-bar` | Barre de signaux de confiance |
| `.visa-snapshot` | Carte "visa en un coup d'œil" (KPIs) |
| `.country-card` | Carte pays (flag + nom + flèche) |
| `.dir-card` | Carte répertoire (flag large + nom centré) |
| `.dir-tile` | Tuile répertoire enrichie (flag + nom + badge visa + description) — page `/destination` |
| `.dest-card` | Carte destination photo (image + drapeau overlay + badge visa) |
| `.badge` | Badge inline (variantes: brand/success/warning/danger/official/neutral) |
| `.pill-tag` | Tag cliquable arrondi |
| `.btn` | Bouton (variantes: primary/secondary/ghost, tailles: sm/lg) |
| `.table-wrap` | Conteneur tableau responsive (scroll horizontal) |
| `.data-table` | Tableau de données stylé |
| `.steps` | Liste d'étapes numérotées (timeline) |
| `.faq-list` | Accordéon FAQ natif (`<details>/<summary>`) |
| `.alert` | Encadré alerte (info/warning/official/danger/success) |
| `.cta-banner` | Bannière CTA horizontale |
| `.toc` | Table des matières ancrée |
| `.related-links` | Bloc de liens associés |
| `.page-layout` | Grille article (2 col : main + aside) |
| `.sidebar-card` | Carte de la sidebar |
| `.site-footer` | Footer riche multi-colonnes |
| `.back-to-top` | Bouton retour haut de page |
| `.flag-chip` | Chip drapeau + nom |
| `.article-body` | Wrapper typographique pour le contenu éditorial |
| `.continent-group__title` | Séparateur "continent" dans les grilles |

---

## 8. RTL

Le RTL est géré **exclusivement via les propriétés CSS logiques** :

```css
/* Au lieu de :           → Utiliser : */
margin-left / right       → margin-inline-start / end
padding-left / right      → padding-inline-start / end
border-left / right       → border-inline-start / end
left / right              → inset-inline-start / end
text-align: left          → text-align: start
```

Seules exceptions (overrides explicites dans site.css) :
- Chevrons breadcrumb (background-image SVG mirrored pour `[dir="rtl"]`)
- Flèche `country-card__arrow` (translateX inversé)

**Usage en HTML :**
```html
<html lang="ar" dir="rtl">
```

---

## 9. Dark mode

Activé automatiquement via `@media (prefers-color-scheme: dark)`. Redéfinit les tokens surface/ink/line/shadows. Pas de classe manuelle requise.

---

## 10. Accessibilité — checklist

- [ ] Un seul `<h1>` par page
- [ ] Hiérarchie Hn correcte (pas de sauts)
- [ ] Landmarks : `<header role="banner">`, `<nav>`, `<main>`, `<aside>`, `<footer role="contentinfo">`
- [ ] Skip link (`.skip-link`) en premier enfant du `<body>`
- [ ] Focus visible sur tous les éléments interactifs (`:focus-visible`)
- [ ] Images décoratives : `alt=""`; images informatives : alt descriptif
- [ ] Tableaux : `<caption>`, `scope="col"` sur les `<th>`
- [ ] FAQ : structure `FAQPage` JSON-LD
- [ ] Fil d'Ariane : `BreadcrumbList` JSON-LD + microdata itemprop

---

## 11. SEO — par template

| Template | JSON-LD requis |
|---|---|
| Toutes | `Organization` (footer) |
| Toutes pages internes | `BreadcrumbList` |
| Hub pays | `FAQPage` + `HowTo` |
| Pages combinatoires | `FAQPage` |
| Listicles/Blog | `Article` |
| Homepage | `WebSite` + `Sitelinks Searchbox` |

```html
<!-- Canonical (URL propre sans .html) -->
<link rel="canonical" href="https://evisa-card.com/visa-thailand">

<!-- Hreflang x10 + x-default -->
<link rel="alternate" hreflang="en" href="https://evisa-card.com/visa-thailand">
<link rel="alternate" hreflang="fr" href="https://evisa-card.com/fr/visa-thailand">
<!-- ... -->
<link rel="alternate" hreflang="x-default" href="https://evisa-card.com/visa-thailand">
```

---

## 12. Performance

- Images : toujours `width` + `height` + `loading="lazy"` (sauf above-the-fold)
- Drapeaux : `https://flagcdn.com/w40/{cc}.png` (40 px) ou `w80` (80 px). En prod : héberger en local dans `/assets/flags/`
- CSS : fichier unique `site.css`, servi avec `Cache-Control: max-age=31536000, immutable` + version dans l'URL
- Polices : `<link rel="preconnect">` + `display=swap`, chargées per-langue si CJK/Arabic
- `prefers-reduced-motion` : respecté dans toutes les animations/transitions
