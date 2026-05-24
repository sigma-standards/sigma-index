# SIGMA Research Task Matrix — v1.2.0

**Generated:** 2026-05-11  
**Total Tasks:** 37  
**Completed:** 23 (62%)  
**Active:** 2 (5%)  
**Planned:** 12 (33%)

This document provides a comprehensive view of all research tasks across SIGMA's 24-month roadmap. Tasks are organized by phase, priority, and domain. Use this alongside `data/reference/research_tasks.csv` for the machine-readable version.

---

## Summary by Status

### ✅ Done (23 tasks)

**Phase 0–1: Infrastructure & Seed Data**
- P0-INFRA: Project setup and infrastructure
- P1-ISO: ISO Open Data seed
- P1-WIKIDATA: Standards bodies Wikidata SPARQL
- P1-IETF: RFC Editor bulk seed
- P1-ILO: ILO conventions and recommendations
- P1-README-SAMPLES: README badges and samples

**Phase 2: Human Rights, Humanitarian & Development**
- P2A-HEALTH: WHO/Sphere health priority
- P2A-HUM-WASH: Humanitarian WASH standards
- P2A-WASH: WASH priority standards
- P2B-CODEX: Codex Alimentarius
- P2C-HUMANITARIAN: CHS/INEE/IASC/UNHCR/WHO EMT

**Phase 3–8: Domain-Specific & Infrastructure**
- P3-IAEA: IAEA Safety Standards
- P4-GRI-SASB: Sustainability reporting (GRI/SASB)
- P5-W3C: W3C web standards
- P5-NIST: NIST cybersecurity and AI
- P5-OASIS: OASIS standards
- P5-GS1: GS1 supply chain standards
- P6-IEC: IEC electrotechnical standards
- P6-CCSDS: CCSDS/ECSS space standards
- P7-CULTURE: UNESCO/ICOMOS culture heritage
- P7-SPORTS: WADA/IOC/IFAB sports
- P8-NSB: National standards bodies registry
- P9-SEARCH: Pagefind static search

### 🟡 Active (2 tasks)

- P1-SHEET: Google Sheet sync integration
- P9-QA: Quality launch checklist (P9-QA)

### 🔵 Planned (12 tasks)

- P2D-WHO-IRIS: WHO IRIS normative metadata staging → promotion
- P2E-UN-TREATIES: UN/OHCHR human-rights treaty staging → promotion
- P5-ITU: ITU-T telecommunications standards
- P5-ETSI: ETSI ICT standards
- P5-ECMA: Ecma standards (ECMAScript, JSON)
- P9-HDX: HDX humanitarian dataset submission
- P9-ZENODO: Zenodo DOI and GitHub release
- P19-GRAPH: Hybrid architecture (tabular + graph + vector)
- P19-AUTOMATION: Freshness automation (ISO sync, ratification tracking)
- P19-UX: Enhanced UX (faceted search, semantic API, accessibility)

---

## Phase 0: Project Setup & Infrastructure ✅

| Task | Domain | Type | Status | Deliverable | Owner |
|------|--------|------|--------|-------------|-------|
| P0-INFRA | — | setup | ✅ done | GitHub repo, Pages, governance docs, workflows | Mohammad |

**Progress:** 100% (1/1 complete)

---

## Phase 1: Seed from Free Bulk Sources ✅

| Task | Domain | Type | Status | Deliverable | Owner |
|------|--------|------|--------|-------------|-------|
| P1-ISO | — | ingestion | ✅ done | ISO Open Data (25,703 entries) | Mohammad |
| P1-WIKIDATA | — | ingestion | ✅ done | Standards bodies reference (Wikidata SPARQL) | Mohammad |
| P1-IETF | ICT | ingestion | ✅ done | RFC metadata (9,400+ entries) | Mohammad |
| P1-ILO | Labour & Employment | ingestion | ✅ done | ILO standards (252 entries) | Mohammad |
| P1-SHEET | — | synchronization | 🟡 active | Google Sheet sync automation | Mohammad |
| P1-README-SAMPLES | — | publication | ✅ done | README badges, sample records, contributor path | Mohammad |

**Progress:** 83% (5/6 complete)

---

## Phase 2A: Human Rights, Humanitarian & Development — Health Priority ✅

| Task | Domain | Meta-layer | Type | Status | Deliverable | Owner |
|-------|--------|-----------|------|--------|-------------|-------|
| P2A-HEALTH | Health & Medical | L1 Life Sciences | ingestion | ✅ done | health_priority_standards.csv (5 entries) | Mohammad |
| P2A-HUM-WASH | Humanitarian & Emergency Response | L3 Society & Governance | ingestion | ✅ done | Enhanced humanitarian domain | Mohammad |
| P2A-WASH | Water, Sanitation & Hygiene (WASH) | L5 Technology & Infrastructure | ingestion | ✅ done | wash_priority_standards.csv | Mohammad |

**Progress:** 100% (3/3 complete)

---

## Phase 2B: Food Safety & Agriculture Priority ✅

| Task | Domain | Meta-layer | Type | Status | Deliverable | Owner |
|-------|--------|-----------|------|--------|-------------|-------|
| P2B-CODEX | Food Safety & Agriculture | L1 Life Sciences | ingestion | ✅ done | codex_standards.csv (9 entries) | Mohammad |

**Progress:** 100% (1/1 complete)

---

## Phase 2C: Humanitarian Standards Expansion ✅

| Task | Domain | Meta-layer | Type | Status | Deliverable | Owner |
|-------|--------|-----------|------|--------|-------------|-------|
| P2C-HUMANITARIAN | Humanitarian & Emergency Response | L3 Society & Governance | ingestion | ✅ done | humanitarian_priority_standards.csv (7 entries) | Mohammad |

**Progress:** 100% (1/1 complete)

---

## Phase 2D: WHO IRIS Staging 🟡

| Task | Domain | Meta-layer | Type | Status | ETA | Deliverable | Owner |
|--------|--------|-----------|------|--------|-----|-------------|-------|
| P2D-WHO-IRIS | Health & Medical | L1 Life Sciences | staging | 🟡 planned | Jun 2026 | Promote filtered WHO IRIS normative candidates | Mohammad |

**Progress:** 0% (0/1 complete) — Source-mapped, awaiting curator review

---

## Phase 2E: UN Treaty Collection Staging 🟡

| Task | Domain | Meta-layer | Type | Status | ETA | Deliverable | Owner |
|--------|--------|-----------|------|--------|-----|-------------|-------|
| P2E-UN-TREATIES | Human Rights | L3 Society & Governance | staging | 🟡 planned | Jun 2026 | Promote UN/OHCHR core human-rights treaties | Mohammad |

**Progress:** 0% (0/1 complete) — Source-mapped, awaiting curator review

---

## Phase 3A: Environment, Climate & Natural Systems — IAEA Priority ✅

| Task | Domain | Meta-layer | Type | Status | Deliverable | Owner |
|-------|--------|-----------|------|--------|-------------|-------|
| P3-IAEA | Energy & Utilities | L5 Technology & Infrastructure | ingestion | ✅ done | iaea_safety_standards.csv (9 entries) | Mohammad |

**Progress:** 100% (1/1 complete)

---

## Phase 4A: Finance, Trade & Economic Governance — Sustainability Reporting ✅

| Task | Domain | Meta-layer | Type | Status | Deliverable | Owner |
|-------|--------|-----------|------|--------|-------------|-------|
| P4-GRI-SASB | Sustainability, ESG & Circular Economy | L4 Economy & Trade | ingestion | ✅ done | sustainability_reporting_standards.csv (11 entries) | Mohammad |

**Progress:** 100% (1/1 complete)

---

## Phase 5: ICT, Digital, AI & Cybersecurity 📊

| Task | Domain | Meta-layer | Type | Status | ETA | Deliverable | Owner |
|--------|--------|-----------|------|--------|-----|-------------|-------|
| P5-W3C | ICT | L5 Technology & Infrastructure | ingestion | ✅ done | w3c_standards.csv (200 entries) | Mohammad |
| P5-NIST | Cybersecurity & Data Privacy | L5 Technology & Infrastructure | ingestion | ✅ done | nist_priority_standards.csv (7 entries) | Mohammad |
| P5-ITU | ICT | L5 Technology & Infrastructure | ingestion | 🟡 planned | Jul 2026 | itu_recommendations.csv (400 entries) | Mohammad |
| P5-ETSI | ICT | L5 Technology & Infrastructure | ingestion | 🟡 planned | Jul 2026 | etsi_standards.csv (300 entries) | Mohammad |
| P5-ECMA | ICT | L5 Technology & Infrastructure | ingestion | 🟡 planned | Jul 2026 | ecma_standards.csv (30 entries) | Mohammad |
| P5-OASIS | ICT | L5 Technology & Infrastructure | ingestion | ✅ done | open_ict_standards.csv (OASIS + Ecma + GS1) | Mohammad |
| P5-GS1 | Supply Chain & Logistics | L4 Economy & Trade | ingestion | ✅ done | GS1 included in open_ict_standards.csv (200 entries) | Mohammad |

**Progress:** 71% (5/7 complete) — P5-ITU and P5-ETSI deferred to v1.3.0

---

## Phase 6: Transport, Energy, Manufacturing & Built Environment 📊

| Task | Domain | Meta-layer | Type | Status | ETA | Deliverable | Owner |
|--------|--------|-----------|------|--------|-----|-------------|-------|
| P6-IEC | Electrical & Electronics | L2 Physical Sciences & Engineering | ingestion | ✅ done | iec_standards.csv (8 entries) | Mohammad |
| P6-CCSDS | Space & Satellite | L2 Physical Sciences & Engineering | ingestion | ✅ done | space_standards.csv (9 entries) | Mohammad |

**Progress:** 100% (2/2 complete)

---

## Phase 7: Society, Culture, Sports & Specialised Domains ✅

| Task | Domain | Meta-layer | Type | Status | Deliverable | Owner |
|-------|--------|-----------|------|--------|-------------|-------|
| P7-CULTURE | Culture, Heritage & Arts | L3 Society & Governance | curation | ✅ done | culture_heritage_standards.csv (9 entries) | Mohammad |
| P7-SPORTS | Sports & Recreation | L3 Society & Governance | curation | ✅ done | sports_recreation_standards.csv (9 entries) | Mohammad |

**Progress:** 100% (2/2 complete)

---

## Phase 8: National Standards Bodies Comprehensive Expansion ✅

| Task | Domain | Meta-layer | Type | Status | Deliverable | Owner |
|-------|--------|-----------|------|--------|-------------|-------|
| P8-NSB | — | — | domain-expansion | ✅ done | national_standards_bodies.csv (176 ISO members, ARSO, ASEAN) | Mohammad |

**Progress:** 100% (1/1 complete)

---

## Phase 9: Verification, Publication & Community Launch 📊

| Task | Domain | Meta-layer | Type | Status | ETA | Deliverable | Owner |
|--------|--------|-----------|------|--------|-----|-------------|-------|
| P9-SEARCH | — | — | publication | ✅ done | Pagefind static search + fallback JSON search | Mohammad |
| P9-QA | — | — | quality | 🟡 active | Jun 2026 | URL verification, duplicate detection, expert review, release tags | Mohammad |
| P9-HDX | — | — | publication | 🟡 planned | Aug 2026 | HDX dataset + download bundle | Mohammad |
| P9-ZENODO | — | — | publication | 🟡 planned | Aug 2026 | Citable Zenodo DOI + GitHub release | Mohammad |

**Progress:** 25% (1/4 complete)

---

## Phase 19: Enhanced Integration Roadmap 🎯

| Task | Domain | Meta-layer | Type | Status | ETA | Deliverable | Owner |
|--------|--------|-----------|------|--------|-----|-------------|-------|
| P19-GRAPH | — | — | architecture | 🟡 planned | Sep 2026 | Hybrid (tabular + graph + vector) | Mohammad |
| P19-AUTOMATION | — | — | automation | 🟡 planned | Sep 2026 | Freshness automation (ISO, ratification, changelogs) | Mohammad |
| P19-UX | — | — | publication | 🟡 planned | Oct 2026 | Faceted search, semantic API, accessibility | Mohammad |

**Progress:** 0% (0/3 complete)

---

## Meta-Layer Coverage Summary

| Meta-layer | Domains | Tasks | Complete | Progress |
|------------|---------|-------|----------|----------|
| **L1 Life Sciences & Health** | 6 | P2A, P2B, P2C | ✅ | 100% (3/3) |
| **L2 Physical Sciences & Engineering** | 8 | P6-IEC, P6-CCSDS | ✅ | 100% (2/2) |
| **L3 Society, Governance & Law** | 8 | P2C, P7-CULTURE, P7-SPORTS | ✅ | 100% (3/3) |
| **L4 Economy & Trade** | 5 | P4-GRI-SASB, P5-GS1 | ✅ | 100% (2/2) |
| **L5 Technology & Infrastructure** | 8 | P5-W3C, P5-NIST, P5-ITU, P5-ETSI, P3-IAEA | 📊 | 71% (5/7) |
| **L6 Environment & Natural Systems** | 5 | (covered under L5 IAEA) | ✅ | 100% (1/1) |

---

## Priority Distribution

| Priority | Count | Tasks |
|----------|-------|-------|
| **critical** | 5 | P0-INFRA, P1-ISO, P1-IETF, P1-ILO, P8-NSB, P9-ZENODO |
| **high** | 20 | P1-WIKIDATA, P1-SHEET, P2A-*, P2B-CODEX, P2D-WHO-IRIS, P2E-UN-TREATIES, P4-GRI-SASB, P5-W3C, P5-NIST, P5-ITU, P5-ETSI, P6-*, P7-*, P9-HDX, P19-GRAPH, P19-AUTOMATION, P19-UX |
| **medium** | 10 | P5-ECMA, P19-SEARCH, others |

---

## How to Update This Document

Run the task matrix generator:

```bash
make research-tasks
```

This regenerates `docs/RESEARCH_TASKS.md` and `data/reports/research_task_coverage.csv` from `data/reference/research_tasks.csv`.

---

## Contribution Alignment

To contribute to a specific research task:

1. Identify the task ID (e.g., `P5-ITU`)
2. Check status in `data/reference/research_tasks.csv`
3. Create an issue or PR referencing the task ID
4. Link your contribution to the corresponding Makefile target
5. Include the task ID in commit messages: `"feat: implement P5-ITU ingestion"`

---

**Last Generated:** 2026-05-11  
**Maintained by:** Mohammad Ariful Islam (CPI Bangladesh Mission)  
**Source:** `data/reference/research_tasks.csv`