# Phase 2B Codex Priority Ingestion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a curated Codex Alimentarius priority ingestor for Food Safety & Agriculture.

**Architecture:** Keep source-confirmed Codex records in a reviewable reference CSV, process them with a deterministic Python script, and include the processed output in the existing release pipeline. Tests are written first and verify schema, domain coverage, and duplicate avoidance.

**Tech Stack:** Python standard library, CSV master schema, pytest, Makefile release pipeline.

---

### Task 1: Add Failing Codex Tests

**Files:**
- Create: `tests/test_process_codex.py`
- Expect missing: `scripts/process_codex.py`
- Expect missing: `data/reference/codex_priority_sources.csv`

- [ ] **Step 1: Write the failing tests**

```python
import csv
from pathlib import Path


MASTER_FIELDS = [
    "sigma_id",
    "entry_type",
    "meta_layer",
    "domain",
    "sub_domain",
    "name_full",
    "name_short",
    "standard_id",
    "issuer",
    "issuer_type",
    "governance_layer",
    "geographic_scope",
    "year_published",
    "year_first",
    "status",
    "mandate",
    "sector_applicability",
    "why_it_matters",
    "key_outputs",
    "official_url",
    "data_source",
    "notes",
]


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def test_process_codex_writes_schema_and_food_safety_records(tmp_path):
    from scripts.process_codex import process_codex

    output_path = process_codex(Path("."), output_path=tmp_path / "codex.csv")

    rows = read_rows(output_path)
    assert output_path.exists()
    assert len(rows) >= 8
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert {row["domain"] for row in rows} == {"Food Safety & Agriculture"}
    assert {"Standard", "Guideline", "Code of Practice"} <= {row["entry_type"] for row in rows}
    assert all(row["issuer"] == "Codex Alimentarius Commission" for row in rows)
    assert all(row["official_url"].startswith("https://") for row in rows)


def test_codex_ids_do_not_duplicate_domain_seed_ids(tmp_path):
    from scripts.process_codex import process_codex

    output_path = process_codex(Path("."), output_path=tmp_path / "codex.csv")
    codex_ids = {row["sigma_id"] for row in read_rows(output_path)}
    seed_ids = {row["sigma_id"] for row in read_rows(Path("data/processed/domain_seed_standards.csv"))}

    assert codex_ids.isdisjoint(seed_ids)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_process_codex.py -q`

Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.process_codex'`.

### Task 2: Add Source Table and Processor

**Files:**
- Create: `data/reference/codex_priority_sources.csv`
- Create: `scripts/process_codex.py`
- Modify: `Makefile`

- [ ] **Step 1: Add source-confirmed Codex rows**

Create a master-schema CSV for initial cross-cutting Codex standards and guidelines.

- [ ] **Step 2: Add processor**

Create `process_codex(repo_root, source_path=None, output_path=None)` that reads, validates, sorts, and writes canonical Codex records.

- [ ] **Step 3: Wire Makefile**

Add `codex` and run `scripts/process_codex.py` during `make validate`.

- [ ] **Step 4: Verify tests pass**

Run: `.venv/bin/python -m pytest tests/test_process_codex.py -q`

Expected: PASS.

### Task 3: Release Integration and Documentation

**Files:**
- Modify: `README.md`
- Modify: `index.md`
- Modify: `data/reference/research_tasks.csv`
- Modify: `data/reference/source_registry.csv`

- [ ] **Step 1: Document the Codex ingestor**

Describe `make codex`, `data/reference/codex_priority_sources.csv`, and `data/processed/codex_standards.csv`.

- [ ] **Step 2: Mark Phase 2B active**

Add `P2B-CODEX` to the research task matrix and set Domain 2 source registry status to `phase2b_active`.

- [ ] **Step 3: Run verification**

Run: `.venv/bin/python -m pytest tests/test_process_codex.py tests/test_research_task_report.py -q`

Run: `make site`

Expected: both commands exit 0.

### Task 4: Commit and Publish

**Files:**
- All changed files from Tasks 1-3.

- [ ] **Step 1: Commit locally**

Run: `git add ... && git commit -m "feat: add codex priority ingestion"`

- [ ] **Step 2: Publish remotely**

Use the GitHub connector if direct git push is unavailable, then fetch and align local `main` with `origin/main`.

- [ ] **Step 3: Verify remote workflows**

Confirm Schema Validation, Release Build, Publish Pages, and Pages deployment complete successfully for the published commit.
