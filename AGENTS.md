<!-- ============================================================ -->
<!--  RÈGLE ABSOLUE — DOSSIER DE PRODUCTION (NE JAMAIS IGNORER)  -->
<!-- ============================================================ -->

# ⛔ RÈGLE #1 — TOUJOURS ÉDITER LE DOSSIER PROD `www/`

**Le site mis en ligne par FTP manuel est UNIQUEMENT :**

```
C:\Users\chemi\Documents\evisa\pacific-main\www\
```

## OBLIGATIONS (chaque modification de contenu du site)

1. **TOUTE** édition de page / robots.txt / sitemap.xml / .htaccess / asset
   DOIT être faite dans `C:\Users\chemi\Documents\evisa\pacific-main\www\`
   — avec le **chemin ABSOLU complet**, jamais en relatif.

2. **NE JAMAIS éditer** les copies suivantes (elles ne sont PAS uploadées) :
   - `…\pacific-main\.claude\worktrees\…\www\`  ← worktree, souvent PÉRIMÉ
   - les dossiers `en/ fr/ es/ pt/` à la **racine** de `pacific-main\` (ancienne structure 4 langues, NON déployée)

3. **Le CWD du shell se réinitialise souvent sur le worktree** :
   `…\.claude\worktrees\great-chatterjee-b70d97`.
   → AVANT toute commande, faire `cd "C:\Users\chemi\Documents\evisa\pacific-main"`
   et utiliser des chemins absolus `www\...`. Ne jamais se fier au CWD.

4. **AVANT de dire « c'est fait »** : vérifier que la modif est bien dans
   `C:\Users\chemi\Documents\evisa\pacific-main\www\<fichier>` (pas le worktree)
   via un `grep`/`Read` sur le chemin absolu de prod.

5. **robots.txt et sitemap.xml de prod** = `www\robots.txt` et `www\sitemap.xml`.
   Le `robots.txt` / `sitemap.xml` à la racine de `pacific-main\` est IGNORÉ par le serveur — ne pas l'éditer seul.

6. L'utilisateur uploade le **contenu de `www\`** à la racine web par FTP
   (FileZilla, fichiers cachés `.htaccess` inclus). Rien d'autre n'est déployé.

> Si une modif n'est pas dans `pacific-main\www`, elle N'EXISTE PAS pour le site en ligne.

<!-- ============================================================ -->

# ⛔ RÈGLE #2 — REDIRECTION 301 OBLIGATOIRE À CHAQUE CHANGEMENT D'URL

**Dès qu'une URL de page change** (renommage de fichier ou de slug, déplacement,
suppression, fusion de pages, changement de dossier/langue), tu DOIS ajouter une
redirection **301** (permanente) de l'ANCIENNE URL vers la NOUVELLE dans :

```
C:\Users\chemi\Documents\evisa\pacific-main\www\.htaccess
```

## OBLIGATIONS (chaque changement d'URL)

1. Ajouter la règle dans la section `# 301 Redirects — old URLs / restructuration`
   du `.htaccess`, au format (chemins absolus depuis la racine web, **sans** le domaine) :
   ```apache
   Redirect 301 /ancienne-url /nouvelle-url
   ```
2. **Une redirection par langue concernée** (en, fr, es, pt, zh, th, ru, ar, ja, ko)
   si le slug change dans plusieurs dossiers.
3. Mettre à jour EN MÊME TEMPS : `www\sitemap.xml`, les balises `canonical` + `hreflang`
   de la page, et tout lien interne (nav, footer, autres pages) pointant vers l'ancienne URL.
4. **NE JAMAIS** laisser une ancienne URL déjà indexée renvoyer un 404 : c'est une perte
   de trafic SEO directe. Pas de 301 = changement d'URL interdit.
5. Préférer une vraie 301 dans `.htaccess` à une simple balise canonical : la 301 transmet
   le « link juice » et déréférence proprement l'ancienne URL.

> Aucune URL à fort trafic ne doit être cassée. La 301 fait partie de la MÊME modification
> que le renommage — jamais « on verra plus tard ».

<!-- ============================================================ -->

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **evisa** (18173 symbols, 20025 relationships, 196 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/evisa/context` | Codebase overview, check index freshness |
| `gitnexus://repo/evisa/clusters` | All functional areas |
| `gitnexus://repo/evisa/processes` | All execution flows |
| `gitnexus://repo/evisa/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->
