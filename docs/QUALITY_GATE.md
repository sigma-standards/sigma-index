# SIGMA Quality Gate

This file is generated from `scripts/build_quality_gate.py`.
It summarizes deterministic release checks that do not require live network access.

| Check | Severity | Status | Detail |
|---|---|---|---|
| processed_duplicate_sigma_ids | critical | fail | 8 duplicate sigma_id values: BC-CBD-1992, DR-UNDRR-SENDAI-2015, EC-UNFCCC-PARIS-2015, EX-EITI-STANDARD-2023, FB-BCBS-BASELIII-2010, HR-UN-UDHR-1948, MO-UN-UNCLOS-1982, TR-UNECE-ADR-2023 |
| processed_required_fields | critical | pass | 0 missing required field values |
| processed_url_shape | critical | pass | 0 non-http official_url values |
