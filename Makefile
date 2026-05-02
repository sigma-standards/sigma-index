.PHONY: validate relationships research-tasks quality-gate health-priority codex humanitarian-priority who-iris-stage sustainability-reporting nist-priority w3c-priority itu-priority etsi-priority open-ict-priority iec-priority national-standards-bodies release site pagefind-search sync-google-sheet clean

validate:
	python3 scripts/validate_domain_registry.py
	python3 scripts/build_research_task_report.py
	python3 scripts/build_quality_gate.py
	python3 scripts/process_health_priority.py
	python3 scripts/process_codex.py
	python3 scripts/process_humanitarian_priority.py
	python3 scripts/process_sustainability_reporting.py
	python3 scripts/process_nist_priority.py
	python3 scripts/process_w3c_priority.py
	python3 scripts/process_itu_priority.py
	python3 scripts/process_etsi_priority.py
	python3 scripts/process_open_ict_priority.py
	python3 scripts/process_iec_priority.py
	python3 scripts/process_national_standards_bodies.py
	python3 scripts/harvest_who_iris.py --input-xml data/reference/who_iris_oai_sample.xml
	python3 scripts/validate_schema.py data/processed
	python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed
	PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/*.py

relationships:
	python3 scripts/extract_relationships.py
	python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed

research-tasks:
	python3 scripts/build_research_task_report.py

quality-gate:
	python3 scripts/build_quality_gate.py

health-priority:
	python3 scripts/process_health_priority.py
	python3 scripts/validate_schema.py data/processed/health_priority_standards.csv

codex:
	python3 scripts/process_codex.py
	python3 scripts/validate_schema.py data/processed/codex_standards.csv

humanitarian-priority:
	python3 scripts/process_humanitarian_priority.py
	python3 scripts/validate_schema.py data/processed/humanitarian_priority_standards.csv

who-iris-stage:
	python3 scripts/harvest_who_iris.py --input-xml data/reference/who_iris_oai_sample.xml

sustainability-reporting:
	python3 scripts/process_sustainability_reporting.py
	python3 scripts/validate_schema.py data/processed/sustainability_reporting_standards.csv

nist-priority:
	python3 scripts/process_nist_priority.py
	python3 scripts/validate_schema.py data/processed/nist_priority_standards.csv

w3c-priority:
	python3 scripts/process_w3c_priority.py
	python3 scripts/validate_schema.py data/processed/w3c_standards.csv

itu-priority:
	python3 scripts/process_itu_priority.py
	python3 scripts/validate_schema.py data/processed/itu_recommendations.csv

etsi-priority:
	python3 scripts/process_etsi_priority.py
	python3 scripts/validate_schema.py data/processed/etsi_standards.csv

open-ict-priority:
	python3 scripts/process_open_ict_priority.py
	python3 scripts/validate_schema.py data/processed/open_ict_standards.csv

iec-priority:
	python3 scripts/process_iec_priority.py
	python3 scripts/validate_schema.py data/processed/iec_standards.csv

national-standards-bodies:
	python3 scripts/process_national_standards_bodies.py
	python3 scripts/validate_schema.py data/processed/national_standards_bodies.csv

release: relationships validate
	python3 scripts/build_domain_coverage.py
	python3 scripts/build_release.py

site: release
	python3 scripts/build_static_site.py

pagefind-search: site
	npx -y pagefind@1.5.2 --site public --output-subdir pagefind

sync-google-sheet:
	python3 scripts/sync_google_sheet.py
	python3 scripts/validate_schema.py data/processed/google_sheet_master.csv

clean:
	rm -rf dist build public *.egg-info scripts/__pycache__ tests/__pycache__ .pytest_cache
	rm -f rfc-index.txt data/raw/iso/*.temp
