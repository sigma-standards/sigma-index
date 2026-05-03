# Pasted Resource Triage

This report records the files pasted into the repository root on 2026-05-04 and the decision taken for each resource. The goal was to incorporate useful SIGMA-adjacent signal while removing raw, duplicate, sensitive, bulky, or out-of-scope material.

## Incorporated Artifacts

- `data/staging/master_directory_global_standards_v2_0.csv` — CSV extract of the workbook master directory with 516 standards-body/framework entries.
- `data/staging/bangladesh_fhir_canonical_resources.csv` — canonical metadata extracted from the Bangladesh FHIR IG archive.
- `data/staging/bangladesh_shr_link_inventory.csv` — 211 public SHR/DGHS link records converted from `links.json`.
- `data/staging/pasted_resource_inventory.csv` — file-level inventory, hash, action, relevance, and rationale.

## Incorporated As Notes Only

The following resources were relevant but were not committed as raw source files: global health standards narratives, WHO PEN implementation notes, Shared Health Record component notes, FreeSHR playbook notes, and the SIGMA external gap/roadmap review. Their useful role is captured in this report and in the staging inventory.

## Removed Instead Of Committed

Raw `.docx` API files were removed because they contained credential-like examples, endpoint examples, email addresses, and personal-data examples. The 24 MB FHIR IG archive was reduced to canonical metadata. Claude/browser export HTML and asset folders were removed as runtime exports. Duplicate SHR technical detail files were removed. Separate ZarishSphere platform package/catalog files were removed as out of scope for this SIGMA repository.

## Candidate Follow-Up Work

- Review `data/staging/master_directory_global_standards_v2_0.csv` against current SIGMA processed and national standards body data before promoting any rows.
- Use `data/staging/bangladesh_fhir_canonical_resources.csv` to plan a Bangladesh Digital Health/FHIR standards slice.
- Use `data/staging/bangladesh_shr_link_inventory.csv` as a URL/source map for a future health interoperability source registry update.
- Do not reintroduce raw API documents unless they are redacted first.

## Decision Table

| Resource | Action | Rationale | Derived Artifact |
|---|---|---|---|
| `GLOBAL_STANDARD.md` | incorporated-summary | Useful narrative on WHO, ISO, IEC, HL7, SNOMED, ICH, CIOMS, Codex, regional and national implementation layers. | `docs/PASTED_RESOURCE_TRIAGE.md` |
| `STANDARD_BODIES_STAKEHOLDERS_TERMS.md` | incorporated-summary | Useful glossary for health standards bodies, WHO PEN roles, data standards, and implementation pathways. | `docs/PASTED_RESOURCE_TRIAGE.md` |
| `WHO_PEN_Implementation.md` | incorporated-summary | Useful process model connecting guideline development, national adaptation, service delivery, data, M&E, and feedback loops. | `docs/PASTED_RESOURCE_TRIAGE.md` |
| `SIGMA_Deep_Analysis_Gaps_and_Full_Roadmap (2).md` | incorporated-summary | Useful external analysis but not treated as authoritative because it may be stale relative to current repo state. | `docs/PASTED_RESOURCE_TRIAGE.md` |
| `MASTER_DIRECTORY_Global_Standards_v2_0.xlsx` | converted-to-staging-csv | Converted workbook master directory sheet to CSV staging extract. | `data/staging/master_directory_global_standards_v2_0.csv` |
| `full-ig.zip` | converted-to-staging-csv | Extracted canonical resource metadata only; raw 24MB IG archive removed. | `data/staging/bangladesh_fhir_canonical_resources.csv` |
| `links.json` | converted-to-staging-csv | Converted 211 link records to CSV staging inventory. | `data/staging/bangladesh_shr_link_inventory.csv` |
| `HRIS API For SHR.docx` | rejected-sensitive-raw | Relevant but contains example auth tokens, client IDs, email addresses, and personal-data examples; raw document removed, not committed. | `none` |
| `HRIS API For SHR(1).docx` | removed-duplicate | Exact duplicate by SHA-256; removed. | `none` |
| `SHR API Doc V2.0.docx` | rejected-sensitive-raw | Relevant but contains endpoint and credential examples; raw document removed, not committed. | `none` |
| `SHR Encounter API And Terminoloy Synchronization .docx` | rejected-sensitive-raw | Relevant but contains API/auth examples and large XML examples; raw document removed, not committed. | `none` |
| `Technical Details – Shared Health Record (EN).md` | incorporated-summary | Useful public SHR component taxonomy; duplicate variants removed. | `docs/PASTED_RESOURCE_TRIAGE.md` |
| `FreeSHR-Playbooks – Shared Health Record (EN).md` | incorporated-summary | Useful for HIE/SHR implementation context, but not direct SIGMA release data. | `docs/PASTED_RESOURCE_TRIAGE.md` |
| `CATALOGS.md` | rejected-out-of-scope | Mostly separate platform catalog, not SIGMA standards-index source data. | `none` |
| `Zarish Sphere platform development lifecycle - Claude.md` | rejected-out-of-scope | Separate product/platform planning material, not SIGMA source data. | `none` |
| `build_sigma_notebook.py` | rejected-obsolete-tooling | Overlaps older Google Drive/Sheets architecture and contains notebook-generation code not used by current GitHub-first pipeline. | `none` |
| `files.zip` | rejected-out-of-scope | Separate platform package; not SIGMA standards-index source data. | `none` |
| `Shared Health Record technical architecture overview - Claude.html` | rejected-runtime-export | Browser/chat export with companion asset folder; not a clean source artifact. | `none` |
