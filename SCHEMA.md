# SIGMA Data Schema

This document describes the data schema used in the SIGMA Unified Global Standards Index.

## Master Schema — 22 Fields per Entry

Every entry in the SIGMA index carries the following fields:

| # | Field Name | Type | Description | Example |
|---|-----------|------|-------------|---------|
| 1 | `sigma_id` | String | Unique SIGMA identifier | `HL-ISO-15189-2022` |
| 2 | `entry_type` | Enum | Standards Body / Standard / Framework / Treaty / Guideline / Regulation / Classification / Code of Practice / Recommendation | `Standard` |
| 3 | `meta_layer` | Enum | L1 Life Sciences / L2 Physical Sciences / L3 Society & Governance / L4 Economy & Trade / L5 Technology & Infrastructure / L6 Environment | `L1 Life Sciences` |
| 4 | `domain` | String (from 40-domain taxonomy) | Primary domain | `Health & Medical` |
| 5 | `sub_domain` | String | Sub-category within domain | `Clinical Laboratories` |
| 6 | `name_full` | String | Complete official name | `Medical laboratories — Requirements for quality and competence` |
| 7 | `name_short` | String | Common name / acronym | `ISO 15189` |
| 8 | `standard_id` | String | Official identifier from issuing body | `ISO 15189:2022` |
| 9 | `issuer` | String | Name of issuing body | `ISO (TC 212)` |
| 10 | `issuer_type` | Enum | UN Agency / Treaty Body / ISO / IEC / ITU / Industry SDO / Professional Body / NGO / Intergovernmental / National Government | `ISO` |
| 11 | `governance_layer` | Enum | International / Regional / National | `International` |
| 12 | `geographic_scope` | String | Countries / regions where formally applicable | `Global — 175 ISO member countries` |
| 13 | `year_published` | Integer | Year of current edition | `2022` |
| 14 | `year_first` | Integer | Year first published | `2003` |
| 15 | `status` | Enum | Active / Withdrawn / Superseded / Under Development / Under Review | `Active` |
| 16 | `mandate` | Enum | Mandatory / Voluntary / Voluntary-with-regulatory-adoption / Treaty-binding | `Voluntary` |
| 17 | `sector_applicability` | String | Who must/should use this standard | `Healthcare laboratories / accreditation bodies / regulators` |
| 18 | `why_it_matters` | String | Plain-language explanation of significance | `Defines quality requirements for medical labs; basis for lab accreditation in 100+ countries` |
| 19 | `key_outputs` | String | Main standards/versions/elements | `ISO 15189:2022 (third edition); covers pre-examination, examination, post-examination processes` |
| 20 | `official_url` | URL | Primary source URL (authoritative, stable) | `https://www.iso.org/standard/76677.html` |
| 21 | `data_source` | String | Where this entry's data was obtained | `ISO Open Data CSV + manual verification` |
| 22 | `notes` | String | Any additional contextual information | `Replaced 2012 edition; significant restructuring of management requirements` |

## Google Sheet Curation Sync

The shared Google Sheet may include curation-only metadata columns after the 22 master fields, including `related_sigma_ids`, `llm_enriched`, and `last_updated`. These fields are useful for editorial workflow and future enrichment, but they are not part of the published master release schema yet.

Run `make sync-google-sheet` to export the Sheet into `data/processed/google_sheet_master.csv`. The sync script keeps only the 22 master fields so existing validation, release builds, and GitHub Pages downloads remain compatible.

## Supplementary Entity Tables

### Standards Bodies Register

One record per issuing organisation.

Fields: `org_id`, `org_name`, `org_acronym`, `org_type`, `founding_year`, `hq_country`, `hq_city`, `geographic_scope`, `governance_structure`, `iso_member` (Y/N), `wikidata_qid`, `official_url`, `linkedin_url`, `twitter_handle`, `standard_count`, `ics_scope`, `parent_org_id`.

### Relationships Map

Captures inter-standard and inter-organisation relationships.

Fields: `from_id`, `to_id`, `relationship_type`, `confidence`, `source_url`, `notes`.

Allowed `relationship_type` values: `references`, `supersedes`, `adopted_by`, `implements`, `aligned_with`, `referenced_by`, `harmonised_with`, `national_adoption_of`, `inspires`.

Allowed `confidence` values: `source-confirmed`, `curator-reviewed`, `llm-suggested`. LLM-suggested relationships must not be published as final graph edges until a human reviewer confirms the source.

Relationship CSVs are validated by `scripts/validate_relationships.py`. Empty header-only templates are allowed, but published rows require `from_id`, `to_id`, `relationship_type`, `confidence`, and `source_url`.

### Ratification & Adoption Tracker

For treaty and convention entries only. One row per country-per-treaty.

Fields: `sigma_id`, `country_iso3`, `country_name`, `status` (signatory / ratified / acceded / not party), `date`, `reservations`, `source_url`.

## ID Convention

SIGMA IDs follow a deterministic, human-readable pattern:

`[DOMAIN_CODE]-[ISSUER_CODE]-[STD_NUMBER]-[YEAR]`

Examples:
- `HL-ISO-15189-2022` — Health, ISO standard 15189, 2022 edition
- `HR-UN-CRC-1989` — Human Rights, UN Convention, CRC, 1989
- `DG-IETF-RFC9110-2022` — Digital, IETF, RFC 9110, 2022
- `FS-CAC-GL21-2021` — Food Safety, Codex Alimentarius Commission, GL 21, 2021
- `FI-BCBS-BASELIII-2010` — Finance, BCBS, Basel III, 2010
- `HM-IASC-SPHERE-2018` — Humanitarian, IASC/Sphere, 2018 edition
