# GitHub Domain Agents Design

## Goal

Make GitHub the durable operating center for SIGMA domain refreshes, validation, reporting, and publication while keeping the local machine optional.

## Architecture

The first version uses deterministic GitHub Actions workers rather than paid AI agents. Each worker is declared in `data/reference/domain_worker_registry.csv` and executed by `scripts/run_domain_worker.py`, which maps an `agent_id` to a Makefile target. The GitHub workflow runs workers manually or on a schedule, validates output, uploads state artifacts, and opens a pull request when files change.

## Safety Model

Agents do not write directly to `main`. The workflow uses `contents: write` and `pull-requests: write` only so it can create a branch and PR. Secrets are referenced by name, not committed. Optional provider tokens such as `XAI_API_KEY`, `DEEPSEEK_API_KEY`, `NCBI_API_KEY`, `APIFY_TOKEN`, and `HF_TOKEN` are disabled until the repository owner adds them in GitHub Settings.

## Agent Capabilities

- Tool and function calling through Makefile targets.
- Registry-based planning and routing.
- State JSON artifacts for memory and auditability.
- Retry limits and fallback agent metadata.
- Validation after execution.
- Human-in-the-loop PR review before merge.

## Free Options

Free-safe operation relies on GitHub Actions for public repositories, GitHub Pages, the built-in `GITHUB_TOKEN`, public standards sources, and optional no-payment API tokens for higher rate limits. Provider APIs that require credits or billing are documented as optional and must stay disabled unless the owner explicitly enables them.
