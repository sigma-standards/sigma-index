.PHONY: validate relationships research-tasks health-priority codex release site sync-google-sheet clean

validate:
	python3 scripts/validate_domain_registry.py
	python3 scripts/build_research_task_report.py
	python3 scripts/process_health_priority.py
	python3 scripts/process_codex.py
	python3 scripts/validate_schema.py data/processed
	python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed
	PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/*.py

relationships:
	python3 scripts/extract_relationships.py
	python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed

research-tasks:
	python3 scripts/build_research_task_report.py

health-priority:
	python3 scripts/process_health_priority.py
	python3 scripts/validate_schema.py data/processed/health_priority_standards.csv

codex:
	python3 scripts/process_codex.py
	python3 scripts/validate_schema.py data/processed/codex_standards.csv

release: relationships validate
	python3 scripts/build_domain_coverage.py
	python3 scripts/build_release.py

site: release
	python3 scripts/build_static_site.py

sync-google-sheet:
	python3 scripts/sync_google_sheet.py
	python3 scripts/validate_schema.py data/processed/google_sheet_master.csv

clean:
	rm -rf dist build public *.egg-info scripts/__pycache__ tests/__pycache__ .pytest_cache
