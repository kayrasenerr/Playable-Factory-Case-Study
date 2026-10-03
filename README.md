# Playable Factory — Product Manager case study

Research, analysis and report-production package prepared by **Kayra Şener**, with AI-assisted research and production.

The case demonstrates how a genuine product benefit can become a short playable experience and be evaluated against a commercial outcome. It covers Fugo/Words of Wonders and Picnic, a Ready product proposal, three playable reviews, banners, ten prospects and two campaign reports.

Research cutoff: **03 October 2026**. The final report has **43 pages**, **50 registered source inputs**, **46 external references** and **56 embedded attachments**.

## Start here

| Reader / purpose | File |
| --- | --- |
| Recruiter reviewing the case | The separately supplied `Playable_Factory_Case_Study.pdf` |
| Understanding implementation and verification | [Developer log](docs/DEVELOPER_LOG.md) |
| Understanding AI use and my contribution | [AI usage log](docs/AI_USAGE_LOG.md) and [contribution statement](docs/Contribution_Statement.md) |
| Reviewing the project history | [Research workflow and production history](docs/Research_Workflow_and_Production_History.md) |
| Reviewing the concise audit account | [Research and verification log](docs/Research_and_Verification_Log.md) |
| Continuing the project with AI | [Revised master prompt](MASTER_PROMPT_REVISED.md) |
| Reproducing calculations and PDF production | The commands and script map below |

The supplied archive contains the documentation, original inputs, screenshots, calculation code, portable PDF builder, fonts and audit records. The final PDF is distributed separately and can be regenerated from this package. This is a repository-ready folder, not an already published GitHub repository.

## Project purpose and division of labor

I designed the research tree and source-file requirements, selected companies and transferable features, analyzed the evidence, played the ads, supplied insights and creative direction, reviewed each stage and finalized the report and manual intervention logs.

GPT 5.6 Sol mainly supported data gathering and summarization. GPT Astra supported research, source completion, technical elaboration, report writing, structure, visuals and revisions. NotebookLM and Claude Cowork were used in an initial summary-mediated workflow; I discarded that report and worked directly from the source files with Astra because more detail was needed.

AI assisted the wording and production. The logs describe this collaboration and distinguish human judgment, AI synthesis and deterministic verification.

## Repository layout

| Path | Role |
| --- | --- |
| `README.md` | Navigation, file/script purposes, reproduction and maintenance guidelines |
| `MASTER_PROMPT_REVISED.md` | Current AI instruction set for revision or reproduction |
| `docs/` | Detailed logs and concise supporting statements |
| `project_sources/` | Original numbered manual, data, guides and gameplay descriptions |
| `upload/` | Original master-prompt copy and gameplay PNGs used by the builder |
| `data/` | Working raw CSV, recalculation script and regenerated metrics |
| `scripts/` | Portable report builder and package verifier |
| `assets/fonts/` | DejaVu font files used by the builder and their license notice |
| `audit/` | Source hashes, external evidence records, page map and recorded layout warnings |
| `output/manual_intervention/` | Four rationale logs and the process-history input embedded in the report |
| `output/pdf/` | Generated draft and final PDFs; created by the builder |
| `requirements.txt` | Captured versions of the installed PDF-production dependencies |

Generated PDF files and local environments are excluded by `.gitignore`. The archive does not include retrieval caches, session metadata, upload credentials or application-specific transfer helpers.

## Source-file map

The numeric prefix is the exact filename prefix in `project_sources/`. Original guide titles retain their task numbering.

| Prefix / file | Purpose | Use |
| --- | --- | --- |
| 01 — `recalculate.py` | Original calculation implementation | Preserved reference; run the working copy in `data/` |
| 02 — `campaign_raw.csv` | Eight-row transcription of the raw PDF | Preserved numeric source |
| 03 — `campaign_metrics.csv` | Supplied 18-row derived-metric file | Reconciliation reference |
| 04 — `Task_5_2_Raw_Campaign_Data.pdf` | Primary campaign-data snapshot | Authority for supplied values |
| 05 — `PF_Product_Manager_Case_Study.pdf` | Original task manual | Authority for requirements and limits |
| 06 — `manual_extracted.txt` | Manual text extraction | Reading/navigation aid |
| 07 — `MASTER_PROMPT-1-.md` | Original execution prompt | Historical input |
| 08 — `11_Task_5_3_AI_Workflow.md` | Sensor Tower-assisted workflow guide | Task 5.3 research/architecture direction |
| 09 — `08_Task_5_1_Prospect_Research.md` | Prospect criteria and seeds | Qualification method |
| 10 — `07_Task_4_Banner_Concepts.md` | Banner research and format guidance | Task 4 creative direction |
| 11 — `06_Task_3_Playable_Evaluation.md` | Exact exports and observation protocol | Task 3 evaluation structure |
| 12 — `00_README.md` | Original research-kit overview | Historical guide to preparation |
| 13 — `09_Task_5_2_Calculated_Tables.md` | Supplied rounded calculation tables | Audit reference |
| 14 — `12_Task_5_4_AI_Log.md` | Original AI-log preparation guide | Disclosure structure |
| 15 — `13_Delivery_and_QA.md` | Output limits and QA guidance | Production checks |
| 16 — `14_Sources_and_Evidence.md` | Original S-series source register | Preparation-stage evidence context |
| 17 — `01_Case_Requirements.md` | Scope and requirement mapping | Deliverable traceability |
| 18 — `05_Task_2_Product_Improvement.md` | Ready improvement guide | Proposal development |
| 19 — `10_Task_5_2_Analysis_and_Reports.md` | Campaign interpretation guide | Report structure and denominator rules |
| 20 — `04_Task_1_Concept_and_Wireframe.md` | Concept and screen-flow specification | Wireframe development |
| 21 — `02_Market_and_Product_Context.md` | Product/capability research guide | Commercial/product baseline |
| 22 — `03_Task_1_Prospecting_and_Onboarding.md` | Company selection and onboarding guide | Task 1 commercial approach |
| 23 — `clean_it_description.txt` | My Clean It! playthrough description | Gameplay mechanics, timing and behavior |
| 24 — `all-in-hole-description.txt` | My All in Hole playthrough description | Gameplay mechanics, sound and behavior |
| 25 — `squad_busters_description.txt` | My Squad Busters playthrough description | Gameplay mechanics and reward flow |

Guides are preserved research inputs. Their suggested concepts and company seeds are not a substitute for the final evidence ledger.

The report's F-series file IDs are assigned by the builder; they do not correspond directly to these numeric prefixes. For example, F23 is the top-level original prompt copy, while F24–F26 are the three gameplay descriptions. Use `audit/source_manifest.json` for exact F-ID mappings.

## Audit and context files

| File | Purpose |
| --- | --- |
| `audit/source_manifest.json` | Exact F01–F50 mapping, paths, byte sizes, SHA-256 hashes and uses |
| `audit/external_evidence_ledger.json` | E01–E46 source URLs, publishers, supported claims, scope and dates |
| `audit/report_toc.json` | Final report page/section/title map |
| `audit/layout_warnings.json` | Automated geometry-warning result from the final production export |
| `docs/DEVELOPER_LOG.md` | Extensive source architecture, implementation, calculations, production and maintenance account |
| `docs/AI_USAGE_LOG.md` | Extensive model/tool use, task contributions, workflow history and verification account |
| `docs/Research_Workflow_and_Production_History.md` | Concise cross-tool process history |
| `docs/Research_and_Verification_Log.md` | Concise evidence and numerical-control record |
| `docs/Contribution_Statement.md` | My contribution and AI-assistance disclosure |
| `output/manual_intervention/manual_intervention_log_01_task_1_brand_choice.md` | Company-pairing rationale |
| `output/manual_intervention/manual_intervention_log_02_task_2_ready_approval.md` | Ready proposal rationale |
| `output/manual_intervention/manual_intervention_log_03_task_4_banner_priority.md` | First banner-test rationale |
| `output/manual_intervention/manual_intervention_log_04_task_5_campaign_priority.md` | First campaign-investigation rationale |

The process-history copy in `output/manual_intervention/` is one of the report's registered inputs. The copy in `docs/` provides reader-facing navigation. Keep them synchronized if the process account changes.

## Script map and execution behavior

| Script | Reads | Writes / checks |
| --- | --- | --- |
| `data/recalculate.py` | `data/campaign_raw.csv` | Overwrites `data/campaign_metrics.csv`; writes root-level `09_Task_5_2_Calculated_Tables.md`; prints campaign controls |
| `scripts/build_report.py` | Source files, images, working CSVs, rationale/history files and fonts | Creates `output/pdf/draft.pdf` and final PDF; updates TOC and layout-warning JSON |
| `scripts/verify_package.py` | Working/supplied CSVs, manifest, source bytes, evidence ledger, TOC and warning JSON | Validates fixed-case invariants; optional `--pdf` inspects PDF pages, attachments and embedded source hashes |

The recalculation script uses the Python standard library. The report builder requires ReportLab, PyMuPDF and Pillow. The verifier uses the standard library unless its optional PDF check is requested.

The original prefix-named calculation script expects unprefixed CSV names beside itself, so run `data/recalculate.py` instead of executing the preserved copy in `project_sources/`.

## Reproduce the calculations

Use Python 3; the production runtime was Python 3.12. Run these commands from the repository root:

```bash
python data/recalculate.py
python scripts/verify_package.py
```

Expected controls:

| Campaign | Spend USD | Conversions | Total cost per conversion |
| --- | ---: | ---: | ---: |
| Puzzle Game X | 20,000 | 7,160 installs | 2.793296 CPI |
| Grocery App Y | 14,400 | 1,810 first orders | 7.955801 CPA |

The verifier checks eight raw rows, 18 unique derived rows, all 50 source hashes, 46 evidence records, the 43-page recorded map and an empty recorded geometry-warning list. It does not re-open external websites or independently validate source truth.

## Rebuild and inspect the PDF

Install the captured dependency versions:

```bash
python -m pip install -r requirements.txt
python scripts/build_report.py
python scripts/verify_package.py --pdf output/pdf/Playable_Factory_Case_Study.pdf
```

The builder writes the PDF and prints page, attachment, warning and byte-size information. It uses bundled fonts and resolves paths relative to the repository, without the original workspace path.

For visual inspection with Poppler installed:

```bash
mkdir -p audit/rendered
pdftoppm -scale-to 1400 -png output/pdf/Playable_Factory_Case_Study.pdf audit/rendered/page
```

Inspect the rendered pages for clipping, legibility, table spacing, screenshot proportions and source-footnote placement. Automated bounds checks support this review; they do not replace it.

A rebuilt PDF can differ byte-for-byte because metadata and library serialization vary. Verify its content, source hashes, calculations, page map and attachment inventory rather than expecting an identical file hash.

## Research and revision guidelines

Use the manual for requirements and the raw PDF for campaign values. Use my descriptions for gameplay behavior and screenshots for visible states. Use official sources for identity/capabilities and dated ad observations for UA qualification.

Keep the original inputs unchanged. Calculate from working copies. Record source access dates and observation dates separately. Refresh time-sensitive ownership, product, market and ad facts when updating the cutoff.

Ratios use summed counts, not averaged row percentages. Average time has an unspecified measurement base and is not aggregated. The dataset supplies no revenue, retention, margin, campaign dates or attribution window. Interpret differences descriptively until event/cohort definitions and causal factors are tested.

The revised master prompt is current revision guidance; original prompts are historical inputs. Update logs with actual work only. The report and personal statements use first-person or neutral language and concise, complete analytical reasoning.

When inputs or report structure change, update manifests, ledgers, page maps, logs and documentation together. The builder includes every PNG in `upload/`, so adding images changes the source inventory and may change register pages.

## Sharing and scope

The package is designed for recruiter review and technical inspection. It does not perform external publication, recruiter submission, prospect outreach or campaign execution. Sensor Tower access is assumed only in the proposed workflow; no API call was made.

The original brief and data were supplied for a recruitment case. Confirm their redistribution terms before making the complete inputs public. No general reuse license is granted for third-party source documents or screenshots. The bundled font notice covers the font files.

Prompt screenshots and conversation links are handled separately. This package is a project-level production record, not a complete cross-application conversation transcript.
