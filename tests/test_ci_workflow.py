from pathlib import Path


CI_WORKFLOW = Path(".github") / "workflows" / "ci.yml"


def test_ci_workflow_publishes_validation_reports():
    content = CI_WORKFLOW.read_text(encoding="utf-8")

    assert "make validate" in content
    assert "make release" in content
    assert "Upload validation reports" in content
    assert "actions/upload-artifact" in content
    assert "name: sigma-validation-reports" in content
    assert "data/reports/*.csv" in content
    assert "docs/QUALITY_GATE.md" in content
    assert "docs/RESEARCH_TASKS.md" in content


def test_ci_workflow_publishes_release_artifact_manifest():
    content = CI_WORKFLOW.read_text(encoding="utf-8")

    assert "Upload release manifest" in content
    assert "name: sigma-release-manifest" in content
    assert "dist/api_index.json" in content
    assert "dist/domain_coverage.csv" in content
