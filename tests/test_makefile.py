from pathlib import Path


def test_makefile_uses_virtualenv_python_variable():
    content = Path("Makefile").read_text(encoding="utf-8")

    assert "PYTHON ?= .venv/bin/python" in content
    assert "$(PYTHON) scripts/validate_domain_registry.py" in content
    assert "PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m py_compile scripts/*.py" in content
    assert "\tpython3 scripts/" not in content
