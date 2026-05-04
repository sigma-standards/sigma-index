from pathlib import Path


AUDIT_DOC = Path("docs/superpowers/plans/2026-05-04-repo-branch-and-full-implementation-audit.md")


def test_repo_branch_script_audit_records_post_merge_cleanup():
    content = AUDIT_DOC.read_text(encoding="utf-8")

    assert "## Post-Merge Cleanup" in content
    assert "`main` is synced with `origin/main` at `1a79ece95b10da9a23a06d85101b8356ab51ec65`" in content
    assert "Remote branches are clean: only `main` remains." in content
    assert "Local branches are clean: only `main` remains." in content
    assert "Only the primary worktree remains at `/home/health-pm/sigma-index`." in content
    assert "`sigma_full_implementation.py` remains untracked locally" in content
