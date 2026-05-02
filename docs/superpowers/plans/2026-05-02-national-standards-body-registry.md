# Phase 8A National Standards Body Registry Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the first source-backed national standards body registry slice to the SIGMA processed data layer.

**Architecture:** Use the existing curated CSV to processed CSV ingestion pattern. Keep the source table richer than the master schema, then transform rows into `Standards Body` master records.

**Tech Stack:** Python standard library, CSV, pytest, Makefile release pipeline.

---

### Task 1: Add Failing Tests

**Files:**
- Create: `tests/test_process_national_standards_bodies.py`

- [ ] **Step 1: Write the failing processor tests**

Verify that the processor writes master-schema records, includes representative bodies, uses unique `NSB-` identifiers, and links ISO member profiles.

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_process_national_standards_bodies.py -q`

Expected: FAIL with `ModuleNotFoundError` for `scripts.process_national_standards_bodies`.

### Task 2: Add Source Table and Processor

**Files:**
- Create: `data/reference/national_standards_bodies_sources.csv`
- Create: `scripts/process_national_standards_bodies.py`

- [ ] **Step 1: Add curated source rows**

Add 10 representative ISO member-body rows with official organization URLs and ISO member-profile URLs.

- [ ] **Step 2: Add the processor**

Create `process_national_standards_bodies(repo_root, source_path=None, output_path=None)` that validates the source rows and writes `data/processed/national_standards_bodies.csv`.

- [ ] **Step 3: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_process_national_standards_bodies.py -q`

Expected: PASS.

### Task 3: Wire Validation and Documentation

**Files:**
- Modify: `Makefile`
- Modify: `README.md`
- Modify: `index.md`
- Modify: `data/reference/research_tasks.csv`
- Modify: `data/reference/source_registry.csv`

- [ ] **Step 1: Add Makefile target**

Add `national-standards-bodies` and run the processor during `make validate`.

- [ ] **Step 2: Document Phase 8A**

Document the source table, processed output, and limited first-slice scope.

- [ ] **Step 3: Verify release**

Run: `.venv/bin/python -m pytest -q`

Run: `make site`

Expected: all tests pass and the release build includes at least 88,114 entries.
