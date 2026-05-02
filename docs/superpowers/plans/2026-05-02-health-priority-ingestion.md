# Phase 2A Health Priority Ingestion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first curated Life Sciences & Health priority ingestor for WHO/Sphere/WASH standards.

**Architecture:** Store source-confirmed records in a reviewable reference CSV, transform them through a deterministic standard-library Python script, and emit a canonical processed CSV that joins the normal release build. Tests drive the ingestor before implementation.

**Tech Stack:** Python standard library, CSV master schema, pytest, Makefile release pipeline.

---

### Task 1: Add Failing Ingestor Tests

**Files:**
- Create: `tests/test_process_health_priority.py`
- Expect missing: `scripts/process_health_priority.py`
- Expect missing: `data/reference/health_priority_sources.csv`

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


def test_process_health_priority_writes_schema_and_priority_domains(tmp_path):
    from scripts.process_health_priority import process_health_priority

    output_path = process_health_priority(Path("."), output_path=tmp_path / "health_priority.csv")

    rows = read_rows(output_path)
    assert output_path.exists()
    assert rows
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert {"Health & Medical", "Water, Sanitation & Hygiene (WASH)"} <= {row["domain"] for row in rows}
    assert all(row["official_url"].startswith("https://") for row in rows)


def test_health_priority_ids_do_not_duplicate_domain_seed_ids(tmp_path):
    from scripts.process_health_priority import process_health_priority

    output_path = process_health_priority(Path("."), output_path=tmp_path / "health_priority.csv")
    priority_ids = {row["sigma_id"] for row in read_rows(output_path)}
    seed_ids = {row["sigma_id"] for row in read_rows(Path("data/processed/domain_seed_standards.csv"))}

    assert priority_ids.isdisjoint(seed_ids)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_process_health_priority.py -q`

Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.process_health_priority'`.

### Task 2: Implement Source Table and Ingestor

**Files:**
- Create: `data/reference/health_priority_sources.csv`
- Create: `scripts/process_health_priority.py`
- Modify: `Makefile`

- [ ] **Step 1: Add curated source rows**

Create `data/reference/health_priority_sources.csv` with master-schema headers and initial WHO/Sphere records.

- [ ] **Step 2: Add minimal ingestor**

Create `scripts/process_health_priority.py` with `process_health_priority(repo_root, source_path=None, output_path=None)` that reads source rows, checks required fields, rejects duplicate IDs, sorts by `sigma_id`, and writes the processed CSV.

- [ ] **Step 3: Add Makefile target**

Add `health-priority` and make `validate` run the ingestor before schema validation.

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_process_health_priority.py -q`

Expected: PASS.

### Task 3: Release Integration and Documentation

**Files:**
- Modify: `README.md`
- Modify: `index.md`
- Modify: `data/reference/research_tasks.csv`

- [ ] **Step 1: Document the new ingestion path**

Describe `make health-priority`, the source table, and generated processed output.

- [ ] **Step 2: Mark Phase 2A active in research tasks**

Add a health priority ingestion row for Domains 1/33 with status `active`.

- [ ] **Step 3: Run verification**

Run: `.venv/bin/python -m pytest tests/test_process_health_priority.py tests/test_research_task_report.py -q`

Run: `make site`

Expected: both commands exit 0.

### Task 4: Commit and Publish

**Files:**
- All changed files from Tasks 1-3.

- [ ] **Step 1: Commit locally**

Run: `git add ... && git commit -m "feat: add health priority ingestion"`

- [ ] **Step 2: Publish remotely**

Use the GitHub connector if direct git push is unavailable, update `main`, fetch it back, and align local `main` with `origin/main`.

- [ ] **Step 3: Verify remote workflows**

Check GitHub Actions for the published commit and confirm Schema Validation, Release Build, Publish Pages, and Pages deployment complete successfully.
