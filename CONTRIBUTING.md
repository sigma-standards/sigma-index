# Contributing to SIGMA — Unified Global Standards Index

Thank you for your interest in contributing to SIGMA — the world's first free unified index of global standards, treaties, frameworks, and guidelines.

**SIGMA needs you.** Currently 28 of 40 domains have only 1 seeded entry. Every expert who knows a standard is missing can make a real difference.

---

## 🌐 Contribute Without Coding

**You do NOT need GitHub, Python, or coding skills to contribute.**

### Option 1 — Google Sheet (Easiest)

The curation sheet `000_SIGMA_MASTER_DATABASE` accepts new entries from anyone:
👉 **[Open the SIGMA Curation Sheet](https://docs.google.com/spreadsheets/d/12B83jPjlKSbk9QX8IQjAJylqwby8puiwabHwHoFBj0Q/edit?usp=sharing)**

Add a new row following the 22-column schema. The project maintainer reviews new rows weekly and imports them into the processed data layer.

**Columns to fill (minimum for a valid entry):**
- `sigma_id` — format: `[DOMAIN_CODE]-[ISSUER]-[STD_NUMBER]-[YEAR]` (e.g., `HL-WHO-IHR-2005`)
- `entry_type` — Standard / Framework / Treaty / Guideline / Regulation / Standards Body
- `domain` — from the 40-domain taxonomy (see `data/reference/domain_taxonomy.csv`)
- `name_full` — complete official name
- `issuer` — issuing organisation
- `official_url` — primary authoritative source URL (not Wikipedia)
- `why_it_matters` — 1–3 sentences in plain language explaining who uses this and why

### Option 2 — GitHub Issue Form

Use the pre-filled issue forms — no coding needed:

| Task | Form |
|------|------|
| Report a missing standard | [Missing Standard](https://github.com/sigma-standards/sigma-index/issues/new?template=missing_standard.yml) |
| Report an error in existing data | [Source Correction](https://github.com/sigma-standards/sigma-index/issues/new?template=source_correction.yml) |
| Report a broken URL | [Broken Link](https://github.com/sigma-standards/sigma-index/issues/new?template=broken_link.yml) |
| Propose a new data source | [Domain Expansion](https://github.com/sigma-standards/sigma-index/issues/new?template=domain_expansion.yml) |
| Report a duplicate entry | [Duplicate Report](https://github.com/sigma-standards/sigma-index/issues/new?template=duplicate_report.yml) |

### Option 3 — Email

Not on GitHub? Email the project owner at the contact listed in README.md with:
- Standard name + official identifier
- Issuing body
- Official URL
- Why it should be included (1–2 sentences)

---

## 🖥️ Contribute with Code (Technical Path)

### Setup

```bash
git clone https://github.com/sigma-standards/sigma-index.git
cd sigma-index
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
make validate   # Confirm everything passes before changing anything
```

### Workflow

```bash
git checkout -b feature/my-contribution
# Make your changes
make validate   # Must pass before submitting PR
git add .
git commit -m "feat: add X to domain Y"
git push origin feature/my-contribution
# Open PR on GitHub
```

### Adding New Entries (CSV path)

1. Identify the correct processed file in `data/processed/` for your domain
2. Add rows following the 22-field SIGMA schema (see `SCHEMA.md`)
3. Assign a SIGMA ID: `[DOMAIN_CODE]-[ISSUER]-[STD_NUMBER]-[YEAR]`
4. Populate ALL mandatory fields: `sigma_id`, `entry_type`, `meta_layer`, `domain`, `name_full`, `issuer`, `official_url`, `why_it_matters`
5. Set `data_source` to describe where you got the data (specific URL or database)
6. Run `make validate` — must pass with 0 errors

### Adding a New Domain Ingestor (Python path)

1. Read `AGENTS.md` and `scripts/run_domain_worker.py`
2. Create `scripts/process_[domain]_priority.py` following existing patterns
3. Create `data/reference/[domain]_priority_sources.csv` as input table
4. Add Makefile target following the existing pattern
5. Register the agent in `data/reference/domain_worker_registry.csv`
6. Run the new target: `make [domain]-priority`
7. Run `make validate` — must pass
8. Submit PR with both the script and generated `data/processed/` output

### Code Style

- Python 3.8+ compatible
- Follow PEP 8
- Add docstrings to all functions
- Add a test in `tests/` for any new processing logic
- Run: `python -m pytest` before submitting

---

## 📋 Schema Quick Reference

| Field | Type | Required | Example |
|-------|------|----------|---------|
| `sigma_id` | String | ✅ | `HL-ISO-15189-2022` |
| `entry_type` | Enum | ✅ | `Standard` |
| `meta_layer` | Enum | ✅ | `L1 Life Sciences` |
| `domain` | String | ✅ | `Health & Medical` |
| `sub_domain` | String | — | `Clinical Laboratories` |
| `name_full` | String | ✅ | Full official title |
| `name_short` | String | — | `ISO 15189` |
| `standard_id` | String | — | `ISO 15189:2022` |
| `issuer` | String | ✅ | `ISO (TC 212)` |
| `issuer_type` | Enum | — | `ISO` |
| `governance_layer` | Enum | — | `International` |
| `geographic_scope` | String | — | `Global` |
| `year_published` | Integer | — | `2022` |
| `year_first` | Integer | — | `2003` |
| `status` | Enum | ✅ | `Active` |
| `mandate` | Enum | — | `Voluntary` |
| `sector_applicability` | String | — | `Healthcare / regulators` |
| `why_it_matters` | String | ✅ | Plain-language significance |
| `key_outputs` | String | — | Key versions / elements |
| `official_url` | URL | ✅ | Authoritative primary URL |
| `data_source` | String | ✅ | Where data came from |
| `notes` | String | — | Additional context |

**Mandate values:** `Mandatory` / `Voluntary` / `Voluntary-with-regulatory-adoption` / `Treaty-binding`

Full schema documentation: [SCHEMA.md](SCHEMA.md)

---

## 🔑 Quality Rules

Every PR must pass `make validate` (0 errors):
- No duplicate `sigma_id` values
- All mandatory fields populated (no blank required cells)
- All `official_url` values start with `http`
- Domain codes match the canonical 40-domain taxonomy
- Relationship edges have `from_id`, `to_id`, `relationship_type`, `confidence`, `source_url`

**Source requirement:** Every entry must have an authoritative primary source URL in `official_url`. Wikipedia, news articles, and secondary references are not acceptable as the sole source.

---

## 🏆 Highest-Priority Contributions Right Now

These 8 domains have only 1 entry each and are marked `critical` priority:

| Domain | Code | Key Missing Standards |
|--------|------|-----------------------|
| Human Rights | HR | ICCPR, ICESCR, CEDAW, CRC, CRPD, CAT, CMW, CERD |
| Finance, Banking & Accounting | FB | Basel III, FATF 40 Recs, IFRS 1–17, IOSCO Principles |
| Environment & Climate | EC | Paris Agreement, UNFCCC, CBD, Montreal Protocol |
| Transport | TR | SOLAS, MARPOL, ICAO Annexes 1–19, UNECE WP.29 |
| Extractive Industries | EX | EITI Standard, ICMM Principles, Kimberly Process |
| Disaster Risk | DR | Sendai Framework, ISO 22301 family |
| Biodiversity & Conservation | BC | CBD, CITES Appendices, IUCN Red List Criteria |
| Marine & Ocean | MO | UNCLOS, IMO conventions, Regional Seas |

---

## 📜 License

By contributing, you agree to license your contributions under **CC BY 4.0**.
All contributions must be based on publicly available, authoritative sources.
Do not contribute content that reproduces full copyrighted standard texts.

---

## 📬 Questions?

Open an issue: https://github.com/sigma-standards/sigma-index/issues
Project owner: **Mohammad Ariful Islam** — CPI Bangladesh Mission