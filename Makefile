.PHONY: validate relationships release clean

validate:
	python3 scripts/validate_domain_registry.py
	python3 scripts/validate_schema.py data/processed
	python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed
	PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/*.py

relationships:
	python3 scripts/extract_relationships.py
	python3 scripts/validate_relationships.py data/relationships --processed-dir data/processed

release: relationships validate
	python3 scripts/build_domain_coverage.py
	python3 scripts/build_release.py

clean:
	rm -rf dist build *.egg-info scripts/__pycache__ .pytest_cache
