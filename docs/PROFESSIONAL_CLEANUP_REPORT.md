# SIGMA Professional Cleanup Report

**Date:** 2026-05-30  
**Branch:** `restructure/professional-cleanup`

## Purpose

This report records the cleanup decisions used to convert `sigma-index` into a strict, GitHub-hosted source repository. It is the durable handoff for future agents so local machine state, downloaded archives, and temporary session files do not become project source.

## Local Repository Decisions

- Removed generated topology snapshots, copied exports, temporary skill bundles, and redundant root planning documents from tracked source.
- Removed `data/processed/sigma_master_global.csv` because it was a generated aggregate in the same directory as source processed datasets. Keeping it caused schema failure and duplicate release records.
- Removed tracked `data/raw/` and `data/staging/` extracts. Harvesters may still write these folders locally or in Actions runs, but promotion into source must happen through reviewed `data/reference/`, `data/processed/`, `data/relationships/`, or `data/reports/` files.
- Kept durable project governance and setup material in `AGENTS.md`, `docs/`, `.github/`, `.devcontainer/`, `scripts/`, `tests/`, and approved `data/` paths.

## External Asset Review

Reviewed sources:

- `/home/health-pm/Desktop/sigma_project`
- `/home/health-pm/Desktop/sigma_v1`
- `/home/health-pm/Downloads/sigma_patch_v1`
- `/home/health-pm/Downloads/sigma_v1 (1)`
- `/home/health-pm/Downloads/SIGMA-INDEX - GitHub Agentic Workflow Analysis.md`

Imported durable concepts:

- LLM wiki concept: agent-facing knowledge should live in reviewed repository docs, not sidecar folders.
- Domain agent contract: domain workers need stable entrypoints, deterministic validation, source provenance, and human-reviewed PR output.
- Orchestration priority: agent cycles should run through repository workflows and `Makefile` targets instead of ad hoc local scripts.
- GitHub workflow analysis: deterministic validation, safe permissions, secret names only, branch protections, and PR-based automation are the governing model.

Rejected from import:

- `.env`, local virtual environments, local git metadata, Playwright logs, local session logs, package caches, SQLite knowledge graph files, downloaded zips, and generated dashboards.
- Full external `agents/` trees and `.opencode/` bundles because the repository already has a deterministic domain-worker scaffold in `scripts/run_domain_worker.py`, `.github/workflows/domain_agents.yml`, and `data/reference/domain_worker_registry.csv`.
- Generated `public/` and dashboard output because GitHub Pages should rebuild publication artifacts from source.

## Automation Fixes

- CI now uses repository dependencies and the same `make PYTHON=python3 validate` path as local validation.
- Gitleaks now runs through the free CLI container instead of the organization-licensed GitHub Action.
- Release and Pages workflows now use `Makefile` targets for validation, release builds, and static-site generation.
- Domain-agent workflows no longer stage `data/staging/`; staging output remains an intermediate artifact unless promoted to approved source paths.

## Follow-Up

- Configure `main` branch protection or repository rulesets to require PRs and the core checks after this cleanup PR passes.
- Keep external SIGMA folders as local archives until the PR merges, then remove or move them outside active workspace use.
- Treat future copied planning docs as inputs for `docs/`, not as root-level tracked source files.
