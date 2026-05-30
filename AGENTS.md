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
   - verify no disallowed files are staged or changed:
     `git status --porcelain | grep -E "(^|/)(\.(venv|agents|codex|tmp|pytest_cache)|public/|data/raw/|data/staging/)"`

2. Determine the change type and follow the matching flow:

   A. Docs-only change
   - Applies to documentation or narrative edits only: `docs/`, `README.md`, `CHANGELOG.md`, `AGENTS.md`, `docs/*.md`, and similar prose files.
   - Run validations: `make validate` and `git diff --check`.
   - Tests are optional for docs-only edits.

   B. Code/behavior change
   - Applies to code, configuration, scripts, tests, and runtime behavior changes.
   - Run validations: `.venv/bin/python -m pytest`, `make validate`, and `git diff --check`.
   - Add or update unit/integration tests when runtime behavior or public interfaces change.

   C. Data change
   - Applies to generated index data, reference files, processed outputs, and report artifacts under `data/reference/`, `data/processed/`, `data/relationships/`, and `data/reports/`.
   - Run validations: `make validate` and `git diff --check`.
   - For generated data, include a validation summary file such as `data/reports/validation-<date>.md` in the PR.

3. If required tools are missing, abort and report:
   - `Environment missing: .venv or make. Run make setup or contact a maintainer.`
   - Provide fallback commands or Docker container instructions only if the repo maintainer has documented them.

4. If any validation or tests fail locally, do not commit or open a PR.
   - Fix failures locally before proceeding.
   - If failure is unrelated or flaky, document the failure and request maintainer guidance in the PR description.
   - If tests fail locally, stop and fix the issues before committing; do not open a PR that knowingly fails tests.

5. Save changes locally with a commit.
   - Make focused changes: limit each commit to a single logical change (preferably ≤5 files and ≤200 lines changed), follow existing file naming and code style, and include/update tests when behavior is modified.
   - Use branch names like `feat/<short-desc>`, `fix/<short-desc>`, or `docs/<short-desc>`.
   - Use Conventional Commits format for commit messages, e.g. `feat(stats): add aggregation script`, and include ticket/issue references when available.

6. Push through GitHub safely:
   - Always create a feature branch and open a pull request.
   - Only push to `main` directly when explicitly authorized by a repo maintainer in writing.
   - Confirm GitHub checks pass before requesting review.

7. Sync local `main` back to `origin/main` after merge.
   - If merge conflicts occur, rebase local `main` onto `origin/main`, resolve conflicts, run validations again, and push.
   - If unsure, open a draft PR and request maintainer help.

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

State artifacts are generated JSON/YAML/CSV files under `data/processed/`, `data/reference/`, `data/reports/`, or `data/relationships/` that do not contain credentials.

Validation for generated data must include:
- schema validation via `make validate`
- sample spot-checks against source references
- a summary file such as `data/reports/validation-<date>.md` included in the PR

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

If a secret is accidentally committed, follow these remediation steps:
1. Rotate the secret immediately.
2. Remove the secret from history using `git filter-repo` or `git filter-branch`.
3. Force-push a sanitized branch only after coordinating with maintainers.
4. Open an incident PR describing the remediation.
