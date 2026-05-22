# Zenodo Archival & DOI Integration Guide

**Objective:** Publish SIGMA release to Zenodo for persistent archival, citable DOI, and scholarly discoverability.

---

## Overview

Zenodo is operated by CERN and provides persistent digital object identifiers (DOIs) for research datasets. Publishing SIGMA to Zenodo:
- ✅ Creates a citable DOI (e.g., `10.5281/zenodo.XXXXXXX`)
- ✅ Preserves the release in a long-term trusted repository
- ✅ Increases discoverability in academic and research databases
- ✅ Allows versioning (each release gets a new version DOI)
- ✅ Is **completely free** with no upload limits

---

## Pre-Archival Requirements

### 1. Create Zenodo Account
- [ ] Go to https://zenodo.org/
- [ ] Click "Sign up"
- [ ] Use GitHub account (OAuth) for seamless integration
- [ ] Verify email
- [ ] Create SIGMA organization profile (optional but recommended)

### 2. Link GitHub Repository to Zenodo

#### Option A: Enable GitHub Webhook (Automatic per Release)

1. [ ] Go to https://zenodo.org/account/settings/github/
2. [ ] Click "Connect GitHub"
3. [ ] Authorize Zenodo to access your GitHub account
4. [ ] Select `sigma-standards/sigma-index` repository
5. [ ] Toggle "On" to enable automatic archival on tag push

**Result:** Every time you push a Git tag (e.g., `git tag v1.0.0`), Zenodo automatically:
- Archives the repository snapshot
- Creates a DOI
- Publishes metadata

#### Option B: Manual Upload per Release

1. [ ] Go to https://zenodo.org/upload/
2. [ ] Create new upload
3. [ ] Fill in metadata
4. [ ] Download release artifacts from GitHub
5. [ ] Upload files manually
6. [ ] Publish

---

## Zenodo Publication Workflow

### Automatic Publication (GitHub Webhook)

1. [ ] Ensure webhook is enabled (see "Link GitHub Repository" above)

2. [ ] Create a release tag locally:
   ```bash
   git tag -a v1.0.0 -m "SIGMA v1.0.0 - MVP Release"
   ```

3. [ ] Push tag to GitHub:
   ```bash
   git push origin v1.0.0
   ```

4. [ ] Zenodo automatically:
   - [ ] Detects the tag push via webhook
   - [ ] Archives the full repository snapshot
   - [ ] Creates a DOI (e.g., 10.5281/zenodo.XXXXXXX)
   - [ ] Publishes metadata
   - [ ] Sends you a confirmation email with DOI link

5. [ ] Verify on Zenodo:
   - [ ] Go to https://zenodo.org/search/?q=SIGMA
   - [ ] Confirm your release appears
   - [ ] Copy DOI for citation

---

## DOI Citation Format

After publication, cite SIGMA with the DOI:

```bibtex
@dataset{sigma2026,
  author = {Islam, Mohammad Ariful},
  title = {SIGMA v1.0.0: Unified Global Standards Index},
  year = {2026},
  doi = {10.5281/zenodo.XXXXXXX},
  url = {https://zenodo.org/record/XXXXXXX},
  publisher = {Zenodo}
}
```

For APA citation:
```
Islam, M. A. (2026). SIGMA v1.0.0: Unified Global Standards Index [Dataset]. 
Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

---

## Post-Publication Integration

### Update SIGMA Documentation

- [ ] Add Zenodo DOI link to `README.md`
- [ ] Add DOI badge to GitHub Pages
- [ ] Add reference: "For cite-ability, see DOI: 10.5281/zenodo.XXXXXXX"
- [ ] Document in `CHANGELOG.md`

---

## Reference

- **Zenodo:** https://zenodo.org/
- **DOI System:** https://www.doi.org/
- **CC BY 4.0 License:** https://creativecommons.org/licenses/by/4.0/
