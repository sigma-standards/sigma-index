# Pages Redesign And Data Surfaces Design

## Scope

This change improves the published GitHub Pages experience for SIGMA and makes the current data bundle easier to navigate. It does not claim to complete live ingestion for every standards source worldwide; that remains a phased data program. This delivery exposes the current all-domain registry, processed layers, documentation, downloads, and synchronization status in a polished static site.

## Architecture

The Pages workflow will call a repository script, `scripts/build_static_site.py`, after the release bundle is built. The script reads generated artifacts from `dist/` and registry data from `data/reference/`, then writes a dependency-free static site into `public/`.

## User Experience

The published site should include a designed header, navigation, a clear hero, metrics, download cards, data layer cards, all-domain coverage, source registry links, documentation links, and a footer. The page should render as a complete website on desktop and mobile using plain HTML and CSS.

## Data Surfaces

The site will show:

- entry and relationship counts from `dist/api_index.json`
- domain coverage from `dist/domain_coverage.csv`
- canonical domains from `data/reference/domain_taxonomy.csv`
- source registry entries from `data/reference/source_registry.csv`
- generated downloads copied from `dist/`
- documentation copied from repository markdown files

## Synchronization

Local publishing and GitHub Actions publishing should use the same script. The workflow will build release artifacts, then call `python3 scripts/build_static_site.py`, then upload `public/` to GitHub Pages. This keeps local previews and remote Pages synchronized.

## Testing

Tests will validate that the site builder creates `public/index.html`, includes navigation anchors, includes current metrics, includes all 40 domains, and copies downloads and docs into the expected folders.
