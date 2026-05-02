# Phase 2B Codex Priority Ingestion Design

## Purpose

Phase 2B expands Life Sciences & Health coverage into Domain 2, Food Safety & Agriculture, using source-confirmed Codex Alimentarius records. The first Codex slice should add high-value cross-cutting Codex standards and guidelines without attempting a full 3,000+ record bulk scrape.

## Scope

The ingestor reads `data/reference/codex_priority_sources.csv` and writes canonical 22-field SIGMA records to `data/processed/codex_standards.csv`.

Initial records cover:

- Food hygiene and HACCP foundations.
- Food additives, contaminants, analysis, and sampling.
- Nutrition labelling.
- Food import/export inspection and certification systems.

## Architecture

The source table is a curated CSV with the exact 22-field SIGMA schema. `scripts/process_codex.py` validates required fields, rejects duplicate source IDs, sorts records by `sigma_id`, and writes the processed dataset. `make codex` runs the processor and validates its output; `make validate` includes it before whole-repo schema validation.

## Data Rules

- Use official FAO/WHO Codex pages or Codex-hosted document links.
- Do not duplicate the existing `FS-CAC-CXS1-1985` seed record.
- Keep records source-confirmed and human-reviewable.
- Preserve the 22-field master schema exactly.
- Avoid live network dependency in release builds.

## Testing

Tests verify schema preservation, Domain 2 coverage, multiple Codex document types, official HTTPS URLs, and no duplicate IDs against the existing seed file.
