# GitHub Domain Agents Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a free-safe GitHub multi-agent scaffold for domain workers, optional API secrets, validation, state artifacts, and pull-request review gates.

**Architecture:** Domain workers are declared in a CSV registry and executed by a single Python runner that delegates to Makefile targets. GitHub Actions orchestrates manual and scheduled workers, uploads state artifacts, validates output, and opens PRs instead of committing directly to `main`.

**Tech Stack:** GitHub Actions, GitHub CLI, Python standard library, Makefile, pytest.

---

### Task 1: Domain Agent Registry

**Files:**
- Create: `data/reference/domain_worker_registry.csv`
- Test: `tests/test_domain_agent_registry.py`

- [x] **Step 1: Write the failing registry test**

Test that the registry includes at least eight domain agents, requires human review, blocks direct writes to `main`, and declares retry limits.

- [x] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_domain_agent_registry.py -q`

Expected: fails because the registry does not exist.

- [x] **Step 3: Add the registry**

Create `data/reference/domain_worker_registry.csv` with one row per SIGMA domain worker and columns for command routing, outputs, optional secrets, retries, fallbacks, and safety flags.

- [x] **Step 4: Run the registry test**

Run: `.venv/bin/python -m pytest tests/test_domain_agent_registry.py -q`

Expected: registry assertions pass once the runner and workflow files exist.

### Task 2: Domain Agent Runner

**Files:**
- Create: `scripts/run_domain_worker.py`
- Test: `tests/test_domain_agent_registry.py`

- [x] **Step 1: Write the failing runner dry-run test**

Test that `scripts/run_domain_worker.py --agent health --dry-run` writes JSON state and prints the planned Makefile command.

- [x] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_domain_agent_registry.py -q`

Expected: fails because the runner does not exist.

- [x] **Step 3: Add the runner**

Implement CSV loading, known-agent validation, state writing, dry-run output, safety refusal for direct-main writers, and retry execution.

- [x] **Step 4: Run the runner test**

Run: `.venv/bin/python -m pytest tests/test_domain_agent_registry.py::test_domain_agent_runner_dry_run_writes_state_report -q`

Expected: pass.

### Task 3: GitHub Workflow

**Files:**
- Create: `.github/workflows/domain_agents.yml`
- Test: `tests/test_domain_agent_registry.py`

- [x] **Step 1: Write the failing workflow test**

Test for manual dispatch, scheduled runs, least needed write permissions, runner invocation, PR creation, and secret references by name only.

- [x] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_domain_agent_registry.py -q`

Expected: fails because the workflow does not exist.

- [x] **Step 3: Add the workflow**

Create a matrix workflow that selects a domain agent, runs dry-run or execute mode, validates output, uploads state, and creates a PR through `gh pr create` when files change.

- [x] **Step 4: Run workflow tests**

Run: `.venv/bin/python -m pytest tests/test_domain_agent_registry.py -q`

Expected: pass.

### Task 4: Setup Documentation

**Files:**
- Create: `docs/GITHUB_AGENTIC_SETUP_GUIDE.md`
- Create: `docs/superpowers/specs/2026-05-04-github-domain-agents-design.md`
- Create: `docs/superpowers/plans/2026-05-04-github-domain-agents-implementation.md`
- Test: `tests/test_domain_agent_registry.py`

- [x] **Step 1: Write the failing guide test**

Test that the guide includes a fillable template for the requested secret names and click-by-click GitHub setup instructions.

- [x] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_domain_agent_registry.py -q`

Expected: fails because the guide does not exist.

- [x] **Step 3: Add docs**

Write the setup guide, design doc, and implementation plan with no real secrets.

- [x] **Step 4: Run docs tests**

Run: `.venv/bin/python -m pytest tests/test_domain_agent_registry.py -q`

Expected: pass.
