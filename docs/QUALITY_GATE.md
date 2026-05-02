# SIGMA Quality Gate

This file is generated from `scripts/build_quality_gate.py`.
It summarizes deterministic release checks that do not require live network access.

| Check | Severity | Status | Detail |
|---|---|---|---|
| processed_duplicate_sigma_ids | critical | pass | 0 duplicate sigma_id values |
| processed_required_fields | critical | pass | 0 missing required field values |
| processed_url_shape | critical | pass | 0 non-http official_url values |
