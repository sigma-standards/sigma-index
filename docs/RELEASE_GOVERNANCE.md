# Release Governance

This document gives maintainers a repo-native checklist for producing durable SIGMA releases. It focuses on the v1.0 public launch path from the roadmap: version tag, GitHub release notes, downloadable artifacts, and archival copy.

## SIGMA v1.0 Release Checklist

- [ ] Confirm `main` is synced with `origin/main` and all launch PRs are merged.
- [ ] Freeze v1.0 source data after final domain, URL, duplicate, and completeness review.
- [ ] Update `CHANGELOG.md` by moving completed v1.0 items out of `Unreleased`.
- [ ] Run `.venv/bin/python -m pytest`.
- [ ] Run `make validate`.
- [ ] Run `make release` and confirm the local release bundle is complete.
- [ ] Confirm downloadable artifacts exist for CSV, JSON, JSONL, relationship exports, domain coverage, source registry, quality gate, and API index outputs.
- [ ] Create the annotated version tag with `git tag -a v1.0.0 -m "SIGMA v1.0.0"` after validation passes.
- [ ] Push the tag with `git push origin v1.0.0`.
- [ ] Create the GitHub release from `v1.0.0` and paste the release notes template below.
- [ ] Attach or link the `sigma-release-artifacts` download from the successful Release Build workflow.
- [ ] Archive the exact release artifact set on Zenodo or another open repository and add the DOI or persistent URL to the GitHub release.
- [ ] Rebuild and confirm GitHub Pages after the release is published.

## Release Notes Template

Use this template for the v1.0 GitHub release body.

```markdown
# SIGMA v1.0.0

SIGMA v1.0.0 is the first public release of the Unified Global Standards Index.

## Highlights

- Public machine-readable index of global standards, treaties, frameworks, guidelines, classification systems, and standards bodies.
- GitHub Pages browsing and search surface.
- Release bundle generated from committed source and reference data.

## Validation Evidence

- `.venv/bin/python -m pytest`: PASS
- `make validate`: PASS
- `make release`: PASS
- GitHub Actions Release Build run: <link>

## Downloadable Artifacts

- `sigma_master.csv`
- `sigma_master.json`
- `sigma_master.jsonl`
- relationship exports
- domain coverage report
- source registry export
- quality gate report
- API index

## Archival Record

- Git tag: `v1.0.0`
- GitHub release: <link>
- Zenodo DOI or persistent archive URL: <link>

## Known Limitations

- <List launch-scope limitations, excluded domains, or data-quality caveats.>

## Corrections

Report corrections through GitHub Issues: https://github.com/sigma-standards/sigma-index/issues
```

## Patch And Minor Release Notes

- Patch releases, such as `v1.0.1`, should document URL corrections, factual fixes, status updates, and changed artifacts.
- Minor releases, such as `v1.1.0`, should document new entries, domains, schema additions, and any migration notes.
- Every release should keep `CHANGELOG.md`, GitHub release notes, generated artifacts, and archival records aligned.
