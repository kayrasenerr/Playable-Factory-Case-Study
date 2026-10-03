# Developer log — Playable Factory Product Manager case study

**Prepared by:** Kayra Şener, with AI-assisted research, analysis and production  
**Research and report production:** 02–03 October 2026  
**Documentation package:** 03 October 2026  
**Primary deliverable:** 43-page Product Manager case study  
**Purpose:** Explain how the research became a technical, traceable submission and how its calculations and production artifacts can be inspected or reproduced.

## 1. Project objective and scope

I designed this project to connect a genuine product benefit, a short playable interaction and a measurable commercial outcome. The final case covers company selection and client onboarding, a Picnic concept and wireframe, a Ready product proposal, three playable reviews, a non-game adaptation, display banners, prospect research, two campaign analyses, a proposed API-assisted research workflow and a compact AI contribution statement.

The work is a research and product-management case. The wireframe describes a proposed interaction; it is not an executable ad. The Ready extension is a product proposal. Campaign recommendations are investigation and test plans. The Sensor Tower section is a workflow design under the brief's access assumption.

I created the research tree, defined source-file scope and organization, selected the companies and transferable features, supplied my interpretation and creative direction, played the ads, reviewed each stage and finalized the report. AI supported research, synthesis, calculations, technical elaboration and document production.

## 2. Requirements translated into deliverables

The supplied case-study PDF defined the numbered tasks and output limits. The implementation used these constraints to allocate report space before adding the supporting research appendix.

| Requirement | Final report location | Implemented output |
| --- | --- | --- |
| 1.1–1.4 | Pages 3–9 | Seven client-facing pages covering Fugo and Picnic, onboarding, commercial differences, concept and four-screen vector wireframe |
| 2.1–2.2 | Page 10 | One-page Ready proposal for goal-aware launch preparation and a versioned experiment brief |
| 3.1 | Pages 11–13 | Three playable reviews, each with mechanics, a screenshot and exactly three changes |
| 3.2 | Page 14 | Five-step Picnic adaptation of All in Hole's collection-and-growth interaction |
| 4.1 | Page 15 | Three text-only static/automatically animated banner concepts |
| 5.1 | Pages 16–20 | Qualification method and ten prospects: five gaming studios and five European online-grocery businesses |
| 5.2 | Pages 21–22 | Separate one-page reports for Puzzle Game X and Grocery App Y |
| 5.3 | Page 23 | Approximately half a page of Sensor Tower + AI workflow design |
| 5.4 | Page 24 | One-page workflow and division-of-labor disclosure |
| Research appendix | Pages 25–40 | Workflow log, source register, arithmetic appendix and external evidence ledger |
| Gameplay visual appendix | Pages 41–43 | Selected start-to-end screenshot sequences |

The appendix supports the main answers. It does not replace required content inside the capped sections. Prompt screenshots and conversation links are outside this documentation package's scope and will be supplied separately.

## 3. Source architecture

The source collection has four practical layers.

1. **Primary case inputs:** the case-study manual and raw campaign-data PDF.
2. **Research guides:** scope, product context, task-specific research directions, calculation tables and production guidance.
3. **First-hand gameplay evidence:** my three descriptions and screenshots of the exact playable exports.
4. **External research:** official product/company pages, app-store listings, company profiles, technical documentation and dated ad-intelligence observations.

The original guide files remain preserved as research inputs. They describe how to investigate and produce the case; their seeds, questions and suggested concepts are not independently verified findings. The final report's external ledger records the sources actually relied on for its product and prospect claims.

The report uses **F01–F50** for its supplied-file register and **E01–E46** for its external ledger. The original preparation guides use **S-series** identifiers. Each identifier resolves within its own register; the three series are not interchangeable.

The package's `audit/source_manifest.json` records the report's 50 registered source files, their relative paths, byte sizes, full SHA-256 hashes and stated uses. The report embeds 56 attachments: those 50 source records, a manifest, regenerated metrics and four manual intervention logs.

## 4. Research workflow and production history

### Research design

I established the research tree and defined the information required in each source file. This organized the work around deliverables rather than an undirected collection of links. Company selection and transferable-feature choices came from my analysis of the gathered evidence.

### Source collection and interpretation

GPT 5.6 Sol mainly supported data gathering and summarization. GPT Astra also researched the web, completed source files and drafted report content from my insights. Official pages established product identity and capability; store records supported app/publisher matching; company profiles and ad observations supported prospect screening.

I read and analyzed the gathered material. My creative additions drew on my game experience and industry understanding, informed by this evidence. AI helped express that reasoning as commercial concepts, implementation details and testable recommendations.

### Working with source detail

I first uploaded the sources to NotebookLM and connected it to Claude Cowork, using NotebookLM as a source database to reduce context overhead. The summaries did not retain enough detail for the case. I discarded that report and moved the source files into the report project to work directly with Astra at medium-to-high usage.

This workflow change established direct source access as the basis for the final analysis. It also kept the requirements, source data and gameplay descriptions available during detailed drafting.

### Gameplay documentation

I played Squad Busters, Clean It! and All in Hole and supplied descriptions and screenshots. My descriptions establish mechanics, timing, sound and redirection behavior. Screenshots establish visible interface states, art style and selected sequences. AI inspected the images and organized the findings; the record does not attribute the playthrough to AI.

### Production and final review

GPT Astra 6 supported structure, report writing, visuals and live revisions. AI-assisted production also included requirement mapping, numerical reconciliation, source registration, vector wireframe drawing, screenshot selection, attachment packaging and rendered-layout inspection.

I reviewed each stage and finalized the report and manual intervention logs. The report uses first-person or neutral language, presents a complete analysis and keeps implementation history in the supporting documentation.

## 5. Product and creative implementation

### Task 1: benefit, interaction and commercial outcome

Fugo's Words of Wonders supports a short, authentic word-solving payoff. Picnic supports a useful meal-to-ingredients/basket demonstration. The distinction carries through the commercial narrative: a gaming acquisition test evaluates installs alongside player quality; a grocery acquisition test evaluates first orders and, where available, contribution and repeat ordering.

The wireframe is drawn with ReportLab primitives and text. Its four states show the hook, ingredient selection, completed basket and explicit destination handoff. It is readable inside the PDF without a separate prototype link.

### Task 2: Ready proposal

Research established that Ready already offers template customization and variant/A/B workflows. The proposed addition addresses the handoff into a useful experiment: goal definitions, event contract, experiment/version metadata, QA checks and destination validation.

The proposal includes gaming and grocery applications, an initial implementation scope and discovery/validation questions. It does not claim that an unmentioned feature is absent or that the proposed benefit has already been validated with customers.

### Task 3: playable analysis

| Playable | Main observed issue | Proposed direction |
| --- | --- | --- |
| Squad Busters | Combat has no effective damage-and-survival consequence; emeralds and coins have the same value | Functional health and a losing condition, two-coin emerald value, clearer recruit/fusion confirmation |
| Clean It! | Four recent pickups can win without disposal; pickups expire after ten seconds | Win through four deposited pieces, align the floor goal with its visible threshold, reduce unrelated customer cues |
| All in Hole | Early frightening alarm, sparse result communication and any-tap store redirection | Readable outcome and explicit CTA, restrained final-seconds warning, objective guidance before timer pressure |

Each review contains three improvements with rationale and validation measures. Proposed changes are separate from the current mechanics. The Picnic adaptation preserves drag movement, collection and progress feedback while using a recipe basket and an explicit CTA.

### Task 4: display banners

The three banner concepts use static or automatic visual sequences. Their interaction requirements differ from playables: they convey a benefit without gameplay input. The copy and destination strategy are proposed creative work, with brand and serviceability review required before a real launch.

## 6. Prospect research and qualification

The gaming prospects are Grand Games, Rooftop Games, Leap Games, Infinity Games and Cypher Games. The grocery prospects are Picnic, Ocado Retail, Everli, Rohlik Group/Knuspr and Flink.

Gaming qualification combines casual/puzzle fit, app/publisher identity, a studio-size/ownership screen and dated US/European acquisition-ad observations. The report defines recent as 06 July–03 October 2026, inclusive. Its cited observations fall in September 2026.

The research separates country-specific ad observations from store availability, download popularity and job listings. SocialPeta observations are acquisition signals, not audited spend. LinkedIn size bands are self-reported. First-contact recommendations name roles; they are not verified individual contact records.

Fugo remains the Task 1 company. Cypher supplies the fifth gaming prospect in Task 5.1, where dated geographic ad evidence is required. Buying entity, budget ownership and publisher/agency relationships remain standard pre-outreach checks, particularly where an app's advertiser label differs from the studio identity.

## 7. Campaign-data implementation

### Inputs and grain

The supplied raw PDF contains eight observations split horizontally across two pages. The CSV joins the identity and metric columns by row alignment. Each observation is one campaign × geography × operating-system cell.

The raw fields include campaign, vertical, geography, operating system, spend, impressions, playable loads, first interaction, average time, end-card reach, CTA clicks and conversions. Puzzle conversions are installs; grocery conversions are first orders. Spend is in USD.

### Calculation script

`data/recalculate.py` uses Python's standard library. It reads `campaign_raw.csv` beside the script, asserts eight unique campaign/geography/OS keys, validates non-negative inputs and checks the supplied count ordering.

It creates eight cell rows plus two campaign-total rows, four geography-total rows and four OS-total rows: **18 derived rows**. Aggregate numerators and denominators are summed before division.

| Metric | Formula | Meaning |
| --- | --- | --- |
| CPI / first-order CPA | Spend ÷ conversions | Cost of the named business outcome |
| CPM | 1,000 × spend ÷ impressions | Media cost per thousand impressions |
| CPC | Spend ÷ CTA clicks | Diagnostic click cost |
| Load rate | Loads ÷ impressions | Entry into the playable |
| Interaction rate | First interactions ÷ loads | First action among loaded experiences |
| End-card reach | End cards ÷ first interactions | Reach among interactors |
| Click per end card | CTA clicks ÷ end cards | Descriptive ratio at the handoff |
| CTR | CTA clicks ÷ impressions | Click yield from exposure |
| Conversion per click | Conversions ÷ CTA clicks | Descriptive downstream ratio |
| Outcome yield | 1,000 × conversions ÷ impressions | Installs/orders per thousand impressions |

Percentage fields multiply these ratios by 100. The script writes full-precision CSV values and rounded Markdown audit tables. Average time is retained at source-row level and is not aggregated because its measurement base is unspecified.

### Reconciliation

The report builder compares regenerated metrics with `project_sources/03-campaign_metrics.csv`. It requires matching row count, column keys and campaign/segment labels, then uses `math.isclose` with relative and absolute tolerances of `1e-12` for numeric fields.

| Campaign | Spend | Outcomes | Recomputed total |
| --- | ---: | ---: | ---: |
| Puzzle Game X | $20,000 | 7,160 installs | $2.793296 CPI |
| Grocery App Y | $14,400 | 1,810 first orders | $7.955801 CPA |

Count ordering is a validation of this supplied dataset. It does not establish unique users, an event sequence or matched attribution cohorts. The script assumes non-zero denominators in these rows; it is not a general-purpose ingestion pipeline for arbitrary campaign data.

### Interpretation

Germany Android is the weak puzzle cell. Similar German CPMs and different outcome yields point toward investigation of loading, audience/device/placement composition and the opening interaction. They do not identify a single cause.

The grocery report compares US and Türkiye efficiency while requiring economics and service capacity before expansion. Revenue, margin, retention, campaign dates, attribution windows and targets were not supplied. No ROAS, profitability, statistical significance or population-level performance is inferred.

## 8. PDF engineering and packaging

`scripts/build_report.py` is a portable copy of the final production builder. It resolves the repository root from its own location, reads regenerated data from `data/` and uses bundled DejaVu fonts.

The builder uses ReportLab for a 1000 × 700-point landscape canvas, typographic hierarchy, tables, color treatments, screenshot placement, source links and outline navigation. It uses PyMuPDF to attach source bytes and save the final PDF with compression.

It writes:

- `output/pdf/draft.pdf`: ReportLab's pre-attachment intermediate.
- `output/pdf/Playable_Factory_Case_Study.pdf`: final report with attachments.
- `audit/report_toc.json`: page, section and title register.
- `audit/layout_warnings.json`: text, box and table overflow warnings.

The automated geometry checks flag text/table bounds and box overflow. Rendered page inspection checks visual issues beyond those heuristics, including legibility, screenshot proportions, title fit, spacing and page hierarchy. The final report recorded 43 pages, 56 attachments and no automated layout warnings.

## 9. Reproducibility package added for this handoff

This documentation handoff includes the detailed logs, revised master prompt and GitHub README, plus a portable builder, original calculation script, source files, screenshot assets, fonts, dependency versions, manifests and a verification utility.

The portable builder changes path resolution and font lookup; the report content and calculation method remain those of the final report. `scripts/verify_package.py` checks the registered source hashes, recalculated metrics and expected control totals. It can also inspect a supplied PDF's page and attachment counts.

The portable builder was executed successfully for this handoff. Its rebuilt report retained 43 pages, 56 attachments and zero automated layout warnings. Package verification passed for all 50 source hashes, 46 external records, eight raw rows and 18 derived rows; the rebuilt PDF’s embedded source hashes also matched. Documentation links were checked against the packaged files.

The package excludes temporary retrieval caches, application-specific upload helpers, intermediate revision scripts and conversation/session metadata. These are operational artifacts, not part of the research method or report dependency chain.

## 10. Maintenance and release discipline

For a revision, preserve original inputs, modify a working copy, regenerate calculations, update evidence dates where facts are time-sensitive, edit the builder and review the resulting PDF. Update the logs only with work actually performed.

Changing input files changes hashes. Changing report structure changes the table of contents and may require page-map updates. Additional source images change the registered-source count because the builder includes all PNGs in `upload/`. Those are deliberate release changes; update the manifests and documentation together.

The revised master prompt is a current instruction set for continuing or reproducing this case. It is not a reconstruction of historical prompts. The original prompts remain preserved as inputs.
