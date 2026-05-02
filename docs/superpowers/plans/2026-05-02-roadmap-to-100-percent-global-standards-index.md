# Roadmap to 100 Percent Global Standards Index

> **For agentic workers:** Execute this roadmap in sequence against the canonical research plan in `RESEARCH_PROJECT_PLAN_Global_Standards_Index.md`. Keep every source-backed data addition local and remote, update the source registry and research task matrix with each slice, and run validation before publishing.

**Goal:** Move SIGMA from the current public MVP into a complete, source-backed, machine-readable global standards index covering all 40 domains, all relevant layers, and all major international, regional, and national standards ecosystems.

**Current baseline:** 88,187 release entries, 20,130 relationship edges, all 40 canonical domains represented, and first ingestors completed for ISO, IETF RFCs, ILO, health priority records, Codex priority records, humanitarian priority records, WHO IRIS staging, IAEA Safety Standards priority records, GRI/SASB sustainability reporting records, NIST cybersecurity and AI priority records, W3C web standards priority records, ITU telecommunications priority records, ETSI ICT priority records, OASIS/Ecma/GS1 priority records, IEC electrotechnical priority records, CCSDS/ECSS space priority records, national standards bodies, and deterministic release quality gates.

**Completion target:** A v1.0 global release with comprehensive source registry coverage, repeatable ingestion pipelines, explicit provenance, deduplicated relationships, human-readable documentation, rendered project pages, quality reports, and public release artifacts.

---

## 0. Definition of 100 Percent

100 percent does not mean every paywalled full text is copied. It means SIGMA has the best lawful open metadata and source references for every major standards family, and full public-text harvesting where licensing permits.

### 0.1 Completion Criteria

1. **Domain coverage:** all 40 canonical domains have source-backed records beyond seed placeholders.
2. **Layer coverage:** global, regional, national, sectoral, treaty, classification, technical, governance, and implementation layers are represented.
3. **Source coverage:** every active source family has an entry in `data/reference/source_registry.csv`.
4. **Task coverage:** every domain has planned, active, or completed tasks in `data/reference/research_tasks.csv`.
5. **Processed data:** every promoted source writes schema-valid rows into `data/processed/`.
6. **Staging discipline:** broad harvesters write to `data/staging/` until curator filters are proven.
7. **Relationship graph:** issuer, successor, amendment, adoption, domain, treaty, and implementation relationships are captured in `data/relationships/`.
8. **Quality gates:** duplicate IDs, missing required fields, malformed URLs, broken local docs, and invalid relationships are checked before release.
9. **Publication:** GitHub Pages renders the landing page, downloads, domain coverage, source registry, task coverage, quality reports, and project documentation as HTML.
10. **Release governance:** v1.0 has release notes, a Git tag, persistent archival copy, and contribution workflow.

### 0.2 Workstream Numbering

The remaining work follows the actual research plan order:

1. Phase 0: Infrastructure hardening.
2. Phase 1: Free bulk source completion.
3. Phase 2: Human rights, humanitarian, health, labour, education, and development.
4. Phase 3: Environment, climate, and natural systems.
5. Phase 4: Finance, trade, and economic governance.
6. Phase 5: ICT, digital, AI, and cybersecurity.
7. Phase 6: Transport, energy, manufacturing, and built environment.
8. Phase 7: Society, culture, sports, legal, and specialised domains.
9. Phase 8: National standards bodies and regional standards networks.
10. Phase 9: Verification, publication, and community launch.
11. Phase 19: Enhanced architecture, automation, API, graph, multilingual, and sustainability roadmap.

---

## 1. Phase 0 - Infrastructure Hardening

### 1.1 Repository and Release Discipline

**Objective:** keep local and remote synchronized for every roadmap step.

**Tasks:**

1. Confirm `main` is aligned with `origin/main` before each data slice.
2. Keep generated outputs reproducible through `make release`.
3. Keep `dist/` ignored and regenerate it from source data.
4. Store all source references in `data/reference/`.
5. Store all promoted normalized records in `data/processed/`.
6. Store broad, uncurated harvest results in `data/staging/`.
7. Store generated reports in `data/reports/` and rendered docs in `docs/`.

**Validation:**

```bash
make validate
make release
python3 scripts/build_static_site.py
pytest
```

### 1.2 Documentation Navigation

**Objective:** make every project reference open as rendered HTML on GitHub Pages.

**Tasks:**

1. Add every major plan, task report, quality report, and schema reference to the static site documentation list.
2. Add cross-links from `README.md`, `index.md`, and the generated Pages footer.
3. Ensure documentation links use HTML targets, not raw Markdown targets.
4. Add tests for project reference links where possible.

---

## 2. Phase 1 - Free Bulk Source Completion

### 2.1 ISO Metadata Expansion

**Official resources:** ISO Standards catalogue, ISO members, ISO technical committees.

**References:**

- https://www.iso.org/standards.html
- https://www.iso.org/members.html
- https://www.iso.org/technical-committees.html

**Tasks:**

1. Refresh raw ISO open metadata if a newer official export is available.
2. Reconcile ISO deliverables with domain taxonomy, ICS codes, technical committees, and national member body records.
3. Add relationship edges for `issued_by`, `classified_by_ics`, `handled_by_tc`, `replaced_by`, and `adopted_by` where source metadata supports it.
4. Create an ISO refresh report with counts by ICS field, status, committee, and domain.
5. Run duplicate detection against national adoptions and IEC/ISO joint standards.

**Deliverables:**

- Updated `data/raw/iso/`.
- Updated `data/processed/iso_all.csv`.
- Updated `data/relationships/relationships_template.csv` or generated relationship file.
- Updated source registry and research task status.

### 2.2 IETF RFC Completion

**Official resources:** RFC Editor index and IETF Datatracker.

**References:**

- https://www.rfc-editor.org/rfc-index.html
- https://www.rfc-editor.org/rfc-index.xml
- https://datatracker.ietf.org/

**Tasks:**

1. Refresh RFC metadata from the RFC Editor index.
2. Add status, obsoletes, updates, and BCP/STD/FYI relationships.
3. Cross-link active standards-track RFCs to IANA registries where possible.
4. Add release report counts by RFC status and stream.

### 2.3 ILO NORMLEX Completion

**Official resources:** ILO NORMLEX instruments and ratification data.

**References:**

- https://normlex.ilo.org/
- https://www.ilo.org/international-labour-standards

**Tasks:**

1. Refresh all conventions, recommendations, protocols, and declarations.
2. Add ratification counts and status metadata where freely accessible.
3. Add relationships between conventions and protocols.
4. Add labour-domain quality report for active, revised, shelved, and withdrawn instruments.

### 2.4 UN Treaty Collection Foundation

**Official resources:** UN Treaty Collection.

**References:**

- https://treaties.un.org/

**Tasks:**

1. Create a UN treaty source registry record and staged ingestion table.
2. Capture treaty title, chapter, depositary, entry into force, status URL, and parties URL.
3. Promote high-confidence multilateral treaties into processed data by domain.
4. Add relationships between treaties, protocols, amendments, and implementing bodies.

---

## 3. Phase 2 - Human Rights, Humanitarian, Health, Labour, Education, and Development

### 3.1 Domain 1 - Health and Medical Standards

**Official resources:** WHO IRIS, WHO publications, International Health Regulations, ICD, ICF, essential medicines, emergency care standards.

**References:**

- https://iris.who.int/
- https://www.who.int/publications
- https://www.who.int/standards/classifications/classification-of-diseases
- https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health
- https://www.who.int/teams/health-product-policy-and-standards/standards-and-specifications/norms-and-standards-for-pharmaceuticals

**Tasks:**

1. Turn WHO IRIS staging into a production harvester with strict normative filters.
2. Separate guidelines, classifications, treaties, policy frameworks, and technical specifications.
3. Promote only curator-approved IRIS records from `data/staging/who_iris_filtered_metadata.csv`.
4. Add WHO source families to `source_registry.csv` with harvesting cadence and risk notes.
5. Add relationship edges from WHO records to health, WASH, humanitarian, emergency response, and medicine domains.
6. Add tests that prevent general publications from flooding the standards index.

### 3.2 Domain 2 - Food Safety and Agriculture

**Official resources:** Codex Alimentarius, FAOLEX, IPPC ISPMs, WOAH Codes and Manuals.

**References:**

- https://www.fao.org/fao-who-codexalimentarius/codex-texts/list-standards/
- https://www.fao.org/faolex/
- https://www.ippc.int/en/core-activities/standards-setting/ispms/
- https://www.woah.org/en/what-we-do/standards/

**Tasks:**

1. Expand Codex beyond the first priority slice to all standards, guidelines, codes of practice, and maximum residue limits where metadata is open.
2. Add IPPC adopted ISPMs with adoption date, CPM status, and topic.
3. Add WOAH Terrestrial Code, Aquatic Code, Terrestrial Manual, and Aquatic Manual metadata.
4. Stage FAOLEX treaty and legislation records, then promote only international and regional standards-relevant instruments.
5. Add relationships among Codex, WHO, FAO, WTO SPS, IPPC, and WOAH instruments.

### 3.3 Domain 15 - Human Rights

**Official resources:** OHCHR core instruments, treaty bodies, special procedures, UN Treaty Collection, regional human rights systems.

**References:**

- https://www.ohchr.org/en/core-international-human-rights-instruments-and-their-monitoring-bodies
- https://www.ohchr.org/en/treaty-bodies
- https://www.ohchr.org/en/special-procedures-human-rights-council
- https://treaties.un.org/
- https://www.echr.coe.int/
- https://achpr.au.int/
- https://www.oas.org/en/iachr/

**Tasks:**

1. Add all core UN human rights treaties and optional protocols.
2. Add treaty body general comments and recommendations with issuing committee and instrument relationship.
3. Add regional instruments from Europe, Africa, Inter-American, Arab, and ASEAN systems.
4. Add relationships between treaties, protocols, monitoring bodies, and regional analogues.
5. Add domain review checklist for sensitive naming, historical status, and official citation.

### 3.4 Domain 16 - Labour

**Official resources:** ILO NORMLEX.

**References:**

- https://normlex.ilo.org/
- https://www.ilo.org/international-labour-standards

**Tasks:**

1. Complete all ILO conventions, recommendations, protocols, declarations, and maritime labour instruments.
2. Add fundamental, governance, technical, and occupational safety classification.
3. Add relationship edges for revises, supplements, protocol-to-convention, and category membership.
4. Add ratification/status summary fields where the schema permits or sidecar tables where needed.

### 3.5 Domain 17 - Humanitarian Standards

**Official resources:** Sphere, CHS, INEE, IASC, UNHCR Emergency Handbook, WHO Emergency Medical Teams.

**References:**

- https://spherestandards.org/handbook/
- https://www.corehumanitarianstandard.org/
- https://inee.org/minimum-standards
- https://interagencystandingcommittee.org/
- https://emergency.unhcr.org/
- https://extranet.who.int/emt/

**Tasks:**

1. Complete Sphere chapter-level and standard-level records.
2. Expand CHS commitments, quality criteria, and verification scheme records.
3. Add INEE domains, standards, key actions, and guidance notes at the appropriate granularity.
4. Add IASC guidelines for protection, GBV, PSEA, mental health, accountability, coordination, shelter, CCCM, and inclusion.
5. Add UNHCR emergency standards and policy records.
6. Add WHO EMT minimum standards and classification records.
7. Add relationships among humanitarian, health, WASH, education, protection, and disaster-risk records.

### 3.6 Domain 20 - Education and Research

**Official resources:** UNESCO, ISCED, Declaration of Helsinki, ICH GCP, FAIR Principles, ORCID, Crossref, Dublin Core.

**References:**

- https://uis.unesco.org/en/topic/international-standard-classification-education-isced
- https://www.unesco.org/en/legal-affairs/conventions
- https://www.wma.net/policies-post/wma-declaration-of-helsinki/
- https://ich.org/page/efficacy-guidelines
- https://www.go-fair.org/fair-principles/
- https://info.orcid.org/documentation/
- https://www.crossref.org/documentation/
- https://www.dublincore.org/specifications/

**Tasks:**

1. Add ISCED and UNESCO qualification recognition conventions.
2. Add core research ethics and clinical research standards.
3. Add scholarly metadata standards and persistent identifier systems.
4. Add relationships between education classifications, research ethics, metadata, and health research standards.

---

## 4. Phase 3 - Environment, Climate, and Natural Systems

### 4.1 Climate Change and Emissions

**Official resources:** UNFCCC, Kyoto Protocol, Paris Agreement, GHG Protocol, SBTi, TNFD.

**References:**

- https://unfccc.int/process-and-meetings
- https://ghgprotocol.org/standards
- https://sciencebasedtargets.org/standards
- https://tnfd.global/

**Tasks:**

1. Add UNFCCC, Kyoto Protocol, Paris Agreement, and major COP decision families.
2. Add GHG Protocol standards and guidance documents.
3. Add SBTi criteria and sector guidance records.
4. Add TNFD disclosure framework metadata.
5. Link climate records to finance, corporate reporting, energy, agriculture, and biodiversity records.

### 4.2 Biodiversity, Conservation, and Chemicals

**Official resources:** CBD, CITES, Ramsar, Basel/Rotterdam/Stockholm conventions, Minamata Convention, Montreal Protocol.

**References:**

- https://www.cbd.int/convention/
- https://cites.org/eng/disc/text.php
- https://www.ramsar.org/
- https://www.brsmeas.org/
- https://minamataconvention.org/
- https://ozone.unep.org/treaties/montreal-protocol

**Tasks:**

1. Add convention, protocol, annex, appendix, and COP decision families.
2. Model controlled substances, species appendices, wetlands guidance, and chemicals conventions as linked records.
3. Add treaty-to-secretariat and treaty-to-protocol relationships.
4. Add environmental source review checklist for living appendices and amendments.

### 4.3 Disaster Risk, Oceans, and Nuclear Safety

**Official resources:** Sendai Framework, UNCLOS, IMO conventions, IAEA Safety Standards.

**References:**

- https://www.undrr.org/implementing-sendai-framework
- https://www.un.org/depts/los/convention_agreements/convention_overview_convention.htm
- https://www.imo.org/en/About/Conventions/Pages/ListOfConventions.aspx
- https://www.iaea.org/resources/safety-standards

**Tasks:**

1. Add Sendai Framework and UNDRR terminology records.
2. Add UNCLOS and related ocean instruments.
3. Add IMO marine environment and safety conventions that overlap with environment.
4. Maintain and expand the active IAEA Safety Standards priority metadata slice toward full Safety Standards Series catalogue coverage and relationships to nuclear, energy, health, and environment domains.

---

## 5. Phase 4 - Finance, Trade, and Economic Governance

### 5.1 Financial Stability, Banking, Insurance, Securities

**Official resources:** BCBS, FSB, IOSCO, IAIS.

**References:**

- https://www.bis.org/basel_framework/
- https://www.fsb.org/work-of-the-fsb/about-the-compendium-of-standards/
- https://www.iosco.org/library/pubdocs/
- https://www.iaisweb.org/activities/standard-setting/

**Tasks:**

1. Add Basel Framework standards and supporting publications.
2. Add FSB key standards and compendium links.
3. Add IOSCO principles, objectives, and methodology records.
4. Add IAIS Insurance Core Principles and ComFrame.
5. Link finance records to risk, governance, cybersecurity, sustainability, and accounting records.

### 5.2 Accounting, Audit, Anti-Money Laundering, Tax

**Official resources:** IFRS Foundation, ISSB, IAASB, FATF, OECD legal instruments and BEPS.

**References:**

- https://www.ifrs.org/issued-standards/list-of-standards/
- https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/
- https://www.iaasb.org/standards-pronouncements
- https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html
- https://legalinstruments.oecd.org/
- https://www.oecd.org/tax/beps/

**Tasks:**

1. Add IFRS, IAS, IFRIC, SIC, and ISSB standards metadata.
2. Add audit and assurance standards from IAASB.
3. Add FATF Recommendations, methodology, and guidance.
4. Add OECD BEPS actions and major tax instruments.
5. Add relationships between disclosure, audit, AML, tax, and sustainability reporting standards.

### 5.3 Trade, Customs, and Product Rules

**Official resources:** WTO, WCO, UN/CEFACT, ISO 20022.

**References:**

- https://www.wto.org/english/docs_e/legal_e/legal_e.htm
- https://tbtims.wto.org/
- https://www.wcoomd.org/
- https://unece.org/trade/uncefact
- https://www.iso20022.org/

**Tasks:**

1. Add WTO agreements, SPS/TBT links, and legal texts.
2. Stage WTO TBT/SPS notification metadata only where it describes standards-relevant instruments.
3. Add WCO Harmonized System and customs instruments.
4. Add UN/CEFACT trade facilitation recommendations.
5. Add ISO 20022 metadata and relationships to banking, payments, and messaging standards.

---

## 6. Phase 5 - ICT, Digital, AI, and Cybersecurity

### 6.1 Web, Internet, Telecom, and Interoperability

**Official resources:** W3C, IETF, ITU, ETSI, OASIS, ECMA, GS1.

**References:**

- https://www.w3.org/TR/
- https://www.rfc-editor.org/
- https://www.itu.int/rec/
- https://www.etsi.org/standards
- https://www.oasis-open.org/standards/
- https://ecma-international.org/publications-and-standards/standards/
- https://www.gs1.org/standards

**Tasks:**

1. Maintain and expand the active W3C priority Standards metadata slice toward the full Technical Reports standards index.
2. Maintain and expand the active ITU priority Recommendations slice by sector, series, and study group.
3. Maintain and expand the active ETSI priority standards slice and cross-links to European standards.
4. Maintain and expand the active OASIS, Ecma, and GS1 priority metadata slices toward full standards-catalogue coverage.
5. Create relationships among web, telecom, identity, supply chain, and cybersecurity records.

### 6.2 Cybersecurity and Privacy

**Official resources:** NIST CSRC, FIPS, ENISA, PCI SSC, ISO/IEC metadata.

**References:**

- https://csrc.nist.gov/
- https://csrc.nist.gov/publications/fips
- https://www.enisa.europa.eu/publications
- https://www.pcisecuritystandards.org/standards/
- https://www.iso.org/committee/45306.html

**Tasks:**

1. Add NIST SP 800 series and FIPS records.
2. Add ENISA good-practice and framework records where standards-relevant.
3. Add PCI DSS and PCI SSC standards.
4. Link ISO/IEC 27000 family metadata to cybersecurity frameworks and controls.
5. Add privacy regulation instruments only when they define reusable compliance frameworks or standards.

### 6.3 Artificial Intelligence and Emerging Technology

**Official resources:** NIST AI RMF, ISO/IEC JTC 1 SC 42, OECD AI, UNESCO AI Ethics, EU AI Act.

**References:**

- https://www.nist.gov/itl/ai-risk-management-framework
- https://www.iso.org/committee/6794475.html
- https://oecd.ai/en/ai-principles
- https://www.unesco.org/en/artificial-intelligence/recommendation-ethics
- https://eur-lex.europa.eu/

**Tasks:**

1. Add AI risk, governance, ethics, management, and conformity assessment records.
2. Add quantum, identity, and data governance standards from official standards bodies.
3. Link AI records to privacy, cybersecurity, human rights, health, finance, and education domains.

---

## 7. Phase 6 - Transport, Energy, Manufacturing, and Built Environment

### 7.1 Aviation, Maritime, Space, Road, and Rail

**Official resources:** ICAO, IMO, CCSDS, ECSS, UNECE WP.29, UIC where public.

**References:**

- https://www.icao.int/safety/safetymanagement/pages/sarps.aspx
- https://www.imo.org/en/About/Conventions/Pages/ListOfConventions.aspx
- https://ccsds.org/publications/bluebooks2-0/
- https://ecss.nl/standards/active-standards/
- https://unece.org/transport/vehicle-regulations
- https://uic.org/

**Tasks:**

1. Add ICAO Annex-level metadata and SARPs structure where lawful.
2. Add IMO conventions, codes, and circular families.
3. Maintain and expand the active CCSDS/ECSS priority metadata slice toward full space standards catalogue coverage.
4. Add UNECE vehicle regulations and global technical regulations.
5. Add relationship edges among transport safety, space operations, emissions, labour, trade, and accessibility standards.

### 7.2 Energy, Electrical, Nuclear, and Smart Infrastructure

**Official resources:** IEC, IAEA, ISO 50001, ITU smart grid, IRENA where standards-relevant.

**References:**

- https://webstore.iec.ch/
- https://www.iaea.org/resources/safety-standards
- https://www.iso.org/iso-50001-energy-management.html
- https://www.itu.int/rec/
- https://www.irena.org/

**Tasks:**

1. Maintain and expand the active IEC priority metadata slice toward full IEC catalogue coverage by technical committee and standard family.
2. Add ISO energy management family metadata.
3. Maintain and expand the active IAEA Safety Standards priority metadata slice and add nuclear security series.
4. Add smart grid, renewable energy, and energy efficiency framework records.

### 7.3 Manufacturing, Quality, Construction, and Built Environment

**Official resources:** ISO, IEC, ASTM, ASME, NFPA, ASHRAE, CEN/CENELEC public metadata.

**References:**

- https://www.iso.org/standards.html
- https://webstore.iec.ch/
- https://www.astm.org/products-services/standards-and-publications.html
- https://www.asme.org/codes-standards
- https://www.nfpa.org/codes-and-standards
- https://www.ashrae.org/technical-resources/standards-and-guidelines
- https://www.cencenelec.eu/

**Tasks:**

1. Capture public metadata for major engineering standards where full text is paywalled.
2. Enrich internationally important quality, safety, construction, and manufacturing standards.
3. Add adoption relationships between ISO/IEC, European, and national standards where source metadata permits.

---

## 8. Phase 7 - Society, Culture, Sports, Legal, and Specialised Domains

### 8.1 Law, Commercial Practice, and Governance

**Official resources:** UNCITRAL, UNIDROIT, OECD legal instruments, ICC public summaries, UN Treaty Collection.

**References:**

- https://uncitral.un.org/en/texts
- https://www.unidroit.org/instruments/
- https://legalinstruments.oecd.org/
- https://iccwbo.org/business-solutions/incoterms-rules/
- https://treaties.un.org/

**Tasks:**

1. Add UNCITRAL model laws, conventions, legislative guides, and rules.
2. Add UNIDROIT conventions, principles, and model laws.
3. Add OECD legal instruments by theme.
4. Add ICC instruments with open metadata and official reference URLs.
5. Add relationships between legal instruments, trade, finance, arbitration, and governance records.

### 8.2 Culture, Heritage, and Knowledge Systems

**Official resources:** UNESCO conventions, ICOMOS charters, ICOM Code of Ethics, ICCROM resources.

**References:**

- https://www.unesco.org/en/legal-affairs/conventions
- https://www.icomos.org/en/resources/charters-and-texts
- https://icom.museum/en/resources/standards-guidelines/code-of-ethics/
- https://www.iccrom.org/resources

**Tasks:**

1. Add UNESCO culture and heritage conventions.
2. Add ICOMOS charters and doctrinal texts.
3. Add ICOM and ICCROM standards and guidance records.
4. Link culture records to education, indigenous rights, environment, and disaster risk.

### 8.3 Sports, Anti-Doping, and Event Governance

**Official resources:** WADA, UNESCO anti-doping convention, IOC, FIFA, World Athletics, CAS.

**References:**

- https://www.wada-ama.org/en/what-we-do/world-anti-doping-code
- https://www.unesco.org/en/legal-affairs/international-convention-against-doping-sport
- https://olympics.com/ioc/olympic-charter
- https://www.fifa.com/legal
- https://worldathletics.org/about-iaaf/documents/book-of-rules
- https://www.tas-cas.org/en/arbitration/code-procedural-rules.html

**Tasks:**

1. Add WADA Code, international standards, and prohibited list records.
2. Add UNESCO anti-doping convention.
3. Add Olympic Charter, FIFA legal instruments, World Athletics rules, and CAS procedural rules.
4. Link sports records to health, law, human rights, safety, and event management.

### 8.4 Defence, Security, Arms Control, and Public Safety

**Official resources:** UNODA, OPCW, CTBTO, IAEA, NATO public documents, US DoD public standards.

**References:**

- https://disarmament.unoda.org/
- https://www.opcw.org/chemical-weapons-convention
- https://www.ctbto.org/our-mission/the-treaty
- https://www.iaea.org/topics/safeguards-legal-framework
- https://www.nato.int/cps/en/natohq/official_texts.htm
- https://quicksearch.dla.mil/

**Tasks:**

1. Add arms control treaties and verification instruments.
2. Add public NATO documents and declassified/public military standards metadata.
3. Add relationships among security, nuclear, chemical, humanitarian law, and public safety records.
4. Keep restricted or non-public material out of the index.

---

## 9. Phase 8 - National Standards Bodies and Regional Networks

### 9.1 ISO Member Body Completion

**Official resources:** ISO member list and national body websites.

**References:**

- https://www.iso.org/members.html

**Tasks:**

1. Expand from the first 10 national standards bodies to every ISO member, correspondent member, and subscriber member.
2. Capture official name, acronym, country, website, membership category, founding year where available, and designation series.
3. Link each body to ISO, IEC, regional standards organizations, and national standards catalogues.
4. Add national body validation checks for official URL, ISO membership category, and duplicate country coverage.

### 9.2 Regional Standards Organizations

**Official resources:** CEN/CENELEC, ETSI, ARSO, ASEAN, GSO, COPANT, PASC.

**References:**

- https://www.cencenelec.eu/
- https://www.etsi.org/
- https://www.arso-oran.org/
- https://asean.org/our-communities/economic-community/standards-and-conformance/
- https://www.gso.org.sa/
- https://www.copant.org/
- https://www.pascnet.org/

**Tasks:**

1. Add regional standards organizations and member relationships.
2. Add regional standard series metadata where public.
3. Map adoption links between international, regional, and national layers.
4. Prioritize regions underrepresented in current global standards datasets.

### 9.3 Nationally Important Standard Families

**References:** national catalogue URLs from each source registry entry.

**Tasks:**

1. For each high-impact national body, identify internationally significant native standard families.
2. Add public metadata only unless full text is open.
3. Mark adoption, equivalence, withdrawal, and replacement relationships.
4. Document licensing limits for paywalled national standards.

---

## 10. Phase 9 - Verification, Publication, and Community Launch

### 10.1 Data Quality Gates

**Tasks:**

1. Duplicate `sigma_id` check.
2. Required field completeness check.
3. Official URL syntax check.
4. Optional live URL audit with rate limits and retry policy.
5. Relationship target existence check.
6. Domain taxonomy validity check.
7. Source registry coverage check.
8. Research task coverage check.
9. Markdown documentation rendering check.
10. Release artifact generation check.

### 10.2 Expert and Community Review

**Tasks:**

1. Assign one reviewer per meta-layer: health, food/agriculture, labour, humanitarian, environment, finance/trade, ICT, engineering, law, culture/sports, national bodies.
2. Create GitHub issue templates for source correction, duplicate report, missing standard, broken link, and domain expansion.
3. Add review labels that map back to domain IDs and roadmap phases.
4. Publish review status in `docs/RESEARCH_TASKS.md`.

### 10.3 v1.0 Publication

**Tasks:**

1. Freeze v1.0 source data after validation.
2. Generate CSV, JSON, JSONL, relationship, domain coverage, source registry, quality gate, and task coverage artifacts.
3. Build and publish GitHub Pages.
4. Create GitHub release and tag.
5. Archive release on Zenodo or another open repository.
6. Announce to standards, open data, humanitarian, public health, and research communities.

---

## 11. Phase 19 - Enhanced Architecture and Sustainability

### 11.1 Knowledge Graph

**Tasks:**

1. Define RDF/JSON-LD mapping for standards, bodies, domains, classifications, treaties, and relationships.
2. Generate graph exports from canonical CSV/JSON.
3. Add relationship types for `implements`, `amends`, `replaces`, `cites`, `adopts`, `equivalent_to`, `classified_by`, and `issued_by`.
4. Add graph validation checks.

### 11.2 Search, API, and User Experience

**Tasks:**

1. Maintain the active Pagefind-compatible static full-text search layer in GitHub Pages.
2. Extend domain filtering into issuer, country, source family, status, and phase filters.
3. Add API index documentation with examples.
4. Add downloadable slices for standards bodies, treaties, health, humanitarian, environment, finance, ICT, and national body records.
5. Add accessibility checks for the published Pages site.

### 11.3 Automation and Freshness

**Tasks:**

1. Classify sources by update cadence: daily, weekly, monthly, quarterly, annual, manual.
2. Add deterministic fixture tests for every harvester.
3. Add staging reports that show candidate counts, promoted counts, rejected counts, and filter reasons.
4. Add source freshness reports by domain.
5. Keep broad harvesters conservative until false-positive risk is measured.

### 11.4 Multilingual and Global Equity

**Tasks:**

1. Preserve official names in original languages where available.
2. Add alternate names and acronyms without overwriting official English titles.
3. Prioritize underrepresented regions and Global South standards bodies.
4. Add translation and transliteration fields only through schema-governed changes.

### 11.5 Governance and Partnerships

**Tasks:**

1. Publish curation rules, conflict resolution process, and source acceptance rules.
2. Recruit domain maintainers.
3. Create partnership outreach list for standards bodies, academic libraries, humanitarian networks, and open data communities.
4. Define release cadence after v1.0.

---

## 12. Sequenced Execution Plan

### 12.1 Next 30 Days

1. Promote the roadmap into project documentation and Pages navigation.
2. Complete Phase 2 WHO IRIS promotion rules.
3. Expand Codex/IPPC/WOAH food and agriculture coverage.
4. Expand CHS/INEE/IASC/UNHCR/EMT humanitarian coverage.
5. Add OHCHR core human rights instruments.
6. Add UN Treaty Collection staging.
7. Add source registry rows for every source touched.
8. Run full validation and publish after each slice.

### 12.2 Days 31-90

1. Complete Phase 2 labour, human rights, health, humanitarian, education, and development.
2. Build Phase 3 environmental treaty ingestors and curated tables.
3. Add first finance/trade source families: BCBS, FATF, IFRS, WTO, OECD.
4. Add relationship extraction improvements.
5. Add source freshness and task coverage reports to Pages.

### 12.3 Months 4-6

1. Complete Phase 3 environment and climate.
2. Complete Phase 4 finance, trade, and economic governance.
3. Expand active W3C, ITU, NIST, ETSI, OASIS, Ecma, and GS1 metadata from priority slices toward full catalogue coverage.
4. Add national standards body expansion to at least all ISO full members.
5. Add expert review workflow and issue labels.

### 12.4 Months 7-12

1. Complete Phase 5 ICT, AI, privacy, and cybersecurity.
2. Complete Phase 6 transport, energy, manufacturing, and built environment metadata.
3. Complete Phase 7 legal, culture, sports, defence, and specialised domains.
4. Complete all ISO member, correspondent, and subscriber body records.
5. Prepare v0.9 release candidate with quality reports.

### 12.5 Months 13-24

1. Complete regional and national adoption relationships.
2. Build knowledge graph exports.
3. Add richer static search and API documentation.
4. Complete multilingual metadata policy and first alternate-name pass.
5. Run expert review and public correction campaign.
6. Publish SIGMA v1.0 complete release.

---

## 13. Master Source Reference Register

| Phase | Source family | Official resource |
|---|---|---|
| 1 | ISO standards | https://www.iso.org/standards.html |
| 1 | ISO members | https://www.iso.org/members.html |
| 1 | RFC Editor | https://www.rfc-editor.org/rfc-index.html |
| 1 | IETF Datatracker | https://datatracker.ietf.org/ |
| 1 | ILO NORMLEX | https://normlex.ilo.org/ |
| 1 | UN Treaty Collection | https://treaties.un.org/ |
| 2 | WHO IRIS | https://iris.who.int/ |
| 2 | WHO publications | https://www.who.int/publications |
| 2 | Codex Alimentarius | https://www.fao.org/fao-who-codexalimentarius/codex-texts/list-standards/ |
| 2 | FAOLEX | https://www.fao.org/faolex/ |
| 2 | IPPC ISPMs | https://www.ippc.int/en/core-activities/standards-setting/ispms/ |
| 2 | WOAH standards | https://www.woah.org/en/what-we-do/standards/ |
| 2 | OHCHR instruments | https://www.ohchr.org/en/core-international-human-rights-instruments-and-their-monitoring-bodies |
| 2 | Sphere Handbook | https://spherestandards.org/handbook/ |
| 2 | Core Humanitarian Standard | https://www.corehumanitarianstandard.org/ |
| 2 | INEE Minimum Standards | https://inee.org/minimum-standards |
| 2 | IASC | https://interagencystandingcommittee.org/ |
| 2 | UNHCR Emergency Handbook | https://emergency.unhcr.org/ |
| 2 | WHO Emergency Medical Teams | https://extranet.who.int/emt/ |
| 2 | UNESCO ISCED | https://uis.unesco.org/en/topic/international-standard-classification-education-isced |
| 3 | UNFCCC | https://unfccc.int/process-and-meetings |
| 3 | GHG Protocol | https://ghgprotocol.org/standards |
| 3 | CBD | https://www.cbd.int/convention/ |
| 3 | CITES | https://cites.org/eng/disc/text.php |
| 3 | Ramsar | https://www.ramsar.org/ |
| 3 | Basel, Rotterdam, Stockholm conventions | https://www.brsmeas.org/ |
| 3 | Minamata Convention | https://minamataconvention.org/ |
| 3 | Montreal Protocol | https://ozone.unep.org/treaties/montreal-protocol |
| 3 | UNDRR Sendai | https://www.undrr.org/implementing-sendai-framework |
| 3 | UNCLOS | https://www.un.org/depts/los/convention_agreements/convention_overview_convention.htm |
| 3 | IAEA Safety Standards | https://www.iaea.org/resources/safety-standards |
| 4 | Basel Framework | https://www.bis.org/basel_framework/ |
| 4 | FSB compendium | https://www.fsb.org/work-of-the-fsb/about-the-compendium-of-standards/ |
| 4 | IOSCO publications | https://www.iosco.org/library/pubdocs/ |
| 4 | IAIS standards | https://www.iaisweb.org/activities/standard-setting/ |
| 4 | IFRS standards | https://www.ifrs.org/issued-standards/list-of-standards/ |
| 4 | IAASB standards | https://www.iaasb.org/standards-pronouncements |
| 4 | FATF recommendations | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html |
| 4 | OECD legal instruments | https://legalinstruments.oecd.org/ |
| 4 | WTO legal texts | https://www.wto.org/english/docs_e/legal_e/legal_e.htm |
| 4 | WTO TBT IMS | https://tbtims.wto.org/ |
| 4 | WCO | https://www.wcoomd.org/ |
| 4 | UN/CEFACT | https://unece.org/trade/uncefact |
| 5 | W3C Recommendations | https://www.w3.org/TR/ |
| 5 | ITU Recommendations | https://www.itu.int/rec/ |
| 5 | ETSI standards | https://www.etsi.org/standards |
| 5 | OASIS standards | https://www.oasis-open.org/standards/ |
| 5 | ECMA standards | https://ecma-international.org/publications-and-standards/standards/ |
| 5 | GS1 standards | https://www.gs1.org/standards |
| 5 | NIST CSRC | https://csrc.nist.gov/ |
| 5 | NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework |
| 5 | ENISA publications | https://www.enisa.europa.eu/publications |
| 5 | PCI SSC standards | https://www.pcisecuritystandards.org/standards/ |
| 5 | UNESCO AI Ethics | https://www.unesco.org/en/artificial-intelligence/recommendation-ethics |
| 6 | IEC standards | https://webstore.iec.ch/ |
| 6 | ICAO SARPs | https://www.icao.int/safety/safetymanagement/pages/sarps.aspx |
| 6 | IMO conventions | https://www.imo.org/en/About/Conventions/Pages/ListOfConventions.aspx |
| 6 | UNECE vehicle regulations | https://unece.org/transport/vehicle-regulations |
| 6 | ASTM standards | https://www.astm.org/products-services/standards-and-publications.html |
| 6 | ASME codes and standards | https://www.asme.org/codes-standards |
| 6 | NFPA codes and standards | https://www.nfpa.org/codes-and-standards |
| 6 | ASHRAE standards | https://www.ashrae.org/technical-resources/standards-and-guidelines |
| 7 | UNCITRAL texts | https://uncitral.un.org/en/texts |
| 7 | UNIDROIT instruments | https://www.unidroit.org/instruments/ |
| 7 | UNESCO conventions | https://www.unesco.org/en/legal-affairs/conventions |
| 7 | ICOMOS charters | https://www.icomos.org/en/resources/charters-and-texts |
| 7 | ICOM Code of Ethics | https://icom.museum/en/resources/standards-guidelines/code-of-ethics/ |
| 7 | WADA Code | https://www.wada-ama.org/en/what-we-do/world-anti-doping-code |
| 7 | IOC Olympic Charter | https://olympics.com/ioc/olympic-charter |
| 7 | FIFA legal | https://www.fifa.com/legal |
| 7 | World Athletics rules | https://worldathletics.org/about-iaaf/documents/book-of-rules |
| 7 | CAS rules | https://www.tas-cas.org/en/arbitration/code-procedural-rules.html |
| 7 | UNODA disarmament | https://disarmament.unoda.org/ |
| 7 | OPCW Chemical Weapons Convention | https://www.opcw.org/chemical-weapons-convention |
| 7 | CTBTO treaty | https://www.ctbto.org/our-mission/the-treaty |
| 8 | CEN/CENELEC | https://www.cencenelec.eu/ |
| 8 | ARSO | https://www.arso-oran.org/ |
| 8 | ASEAN standards and conformance | https://asean.org/our-communities/economic-community/standards-and-conformance/ |
| 8 | GSO | https://www.gso.org.sa/ |
| 8 | COPANT | https://www.copant.org/ |
| 8 | PASC | https://www.pascnet.org/ |

---

## 14. Acceptance Checklist for Every Slice

1. Source is official, stable, and documented.
2. Licensing is respected; paywalled full text is not copied.
3. New source family is added to `source_registry.csv`.
4. New task or status update is added to `research_tasks.csv`.
5. Ingestor has deterministic fixture tests when automated.
6. Processed rows conform to `SCHEMA.md`.
7. Relationship rows validate against processed IDs.
8. Documentation explains scope, exclusions, and next steps.
9. `make validate` passes.
10. Static site builds and renders relevant docs.
11. Changes are committed locally and published remotely.

---

## 15. Gap Analysis Incorporation Register

The external feedback document `docs/SIGMA_GAP_ANALYSIS_AND_ENHANCEMENT_PLAN.md` has been reviewed against the current repository state. Items below are now accepted into the roadmap and reflected in `data/reference/research_tasks.csv` where they require follow-up work.

### 15.1 Accepted Critical Enhancements

1. **Full CI gate:** add one explicit `ci.yml` that runs `make validate` and the pytest suite on push and pull request, complementing the existing schema, release, URL check, and Pages workflows.
2. **README credibility signals:** keep badges, sample records, and contributor pathways visible from the first screen of the repository.
3. **Search and discovery:** maintain the active Pagefind-compatible static search layer and extend it with richer filters before public v1.0.
4. **Priority ingestors:** add W3C, NIST, IEC, ITU, IAEA, CCSDS, GRI/SASB, UN Treaty Collection, sports, and culture/heritage work items to the task matrix.
5. **Publication and outreach:** track HDX submission and Zenodo DOI publication as launch-quality tasks.

### 15.2 Current-State Corrections

1. GitHub Actions are present; the gap is unified CI coverage and report publication, not total absence of workflows.
2. GitHub Pages is present and designed with Pagefind-compatible search; the remaining gap is richer faceting and entry-level browsing.
3. Issue templates exist; the gap is structured YAML forms for domain contributions and source corrections.
4. Relationship edges exist in `relationships_extracted.csv`; the remaining quality task is confidence review and source traceability.

### 15.3 First Implementation Order

1. Add full CI workflow.
2. Render the gap analysis as a project reference.
3. Convert accepted recommendations into `research_tasks.csv`.
4. Generate updated task coverage docs.
5. Keep future harvester implementation in separate source-specific slices so each source can be tested and reviewed safely.
