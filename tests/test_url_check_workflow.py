from pathlib import Path


URL_CHECK_WORKFLOW = Path(".github") / "workflows" / "url_check.yml"


def test_url_check_workflow_installs_only_runtime_dependency_needed_by_script():
    content = URL_CHECK_WORKFLOW.read_text(encoding="utf-8")

    assert "pip install requests" in content
    assert "pip install requests pandas" not in content
    assert "make PYTHON=python check-urls" in content
