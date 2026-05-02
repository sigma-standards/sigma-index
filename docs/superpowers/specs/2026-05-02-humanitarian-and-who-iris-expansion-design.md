# Phase 2C and 2D Humanitarian and WHO IRIS Expansion Design

## Purpose

Phase 2C extends Domain 17 beyond the existing Sphere WASH record with source-confirmed humanitarian standards from CHS, INEE, IASC, UNHCR, and WHO Emergency Medical Teams. Phase 2D adds a conservative WHO IRIS/OAI metadata harvester that stages candidate normative WHO records for curator review before publication.

## Scope

Phase 2C writes canonical 22-field SIGMA records from `data/reference/humanitarian_priority_sources.csv` to `data/processed/humanitarian_priority_standards.csv`.

Phase 2D reads WHO IRIS OAI-PMH XML, filters for likely normative records using explicit terms such as `guideline`, `standard`, `classification`, `model list`, `manual`, and `framework`, and writes staged metadata to `data/staging/who_iris_filtered_metadata.csv`. Staged records are not included in the release bundle until they are manually promoted into a processed dataset.

## Architecture

Both pipelines use Python standard-library CSV/XML processing. Humanitarian ingestion mirrors the Phase 2A and 2B curated-source pattern. WHO IRIS harvesting supports fixture-based deterministic runs and optional live OAI-PMH fetching, but the Makefile target uses the fixture so CI remains stable.

## Data Rules

- Humanitarian records must use authoritative public URLs.
- WHO IRIS records must remain staged with `review_status=needs-curator-review`.
- No WHO IRIS staged row enters `data/processed` automatically.
- Duplicate IDs against seed records are rejected in the curated humanitarian ingestor.

## Testing

Tests verify that humanitarian records preserve the master schema and avoid seed duplicates. WHO IRIS tests verify filtering, exclusion of general reports, record-type labels, and staging fields.
