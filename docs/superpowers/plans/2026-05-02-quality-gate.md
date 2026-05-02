# Phase 9A Quality Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add deterministic release quality-gate reports to the SIGMA validation and release pipeline.

**Architecture:** Scan processed master-schema CSV files, compute critical release checks, and emit CSV plus Markdown reports. Keep live URL reachability outside the gate so CI remains stable.

**Tech Stack:** Python standard library, CSV, pytest, Makefile release pipeline.

---

### Task 1: Add Failing Tests

**Files:**
- Create: `tests/test_build_quality_gate.py`

- [ ] **Step 1: Write clean-data test**

Create a temporary processed CSV and assert the generated report contains pass rows for duplicate IDs, required fields, and URL shape.

- [ ] **Step 2: Write failing-data test**

Create a temporary processed CSV with a duplicate ID, missing issuer, and malformed URL. Assert the generated report marks each check as failed.

- [ ] **Step 3: Verify red state**

Run: `.venv/bin/python -m pytest tests/test_build_quality_gate.py -q`

Expected: FAIL with `ModuleNotFoundError` for `scripts.build_quality_gate`.

### Task 2: Implement Quality Gate

**Files:**
- Create: `scripts/build_quality_gate.py`

- [ ] **Step 1: Add processed-row reader**

Read `data/processed/*.csv` files that contain `sigma_id`.

- [ ] **Step 2: Add checks**

Compute duplicate `sigma_id` values, missing required fields, and non-HTTP `official_url` values.

- [ ] **Step 3: Write reports**

Write `data/reports/quality_gate.csv` and `docs/QUALITY_GATE.md`.

- [ ] **Step 4: Verify green state**

Run: `.venv/bin/python -m pytest tests/test_build_quality_gate.py -q`

Expected: PASS.

### Task 3: Wire Release Pipeline

**Files:**
- Modify: `Makefile`
- Modify: `scripts/build_release.py`
- Modify: `README.md`
- Modify: `index.md`
- Modify: `data/reference/research_tasks.csv`

- [ ] **Step 1: Add Makefile target**

Add `quality-gate` and run `scripts/build_quality_gate.py` during `make validate`.

- [ ] **Step 2: Copy report into release artifacts**

Add `quality_gate.csv` to the reports copied by `scripts/build_release.py`.

- [ ] **Step 3: Document Phase 9A**

Document the deterministic quality gate and why live URL checks remain separate.

- [ ] **Step 4: Verify release**

Run: `.venv/bin/python -m pytest -q`

Run: `make site`

Expected: all tests pass and `dist/quality_gate.csv` is generated.
