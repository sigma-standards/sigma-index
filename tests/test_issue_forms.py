from pathlib import Path


ISSUE_TEMPLATE_DIR = Path(".github") / "ISSUE_TEMPLATE"

EXPECTED_FORMS = {
    "missing_standard.yml": ["official_url", "issuing_body", "domain", "inclusion_reason"],
    "source_correction.yml": ["sigma_id", "field_name", "corrected_value", "source_url"],
    "duplicate_report.yml": ["primary_sigma_id", "duplicate_sigma_id", "evidence_url"],
    "broken_link.yml": ["sigma_id", "broken_url", "replacement_url"],
    "domain_expansion.yml": ["domain", "source_family", "official_catalogue_url"],
}


def test_structured_issue_forms_exist_for_review_workflows():
    for filename, required_ids in EXPECTED_FORMS.items():
        form_path = ISSUE_TEMPLATE_DIR / filename
        assert form_path.exists(), f"Missing issue form: {filename}"

        content = form_path.read_text(encoding="utf-8")

        assert "name:" in content
        assert "description:" in content
        assert "title:" in content
        assert "labels:" in content
        assert "body:" in content
        assert "type: markdown" in content

        for field_id in required_ids:
            assert f"id: {field_id}" in content


def test_issue_template_config_routes_blank_issues_to_discussions():
    config_path = ISSUE_TEMPLATE_DIR / "config.yml"
    assert config_path.exists()

    content = config_path.read_text(encoding="utf-8")

    assert "blank_issues_enabled: false" in content
    assert "SIGMA contribution guide" in content
    assert "https://github.com/sigma-standards/sigma-index/blob/main/CONTRIBUTING.md" in content
