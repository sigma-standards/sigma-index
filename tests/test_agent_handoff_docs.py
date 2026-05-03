from pathlib import Path


ROOT_AGENTS = Path("AGENTS.md")
OPERATOR_DASHBOARD = Path("docs/OPERATOR_DASHBOARD.md")
MEMORY_HANDOFF = Path("docs/AGENT_MEMORY_HANDOFF.md")
COPILOT_INSTRUCTIONS = Path(".github/copilot-instructions.md")


def test_root_agents_file_defines_repo_operating_rules():
    content = ROOT_AGENTS.read_text(encoding="utf-8")

    assert "/home/health-pm/sigma-index" in content
    assert "sigma-standards/sigma-index" in content
    assert ".venv/bin/python" in content
    assert "make PYTHON=python3" in content
    assert "Do not commit local/runtime artifacts" in content
    assert "docs/GITHUB_AGENTIC_SETUP_GUIDE.md" in content


def test_operator_dashboard_separates_local_remote_and_generated_state():
    content = OPERATOR_DASHBOARD.read_text(encoding="utf-8")

    assert "Local Versus Remote Rules" in content
    assert "gh pr checks" in content
    assert "git fetch --all --prune" in content
    assert "dist/" in content
    assert "public/" in content
    assert "raw Codex runtime files" in content


def test_memory_handoff_excludes_raw_codex_runtime_paths():
    content = MEMORY_HANDOFF.read_text(encoding="utf-8")

    assert "safe repository-level memory handoff" in content
    assert "Do not commit:" in content
    assert "/home/health-pm/.codex/memories/" in content
    assert "raw subagent transcripts" in content
    assert "rewrite them into a short, safe repo document" in content


def test_copilot_instructions_point_to_agents_file():
    content = COPILOT_INSTRUCTIONS.read_text(encoding="utf-8")

    assert "Follow `AGENTS.md` first." in content
    assert "Do not commit secrets" in content
    assert "pull request review gates" in content
