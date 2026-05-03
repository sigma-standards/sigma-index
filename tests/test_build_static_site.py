import csv
import json
from pathlib import Path


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_fixture_repo(tmp_path):
    (tmp_path / "dist").mkdir()
    (tmp_path / "data" / "reference").mkdir(parents=True)

    (tmp_path / "dist" / "api_index.json").write_text(
        json.dumps(
            {
                "entry_count": 88083,
                "relationship_count": 20130,
                "files": {
                    "sigma_master.csv": "sigma_master.csv",
                    "api_index.json": "api_index.json",
                },
            }
        ),
        encoding="utf-8",
    )
    write_csv(
        tmp_path / "dist" / "sigma_master.csv",
        [
            {
                "sigma_id": "HL-WHO-IHR-2005",
                "entry_type": "standard",
                "meta_layer": "Life Sciences & Health",
                "domain": "Health & Medical",
                "sub_domain": "Public health emergency",
                "name_full": "International Health Regulations",
                "name_short": "IHR",
                "standard_id": "IHR (2005)",
                "issuer": "World Health Organization",
                "issuer_type": "UN specialized agency",
                "governance_layer": "Global",
                "geographic_scope": "Global",
                "year_published": "2005",
                "year_first": "1969",
                "status": "active",
                "mandate": "Treaty-binding",
                "sector_applicability": "Public health",
                "why_it_matters": "Core framework for cross-border public health risk response.",
                "key_outputs": "Notification, coordination, core capacities",
                "official_url": "https://www.who.int/health-topics/international-health-regulations",
                "data_source": "WHO",
                "notes": "fixture",
            },
            {
                "sigma_id": "CY-NIST-SP800-53R5",
                "entry_type": "standard",
                "meta_layer": "Technology & Infrastructure",
                "domain": "Cybersecurity & Data Privacy",
                "sub_domain": "Security controls",
                "name_full": "Security and Privacy Controls for Information Systems and Organizations",
                "name_short": "SP 800-53 Rev. 5",
                "standard_id": "NIST SP 800-53 Rev. 5",
                "issuer": "National Institute of Standards and Technology",
                "issuer_type": "National standards body",
                "governance_layer": "National",
                "geographic_scope": "United States",
                "year_published": "2020",
                "year_first": "2005",
                "status": "active",
                "mandate": "Voluntary-with-regulatory-adoption",
                "sector_applicability": "Cybersecurity",
                "why_it_matters": "Baseline controls for federal and enterprise systems.",
                "key_outputs": "Control catalog",
                "official_url": "https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final",
                "data_source": "NIST",
                "notes": "fixture",
            },
        ],
    )
    (tmp_path / "dist" / "api_index.json").write_text(
        json.dumps({"entry_count": 88083, "relationship_count": 20130}),
        encoding="utf-8",
    )
    (tmp_path / "dist" / "domain_coverage.csv").write_text(
        "domain,entry_count,source_count,relationship_count\nHealth,20,2,5\nAgriculture,10,1,2\n",
        encoding="utf-8",
    )

    write_csv(
        tmp_path / "data" / "reference" / "domain_taxonomy.csv",
        [
            {
                "domain_id": "health",
                "domain_name": "Health",
                "description": "Health standards and frameworks",
            },
            {
                "domain_id": "agriculture",
                "domain_name": "Agriculture",
                "description": "Agriculture and food standards",
            },
        ],
    )
    write_csv(
        tmp_path / "data" / "reference" / "source_registry.csv",
        [
            {
                "domain": "Health",
                "source_name": "WHO",
                "source_url": "https://www.who.int/",
                "source_type": "standards body",
                "sync_status": "planned",
            },
            {
                "domain": "Agriculture",
                "source_name": "Codex Alimentarius",
                "source_url": "https://www.fao.org/fao-who-codexalimentarius/",
                "source_type": "standards body",
                "sync_status": "planned",
            },
        ],
    )

    for filename in [
        "README.md",
        "SCHEMA.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "RESEARCH_PROJECT_PLAN_Global_Standards_Index.md",
    ]:
        (tmp_path / filename).write_text(f"# {filename}\n", encoding="utf-8")
    roadmap = tmp_path / "docs" / "superpowers" / "plans" / "2026-05-02-roadmap-to-100-percent-global-standards-index.md"
    roadmap.parent.mkdir(parents=True, exist_ok=True)
    roadmap.write_text("# Roadmap to 100 Percent\n\nhttps://www.iso.org/standards.html\n", encoding="utf-8")
    (tmp_path / "docs" / "RESEARCH_TASKS.md").write_text("# SIGMA Research Task Matrix\n", encoding="utf-8")
    (tmp_path / "docs" / "PROJECT_KNOWLEDGE_GRAPH.md").write_text("# Project Knowledge Graph\n", encoding="utf-8")
    (tmp_path / "docs" / "SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.md").write_text(
        "# SIGMA Gap Analysis and Enhancement Plan\n",
        encoding="utf-8",
    )
    (tmp_path / "docs" / "PROJECT_STATUS_REPORT_2026-05-02.md").write_text(
        "# SIGMA Project Status Report\n",
        encoding="utf-8",
    )


def test_build_site_creates_designed_navigation_and_metrics(tmp_path):
    from scripts.build_static_site import build_site

    make_fixture_repo(tmp_path)

    build_site(tmp_path)

    html = (tmp_path / "public" / "index.html").read_text(encoding="utf-8")
    css = (tmp_path / "public" / "assets" / "styles.css").read_text(encoding="utf-8")

    assert '<nav class="site-nav"' in html
    assert 'href="#downloads"' in html
    assert 'href="#domains"' in html
    assert "88,083" in html
    assert "20,130" in html
    assert "Health" in html
    assert "Agriculture" in html
    assert "Codex Alimentarius" in html
    assert "linear-gradient" in css


def test_build_site_renders_progress_and_owner_contact(tmp_path):
    from scripts.build_static_site import build_site

    make_fixture_repo(tmp_path)

    build_site(tmp_path)

    html = (tmp_path / "public" / "index.html").read_text(encoding="utf-8")

    assert 'id="progress"' in html
    assert 'class="progress-meter"' in html
    assert 'style="--progress: 22%"' in html
    assert "22% complete global vision" in html
    assert "Mohammad Ariful Islam" in html
    assert 'href="https://github.com/sigma-standards/sigma-index/issues"' in html


def test_build_site_copies_downloads_and_docs(tmp_path):
    from scripts.build_static_site import build_site

    make_fixture_repo(tmp_path)

    build_site(tmp_path)

    assert (tmp_path / "public" / "downloads" / "sigma_master.csv").exists()
    assert (tmp_path / "public" / "downloads" / "api_index.json").exists()
    assert (tmp_path / "public" / "docs" / "README.html").exists()
    assert (tmp_path / "public" / "docs" / "SCHEMA.html").exists()
    assert (
        tmp_path / "public" / "docs" / "2026-05-02-roadmap-to-100-percent-global-standards-index.html"
    ).exists()
    assert (tmp_path / "public" / "docs" / "RESEARCH_TASKS.html").exists()
    assert (tmp_path / "public" / "docs" / "PROJECT_KNOWLEDGE_GRAPH.html").exists()
    assert (tmp_path / "public" / "docs" / "SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.html").exists()
    assert (tmp_path / "public" / "docs" / "PROJECT_STATUS_REPORT_2026-05-02.html").exists()


def test_build_site_creates_search_page_and_pagefind_records(tmp_path):
    from scripts.build_static_site import build_site

    make_fixture_repo(tmp_path)

    build_site(tmp_path)

    index_html = (tmp_path / "public" / "index.html").read_text(encoding="utf-8")
    search_html = (tmp_path / "public" / "search.html").read_text(encoding="utf-8")
    search_index = json.loads((tmp_path / "public" / "search-index.json").read_text(encoding="utf-8"))
    records_html = (tmp_path / "public" / "search-records" / "records-0001.html").read_text(encoding="utf-8")

    assert 'href="search.html"' in index_html
    assert 'id="pagefind-search"' in search_html
    assert "pagefind/pagefind-component-ui.js" in search_html
    assert "<pagefind-searchbox" in search_html
    assert "search-index.json" in search_html
    assert search_index[0]["sigma_id"] == "HL-WHO-IHR-2005"
    assert search_index[1]["sigma_id"] == "CY-NIST-SP800-53R5"
    assert 'data-pagefind-body' in records_html
    assert 'data-pagefind-meta="domain:Health &amp; Medical"' in records_html
    assert "International Health Regulations" in records_html
    assert "NIST SP 800-53 Rev. 5" in records_html


def test_build_site_adds_free_safe_semantic_search_helper(tmp_path):
    from scripts.build_static_site import build_site

    make_fixture_repo(tmp_path)

    build_site(tmp_path)

    search_html = (tmp_path / "public" / "search.html").read_text(encoding="utf-8")
    semantic_js = (tmp_path / "public" / "assets" / "semantic-search.js").read_text(encoding="utf-8")

    assert 'id="semantic-search"' in search_html
    assert 'data-semantic-search' in search_html
    assert 'type="module" src="assets/semantic-search.js"' in search_html
    assert "Semantic search is optional. Lexical search works even when the model is unavailable." in search_html
    assert "@huggingface/transformers" in semantic_js
    assert "Xenova/all-MiniLM-L6-v2" in semantic_js
    assert "dtype: \"q8\"" in semantic_js
    assert "feature-extraction" in semantic_js
    assert "search-index.json" in semantic_js
    assert "dispose()" in semantic_js
    assert "beforeunload" in semantic_js
    assert "Semantic model unavailable. Lexical search remains available." in semantic_js


def test_project_reference_links_rendered_html_docs_not_raw_markdown(tmp_path):
    from scripts.build_static_site import build_site

    make_fixture_repo(tmp_path)

    build_site(tmp_path)

    html = (tmp_path / "public" / "index.html").read_text(encoding="utf-8")
    readme = (tmp_path / "public" / "docs" / "README.html").read_text(encoding="utf-8")
    research_plan = (
        tmp_path / "public" / "docs" / "RESEARCH_PROJECT_PLAN_Global_Standards_Index.html"
    ).read_text(encoding="utf-8")

    assert 'href="docs/README.html"' in html
    assert 'href="docs/SCHEMA.html"' in html
    assert 'href="docs/RESEARCH_PROJECT_PLAN_Global_Standards_Index.html"' in html
    assert 'href="docs/RESEARCH_TASKS.html"' in html
    assert 'href="docs/PROJECT_KNOWLEDGE_GRAPH.html"' in html
    assert 'href="docs/SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.html"' in html
    assert 'href="docs/PROJECT_STATUS_REPORT_2026-05-02.html"' in html
    assert 'href="docs/2026-05-02-roadmap-to-100-percent-global-standards-index.html"' in html
    assert "Roadmap to 100%" in html
    assert "Research Task Matrix" in html
    assert "Project Knowledge Graph" in html
    assert "Gap Analysis" in html
    assert 'href="docs/README.md"' not in html
    assert "<!doctype html>" in readme
    assert "<h1>README.md</h1>" in readme
    assert "<h1>RESEARCH_PROJECT_PLAN_Global_Standards_Index.md</h1>" in research_plan
    roadmap = (
        tmp_path / "public" / "docs" / "2026-05-02-roadmap-to-100-percent-global-standards-index.html"
    ).read_text(encoding="utf-8")
    assert '<a href="https://www.iso.org/standards.html">https://www.iso.org/standards.html</a>' in roadmap
