# SIGMA Agent Memory Handoff

This document is the safe repository-level memory handoff for future agents. It intentionally summarizes durable operating knowledge instead of copying raw Codex memory, plugin caches, subagent logs, or session transcripts.

## Durable Facts

- Repository: `sigma-standards/sigma-index`
- Local path used in prior work: `/home/health-pm/sigma-index`
- Default branch: `main`
- Local Python preference: `.venv/bin/python`
- CI Python preference: `make PYTHON=python3 ...`
- Makefile is the shared execution layer for local and GitHub Actions.
- Generated folders such as `dist/`, `public/`, `.venv/`, and caches should stay ignored.
- Committed truth lives in source files, scripts, tests, docs, reference data, processed data, relationships, and intentional reports.

## Recent Completed Milestones

- Added relationship quality reporting and release hardening.
- Added required GitHub workflow gates for branch protection.
- Added a free-safe GitHub Domain Agents scaffold:
  - `data/reference/domain_worker_registry.csv`
  - `scripts/run_domain_worker.py`
  - `.github/workflows/domain_agents.yml`
  - `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`
- Added this repository-level agent handoff layer:
  - `AGENTS.md`
  - `docs/OPERATOR_DASHBOARD.md`
  - `docs/AGENT_MEMORY_HANDOFF.md`
  - `.github/copilot-instructions.md`

## Working Pattern

For domain ingestion or automation slices:

1. Add or update a focused test.
2. Add or update the processor or workflow behavior.
3. Update reference or processed CSVs.
4. Sync docs and project status.
5. Run validation:
   - `.venv/bin/python -m pytest`
   - `make validate`
   - `git diff --check`
6. Push through a branch and PR when protected branch rules require it.
7. Verify GitHub checks and Pages/release output.

## GitHub Agentic Automation

The first cloud-agent setup is deterministic by design. It does not require paid LLM APIs. Optional provider tokens are supported only through GitHub Secrets and should remain disabled until the repository owner adds them.

Important safety decisions:

- Domain agents do not write directly to `main`.
- Workflows create pull requests when tracked files change.
- State artifacts must not contain secret values.
- Raw local or Codex runtime memory must not be committed.

## Useful Files For Future Agents

- `AGENTS.md`: repo-wide operating instructions.
- `docs/OPERATOR_DASHBOARD.md`: current repo/cloud/local operations guide.
- `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`: click-by-click GitHub and secret setup.
- `docs/superpowers/specs/2026-05-04-github-domain-agents-design.md`: domain-agent design.
- `docs/superpowers/plans/2026-05-04-github-domain-agents-implementation.md`: implementation plan.
- `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md`: long-range research roadmap.

## What Not To Preserve In Repo

Do not commit:

- `/home/health-pm/.codex/memories/`
- `/home/health-pm/.codex/sessions/`
- `/home/health-pm/.codex/plugins/`
- raw subagent transcripts
- local IDE secrets
- API keys
- generated runtime caches

When durable lessons matter, rewrite them into a short, safe repo document.
