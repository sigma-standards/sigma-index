# UNIFIED INDEX OF ALL GLOBAL STANDARDS
## World's First Universal Digital Ecosystem of Human Civilisation's Standards
### Research Project Plan — v1.0 | May 2026

---

> **Project Codename:** `SIGMA` — *Standards Index of Global Meta-Archives*
>
> **Owner:**  Mohammad Ariful Islam
>
> **Classification:** Open Research | Free to Use | CC BY 4.0
>
> **Ambition:** Build and maintain the world's most complete, freely accessible, machine-readable,
> human-navigable unified index of every global standard, framework, treaty, guideline, and
> classification system that governs human civilisation — across all domains, all layers, all sectors,
> all geographies — without any subscription, paywall, or credit card requirement.

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement & Rationale](#2-problem-statement--rationale)
3. [Vision, Mission & Guiding Principles](#3-vision-mission--guiding-principles)
4. [Scope — The Full Universe of Human Standards](#4-scope--the-full-universe-of-human-standards)
5. [Master Domain Taxonomy — All 40 Domains](#5-master-domain-taxonomy--all-40-domains)
6. [Scale & Quantitative Scope](#6-scale--quantitative-scope)
7. [Free Data Sources — Deep Research Findings](#7-free-data-sources--deep-research-findings)
8. [Free Tools Stack — Zero Cost, Zero Credit Card](#8-free-tools-stack--zero-cost-zero-credit-card)
9. [Data Schema & Architecture](#9-data-schema--architecture)
10. [Phased Research & Build Plan](#10-phased-research--build-plan)
11. [Research Methodology per Domain](#11-research-methodology-per-domain)
12. [Quality Assurance & Validation Protocol](#12-quality-assurance--validation-protocol)
13. [Governance & Maintenance Model](#13-governance--maintenance-model)
14. [Risk Register & Mitigations](#14-risk-register--mitigations)
15. [Milestones & Success Metrics](#15-milestones--success-metrics)
16. [Annex A — Full Domain-by-Domain Source Map](#annex-a--full-domain-by-domain-source-map)
17. [Annex B — Free Tool Setup Guide](#annex-b--free-tool-setup-guide)
18. [Annex C — Wikidata SPARQL Queries for Standards Bodies](#annex-c--wikidata-sparql-queries-for-standards-bodies)

---

## 1. EXECUTIVE SUMMARY

The world currently has **no single place** where anyone — a researcher, a policymaker, an NGO worker, a student, a regulator, a journalist — can look up any global standard and find verified, structured, cross-referenced information about it. Standards exist in silos: ISO has its catalogue, WHO has its guidelines, ILO has its conventions, ICAO has its SARPs, and thousands of other bodies maintain their own registries. None of these are interoperable, and none are free.

This project — **SIGMA** — exists to solve that problem permanently.

SIGMA will be a **unified, freely accessible, machine-readable index** of every known global standard, standards body, framework, treaty, guideline, classification system, code of practice, and technical specification that has formal international standing. It will cover every domain of human society: from health and education to aerospace and art, from nuclear energy to humanitarian response, from financial regulation to sports governance.

The index will be built entirely using **free, open tools** — requiring no subscriptions, no credit card, no proprietary software. It will be published on GitHub under CC BY 4.0 license, hosted freely on GitHub Pages, and made downloadable in Excel, CSV, JSON, and Parquet formats so that anyone in the world can use it regardless of their technology environment.

This document is the complete research and build plan for SIGMA v1.0 through v3.0.

---

## 2. PROBLEM STATEMENT & RATIONALE

### 2.1 The Fragmentation Crisis

Global standards are among the most important intellectual infrastructure in human civilisation. They define how medicines are tested, how buildings stand, how aircraft fly, how money moves, how data is protected, how food is grown, how children are protected in emergencies, how refugees are treated, and how nations cooperate on climate change.

Yet this infrastructure is **profoundly fragmented**:

- **ISO** alone has 25,703+ published standards and charges USD 120–400 per document
- **IEC** has 12,000+ electrotechnical standards, similarly paywalled
- **ITU** has thousands of telecommunications recommendations, partially free
- **WHO** has hundreds of guidelines, largely free but scattered across topic pages
- **UN Treaty Collection** has 560+ multilateral treaties, free but poorly structured
- **ILO NORMLEX** has 190 Conventions, navigable only through their own interface
- **FATF** has 40 Recommendations plus thousands of country assessments
- **Codex Alimentarius** has thousands of food safety standards in 8 separate databases
- National standards bodies add another 200,000+ national standards globally

No single searchable, filterable, cross-referenced index exists that covers even a fraction of this landscape. Even the WTO's TBT Information Management System — the closest thing to a registry — only covers notifications submitted under the Technical Barriers to Trade Agreement.

### 2.2 The Access Inequality Problem

The entities most harmed by this fragmentation are the ones with fewest resources: NGOs working in humanitarian settings, government agencies in low-income countries, small businesses trying to export, researchers at underfunded institutions, and citizens trying to understand their rights. A Bangladeshi health worker trying to find the relevant WHO standard, a refugee protection officer checking the applicable UNHCR guidelines, or a water engineer in a camp setting needing the Sphere WASH standard should not need to know which organisation to look in, in which database, using which search syntax.

### 2.3 Why Now

Several developments make this project feasible for the first time:

- **ISO Open Data** has made metadata for all 25,703+ standards freely downloadable in CSV/JSON/Parquet format — no registration required
- **Wikidata** now contains structured data on thousands of standards bodies, queryable via free SPARQL endpoint
- **GitHub** provides free hosting, version control, and collaborative editing for structured data of this size
- **GitHub Pages** provides free static website hosting
- **Google Sheets** handles datasets up to 10 million cells for free, with a free API
- **Wikipedia's List of Technical Standard Organizations** provides a free, regularly maintained starting list
- **UN Treaty Collection**, **OHCHR**, **ILO NORMLEX**, **WHO Institutional Repository**, **ITU Publications**, and dozens of other UN agency databases are freely accessible

The tools, the data seeds, and the global need all align. What is missing is a coordinated research and curation effort — which this plan provides.

---

## 3. VISION, MISSION & GUIDING PRINCIPLES

### 3.1 Vision Statement

> *A world in which any person, in any country, in any sector, can instantly find, verify, and understand any global standard that affects their work or life — for free, in their language, in the format they need.*

### 3.2 Mission Statement

> *To build, maintain, and freely publish the world's most complete, accurate, and usable unified index of global standards, standards bodies, frameworks, treaties, and guidelines — covering every domain of human society, in a machine-readable and human-navigable format, requiring no subscription or payment to access.*

### 3.3 Guiding Principles

| # | Principle | What It Means in Practice |
|---|-----------|--------------------------|
| 1 | **Free Forever** | No paywall. No credit card. No registration. No subscription. Ever. |
| 2 | **Completeness over Perfection** | Include everything with a credible claim to global standing, then verify iteratively. An incomplete entry is better than no entry. |
| 3 | **Source Truth over Opinion** | Every entry cites its primary authoritative source. We describe standards; we do not evaluate them. |
| 4 | **Open by Default** | CC BY 4.0 license. All data on GitHub. All formats available for download. |
| 5 | **Machine-readable First** | CSV, JSON, Parquet are the primary outputs. Excel and web portal are derived views. |
| 6 | **Community Maintained** | No single point of failure. Anyone can contribute a correction or addition via GitHub pull request. |
| 7 | **Layer Neutral** | International, regional, and national standards are all equally valid. We do not privilege any governance level. |
| 8 | **Politically Neutral** | We describe what a standard says and who issued it. We do not take positions on contested standards, disputed territories, or political classifications. |
| 9 | **Continuously Updated** | Standards change. A standard marked Active today may be Withdrawn tomorrow. Automated checks and community reports keep the index current. |
| 10 | **Domain Agnostic** | No domain is too obscure, too niche, or too political for inclusion. Sports, arts, space, military, esoteric trade — all are in scope. |

---

## 4. SCOPE — THE FULL UNIVERSE OF HUMAN STANDARDS

This index covers **every formal global standard** that meets the following inclusion criteria:

### 4.1 Inclusion Criteria

A standard is included if it meets **all three** of the following:

1. **Formal issuance** — Published by an identifiable standards body, international organisation, intergovernmental body, recognised professional association, or national government agency acting in a standardisation capacity
2. **Cross-jurisdictional reach** — Intended to apply across at least two countries, or formally adopted/referenced by international bodies, or forms the basis of national legislation in multiple jurisdictions
3. **Referenceability** — Has a stable, citable identifier (standard number, convention number, resolution number, treaty name, etc.) and a verifiable primary source URL

### 4.2 What Is Explicitly Included

- All **ISO standards** (25,703+ published documents across 250+ Technical Committees)
- All **IEC standards** (12,000+ electrotechnical standards)
- All **ITU Recommendations** (ITU-T, ITU-R, ITU-D — thousands of documents)
- All **UN Treaties and Conventions** (560+ multilateral treaties in UN Treaty Collection)
- All **ILO Conventions and Recommendations** (190 Conventions, 206 Recommendations)
- All **WHO Guidelines, Frameworks, Classifications** (ICD-11, ICF, EML, IHR, 100s of guidelines)
- All **UN Specialised Agency standards** (ICAO SARPs, IMO Conventions, IAEA Safety Standards, FAO/WHO Codex, WIPO treaties, WMO Technical Regulations, UNESCO Conventions, UPU Convention)
- All **Financial stability standards** (BCBS Basel Accords, IOSCO Principles, IAIS ICPs, FSB Key Standards, FATF 40 Recommendations, IFRS/IAS, ISSB, ISAs)
- All **Human rights instruments** (UDHR, ICCPR, ICESCR, CEDAW, CRC, CRPD, CAT, CMW, CERD, all Optional Protocols)
- All **Humanitarian standards** (Sphere, CHS, INEE, IASC Guidelines, UNHCR Policies)
- All **Environmental treaties** (Paris Agreement, CBD, Ramsar, CITES, Stockholm, Basel, Rotterdam, Minamata, Montreal Protocol, UNCLOS)
- All **Major regional standards** (EN/CEN/CENELEC/ETSI for Europe; ASEAN standards; AU/ARSO standards; Arab/AIDMO standards)
- All **NSB national standards** where the NSB is an ISO member (175 national bodies, representing 175 national standard systems)
- All **Major industry/professional standards** (IEEE, IETF RFCs, W3C Recommendations, ASTM, ASME, API, NFPA, SAE, ASHRAE)
- All **Data and digital standards** (NIST frameworks, GDPR, ISO/IEC 27001 family, ISO/IEC 42001, NIST AI RMF, IETF RFCs for core internet protocols)
- All **Development and aid standards** (IATI Standard, OECD DAC Criteria, World Bank ESF, UN Evaluation Norms)
- All **Sports governance standards** (IOC, FIFA, World Athletics, WADA anti-doping code)
- All **Cultural heritage standards** (UNESCO World Heritage, ICCROM guidelines, ICOM standards)
- All **Defence and military standards** (NATO STANAGs, US MIL-STD series where declassified, SIPRI frameworks)
- All **Space and aerospace standards** (CCSDS, ECSS, FAA/EASA technical standards, ISO TC 20)
- All **Agricultural and food standards** (Codex Alimentarius, ISPM phytosanitary measures, WOAH animal health codes, GlobalGAP)
- All **Construction and built environment standards** (ISO TC 59, ICC codes, NFPA, ASHRAE)
- All **Occupational health and safety standards** (ILO OSH Conventions, ISO 45001, OSHA standards)
- All **Legal and commercial law standards** (UNCITRAL Model Laws, CISG, UNIDROIT Principles, ICC Incoterms)

### 4.3 What Is Explicitly Out of Scope

- **Proprietary company-specific standards** that have not been adopted as industry or national standards (e.g., internal company processes, brand specifications)
- **Draft standards not yet formally adopted** — these may be noted as "Under Development" but are not full entries
- **Purely local/municipal standards** with no cross-jurisdictional reference
- **Classified or restricted-access military technical specifications** where the full text is not publicly available
- **Academic style guides and disciplinary conventions** (APA, MLA, Chicago) — these are not formal standards in the sense of the index

---

## 5. MASTER DOMAIN TAXONOMY — ALL 40 DOMAINS

The index is organised into **40 primary domains** across **6 meta-layers**. Each domain has defined sub-domains that further classify entries.

---

### META-LAYER 1: LIFE SCIENCES & HEALTH (Domains 1–6)

**Domain 1 — Health & Medical**
Core clinical care, public health, epidemiology, medical products, and health system standards. This is the most populated domain in terms of formally adopted global standards. Key sub-domains include: public health and disease surveillance; clinical guidelines and protocols; pharmaceuticals and good clinical practice; medical devices and in vitro diagnostics; health informatics and interoperability; clinical terminologies and classifications; laboratory standards; patient safety; blood and transplantation; traditional and complementary medicine; global health security; antimicrobial resistance; mental health; non-communicable diseases; and immunisation.

**Domain 2 — Food Safety & Agriculture**
Standards governing what humans eat and how food is produced. Encompasses: food safety management systems; Codex Alimentarius standards (commodity standards, MRLs, codes of practice, guidelines); agricultural production standards; pesticide residue limits; food labelling; organic production; GMO/biotechnology standards; aquaculture; food fraud and authenticity; and nutritional standards.

**Domain 3 — Animal Health & Veterinary**
Standards for animal disease control, food-of-animal-origin safety, and animal welfare. Covers: WOAH Terrestrial and Aquatic Animal Health Codes; zoonotic disease standards; veterinary drug residues; animal welfare during transport and slaughter; aquatic animal diseases; and wildlife disease monitoring.

**Domain 4 — Plant Health & Phytosanitary**
International standards preventing the spread of plant pests and diseases through trade. Covers all ISPMs (International Standards for Phytosanitary Measures) under IPPC; pest risk analysis; phytosanitary treatments; wood packaging standards; and plant genetic resources.

**Domain 5 — Occupational Health & Safety**
Standards for worker health and safety. Covers: ILO OSH Conventions (C155, C161, C170, C176, C184, C187); ISO 45001 management systems; OSHA standards (US and adopted internationally); construction safety; mining safety; chemical safety at work; radiation protection for workers; ergonomics; and psychosocial risk standards.

**Domain 6 — Pharmaceuticals & Medicines**
Specific standards for pharmaceutical development, manufacturing, and regulation. Covers: ICH Q, S, E, M guidelines; GMP standards; pharmacopoeias (US, European, International, Japanese); drug registration dossier requirements; pharmacovigilance; and biosimilars.

---

### META-LAYER 2: PHYSICAL SCIENCES & ENGINEERING (Domains 7–14)

**Domain 7 — Measurement & Metrology**
The foundational science of measurement that underpins all other standards. Covers: SI (International System of Units) and the Metre Convention; BIPM publications and the CIPM MRA; OIML International Recommendations; national measurement institute standards; calibration and traceability; legal metrology; and the ILAC MRA for laboratory accreditation.

**Domain 8 — Manufacturing & Industry**
Standards for industrial production processes, machinery, and manufactured products across all sectors. Covers: industrial automation (IEC 61511, IEC 62061, ISO 10218); process safety; pressure equipment (ASME BPVC); welding (ISO TC 44, IIW); materials testing (ASTM, ISO); machine safety; industrial gases; textile standards; leather standards; plastics; rubber; ceramics; and packaging.

**Domain 9 — Electrical & Electronics**
IEC-domain standards for electrical and electronic devices, safety, and performance. Covers: IEC 60364 (electrical installations); IEC 60335 (household appliances); IEC 60601 (medical electrical equipment); semiconductor standards (IEC TC 47); electromagnetic compatibility (IEC 61000); power electronics; batteries; and lighting standards (CIE, IEC TC 34).

**Domain 10 — Construction & Built Environment**
Standards for buildings, infrastructure, and the constructed environment. Covers: ISO TC 59 building standards; ISO 19650 (BIM/information management); ISO 21930 (environmental product declarations); ISO 37120 (sustainable cities); ISO 37122 (smart cities); fire safety (NFPA codes, ISO TC 21); structural engineering codes; building materials (ISO, ASTM, EN); accessibility (ISO/TR 22411); and green building standards (BREEAM, LEED reference standards, ISO TC 163).

**Domain 11 — Chemical & Process Industries**
Standards for chemical manufacturing, process safety, and chemical substances management. Covers: GHS (Globally Harmonised System for Classification and Labelling of Chemicals); REACH regulation (EU, internationally referenced); API standards for oil and gas; ISO TC 60 (gears), TC 67 (oil and gas); Responsible Care® Global Charter; and hazardous substance standards.

**Domain 12 — Materials Science & Testing**
Cross-cutting standards for materials characterisation and testing regardless of end-use. Covers: ASTM materials standards (12,000+); ISO materials standards (ISO TC 61 plastics, TC 79 aluminium, TC 17 steel); EN materials norms; corrosion standards; non-destructive testing; and reference materials (BIPM/IRMM).

**Domain 13 — Aerospace & Aviation**
Standards governing the design, manufacture, certification, operation, and safety of aircraft and spacecraft. Covers: ICAO Annexes (1–19), SARPs, PANS, and DOCs; EASA certification specifications; FAA TSOs; SAE AS9100 (aviation QMS); DO-178C (airborne software); DO-254 (hardware); RTCA standards; and military aviation standards (MIL-STD-461 for EMC, etc.).

**Domain 14 — Space & Satellite**
Standards for space systems, spacecraft, and satellite operations. Covers: CCSDS (Consultative Committee for Space Data Systems) standards for space data communications; ECSS (European Cooperation for Space Standardisation); ISO TC 20 SC 14 (space systems); ITU Radio Regulations for satellite orbital slots and frequency allocation; COPUOS guidelines for space debris mitigation; and emerging commercial space standards.

---

### META-LAYER 3: SOCIETY, GOVERNANCE & LAW (Domains 15–22)

**Domain 15 — Human Rights**
The full architecture of international human rights law and standards. Covers: the International Bill of Human Rights (UDHR, ICCPR, ICESCR); the nine core UN human rights treaties (CEDAW, CRC, CRPD, CAT, CMW, CERD, CED, and their Optional Protocols); General Comments and Recommendations of treaty bodies; UN Human Rights Council resolutions; Special Procedure mandates and reports; the UNGPs on Business and Human Rights; and regional human rights instruments (ECHR, ACHPR, ACHR, Arab Charter).

**Domain 16 — Labour & Employment**
ILO and related standards governing work, employment, and labour relations. Covers: all 190 ILO Conventions and 206 Recommendations; the ILO 1998 Declaration on Fundamental Principles and Rights at Work; the MLC 2006 (Maritime Labour Convention); OSH standards (covered also in Domain 5); social protection floors; employment policy standards; labour administration and inspection standards; and OECD Guidelines for MNEs on employment.

**Domain 17 — Humanitarian & Emergency Response**
Standards governing humanitarian action, emergency response, and protection in crises. Covers: Sphere Handbook (WASH, food, shelter, health minimum standards); Core Humanitarian Standard (CHS) — 9 commitments; INEE Minimum Standards for Education in Emergencies; IASC Cluster System and guidelines; UNHCR policies and guidelines (GBV, RSD, AGD, Solutions); ICRC Customary IHL database; Code of Conduct for the IRCR and NGOs; HAP Standard (now CHS); Emergency Medical Teams (WHO EMT) standards; Mass Casualty Management; and Camp Coordination and Camp Management (CCCM) standards.

**Domain 18 — Legal & Commercial Law**
International legal standards, model laws, and commercial law frameworks. Covers: UNCITRAL Model Laws (international arbitration, electronic commerce, insolvency, procurement); CISG (UN Convention on Contracts for the International Sale of Goods); UNIDROIT Principles of International Commercial Contracts; ICC Incoterms® 2020; ICC Uniform Customs and Practice for Documentary Credits (UCP 600); New York Convention on arbitral awards; Rome Statute (ICC); and OECD legal instruments.

**Domain 19 — Governance, Transparency & Anti-Corruption**
Standards for good governance, institutional accountability, and anti-corruption. Covers: UNCAC (UN Convention Against Corruption); OECD Anti-Bribery Convention; ISO 37001 (anti-bribery management systems); ISO 37301 (compliance management); ISO 37000 (governance of organisations); EITI Standard (Extractive Industries Transparency Initiative); Open Government Partnership commitments; and GRECO standards.

**Domain 20 — Education & Research**
Standards for educational systems, institutions, qualifications, and research practices. Covers: UNESCO Conventions on recognition of qualifications (Lisbon/Tokyo/Addis Conventions); ISO 21001 (educational organisations); ISCED (International Standard Classification of Education); ICH E6(R3) GCP for research; Declaration of Helsinki (medical research ethics); FAIR Data Principles; ORCID, DOI, ISBN, ISSN as research identifier standards; UNESCO Science Report frameworks; and OECD Programme for International Student Assessment (PISA) methodology.

**Domain 21 — Culture, Heritage & Arts**
Standards protecting and promoting cultural heritage, arts, and intangible heritage. Covers: UNESCO World Heritage Convention (1972); UNESCO Convention for the Safeguarding of the Intangible Cultural Heritage (2003); UNESCO Convention on the Protection and Promotion of the Diversity of Cultural Expressions (2005); 1954 Hague Convention for the Protection of Cultural Property in Armed Conflict; ICOM Code of Ethics for Museums; ICCROM guidelines for conservation; and ICOMOS Charters (Venice Charter, Burra Charter, Nara Document on Authenticity).

**Domain 22 — Sports & Recreation**
International standards for sports governance, anti-doping, and physical education. Covers: World Anti-Doping Agency (WADA) Code — the binding international framework for anti-doping; International Convention Against Doping in Sport (UNESCO); IOC Olympic Charter; FIFA Regulations (transfer, stadium, match operations); World Athletics Technical Rules; FINA (now World Aquatics) Standards; ISO TC 83 (sports and recreational equipment); and international arbitration through CAS (Court of Arbitration for Sport).

---

### META-LAYER 4: ECONOMY & TRADE (Domains 23–27)

**Domain 23 — Finance, Banking & Accounting**
International standards governing the financial system. Covers: Basel I/II/III/IV (BCBS capital and liquidity standards); IOSCO Principles of Securities Regulation; IAIS Insurance Core Principles; FATF 40 Recommendations on AML/CFT; FSB Key Standards; IFRS (all 17 standards); IAS (all active IAS standards); ISSB S1/S2; ISAs (international auditing standards); IESBA Code of Ethics; CPMI Principles for Financial Market Infrastructures; IADI Core Principles for deposit insurance; IMF Special Data Dissemination Standards (SDDS, e-GDDS); and ISO 20022 (financial messaging).

**Domain 24 — Trade & Customs**
Standards facilitating and governing international trade flows. Covers: WTO TBT Agreement and its Code of Good Practice; WTO SPS Agreement; WTO Trade Facilitation Agreement; WCO Harmonized System (HS) — the 6-digit commodity classification used by 212 countries; WCO SAFE Framework of Standards; AEO (Authorised Economic Operator) standards; UN/CEFACT trade facilitation standards; and INCOTERMS (ICC) terms of sale.

**Domain 25 — Supply Chain & Logistics**
Standards governing the identification, tracking, and management of goods through supply chains. Covers: GS1 standards (GTIN, GLN, GS1-128, EPC/RFID, EPCIS, EDI standards EANCOM and XML); ISO 28000 (supply chain security management); ISO 31000 (risk management); pharmaceutical supply chain standards (GDP, GDP serialisation); food chain traceability standards (ISO 22005); and responsible sourcing standards (OECD DDG for minerals, RBA Code of Conduct for electronics).

**Domain 26 — Sustainability, ESG & Circular Economy**
Standards for environmental, social, and governance reporting and performance. Covers: GRI Universal Standards and Sector Standards; SASB Standards (77 industries); IFRS S1 and S2 (ISSB); EU ESRS (12 standards under CSRD); EU Taxonomy Regulation; TCFD Recommendations; TNFD Framework; GHG Protocol (Corporate Standard, Product Standard, Scope 3 Standard); SBTi Corporate Net-Zero Standard; ISO 14001 (EMS); ISO 14040/14044 (LCA); ISO 14064 (GHG quantification); ISO 26000 (social responsibility); SA8000 (social accountability); and Fairtrade Standards.

**Domain 27 — Taxation & Public Finance**
International frameworks governing taxation, fiscal transparency, and public financial management. Covers: OECD BEPS Framework (15 actions, Pillar One and Two); OECD CRS (Common Reporting Standard for automatic exchange of tax information); OECD/G20 Inclusive Framework (145+ countries); FATF standards on tax crime as a predicate offence; IMF Government Finance Statistics Manual; and the Addis Ababa Action Agenda on financing for development.

---

### META-LAYER 5: TECHNOLOGY & INFRASTRUCTURE (Domains 28–35)

**Domain 28 — Information & Communications Technology (ICT)**
The broadest technology domain, covering all aspects of digital infrastructure, software, and communications. Covers: ISO/IEC JTC 1 output (1,000+ IT standards); ITU-T Recommendations; IEEE 802 standards (Wi-Fi, Ethernet, Bluetooth); IETF RFCs (8,000+ internet protocol standards, all freely available); W3C Recommendations (HTML5, CSS, XML, WebAuthn, WebAssembly, WCAG); 3GPP standards (4G LTE, 5G NR); ETSI standards; and ECMA standards (ECMAScript/JavaScript, C#).

**Domain 29 — Cybersecurity & Data Privacy**
Standards for protecting information systems and personal data. Covers: ISO/IEC 27001 family (28 standards in the 27000 series); ISO/IEC 27701 (privacy information management); NIST SP 800 series (180+ publications); NIST Cybersecurity Framework (CSF 2.0); NIST Privacy Framework; PCI DSS v4.0 (payment card security); SOC 2 criteria (AICPA); GDPR (EU, with global extraterritorial effect); CCPA/CPRA (California, with global influence); MITRE ATT&CK Framework; CIS Controls v8; and ENISA standards.

**Domain 30 — Artificial Intelligence & Emerging Technologies**
The fastest-growing area of global standardisation. Covers: ISO/IEC 42001:2023 (AI Management Systems — world's first AI management standard); ISO/IEC 22989 (AI concepts and terminology); ISO/IEC 23894 (AI risk management); ISO/IEC 42005 (AI impact assessment, under development); NIST AI RMF 1.0; OECD AI Principles (adopted by 42+ governments); UNESCO Recommendation on the Ethics of AI; EU AI Act (2024, with global regulatory influence); IEEE Ethically Aligned Design; ISO/IEC JTC 3 (Quantum Technologies — new 2024 committee for quantum computing, simulation, sensing, and communications); and W3C Decentralised Identifier standards.

**Domain 31 — Energy & Utilities**
Standards governing energy production, distribution, and management. Covers: IAEA Safety Standards (GSR, SSR, GSG series — nuclear safety, security, safeguards); IEC TC 8 (energy systems), TC 57 (power systems management), TC 82 (solar photovoltaic); ISO 50001 (energy management); ISO TC 197 (hydrogen technologies); ISO TC 244 (domestic gas appliances); CIGRE technical brochures (large electric systems); IEEE 2030 series (smart grid); NPT (nuclear non-proliferation treaty); Euratom safeguards; and IRENA guidelines.

**Domain 32 — Transport (Land, Sea, Air, Rail)**
The full multi-modal transport standards landscape. Covers: ICAO Annexes 1–19 to the Chicago Convention; IMO SOLAS, MARPOL, STCW, ISM Code, MLC 2006, ISPS Code, Ballast Water Convention; UNECE road vehicle regulations (WP.29 — 150+ regulations); UNECE ADR (road transport of dangerous goods), RID (rail), ADN (inland waterways); UIC International Railway Standards; ISO TC 22 (road vehicles, 150+ standards); IMO polar code; OTIF/COTIF (rail transport law); and aviation dangerous goods (IATA DGR).

**Domain 33 — Water, Sanitation & Hygiene (WASH)**
Standards for drinking water quality, sanitation systems, and hygiene practice. Covers: WHO Guidelines for Drinking-Water Quality (4th edition); WHO Sanitation Safety Planning Manual; ISO 24510-24512 (drinking water and wastewater services); Sphere WASH minimum standards; JMP definitions (WHO/UNICEF Joint Monitoring Programme) for safely managed water and sanitation; UNHCR WASH standards for refugee settings; Water Point Data Exchange (WPDx) open standard; and IWRA water governance frameworks.

**Domain 34 — Built Environment & Urban Systems**
Smart city, urban planning, and infrastructure management standards beyond pure construction. Covers: ISO 37100 series (sustainable cities and communities: ISO 37101, 37102, 37104, 37105, 37106, 37120, 37122, 37123); IEC SyC Smart Cities; IEEE Smart Cities Initiative; ITU-T Y.4000 series (IoT and smart city); UN-Habitat Urban Land Policies; and the New Urban Agenda (Quito Declaration, 2016).

**Domain 35 — Defence & Security (Declassified)**
Publicly available international standards and frameworks for defence and security. Covers: NATO STANAGs (Standardisation Agreements — those in public domain); US MIL-STD series where declassified and internationally referenced (MIL-STD-461 for EMC, MIL-STD-810 for environmental testing); UN Arms Trade Treaty; Wassenaar Arrangement control lists; Chemical Weapons Convention (CWC) and OPCW verification standards; Biological Weapons Convention (BWC); Ottawa Treaty (Anti-Personnel Mines); Convention on Cluster Munitions; CTBT International Monitoring System standards; UN PKO Standards of Conduct; and Interpol standards for police cooperation.

---

### META-LAYER 6: ENVIRONMENT & NATURAL SYSTEMS (Domains 36–40)

**Domain 36 — Environment & Climate**
The full landscape of environmental management and climate-related standards. Covers: UNFCCC and Paris Agreement (NDCs, Global Stocktake, Article 6 carbon markets); Kyoto Protocol mechanisms; CBD Kunming-Montreal Global Biodiversity Framework (30×30 target); Montreal Protocol and Kigali Amendment; Stockholm Convention (POPs); Basel Convention (hazardous waste); Rotterdam Convention (prior informed consent for chemicals); Minamata Convention (mercury); UNCLOS (Law of the Sea — includes marine environment protection); ISO 14001 family (14 EMS-related standards); ISO 14064 (GHG quantification); GHG Protocol; and IPCC methodology guidelines for national GHG inventories.

**Domain 37 — Marine & Ocean**
Standards for ocean governance, marine safety, and marine resource management. Covers: UNCLOS (full treaty); IMO conventions not covered under Transport; MARPOL annexes I–VI; London Protocol (marine dumping); International Whaling Convention; CCAMLR (Antarctic marine living resources); MSC Fisheries Standard; FAO Code of Conduct for Responsible Fisheries and ISMs; regional seas conventions (Barcelona, Cartagena, Nairobi, etc.); and OSPAR Convention (Northeast Atlantic).

**Domain 38 — Biodiversity & Conservation**
Standards for biodiversity measurement, conservation practice, and natural capital accounting. Covers: CBD and Nagoya Protocol (access and benefit sharing); CITES Appendices I, II, III; Ramsar Convention on Wetlands; World Heritage Convention (natural heritage criteria); IUCN Red List Categories and Criteria (the global standard for species threat assessment); IUCN Green List Standards for protected area management; IPBES Conceptual Framework and methods; and TNFD nature-related risk framework.

**Domain 39 — Disaster Risk & Humanitarian Preparedness**
Standards for systemic disaster risk reduction and preparedness. Covers: Sendai Framework for Disaster Risk Reduction 2015–2030 (7 global targets, 38 indicators); UNDRR Terminology on Disaster Risk Reduction; ISO 22301 (business continuity management); ISO 22313 (BCMS guidance); ISO 22316 (organisational resilience); Hyogo Framework legacy guidance; regional DRR frameworks (AADMER for ASEAN; AU Disaster Risk Reduction Strategy); and WHO Health Emergency and Disaster Risk Management Framework.

**Domain 40 — Extractive Industries & Natural Resources**
Standards governing the responsible extraction and management of natural resources. Covers: EITI (Extractive Industries Transparency Initiative) Standard — the global transparency standard for oil, gas, and mining; ICMM (International Council on Mining and Metals) principles and position statements; ISO TC 82 (mining standards); API standards for petroleum (400+ standards); IOGP (International Association of Oil and Gas Producers) guidelines; FSC Forest Management Standard and CoC Standard; RSPO Principles and Criteria (sustainable palm oil); and IRMA (Initiative for Responsible Mining Assurance) standard.

---

## 6. SCALE & QUANTITATIVE SCOPE

Understanding the scale of this project is essential for realistic planning.

| Source | Estimated Entries | Freely Available | Primary Format |
|--------|------------------|-----------------|----------------|
| ISO standards (all TCs) | 25,703 | Metadata only (full text paid) | CSV/JSON via ISO Open Data |
| IEC standards | 12,000+ | Metadata only | IEC website (no bulk download) |
| ITU Recommendations (T, R, D) | 5,000+ | Free to download (no registration) | PDF per document; no bulk CSV |
| ILO Conventions & Recommendations | 396 | Full text free | NORMLEX database (HTML) |
| UN Treaties (UNTC) | 560+ multilateral | Full text free | UNTC online (no bulk download) |
| OHCHR core instruments | 9 core + protocols | Full text free | OHCHR website |
| WHO guidelines and classifications | 500+ | Largely free | WHO IRIS repository |
| ICAO SARPs (19 Annexes) | 44,000 provisions | Limited free access | ICAO Doc Store (subscription) |
| IMO Conventions | 50+ | Summary free; text partially paywalled | IMO website |
| Codex Alimentarius | 3,000+ texts | Fully free | CODEXALIMENTARIUS.NET |
| IETF RFCs | 9,000+ | Fully free | RFC Editor (TXT/HTML/PDF) |
| W3C Recommendations | 400+ | Fully free | W3C.org |
| IEEE standards | 1,300+ active | ~200 free; rest paywalled | IEEE Xplore |
| ASTM standards | 12,500+ | Paywalled | ASTM website |
| NIST publications (SP 800 etc.) | 500+ | Fully free | NIST.gov |
| GRI Standards | 40+ | Fully free | GRI website |
| National standards bodies × 175 | 200,000+ combined | Varies | Each NSB website |
| Wikidata (standards body entities) | 10,000+ entities | Fully free | SPARQL endpoint |
| **Realistic SIGMA scope (v1.0)** | **5,000–8,000** | **Metadata + URLs** | **CSV/JSON/XLSX** |
| **Realistic SIGMA scope (v2.0)** | **15,000–25,000** | **Metadata + URLs** | **CSV/JSON/XLSX** |
| **Realistic SIGMA scope (v3.0)** | **50,000+** | **Metadata + URLs** | **CSV/JSON/XLSX/Parquet** |

> **Critical Insight:** The goal of SIGMA is not to reproduce the full text of standards (which would violate copyright for most ISO/IEC/ASTM content). The goal is to create a **comprehensive metadata index** — structured information *about* each standard (ID, name, issuer, domain, year, status, URL, mandate type, etc.) so that any user can instantly find which standard they need and where to access it.

---

## 7. FREE DATA SOURCES — DEEP RESEARCH FINDINGS

This section documents every freely accessible, no-registration-required primary data source identified through web research. These are the raw materials for building SIGMA.

### 7.1 Tier 1 — Bulk Machine-Readable Free Datasets (Highest Priority)

These sources provide structured, downloadable data requiring zero registration or payment.

---

**7.1.1 ISO Open Data**
- **URL:** `https://www.iso.org/open-data.html`
- **What it provides:** Machine-readable metadata for all 25,703+ ISO standards, all 800+ Technical Committees and Subcommittees, and the complete International Classification for Standards (ICS) taxonomy
- **Formats:** CSV, JSONLines, Parquet
- **License:** CC BY (attribution required)
- **Update frequency:** Regular (ISO states "up-to-date")
- **Key fields available:** Standard number, title, status (Published/Withdrawn/Under Development), technical committee, year published, ICS codes, DOI, edition number
- **How to access:** Direct download links on the Open Data page — no account required
- **Strategic value:** This single source seeds the entire ISO portion of the index (25,703 entries) automatically. It is the single most important free data source for this project.

---

**7.1.2 Wikidata SPARQL Endpoint**
- **URL:** `https://query.wikidata.org/`
- **What it provides:** Structured linked data on tens of thousands of standards bodies, standards, and frameworks as Wikidata entities (Q items), queryable in real-time
- **Format:** JSON, CSV, XML, TSV (selectable at query time)
- **License:** CC0 (public domain)
- **Rate limits:** 60-second query timeout; no daily cap for well-optimised queries
- **Key SPARQL properties for standards bodies:**
  - `wdt:P31` — instance of (standards organization = Q176799)
  - `wdt:P571` — inception date
  - `wdt:P856` — official website
  - `wdt:P18` — image
  - `wdt:P131` — located in administrative territorial entity
  - `wdt:P749` — parent organisation
- **Key SPARQL properties for standards documents:**
  - `wdt:P31 wd:Q317623` — instance of standard
  - `wdt:P123` — publisher
  - `wdt:P577` — publication date
  - `wdt:P407` — language of work
- **Strategic value:** Provides structured data on thousands of standards bodies and their relationships that is not available from any other free bulk source. Requires writing SPARQL queries (see Annex C for ready-to-use queries).

---

**7.1.3 IETF RFC Editor**
- **URL:** `https://www.rfc-editor.org/`
- **What it provides:** Full text and metadata for all 9,000+ IETF Request for Comments (RFCs) — the internet protocol standards
- **Formats:** TXT, HTML, PDF; bulk index in JSON at `https://www.rfc-editor.org/rfc/index.json`
- **License:** IETF Trust (freely redistributable with attribution)
- **Update frequency:** Continuous (new RFCs published monthly)
- **Key fields:** RFC number, title, authors, status (Standard/BCP/Informational/Experimental/Historic), date, abstract, DOI, related RFCs
- **Strategic value:** Complete, structured, bulk-downloadable dataset of all internet standards — a unique and complete free source.

---

**7.1.4 UN Treaty Collection**
- **URL:** `https://treaties.un.org/`
- **What it provides:** Full text and status data for all 560+ multilateral treaties deposited with the UN Secretary-General; also tracks ratification status by all 193 member states
- **Formats:** HTML search interface; no bulk download but structured HTML parseable by web scraper
- **License:** UN copyright (free for research and educational use)
- **Key fields:** Treaty name, UNTS number, date opened for signature, date entered into force, number of parties, depositary
- **Strategic value:** The authoritative source for all UN-framework treaties (human rights, environment, trade, disarmament). Must be scraped systematically.

---

**7.1.5 ILO NORMLEX**
- **URL:** `https://normlex.ilo.org/`
- **What it provides:** Full text, ratification status, and supervisory body decisions for all 190 ILO Conventions and 206 Recommendations
- **Formats:** HTML interface; bulk data available via ILO Data API (free, no key required for basic queries)
- **ILO Data API:** `https://www.ilo.org/ilostat-files/Documents/ILOSTAT_API_guidelines.pdf`
- **License:** ILO copyright (free for research)
- **Strategic value:** Complete, authoritative source for international labour standards with ratification tracking.

---

**7.1.6 WHO Institutional Repository (IRIS)**
- **URL:** `https://iris.who.int/`
- **What it provides:** Full text and metadata for WHO publications including guidelines, technical reports, normative documents, and manuals. OAI-PMH endpoint available for bulk metadata harvesting.
- **OAI-PMH endpoint:** `https://iris.who.int/oai/request`
- **Formats:** Dublin Core XML via OAI-PMH; full text PDF free
- **License:** WHO copyright (free for research and educational use)
- **Strategic value:** Enables systematic harvesting of WHO guideline metadata without page-by-page scraping.

---

**7.1.7 Wikipedia — List of Technical Standard Organizations**
- **URL:** `https://en.wikipedia.org/wiki/List_of_technical_standard_organizations`
- **What it provides:** Structured list of international, regional, and national standards bodies with descriptions, organized by sector and geography. Also links to national standards body pages per country.
- **Format:** HTML (parseable); also available via Wikipedia API in JSON
- **Wikipedia API example:** `https://en.wikipedia.org/api/rest_v1/page/summary/List_of_technical_standard_organizations`
- **License:** CC BY-SA 3.0
- **Strategic value:** Provides a maintained, human-vetted list of standards bodies that can be used to seed the organisations layer of SIGMA. Updated continuously by Wikipedia editors.

---

**7.1.8 WTO TBT Code — List of Standardizing Bodies**
- **URL:** `https://tbtcode.iso.org/list-of-standardizing-bodies.html`
- **What it provides:** Official list of standardizing bodies that have accepted the WTO TBT Code of Good Practice — approximately 200+ bodies, with country, type, year of acceptance, and contact details
- **Format:** HTML table (parseable)
- **License:** ISO/WTO (free for research)
- **Strategic value:** Provides a formally validated list of standards bodies with proven cross-border relevance — a quality filter not available elsewhere.

---

**7.1.9 NIST — Standards Organizations Offering Free Access**
- **URL:** `https://www.nist.gov/standardsgov/standards-organizations-offer-free-access-their-standards`
- **What it provides:** Curated list of standards organizations offering free or partially free access to their standards documents
- **Format:** HTML list
- **Strategic value:** Identifies which standards bodies have freely accessible full texts — prioritising these for content linking in SIGMA.

---

**7.1.10 Codex Alimentarius**
- **URL:** `https://www.fao.org/fao-who-codexalimentarius/codex-texts`
- **What it provides:** Full text of all Codex standards, guidelines, codes of practice, and MRLs — freely accessible
- **Format:** HTML/PDF; structured list downloadable
- **License:** FAO/WHO copyright (free for research)
- **Strategic value:** Complete, free access to 3,000+ food safety standards — one of the most comprehensive free standards databases available.

---

### 7.2 Tier 2 — Domain-Specific Free Portals (Medium Priority)

These require page-by-page navigation but offer free access to full content.

| Portal | Domain | URL | Notes |
|--------|--------|-----|-------|
| OHCHR Human Rights Bodies | Human Rights | ohchr.org/treaties | All treaty texts, ratification tables, GCs free |
| FAO Legal Office | Agriculture/Environment | fao.org/faolex | FAOLEX database — 250,000+ legal texts |
| ITU Publications | ICT/Telecom | itu.int/pub | ITU-T recommendations free after register (no CC) |
| WOAH WAHIS | Animal Health | wahis.woah.org | Animal disease notification data free |
| IPPC Portal | Phytosanitary | ippc.int/en/core-activities/standards-setting | All ISPMs free PDF |
| IAEA Safety Standards | Nuclear | iaea.org/resources/safety-standards | All safety standards free PDF |
| GRI Standards | Sustainability | globalreporting.org/standards | All GRI standards free PDF |
| SASB Standards | ESG | sasb.org/standards | All 77 industry standards free |
| IFRS Foundation | Finance | ifrs.org/issued-standards | Consolidated IFRS free (requires free account) |
| OECD iLibrary | OECD Standards | oecd-ilibrary.org | Many OECD standards free; some paywalled |
| Basel Committee | Finance | bis.org/bcbs | All BCBS publications free |
| FSB | Finance | fsb.org | All FSB publications free |
| FATF | AML/CFT | fatf-gafi.org | All FATF Recommendations free |
| WTO Legal Texts | Trade | wto.org/english/docs_e/legal_e/legal_e.htm | All WTO agreements free |
| IETF Datatracker | Internet | datatracker.ietf.org | All RFCs and drafts free |
| W3C Standards | Web | w3.org/standards | All W3C Recommendations free |
| NIST Publications | Digital/Cyber | nvlpubs.nist.gov | All NIST SPs, FIPs, ITLBs free |
| Sphere Handbook | Humanitarian | spherestandards.org | Free PDF and online access |
| CHS Alliance | Humanitarian | corehumanitarianstandard.org | CHS free PDF |
| INEE Standards | Education/Emergency | inee.org/minimum-standards | Free download, no registration |
| UNHCR Operational Data | Refugees | unhcr.org/operational/operational-innovation | Many guidelines free |
| IATI Standard | Aid Transparency | iatistandard.org | Full standard free |
| GHG Protocol | Climate | ghgprotocol.org | All standards free PDF |
| SBTi Resources | Climate | sciencebasedtargets.org/resources | Free |
| CITES Appendices | Biodiversity | cites.org/eng/app | Full appendices free |
| CBD Texts | Biodiversity | cbd.int/convention/text | All CBD texts free |
| UNFCCC Texts | Climate | unfccc.int/process/the-convention | All treaty texts free |

---

### 7.3 Tier 3 — Paywalled but Strategically Important (Metadata Available Free)

These are important standards sources where the metadata is free but the full standard text requires purchase. For SIGMA, we capture metadata (title, number, issuer, year, status, URL) and note they are paywalled.

| Source | What's Paywalled | Free Workaround |
|--------|-----------------|----------------|
| ISO Standards (full text) | ~USD 120–400 per standard | ISO Open Data provides full metadata; ICS subject classification free |
| IEC Standards (full text) | ~EUR 200–350 per standard | IEC search free; metadata via IEC website |
| ASTM Standards | ~USD 40–100 per standard | ASTM subject search free; some free via NIST reference |
| ASME BPVC | ~USD 3,000+ for full set | ASME abstracts and scope free |
| ICAO SARPs | Full text subscription | ICAO summary and amendment lists free; States may publish adoptions |
| IEEE Standards (most) | ~USD 100–200 per standard | ~200 IEEE standards free via IEEE Xplore (marked "free") |
| SAE Standards | ~USD 50–150 per standard | SAE abstracts free; some open via SAE Mobilus |

---

## 8. FREE TOOLS STACK — ZERO COST, ZERO CREDIT CARD

Every tool in this stack is **completely free** and requires no credit card to create an account.

### 8.1 The Core Stack

```
COLLECTION LAYER
├── Web Browser (Chrome/Firefox) + browser automation
├── Python 3 (free, open source) for scripting
├── requests + BeautifulSoup (Python scraping libraries)
├── SPARQLWrapper (Python library for Wikidata)
└── wget / curl (command-line download tools)

STORAGE & CURATION LAYER
├── GitHub (free tier) — version control, hosting, issue tracking
│   └── github.com — free public repositories, unlimited collaborators
├── Google Sheets (free tier) — online editing, collaboration, API
│   └── Up to 10 million cells per spreadsheet; free Google account
├── Google Drive (free tier) — 15 GB free storage for files
├── CSV files — universal, no software required to read or write
└── Excel (.xlsx) — for non-technical users (LibreOffice free alternative)

DATABASE LAYER (OPTIONAL, PHASE 3+)
├── NocoDB — open source, free, Airtable-alternative
│   └── github.com/nocodb/nocodb — runs on free-tier cloud or local
├── Baserow — open source, MIT license, free cloud tier
│   └── baserow.io — free plan: unlimited rows, 2 GB storage
└── SQLite — file-based database, zero infrastructure, fully free

PUBLICATION LAYER
├── GitHub Pages — free static website hosting from GitHub repo
│   └── Supports custom domains; unlimited bandwidth for public repos
├── Markdown files — human-readable documentation, renders on GitHub
└── Observable (observablehq.com) — free interactive data notebooks

AUTOMATION LAYER
├── GitHub Actions — free CI/CD (2,000 minutes/month on free tier)
│   └── Use for: automated URL checking, weekly data refresh, lint checks
├── Google Apps Script — free automation within Google Workspace
│   └── Automate Google Sheets operations, fetch data from APIs
└── Zapier Free Tier — 100 tasks/month free (optional, limited use)

SEARCH & DISCOVERY (for users)
├── GitHub native search — full-text search of repository content
├── Google Sheets filter views — no-code filtering for non-technical users
└── Future: Pagefind (open source) or Lunr.js for static site search
```

### 8.2 Tool-by-Tool Setup Notes

**GitHub (github.com)**
Creating a GitHub account requires only an email address — no credit card, no phone verification required. A free account can create unlimited public repositories. The SIGMA project will live at a URL like `github.com/sigma-standards/sigma-index`. GitHub also provides 1 GB of file storage per repository (more with Git LFS for large files), and unlimited collaborators on public repos.

**Google Sheets**
A free Google account (Gmail) provides access to Google Sheets with up to 10 million cells per spreadsheet and 15 GB of Drive storage. The Sheets API is free for read/write operations up to 300 requests per minute per project. No billing account is required. Google Sheets will serve as the primary working database for data entry and curation phases (Phases 1–3), before migrating to a more structured format.

**NocoDB (Self-hosted or Cloud Free Tier)**
NocoDB is a fully open-source, MIT-licensed tool that transforms any relational database into a collaborative spreadsheet interface — functionally equivalent to Airtable but completely free. It can be deployed for free on Render.com (free tier), Railway.app (free starter), or locally. No credit card required for the free tiers. NocoDB provides a REST API, form views, gallery views, and granular access controls.

**GitHub Pages**
Any public repository on GitHub can be published as a free website at `username.github.io/repository-name`. Supports static HTML/JS/CSS, Markdown (via Jekyll), and modern static site generators (Hugo, Eleventy). Zero cost, zero configuration required beyond enabling the feature in repository settings. This will serve as the public-facing web portal for SIGMA.

**GitHub Actions (Automation)**
Free tier includes 2,000 minutes/month of compute time for public repositories. This is sufficient for automated URL health checks (run monthly), CSV validation, and data refresh scripts. Workflows are defined in YAML files committed to the repository.

---

## 9. DATA SCHEMA & ARCHITECTURE

### 9.1 Master Schema — 22 Fields per Entry

Every entry in the SIGMA index will carry the following fields:

| # | Field Name | Type | Description | Example |
|---|-----------|------|-------------|---------|
| 1 | `sigma_id` | String | Unique SIGMA identifier | `HL-ISO-15189-2022` |
| 2 | `entry_type` | Enum | Standards Body / Standard / Framework / Treaty / Guideline / Regulation / Classification / Code of Practice / Recommendation | `Standard` |
| 3 | `meta_layer` | Enum | L1 Life Sciences / L2 Physical Sciences / L3 Society & Governance / L4 Economy & Trade / L5 Technology & Infrastructure / L6 Environment | `L1 Life Sciences` |
| 4 | `domain` | String (from 40-domain taxonomy) | Primary domain | `Health & Medical` |
| 5 | `sub_domain` | String | Sub-category within domain | `Clinical Laboratories` |
| 6 | `name_full` | String | Complete official name | `Medical laboratories — Requirements for quality and competence` |
| 7 | `name_short` | String | Common name / acronym | `ISO 15189` |
| 8 | `standard_id` | String | Official identifier from issuing body | `ISO 15189:2022` |
| 9 | `issuer` | String | Name of issuing body | `ISO (TC 212)` |
| 10 | `issuer_type` | Enum | UN Agency / Treaty Body / ISO / IEC / ITU / Industry SDO / Professional Body / NGO / Intergovernmental / National Government | `ISO` |
| 11 | `governance_layer` | Enum | International / Regional / National | `International` |
| 12 | `geographic_scope` | String | Countries / regions where formally applicable | `Global — 175 ISO member countries` |
| 13 | `year_published` | Integer | Year of current edition | `2022` |
| 14 | `year_first` | Integer | Year first published | `2003` |
| 15 | `status` | Enum | Active / Withdrawn / Superseded / Under Development / Under Review | `Active` |
| 16 | `mandate` | Enum | Mandatory / Voluntary / Voluntary-with-regulatory-adoption / Treaty-binding | `Voluntary` |
| 17 | `sector_applicability` | String | Who must/should use this standard | `Healthcare laboratories / accreditation bodies / regulators` |
| 18 | `why_it_matters` | String | Plain-language explanation of significance | `Defines quality requirements for medical labs; basis for lab accreditation in 100+ countries` |
| 19 | `key_outputs` | String | Main standards/versions/elements | `ISO 15189:2022 (third edition); covers pre-examination, examination, post-examination processes` |
| 20 | `official_url` | URL | Primary source URL (authoritative, stable) | `https://www.iso.org/standard/76677.html` |
| 21 | `data_source` | String | Where this entry's data was obtained | `ISO Open Data CSV + manual verification` |
| 22 | `notes` | String | Any additional contextual information | `Replaced 2012 edition; significant restructuring of management requirements` |

### 9.2 Supplementary Entity Tables

In addition to the main standards index, SIGMA maintains three supporting tables:

**Table B — Standards Bodies Register**
One record per issuing organisation. Fields: `org_id`, `org_name`, `org_acronym`, `org_type`, `founding_year`, `hq_country`, `hq_city`, `geographic_scope`, `governance_structure`, `iso_member` (Y/N), `wikidata_qid`, `official_url`, `linkedin_url`, `twitter_handle`, `standard_count`, `ics_scope`, `parent_org_id`.

**Table C — Relationships Map**
Captures inter-standard and inter-organisation relationships. Fields: `from_id`, `to_id`, `relationship_type` (supersedes / referenced_by / harmonised_with / implements / national_adoption_of / inspires), `notes`.

**Table D — Ratification & Adoption Tracker**
For treaty and convention entries only. One row per country-per-treaty. Fields: `sigma_id`, `country_iso3`, `country_name`, `status` (signatory / ratified / acceded / not party), `date`, `reservations`, `source_url`.

### 9.3 ID Convention

SIGMA IDs follow a deterministic, human-readable pattern:

`[DOMAIN_CODE]-[ISSUER_CODE]-[STD_NUMBER]-[YEAR]`

Examples:
- `HL-ISO-15189-2022` — Health, ISO standard 15189, 2022 edition
- `HR-UN-CRC-1989` — Human Rights, UN Convention, CRC, 1989
- `DG-IETF-RFC9110-2022` — Digital, IETF, RFC 9110, 2022
- `FS-CAC-GL21-2021` — Food Safety, Codex Alimentarius Commission, GL 21, 2021
- `FI-BCBS-BASELIII-2010` — Finance, BCBS, Basel III, 2010
- `HM-IASC-SPHERE-2018` — Humanitarian, IASC/Sphere, 2018 edition

---

## 10. PHASED RESEARCH & BUILD PLAN

The project is structured into **9 phases** spanning **24 months**, building from a seed dataset to a comprehensive, community-maintained living index.

---

### PHASE 0 — PROJECT SETUP & INFRASTRUCTURE
**Duration:** 2 weeks | **Status:** Ready to start

**Objective:** Establish all free infrastructure, governance documents, and working tools before any data collection begins.

**Activities:**

1. **Create GitHub organisation** `sigma-standards` at github.com — free, requires only email
2. **Create repository** `sigma-standards/sigma-index` — public repository under CC BY 4.0 license
3. **Set up GitHub Pages** — enable for `sigma-index` repository, configure basic landing page in Markdown
4. **Create Google Sheets Master Working Database** — one shared Google Sheets file with tabs for each domain group; share link with all contributors
5. **Download ISO Open Data** — download the latest CSV files from `iso.org/open-data.html` and commit to the repository's `/data/raw/iso/` directory
6. **Create project documentation** — write `README.md`, `CONTRIBUTING.md`, `SCHEMA.md`, `LICENSE` (CC BY 4.0), and `CODE_OF_CONDUCT.md` in the repository
7. **Set up GitHub Issues templates** — create issue templates for: new entry submission, error correction, URL update, domain expansion request
8. **Write initial SPARQL queries** — test Wikidata queries for standards bodies (see Annex C)
9. **Create GitHub Actions workflow** — set up monthly URL health check automation
10. **Define contributor roles** — Curator (Ariful), Domain Researchers (volunteers), Technical Reviewer, Community Manager

**Deliverables:**
- Live GitHub repository at `github.com/sigma-standards/sigma-index`
- GitHub Pages site live at `sigma-standards.github.io`
- ISO Open Data CSV committed to repo (seeds ~25,703 standard metadata entries)
- Google Sheets Master Working Database
- All governance documentation

---

### PHASE 1 — SEED FROM FREE BULK SOURCES
**Duration:** 4 weeks | **Effort:** 20 hours per week

**Objective:** Use the largest free bulk data sources to rapidly seed the index with structured metadata for the highest-priority standards and bodies.

**Activities:**

1. **Process ISO Open Data CSV** — clean, normalise, and map ISO metadata to SIGMA schema; assign SIGMA IDs to all 25,703 ISO entries; commit clean CSV to `/data/processed/iso_all.csv`
2. **Run Wikidata SPARQL queries** — extract all standards bodies (Q176799 instances) with names, URLs, founding years, countries; export to CSV; cross-reference with ISO Open Data
3. **Download and process all IETF RFC metadata** — fetch `https://www.rfc-editor.org/rfc/index.json`; map to SIGMA schema; assign SIGMA IDs to all 9,000+ RFCs
4. **Scrape ILO NORMLEX** — use ILO Data API to extract all 190 Conventions and 206 Recommendations with adoption status; map to SIGMA schema
5. **Process Codex Alimentarius index** — systematically download the Codex standards list; map to SIGMA schema
6. **Download all GRI Standards** — from globalreporting.org; map to SIGMA schema (40+ standards, free PDF)
7. **Download all SASB Standards** — from sasb.org; map to SIGMA schema (77 industry standards, free)
8. **Manually compile UN Treaties list** — from UNTC; extract all 560+ multilateral treaties with key metadata; map to SIGMA schema
9. **Compile all ILO fundamental Conventions** — 8 fundamental, 4 priority, 178 technical
10. **Compile OHCHR core instruments** — 9 treaties, all optional protocols, all General Comments
11. **Compile WHO key frameworks** — IHR 2005, ICD-11, ICF, EML, key WHO Guidelines (top 50 by citation)
12. **Compile all Sphere/CHS/INEE humanitarian standards** — complete free catalogue

**Deliverables:**
- `/data/processed/` directory with domain-specific clean CSVs
- Combined `sigma_v1_seed.csv` — estimated 35,000–40,000 entries (dominated by ISO)
- Data quality report noting completeness by field
- Wikidata entity cross-reference table

---

### PHASE 2 — HUMAN RIGHTS, HUMANITARIAN & DEVELOPMENT (Priority Domains)
**Duration:** 3 weeks | **Focus:** Domains 15, 16, 17, 20

**Objective:** Achieve comprehensive, deeply verified coverage of the domains most relevant to humanitarian practice — these are also the domains where freely available full text is most accessible.

**Domain 15 — Human Rights:** All 9 core UN human rights treaties; all Optional Protocols; all General Comments and General Recommendations of treaty bodies (these are freely available via OHCHR); all UN Human Rights Council resolutions of general application; all UPR outcomes with thematic analysis; all Special Procedure mandate reports; regional human rights instruments (ECHR, ACHPR, ACHR, Arab Charter, ASEAN Human Rights Declaration)

**Domain 16 — Labour:** All 190 ILO Conventions with ratification count; all 206 Recommendations; ILO Fundamental Conventions (C29, C87, C98, C100, C105, C111, C138, C182); ILO Governance Conventions; 2019 Centenary Declaration; MLC 2006 (Maritime Labour Convention); ILO OSH standards

**Domain 17 — Humanitarian:** Sphere Handbook 2018 (all 4 technical chapters — WASH, Food Security, Shelter, Health); CHS 9 commitments; INEE Minimum Standards; all IASC Guidelines (GBV, SGBV, PSEA, Mental Health, Accountability, Protection, CCCM, NFI, AAP, child protection, inclusion); UNHCR policies (AGD, GBV, RSD, Solutions, Cash, SGBV, Accountability); ICRC Customary IHL study (161 rules); Code of Conduct (1994); Emergency Medical Teams minimum standards; WHO Health Emergency and Disaster Risk Management Framework; HAP Standard history; OCHA Coordination Architecture

**Domain 20 — Education & Research:** UNESCO Conventions on qualifications recognition; ISCED 2011 (classification of education); ICH E6(R3) GCP; Declaration of Helsinki 2013; Belmont Report; FAIR Principles; ORCID standard; CrossRef DOI metadata standard; Dublin Core; ORCID; ISSN, ISBN, ISMN; open access standards (Budapest Open Access Initiative)

---

### PHASE 3 — ENVIRONMENT, CLIMATE & NATURAL SYSTEMS
**Duration:** 4 weeks | **Focus:** Domains 36–40

**Objective:** Build comprehensive environmental standards coverage, leveraging the extensive free treaty and framework texts available from UNFCCC, CBD, UNEP, and IAEA.

**Research approach for each treaty family:**
- Extract full treaty text URL from UNEP/UN/treaty secretariat
- Record entry-into-force date, number of parties, depositary
- List all subsidiary agreements, protocols, amendments, and COP decisions of general applicability
- Map to SIGMA schema and assign domain, sub-domain, mandate type

**Key research targets:**
- UNFCCC + Kyoto Protocol + Paris Agreement + all COP decisions (1–28) of general applicability
- CBD + Cartagena Protocol + Nagoya Protocol + Kunming-Montreal GBF (2022)
- All six major UNEP environmental conventions (Stockholm, Basel, Rotterdam, Minamata, Montreal, Ramsar)
- UNCLOS (comprehensive — the most important ocean treaty)
- CITES Appendices and Conference Resolutions
- IAEA Safety Standards series (complete — all free PDF)
- ISO 14000 family (ISO Open Data metadata + manual why-it-matters content)
- GHG Protocol full suite
- TNFD Framework v1.0 (free)
- SBTi Standards (free)
- Sendai Framework for DRR and UNDRR terminology standard
- FSC Forest Management Standard (free download via fsc.org)
- MSC Fisheries Standard (free download via msc.org)
- EITI Standard 2023 (free download via eiti.org)

---

### PHASE 4 — FINANCE, TRADE & ECONOMIC GOVERNANCE
**Duration:** 4 weeks | **Focus:** Domains 23–27

**Research approach:** Financial standards bodies publish almost all their standards freely. This phase involves systematic cataloguing of every publication from BCBS, IOSCO, IAIS, FSB, FATF, IFRS Foundation, IASB, ISSB, IFAC, and CPMI. The WTO legal texts and WCO Harmonized System chapters are all freely accessible.

**Key research targets:**
- All Basel Committee publications (Basel I, II, III, IV and all supporting standards)
- All IOSCO Principles and detailed standards
- All IAIS Insurance Core Principles (ICP 1–26) and ComFrame
- All FSB Key Standards (12 areas, full catalogue)
- All FATF 40 Recommendations + Interpretive Notes + FATF Guidance documents
- IFRS Standards — all 17 IFRS and 28 active IAS (free via IFRS Foundation with free account)
- All ISA/ISAE/ISRE/ISA auditing standards (IAASB/IFAC)
- OECD BEPS Actions 1–15 and Pillar One/Two documentation (free on oecd.org)
- All WTO agreements and annexes (free on wto.org)
- WCO Harmonized System chapter headings and subheadings (HS 2022)
- UN/CEFACT trade facilitation recommendations
- ISO 20022 (financial messaging) metadata

---

### PHASE 5 — ICT, DIGITAL, AI & CYBERSECURITY
**Duration:** 4 weeks | **Focus:** Domains 28–30

**Research approach:** The internet and digital space is paradoxically both the most standardised and most chaotic domain. IETF RFCs are already seeded from Phase 1. This phase deepens coverage with W3C, IEEE (free standards), NIST, ISO/IEC JTC 1 (metadata from ISO Open Data), and emerging AI/quantum standards.

**Key research targets:**
- W3C Recommendations (complete list from w3.org/TR/?status=rec)
- NIST SP 800 series (complete — all free from nvlpubs.nist.gov)
- NIST FIPS (Federal Information Processing Standards — all free)
- NIST AI RMF 1.0 and all supporting documents
- ISO/IEC 27001 family metadata (from ISO Open Data)
- ISO/IEC 42001 (AI Management) and all JTC 1 SC 42 output
- ISO/IEC JTC 3 (Quantum Technologies — new 2024) preliminary work
- IEEE 802 standards (Wi-Fi, Ethernet — catalogue with free summaries)
- ETSI standards catalogue (full list from etsi.org/standards)
- OASIS standards complete catalogue (oasis-open.org/standards)
- ECMA International standards (ecma-international.org — all free)
- GDPR, CCPA/CPRA, PIPL (China), PDPA (Thailand), LGPD (Brazil), POPIA (South Africa) — regulatory instruments
- EU AI Act (2024 — full text free from eur-lex.europa.eu)
- UNESCO AI Ethics Recommendation (2021 — free)
- OECD AI Principles (free)

---

### PHASE 6 — TRANSPORT, ENERGY, MANUFACTURING & BUILT ENVIRONMENT
**Duration:** 5 weeks | **Focus:** Domains 7–14, 31–34

**Research approach:** This is the most technically complex phase, spanning engineering standards that are largely ISO/IEC/ASTM (metadata free, full text paywalled). The strategy is to capture complete metadata for all standards in these domains from ISO Open Data (already done in Phase 1), then manually enrich the most important entries with why-it-matters content and cross-references.

**Aviation deep-dive:** ICAO's 19 Annexes and 44,000 SARPs are the backbone of global aviation safety. While full SARPs text requires ICAO subscription, ICAO provides free access to the table of contents of each Annex and amendment status. This phase documents the structure of each Annex and links to ICAO's free summaries.

**Maritime deep-dive:** IMO conventions (SOLAS, MARPOL, STCW, ISM Code, MLC 2006, ISPS Code, Ballast Water, Polar Code) are the core. IMO provides convention summaries free; full consolidated texts require subscription. Approach: document all conventions with summary, status, and official IMO reference page.

**Energy:** Complete IAEA Safety Standards catalogue (all free PDF); ISO 50001 family metadata; IEC TC 82 photovoltaics; IEC TC 88 wind turbines; IEEE 2030 smart grid series; ITU-T recommendations for smart energy grids.

---

### PHASE 7 — SOCIETY, CULTURE, SPORTS & SPECIALISED DOMAINS
**Duration:** 4 weeks | **Focus:** Domains 18–22, 35, 39–40

**Objective:** Achieve coverage of domains often overlooked in standards indices but crucial for comprehensive human-society coverage.

**Legal & Commercial Law (Domain 18):** All UNCITRAL Model Laws and Convention texts (all free from uncitral.un.org); all UNIDROIT instruments (free from unidroit.org); ICC Incoterms 2020 (summary free, full text paid); ICC UCP 600 (summary free); New York Convention on arbitral awards; Rome Statute; Palermo Protocols.

**Culture & Heritage (Domain 21):** UNESCO 1972 World Heritage Convention; UNESCO 2003 ICH Convention; UNESCO 2005 Cultural Diversity Convention; 1954 Hague Convention; ICOM Code of Ethics 2017; all ICOMOS International Charters (Venice, Burra, Nara, etc. — all free from icomos.org); ICCROM guidelines; UNESCO heritage management guidelines.

**Sports (Domain 22):** WADA Code 2021; UNESCO Convention Against Doping (2005); IOC Olympic Charter (free from olympics.com); all World Athletics Technical Rules (free); FIFA Regulations (Laws of the Game, Statutes — all free from fifa.com); CAS Arbitration Rules (free); ICAS Statutes; WACO anti-doping policy.

**Defence & Security (Domain 35 — Declassified):** UN Arms Trade Treaty; Ottawa Treaty; CCM; CTBT; CWC; BWC; NPT; Wassenaar Arrangement control list; IAEA safeguards agreements; NATO basic documents (free from nato.int); MIL-STD-461F and MIL-STD-810H (US DoD — freely downloadable).

---

### PHASE 8 — NATIONAL STANDARDS BODIES COMPREHENSIVE EXPANSION
**Duration:** 6 weeks | **Focus:** 175 national standards bodies + key national standards

**Objective:** Achieve complete coverage of all 175 ISO member national standards bodies (NSBs), including non-members. For each NSB, document the body itself plus its most internationally significant national standards that are not already covered as ISO adoptions.

**Research approach per NSB:**
1. Verify current NSB name, acronym, website, founding year, ISO membership type (full/correspondent/subscriber)
2. Confirm HQ city and government vs. private sector status
3. Document the NSB's primary standard series designation (BS, DIN, NF, JIS, GB/T, BDS, etc.)
4. Identify any nationally-originated standards that have achieved international significance or adoption

**Priority NSB regions:**
- **Sub-Saharan Africa (55 bodies):** ARSO member bodies — KEBS (Kenya), SABS (South Africa), SON (Nigeria), BOBS (Botswana), etc.
- **South & Southeast Asia (20 bodies):** BSTI (Bangladesh), BIS (India), SIRIM (Malaysia), PSQCA (Pakistan), SNV (Nepal), BSB (Bhutan), etc.
- **Latin America (20 bodies):** ABNT (Brazil), IRAM (Argentina), ICONTEC (Colombia), INDECOPI (Peru), etc.
- **MENA (18 bodies):** ESMA (UAE), SASO (Saudi Arabia), ONGPQ (Morocco), EOS (Egypt), etc.
- **Pacific (15 bodies):** SAI Global/Standards Australia, PCREEE, Pacific island NSBs

---

### PHASE 9 — VERIFICATION, PUBLICATION & COMMUNITY LAUNCH
**Duration:** 4 weeks

**Objective:** Quality assurance pass, public launch, and establishment of community contribution processes.

**Activities:**
1. **URL Verification Campaign** — automated check of all official_url fields; flag dead links for manual resolution (target: <2% dead links at launch)
2. **Completeness Review** — for every entry, check all 22 fields are populated or explicitly marked as `N/A` with reason
3. **Duplicate Detection** — algorithmic check for duplicate entries (same standard_id from same issuer); resolve or merge
4. **Expert Domain Review** — invite one domain expert per meta-layer to review entries in their area for accuracy
5. **GitHub Pages Website Build** — build search and filter interface using free static site tools (Jekyll or Hugo + Pagefind for full-text search)
6. **Generate final release files** — `sigma_v1.0_complete.csv`, `sigma_v1.0_complete.json`, `sigma_v1.0_bodies_only.csv`, `sigma_v1.0_treaties_only.csv`
7. **Write press release and outreach materials** — announce to IATI community, ALNAP, HumanitarianResponse.info, LinkedIn, ResearchGate
8. **Submit to open data catalogues** — submit to data.world (free), Kaggle Datasets (free), Zenodo (free DOI for datasets), EU Open Data Portal
9. **Establish GitHub Issues workflow** — documented, labelled, maintained for community contributions
10. **Version tagging** — tag the v1.0 release in GitHub with release notes

---

## 11. RESEARCH METHODOLOGY PER DOMAIN

### 11.1 Standard Research Protocol — Applied to Every Entry

For every new entry added to SIGMA, the researcher follows this 8-step protocol:

**Step 1 — Identify:** Confirm the standard/body exists and has a stable official identifier (standard number, treaty name, convention number, framework title)

**Step 2 — Primary Source:** Find the single most authoritative primary source URL — the issuing body's own official page, not a secondary reference, Wikipedia, or news article

**Step 3 — Classify:** Assign domain, sub-domain, meta-layer, governance layer, entry type, and mandate type using SIGMA taxonomy

**Step 4 — Metadata Capture:** Record all 22 SIGMA schema fields; mark unknown fields as `UNKNOWN` (not blank)

**Step 5 — Why It Matters:** Write a 1–3 sentence plain-language explanation of why this standard matters in practice, written for a non-expert audience. This is the most valuable field for general users and must be completed for every entry.

**Step 6 — Status Verification:** Confirm the standard is currently Active, or if Withdrawn/Superseded, identify its replacement

**Step 7 — Cross-Reference Check:** Check whether this standard references, supersedes, or is referenced by any existing SIGMA entry; update the Relationships Map (Table C)

**Step 8 — Source Logging:** Record in the `data_source` field exactly where the metadata came from (ISO Open Data CSV, Wikidata Q[number], manual research from URL, etc.)

### 11.2 Escalation Protocol for Uncertain Entries

When a researcher is uncertain about an entry (e.g., unclear whether a standard has global vs. regional standing, or whether its status is Active or Under Review), the following escalation applies:

- **Level 1:** Check the issuing body's official website directly for current status
- **Level 2:** Search for the standard in Wikidata — if it has a Q item, use that structured data
- **Level 3:** Search NIST's Standards Reference Database (free) for citation evidence
- **Level 4:** Create a GitHub Issue tagged `status-uncertain` for community review before including
- **Level 5:** Include with `status = UNVERIFIED` and note in the `notes` field

---

## 12. QUALITY ASSURANCE & VALIDATION PROTOCOL

### 12.1 Automated Checks (Monthly via GitHub Actions)

A GitHub Actions workflow runs on the 1st of every month:

1. **URL Health Check** — for every `official_url` field, sends an HTTP GET request and records the response code; flags 404/403/301-chains for manual review
2. **Schema Validation** — validates every CSV row against the SIGMA schema (correct number of columns, valid enum values, non-empty mandatory fields)
3. **Duplicate Detection** — checks for identical `standard_id` + `issuer` combinations; flags duplicates
4. **Mandatory Field Completeness** — reports percentage completeness for each field across all entries; tracks trend over time

### 12.2 Human Review Layers

**Contributor Level:** Any contributor submitting a new entry via GitHub Pull Request must complete a checklist confirming all 22 fields are populated, the URL has been verified live, and the entry type and domain are correctly assigned.

**Curator Level (Ariful/Lead):** The project curator reviews and approves all PRs. For additions, the curator spot-checks 10% of entries for accuracy. For corrections, the curator verifies the proposed change against the primary source before merging.

**Domain Expert Level (Phase 9+):** Quarterly domain expert reviews, where subject matter experts audit a random sample of 50 entries in their domain for accuracy, currency, and completeness.

### 12.3 Community Correction Mechanism

Any user can submit a correction via:
- **GitHub Issue** — using the "Error Report" issue template
- **GitHub Pull Request** — direct edit of the source CSV with documented change reason
- **Email** — for users without GitHub accounts; email submissions are triaged to Issues

All accepted corrections are logged in `CHANGELOG.md` with date, field changed, old value, new value, and source of correction.

---

## 13. GOVERNANCE & MAINTENANCE MODEL

### 13.1 Roles and Responsibilities

| Role | Responsibility | Commitment |
|------|---------------|------------|
| **Lead Curator** (Ariful) | Overall direction, final review of all PRs, annual version releases, partner outreach | 4–6 hours/month post-launch |
| **Domain Researcher** (per domain, volunteer) | Initial population and ongoing maintenance of assigned domain entries | 2–4 hours/month per domain |
| **Technical Maintainer** (volunteer) | GitHub Actions, website, data pipeline scripts, API | 2–4 hours/month |
| **Community Manager** (volunteer) | Triage GitHub Issues, welcome new contributors, maintain CONTRIBUTING.md | 2–3 hours/month |
| **External Reviewers** (volunteers) | Subject matter experts who review entries in their professional domain | 2–4 hours/quarter |

### 13.2 Version Release Schedule

| Version | Trigger | Release Process |
|---------|---------|----------------|
| **Patch (v1.0.1)** | URL corrections, factual error fixes, status updates | Merge to main; auto-update data files; GitHub release note |
| **Minor (v1.1)** | New entries added, new field added, new domain | Curated PR batch; updated `CHANGELOG.md`; new GitHub release |
| **Major (v2.0, v3.0)** | Significant scope expansion, schema change, new technology platform | Full release planning; blog post; outreach to partners |

### 13.3 Sustainability Strategy

The project is designed to survive without any single individual:

1. **All data is in public GitHub repository** — anyone can fork and continue
2. **All tooling is documented** — any competent volunteer can run the pipeline
3. **CC BY 4.0 license** — anyone can reuse, redistribute, and build on the data
4. **Multiple contributor model** — no single point of failure
5. **Automated maintenance** — GitHub Actions runs checks without human intervention
6. **Partner institutions** — seek adoption by IATI, ISC, ALNAP, Humanitarian Data Exchange (HDX) for long-term hosting resilience

---

## 14. RISK REGISTER & MITIGATIONS

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| R1 | ISO closes its Open Data portal or changes license | Low | Very High | Download and archive all ISO Open Data CSVs at every release; store in Git history; mirror on Zenodo |
| R2 | GitHub changes free tier terms | Low | High | All data is portable CSV/JSON; can migrate to GitLab, Codeberg (both free) or self-hosted Gitea in <1 day |
| R3 | Key contributor loses time or interest | Medium | Medium | Multi-contributor model; documented processes; no single point of failure |
| R4 | Standards bodies object to metadata indexing | Low | Low | We index metadata only (title, ID, issuer, URL) — not the full text of paywalled standards; this is fair use / transformative use; standard practice for bibliographic databases |
| R5 | Data becomes outdated (standards revised/withdrawn) | High | Medium | Monthly automated URL checks; annual full review; community corrections; data includes version/year field so staleness is visible |
| R6 | Scope overwhelm — project becomes unmanageable | Medium | High | Phased approach with clear deliverables per phase; scope clearly defined by inclusion criteria; "good enough" entries are valid — completeness over perfection |
| R7 | Wikidata SPARQL endpoint becomes unreliable | Medium | Low | Wikidata data is downloadable as bulk dump; also available via multiple mirror endpoints |
| R8 | Naming/classification disputes for politically sensitive standards | Medium | Low | SIGMA describes and indexes; does not evaluate or take positions; disputed items noted as `[DISPUTED]` in notes field |
| R9 | Copyright claims on standard metadata (title, number) | Very Low | Low | Bibliographic metadata (title, year, issuer, ID number) is universally considered non-copyrightable; this is settled law in most jurisdictions |
| R10 | Google Sheets hits limits during data population | Low | Medium | Migrate to NocoDB (free, self-hostable) in Phase 3 if Sheets limits are hit; data always in CSV regardless |

---

## 15. MILESTONES & SUCCESS METRICS

### 15.1 Milestone Timeline

| Milestone | Target Date | Success Criterion |
|-----------|------------|-------------------|
| M0 — Infrastructure Ready | Week 2 | GitHub repo live, Google Sheets created, ISO Open Data downloaded |
| M1 — Seed Dataset | Week 6 | 35,000+ entries in CSV from bulk sources (ISO, IETF, ILO, Codex) |
| M2 — Priority Domains Complete | Week 10 | Health, Humanitarian, Human Rights, Finance, Climate fully populated and verified |
| M3 — Environmental & Trade Domains | Week 16 | Domains 23–27, 36–40 fully populated |
| M4 — Technology Domains | Week 22 | Domains 28–35 fully populated |
| M5 — National Bodies Complete | Week 32 | All 175 NSBs documented; key national standards captured |
| M6 — Quality Review Complete | Week 36 | URL check <2% dead; completeness >85% across all mandatory fields |
| **M7 — SIGMA v1.0 PUBLIC LAUNCH** | **Week 40** | Full public release on GitHub; all download formats live; announcement published |
| M8 — Community Established | Week 52 | 20+ GitHub contributors; 5+ institutional partners citing SIGMA |
| M9 — SIGMA v2.0 | Month 18 | 15,000+ entries; web portal with full-text search; REST API live |
| M10 — SIGMA v3.0 | Month 24 | 50,000+ entries; multilingual support (at minimum French, Arabic, Spanish); Zenodo DOI assigned |

### 15.2 Success Metrics at Each Version

**v1.0 Success Criteria (Month 10):**
- Minimum 5,000 fully verified entries across all 40 domains
- All 40 domains represented with at least 10 entries each
- All 175 ISO member NSBs documented
- URL validity: ≥98% live URLs at launch
- Field completeness: ≥85% of mandatory fields populated across all entries
- GitHub repository: public, CC BY 4.0, with README, schema, and contributing guide
- Downloadable in CSV, JSON, and XLSX formats
- At least 3 external organisations citing or linking to SIGMA

**v2.0 Success Criteria (Month 18):**
- Minimum 15,000 entries
- All 9,000 IETF RFCs fully mapped
- All ISO metadata (25,703) incorporated with enriched why-it-matters content for top 1,000
- Web portal with full-text search (GitHub Pages + Pagefind)
- REST API endpoint (simple, free-tier hosted)
- At least 10 institutional partners (NGOs, universities, government agencies)
- Community: 50+ GitHub contributors

**v3.0 Success Criteria (Month 24):**
- Minimum 50,000 entries
- Ratification tracker live for all 560+ UN treaties
- Multilingual entries (French and Spanish equivalents for all domains)
- Machine-readable update feed (RSS/Atom) for new entries and status changes
- Zenodo DOI for permanent citability
- Academic citation in at least one peer-reviewed publication

---

## ANNEX A — FULL DOMAIN-BY-DOMAIN SOURCE MAP

| Domain | Primary Free Sources | Estimated Entries | Key Challenge |
|--------|---------------------|------------------|---------------|
| Health & Medical | WHO IRIS (OAI-PMH), ISO Open Data (TC 212), IHTSDO/SNOMED (metadata free), HL7 website | 400–600 | Thousands of WHO guidelines; need curation for most important |
| Food Safety | Codex Alimentarius website (complete, free), ISO Open Data (TC 34), FAO FAOLEX | 3,000–4,000 | Codex has 3,000+ texts; categorisation work |
| Animal Health | WOAH website (full, free), OIE codes, FAO FAOLEX | 100–200 | Need to parse WOAH code structure |
| Plant Health | IPPC website (complete, free ISPMs), FAO FAOLEX | 50–100 | ISPMs are well-structured and complete |
| OHS | ILO NORMLEX (free), ISO Open Data (TC 283), OSHA publications | 250–350 | ILO conventions well-catalogued |
| Pharmaceuticals | ICH website (free guidelines), WHO prequalification, EMA public docs | 150–250 | ICH guidelines are well-documented |
| Metrology | BIPM website (free), OIML (free), ILAC (free) | 100–150 | Compact, well-defined domain |
| Manufacturing | ISO Open Data (multiple TCs), ASTM metadata (free preview), ASME metadata | 2,000–3,000 | Vast domain; prioritise internationally referenced standards |
| Electrical & Electronics | ISO Open Data (IEC via ISO), IEC website (metadata free) | 2,000–3,000 | IEC doesn't have open data like ISO |
| Construction | ISO Open Data (TC 59, TC 268), ICC model codes (free summaries), NFPA (free view) | 500–800 | National codes vary widely |
| Chemical Industries | ISO Open Data, UNECE GHS, REACH (EUR-Lex free) | 300–500 | GHS well-documented; API standards harder |
| Materials | ISO Open Data (multiple TCs), ASTM metadata | 1,500–2,000 | Vast; prioritise referenced standards |
| Aerospace | ISO Open Data (TC 20), ICAO summaries (free), SAE metadata | 400–600 | ICAO full text paywalled; use official summaries |
| Space | CCSDS free documents, ISO TC 20 SC 14, ITU Radio Regs | 150–250 | CCSDS documents are fully free |
| Human Rights | OHCHR (complete, free), UN Treaty Collection | 100–200 | Well-documented; all texts free |
| Labour | ILO NORMLEX (complete, free), ILO Data API | 400–450 | ILO has excellent free structured data |
| Humanitarian | Sphere (free), CHS (free), IASC (free), UNHCR (largely free) | 150–250 | Scattered across multiple NGO sites |
| Legal & Commercial | UNCITRAL (free), UNIDROIT (free), ICC summaries | 100–200 | ICC full texts partially paywalled |
| Governance & AC | ISO 37000 series (metadata), UNCAC (free), OECD (largely free) | 80–120 | Well-catalogued, manageable |
| Education & Research | UNESCO (free), OECD ISCED (free), DOI/ORCID metadata | 80–120 | Scattered; need curation |
| Culture & Heritage | UNESCO (free), ICOMOS charters (free), ICOM code (free) | 60–100 | Relatively compact domain |
| Sports | WADA (free), IOC (free), FIFA (free), World Athletics (free) | 60–100 | All major sports bodies publish freely |
| Finance & Banking | BIS/BCBS (free), FSB (free), IOSCO (free), FATF (free), IFRS (free account) | 300–500 | High quality free sources available |
| Trade & Customs | WTO (free), WCO HS (metadata free), UN/CEFACT (free) | 100–200 | WTO texts completely free |
| Supply Chain | GS1 website (metadata free), ISO Open Data | 80–120 | GS1 standards well-documented |
| Sustainability/ESG | GRI (free), SASB (free), ISSB (free account), EU ESRS (free) | 150–250 | Rapidly evolving domain |
| Taxation | OECD (free for most), IMF (free) | 50–80 | OECD documents largely free |
| ICT | ISO Open Data (JTC 1), IETF RFCs (9,000+, all free), W3C (400+, all free), ETSI | 12,000–15,000 | IETF alone contributes 9,000+ entries |
| Cybersecurity | NIST SP 800 (free), ISO metadata, ENISA (free) | 300–400 | NIST docs completely free |
| AI & Emerging Tech | ISO/IEC 42001 metadata, NIST AI RMF (free), OECD (free), UNESCO (free) | 80–150 | Fast-moving; new standards appearing monthly |
| Energy & Utilities | IAEA (all free), ISO Open Data, IEC metadata, ITU-T | 400–600 | IAEA Safety Standards are completely free |
| Transport | ICAO summaries (free), IMO summaries (free), UNECE (free), ISO Open Data | 500–800 | ICAO/IMO full texts partially paywalled |
| WASH | WHO (free), Sphere (free), JMP methodology (free), WPDx (free) | 60–100 | Compact, critical for humanitarian work |
| Built Environment/Urban | ISO 37100 series (metadata), IEC SyC (metadata), ITU-T (free) | 100–150 | Growing domain; well-documented |
| Defence (Declassified) | UN ATT (free), Ottawa/CCM (free), CTBT (free), MIL-STDs (free where declassified) | 80–120 | Declassified subset only |
| Environment & Climate | UNFCCC (free), CBD (free), UNEP conventions (free), ISO 14000 (metadata) | 200–300 | Treaty texts all free; ISO metadata free |
| Marine & Ocean | UNCLOS (free), IMO (summaries free), FAO (free), regional seas (free) | 100–150 | IMO full conventions partially paywalled |
| Biodiversity | CBD (free), CITES (free), IUCN (free), RAMSAR (free) | 80–120 | All major texts freely available |
| Disaster Risk | UNDRR (free), ISO 22301 metadata, Sendai (free) | 50–80 | Compact and well-documented |
| Extractive Industries | EITI (free), ICMM (free), API metadata, ISO TC 82 (metadata) | 80–120 | EITI standard completely free |
| **TOTAL ESTIMATED** | | **~40,000–55,000** | *Phase 1 seed: ~35,000. Full scope with enrichment: 50,000+* |

---

## ANNEX B — FREE TOOL SETUP GUIDE

### Step 1: Create GitHub Account
1. Go to `github.com/signup`
2. Enter email, create password, choose username `sigma-standards` or similar
3. Verify email — **no credit card required at any step**
4. Create new organisation (free): Settings → Organisations → New Organisation → Free tier

### Step 2: Create Repository
1. In your organisation, click "New Repository"
2. Name: `sigma-index`
3. Set to **Public** (required for free GitHub Pages)
4. Add README, choose MIT or CC BY license
5. Enable GitHub Pages: Settings → Pages → Source: main branch → `/docs` or root

### Step 3: Download ISO Open Data
1. Go to `https://www.iso.org/open-data.html`
2. Click download links for: `iso_deliverables.csv` (standards metadata), `iso_committees.csv` (TC data), `iso_ics.csv` (classification)
3. No registration required — direct download links
4. Commit these files to your repo under `/data/raw/iso/`

### Step 4: Set Up Google Sheets Working Database
1. Create a free Google account at `accounts.google.com` (no credit card)
2. Go to `sheets.google.com` → New Spreadsheet
3. Name it "SIGMA Master Working Database"
4. Create tabs for each domain group (Phase groupings work well)
5. Share with collaborators via link ("Anyone with link can edit")

### Step 5: First Wikidata SPARQL Query
1. Go to `https://query.wikidata.org/`
2. Paste the standards body query from Annex C
3. Click Run — results appear in seconds
4. Click Download → CSV to get a clean CSV of results

### Step 6: Configure GitHub Actions for URL Checks
Create file `.github/workflows/url-check.yml` in your repository:
```yaml
name: Monthly URL Health Check
on:
  schedule:
    - cron: '0 0 1 * *'  # Runs at midnight on 1st of each month
  workflow_dispatch:      # Also allow manual trigger

jobs:
  check-urls:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install requests pandas
      - name: Run URL check
        run: python scripts/check_urls.py
      - name: Commit results
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "SIGMA Bot"
          git add data/url_health_report.csv
          git diff --staged --quiet || git commit -m "Monthly URL health check [automated]"
          git push
```

---

## ANNEX C — WIKIDATA SPARQL QUERIES FOR STANDARDS BODIES

The following SPARQL queries can be run directly at `https://query.wikidata.org/` with no registration. Results can be downloaded as CSV for immediate import into SIGMA.

### Query 1: All International Standards Bodies

```sparql
SELECT DISTINCT ?org ?orgLabel ?inception ?country ?countryLabel ?website WHERE {
  ?org wdt:P31/wdt:P279* wd:Q176799 .  # instance of: standards organization
  OPTIONAL { ?org wdt:P571 ?inception . }
  OPTIONAL { ?org wdt:P17 ?country . }
  OPTIONAL { ?org wdt:P856 ?website . }
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY ?orgLabel
LIMIT 2000
```

### Query 2: All ISO Published Standards with Metadata

```sparql
SELECT ?std ?stdLabel ?issuer ?issuerLabel ?year ?doi WHERE {
  ?std wdt:P31 wd:Q317623 .          # instance of: standard
  ?std wdt:P123 wd:Q193579 .         # publisher: ISO
  OPTIONAL { ?std wdt:P577 ?year . }
  OPTIONAL { ?std wdt:P356 ?doi . }
  OPTIONAL { ?std wdt:P123 ?issuer . }
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY ?stdLabel
LIMIT 5000
```

### Query 3: All UN Treaty Bodies and Treaty Names

```sparql
SELECT DISTINCT ?treaty ?treatyLabel ?year ?parties WHERE {
  ?treaty wdt:P31/wdt:P279* wd:Q131569 .   # instance of: treaty
  ?treaty wdt:P17 wd:Q1065 .                # country: United Nations (Q1065)
  OPTIONAL { ?treaty wdt:P577 ?year . }
  OPTIONAL { ?treaty wdt:P1132 ?parties . }
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY ?treatyLabel
LIMIT 1000
```

### Query 4: National Standards Bodies by Country

```sparql
SELECT DISTINCT ?org ?orgLabel ?country ?countryLabel ?website ?founding WHERE {
  ?org wdt:P31/wdt:P279* wd:Q1639634 .  # instance of: national standards body
  OPTIONAL { ?org wdt:P17 ?country . }
  OPTIONAL { ?org wdt:P856 ?website . }
  OPTIONAL { ?org wdt:P571 ?founding . }
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY ?countryLabel
LIMIT 500
```

### Query 5: ISO Technical Committees

```sparql
SELECT ?tc ?tcLabel ?scope WHERE {
  ?tc wdt:P31 wd:Q1664689 .           # instance of: technical committee
  ?tc wdt:P749 wd:Q193579 .           # parent organization: ISO
  OPTIONAL { ?tc schema:description ?scope FILTER(lang(?scope) = "en") . }
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY ?tcLabel
LIMIT 1000
```

---

*End of Research Project Plan — SIGMA v1.0*

---

**Document Control**

| Field | Value |
|-------|-------|
| Document Title | SIGMA Research Project Plan |
| Version | 1.0 |
| Date | May 2026 |
| Lead Author | Mohammad Ariful Islam, CPI Bangladesh Mission |
| License | CC BY 4.0 — Free to share and adapt with attribution |
| Contact | Via GitHub Issues at `github.com/sigma-standards/sigma-index` |
| Next Review | November 2026 |

> *"Standards are the architecture of trust. SIGMA is the map of that architecture."*

---

## 19. ENHANCED INTEGRATION ROADMAP (ADDED MAY 2026)

This section incorporates the latest improvement recommendations and aligns implementation with a scalable, self-improving, open infrastructure.

### 19.1 Strategic Upgrade Summary

SIGMA remains metadata-first and free-first, while adding:

1. **Hybrid storage model**: tabular datasets (CSV/JSON/Parquet) plus a relationship-centric knowledge graph.
2. **Continuous ingestion**: scheduled source refresh for rapidly changing registries (especially ISO open data).
3. **LLM-assisted operations**: enrichment, classification, deduplication, and quality checks.
4. **Improved publication UX**: faceted navigation, semantic search, multilingual support, and public API endpoints.
5. **Institutional resilience**: formal partner pathways and mirrored archival strategy.

### 19.2 Architecture Extension — Tabular + Graph + Vector

- **Tabular canonical layer**: maintains master schema and source-truth records.
- **Graph layer** (Neo4j Community / RDF4J / Apache Jena): models `references`, `supersedes`, `adopted_by`, `implements`, `aligned_with`.
- **Vector layer** (Qdrant or equivalent): enables semantic retrieval over summaries and metadata fields.
- **GraphRAG query path**: combines symbolic relationships + semantic retrieval for higher-precision answers.

### 19.3 Automation and Freshness

Add scheduled jobs (GitHub Actions and/or Dagster/n8n) for:

- Daily ISO open data delta ingestion (deliverables, TCs, ICS).
- Weekly Wikidata SPARQL sync for organisations and identifiers.
- Periodic refresh of treaty ratification and instrument status sources.
- Automated change logs and dataset version snapshots.

### 19.4 LLM Integration (Open/Low-cost Stack)

Use open/free model workflows for curation support:

- Auto-generate draft `why_it_matters` notes from source metadata.
- Suggest domain/sub-domain tags and relationship candidates.
- Detect potential duplicates, stale links, and schema anomalies.
- Support multilingual summaries for high-impact entries.

Human review remains mandatory for publication to preserve source-truth principles.

### 19.5 Quality Controls at Scale

In addition to existing QA:

- Add rule-based schema validation gates in CI.
- Add graph consistency constraints (SHACL-style rules where feasible).
- Add LLM-assisted consistency review with explicit confidence flags.
- Track data provenance and transformation lineage for each record.

### 19.6 UX, Accessibility, and API

Enhance discoverability for non-technical users:

- Faceted browsing by domain, body, status, geography, and year.
- Natural language search interface over indexed metadata.
- Lightweight public API for filtered retrieval and integrations.
- Accessibility-first publishing (clear language, low-bandwidth pages, multilingual priorities).

### 19.7 Sustainability and Ecosystem Strategy

To reduce single-maintainer risk:

- Mirror releases to Zenodo and other archival platforms.
- Publish reusable ingestion scripts and data contracts.
- Build contributor playbooks for domain maintainers.
- Pursue collaborations with universities, open-data communities, and standards-focused civil society groups.

### 19.8 Revised 8-Week Execution Sprint

**Week 1–2**
- Ingest latest ISO + Wikidata updates into canonical schema.
- Stand up initial graph schema and relationship extractor.

**Week 3–4**
- Launch automated sync pipeline and validation workflow.
- Enable first LLM-assisted enrichment pass with human approval.

**Week 5–6**
- Publish MVP search + faceted navigation + downloadable bundles.
- Expose minimal API and changelog feed.

**Week 7–8**
- Expand to 5–10 high-impact domains with enriched relationship mapping.
- Publish contributor onboarding and partnership outreach package.

### 19.9 Implementation Checkpoint — Started from Final Roadmap

Initial implementation now begins from the final roadmap layer rather than the earliest research phases:

- Added a schema validation gate for processed CSV datasets.
- Added GitHub Actions validation workflow for pull requests and main-branch pushes.
- Added a relationship-map template for the graph layer with confidence/provenance fields.
- Added relationship-map validation for graph edge fields, provenance, and known SIGMA IDs.
- Added relationship extraction for ILO `supersedes` and source-resolved ISO `references` links.
- Added release artifact generation for CSV, JSON, JSONL, relationship exports, and a lightweight API index.
- Added a canonical 40-domain registry, domain source map, curated domain seed records, and generated coverage report.
- Added `Makefile`, GitHub release-build workflow, and GitHub Pages workflow to make validation, artifact builds, and publishing repeatable.
- Updated schema documentation to align graph relationship terminology with the enhanced roadmap.

Current generated bundle: 88,083 master entries, 20,130 relationship edges, and all 40 canonical domains represented.

Next implementation step: expand relationship extraction to source-confirmed `national_adoption_of` links and add additional source ingestors for priority domains.
