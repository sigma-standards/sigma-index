# Phase 2A Health Priority Ingestion Design

## Purpose

Phase 2A adds a small, source-confirmed ingestion path for high-impact life-science, health, humanitarian, and WASH standards. The first slice must expand beyond one-record domain seeds while avoiding duplicate `sigma_id` values already present in `data/processed/domain_seed_standards.csv`.

## Scope

The ingestor reads a curated source table at `data/reference/health_priority_sources.csv` and writes canonical 22-field SIGMA records to `data/processed/health_priority_standards.csv`.

Initial records cover:

- WHO classification and clinical/public-health guidance for Domain 1, Health & Medical.
- WHO WASH guidance for Domain 33, Water, Sanitation & Hygiene.
- Sphere WASH minimum standards for Domain 17, Humanitarian & Emergency Response, where the official source is a standards body handbook rather than a WHO publication.

## Architecture

The source table is intentionally human-reviewable CSV. `scripts/process_health_priority.py` validates that each source row already contains every master schema field, rejects duplicate `sigma_id` values inside the source file, and writes a stable sorted processed CSV. `make health-priority` runs the ingestor and validates only the generated file; `make validate` includes it through the existing processed-data validation path.

## Data Rules

- Do not fetch live content during release builds.
- Use only authoritative public source URLs.
- Preserve the 22-field master schema exactly.
- Keep entries source-confirmed, not LLM-generated.
- Use unique IDs that do not duplicate existing seed IDs.

## Testing

Tests verify that the ingestor writes the expected records, preserves the schema, includes both Domain 1 and Domain 33 coverage, and avoids known duplicate seed IDs.
