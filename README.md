# SIGMA — Unified Global Standards Index

**Free. Complete. Machine-readable. Human-navigable.**

[![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)](LICENSE)
[![Entries](https://img.shields.io/badge/entries-88%2C203-brightgreen)](#current-data-scope)
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
- `docs/PROJECT_STATUS_REPORT_2026-05-02.md` — current journey summary, accomplishments, challenges, best practices, and next steps.
- `docs/GITHUB_AGENTIC_SETUP_GUIDE.md` — click-by-click GitHub setup guide for free-safe domain-agent automation and optional API secrets.
- `docs/OPERATOR_DASHBOARD.md` — maintainer dashboard for local, remote, workflow, and publishing operations.
- `docs/AGENT_MEMORY_HANDOFF.md` — safe durable memory handoff for future repo agents.
- `data/relationships/relationships_template.csv` — relationship map template for graph edges.
- `data/reference/domain_worker_registry.csv` — GitHub domain-agent registry for scheduled and manual cloud workers.
- `AGENTS.md` — repository-wide instructions for Codex and other automation agents.
- `.github/` — GitHub configuration (issues, workflows).

## Current Data Scope

- Generated release bundle: **88,203 master entries** and **20,130 relationship edges** after the Phase 7B sports and recreation priority slice.
- All **40 canonical domains** are represented through bulk ingestors and curated seed records.
- Current processed sources include ISO metadata, IETF RFC metadata, ILO standards, Wikidata standards-body metadata, Google Sheet curation, Phase 2A WHO/Sphere health priority records, Phase 2B Codex food-safety records, Phase 2C humanitarian standards records, Phase 3A IAEA Safety Standards records, Phase 4A GRI/SASB sustainability reporting records, Phase 5A NIST cybersecurity and AI records, Phase 5B W3C web standards records, Phase 5C ITU telecommunications records, Phase 5D ETSI ICT standards records, Phase 5E OASIS/Ecma/GS1 records, Phase 6A IEC electrotechnical records, Phase 6B CCSDS/ECSS space records, Phase 7A UNESCO/ICOMOS/ICOM/ICCROM culture and heritage records, Phase 7B WADA/IOC/IFAB/World Athletics/CAS/FIBA/ITF sports governance records, and Phase 8A national standards body records.
- Current staged sources include Phase 2D WHO IRIS normative candidates and Phase 2E UN/OHCHR human-rights treaty candidates. Staged rows are excluded from release counts until curator promotion.
- Raw ISO technical committees and ICS seed datasets are included in `data/raw/iso/`.
- Additional sources (UN treaties, IAEA, CCSDS, ICAO, IMO, ASTM, ASME, CEN/CENELEC, and others) remain planned in phased ingestion.

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

## GitHub Domain Agents

SIGMA includes a free-safe GitHub Actions scaffold for domain-based automation. The `Domain Agents` workflow can be run manually or on a weekly schedule; it dispatches registered agents from `data/reference/domain_worker_registry.csv`, writes a state artifact, validates generated data, and opens a pull request when a worker changes tracked source or report files.

Start with `dry_run` enabled in GitHub Actions. Add optional provider tokens only through GitHub repository secrets, never in commits. See `docs/GITHUB_AGENTIC_SETUP_GUIDE.md` for the fillable secret template and click-by-click setup.

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

## Public Search

The GitHub Pages build now publishes a searchable standards browser:

```bash
make pagefind-search
```

The static site generator writes `public/search.html`, `public/search-index.json`, and Pagefind-readable record pages under `public/search-records/`. The Pages workflow then runs `npx -y pagefind@1.5.2 --site public --output-subdir pagefind` so the deployed site has a low-bandwidth Pagefind search bundle plus a JSON fallback search for local previews.

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

## Phase 2E UN Treaty Collection Staging

The first UN treaty staging pass transforms source-confirmed UN Treaty Collection and OHCHR core-instrument records into a curator-review table:

```bash
make un-treaties-stage
```

The curated source table is `data/reference/un_treaty_priority_sources.csv`, and the staged output is `data/staging/un_treaty_candidates.csv`. This slice activates the UN Treaty Collection task for Domain 15 and stages the nine OHCHR core international human-rights treaties for review before any release-bundle promotion.

## Phase 3A IAEA Safety Standards Priority Ingestion

The first IAEA ingestor transforms source-confirmed Safety Standards Series records into the processed data layer:

```bash
make iaea-priority
```

The curated source table is `data/reference/iaea_priority_sources.csv`, and the generated canonical output is `data/processed/iaea_safety_standards.csv`. This slice activates the IAEA gap-analysis task for Domain 31 and covers priority Safety Fundamentals, General Safety Requirements, and Specific Safety Requirements for radiation protection, emergency preparedness, nuclear regulatory frameworks, site evaluation, and nuclear power plant safety.

## Phase 4A Sustainability Reporting Standards

The first sustainability reporting ingestor transforms curated GRI and SASB source records into the processed data layer:

```bash
make sustainability-reporting
```

The curated source table is `data/reference/sustainability_reporting_sources.csv`, and the generated canonical output is `data/processed/sustainability_reporting_standards.csv`. This slice activates the GRI/SASB gap-analysis task for Domain 26 and establishes the pattern for expanding into ISSB, ESRS, and GHG Protocol records.

## Phase 5A NIST Cybersecurity and AI Priority Ingestion

The first NIST ingestor transforms source-confirmed CSRC and AI RMF records into the processed data layer:

```bash
make nist-priority
```

The curated source table is `data/reference/nist_priority_sources.csv`, and the generated canonical output is `data/processed/nist_priority_standards.csv`. This slice activates the NIST gap-analysis task for Domain 29 and includes cross-domain AI RMF records for Domain 30.

## Phase 5B W3C Web Standards Priority Ingestion

The first W3C ingestor transforms source-confirmed W3C Technical Reports records into the processed data layer:

```bash
make w3c-priority
```

The curated source table is `data/reference/w3c_priority_sources.csv`, and the generated canonical output is `data/processed/w3c_standards.csv`. This slice activates the W3C gap-analysis task for Domain 28 and covers priority W3C Standards across accessibility, web APIs, verifiable credentials, data catalogues, graphics, real-time communications, and web fonts.

## Phase 5C ITU Telecommunications Priority Ingestion

The first ITU ingestor transforms source-confirmed ITU-T Recommendation records into the processed data layer:

```bash
make itu-priority
```

The curated source table is `data/reference/itu_priority_sources.csv`, and the generated canonical output is `data/processed/itu_recommendations.csv`. This slice activates the ITU gap-analysis task for Domain 28 and covers priority telecommunications recommendations across numbering, optical transport, broadband access, video coding, public-key infrastructure, quality assessment, and machine learning in future networks.

## Phase 5D ETSI ICT Standards Priority Ingestion

The first ETSI ingestor transforms source-confirmed ETSI deliverable records into the processed data layer:

```bash
make etsi-priority
```

The curated source table is `data/reference/etsi_priority_sources.csv`, and the generated canonical output is `data/processed/etsi_standards.csv`. This slice activates the ETSI roadmap task for Domain 28 and covers priority ETSI standards across ICT accessibility, consumer IoT cybersecurity, radio spectrum access, connected transport, 5G system architecture, NFV interoperability, and conformance assessment.

## Phase 5E OASIS, Ecma, and GS1 Priority Ingestion

The open ICT priority ingestor transforms source-confirmed OASIS, Ecma, and GS1 records into the processed data layer:

```bash
make open-ict-priority
```

The curated source table is `data/reference/open_ict_priority_sources.csv`, and the generated canonical output is `data/processed/open_ict_standards.csv`. This slice activates the OASIS, Ecma, and GS1 roadmap tasks with priority records for MQTT, SAML, OpenDocument, STIX, TAXII, ECMAScript, JSON, GS1 General Specifications, EPCIS/CBV, and GS1 Digital Link.

## Phase 6A IEC Electrotechnical Priority Ingestion

The first IEC ingestor transforms source-confirmed IEC Webstore metadata records into the processed data layer:

```bash
make iec-priority
```

The curated source table is `data/reference/iec_priority_sources.csv`, and the generated canonical output is `data/processed/iec_standards.csv`. This slice activates the IEC gap-analysis task for Domain 9 and covers priority electrotechnical families including IEC 60364, IEC 60601, IEC 61000, IEC 61508, IEC 62443, and IEC 60079.

## Phase 6B CCSDS and ECSS Space Standards Priority Ingestion

The first space standards ingestor transforms source-confirmed CCSDS and ECSS records into the processed data layer:

```bash
make space-priority
```

The curated source table is `data/reference/space_priority_sources.csv`, and the generated canonical output is `data/processed/space_standards.csv`. This slice activates the CCSDS/ECSS gap-analysis task for Domain 14 and covers priority space packet, telemetry, telecommand, file delivery, systems engineering, project management, and product-assurance standards.

## Phase 7A Culture and Heritage Priority Ingestion

The first culture and heritage ingestor transforms source-confirmed UNESCO, ICOMOS, ICOM, and ICCROM records into the processed data layer:

```bash
make culture-priority
```

The curated source table is `data/reference/culture_priority_sources.csv`, and the generated canonical output is `data/processed/culture_heritage_standards.csv`. This slice activates the culture and heritage roadmap task for Domain 21 and covers UNESCO heritage conventions, ICOMOS conservation frameworks, the ICOM Code of Ethics for Museums, and ICCROM crisis first-aid guidance.

## Phase 7B Sports and Recreation Priority Ingestion

The first sports and recreation ingestor transforms source-confirmed WADA, IOC, IFAB, World Athletics, CAS, FIBA, and ITF records into the processed data layer:

```bash
make sports-priority
```

The curated source table is `data/reference/sports_priority_sources.csv`, and the generated canonical output is `data/processed/sports_recreation_standards.csv`. This slice activates the sports and recreation roadmap task for Domain 22 and covers anti-doping governance, Olympic Movement governance, football laws, athletics rules, sports arbitration, basketball rules, and tennis rules.

## Life-Science Research Utilities

BindingDB ligand and target lookups can be run through the compact REST wrapper:

```bash
python3 scripts/bindingdb_lookup.py pdb 1Q0L --cutoff 100 --identity 92 --max-items 10
python3 scripts/bindingdb_lookup.py smiles 'CC(=O)OC1=CC=CC=C1C(=O)O' --cutoff 0.9
```

The wrapper delegates requests to `scripts/rest_request.py`, defaults broad lookups to compact output, and supports `--save-raw --raw-output-path ...` when a curator needs to archive the full BindingDB payload.

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

The current project status report is preserved in `docs/PROJECT_STATUS_REPORT_2026-05-02.md`. It summarizes the journey so far, current release metrics, remaining workstreams, lessons learned, challenges, strategies, and operating best practices.

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
- GitHub Pages publishing for a designed static site, generated data downloads, source registry, domain coverage, Pagefind search, fallback JSON search, and project documentation.

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
