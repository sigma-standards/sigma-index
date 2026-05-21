"""Build the static GitHub Pages site for SIGMA."""

from __future__ import annotations

import csv
import html
import json
import re
import shutil
from collections import Counter
from pathlib import Path


DOC_FILES = [
    "README.md",
    "SCHEMA.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "LICENSE",
    "RESEARCH_PROJECT_PLAN_Global_Standards_Index.md",
    "docs/RELEASE_GOVERNANCE.md",
    "docs/RESEARCH_TASKS.md",
    "docs/PROJECT_KNOWLEDGE_GRAPH.md",
    "docs/SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.md",
    "docs/PROJECT_STATUS_REPORT_2026-05-02.md",
    "docs/PROJECT_PROGRESS.md",
    "docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md",
]


DOWNLOAD_LABELS = {
    "sigma_master.csv": "Master CSV",
    "sigma_master.json": "Master JSON",
    "sigma_master.jsonl": "Master JSONL",
    "relationships.csv": "Relationships CSV",
    "relationships.json": "Relationships JSON",
    "api_index.json": "API Index",
    "domain_taxonomy.csv": "Domain Taxonomy",
    "source_registry.csv": "Source Registry",
    "domain_coverage.csv": "Domain Coverage",
}

TASK_REGISTRY = Path("data/reference/research_tasks.csv")
DOMAIN_REGISTRY = Path("data/reference/domain_taxonomy.csv")

SEARCH_FIELDS = [
    "sigma_id",
    "name_full",
    "name_short",
    "standard_id",
    "domain",
    "sub_domain",
    "meta_layer",
    "issuer",
    "year_published",
    "status",
    "mandate",
    "why_it_matters",
    "key_outputs",
    "official_url",
]

SEARCH_RECORD_CHUNK_SIZE = 1000

PROJECT_PROGRESS = {
    "full_vision_percent": 25,
    "public_mvp_percent": 75,
    "stage": "Public MVP with v1.2.0 release - research task completion and GitHub Pages deployment",
    "owner": "Mohammad Ariful Islam",
    "owner_role": "Lead Curator and Project Owner",
    "contact_url": "https://github.com/sigma-standards/sigma-index/issues",
    "contact_label": "Open a GitHub issue",
}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def fmt_number(value: object) -> str:
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return "0"


def compute_project_progress(root: Path | str = Path(".")) -> dict[str, object]:
    root = Path(root)
    task_rows = read_csv(root / TASK_REGISTRY)
    domain_rows = read_csv(root / DOMAIN_REGISTRY)
    if not task_rows or not domain_rows:
        return PROJECT_PROGRESS

    existing_domain_ids = {row.get("domain_id") for row in task_rows if row.get("domain_id")}
    for domain in domain_rows:
        domain_id = domain.get("domain_id")
        if domain_id and domain_id not in existing_domain_ids:
            task_rows.append({"status": "planned", "domain_id": domain_id})

    statuses = Counter(row.get("status") for row in task_rows)
    total = len(task_rows)
    done = statuses.get("done", 0)
    active = statuses.get("active", 0)
    planned = statuses.get("planned", 0)
    blocked = statuses.get("blocked", 0)
    full_vision_percent = int(round(100 * done / total)) if total else PROJECT_PROGRESS["full_vision_percent"]
    public_mvp_percent = int(round(100 * (done + active) / total)) if total else PROJECT_PROGRESS["public_mvp_percent"]
    stage = f"Roadmap progress: {done} completed, {active} active, {planned} planned across {total} roadmap tasks."
    return {
        "full_vision_percent": full_vision_percent,
        "public_mvp_percent": public_mvp_percent,
        "stage": stage,
        "owner": PROJECT_PROGRESS["owner"],
        "owner_role": PROJECT_PROGRESS["owner_role"],
        "contact_url": PROJECT_PROGRESS["contact_url"],
        "contact_label": PROJECT_PROGRESS["contact_label"],
    }


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def record_anchor(row: dict[str, str]) -> str:
    source = row.get("sigma_id") or row.get("title") or "record"
    slug = re.sub(r"[^A-Za-z0-9._:-]+", "-", source).strip("-")
    return f"record-{slug or 'record'}"


def clean_public(root: Path) -> Path:
    public = root / "public"
    if public.exists():
        shutil.rmtree(public)
    (public / "assets").mkdir(parents=True)
    (public / "downloads").mkdir()
    (public / "docs").mkdir()
    return public


def copy_files(source_dir: Path, target_dir: Path) -> list[str]:
    copied = []
    if not source_dir.exists():
        return copied
    for source in sorted(path for path in source_dir.iterdir() if path.is_file()):
        shutil.copy2(source, target_dir / source.name)
        copied.append(source.name)
    return copied


def copy_docs(root: Path, target_dir: Path) -> list[str]:
    rendered = []
    for name in DOC_FILES:
        source = root / name
        if source.exists():
            target = target_dir / doc_html_name(name)
            target.write_text(render_doc_page(name, source.read_text(encoding="utf-8")), encoding="utf-8")
            rendered.append(name)
    return rendered


def searchable_title(row: dict[str, str]) -> str:
    return row.get("name_full") or row.get("name") or row.get("standard_id") or row.get("sigma_id", "")


def search_text(row: dict[str, str]) -> str:
    return " ".join(str(row.get(field, "")) for field in SEARCH_FIELDS if row.get(field))


def normalize_search_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized = []
    for row in rows:
        sigma_id = row.get("sigma_id", "").strip()
        title = searchable_title(row).strip()
        if not sigma_id or not title:
            continue
        normalized.append(
            {
                "sigma_id": sigma_id,
                "title": title,
                "short": (row.get("name_short") or row.get("standard_id") or "").strip(),
                "standard_id": row.get("standard_id", "").strip(),
                "domain": row.get("domain", "").strip(),
                "issuer": row.get("issuer", "").strip(),
                "year": row.get("year_published", "").strip(),
                "status": row.get("status", "").strip(),
                "mandate": row.get("mandate", "").strip(),
                "official_url": row.get("official_url", "").strip(),
                "summary": row.get("why_it_matters", "").strip(),
                "text": search_text(row).strip(),
            }
        )
    return normalized


def write_search_index(public: Path, rows: list[dict[str, str]]) -> None:
    compact_rows = [
        {
            "sigma_id": row["sigma_id"],
            "title": row["title"],
            "short": row["short"],
            "standard_id": row["standard_id"],
            "domain": row["domain"],
            "issuer": row["issuer"],
            "year": row["year"],
            "status": row["status"],
            "mandate": row["mandate"],
            "official_url": row["official_url"],
            "summary": row["summary"],
            "text": row["text"],
            "record_url": row.get("record_url", ""),
        }
        for row in rows
    ]
    (public / "search-index.json").write_text(
        json.dumps(compact_rows, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def render_semantic_search_js() -> str:
    return """const TRANSFORMERS_CDN = "https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.8.1";
const MODEL_ID = "Xenova/all-MiniLM-L6-v2";
const MAX_LEXICAL_CANDIDATES = 48;
const MAX_SEMANTIC_RESULTS = 12;

const root = document.querySelector("[data-semantic-search]");
const form = root?.querySelector("[data-semantic-form]");
const input = root?.querySelector("[data-semantic-query]");
const status = root?.querySelector("[data-semantic-status]");
const results = root?.querySelector("[data-semantic-results]");
const loadButton = root?.querySelector("[data-semantic-load]");
const searchButton = root?.querySelector("[data-semantic-submit]");

let records = [];
let extractorPromise = null;
let extractor = null;

function escapeHtml(value) {
  return String(value || "").replace(/[&<>"']/g, (character) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  })[character]);
}

function setStatus(message) {
  if (status) {
    status.textContent = message;
  }
}

function setUnavailable() {
  setStatus("Semantic model unavailable. Lexical search remains available.");
  if (loadButton) {
    loadButton.disabled = false;
  }
  if (searchButton) {
    searchButton.disabled = true;
  }
}

function lexicalScore(record, query) {
  if (!query) {
    return 0;
  }
  const text = `${record.title || ""} ${record.short || ""} ${record.domain || ""} ${record.issuer || ""} ${record.text || ""}`.toLowerCase();
  const words = query.toLowerCase().split(/\\s+/).filter(Boolean);
  return words.reduce((score, word) => score + (text.includes(word) ? 1 : 0), 0);
}

function lexicalCandidates(query) {
  return records
    .map((record) => ({ record, lexical: lexicalScore(record, query) }))
    .filter((item) => item.lexical > 0)
    .sort((left, right) => right.lexical - left.lexical)
    .slice(0, MAX_LEXICAL_CANDIDATES)
    .map((item) => item.record);
}

function resultText(record) {
  return [
    record.title,
    record.short,
    record.standard_id,
    record.domain,
    record.issuer,
    record.mandate,
    record.summary,
    record.text
  ].filter(Boolean).join(" ");
}

function renderResults(items) {
  if (!results) {
    return;
  }
  if (!items.length) {
    results.innerHTML = "<p>No semantic matches found. Try the lexical search below.</p>";
    return;
  }
  results.innerHTML = items.map(({ record, score }) => `
    <article class="semantic-result">
      <span>${escapeHtml(record.domain || "Unclassified")}</span>
      <h2>${escapeHtml(record.title)}</h2>
      <p>${escapeHtml(record.summary || record.issuer || record.sigma_id)}</p>
      <small>${escapeHtml(record.sigma_id)} · ${escapeHtml(record.issuer || "Unknown issuer")} · similarity ${score.toFixed(3)}</small>
      ${record.official_url ? `<a href="${escapeHtml(record.official_url)}">Official source</a>` : ""}
    </article>
  `).join("");
}

async function loadRecords() {
  if (records.length) {
    return records;
  }
  const response = await fetch("search-index.json");
  if (!response.ok) {
    throw new Error(`Search index request failed: ${response.status}`);
  }
  records = await response.json();
  return records;
}

async function loadExtractor() {
  if (extractor) {
    return extractor;
  }
  if (!extractorPromise) {
    extractorPromise = import(TRANSFORMERS_CDN)
      .then(({ env, pipeline }) => {
        env.allowLocalModels = false;
        return pipeline("feature-extraction", MODEL_ID, {
          dtype: "q8",
          progress_callback: (progress) => {
            if (progress.status) {
              setStatus(`Loading semantic model: ${progress.status}`);
            }
          }
        });
      })
      .then((pipelineInstance) => {
        extractor = pipelineInstance;
        setStatus("Semantic search ready. Queries run fully in this browser.");
        if (searchButton) {
          searchButton.disabled = false;
        }
        return extractor;
      })
      .catch((error) => {
        console.warn("SIGMA semantic search disabled:", error);
        extractorPromise = null;
        setUnavailable();
        throw error;
      });
  }
  return extractorPromise;
}

function dot(left, right) {
  const length = Math.min(left.length, right.length);
  let total = 0;
  for (let index = 0; index < length; index += 1) {
    total += left[index] * right[index];
  }
  return total;
}

async function embed(texts) {
  const pipe = await loadExtractor();
  const output = await pipe(texts, { pooling: "mean", normalize: true });
  const dims = output.dims || [];
  const width = dims[dims.length - 1] || output.data.length;
  const vectors = [];
  for (let offset = 0; offset < output.data.length; offset += width) {
    vectors.push(Array.from(output.data.slice(offset, offset + width)));
  }
  if (typeof output.dispose === "function") {
    output.dispose();
  }
  return vectors;
}

async function runSemanticSearch(query) {
  await loadRecords();
  const candidates = lexicalCandidates(query);
  if (!candidates.length) {
    renderResults([]);
    return;
  }
  setStatus(`Embedding ${candidates.length} lexical candidates in this browser...`);
  const [queryVector, ...candidateVectors] = await embed([query, ...candidates.map(resultText)]);
  const ranked = candidates
    .map((record, index) => ({ record, score: dot(queryVector, candidateVectors[index]) }))
    .sort((left, right) => right.score - left.score)
    .slice(0, MAX_SEMANTIC_RESULTS);
  renderResults(ranked);
  setStatus("Semantic results ranked locally. Lexical search remains available below.");
}

async function cleanup() {
  if (extractor && typeof extractor.dispose === "function") {
    await extractor.dispose();
  }
  extractor = null;
  extractorPromise = null;
}

if (root && form && input) {
  loadRecords().catch(() => setStatus("Semantic helper could not load the local search index. Lexical search remains available."));

  loadButton?.addEventListener("click", () => {
    setStatus("Loading semantic model in this browser...");
    if (loadButton) {
      loadButton.disabled = true;
    }
    loadExtractor().catch(() => undefined);
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const query = input.value.trim();
    if (!query) {
      renderResults([]);
      setStatus("Enter a question or concept to search semantically.");
      return;
    }
    runSemanticSearch(query).catch(() => setUnavailable());
  });

  window.addEventListener("beforeunload", () => {
    cleanup();
  });
}
"""


def render_search_record_article(row: dict[str, str]) -> str:
    url = row.get("official_url", "")
    official_link = f'<a href="{esc(url)}">Official source</a>' if url else ""
    anchor = record_anchor(row)
    return f"""
      <article id="{esc(anchor)}" class="search-record" data-pagefind-body data-pagefind-meta="domain:{esc(row['domain'])}" data-pagefind-filter="domain:{esc(row['domain'])}">
        <p class="eyebrow">{esc(row['domain'])}</p>
        <h2>{esc(row['title'])}</h2>
        <p class="record-short">{esc(row['short'])}</p>
        <p class="record-short">{esc(row['standard_id'])}</p>
        <dl>
          <div><dt>SIGMA ID</dt><dd>{esc(row['sigma_id'])}</dd></div>
          <div><dt>Issuer</dt><dd>{esc(row['issuer'])}</dd></div>
          <div><dt>Mandate</dt><dd>{esc(row['mandate'])}</dd></div>
          <div><dt>Status</dt><dd>{esc(row['status'])}</dd></div>
        </dl>
        <p>{esc(row['summary'] or row['text'])}</p>
        {official_link}
      </article>
    """


def render_search_record_page(rows: list[dict[str, str]], page_number: int) -> str:
    start = (page_number - 1) * SEARCH_RECORD_CHUNK_SIZE + 1
    end = start + len(rows) - 1
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SIGMA Search Records {page_number:04d}</title>
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="../assets/styles.css">
</head>
<body class="doc-page">
  <header class="site-header">
    <a class="brand" href="../index.html" aria-label="SIGMA home">
      <span class="brand-mark">S</span>
      <span><strong>SIGMA</strong><small>Global Standards Index</small></span>
    </a>
    <nav class="site-nav" aria-label="Search record navigation">
      <a href="../search.html">Search</a>
      <a href="../index.html#downloads">Downloads</a>
      <a href="../index.html#docs">Docs</a>
    </nav>
  </header>
  <main class="doc-shell">
    <section class="doc-content">
      <h1>Search Records {start:,}-{end:,}</h1>
      <p>This generated page gives Pagefind static HTML content for SIGMA records while the canonical data remains in the release bundle.</p>
      {"".join(render_search_record_article(row) for row in rows)}
    </section>
  </main>
</body>
</html>
"""


def write_search_record_pages(public: Path, rows: list[dict[str, str]]) -> list[str]:
    search_records = public / "search-records"
    search_records.mkdir()
    pages = []
    for index in range(0, len(rows), SEARCH_RECORD_CHUNK_SIZE):
        chunk = rows[index : index + SEARCH_RECORD_CHUNK_SIZE]
        page_number = (index // SEARCH_RECORD_CHUNK_SIZE) + 1
        filename = f"records-{page_number:04d}.html"
        (search_records / filename).write_text(render_search_record_page(chunk, page_number), encoding="utf-8")
        pages.append(filename)
    return pages


def add_search_record_urls(rows: list[dict[str, str]]) -> None:
    for index, row in enumerate(rows):
        page_number = (index // SEARCH_RECORD_CHUNK_SIZE) + 1
        row["record_url"] = f"search-records/records-{page_number:04d}.html#{record_anchor(row)}"


def render_search_page(api: dict, row_count: int) -> str:
    entry_count = fmt_number(api.get("entry_count") or row_count)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Search · SIGMA Global Standards Index</title>
  <meta name="description" content="Search SIGMA standards metadata across domains, issuers, mandates, and source-backed release records.">
  <link rel="stylesheet" href="assets/styles.css">
  <link rel="stylesheet" href="pagefind/pagefind-component-ui.css">
  <script src="pagefind/pagefind-component-ui.js" type="module"></script>
</head>
<body class="search-page">
  <header class="site-header">
    <a class="brand" href="index.html" aria-label="SIGMA home">
      <span class="brand-mark">S</span>
      <span><strong>SIGMA</strong><small>Global Standards Index</small></span>
    </a>
    <nav class="site-nav" aria-label="Primary navigation">
      <a href="index.html#progress">Progress</a>
      <a href="index.html#downloads">Downloads</a>
      <a href="index.html#domains">Domains</a>
      <a href="index.html#sources">Sources</a>
      <a href="index.html#docs">Docs</a>
    </nav>
  </header>
  <main class="search-shell">
    <section class="search-hero" data-pagefind-ignore>
      <p class="eyebrow">Standards browser</p>
      <h1>Search {entry_count} SIGMA records</h1>
      <p>Look up standards, treaties, guidelines, issuers, domains, mandates, and source-backed metadata from the current release bundle.</p>
    </section>
    <section class="search-panel" data-pagefind-ignore>
      <div id="pagefind-search">
        <pagefind-searchbox placeholder="Search SIGMA records..." show-sub-results></pagefind-searchbox>
      </div>
      <section id="semantic-search" class="semantic-search" data-semantic-search>
        <div class="semantic-copy">
          <p class="eyebrow">Optional semantic helper</p>
          <h2>Rank a small lexical candidate set with browser embeddings</h2>
          <p>Semantic search is optional. Lexical search works even when the model is unavailable.</p>
        </div>
        <form class="semantic-form" data-semantic-form role="search">
          <label for="semantic-query">Semantic query</label>
          <div class="semantic-row">
            <input id="semantic-query" data-semantic-query type="search" autocomplete="off" placeholder="Example: public health emergency reporting">
            <button type="button" data-semantic-load>Load model</button>
            <button type="submit" data-semantic-submit disabled>Rank</button>
          </div>
        </form>
        <p class="semantic-status" data-semantic-status aria-live="polite">Uses a small quantized Transformers.js feature-extraction model only after you load it.</p>
        <div class="semantic-results" data-semantic-results aria-live="polite"></div>
      </section>
      <form class="fallback-search" role="search">
        <label for="fallback-query">Fallback search</label>
        <div class="fallback-row">
          <input id="fallback-query" type="search" autocomplete="off" placeholder="Search by ID, title, issuer, domain, or mandate">
          <select id="fallback-domain" aria-label="Filter by domain">
            <option value="">All domains</option>
          </select>
          <button type="submit">Search</button>
        </div>
      </form>
      <div id="fallback-results" class="fallback-results" aria-live="polite"></div>
    </section>
  </main>
  <script>
    const form = document.querySelector(".fallback-search");
    const input = document.getElementById("fallback-query");
    const domain = document.getElementById("fallback-domain");
    const results = document.getElementById("fallback-results");
    let records = [];

    function escapeHtml(value) {{
      return String(value || "").replace(/[&<>"']/g, (character) => ({{
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
      }})[character]);
    }}

    function renderResults(items) {{
      if (!items.length) {{
        results.innerHTML = "<p>No matching records found.</p>";
        return;
      }}
      const resultSummary = `<p>Showing ${{items.length > 50 ? "50 of " : ""}}${{items.length}} matching records.</p>`;
      results.innerHTML = resultSummary + items.slice(0, 50).map((item) => `
        <article class="fallback-result">
          <span>${{escapeHtml(item.domain || "Unclassified")}}</span>
          <h2>${{escapeHtml(item.title)}}</h2>
          <p>${{escapeHtml(item.summary || item.issuer || item.sigma_id)}}</p>
          <small>${{escapeHtml(item.sigma_id)}} · ${{escapeHtml(item.issuer || "Unknown issuer")}} · ${{escapeHtml(item.status || "unknown")}}</small>
          ${{item.record_url ? `<a href="${{escapeHtml(item.record_url)}}">Open indexed record</a>` : ""}}
          ${{item.official_url ? `<a href="${{escapeHtml(item.official_url)}}">Official source</a>` : ""}}
        </article>
      `).join("");
    }}

    function recordSearchText(item) {{
      return [
        item.sigma_id,
        item.title,
        item.short,
        item.standard_id,
        item.domain,
        item.issuer,
        item.status,
        item.mandate,
        item.summary,
        item.text
      ].filter(Boolean).join(" ").toLowerCase();
    }}

    fetch("search-index.json")
      .then((response) => response.json())
      .then((data) => {{
        records = data;
        const domains = [...new Set(records.map((item) => item.domain).filter(Boolean))].sort();
        domain.insertAdjacentHTML("beforeend", domains.map((name) => `<option value="${{escapeHtml(name)}}">${{escapeHtml(name)}}</option>`).join(""));
      }})
      .catch(() => {{
        results.innerHTML = "<p>The fallback index is not available in this build.</p>";
      }});

    form.addEventListener("submit", (event) => {{
      event.preventDefault();
      const query = input.value.trim().toLowerCase();
      const selectedDomain = domain.value;
      const matches = records.filter((item) => {{
        const domainMatch = !selectedDomain || item.domain === selectedDomain;
        const textMatch = !query || recordSearchText(item).includes(query);
        return domainMatch && textMatch;
      }});
      renderResults(matches);
    }});
  </script>
  <script type="module" src="assets/semantic-search.js"></script>
</body>
</html>
"""


def doc_html_name(name: str) -> str:
    return f"{Path(name).stem}.html"


def render_inline_markdown(text: str) -> str:
    code_spans: list[str] = []

    def stash_code(match: re.Match[str]) -> str:
        code_spans.append(f"<code>{esc(match.group(1))}</code>")
        return f"@@CODE{len(code_spans) - 1}@@"

    escaped = esc(re.sub(r"`([^`]+)`", stash_code, text))
    # Keep this intentionally small and deterministic; source docs stay canonical.
    for marker in ["**", "__"]:
        parts = escaped.split(marker)
        if len(parts) >= 3:
            rebuilt = [parts[0]]
            strong = True
            for part in parts[1:]:
                rebuilt.append(f"<strong>{part}</strong>" if strong else part)
                strong = not strong
            escaped = "".join(rebuilt)
    escaped = re.sub(
        r"(https?://[^\s<]+[^\s<.,)])",
        lambda match: f'<a href="{match.group(1)}">{match.group(1)}</a>',
        escaped,
    )
    for index, code in enumerate(code_spans):
        escaped = escaped.replace(f"@@CODE{index}@@", code)
    return escaped


def render_markdown_body(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    ordered_items: list[str] = []
    table_lines: list[str] = []
    code_lines: list[str] = []
    in_code = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(f"<p>{render_inline_markdown(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            blocks.append("<ul>" + "".join(f"<li>{render_inline_markdown(item)}</li>" for item in list_items) + "</ul>")
            list_items = []

    def flush_ordered_list() -> None:
        nonlocal ordered_items
        if ordered_items:
            blocks.append(
                "<ol>" + "".join(f"<li>{render_inline_markdown(item)}</li>" for item in ordered_items) + "</ol>"
            )
            ordered_items = []

    def flush_table() -> None:
        nonlocal table_lines
        if not table_lines:
            return
        rows = [line.strip().strip("|").split("|") for line in table_lines]
        if len(rows) >= 2 and all(set(cell.strip()) <= {"-", ":"} for cell in rows[1]):
            header = rows[0]
            body_rows = rows[2:]
            header_html = "".join(f"<th>{render_inline_markdown(cell.strip())}</th>" for cell in header)
            body_html = "".join(
                "<tr>" + "".join(f"<td>{render_inline_markdown(cell.strip())}</td>" for cell in row) + "</tr>"
                for row in body_rows
            )
            blocks.append(f"<table><thead><tr>{header_html}</tr></thead><tbody>{body_html}</tbody></table>")
        else:
            for row in table_lines:
                blocks.append(f"<p>{render_inline_markdown(row)}</p>")
        table_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code:
                blocks.append(f"<pre><code>{esc(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                flush_paragraph()
                flush_list()
                flush_ordered_list()
                flush_table()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not stripped:
            flush_paragraph()
            flush_list()
            flush_ordered_list()
            flush_table()
            continue
        if stripped.startswith("|"):
            flush_paragraph()
            flush_list()
            flush_ordered_list()
            table_lines.append(stripped)
            continue
        if stripped.startswith("#"):
            flush_paragraph()
            flush_list()
            flush_ordered_list()
            flush_table()
            level = min(len(stripped) - len(stripped.lstrip("#")), 4)
            text = stripped[level:].strip()
            blocks.append(f"<h{level}>{render_inline_markdown(text)}</h{level}>")
            continue
        if stripped.startswith(("- ", "* ")):
            flush_paragraph()
            flush_ordered_list()
            flush_table()
            list_items.append(stripped[2:].strip())
            continue
        ordered_match = re.match(r"\d+\.\s+(.+)", stripped)
        if ordered_match:
            flush_paragraph()
            flush_list()
            flush_table()
            ordered_items.append(ordered_match.group(1).strip())
            continue
        paragraph.append(stripped)

    flush_paragraph()
    flush_list()
    flush_ordered_list()
    flush_table()
    if in_code:
        blocks.append(f"<pre><code>{esc(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(blocks)


def render_doc_page(source_name: str, markdown_text: str) -> str:
    labels = doc_labels()
    title = labels.get(source_name, source_name)
    body = render_markdown_body(markdown_text)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)} · SIGMA</title>
  <link rel="stylesheet" href="../assets/styles.css">
</head>
<body class="doc-page">
  <header class="site-header">
    <a class="brand" href="../index.html" aria-label="SIGMA home">
      <span class="brand-mark">S</span>
      <span><strong>SIGMA</strong><small>Global Standards Index</small></span>
    </a>
    <nav class="site-nav" aria-label="Documentation navigation">
      <a href="../index.html#docs">Project References</a>
      <a href="../index.html#downloads">Downloads</a>
    </nav>
  </header>
  <main class="doc-shell">
    <article class="doc-content">
      {body}
    </article>
  </main>
</body>
</html>
"""


def merge_domain_rows(domain_rows: list[dict[str, str]], coverage_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    coverage_by_id = {row.get("domain_id", ""): row for row in coverage_rows}
    merged = []
    for row in domain_rows:
        coverage = coverage_by_id.get(row.get("domain_id", ""), {})
        merged.append(
            {
                "domain_id": row.get("domain_id", ""),
                "domain_name": row.get("domain_name", ""),
                "domain_code": row.get("domain_code", ""),
                "meta_layer": row.get("meta_layer") or coverage.get("meta_layer", ""),
                "entry_count": coverage.get("entry_count", "0"),
                "coverage_status": coverage.get("coverage_status", "tracked"),
            }
        )
    return merged


def render_download_cards(downloads: list[str]) -> str:
    cards = []
    for filename in downloads:
        label = DOWNLOAD_LABELS.get(filename, filename)
        extension = filename.rsplit(".", 1)[-1].upper()
        cards.append(
            f"""
            <a class="download-card" href="downloads/{esc(filename)}">
              <span class="download-type">{esc(extension)}</span>
              <strong>{esc(label)}</strong>
              <small>{esc(filename)}</small>
            </a>
            """
        )
    return "\n".join(cards)


def render_domain_cards(domains: list[dict[str, str]]) -> str:
    cards = []
    for row in domains:
        cards.append(
            f"""
            <article class="domain-card">
              <div>
                <span class="domain-code">{esc(row['domain_code'] or row['domain_id'])}</span>
                <h3>{esc(row['domain_name'])}</h3>
                <p>{esc(row['meta_layer'])}</p>
              </div>
              <div class="domain-meta">
                <span>{fmt_number(row['entry_count'])} entries</span>
                <span>{esc(row['coverage_status']).title()}</span>
              </div>
            </article>
            """
        )
    return "\n".join(cards)


def render_source_rows(sources: list[dict[str, str]]) -> str:
    rows = []
    for row in sources:
        source_name = row.get("source_name") or row.get("primary_free_sources", "")
        source_url = row.get("source_url", "")
        source_label = esc(source_name)
        if source_url:
            source_label = f'<a href="{esc(source_url)}">{source_label}</a>'
        rows.append(
            f"""
            <tr>
              <td>{esc(row.get('domain_name') or row.get('domain'))}</td>
              <td>{source_label}</td>
              <td>{esc(row.get('source_type') or 'registry')}</td>
              <td><span class="status-pill">{esc(row.get('sync_status') or row.get('collection_status') or 'tracked')}</span></td>
            </tr>
            """
        )
    return "\n".join(rows)


def render_doc_links(docs: list[str]) -> str:
    labels = doc_labels()
    return "\n".join(
        f'<a class="doc-link" href="docs/{esc(doc_html_name(name))}">{esc(labels.get(name, name))}</a>' for name in docs
    )


def doc_labels() -> dict[str, str]:
  return {
    "README.md": "Project Overview",
    "SCHEMA.md": "Data Schema",
    "CONTRIBUTING.md": "Contributing",
    "CODE_OF_CONDUCT.md": "Code of Conduct",
    "CHANGELOG.md": "Changelog",
    "LICENSE": "License",
    "RESEARCH_PROJECT_PLAN_Global_Standards_Index.md": "Research Plan",
    "docs/RELEASE_GOVERNANCE.md": "Release Governance",
    "docs/RESEARCH_TASKS.md": "Research Task Matrix",
    "docs/PROJECT_KNOWLEDGE_GRAPH.md": "Project Knowledge Graph",
    "docs/SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.md": "Gap Analysis",
    "docs/PROJECT_STATUS_REPORT_2026-05-02.md": "Project Status Report",
    "docs/PROJECT_PROGRESS.md": "Project Progress",
    "docs/superpowers/plans/2026-05-02-roadmap-to-100-percent-global-standards-index.md": "Roadmap to 100%",
  }
def render_html(api: dict, domains: list[dict[str, str]], sources: list[dict[str, str]], downloads: list[str], docs: list[str], progress: dict[str, object]) -> str:
    entry_count = fmt_number(api.get("entry_count"))
    relationship_count = fmt_number(api.get("relationship_count"))
    domain_count = fmt_number(len(domains))
    source_count = fmt_number(len(sources))
    full_progress = progress.get("full_vision_percent", PROJECT_PROGRESS["full_vision_percent"])
    public_progress = progress.get("public_mvp_percent", PROJECT_PROGRESS["public_mvp_percent"])

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SIGMA Global Standards Index</title>
  <meta name="description" content="Open, machine-readable metadata for global standards, treaties, frameworks, guidelines, and classification systems.">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="brand" href="#top" aria-label="SIGMA home">
      <span class="brand-mark">S</span>
      <span><strong>SIGMA</strong><small>Global Standards Index</small></span>
    </a>
    <nav class="site-nav" aria-label="Primary navigation">
      <a href="#progress">Progress</a>
      <a href="search.html">Search</a>
      <a href="#downloads">Downloads</a>
      <a href="#domains">Domains</a>
      <a href="#sources">Sources</a>
      <a href="#docs">Docs</a>
    </nav>
  </header>

  <main id="top">
    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow">Open standards intelligence</p>
        <h1>SIGMA Global Standards Index</h1>
        <p class="lede">A unified, machine-readable map of global standards, treaties, frameworks, guidelines, and classification systems across public-interest domains.</p>
        <div class="hero-actions">
          <a class="primary-action" href="#downloads">Get the data</a>
          <a class="secondary-action" href="search.html">Search records</a>
        </div>
      </div>
      <div class="hero-panel" aria-label="Current release metrics">
        <div><strong>{entry_count}</strong><span>master entries</span></div>
        <div><strong>{relationship_count}</strong><span>relationship edges</span></div>
        <div><strong>{domain_count}</strong><span>canonical domains</span></div>
        <div><strong>{source_count}</strong><span>source registry rows</span></div>
      </div>
    </section>

    <section id="progress" class="section progress-band">
      <div class="section-heading">
        <p class="eyebrow">Project progress</p>
        <h2>From public MVP to complete global index.</h2>
        <p>The roadmap defines 100% as source-backed coverage across all 40 domains, all major layers, repeatable ingestors, relationship graph exports, quality gates, and rendered public documentation.</p>
      </div>
      <div class="progress-layout">
        <article class="progress-card">
          <div class="progress-meter" style="--progress: {full_progress}%">
            <span></span>
          </div>
          <strong>{full_progress}% complete global vision</strong>
          <p>{esc(PROJECT_PROGRESS["stage"])}. The remaining work is tracked by the roadmap, research task matrix, source registry, and quality reports.</p>
        </article>
        <article class="progress-card">
          <div class="progress-meter secondary" style="--progress: {public_progress}%">
            <span></span>
          </div>
          <strong>{public_progress}% public MVP readiness</strong>
          <p>The published site has release downloads, all-domain coverage, source registry views, rendered project references, and deterministic validation.</p>
        </article>
        <article class="owner-card">
          <span>Project owner</span>
          <strong>{esc(PROJECT_PROGRESS["owner"])}</strong>
          <p>{esc(PROJECT_PROGRESS["owner_role"])}</p>
          <a href="{esc(PROJECT_PROGRESS["contact_url"])}">{esc(PROJECT_PROGRESS["contact_label"])}</a>
        </article>
      </div>
    </section>

    <section class="section band">
      <div>
        <p class="eyebrow">Current data layers</p>
        <h2>Built for humans, scripts, and future APIs.</h2>
      </div>
      <div class="layer-grid">
        <article><strong>Raw seeds</strong><span>Source metadata and classification inputs.</span></article>
        <article><strong>Processed records</strong><span>Normalized domain datasets ready for validation.</span></article>
        <article><strong>Relationships</strong><span>High-confidence graph edges between standards and bodies.</span></article>
        <article><strong>Release bundle</strong><span>CSV, JSON, JSONL, registry, coverage, and API index files.</span></article>
      </div>
    </section>

    <section id="downloads" class="section">
      <div class="section-heading">
        <p class="eyebrow">Downloads</p>
        <h2>Release files</h2>
        <p>Generated artifacts are rebuilt by the release workflow and copied into this site for direct access.</p>
      </div>
      <div class="download-grid">
        {render_download_cards(downloads)}
      </div>
    </section>

    <section id="domains" class="section">
      <div class="section-heading">
        <p class="eyebrow">Coverage</p>
        <h2>All canonical domains</h2>
        <p>Every domain is tracked with a meta-layer, compact code, current entry count, and collection status.</p>
      </div>
      <div class="domain-grid">
        {render_domain_cards(domains)}
      </div>
    </section>

    <section id="sources" class="section">
      <div class="section-heading">
        <p class="eyebrow">Synchronization</p>
        <h2>Source registry</h2>
        <p>The registry records the free/public source path for each domain and its current collection status.</p>
      </div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Domain</th><th>Source path</th><th>Type</th><th>Status</th></tr>
          </thead>
          <tbody>
            {render_source_rows(sources)}
          </tbody>
        </table>
      </div>
    </section>

    <section id="docs" class="section docs-band">
      <div class="section-heading">
        <p class="eyebrow">Documentation</p>
        <h2>Project references</h2>
        <p>Read the schema, contribution process, governance documents, and research plan.</p>
      </div>
      <div class="doc-grid">
        {render_doc_links(docs)}
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <span>Data and documentation are released under CC BY 4.0.</span>
    <a href="https://github.com/sigma-standards/sigma-index">GitHub repository</a>
  </footer>
</body>
</html>
"""


def render_css() -> str:
    return """
:root {
  color-scheme: light;
  --ink: #172026;
  --muted: #5d6970;
  --paper: #fbfaf6;
  --surface: #ffffff;
  --line: #d9ded8;
  --forest: #1f5f4b;
  --teal: #0f6b78;
  --gold: #c58b2b;
  --berry: #8c315d;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  color: var(--ink);
  background: var(--paper);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

a {
  color: inherit;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 14px clamp(18px, 4vw, 56px);
  background: rgba(251, 250, 246, 0.92);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(16px);
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}

.brand-mark {
  display: grid;
  width: 38px;
  height: 38px;
  place-items: center;
  color: white;
  background: var(--forest);
  border-radius: 8px;
  font-weight: 800;
}

.brand small {
  display: block;
  color: var(--muted);
  font-size: 0.78rem;
}

.site-nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: 8px;
}

.site-nav a {
  padding: 8px 10px;
  color: #2c3b41;
  text-decoration: none;
  border-radius: 6px;
}

.site-nav a:hover {
  background: #e7eee9;
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(300px, 0.8fr);
  gap: clamp(24px, 5vw, 60px);
  align-items: center;
  min-height: 74vh;
  padding: clamp(52px, 8vw, 96px) clamp(20px, 5vw, 76px);
  background:
    linear-gradient(135deg, rgba(31, 95, 75, 0.96), rgba(15, 107, 120, 0.88)),
    linear-gradient(45deg, #f4ead2, #dce8df);
  color: white;
}

.eyebrow {
  margin: 0 0 10px;
  color: var(--gold);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0;
  text-transform: uppercase;
}

.hero .eyebrow {
  color: #f5c46d;
}

h1,
h2,
h3,
p {
  overflow-wrap: anywhere;
}

h1 {
  max-width: 860px;
  margin: 0;
  font-size: clamp(2.4rem, 7vw, 5.8rem);
  line-height: 0.96;
  letter-spacing: 0;
}

.lede {
  max-width: 740px;
  margin: 24px 0 0;
  color: rgba(255, 255, 255, 0.88);
  font-size: clamp(1.05rem, 2vw, 1.35rem);
  line-height: 1.65;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 30px;
}

.primary-action,
.secondary-action {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 11px 16px;
  border-radius: 8px;
  font-weight: 750;
  text-decoration: none;
}

.primary-action {
  color: #173126;
  background: #f5c46d;
}

.secondary-action {
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.42);
}

.hero-panel {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.hero-panel div,
.layer-grid article,
.download-card,
.domain-card,
.doc-link,
.search-panel,
.fallback-result,
.semantic-result,
.search-record {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--surface);
}

.hero-panel div {
  min-height: 132px;
  padding: 20px;
  color: var(--ink);
}

.hero-panel strong {
  display: block;
  color: var(--forest);
  font-size: clamp(1.7rem, 4vw, 2.55rem);
}

.hero-panel span {
  color: var(--muted);
}

.section {
  max-width: 1180px;
  margin: 0 auto;
  padding: 72px 20px;
}

.progress-band {
  max-width: none;
  padding-inline: clamp(20px, 5vw, 76px);
  background: #f6efe2;
}

.progress-layout {
  display: grid;
  grid-template-columns: minmax(220px, 1fr) minmax(220px, 1fr) minmax(240px, 0.82fr);
  gap: 14px;
}

.progress-card,
.owner-card {
  min-height: 220px;
  padding: 20px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: white;
}

.progress-card strong,
.owner-card strong {
  display: block;
  margin-top: 16px;
  color: var(--ink);
  font-size: 1.25rem;
}

.progress-card p,
.owner-card p {
  color: var(--muted);
  line-height: 1.6;
}

.progress-meter {
  height: 14px;
  overflow: hidden;
  border-radius: 999px;
  background: #dce5df;
}

.progress-meter span {
  display: block;
  width: var(--progress);
  height: 100%;
  background: linear-gradient(90deg, var(--forest), var(--teal));
}

.progress-meter.secondary span {
  background: linear-gradient(90deg, var(--gold), var(--berry));
}

.owner-card span {
  color: var(--berry);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.owner-card a {
  display: inline-flex;
  margin-top: 8px;
  color: var(--forest);
  font-weight: 800;
  text-decoration: none;
}

.band {
  display: grid;
  grid-template-columns: minmax(220px, 0.8fr) minmax(0, 1.2fr);
  gap: 28px;
  max-width: none;
  padding-inline: clamp(20px, 5vw, 76px);
  background: #edf4ef;
}

.section h2 {
  max-width: 760px;
  margin: 0;
  font-size: clamp(1.8rem, 4vw, 3rem);
  line-height: 1.05;
}

.section-heading {
  display: grid;
  gap: 10px;
  margin-bottom: 28px;
}

.section-heading p:not(.eyebrow) {
  max-width: 760px;
  margin: 0;
  color: var(--muted);
  line-height: 1.65;
}

.layer-grid,
.download-grid,
.domain-grid,
.doc-grid {
  display: grid;
  gap: 14px;
}

.layer-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.layer-grid article {
  padding: 18px;
}

.layer-grid strong,
.layer-grid span {
  display: block;
}

.layer-grid span {
  margin-top: 8px;
  color: var(--muted);
  line-height: 1.5;
}

.download-grid {
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
}

.download-card {
  min-height: 148px;
  padding: 18px;
  text-decoration: none;
  transition: transform 160ms ease, border-color 160ms ease, box-shadow 160ms ease;
}

.download-card:hover,
.doc-link:hover {
  transform: translateY(-2px);
  border-color: var(--teal);
  box-shadow: 0 14px 30px rgba(23, 32, 38, 0.08);
}

.download-type {
  display: inline-flex;
  margin-bottom: 22px;
  padding: 5px 8px;
  color: white;
  background: var(--berry);
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 800;
}

.download-card strong,
.download-card small {
  display: block;
}

.download-card small {
  margin-top: 8px;
  color: var(--muted);
}

.domain-grid {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.domain-card {
  display: flex;
  min-height: 190px;
  flex-direction: column;
  justify-content: space-between;
  padding: 18px;
}

.domain-code {
  display: inline-flex;
  padding: 4px 7px;
  color: white;
  background: var(--teal);
  border-radius: 6px;
  font-size: 0.74rem;
  font-weight: 800;
}

.domain-card h3 {
  margin: 14px 0 8px;
  font-size: 1.08rem;
}

.domain-card p,
.domain-meta {
  color: var(--muted);
}

.domain-meta {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  padding-top: 16px;
  font-size: 0.88rem;
}

.table-wrap {
  overflow-x: auto;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: white;
}

table {
  width: 100%;
  min-width: 760px;
  border-collapse: collapse;
}

th,
td {
  padding: 14px 16px;
  text-align: left;
  border-bottom: 1px solid var(--line);
  vertical-align: top;
}

th {
  color: #314149;
  background: #edf4ef;
  font-size: 0.84rem;
}

td {
  color: var(--muted);
}

td:first-child {
  color: var(--ink);
  font-weight: 700;
}

.status-pill {
  display: inline-flex;
  padding: 4px 8px;
  color: #173126;
  background: #f3dfb5;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 750;
}

.docs-band {
  max-width: none;
  padding-inline: clamp(20px, 5vw, 76px);
  background: #172026;
  color: white;
}

.docs-band .section-heading p:not(.eyebrow) {
  color: rgba(255, 255, 255, 0.72);
}

.doc-grid {
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
}

.doc-link {
  padding: 18px;
  color: var(--ink);
  text-decoration: none;
}

.search-shell {
  max-width: 1120px;
  margin: 0 auto;
  padding: 56px 20px 84px;
}

.search-hero {
  padding: 24px 0 34px;
}

.search-hero h1 {
  color: var(--forest);
  font-size: clamp(2.2rem, 6vw, 4.7rem);
}

.search-hero p:not(.eyebrow) {
  max-width: 760px;
  color: var(--muted);
  font-size: 1.1rem;
  line-height: 1.65;
}

.search-panel {
  padding: clamp(18px, 3vw, 28px);
}

.fallback-search {
  display: grid;
  gap: 12px;
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid var(--line);
}

.fallback-search label {
  color: var(--ink);
  font-weight: 800;
}

.semantic-search {
  display: grid;
  gap: 12px;
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid var(--line);
}

.semantic-copy h2 {
  margin: 0;
  color: var(--forest);
  font-size: 1.35rem;
}

.semantic-copy p:not(.eyebrow),
.semantic-status {
  max-width: 760px;
  margin: 8px 0 0;
  color: var(--muted);
  line-height: 1.6;
}

.semantic-form {
  display: grid;
  gap: 10px;
}

.semantic-form label {
  color: var(--ink);
  font-weight: 800;
}

.semantic-row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto auto;
  gap: 10px;
}

.semantic-row input,
.semantic-row button {
  min-height: 44px;
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  font: inherit;
}

.semantic-row button {
  color: white;
  background: var(--teal);
  border-color: var(--teal);
  font-weight: 800;
}

.semantic-row button:disabled {
  cursor: not-allowed;
  background: #8aa0a2;
  border-color: #8aa0a2;
}

.semantic-results {
  display: grid;
  gap: 12px;
}

.fallback-row {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(180px, 0.55fr) auto;
  gap: 10px;
}

.fallback-row input,
.fallback-row select,
.fallback-row button {
  min-height: 44px;
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  font: inherit;
}

.fallback-row button {
  color: white;
  background: var(--forest);
  border-color: var(--forest);
  font-weight: 800;
}

.fallback-results {
  display: grid;
  gap: 12px;
  margin-top: 20px;
}

.fallback-result,
.semantic-result,
.search-record {
  padding: 16px;
}

.fallback-result span,
.semantic-result span {
  color: var(--berry);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.fallback-result h2,
.semantic-result h2,
.search-record h2 {
  margin: 8px 0;
  font-size: 1.15rem;
}

.fallback-result p,
.fallback-result small,
.semantic-result p,
.semantic-result small,
.search-record p,
.search-record dd {
  color: var(--muted);
}

.fallback-result a,
.semantic-result a,
.search-record a {
  display: inline-flex;
  margin-top: 10px;
  color: var(--forest);
  font-weight: 800;
  text-decoration: none;
}

.search-record {
  margin-top: 14px;
}

.search-record dl {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 10px;
  margin: 14px 0;
}

.search-record dt {
  color: var(--ink);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.search-record dd {
  margin: 4px 0 0;
}

.site-footer {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 12px;
  padding: 26px clamp(20px, 5vw, 76px);
  color: #dce5df;
  background: #10171b;
}

.site-footer a {
  color: #f5c46d;
  text-decoration: none;
}

.doc-shell {
  max-width: 980px;
  margin: 0 auto;
  padding: 48px 20px 84px;
}

.doc-content {
  padding: clamp(22px, 4vw, 42px);
  border: 1px solid var(--line);
  border-radius: 8px;
  background: white;
}

.doc-content h1 {
  color: var(--forest);
  font-size: clamp(2rem, 5vw, 3.6rem);
}

.doc-content h2 {
  margin-top: 34px;
  padding-top: 22px;
  border-top: 1px solid var(--line);
}

.doc-content p,
.doc-content li,
.doc-content td {
  line-height: 1.7;
}

.doc-content code {
  padding: 2px 5px;
  border-radius: 5px;
  background: #edf4ef;
  font-size: 0.92em;
}

.doc-content pre {
  overflow-x: auto;
  padding: 16px;
  border-radius: 8px;
  background: #10171b;
}

.doc-content pre code {
  padding: 0;
  color: #eef7f1;
  background: transparent;
}

@media (max-width: 820px) {
  .site-header {
    align-items: flex-start;
    flex-direction: column;
  }

  .site-nav {
    justify-content: flex-start;
  }

  .hero,
  .band,
  .progress-layout {
    grid-template-columns: 1fr;
  }

  .hero-panel {
    grid-template-columns: 1fr;
  }

  .layer-grid {
    grid-template-columns: 1fr;
  }

  .fallback-row {
    grid-template-columns: 1fr;
  }

  .semantic-row {
    grid-template-columns: 1fr;
  }
}
"""


def build_site(root: Path | str = Path(".")) -> Path:
    root = Path(root)
    public = clean_public(root)

    dist_dir = root / "dist"
    downloads = copy_files(dist_dir, public / "downloads")
    docs = copy_docs(root, public / "docs")

    api = read_json(dist_dir / "api_index.json")
    domain_rows = read_csv(root / "data" / "reference" / "domain_taxonomy.csv")
    coverage_rows = read_csv(dist_dir / "domain_coverage.csv")
    if not coverage_rows:
        coverage_rows = read_csv(root / "data" / "reports" / "domain_coverage.csv")
    source_rows = read_csv(root / "data" / "reference" / "source_registry.csv")
    search_rows = normalize_search_rows(read_csv(dist_dir / "sigma_master.csv"))
    add_search_record_urls(search_rows)
    domains = merge_domain_rows(domain_rows, coverage_rows)

    (public / "assets" / "styles.css").write_text(render_css(), encoding="utf-8")
    (public / "assets" / "semantic-search.js").write_text(render_semantic_search_js(), encoding="utf-8")
    write_search_index(public, search_rows)
    write_search_record_pages(public, search_rows)
    (public / "search.html").write_text(render_search_page(api, len(search_rows)), encoding="utf-8")
    progress = compute_project_progress(root)
    (public / "index.html").write_text(
        render_html(api, domains, source_rows, downloads, docs, progress),
        encoding="utf-8",
    )
    return public


def main() -> None:
    build_site(Path("."))


if __name__ == "__main__":
    main()
