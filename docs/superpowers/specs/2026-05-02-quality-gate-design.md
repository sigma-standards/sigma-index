# Phase 9A Quality Gate Design

## Purpose

Phase 9A adds a deterministic release quality gate before broader publication and community launch work. The first gate focuses on checks that are stable in CI and do not depend on live source availability.

## Scope

The quality gate scans `data/processed/*.csv` files that contain `sigma_id` and writes:

- `data/reports/quality_gate.csv`
- `docs/QUALITY_GATE.md`

The first checks cover duplicate `sigma_id` values, missing required master-schema fields, and malformed `official_url` values. Live URL reachability is intentionally excluded from the release gate because many source sites block HEAD requests, rate-limit automated traffic, or return transient network errors.

## Data Rules

- Duplicate published IDs are critical failures.
- Missing required master-schema values are critical failures.
- Official URLs must be HTTP or HTTPS.
- Reports must be generated with only the Python standard library.

## Testing

Tests create temporary processed datasets and verify both clean-pass output and fail output for duplicate IDs, missing fields, and malformed URLs.
