# SIGMA Research Task Matrix

This file is generated from `data/reference/research_tasks.csv` by `scripts/build_research_task_report.py`.
It turns the research plan into an executable task matrix across all phases, domains, levels, and publication workstreams.

## Current Interpretation

- `done`: implemented in the repository and covered by validation or generated data.
- `active`: wired into the pipeline, but still awaiting more source rows or enrichment.
- `planned`: accepted scope from the research plan that still needs source-specific ingestion and verification.
- `blocked`: cannot proceed until access, licensing, or source availability is resolved.

## Phase 0: Project setup and infrastructure

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| P0-INFRA | Program | setup | done | critical | Infrastructure baseline |

## Phase 1: Seed from free bulk sources

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| D03-EXPAND | Animal Health & Veterinary | domain-expansion | planned | high | Animal Health & Veterinary verified catalogue |
| D04-EXPAND | Plant Health & Phytosanitary | domain-expansion | planned | high | Plant Health & Phytosanitary verified catalogue |
| D06-EXPAND | Pharmaceuticals & Medicines | domain-expansion | planned | high | Pharmaceuticals & Medicines verified catalogue |
| P1-IETF | Information & Communications Technology (ICT) | ingestion | done | critical | Processed IETF RFC metadata |
| P1-ILO | Labour & Employment | ingestion | done | critical | Processed ILO standards metadata |
| P1-ISO | Program | ingestion | done | critical | Processed ISO metadata |
| P1-README-SAMPLES | Program | publication | active | high | Repository discovery and contributor-readiness improvements |
| P1-SHEET | Program | synchronization | active | high | Processed Google Sheet sync file |
| P1-WIKIDATA | Program | ingestion | done | high | Standards bodies reference dataset |

## Phase 2: Human rights humanitarian and development priority domains

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| D05-EXPAND | Occupational Health & Safety | domain-expansion | planned | high | Occupational Health & Safety verified catalogue |
| D20-EXPAND | Education & Research | domain-expansion | planned | high | Education & Research verified catalogue |
| P2A-HEALTH | Health & Medical | ingestion | done | critical | Processed Phase 2A health priority standards |
| P2A-HUM-WASH | Humanitarian & Emergency Response | ingestion | active | high | Processed humanitarian WASH priority standards |
| P2A-WASH | Water, Sanitation & Hygiene (WASH) | ingestion | active | critical | Processed WASH priority standards |
| P2B-CODEX | Food Safety & Agriculture | ingestion | done | critical | Processed Phase 2B Codex priority standards |
| P2C-HUMANITARIAN | Humanitarian & Emergency Response | ingestion | done | critical | Processed Phase 2C humanitarian standards |
| P2D-WHO-IRIS | Health & Medical | staging | active | high | Filtered WHO IRIS normative candidate metadata |
| P2E-UN-TREATIES | Human Rights | staging | active | high | Staged UN treaty collection metadata for curator review |

## Phase 3: Environment climate and natural systems

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| D36-EXPAND | Environment & Climate | domain-expansion | planned | critical | Environment & Climate verified catalogue |
| D37-EXPAND | Marine & Ocean | domain-expansion | planned | high | Marine & Ocean verified catalogue |
| D38-EXPAND | Biodiversity & Conservation | domain-expansion | planned | high | Biodiversity & Conservation verified catalogue |
| D40-EXPAND | Extractive Industries & Natural Resources | domain-expansion | planned | medium | Extractive Industries & Natural Resources verified catalogue |
| P3-IAEA | Energy & Utilities | ingestion | done | high | Processed IAEA Safety Standards catalogue |

## Phase 4: Finance trade and economic governance

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| D23-EXPAND | Finance, Banking & Accounting | domain-expansion | planned | critical | Finance, Banking & Accounting verified catalogue |
| D24-EXPAND | Trade & Customs | domain-expansion | planned | critical | Trade & Customs verified catalogue |
| D27-EXPAND | Taxation & Public Finance | domain-expansion | planned | medium | Taxation & Public Finance verified catalogue |
| P4-GRI-SASB | Sustainability, ESG & Circular Economy | ingestion | done | high | Processed sustainability reporting standards catalogue |

## Phase 5: ICT digital AI and cybersecurity

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| D30-EXPAND | Artificial Intelligence & Emerging Technologies | domain-expansion | planned | critical | Artificial Intelligence & Emerging Technologies verified catalogue |
| P5-ECMA | Information & Communications Technology (ICT) | ingestion | done | high | Processed Ecma priority standards metadata |
| P5-ETSI | Information & Communications Technology (ICT) | ingestion | done | high | Processed ETSI priority standards metadata |
| P5-GS1 | Supply Chain & Logistics | ingestion | done | high | Processed GS1 priority standards metadata |
| P5-ITU | Information & Communications Technology (ICT) | ingestion | done | high | Processed ITU recommendations metadata |
| P5-NIST | Cybersecurity & Data Privacy | ingestion | done | critical | Processed NIST cybersecurity and AI standards metadata |
| P5-OASIS | Information & Communications Technology (ICT) | ingestion | active | high | Processed OASIS priority standards metadata |
| P5-W3C | Information & Communications Technology (ICT) | ingestion | active | high | Processed W3C Recommendations catalogue |

## Phase 6: Transport energy manufacturing and built environment

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| D07-EXPAND | Measurement & Metrology | domain-expansion | planned | medium | Measurement & Metrology verified catalogue |
| D08-EXPAND | Manufacturing & Industry | domain-expansion | planned | medium | Manufacturing & Industry verified catalogue |
| D10-EXPAND | Construction & Built Environment | domain-expansion | planned | medium | Construction & Built Environment verified catalogue |
| D11-EXPAND | Chemical & Process Industries | domain-expansion | planned | medium | Chemical & Process Industries verified catalogue |
| D12-EXPAND | Materials Science & Testing | domain-expansion | planned | medium | Materials Science & Testing verified catalogue |
| D13-EXPAND | Aerospace & Aviation | domain-expansion | planned | high | Aerospace & Aviation verified catalogue |
| D32-EXPAND | Transport (Land, Sea, Air, Rail) | domain-expansion | planned | high | Transport (Land, Sea, Air, Rail) verified catalogue |
| D34-EXPAND | Built Environment & Urban Systems | domain-expansion | planned | medium | Built Environment & Urban Systems verified catalogue |
| P6-CCSDS | Space & Satellite | ingestion | active | high | Processed space and satellite standards metadata |
| P6-IEC | Electrical & Electronics | ingestion | done | critical | Processed IEC electrotechnical standards metadata |

## Phase 7: Society culture sports and specialised domains

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| D18-EXPAND | Legal & Commercial Law | domain-expansion | planned | medium | Legal & Commercial Law verified catalogue |
| D19-EXPAND | Governance, Transparency & Anti-Corruption | domain-expansion | planned | medium | Governance, Transparency & Anti-Corruption verified catalogue |
| D35-EXPAND | Defence & Security (Declassified) | domain-expansion | planned | medium | Defence & Security (Declassified) verified catalogue |
| D39-EXPAND | Disaster Risk & Humanitarian Preparedness | domain-expansion | planned | high | Disaster Risk & Humanitarian Preparedness verified catalogue |
| P7-CULTURE | Culture, Heritage & Arts | curation | done | critical | Curated culture and heritage standards catalogue |
| P7-SPORTS | Sports & Recreation | curation | done | critical | Curated sports and recreation standards catalogue |

## Phase 8: National standards bodies comprehensive expansion

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| P8-NSB | Program | domain-expansion | done | critical | National standards body register |

## Phase 9: Verification publication and community launch

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| P9-HDX | Program | publication | planned | high | HDX publication package for humanitarian discovery |
| P9-QA | Program | quality | active | critical | v1.0 quality launch checklist |
| P9-ZENODO | Program | publication | planned | high | Citable Zenodo dataset release |

## Phase 19: Enhanced integration roadmap

| Task | Domain | Type | Status | Priority | Deliverable |
|---|---|---|---|---|---|
| P19-AUTOMATION | Program | automation | planned | high | Freshness automation plan |
| P19-GRAPH | Program | architecture | planned | high | Hybrid data architecture plan |
| P19-SEARCH | Program | publication | done | critical | Searchable public standards browser |
| P19-UX | Program | publication | planned | high | Enhanced publication roadmap |
