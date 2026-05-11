# SIGMA Agent Instructions

These instructions apply to the entire `sigma-index` repository.

## Mission

SIGMA is the Unified Global Standards Index: a public, machine-readable, human-navigable index of global standards, treaties, frameworks, guidelines, classification systems, and standards bodies. It is the world's first free, open dataset of its kind.

Keep the project useful after any local machine or temporary session disappears. Durable operating knowledge belongs in this repository as reviewed source, docs, tests, workflows, and reference data.

## Source Of Truth

| Item | Value |
|------|-------|
| Local repo path | `/home/health-pm/sigma-index` |
| GitHub repo | `sigma-standards/sigma-index` |
| Default branch | `main` |
| Python (local) | `.venv/bin/python` |
| Python (CI) | `make PYTHON=python3 ...` |
| Primary execution layer | `Makefile` (run `make help` for all targets) |

## Files That Must Be Committed

```
.github/          — workflows, issue templates, copilot instructions
AGENTS.md         — this file
README.md         — project overview with sample data table
SCHEMA.md         — 22-field canonical schema
CHANGELOG.md      — version history
CONTRIBUTING.md   — contribution guide (coding + non-coding paths)
RESEARCH_PROJECT_PLAN_Global_Standards_Index.md
Makefile          — primary build interface
pyproject.toml    — Python package config
docs/             — all project documentation
scripts/          — all processing scripts (with __init__.py)
tests/            — full pytest suite
data/reference/   — taxonomy, source registry, research tasks
data/processed/   — curated, schema-valid CSVs (source of truth)
data/relationships/ — relationship graph edges
data/reports/     — quality gate, coverage, task coverage (generated, committed)
data/staging/     — curator-review candidates (committed but NOT in release)
```

## Files That Must NOT Be Committed

```
.venv/                  — virtual environment
dist/                   — generated release artifacts
public/                 — generated static site
__pycache__/            — Python bytecaches
*.py[cod]               — compiled Python
.pytest_cache/          — test cache
.env                    — environment variables / secrets
*.key / *.token         — credentials
sigma_full_implementation.py  — ad-hoc push script (security risk)
/home/health-pm/.codex/ — Codex session memory, NEVER commit
```

## Required Workflow For Every Change

1. **Check state** before touching anything:
   ```bash
   git status --short --branch
   git remote -v
   ```
2. **Make focused changes** matching existing patterns.
3. **Add tests** for any new processing logic.
4. **Validate** before committing:
   ```bash
   make validate
   make lint
   python -m pytest
   ```
5. **Commit** with a clear message:
   ```bash
   git add <files>
   git commit -m "feat|fix|docs|chore: short description"
   ```
6. **Push via branch + PR** (direct pushes to `main` are blocked):
   ```bash
   git checkout -b feat/my-change
   git push origin feat/my-change
   gh pr create --base main --head feat/my-change --title "..."
   ```
7. **Sync** after merge:
   ```bash
   git fetch --all --prune && git switch main && git reset --hard origin/main
   ```

## Domain Agents (GitHub Actions)

Registry: `data/reference/domain_worker_registry.csv`
Runner: `scripts/run_domain_worker.py`
Workflow: `.github/workflows/domain_agents.yml`
Setup guide: `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`

Domain agents MUST:
- Run through Makefile targets only
- Write state artifacts (no secrets)
- Validate before opening PRs
- Open PRs — never commit directly to `main`
- Require human review before merge

## Secrets Management

Never commit secrets. Add provider credentials only through:

**GitHub → Settings → Secrets and variables → Actions**

All known optional secret names are documented in `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`.

## Data Quality Rules

- Every `data/processed/*.csv` file must pass `make validate` (0 errors)
- `data/staging/` files are excluded from the release bundle until curated
- `llm-suggested` relationship edges must NOT be published without human review
- All `official_url` values must start with `https://`
- No duplicate `sigma_id` values anywhere in processed data

## Memory And Handoff

Never copy raw session memory, plugin caches, or subagent logs into this public repo. Convert durable knowledge into safe project documents in `docs/`. If a future agent needs prior context, read `docs/AGENT_MEMORY_HANDOFF.md` first.
