# SIGMA Agent Instructions

These instructions apply to the entire `sigma-index` repository.

## Mission

SIGMA is the Unified Global Standards Index: a public, machine-readable, human-navigable index of global standards, treaties, frameworks, guidelines, classification systems, and standards bodies.

Keep the project useful after any local machine or temporary Codex session disappears. Durable operating knowledge belongs in this repository as reviewed source, docs, tests, workflows, and reference data.

## Source Of Truth

- Local repo path: `/home/health-pm/sigma-index`
- GitHub repo: `sigma-standards/sigma-index`
- Default branch: `main`
- Python local default: `.venv/bin/python`
- GitHub Actions Python override: `make PYTHON=python3 ...`
- Main execution layer: `Makefile`

Commit source truth only:

- `.devcontainer/`
- `.github/`
- `.gitattributes`
- `.gitignore`
- `AGENTS.md`
- `CHANGELOG.md`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `README.md`
- `SCHEMA.md`
- `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md`
- `docs/`
- `scripts/`
- `tests/`
- `data/reference/`
- `data/processed/`
- `data/relationships/`
- `data/reports/`
- `Makefile`
- `pyproject.toml`

Generated aggregates, local topology snapshots, generated Pages output, raw harvest outputs, staging extracts, local agent memory, downloaded patches, and exploratory archives are not source truth. Convert durable knowledge from them into approved docs, tests, workflows, scripts, or reference data before removing them.

Do not commit local/runtime artifacts:

- `.venv/`
- `.agents/`
- `.codex/`
- `.tmp/`
- `.pytest_cache/`
- `.vscode/` unless a repo maintainer explicitly asks for IDE config
- `.windsurf/`
- `dist/`
- `public/`
- `data/raw/`
- `data/staging/`
- `__pycache__/`
- `temp_assets/`
- `.envrc`
- root-level generated inventory files such as `*_sigma-index.md`
- root-level copied exports such as `sigma_master*.csv`
- raw Codex memory or session folders from `/home/health-pm/.codex/`
- secrets, tokens, API keys, or copied logs that may contain credentials

## Required Workflow

1. Inspect current state before changing files:
   - `git status --short --branch --untracked-files=all`
   - `git remote -v`
   - `git branch -vv --all`
2. Make focused changes that match existing repo patterns.
3. Use tests for behavior changes.
4. Run relevant validation:
   - `.venv/bin/python -m pytest`
   - `make validate`
   - `git diff --check`
5. Save changes locally with a commit.
6. Push through GitHub safely:
   - direct pushes to `main` may be blocked by branch rules
   - use a feature branch and pull request when required
   - confirm GitHub checks pass
7. Sync local `main` back to `origin/main` after merge.

## GitHub Domain Agents

The repository includes a free-safe, deterministic multi-agent scaffold:

- Registry: `data/reference/domain_worker_registry.csv`
- Runner: `scripts/run_domain_worker.py`
- Workflow: `.github/workflows/domain_agents.yml`
- Setup guide: `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`

Domain agents should:

- run through Makefile targets
- write state artifacts, not secret values
- validate generated data before PR creation
- open pull requests instead of writing directly to `main`
- require human review before merge

## Memory And Handoff

Do not copy raw `/home/health-pm/.codex/memories`, sessions, plugin caches, or subagent logs into this public repo. Convert durable knowledge into safe project documents:

- `docs/OPERATOR_DASHBOARD.md`
- `docs/AGENT_MEMORY_HANDOFF.md`
- `docs/superpowers/plans/`
- `docs/superpowers/specs/`

If a future agent needs prior context, read those repo docs first.

## Secrets

Never commit real secrets. Add optional provider credentials only through GitHub:

`Settings -> Secrets and variables -> Actions`

Known optional secret names are documented in `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`.
