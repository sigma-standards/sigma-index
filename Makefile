PYTHON ?= .venv/bin/python

.PHONY: validate relationships relationship-quality research-tasks quality-gate health-priority codex humanitarian-priority who-iris-stage un-treaties-stage sustainability-reporting nist-priority w3c-priority itu-priority etsi-priority open-ict-priority iec-priority space-priority iaea-priority culture-priority sports-priority national-standards-bodies release site pagefind-search sync-google-sheet clean

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

relationships:
	$(PYTHON) scripts/extract_relationships.py
	$(PYTHON) scripts/validate_relationships.py data/relationships --processed-dir data/processed

relationship-quality:
	$(PYTHON) scripts/build_relationship_quality.py

research-tasks:
	$(PYTHON) scripts/build_research_task_report.py

quality-gate:
	$(PYTHON) scripts/build_quality_gate.py

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

release: relationships validate
	$(PYTHON) scripts/build_domain_coverage.py
	$(PYTHON) scripts/build_release.py

site: release
	$(PYTHON) scripts/build_static_site.py

pagefind-search: site
	npx -y pagefind@1.5.2 --site public --output-subdir pagefind

sync-google-sheet:
	$(PYTHON) scripts/sync_google_sheet.py
	$(PYTHON) scripts/validate_schema.py data/processed/google_sheet_master.csv

clean:
	rm -rf dist build public *.egg-info scripts/__pycache__ tests/__pycache__ .pytest_cache
	rm -f rfc-index.txt data/raw/iso/*.temp
