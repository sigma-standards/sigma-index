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
    (tmp_path / "dist" / "sigma_master.csv").write_text("sigma_id,name\nSIGMA-1,One\n", encoding="utf-8")
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
    assert 'href="docs/2026-05-02-roadmap-to-100-percent-global-standards-index.html"' in html
    assert "Roadmap to 100%" in html
    assert "Research Task Matrix" in html
    assert "Project Knowledge Graph" in html
    assert 'href="docs/README.md"' not in html
    assert "<!doctype html>" in readme
    assert "<h1>README.md</h1>" in readme
    assert "<h1>RESEARCH_PROJECT_PLAN_Global_Standards_Index.md</h1>" in research_plan
    roadmap = (
        tmp_path / "public" / "docs" / "2026-05-02-roadmap-to-100-percent-global-standards-index.html"
    ).read_text(encoding="utf-8")
    assert '<a href="https://www.iso.org/standards.html">https://www.iso.org/standards.html</a>' in roadmap
