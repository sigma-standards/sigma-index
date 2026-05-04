from pathlib import Path


RELEASE_GOVERNANCE = Path("docs/RELEASE_GOVERNANCE.md")


def test_release_governance_doc_has_v1_release_checklist():
    content = RELEASE_GOVERNANCE.read_text(encoding="utf-8")

    assert "SIGMA v1.0 Release Checklist" in content
    assert "git tag -a v1.0.0" in content
    assert "GitHub release" in content
    assert "CHANGELOG.md" in content
    assert "sigma-release-artifacts" in content
    assert "Zenodo" in content


def test_release_governance_doc_defines_release_notes_template():
    content = RELEASE_GOVERNANCE.read_text(encoding="utf-8")

    assert "Release Notes Template" in content
    assert "Validation Evidence" in content
    assert "Downloadable Artifacts" in content
    assert "Archival Record" in content
    assert "Known Limitations" in content
