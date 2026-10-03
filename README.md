# Playable Factory — Product Manager Case Study

A product-management case study prepared by **Kayra Şener**, with AI-assisted research, analysis and report production.

The case connects a genuine product benefit, a short playable interaction and a measurable commercial outcome. It covers commercial strategy for Fugo and Picnic, a Ready product proposal, three playable reviews, a non-game adaptation, display banners, prospect research and campaign analysis.

**Research and production period:** 02–03 October 2026.

## Reading guide

Start with the case-study PDF in the repository root for the complete analysis, recommendations, wireframe and research appendix. The supporting files explain the workflow, evidence and contribution behind the report.

| File | Purpose |
| --- | --- |
| [DEVELOPER_LOG.md](./DEVELOPER_LOG.md) | Detailed account of research architecture, task implementation, calculations, report production and verification |
| [AI_USAGE_LOG.md](./AI_USAGE_LOG.md) | Model/tool roles, task-by-task contributions, the source workflow and AI-assisted checks |
| [MASTER_PROMPT.md](./MASTER_PROMPT.md) | Instructions for working with the case materials and continuing the research/reporting workflow |
| [Research workflow and production history](./logs/Research_Workflow_and_Production_History.md) | Project history, source handling and division of labor |
| [Research and verification log](./logs/Research_and_Verification_Log.md) | Evidence scope, numerical controls and verification methods |

## Folder structure

| Location | Contents and purpose |
| --- | --- |
| Repository root | Case-study PDF, developer log, AI usage log, master prompt and this README |
| [descriptions/](./descriptions/) | My written playthrough descriptions of the three playable ads |
| [logs/](./logs/) | Research workflow, production history and verification records |
| [screenshots/](./screenshots/) | Gameplay screenshots organized by playable |
| [sources/](./sources/) | Case manual, research guides, source register, calculation tables, campaign metrics and calculation script |

## Gameplay evidence

I played the three ads and documented their mechanics, progression, timing and end behavior. The descriptions provide the basis for behavioral observations; screenshots support the visual and interface assessment.

| Playable | Description | Screenshots |
| --- | --- | --- |
| Squad Busters | [squad_busters_description.txt](./descriptions/squad_busters_description.txt) | [Squad Busters sequence](./screenshots/squad%20busters/) |
| Clean It! | [clean_it_description.txt](./descriptions/clean_it_description.txt) | [Clean It sequence](./screenshots/clean%20it/) |
| All in Hole | [all in hole description.txt](./descriptions/all%20in%20hole%20description.txt) | [All in Hole sequence](./screenshots/all%20in%20hole/) |

The report develops exactly three proposed changes per playable, with rationale and validation measures. Its Picnic adaptation translates the collection-and-growth interaction into gathering ingredients for dinner.

## Source and guideline map

The numbered Markdown files organize the research by task. They document research directions, methods and production guidelines. Source-backed findings and the final recommendations are presented in the case-study report.

| File | Purpose |
| --- | --- |
| [00_README_PROMPT.md](./sources/00_README_PROMPT.md) | Overview of the research materials and execution approach |
| [01_Case_Requirements.md](./sources/01_Case_Requirements.md) | Task scope, output limits and requirement mapping |
| [02_Market_and_Product_Context.md](./sources/02_Market_and_Product_Context.md) | Playable Factory capabilities and commercial/product context |
| [03_Task_1_Prospecting_and_Onboarding.md](./sources/03_Task_1_Prospecting_and_Onboarding.md) | Company selection, client approach and onboarding guidance |
| [04_Task_1_Concept_and_Wireframe.md](./sources/04_Task_1_Concept_and_Wireframe.md) | Concept development and screen-flow specification |
| [05_Task_2_Product_Improvement.md](./sources/05_Task_2_Product_Improvement.md) | Ready proposal, implementation scope and validation guidance |
| [06_Task_3_Playable_Evaluation.md](./sources/06_Task_3_Playable_Evaluation.md) | Playable evaluation protocol and non-game adaptation guidance |
| [07_Task_4_Banner_Concepts.md](./sources/07_Task_4_Banner_Concepts.md) | Static/animated display-banner concepts and format requirements |
| [08_Task_5_1_Prospect_Research.md](./sources/08_Task_5_1_Prospect_Research.md) | Prospect qualification rules, candidate research and evidence fields |
| [09_Task_5_2_Calculated_Tables.md](./sources/09_Task_5_2_Calculated_Tables.md) | Campaign and segment metrics in readable audit tables |
| [10_Task_5_2_Analysis_and_Reports.md](./sources/10_Task_5_2_Analysis_and_Reports.md) | Campaign interpretation, metric selection and report guidance |
| [11_Task_5_3_AI_Workflow.md](./sources/11_Task_5_3_AI_Workflow.md) | Proposed Sensor Tower + AI prospecting workflow |
| [12_Task_5_4_AI_Log.md](./sources/12_Task_5_4_AI_Log.md) | Guidance for documenting actual AI use and human contribution |
| [13_Delivery_and_QA.md](./sources/13_Delivery_and_QA.md) | Presentation, numerical, evidence and layout checks |
| [14_Sources_and_Evidence.md](./sources/14_Sources_and_Evidence.md) | Preparation-stage source register and verification scope |
| [PF_Product_Manager_Case_Study.pdf](./sources/PF_Product_Manager_Case_Study.pdf) | Original case brief and deliverable requirements |
| [manual_extracted.txt](./sources/manual_extracted.txt) | Text extraction of the case manual for reading and navigation |
| [campaign_metrics.csv](./sources/campaign_metrics.csv) | Machine-readable metrics at campaign-cell, total, geography and OS levels |
| [recalculate.py](./sources/recalculate.py) | Python calculation logic used to validate counts, aggregate observations and derive campaign ratios |

## Research and calculation method

The analysis uses official product/company material, app records, company profiles and dated advertising observations. Product facts inform the creative concepts; proposed improvements include a mechanism and a way to test the intended benefit.

Gaming prospect qualification considers casual/puzzle fit, app/publisher identity, studio scale and recent US/European acquisition-ad observations. The non-gaming vertical is app-based online grocery shopping and home delivery in Europe. Ad observations are acquisition signals; company-profile size bands are self-reported.

Campaign analysis uses eight supplied campaign × geography × operating-system observations. The calculation script produces 18 derived rows covering the original cells and campaign, geography and OS aggregates. Total ratios use summed numerators and denominators.

| Campaign | Spend | Outcomes | Total cost per outcome |
| --- | ---: | ---: | ---: |
| Puzzle Game X | $20,000 | 7,160 installs | $2.793296 CPI |
| Grocery App Y | $14,400 | 1,810 first orders | $7.955801 CPA |

The reports distinguish descriptive results, possible explanations and recommended tests. Historical efficiency informs investigation and bounded experiments. Proposed playable events and downstream quality measures explain how a real pilot could be evaluated.

## Workflow and contribution

I created the research tree and source-file requirements, selected the companies and transferable features, analyzed the evidence, played the ads and supplied commercial and creative insights. I reviewed each stage and finalized the report and manual intervention logs.

GPT 5.6 Sol mainly supported data gathering and summarization. GPT Astra supported research, source completion, technical elaboration, report structure, writing, visuals and revisions. I initially used NotebookLM with Claude Cowork as a source-summary workflow, then moved to direct source files with Astra to retain the detail needed for the report.

AI assisted wording and production. I retained responsibility for the analysis, judgments, creative direction, review and finalization. The [AI usage log](./AI_USAGE_LOG.md), [developer log](./DEVELOPER_LOG.md) and [research history](./logs/Research_Workflow_and_Production_History.md) provide the detailed account.
