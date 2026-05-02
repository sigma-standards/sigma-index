from pathlib import Path


CI_WORKFLOW = Path(".github") / "workflows" / "ci.yml"
WORKFLOW_DIR = Path(".github") / "workflows"


def test_ci_workflow_publishes_validation_reports():
    content = CI_WORKFLOW.read_text(encoding="utf-8")

    assert "make PYTHON=python3 validate" in content
    assert "make PYTHON=python3 release" in content
    assert "Upload validation reports" in content
    assert "actions/upload-artifact" in content
    assert "name: sigma-validation-reports" in content
    assert "data/reports/*.csv" in content
    assert "docs/QUALITY_GATE.md" in content
    assert "docs/RESEARCH_TASKS.md" in content
    assert "docs/RELATIONSHIP_QUALITY.md" in content


def test_ci_workflow_publishes_release_artifact_manifest():
    content = CI_WORKFLOW.read_text(encoding="utf-8")

    assert "Upload release manifest" in content
    assert "name: sigma-release-manifest" in content
    assert "dist/api_index.json" in content
    assert "dist/domain_coverage.csv" in content


def test_workflows_use_make_python_override_for_python_scripts():
    for workflow_path in WORKFLOW_DIR.glob("*.yml"):
        content = workflow_path.read_text(encoding="utf-8")
        assert "python3 scripts/" not in content
