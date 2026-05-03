# SIGMA Operator Dashboard

Last reviewed locally: 2026-05-04, Asia/Dhaka.

## Project Identity

- Project: SIGMA — Unified Global Standards Index
- Local path: `/home/health-pm/sigma-index`
- GitHub repository: `sigma-standards/sigma-index`
- Default branch: `main`
- Public site pipeline: GitHub Pages through GitHub Actions

## Current Operating Model

SIGMA is maintained as a GitHub-first project. The local machine is a working copy, not the durable source of truth. Durable state should be committed, pushed, validated by GitHub Actions, and documented in the repository.

The project uses a hybrid automation model:

- local `git` and `gh` for branch, commit, push, PR, and Actions inspection
- GitHub connector/app for structured repo and PR operations when available
- GitHub Actions for CI, release, Pages, CodeQL, required gate, and domain agents
- Makefile targets as the common execution layer across local and CI

## Automation Inventory

Core workflows:

- `.github/workflows/ci.yml`
- `.github/workflows/schema_validation.yml`
- `.github/workflows/release_build.yml`
- `.github/workflows/pages.yml`
- `.github/workflows/url_check.yml`
- `.github/workflows/required_gate.yml`
- `.github/workflows/domain_agents.yml`

Agentic automation:

- `data/reference/domain_worker_registry.csv`
- `scripts/run_domain_worker.py`
- `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`

## Validation Commands

Use these before publishing changes:

```bash
git status --short --branch --untracked-files=all
.venv/bin/python -m pytest
make validate
git diff --check
```

Use these after publishing changes:

```bash
gh pr checks <PR_NUMBER> --repo sigma-standards/sigma-index --watch=false
gh run list --repo sigma-standards/sigma-index --branch main --limit 8
git fetch --all --prune
git status --short --branch
```

## Local Versus Remote Rules

Safe to commit:

- source code
- tests
- reference CSVs
- processed CSVs
- relationship CSVs
- project docs
- workflow files
- generated reports that are intentionally part of project status

Keep local only:

- `.venv/`
- `.pytest_cache/`
- `.vscode/` unless intentionally requested
- `dist/`
- `public/`
- `__pycache__/`
- raw Codex runtime files
- secrets and credentials

## Branch And Merge Rules

The GitHub repository protects `main`. If direct push fails, create a branch and PR:

```bash
git switch -c codex/<short-description>
git push -u origin codex/<short-description>
gh pr create --repo sigma-standards/sigma-index --base main --head codex/<short-description>
```

After the PR merges:

```bash
git fetch --all --prune
git switch main
git reset --hard origin/main
```

Use destructive sync commands only when the local branch contains no unrelated user work.

## Provider And Secret Setup

Optional API/provider setup belongs in GitHub repository secrets, not files. Follow:

- `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`

Known optional names:

- `XAI_API_KEY`
- `DEEPSEEK_API_KEY`
- `NCBI_API_KEY`
- `NCBI_USERNAME`
- `APIFY_TOKEN`
- `HF_TOKEN`
- `OPENALEX_MAILTO`
- `CROSSREF_MAILTO`
- `NVD_API_KEY`

Known optional variable names:

- `APIFY_USER_ID`
- `SIGMA_BOT_NAME`
- `SIGMA_BOT_EMAIL`
