# SIGMA Project Knowledge Graph

This document is a maintainer map for understanding the repository quickly. It does not add proprietary data or replace the canonical dataset. The source of truth remains `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md` and `docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md`.

## 1. Core Nodes

| Node | Type | Repository path | Role |
|---|---|---|---|
| Research Plan | Source of truth | `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md` | Canonical 24-month phase structure, methodology, schema, governance, and domain strategy |
| Roadmap to 100 Percent | Source of truth | `docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md` | Detailed remaining-work execution plan from current MVP to v1.0 |
| Gap Analysis | External feedback | `docs/SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.md` | Friend-reviewed gap report incorporated into roadmap checkpoints and research tasks |
| Project Status Report | Status report | `docs/PROJECT_STATUS_REPORT_2026-05-02.md` | Dated journey summary, accomplishments, current metrics, challenges, strategies, best practices, and next steps |
| Schema | Contract | `SCHEMA.md` | Published 22-field master-entry contract |
| Domain Taxonomy | Reference data | `data/reference/domain_taxonomy.csv` | Canonical 40-domain registry |
| Source Registry | Reference data | `data/reference/source_registry.csv` | Public source map and source status table |
| Research Tasks | Reference data | `data/reference/research_tasks.csv` | Machine-readable task matrix for phases, domains, and priorities |
| Processed Data | Canonical data layer | `data/processed/` | Normalized source-backed records used by release builds |
| Relationships | Graph edge layer | `data/relationships/` | Relationship edges between standards, bodies, domains, and source records |
| Reports | Generated report layer | `data/reports/` and `docs/` | Quality, domain coverage, and task coverage summaries |
| Static Site | Publication layer | `scripts/build_static_site.py` and `public/` | GitHub Pages site generated from release artifacts, searchable record pages, and documentation |
| Pagefind Search | Publication layer | `public/search.html`, `public/search-records/`, `public/pagefind/` | Static full-text search surface for the generated Pages site |

## 2. Pipeline Edges

| From | Relationship | To |
|---|---|---|
| Research Plan | defines | Domain Taxonomy |
| Research Plan | defines | Research Tasks |
| Roadmap to 100 Percent | prioritizes | Research Tasks |
| Gap Analysis | adds accepted enhancement tasks to | Research Tasks |
| Project Status Report | summarizes current progress toward | Roadmap to 100 Percent |
| Source Registry | authorizes source families for | Processed Data |
| Raw Data | feeds | Processing Scripts |
| Reference Data | feeds | Processing Scripts |
| Processing Scripts | generate | Processed Data |
| NIST Priority Sources | feed | `scripts/process_nist_priority.py` |
| `scripts/process_nist_priority.py` | generates | `data/processed/nist_priority_standards.csv` |
| W3C Priority Sources | feed | `scripts/process_w3c_priority.py` |
| `scripts/process_w3c_priority.py` | generates | `data/processed/w3c_standards.csv` |
| ITU Priority Sources | feed | `scripts/process_itu_priority.py` |
| `scripts/process_itu_priority.py` | generates | `data/processed/itu_recommendations.csv` |
| ETSI Priority Sources | feed | `scripts/process_etsi_priority.py` |
| `scripts/process_etsi_priority.py` | generates | `data/processed/etsi_standards.csv` |
| OASIS/Ecma/GS1 Priority Sources | feed | `scripts/process_open_ict_priority.py` |
| `scripts/process_open_ict_priority.py` | generates | `data/processed/open_ict_standards.csv` |
| IEC Priority Sources | feed | `scripts/process_iec_priority.py` |
| `scripts/process_iec_priority.py` | generates | `data/processed/iec_standards.csv` |
| Space Priority Sources | feed | `scripts/process_space_priority.py` |
| `scripts/process_space_priority.py` | generates | `data/processed/space_standards.csv` |
| IAEA Priority Sources | feed | `scripts/process_iaea_priority.py` |
| `scripts/process_iaea_priority.py` | generates | `data/processed/iaea_safety_standards.csv` |
| Culture Priority Sources | feed | `scripts/process_culture_priority.py` |
| `scripts/process_culture_priority.py` | generates | `data/processed/culture_heritage_standards.csv` |
| UN Treaty Priority Sources | feed | `scripts/stage_un_treaties.py` |
| `scripts/stage_un_treaties.py` | generates | `data/staging/un_treaty_candidates.csv` |
| Processed Data | validates against | Schema |
| Processed Data | supports | Relationships |
| Relationships | validates against | Processed Data |
| Processed Data | builds | Release Bundle |
| Reports | explain | Release Bundle |
| Release Bundle | publishes through | Static Site |
| Release Bundle | feeds | Pagefind Search |
| Documentation | renders through | Static Site |

## 3. Command Graph

| Command | Inputs | Outputs |
|---|---|---|
| `make validate` | reference data, processed data, relationships, staging fixture | schema checks, relationship checks, quality gate, generated task docs |
| `make nist-priority` | `data/reference/nist_priority_sources.csv` | `data/processed/nist_priority_standards.csv` |
| `make w3c-priority` | `data/reference/w3c_priority_sources.csv` | `data/processed/w3c_standards.csv` |
| `make itu-priority` | `data/reference/itu_priority_sources.csv` | `data/processed/itu_recommendations.csv` |
| `make etsi-priority` | `data/reference/etsi_priority_sources.csv` | `data/processed/etsi_standards.csv` |
| `make open-ict-priority` | `data/reference/open_ict_priority_sources.csv` | `data/processed/open_ict_standards.csv` |
| `make iec-priority` | `data/reference/iec_priority_sources.csv` | `data/processed/iec_standards.csv` |
| `make space-priority` | `data/reference/space_priority_sources.csv` | `data/processed/space_standards.csv` |
| `make iaea-priority` | `data/reference/iaea_priority_sources.csv` | `data/processed/iaea_safety_standards.csv` |
| `make culture-priority` | `data/reference/culture_priority_sources.csv` | `data/processed/culture_heritage_standards.csv` |
| `make un-treaties-stage` | `data/reference/un_treaty_priority_sources.csv` | `data/staging/un_treaty_candidates.csv` |
| `make release` | validated processed data and relationships | `dist/` release bundle |
| `make site` | release bundle and documentation | `public/` GitHub Pages output |
| `make pagefind-search` | static site output | `public/pagefind/` static search bundle |
| `make clean` | generated local artifacts | removes `dist/`, `public/`, caches, build outputs |
| GitHub Actions `ci.yml` | repository checkout and installed package | `make validate` and pytest status on push and pull request |

## 4. Stewardship Rules

1. Treat the research plan and roadmap as the navigation source of truth.
2. Keep source evidence in reference tables before promoting processed rows.
3. Keep broad harvesters in staging until filters are proven.
4. Keep generated files reproducible from scripts.
5. Avoid committing temporary downloads, caches, local virtual environments, and one-off conversion files.
6. Use GitHub Issues as the public contact and contribution intake path.
