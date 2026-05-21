# HDX Publication Checklist

**Target:** Publish SIGMA master dataset and metadata to [Humanitarian Data Exchange](https://data.humdata.org/)

---

## Overview

The Humanitarian Data Exchange (HDX) is operated by the UN Office for the Coordination of Humanitarian Affairs (OCHA). It is the primary platform for humanitarian datasets and is widely used by NGOs, humanitarian response teams, and development organizations.

Publishing SIGMA to HDX expands access to humanitarian professionals, practitioners, and researchers who rely on HDX as their primary data discovery platform.

---

## Pre-Publication Requirements

### 1. Dataset Preparation
- [ ] Generate final release artifacts:
  ```bash
  make release
  ```
- [ ] Verify all required files exist in `dist/`:
  - [ ] `sigma_master.csv` (all entries)
  - [ ] `sigma_master.json` (structured format)
  - [ ] `sigma_master.jsonl` (newline-delimited)
  - [ ] `relationships.csv` (relationship edges)
  - [ ] `domain_taxonomy.csv` (domain reference)
  - [ ] `source_registry.csv` (source metadata)
  - [ ] `quality_gate.csv` (quality metrics)

### 2. Metadata Preparation
- [ ] Prepare dataset metadata in HDX-compatible format
- [ ] Title: "SIGMA - Unified Global Standards Index"
- [ ] Organization: "sigma-standards"
- [ ] Dataset date: [today's date]
- [ ] Update frequency: "Monthly"
- [ ] License: "CC BY 4.0 (Attribution required)"

### 3. Quality Assurance
- [ ] Run full validation:
  ```bash
  make validate
  python3 -m pytest -v
  ```
- [ ] Check URL health (sample):
  ```bash
  python3 scripts/check_urls.py --sample 100
  ```
- [ ] Confirm no duplicate sigma_ids
- [ ] Verify all mandatory fields are populated
- [ ] Test download links are accessible

### 4. Documentation
- [ ] Prepare README for HDX dataset
- [ ] Prepare schema guide for HDX users

---

## HDX Publication Steps

### Step 1: Create HDX Organization Account
- [ ] Go to https://data.humdata.org/
- [ ] Sign up or log in
- [ ] Create organization: `SIGMA Standards`
- [ ] Add team members with contributor permissions

### Step 2: Create Dataset on HDX
- [ ] Click "Create dataset"
- [ ] Fill in metadata:
  - [ ] Title: "SIGMA - Unified Global Standards Index"
  - [ ] Organization: SIGMA Standards
  - [ ] Dataset date: [release date]
  - [ ] Visibility: Public

### Step 3: Upload Resources
- [ ] Add resource: SIGMA Master Index (CSV)
- [ ] Add resource: SIGMA Master Index (JSON)
- [ ] Add resource: Relationship Graph
- [ ] Add resource: Domain Taxonomy
- [ ] Add resource: Source Registry

### Step 4: Add Documentation
- [ ] Add resource: README (PDF or Word)
- [ ] Add resource: Schema Guide

### Step 5: Link GitHub Release
- [ ] In dataset metadata, add reference to GitHub release

### Step 6: Review & Publish
- [ ] Review all metadata and resources
- [ ] Confirm visibility is "Public"
- [ ] Publish dataset

---

## Post-Publication

### Step 1: Verify Visibility
- [ ] Search for "SIGMA" on HDX
- [ ] Confirm dataset appears in results
- [ ] Verify all download links work

### Step 2: Update SIGMA Documentation
- [ ] Add HDX dataset link to README.md
- [ ] Add HDX link to GitHub Pages site

### Step 3: Update Dataset Regularly
- [ ] After each monthly release, update HDX resources

### Step 4: Monitor & Engage
- [ ] Monitor HDX views/downloads
- [ ] Respond to any HDX user comments

---

## Reference

- **HDX Documentation:** https://data.humdata.org/
- **HDX API:** https://data.humdata.org/api/
