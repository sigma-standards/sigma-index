# SIGMA — Unified Global Standards Index

**Free. Complete. Machine-readable. Human-navigable.**

SIGMA is an open project to build the world’s most complete public index of global standards, treaties, frameworks, guidelines, and classification systems.

## Repository Contents

- `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md` — full strategy and execution plan (v1.1 enhanced roadmap).
- `index.md` — lightweight public landing-page copy.
- `data/raw/iso/ICS.csv` — ISO International Classification for Standards seed data.
- `data/raw/iso/iso_deliverables_metadata.csv` — ISO deliverables metadata.
- `data/raw/iso/iso_technical_committees.csv` — ISO technical committee seed data.
- `SCHEMA.md` — data schema documentation.
- `CONTRIBUTING.md` — contribution guidelines.
- `CODE_OF_CONDUCT.md` — code of conduct.
- `pyproject.toml` — Python project configuration.
- `scripts/` — data processing scripts.
- `data/reference/domain_taxonomy.csv` — canonical 40-domain registry.
- `data/reference/source_registry.csv` — source map for all 40 domains.
- `data/reports/domain_coverage.csv` — generated coverage report.
- `data/relationships/relationships_template.csv` — relationship map template for graph edges.
- `.github/` — GitHub configuration (issues, workflows).

## Current Data Scope

- Generated release bundle: **88,083 master entries** and **20,130 relationship edges**.
- All **40 canonical domains** are represented through bulk ingestors and curated seed records.
- Current processed sources include ISO metadata, IETF RFC metadata, ILO standards, and Wikidata standards-body metadata.
- Raw ISO technical committees and ICS seed datasets are included in `data/raw/iso/`.
- Additional sources (UN, WHO, Codex, ITU, W3C, national bodies, etc.) remain planned in phased ingestion.

## Setup

1. Create a virtual environment: `python3 -m venv venv`
2. Activate it: `source venv/bin/activate`
3. Install dependencies: `pip install -e .`

## Validation

- Master entry schema: `python3 scripts/validate_schema.py data/processed`
- Relationship maps: `python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed`
- Full local check: `make validate`

## Relationship Extraction

Generate high-confidence relationship edges:

```bash
python3 scripts/extract_relationships.py
python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed
```

Or run `make relationships`.

## Release Build

Build downloadable artifacts in `dist/`:

```bash
make release
```

The release build currently emits:

- `sigma_master.csv`
- `sigma_master.json`
- `sigma_master.jsonl`
- `relationships.csv`
- `relationships.json`
- `api_index.json`
- `domain_taxonomy.csv`
- `source_registry.csv`
- `domain_coverage.csv`

`dist/` is ignored by Git because release artifacts are generated outputs.

## Publishing

GitHub Actions includes:

- Schema validation on pull requests and main-branch pushes.
- Release artifact build/upload on main-branch pushes.
- GitHub Pages publishing for a static download page and generated data files.

Enable Pages in repository settings with **GitHub Actions** as the source, then run the `Publish Pages` workflow.

## Enhancement Focus Added (May 2026)

The plan now explicitly includes:

- Hybrid architecture (tabular + knowledge graph).
- Automated freshness pipelines for daily/weekly source sync.
- LLM-assisted enrichment and validation workflows.
- Multilingual, accessibility, API, and improved UX roadmap.
- Governance/partnership strategy for long-term sustainability.

## Airtable / MCP Note

No Airtable MCP server is required for the current build. The project plan uses free/open collaboration paths: Google Sheets for early curation and NocoDB as the Airtable-style open-source option if a database UI is needed.

## Contributing

1. Open an issue with a source-backed addition/correction.
2. Submit a pull request with schema-compliant updates.
3. Include source URLs for all added or changed records.

## License

- Data and documentation: **CC BY 4.0** (see `LICENSE`).
