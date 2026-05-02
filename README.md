# SIGMA — Unified Global Standards Index

**Free. Complete. Machine-readable. Human-navigable.**

[![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)](LICENSE)
[![Entries](https://img.shields.io/badge/entries-88%2C114-brightgreen)](#current-data-scope)
[![Domains](https://img.shields.io/badge/domains-40-blue)](data/reference/domain_taxonomy.csv)
[![Quality Gate](https://img.shields.io/badge/quality%20gate-active-1f5f4b)](docs/QUALITY_GATE.md)
[![Roadmap](https://img.shields.io/badge/roadmap-to%20100%25-c58b2b)](docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md)

SIGMA is an open project to build the world’s most complete public index of global standards, treaties, frameworks, guidelines, and classification systems.

## Repository Contents

- `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md` — full strategy and execution plan (v1.1 enhanced roadmap).
- `docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md` — detailed remaining-work roadmap from the current MVP toward a complete v1.0 global standards index.
- `index.md` — lightweight public landing-page copy.
- `data/raw/iso/ICS.csv` — ISO International Classification for Standards seed data.
- `data/raw/iso/iso_deliverables_metadata.csv` — ISO deliverables metadata.
- `data/raw/iso/iso_technical_committees.csv` — ISO technical committee seed data.
- `SCHEMA.md` — data schema documentation.
- `CONTRIBUTING.md` — contribution guidelines.
- `CODE_OF_CONDUCT.md` — code of conduct.
- `pyproject.toml` — Python project configuration.
- `scripts/` — data processing scripts.
- `data/reference/domain_taxonomy.csv` — canonical 40-domain registry.
- `data/reference/source_registry.csv` — source map for all 40 domains.
- `data/reports/domain_coverage.csv` — generated coverage report.
- `docs/PROJECT_KNOWLEDGE_GRAPH.md` — maintainer-oriented map of source-of-truth documents, generated artifacts, and pipeline relationships.
- `docs/SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.md` — external feedback gap analysis incorporated into the roadmap and task matrix.
- `data/relationships/relationships_template.csv` — relationship map template for graph edges.
- `.github/` — GitHub configuration (issues, workflows).

## Current Data Scope

- Generated release bundle: **88,114 master entries** and **20,130 relationship edges** after the Phase 8A national standards body registry slice.
- All **40 canonical domains** are represented through bulk ingestors and curated seed records.
- Current processed sources include ISO metadata, IETF RFC metadata, ILO standards, Wikidata standards-body metadata, Google Sheet curation, Phase 2A WHO/Sphere health priority records, Phase 2B Codex food-safety records, Phase 2C humanitarian standards records, and Phase 8A national standards body records.
- Raw ISO technical committees and ICS seed datasets are included in `data/raw/iso/`.
- Additional sources (UN, WHO, Codex, ITU, W3C, national bodies, etc.) remain planned in phased ingestion.

## Sample Records

| SIGMA ID | Name | Domain | Mandate | Why it matters |
|---|---|---|---|---|
| `HL-WHO-IHR-2005` | International Health Regulations | Health & Medical | Treaty-binding | Core legally binding framework for preventing and responding to cross-border public health risks. |
| `FS-CAC-CXG2-1985` | Guidelines on Nutrition Labelling | Food Safety & Agriculture | Voluntary-with-regulatory-adoption | International guidance for nutrition declarations and related food labelling information. |
| `RFC-9110` | HTTP Semantics | ICT | Voluntary-with-regulatory-adoption | Foundation for interoperable web communication and API semantics. |
| `ILO-C087` | Freedom of Association and Protection of the Right to Organise Convention | Labour & Employment | Treaty-binding | One of the core international labour rights instruments. |
| `NSB-ANSI-USA` | American National Standards Institute | National Standards Body Registry | Standards body | Key national standards body and ISO member for the United States. |

## Setup

1. Create a virtual environment: `python3 -m venv venv`
2. Activate it: `source venv/bin/activate`
3. Install dependencies: `pip install -e .`

## Validation

- Master entry schema: `python3 scripts/validate_schema.py data/processed`
- Relationship maps: `python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed`
- Deterministic release quality gate: `python3 scripts/build_quality_gate.py`
- Full local check: `make validate`

## Relationship Extraction

Generate high-confidence relationship edges:

```bash
python3 scripts/extract_relationships.py
python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed
```

Or run `make relationships`.

## Release Build

Build downloadable artifacts in `dist/`:

```bash
make release
```

The release build currently emits:

- `sigma_master.csv`
- `sigma_master.json`
- `sigma_master.jsonl`
- `relationships.csv`
- `relationships.json`
- `api_index.json`
- `domain_taxonomy.csv`
- `source_registry.csv`
- `domain_coverage.csv`
- `quality_gate.csv`

`dist/` is ignored by Git because release artifacts are generated outputs.

## Google Sheet Sync

The public curation sheet `000_SIGMA_MASTER_DATABASE` can be synchronized into the processed data layer:

```bash
make sync-google-sheet
```

The sync reads the public CSV export, keeps the 22-field SIGMA master schema, and writes `data/processed/google_sheet_master.csv`. Sheet-only curation metadata such as `related_sigma_ids`, `llm_enriched`, and `last_updated` is ignored by the release bundle until those fields are formally added to the published schema.

## Phase 2A Health Priority Ingestion

The first Life Sciences & Health priority ingestor transforms source-confirmed WHO/Sphere/WASH records into the processed data layer:

```bash
make health-priority
```

The curated source table is `data/reference/health_priority_sources.csv`, and the generated canonical output is `data/processed/health_priority_standards.csv`. This slice expands Domain 1 Health & Medical, Domain 33 Water, Sanitation & Hygiene, and related humanitarian WASH coverage without duplicating the original seed IDs.

## Phase 2B Codex Priority Ingestion

The first Codex Alimentarius ingestor transforms source-confirmed food-safety records into the processed data layer:

```bash
make codex
```

The curated source table is `data/reference/codex_priority_sources.csv`, and the generated canonical output is `data/processed/codex_standards.csv`. This slice expands Domain 2 Food Safety & Agriculture with cross-cutting Codex hygiene, additive, contaminant, labelling, analysis, sampling, and import/export inspection records.

## Phase 2C Humanitarian Standards Expansion

The humanitarian priority ingestor extends Domain 17 beyond Sphere WASH:

```bash
make humanitarian-priority
```

The curated source table is `data/reference/humanitarian_priority_sources.csv`, and the generated canonical output is `data/processed/humanitarian_priority_standards.csv`. This slice adds CHS, INEE, IASC, UNHCR, and WHO Emergency Medical Teams standards and guidance.

## Phase 2D WHO IRIS/OAI Staging

The WHO IRIS harvester stages likely normative WHO metadata for curator review before publication:

```bash
make who-iris-stage
```

The deterministic fixture is `data/reference/who_iris_oai_sample.xml`, and the staged output is `data/staging/who_iris_filtered_metadata.csv`. Staged rows are deliberately excluded from the release bundle until a curator promotes them into `data/processed`.

## Phase 8A National Standards Body Registry

The first national standards body registry slice transforms source-confirmed ISO member-body records into the processed data layer:

```bash
make national-standards-bodies
```

The curated source table is `data/reference/national_standards_bodies_sources.csv`, and the generated canonical output is `data/processed/national_standards_bodies.csv`. This initial slice covers 10 high-impact ISO member bodies and establishes the pattern for expanding toward the full ISO national body network.

## Research Task Matrix

The 24-month research plan is tracked as machine-readable work items in `data/reference/research_tasks.csv`. Run:

```bash
make research-tasks
```

This generates `data/reports/research_task_coverage.csv` and `docs/RESEARCH_TASKS.md`, covering all 40 domains, all major phases, and the enhanced integration roadmap.

## Roadmap to 100 Percent

The remaining work toward the complete global standards index is documented in `docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md`. It follows the canonical Phase 0 through Phase 9 research plan, then extends into the enhanced graph, API, automation, multilingual, and sustainability roadmap.

The friend-reviewed gap analysis is preserved in `docs/SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.md`. Its actionable recommendations have been converted into roadmap checkpoints and machine-readable research tasks.

## Contribute Without Coding

Non-technical contributors can propose corrections, missing standards, or new source families through GitHub Issues. Use the issue templates for new entries and corrections, and include an official source URL for every claim.

## Project Owner and Contact

The project owner and lead curator is **Mohammad Ariful Islam**. For public questions, corrections, missing sources, or contribution proposals, open an issue at `https://github.com/sigma-standards/sigma-index/issues`.

## Phase 9A Quality Gate

The first release quality gate performs deterministic checks that are safe for local and CI runs:

```bash
make quality-gate
```

It writes `data/reports/quality_gate.csv` and `docs/QUALITY_GATE.md`, covering duplicate `sigma_id` values, missing required master-schema fields, and malformed `official_url` values. Live URL reachability remains a separate audit step because source sites can rate-limit, redirect, or block automated requests.

## Publishing

GitHub Actions includes:

- Schema validation on pull requests and main-branch pushes.
- Release artifact build/upload on main-branch pushes.
- GitHub Pages publishing for a designed static site, generated data downloads, source registry, domain coverage, and project documentation.

Enable Pages in repository settings with **GitHub Actions** as the source, then run the `Publish Pages` workflow.

Build the same site locally after creating release artifacts:

```bash
make release
python3 scripts/build_static_site.py
```

The local and remote Pages builds use the same script so navigation, downloads, documentation links, and all-domain coverage stay synchronized.

## Enhancement Focus Added (May 2026)

The plan now explicitly includes:

- Hybrid architecture (tabular + knowledge graph).
- Automated freshness pipelines for daily/weekly source sync.
- LLM-assisted enrichment and validation workflows.
- Multilingual, accessibility, API, and improved UX roadmap.
- Governance/partnership strategy for long-term sustainability.

## Airtable / MCP Note

No Airtable MCP server is required for the current build. The project plan uses free/open collaboration paths: Google Sheets for early curation and NocoDB as the Airtable-style open-source option if a database UI is needed.

## Contributing

1. Open an issue with a source-backed addition/correction.
2. Submit a pull request with schema-compliant updates.
3. Include source URLs for all added or changed records.

## License

- Data and documentation: **CC BY 4.0** (see `LICENSE`).
