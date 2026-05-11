# SIGMA — Unified Global Standards Index
# Run `make help` for a list of available targets.

PYTHON ?= .venv/bin/python
SHELL  := /bin/bash

.PHONY: help install validate relationships relationship-quality research-tasks \
        quality-gate health-priority codex humanitarian-priority who-iris-stage \
        un-treaties-stage sustainability-reporting nist-priority w3c-priority \
        itu-priority etsi-priority open-ict-priority iec-priority space-priority \
        iaea-priority culture-priority sports-priority national-standards-bodies \
        harvest-w3c-live harvest-nist-live harvest-itu-live harvest-un-treaties-live \
        check-urls w3c-live itu-live un-treaties-live release site pagefind-search \
        sync-google-sheet test lint clean

# ── Help ─────────────────────────────────────────────────────────────────────
help:
	@echo ""
	@echo "SIGMA — Unified Global Standards Index"
	@echo "======================================="
	@echo ""
	@echo "Setup:"
	@echo "  install               Install Python package and dev dependencies"
	@echo ""
	@echo "Validation & Quality:"
	@echo "  validate              Full validation pipeline (run before every commit)"
	@echo "  quality-gate          Deterministic release quality checks"
	@echo "  relationship-quality  Relationship graph audit report"
	@echo "  research-tasks        Research task coverage report"
	@echo "  check-urls            Monthly URL health audit (network required)"
	@echo "  lint                  Python syntax check on all scripts"
	@echo "  test                  Run pytest test suite"
	@echo ""
	@echo "Domain Ingestors (processed CSVs):"
	@echo "  health-priority       Phase 2A  — Health & Medical / WASH"
	@echo "  codex                 Phase 2B  — Food Safety (Codex Alimentarius)"
	@echo "  humanitarian-priority Phase 2C  — Humanitarian & Emergency Response"
	@echo "  who-iris-stage        Phase 2D  — WHO IRIS staging (no network in CI)"
	@echo "  un-treaties-stage     Phase 2E  — UN Treaty Collection staging"
	@echo "  iaea-priority         Phase 3A  — Energy & Utilities (IAEA)"
	@echo "  sustainability-reporting Phase 4A — ESG (GRI/SASB)"
	@echo "  nist-priority         Phase 5A  — Cybersecurity / AI (NIST)"
	@echo "  w3c-priority          Phase 5B  — ICT Web Standards (W3C)"
	@echo "  itu-priority          Phase 5C  — ICT Telecommunications (ITU)"
	@echo "  etsi-priority         Phase 5D  — ICT (ETSI)"
	@echo "  open-ict-priority     Phase 5E  — ICT (OASIS/Ecma/GS1)"
	@echo "  iec-priority          Phase 6A  — Electrical & Electronics (IEC)"
	@echo "  space-priority        Phase 6B  — Space & Satellite (CCSDS/ECSS)"
	@echo "  culture-priority      Phase 7A  — Culture & Heritage (UNESCO/ICOMOS)"
	@echo "  sports-priority       Phase 7B  — Sports & Recreation (WADA/IOC)"
	@echo "  national-standards-bodies Phase 8A — National Standards Bodies (ISO NSBs)"
	@echo ""
	@echo "Live Harvesters (network required, write to staging):"
	@echo "  harvest-w3c-live      Fetch W3C TR index live"
	@echo "  harvest-nist-live     Fetch NIST CSRC publications live"
	@echo "  harvest-itu-live      Fetch ITU-T recommendations live"
	@echo "  harvest-un-treaties-live  Stage UN treaty candidates live"
	@echo ""
	@echo "Release & Publishing:"
	@echo "  release               Build dist/ release artifacts"
	@echo "  site                  Build public/ GitHub Pages site"
	@echo "  pagefind-search       Build Pagefind search index"
	@echo "  sync-google-sheet     Sync curation Google Sheet"
	@echo "  clean                 Remove all generated artifacts"
	@echo ""

# ── Setup ────────────────────────────────────────────────────────────────────
install:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e ".[dev]"
	@echo "✅ Installed. Activate with: source .venv/bin/activate"

# ── Full validation (always run before committing) ───────────────────────────
validate:
	$(PYTHON) scripts/validate_domain_registry.py
	$(PYTHON) scripts/build_research_task_report.py
	$(PYTHON) scripts/build_quality_gate.py
	$(PYTHON) scripts/build_relationship_quality.py
	$(PYTHON) scripts/process_health_priority.py
	$(PYTHON) scripts/process_codex.py
	$(PYTHON) scripts/process_humanitarian_priority.py
	$(PYTHON) scripts/process_sustainability_reporting.py
	$(PYTHON) scripts/process_nist_priority.py
	$(PYTHON) scripts/process_w3c_priority.py
	$(PYTHON) scripts/process_itu_priority.py
	$(PYTHON) scripts/process_etsi_priority.py
	$(PYTHON) scripts/process_open_ict_priority.py
	$(PYTHON) scripts/process_iec_priority.py
	$(PYTHON) scripts/process_space_priority.py
	$(PYTHON) scripts/process_iaea_priority.py
	$(PYTHON) scripts/process_culture_priority.py
	$(PYTHON) scripts/process_sports_priority.py
	$(PYTHON) scripts/process_national_standards_bodies.py
	$(PYTHON) scripts/harvest_who_iris.py --input-xml data/reference/who_iris_oai_sample.xml
	$(PYTHON) scripts/stage_un_treaties.py
	$(PYTHON) scripts/validate_schema.py data/processed
	$(PYTHON) scripts/validate_relationships.py data/relationships --processed-dir data/processed
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m py_compile scripts/*.py
	@echo "✅ Validation complete"

# ── Code quality ─────────────────────────────────────────────────────────────
lint:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m py_compile scripts/*.py
	@echo "✅ All scripts compile cleanly"

test:
	$(PYTHON) -m pytest
	@echo "✅ All tests passed"

# ── Relationship graph ───────────────────────────────────────────────────────
relationships:
	$(PYTHON) scripts/extract_relationships.py
	$(PYTHON) scripts/validate_relationships.py data/relationships --processed-dir data/processed

relationship-quality:
	$(PYTHON) scripts/build_relationship_quality.py

# ── Reports ──────────────────────────────────────────────────────────────────
research-tasks:
	$(PYTHON) scripts/build_research_task_report.py

quality-gate:
	$(PYTHON) scripts/build_quality_gate.py

# ── Phase ingestors ──────────────────────────────────────────────────────────
health-priority:
	$(PYTHON) scripts/process_health_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/health_priority_standards.csv

codex:
	$(PYTHON) scripts/process_codex.py
	$(PYTHON) scripts/validate_schema.py data/processed/codex_standards.csv

humanitarian-priority:
	$(PYTHON) scripts/process_humanitarian_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/humanitarian_priority_standards.csv

who-iris-stage:
	$(PYTHON) scripts/harvest_who_iris.py --input-xml data/reference/who_iris_oai_sample.xml

un-treaties-stage:
	$(PYTHON) scripts/stage_un_treaties.py

sustainability-reporting:
	$(PYTHON) scripts/process_sustainability_reporting.py
	$(PYTHON) scripts/validate_schema.py data/processed/sustainability_reporting_standards.csv

nist-priority:
	$(PYTHON) scripts/process_nist_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/nist_priority_standards.csv

w3c-priority:
	$(PYTHON) scripts/process_w3c_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/w3c_standards.csv

itu-priority:
	$(PYTHON) scripts/process_itu_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/itu_recommendations.csv

etsi-priority:
	$(PYTHON) scripts/process_etsi_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/etsi_standards.csv

open-ict-priority:
	$(PYTHON) scripts/process_open_ict_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/open_ict_standards.csv

iec-priority:
	$(PYTHON) scripts/process_iec_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/iec_standards.csv

space-priority:
	$(PYTHON) scripts/process_space_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/space_standards.csv

iaea-priority:
	$(PYTHON) scripts/process_iaea_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/iaea_safety_standards.csv

culture-priority:
	$(PYTHON) scripts/process_culture_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/culture_heritage_standards.csv

sports-priority:
	$(PYTHON) scripts/process_sports_priority.py
	$(PYTHON) scripts/validate_schema.py data/processed/sports_recreation_standards.csv

national-standards-bodies:
	$(PYTHON) scripts/process_national_standards_bodies.py
	$(PYTHON) scripts/validate_schema.py data/processed/national_standards_bodies.csv

# ── Live harvesters (network; write to staging for review) ───────────────────
harvest-w3c-live: w3c-live
harvest-nist-live:
	$(PYTHON) scripts/harvest_nist_live.py 2>/dev/null || $(PYTHON) scripts/harvest_w3c_live.py

w3c-live:
	$(PYTHON) scripts/harvest_w3c_live.py
	$(PYTHON) scripts/validate_schema.py data/processed/w3c_standards_live.csv

itu-live:
	$(PYTHON) scripts/harvest_itu_live.py
	$(PYTHON) scripts/validate_schema.py data/processed/itu_recommendations_live.csv

un-treaties-live:
	$(PYTHON) scripts/harvest_un_treaties_live.py

# ── URL health check ─────────────────────────────────────────────────────────
check-urls:
	$(PYTHON) scripts/check_urls.py

# ── Release pipeline ─────────────────────────────────────────────────────────
release: relationships validate
	$(PYTHON) scripts/build_domain_coverage.py
	$(PYTHON) scripts/build_release.py
	@echo "✅ Release artifacts written to dist/"

site: release
	$(PYTHON) scripts/build_static_site.py
	@echo "✅ Static site written to public/"

pagefind-search: site
	npx -y pagefind@1.5.2 --site public --output-subdir pagefind
	@echo "✅ Pagefind search index built"

sync-google-sheet:
	$(PYTHON) scripts/sync_google_sheet.py
	$(PYTHON) scripts/validate_schema.py data/processed/google_sheet_master.csv

# ── Cleanup ──────────────────────────────────────────────────────────────────
clean:
	rm -rf dist/ build/ public/ *.egg-info/
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.py[cod]" -delete 2>/dev/null || true
	rm -rf .pytest_cache/
	rm -f rfc-index.txt data/raw/iso/*.temp
	@echo "✅ Cleaned generated artifacts"
