---
engine: gemini
tools:
  - github
  - web
---

# SIGMA Standards Researcher Agent

Monitor standards bodies and ingest updates autonomously.

## Research Loop

1. **Discover** standards from priority sources
2. **Extract** metadata and relationships
3. **Validate** against schema
4. **Score** confidence and relevance
5. **Generate** PR with standardized format
6. **Submit** for human review

## Data Extraction

For each standard:
- official_id (primary identifier)
- official_name
- official_url
- organization (standards body)
- domain (SIGMA domain)
- publication_date
- abstract/summary
- relationship links

## Validation Gates

- ✓ official_url is live and responds 200-399
- ✓ sigma_id is globally unique
- ✓ All required fields present
- ✓ Domain classification correct
- ✓ Relationships logically consistent

## Approval Model

- Agents CREATE pull requests
- Humans REVIEW and APPROVE
- CI validates completeness
- Merge triggers release build

## Priority Sources

See `docs/research-tasks.md` for current priority source list.
