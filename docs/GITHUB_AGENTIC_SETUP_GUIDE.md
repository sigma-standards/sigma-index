# GitHub Agentic Setup Guide

This guide turns SIGMA into a GitHub-first, multi-agent project without depending on this local machine. The default setup is free-safe and deterministic: GitHub Actions runs domain workers, validates output, uploads artifacts, and opens pull requests for human review.

Do not paste secrets into commits, issues, pull requests, workflow logs, or chat. Add secrets only in GitHub repository settings: Settings -> Secrets and variables -> Actions.

## What The Setup Provides

- Domain-based agents declared in `data/reference/domain_worker_registry.csv`.
- A single runner, `scripts/run_domain_worker.py`, that executes one registered worker.
- GitHub workflows for agents: `.github/workflows/domain_agents.yml` for individual/manual/scheduled workers and `.github/workflows/agent_cycle.yml` for GitHub-web plan, run, and follow-up cycles.
- Human-in-the-loop PR gates instead of direct writes to `main`.
- Retry behavior through each registry row's `retry_limit`.
- State reports in `data/reports/domain_agent_state_<agent>.json`.
- Optional free/API-token integrations by secret name only.

## Fillable Secrets Template

Copy the value from each provider into GitHub Web. Leave blank when you do not have a token or when the provider requires payment.

| Secret name | Required | Free/payment note | Fill here before pasting into GitHub |
|---|---:|---|---|
| `XAI_API_KEY` | No | xAI/Grok API keys may require credits or billing; use only if you have a no-payment/free-credit option. | `________________________________` |
| `DEEPSEEK_API_KEY` | No | DeepSeek API is usage-priced in official pricing; use only if your account has free balance and no payment requirement. | `________________________________` |
| `NCBI_API_KEY` | No | Optional free NCBI key for higher E-utilities rate limits. | `________________________________` |
| `NCBI_USERNAME` | No | Optional NCBI account email/username; store as a secret if used. | `________________________________` |
| `APIFY_TOKEN` | No | Optional Apify token for Apify MCP/platform access; use only within free allowances. | `________________________________` |
| `HF_TOKEN` | No | Optional Hugging Face user access token; use read/fine-grained scope unless writes are truly needed. | `________________________________` |
| `OPENALEX_MAILTO` | No | Email string for polite OpenAlex API usage. | `________________________________` |
| `CROSSREF_MAILTO` | No | Email string for polite Crossref API usage. | `________________________________` |
| `NVD_API_KEY` | No | Optional free NVD key for higher rate limits. | `________________________________` |

## Fillable Variables Template

Use repository variables for non-secret configuration values.

| Variable name | Required | Note | Fill here before pasting into GitHub |
|---|---:|---|---|
| `APIFY_USER_ID` | No | Optional Apify user/account identifier. | `________________________________` |
| `SIGMA_BOT_NAME` | No | Optional commit author name for workflow-created PRs. | `________________________________` |
| `SIGMA_BOT_EMAIL` | No | Optional commit author email for workflow-created PRs. | `________________________________` |

## Click By Click: Repository Settings

1. Open `https://github.com/sigma-standards/sigma-index`.
2. Click `Settings`.
3. Click `Actions`.
4. Click `General`.
5. Under `Actions permissions`, choose `Allow all actions and reusable workflows` or restrict to the actions already used by this repo.
6. Under `Workflow permissions`, choose `Read and write permissions`.
7. Enable `Allow GitHub Actions to create and approve pull requests` when the option is visible.
8. Click `Save`.

## Click By Click: Add Secrets

1. Open the repository on GitHub.
2. Click `Settings`.
3. Click `Secrets and variables`.
4. Click `Actions`.
5. Click `New repository secret`.
6. In `Name`, paste one secret name exactly, for example `HF_TOKEN`.
7. In `Secret`, paste the token value.
8. Click `Add secret`.
9. Repeat for every secret you want to enable.

## Click By Click: Protect Main

1. Open the repository on GitHub.
2. Click `Settings`.
3. Click `Branches`.
4. Click `Add branch ruleset` or `Add branch protection rule`.
5. Set branch name pattern to `main`.
6. Enable `Require a pull request before merging`.
7. Enable `Require status checks to pass`.
8. Select checks such as `CI`, `Schema Validation`, `Release Build`, and `Domain Agents` after they have run at least once.
9. Enable `Block force pushes`.
10. Save the rule.

## Click By Click: Run A Domain Agent

1. Open the repository on GitHub.
2. Click `Actions`.
3. Click `Domain Agents`.
4. Click `Run workflow`.
5. Choose an `agent_id`, such as `health`, `ict`, `sports`, or `all`.
6. Keep `dry_run` enabled for the first run.
7. Click `Run workflow`.
8. Open the completed run and download the `domain-agent-state-*` artifact.
9. Run again with `dry_run` disabled only after the dry run looks right.
10. Review the PR created by the workflow before merging.

## Click By Click: Run The Agent Cycle

1. Open the repository on GitHub.
2. Click `Actions`.
3. Click `Agent Cycle`.
4. Click `Run workflow`.
5. Choose an `agent_id`, or choose `all`.
6. Choose `plan` first to upload state artifacts without changing data.
7. Choose `run` to execute, validate, optionally build release artifacts, and open a PR for review.
8. Choose `follow-up` to produce a web-run summary of recent cycle runs and open agent PRs.

## Agentic Design Coverage

- Tool and function calling: GitHub Actions calls `scripts/run_domain_worker.py`, which dispatches Makefile targets.
- Agent planning and orchestration: `domain_worker_registry.csv` declares agents, outputs, schedules, retries, and fallbacks.
- Memory and context management: the registry, setup guide, state JSON, docs, and GitHub artifacts preserve operating context.
- State machines and multi-step execution: workflow steps move through select, run, validate, upload state, create PR.
- Retry, fallback, and recovery: each agent declares `retry_limit` and `fallback_agent_id`; failed runs keep logs and artifacts.
- Agent evals and reliability testing: tests validate registry safety, workflow permissions, dry-run state, and secret-name-only behavior.
- Cost and latency optimization: deterministic Makefile jobs run first; paid/limited LLM APIs stay optional and disabled by default.
- Human-in-the-loop patterns: agents create pull requests and never write directly to `main`.

## Free-Safe Defaults

- Prefer GitHub's built-in `GITHUB_TOKEN` over personal tokens.
- Use public data APIs without keys when possible.
- Use optional free API keys only for higher rate limits.
- Avoid `pull_request_target` workflows for secret-bearing jobs.
- Keep generated `dist/`, `public/`, `.venv/`, caches, and logs out of commits.
