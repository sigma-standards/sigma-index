const TRANSFORMERS_CDN = "https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.8.1";
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
  const words = query.toLowerCase().split(/\s+/).filter(Boolean);
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
