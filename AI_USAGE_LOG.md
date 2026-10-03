# AI usage log — research, verification and report production

**Prepared by:** Kayra Şener  
**Project period:** 02–03 October 2026  
**Purpose:** Describe the human and AI contributions, the source workflow, a real weak-output correction and the verification supporting the final case.

## 1. Ownership and collaboration

I created the research tree, defined what the source files should contain and how they should be organized, and selected the companies and transferable features. I read and analyzed the gathered research, supplied commercial and product insights, played the three ads and reviewed each stage. My creative additions came from my game experience and industry understanding, supported by the project's evidence.

AI was a substantial collaborator in research and production. GPT 5.6 Sol mainly contributed data gathering and summarization. GPT Astra contributed web research, source-file completion, technical elaboration, reporting, visuals, structure and live revisions. I used Astra at high usage for research and at medium-to-high usage for report production. These roles overlapped across the project.

I initiated, approved and finalized the manual intervention logs. Their first-person wording and the report's wording were prepared with AI assistance. I retained responsibility for the analysis, judgments, creative direction, review and finalization.

## 2. Tool and model roles

| Tool / model | Actual use | Output / boundary |
| --- | --- | --- |
| GPT 5.6 Sol | Mainly data gathering and summarization | Research material and summaries supporting the case |
| GPT Astra 6 | Research, source completion, reporting, technical detail, visuals, structuring and revisions | Final analytical narrative and report production support |
| NotebookLM | Initial source-database and summarization workflow | Summaries passed into the initial Cowork workflow |
| Claude Cowork | Initial report workflow using NotebookLM's source summaries | This report was discarded because its source detail was insufficient |
| Web search and page retrieval | Product/company research, app identity, prospect qualification and technical reference checks | Source-linked claims and dated evidence; no proof of spend from an ad listing alone |
| Python standard library | Raw-data validation, aggregation, ratios and reconciliation | Deterministic calculation outputs; separate from AI interpretation |
| ReportLab | PDF typography, tables, vector wireframe, layout and screenshot placement | Designed report pages |
| PyMuPDF | PDF inspection, source attachments, packaging and compression | Traceable PDF with embedded evidence |
| Image rendering and inspection | Page previews, screenshot sequences and layout review | Visual QA supporting the export |

The documentation package also uses a portable copy of the production builder and a deterministic verification script. These packaging utilities were added for this handoff.

No Sensor Tower API was called. The Task 5.3 section is a proposed workflow under the case brief's API-access assumption. No acquisition campaign, budget reallocation or outreach was executed.

## 3. Research workflow and production history

### Stage 1 — Structure the research

I set the research tree and source-file requirements. AI assisted in translating the brief into task-specific research directions, a source collection and a requirement-to-output map. This established the expected deliverables before report drafting.

### Stage 2 — Gather and analyze evidence

AI helped research the web, collect data, summarize material and fill source files. Official product/company sources established capabilities and identity. App-store and company-profile records supported prospect matching. Dated geographic ad observations supported the gaming prospect screen.

I read and analyzed the collected material. I used it to select the commercial direction and transferable features and to develop the insights that drove the report.

### Stage 3 — Improve source access

I initially uploaded all sources to NotebookLM and connected it to Claude Cowork to reduce context overhead. The summaries did not give Cowork enough detail for the case. I discarded that report, moved the source files into this report's project and worked directly with Astra.

This was the project's concrete weak-result correction: a summary-mediated source workflow was insufficient for detailed reporting. The correction changed how sources were supplied, rather than adding unsupported detail to the draft.

### Stage 4 — Supply first-hand gameplay evidence

I played Squad Busters, Clean It! and All in Hole, documented their exact flows and provided screenshots from start to finish. AI used my descriptions to organize mechanics, timing, sound and redirection observations. It inspected the screenshots for art and visible UI.

My descriptions are the basis for gameplay behavior in the report. AI did not conduct the playthrough on my behalf. My criticism and creative ideas were developed into prioritized recommendations with implementation considerations and test measures.

### Stage 5 — Recalculate and interpret campaign data

AI-assisted Python work rebuilt all ratios from the supplied eight raw rows. Campaign, geography and OS totals use summed counts. The regenerated 18 derived rows were compared with the supplied metric file.

I interpreted the commercial implications and finalized the investigation and testing priorities. Deterministic arithmetic establishes the ratios; it does not establish the causes of the observed segment differences.

### Stage 6 — Produce and inspect the report

AI assisted the report's structure, wording, vector wireframe, technical tables, screenshot selection, source registration, file hashes and source attachments. Rendered-page checks and automated geometry warnings supported layout refinement.

I reviewed the report and supporting statements and finalized them. The final presentation uses first-person or neutral language and a concise division-of-labor account.

## 4. Task-by-task contribution record

| Task | AI-assisted work | My contribution | Verification basis |
| --- | --- | --- | --- |
| 1 — Commercial strategy | Product research, synthesis, onboarding structure, proposed measurement framework and wireframe production | Company/feature selection, commercial interpretation and final concept direction | Official product sources; proposed claims labeled as concepts and tests |
| 2 — Ready proposal | Current-capability research, proposal organization, MVP detail and measurement/QA considerations | Approval of the direction and final rationale | Ready's documented customization and A/B baseline; discovery questions for the proposed extension |
| 3 — Playable review | Organization of mechanics, screenshot inspection, technical wording and validation measures | Playthrough, descriptions, criticism, screenshots and creative insight | My descriptions and supplied image sequences for the exact exports |
| 4 — Banners | Copy drafting and presentation of three static/automatic visual concepts | Industry/creative insight, review and first-test priority | Product truth, format requirements and a proposed test design |
| 5.1 — Prospects | Company/app matching, source collection, profile and ad-evidence research, table organization | Research direction, vertical choice and interpretation of fit | Official identity sources plus dated geographic ad observations |
| 5.2 — Campaign reports | Calculations, aggregation, reconciliation and diagnostic presentation | Commercial interpretation and final investigation priorities | Original PDF, checked transcription and reproducible script |
| 5.3 — Workflow | Structuring retrieval, identity matching, role research, prompts and QA design | Review of the proposed process and limits | Sensor Tower capability reference; no actual API execution |
| 5.4 — AI disclosure | Organization of workflow, contribution tables and first-person wording | Confirmation and finalization of my contribution history | My account of the cross-tool workflow and the production artifacts |

## 5. Research and verification controls

### Product facts and recommendations

Source-backed capability claims were separated from proposed creative treatments and product extensions. Ready's existing customization and variant workflows inform the proposed goal-aware setup; the proposal does not claim basic A/B testing as new.

A public page's silence is not sufficient evidence that a capability is absent. Proposed improvements are framed with an intended mechanism and a validation approach, rather than a guaranteed uplift.

### Prospect qualification

The five gaming leads have app-specific recent ad observations in the US or Europe. The research distinguished acquisition evidence from app popularity, updates and store geography. Company-profile size bands remain self-reported.

The final prospect list is a research shortlist. Budget owner, buying entity, current organizational structure and sales readiness are matters for discovery before outreach.

### Arithmetic

The raw PDF represents eight horizontally split rows. Recalculation generated 18 derived rows. The builder compared the regenerated and supplied values at a numeric tolerance of `1e-12`.

Campaign totals reconcile to $20,000 / 7,160 installs and $14,400 / 1,810 first orders. Average time was not aggregated because its measurement base is unspecified. Missing revenue, margin, retention and attribution details were not filled with assumptions.

### Visual and source QA

The PDF records 43 pages, 50 registered source inputs, 46 external references and 56 attachments. Source bytes are identified by full SHA-256 hashes. Rendered-page inspection supported screenshot and layout checks; automated layout warnings were empty for the final export.

A hash establishes file identity, not the accuracy of every statement in that file. An attachment preserves a research input, not automatic endorsement of a research guide's suggestions.

## 6. Manual intervention records

Four separate rationale files cover company pairing, Ready approval, the first banner test and the first campaign investigation. I initiated, approved and finalized these logs; AI assisted their wording.

They explain the reasons behind my judgments without implying unaided authorship. The report includes the commercial and analytical reasoning in its relevant sections; the individual logs provide additional context.

## 7. Prompt documentation

Two original master-prompt copies remain preserved in the source collection. `MASTER_PROMPT_REVISED.md` is a newly prepared instruction set reflecting the finalized evidence, company choices, gameplay findings, report style and reproducibility workflow.

The revised prompt is intended for future revision or reproduction. It is not represented as a verbatim prompt used earlier. Prompt screenshots and conversation-sharing links will be supplied separately; this log records tool use and contribution without inventing those records.

## 8. Limits of the record

This is a project-level account of research and production, not a message-by-message transcript. Model names and cross-application roles follow the workflow I described. Exact token consumption, elapsed task durations and detailed model routing were not measured in this log.

The deterministic scripts and packaged artifacts support inspection of the calculations, source identity and production method. They cannot independently reconstruct every search or conversation across the applications used.
