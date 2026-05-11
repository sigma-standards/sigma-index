# CHANGELOG

All notable changes to the SIGMA Unified Global Standards Index are documented here.
Format: [Semantic Versioning](https://semver.org/). Data changes use the same version scheme.

---

## [1.1.0] — 2026-05-11

### Added
- Critical domain expansion: 8 domains expanded from 1 to 5-10 entries each
  - Human Rights (HR): 9 core treaties (ICCPR, ICESCR, CEDAW, CRC, CRPD, CAT, CMW, CERD)
  - Finance (FB): 8 financial stability standards (Basel IV, FATF 40 Recs, IOSCO, IFRS 1/9/16/17)
  - Environment (EC): 8 environmental treaties (UNFCCC, Kyoto, CBD GBF, Montreal, Stockholm, Basel, Rotterdam, Minamata)
  - Transport (TR): 8 transport standards (ICAO Annexes 1/2/6, SOLAS, MARPOL, STCW, UNECE WP.29, ADR)
  - Extractive Industries (EX): 6 standards (EITI, ICMM, Kimberly, FSC, RSPO, IRMA)
  - Biodiversity (BC): 6 conservation frameworks (CBD, Nagoya, CITES, Ramsar, IUCN Red List, IUCN Green List)
  - Marine (MO): 6 ocean governance instruments (UNCLOS, London Convention, IWC, CCAMLR, MSC, FAO Code)
  - Disaster Risk (DR): 5 DRR frameworks (Sendai, ISO 22301/22313/22316, WHO HEDRM)
- Research task completion: 15 active tasks marked as done
- Test badge added to README (89 tests passing)
- Quality gate badge updated to pass status

### Changed
- README updated to reflect v1.1.0 in-progress status
- CONTRIBUTING.md updated with critical domain expansion progress
- Research tasks status updated in data/reference/research_tasks.csv

### Metrics
- Master entries: **88,288** (84 additional entries from domain expansion)
- Relationship edges: **20,140**
- Canonical domains: **40 / 40**
- Quality gate: **PASS** (0 critical failures)
- Tests: **89 / 89 passing**

---

## [Unreleased]

### Planned
- Phase 2E UN/OHCHR human-rights treaty promotion from staging to release
- Phase 2D WHO IRIS normative candidates promotion from staging to release
- v1.0 GitHub Release tag + Zenodo DOI assignment
- HDX (Humanitarian Data Exchange) dataset submission
- REST API deployment (Cloudflare Workers free tier)
- Multilingual field additions: `name_full_fr`, `name_full_es`, `name_full_ar`

---

## [0.9.0] — 2026-05-04 (Current)

### Added
- Phase 7B: Sports and Recreation priority ingestor (WADA, IOC, IFAB, World Athletics, CAS, FIBA, ITF) — 9 entries
- Phase 7A: Culture and Heritage priority ingestor (UNESCO, ICOMOS, ICOM, ICCROM) — 9 entries
- Phase 8A: National standards body registry slice (ANSI, BSI, DIN, BIS, JISC, SAC, ABNT, SABS, KEBS, BSTI) — initial 10 bodies
- Phase 6B: CCSDS and ECSS space standards ingestor — 9 entries
- Phase 6A: IEC electrotechnical priority ingestor — 8 entries
- Phase 5E: OASIS, Ecma, and GS1 open ICT standards ingestor
- Phase 5D: ETSI ICT standards priority ingestor
- Phase 5C: ITU-T telecommunications priority ingestor
- Phase 5B: W3C web standards priority ingestor
- Phase 5A: NIST cybersecurity and AI priority ingestor — 7 entries
- Phase 4A: GRI and SASB sustainability reporting ingestor — 11 entries
- Phase 3A: IAEA Safety Standards priority ingestor — 9 entries
- Phase 2C: Humanitarian standards expansion (CHS, INEE, IASC, UNHCR, WHO EMT) — 7 entries
- Phase 2B: Codex Alimentarius priority ingestor — 9 entries
- Phase 2A: Health priority ingestor (WHO/Sphere/WASH) — 5 entries
- Domain agent scaffold: `domain_agents.yml` workflow with 12 domain workers
- `run_domain_worker.py` runner for scheduled and manual agent dispatch
- Pagefind search index on GitHub Pages (`make pagefind-search`)
- `build_relationship_quality.py` — relationship graph audit report
- `stage_un_treaties.py` — UN Treaty Collection staging pipeline
- `check_urls.py` — monthly URL health audit
- `build_static_site.py` — GitHub Pages static site generator
- `sync_google_sheet.py` — Google Sheet curation sync
- All 8 GitHub Issue templates (broken link, domain expansion, duplicate, error correction, missing standard, new entry, source correction, config)
- `AGENTS.md` — repository-wide instructions for Codex and automation agents
- `.github/copilot-instructions.md` — GitHub Copilot instructions
- `docs/PROJECT_KNOWLEDGE_GRAPH.md` — maintainer pipeline map
- `docs/SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.md` — external gap analysis
- `docs/PROJECT_STATUS_REPORT_2026-05-02.md` — milestone status report
- `docs/OPERATOR_DASHBOARD.md` — maintainer operations dashboard
- `docs/AGENT_MEMORY_HANDOFF.md` — safe durable memory handoff
- `docs/GITHUB_AGENTIC_SETUP_GUIDE.md` — click-by-click setup guide
- `data/reference/domain_worker_registry.csv` — GitHub domain-agent registry
- `data/reference/research_tasks.csv` — 24-month research plan as machine-readable tasks
- `data/relationships/relationships_template.csv` — graph edge template
- BindingDB life-science research utilities (`bindingdb_lookup.py`, `rest_request.py`)
- Required gate workflow (`required_gate.yml`)

### Changed
- Release bundle expanded to 13 artifact types
- README enhanced with sample records table, phase-by-phase documentation, badges
- SCHEMA.md updated with supplementary entity table specifications
- Makefile extended to 30+ deterministic targets

### Fixed
- Quality gate now catches duplicate sigma_id, missing required fields, malformed URLs

### Metrics
- Master entries: **88,204**
- Relationship edges: **20,140**
- Canonical domains: **40 / 40**
- Quality gate: **PASS** (0 critical failures)

---

## [0.5.0] — 2026-04-15

### Added
- ISO Open Data seed (25,703 standard metadata records)
- IETF RFC Editor bulk seed (9,400+ internet protocol records)
- ILO NORMLEX bulk ingestor (252 Convention and Recommendation entries)
- Wikidata SPARQL national standards body metadata
- `validate_schema.py`, `validate_relationships.py`, `build_quality_gate.py`
- `build_release.py` generating CSV, JSON, JSONL, and API index artifacts
- `build_domain_coverage.py` — per-domain entry count report
- `extract_relationships.py` — ILO supersedes and ISO references graph edges
- `validate_domain_registry.py`, `build_research_task_report.py`
- CI workflow (`ci.yml`) with schema validation and release build
- Schema validation workflow (`schema_validation.yml`)
- Release build workflow (`release_build.yml`)
- Pages workflow (`pages.yml`) with Pagefind integration
- URL health check workflow (`url_check.yml`) on monthly schedule
- 22-field SIGMA master schema (`SCHEMA.md`)
- 40-domain canonical taxonomy (`data/reference/domain_taxonomy.csv`)
- Source registry (`data/reference/source_registry.csv`)
- CC BY 4.0 LICENSE
- `pyproject.toml` with 6 CLI entry points
- `CODE_OF_CONDUCT.md`

---

## [0.1.0] — 2026-04-01

### Added
- Initial repository structure at `github.com/sigma-standards/sigma-index`
- GitHub organisation `sigma-standards` created
- `README.md`, `CONTRIBUTING.md`, `SCHEMA.md`
- ISO raw seed files committed to `data/raw/iso/`
- GitHub Pages enabled

---

*Maintained by Mohammad Ariful Islam — CPI Bangladesh Mission.*
*Corrections welcome via GitHub Issues: https://github.com/sigma-standards/sigma-index/issues*
