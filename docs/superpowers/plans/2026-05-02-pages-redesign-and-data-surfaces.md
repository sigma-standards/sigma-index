# Pages Redesign And Data Surfaces Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a polished, dependency-free GitHub Pages site that renders SIGMA downloads, documentation, domain coverage, source registry, and synchronization status from the current data bundle.

**Architecture:** Add `scripts/build_static_site.py` as the single site generation entry point. Update the Pages workflow to call that script instead of embedding HTML inside YAML. Cover the generated output with pytest tests using temporary fixture data.

**Tech Stack:** Python standard library, CSV/JSON readers, pytest, GitHub Actions Pages.

---

### Task 1: Site Builder Tests

**Files:**
- Create: `tests/test_build_static_site.py`

- [ ] **Step 1: Write failing tests**

Create pytest coverage that builds fixture `dist/` and `data/reference/` files, calls `build_static_site.build_site()`, and asserts that the output contains navigation, metrics, domain rows, source links, and copied downloads/docs.

- [ ] **Step 2: Run red test**

Run: `pytest tests/test_build_static_site.py -q`

Expected: FAIL because `scripts.build_static_site` does not exist yet.

### Task 2: Static Site Generator

**Files:**
- Create: `scripts/build_static_site.py`

- [ ] **Step 1: Implement the generator**

Read `dist/api_index.json`, `dist/domain_coverage.csv`, `data/reference/domain_taxonomy.csv`, and `data/reference/source_registry.csv`. Write `public/index.html`, `public/assets/styles.css`, `public/downloads/*`, and `public/docs/*`.

- [ ] **Step 2: Run green test**

Run: `pytest tests/test_build_static_site.py -q`

Expected: PASS.

### Task 3: GitHub Pages Workflow

**Files:**
- Modify: `.github/workflows/pages.yml`

- [ ] **Step 1: Replace inline HTML generation**

Keep release-data commands intact, then call `python3 scripts/build_static_site.py` in the static site build step.

- [ ] **Step 2: Run validation**

Run: `make validate`

Expected: PASS.

Run: `python3 scripts/build_static_site.py`

Expected: PASS and creates `public/index.html`.

### Task 4: Documentation Links

**Files:**
- Modify: `README.md`
- Modify: `index.md`

- [ ] **Step 1: Document the improved Pages output**

Mention the generated Pages site, local build command, and synchronized downloads/docs.

- [ ] **Step 2: Verify release build**

Run: `make release`

Expected: PASS and regenerates `dist/`.

### Task 5: Publish

**Files:**
- Commit all intended files.

- [ ] **Step 1: Inspect diff**

Run: `git status -sb` and `git diff --stat`.

- [ ] **Step 2: Commit and push**

Run: `git add ...`, `git commit -m "feat: redesign pages data surfaces"`, and `git push origin main`.

Expected: Push succeeds and GitHub Actions republishes Pages from `main`.
