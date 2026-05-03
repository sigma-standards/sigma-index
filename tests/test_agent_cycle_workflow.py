from pathlib import Path


AGENT_CYCLE_WORKFLOW = Path(".github") / "workflows" / "agent_cycle.yml"


def test_agent_cycle_workflow_exists_with_web_dispatch_selector():
    content = AGENT_CYCLE_WORKFLOW.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in content
    assert "agent_id:" in content
    assert "- all" in content
    assert "cycle_mode:" in content
    assert "- plan" in content
    assert "- run" in content
    assert "- follow-up" in content


def test_agent_cycle_workflow_uses_makefile_runner_and_artifacts():
    content = AGENT_CYCLE_WORKFLOW.read_text(encoding="utf-8")

    assert "python3 -m scripts.run_domain_worker" in content
    assert "--python python3" in content
    assert "make PYTHON=python3 validate" in content
    assert "make PYTHON=python3 release" in content
    assert "actions/upload-artifact" in content
    assert "data/reports/domain_agent_state_*.json" in content


def test_agent_cycle_workflow_creates_review_pr_without_direct_main_commit():
    content = AGENT_CYCLE_WORKFLOW.read_text(encoding="utf-8")

    assert "GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}" in content
    assert "gh pr create" in content
    assert "--base main" in content
    assert "git checkout -B" in content
    assert "git push --set-upstream origin" in content
    assert "git push origin main" not in content
    assert "git checkout main" not in content
