# Phase 8A National Standards Body Registry Design

## Purpose

Phase 8A starts the national standards body expansion with a source-backed registry slice. The goal is to add a repeatable ingestion pattern for ISO national member bodies before scaling toward the full ISO member network and regional NSB organizations.

## Scope

This slice creates `data/reference/national_standards_bodies_sources.csv` and transforms it into `data/processed/national_standards_bodies.csv`. The first batch covers 10 high-impact national standards bodies across North America, Europe, Asia, Latin America, and Oceania.

The source table records the country, region, acronym, full name, ISO membership type, official site, ISO member profile, and notes. The processor emits the 22-field SIGMA master schema with `entry_type=Standards Body`.

## Data Rules

- Every row must have a stable `NSB-` identifier.
- Every row must link both the official organization site and an ISO member profile.
- Records are published as national governance infrastructure, not as individual technical standards.
- This phase does not claim complete coverage of all ISO members.

## Testing

Tests verify master-schema output, required representative bodies, unique `NSB-` identifiers, official HTTPS links, and ISO source links.
