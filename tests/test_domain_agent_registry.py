import csv
import json
import subprocess
from pathlib import Path


REGISTRY = Path("data/reference/domain_worker_registry.csv")
RUNNER = Path("scripts/run_domain_worker.py")
WORKFLOW = Path(".github/workflows/domain_agents.yml")
SETUP_GUIDE = Path("docs/GITHUB_AGENTIC_SETUP_GUIDE.md")


def test_domain_worker_registry_declares_safe_free_agents():
    rows = list(csv.DictReader(REGISTRY.read_text(encoding="utf-8").splitlines()))

    assert len(rows) >= 8
    assert {row["agent_id"] for row in rows} >= {
        "health",
        "food",
        "ict",
        "sustainability",
        "safety",
        "culture",
        "sports",
        "national-bodies",
    }

    for row in rows:
        assert row["make_target"]
        assert row["human_review_required"] == "true"
        assert row["writes_directly_to_main"] == "false"
        assert row["retry_limit"].isdigit()


def test_domain_agent_runner_dry_run_writes_state_report(tmp_path):
    state_path = tmp_path / "state.json"

    result = subprocess.run(
        [
            "python3",
            str(RUNNER),
            "--agent",
            "health",
            "--dry-run",
            "--state-path",
            str(state_path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert "DRY RUN domain agent: health" in result.stdout
    assert state["agent_id"] == "health"
    assert state["mode"] == "dry-run"
    assert state["human_review_required"] is True
    assert "make" in state["planned_command"][0]


def test_domain_agent_workflow_uses_pr_gates_and_secret_names_only():
    content = WORKFLOW.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in content
    assert "schedule:" in content
    assert "pull-requests: write" in content
    assert "contents: write" in content
    assert "scripts/run_domain_worker.py" in content
    assert "git checkout -B \"${branch_name}\"" in content
    assert "gh pr create" in content
    assert "XAI_API_KEY: ${{ secrets.XAI_API_KEY }}" in content
    assert "DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}" in content
    assert "HF_TOKEN: ${{ secrets.HF_TOKEN }}" in content
    assert "APIFY_TOKEN: ${{ secrets.APIFY_TOKEN }}" in content
    assert "sk-" not in content
    assert "xai-" not in content


def test_github_agentic_setup_guide_has_fillable_secret_template():
    content = SETUP_GUIDE.read_text(encoding="utf-8")

    assert "Fillable Secrets Template" in content
    assert "| `XAI_API_KEY` |" in content
    assert "| `DEEPSEEK_API_KEY` |" in content
    assert "| `NCBI_API_KEY` |" in content
    assert "| `APIFY_TOKEN` |" in content
    assert "| `HF_TOKEN` |" in content
    assert "Do not paste secrets into commits" in content
    assert "Settings -> Secrets and variables -> Actions" in content
