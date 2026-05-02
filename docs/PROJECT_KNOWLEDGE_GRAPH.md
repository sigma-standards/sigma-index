# SIGMA Project Knowledge Graph

This document is a maintainer map for understanding the repository quickly. It does not add proprietary data or replace the canonical dataset. The source of truth remains `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md` and `docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md`.

## 1. Core Nodes

| Node | Type | Repository path | Role |
|---|---|---|---|
| Research Plan | Source of truth | `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md` | Canonical 24-month phase structure, methodology, schema, governance, and domain strategy |
| Roadmap to 100 Percent | Source of truth | `docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md` | Detailed remaining-work execution plan from current MVP to v1.0 |
| Schema | Contract | `SCHEMA.md` | Published 22-field master-entry contract |
| Domain Taxonomy | Reference data | `data/reference/domain_taxonomy.csv` | Canonical 40-domain registry |
| Source Registry | Reference data | `data/reference/source_registry.csv` | Public source map and source status table |
| Research Tasks | Reference data | `data/reference/research_tasks.csv` | Machine-readable task matrix for phases, domains, and priorities |
| Processed Data | Canonical data layer | `data/processed/` | Normalized source-backed records used by release builds |
| Relationships | Graph edge layer | `data/relationships/` | Relationship edges between standards, bodies, domains, and source records |
| Reports | Generated report layer | `data/reports/` and `docs/` | Quality, domain coverage, and task coverage summaries |
| Static Site | Publication layer | `scripts/build_static_site.py` and `public/` | GitHub Pages site generated from release artifacts and documentation |

## 2. Pipeline Edges

| From | Relationship | To |
|---|---|---|
| Research Plan | defines | Domain Taxonomy |
| Research Plan | defines | Research Tasks |
| Roadmap to 100 Percent | prioritizes | Research Tasks |
| Source Registry | authorizes source families for | Processed Data |
| Raw Data | feeds | Processing Scripts |
| Reference Data | feeds | Processing Scripts |
| Processing Scripts | generate | Processed Data |
| Processed Data | validates against | Schema |
| Processed Data | supports | Relationships |
| Relationships | validates against | Processed Data |
| Processed Data | builds | Release Bundle |
| Reports | explain | Release Bundle |
| Release Bundle | publishes through | Static Site |
| Documentation | renders through | Static Site |

## 3. Command Graph

| Command | Inputs | Outputs |
|---|---|---|
| `make validate` | reference data, processed data, relationships, staging fixture | schema checks, relationship checks, quality gate, generated task docs |
| `make release` | validated processed data and relationships | `dist/` release bundle |
| `make site` | release bundle and documentation | `public/` GitHub Pages output |
| `make clean` | generated local artifacts | removes `dist/`, `public/`, caches, build outputs |

## 4. Stewardship Rules

1. Treat the research plan and roadmap as the navigation source of truth.
2. Keep source evidence in reference tables before promoting processed rows.
3. Keep broad harvesters in staging until filters are proven.
4. Keep generated files reproducible from scripts.
5. Avoid committing temporary downloads, caches, local virtual environments, and one-off conversion files.
6. Use GitHub Issues as the public contact and contribution intake path.

