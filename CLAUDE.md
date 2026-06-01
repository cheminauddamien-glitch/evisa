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

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **pacific-main** (14458 symbols, 15588 relationships, 78 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## When Debugging

1. `gitnexus_query({query: "<error or symptom>"})` — find execution flows related to the issue
2. `gitnexus_context({name: "<suspect function>"})` — see all callers, callees, and process participation
3. `READ gitnexus://repo/pacific-main/process/{processName}` — trace the full execution flow step by step
4. For regressions: `gitnexus_detect_changes({scope: "compare", base_ref: "main"})` — see what your branch changed

## When Refactoring

- **Renaming**: MUST use `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` first. Review the preview — graph edits are safe, text_search edits need manual review. Then run with `dry_run: false`.
- **Extracting/Splitting**: MUST run `gitnexus_context({name: "target"})` to see all incoming/outgoing refs, then `gitnexus_impact({target: "target", direction: "upstream"})` to find all external callers before moving code.
- After any refactor: run `gitnexus_detect_changes({scope: "all"})` to verify only expected files changed.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Tools Quick Reference

| Tool | When to use | Command |
|------|-------------|---------|
| `query` | Find code by concept | `gitnexus_query({query: "auth validation"})` |
| `context` | 360-degree view of one symbol | `gitnexus_context({name: "validateUser"})` |
| `impact` | Blast radius before editing | `gitnexus_impact({target: "X", direction: "upstream"})` |
| `detect_changes` | Pre-commit scope check | `gitnexus_detect_changes({scope: "staged"})` |
| `rename` | Safe multi-file rename | `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` |
| `cypher` | Custom graph queries | `gitnexus_cypher({query: "MATCH ..."})` |

## Impact Risk Levels

| Depth | Meaning | Action |
|-------|---------|--------|
| d=1 | WILL BREAK — direct callers/importers | MUST update these |
| d=2 | LIKELY AFFECTED — indirect deps | Should test |
| d=3 | MAY NEED TESTING — transitive | Test if critical path |

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/pacific-main/context` | Codebase overview, check index freshness |
| `gitnexus://repo/pacific-main/clusters` | All functional areas |
| `gitnexus://repo/pacific-main/processes` | All execution flows |
| `gitnexus://repo/pacific-main/process/{name}` | Step-by-step execution trace |

## Self-Check Before Finishing

Before completing any code modification task, verify:
1. `gitnexus_impact` was run for all modified symbols
2. No HIGH/CRITICAL risk warnings were ignored
3. `gitnexus_detect_changes()` confirms changes match expected scope
4. All d=1 (WILL BREAK) dependents were updated

## Keeping the Index Fresh

After committing code changes, the GitNexus index becomes stale. Re-run analyze to update it:

```bash
npx gitnexus analyze
```

If the index previously included embeddings, preserve them by adding `--embeddings`:

```bash
npx gitnexus analyze --embeddings
```

To check whether embeddings exist, inspect `.gitnexus/meta.json` — the `stats.embeddings` field shows the count (0 means no embeddings). **Running analyze without `--embeddings` will delete any previously generated embeddings.**

> Claude Code users: A PostToolUse hook handles this automatically after `git commit` and `git merge`.

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
