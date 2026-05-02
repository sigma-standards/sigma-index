# Phase 2C and 2D Humanitarian and WHO IRIS Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend Domain 17 humanitarian coverage and add a conservative WHO IRIS/OAI metadata staging pipeline.

**Architecture:** Phase 2C uses the existing curated CSV to processed CSV pattern. Phase 2D parses OAI-PMH Dublin Core XML into a staged review CSV and deliberately avoids adding unreviewed WHO records to the published release.

**Tech Stack:** Python standard library, CSV, XML ElementTree, pytest, Makefile release pipeline.

---

### Task 1: Add Failing Tests

**Files:**
- Create: `tests/test_process_humanitarian_priority.py`
- Create: `tests/test_harvest_who_iris.py`

- [ ] **Step 1: Write humanitarian processor tests**

Verify the processor writes master-schema Domain 17 records for CHS, INEE, IASC, UNHCR, and WHO EMT without duplicating the seed Sphere ID.

- [ ] **Step 2: Write WHO IRIS harvester tests**

Verify the harvester reads `data/reference/who_iris_oai_sample.xml`, includes normative guideline/classification records, excludes a general statistics report, and writes staging fields.

- [ ] **Step 3: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_process_humanitarian_priority.py tests/test_harvest_who_iris.py -q`

Expected: FAIL with missing modules.

### Task 2: Implement Phase 2C Humanitarian Ingestion

**Files:**
- Create: `data/reference/humanitarian_priority_sources.csv`
- Create: `scripts/process_humanitarian_priority.py`
- Modify: `Makefile`

- [ ] **Step 1: Add source-confirmed humanitarian rows**

Create a master-schema CSV for CHS, INEE, IASC MHPSS, UNHCR Emergency Handbook, and WHO EMT minimum standards.

- [ ] **Step 2: Add processor**

Create `process_humanitarian_priority(repo_root, source_path=None, output_path=None)` that reads, validates, sorts, and writes canonical records.

- [ ] **Step 3: Wire Makefile**

Add `humanitarian-priority` and run the processor during `make validate`.

### Task 3: Implement Phase 2D WHO IRIS Staging

**Files:**
- Create: `data/reference/who_iris_oai_sample.xml`
- Create: `scripts/harvest_who_iris.py`
- Modify: `Makefile`

- [ ] **Step 1: Add deterministic OAI fixture**

Include two normative WHO records and one excluded general report.

- [ ] **Step 2: Add harvester**

Parse OAI Dublin Core, apply allow-list filters, label record types, and write `data/staging/who_iris_filtered_metadata.csv`.

- [ ] **Step 3: Wire Makefile**

Add `who-iris-stage` and run it during `make validate` in fixture mode.

### Task 4: Documentation, Verification, and Publish

**Files:**
- Modify: `README.md`
- Modify: `index.md`
- Modify: `data/reference/research_tasks.csv`
- Modify: `data/reference/source_registry.csv`

- [ ] **Step 1: Document Phase 2C and 2D**

Describe the curated humanitarian output and WHO IRIS staging output.

- [ ] **Step 2: Verify**

Run: `.venv/bin/python -m pytest -q`

Run: `make site`

- [ ] **Step 3: Commit and publish**

Commit as `feat: expand humanitarian and who iris staging`, publish to GitHub, align local/remote, and verify Actions.
