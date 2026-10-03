# Task 2: Ready goal-aware experiment setup and QA

## Product choice and verified baseline

Choose **Ready**. Public documentation already describes customizable templates, asset/difficulty changes and duplication/A/B testing. Data separately advertises analytics and heatmaps. The improvement below is a proposed connected workflow; its absence in the actual product is unconfirmed. Phrase it as “extend Ready with…” and explain what you would validate in a demo. [S04, S07]

## Problem hypothesis

Teams can produce attractive variants without a consistent definition of success, event denominators or a checked destination. A game team may optimize clicks instead of valuable installs; a grocery team may select an engagement-heavy template without defining first-order conversion. This is a plausible discovery hypothesis, not a finding from customer interviews.

## Proposed feature

**Goal-aware launch checklist and experiment brief**, embedded before export:

1. Select business outcome: install, first order, sign-up or an explicitly named custom event.
2. Select audience/market and destination type; record whether conversion measurement is available.
3. Map a standard playable event schema to the template's actual states.
4. Define one test hypothesis and the precise difference between variants.
5. Preview the entire handoff, validate CTA/destination configuration and inspect event coverage.
6. Export a versioned creative and a short experiment brief with metric definitions, caveats and ownership.

Do not promise native attribution integration in the MVP. A manual downstream-results import can be enough to establish the workflow; real connectors can follow when access and matching are clear.

## Both client types

| Element | Game client | Grocery client |
|---|---|---|
| Selected goal | Install | First order |
| Diagnostic events | Tutorial success, error/retry, level completion, CTA | Correct item choice, basket completion, offer view, CTA |
| Primary outcome | CPI with retention guardrail | First-order CPA with margin/repeat guardrail |
| Handoff check | Store/deep link fits OS and market | Destination handles serviceability and new versus existing user |
| Useful experiment | Clearer first action | Benefit framing and shorter basket task |

## MVP and non-goals

MVP: goal selector; event mapping; variant/hypothesis record; destination checks; report brief export; warning for unavailable downstream attribution. Initial implementation can use a few templates, not all formats.

Exclude automated budget allocation, inferred user identity, universal MMP connectors and AI-generated claims of a winning creative. Missing performance data must result in “insufficient evidence,” not a synthetic recommendation.

## Implementation detail for a credible proposal

Data model: project_id, creative_id, version_id, experiment_id, goal_type, target_market, OS, destination, event_schema_version and measurement_status. Each event needs a timestamp, session-scoped identifier where permitted, step and event name. Distinguish unique-session stage reach from repeat clicks. Snapshot the experiment configuration at export so later edits do not silently change the interpretation of prior data.

QA rules: verify required fields; flag mismatched market/OS destination; replay standard success and idle paths; detect missing first-interaction or completion events; ensure intentional CTA click; produce a clear warning if first-order/install data cannot be joined. Do not claim the feature can inspect every external checkout or guarantee attribution.

## Validation plan

Discovery: show the workflow to gaming UA and non-gaming performance/brand users. Ask them to prepare a real campaign brief and identify missing steps. Baseline their current time, tracking issues and handoff problems before promising improvement.

Pilot: compare brief-to-QA-approved-export time, proportion of exports with complete event definitions, and tracking/CTA defects found after launch. These are product adoption and process metrics. Campaign CPI/CPA is a secondary business outcome influenced by many factors; it cannot alone prove that the workflow feature works.

Ship gate: users can produce an interpretable experiment brief, warnings are actionable, and event validation does not create misleading confidence. Stop or simplify if the wizard increases setup time without preventing meaningful errors.

## Prioritization and trade-offs

High-value first: event definitions and destination QA, because mistakes invalidate learning. Next: reusable brief presets. Later: downstream integrations and automated insight summaries. The trade-off is additional setup friction; mitigate with defaults and progressive detail, while preserving explicit measurement limitations.

## One-page proposal layout

Top: “Ready: from fast creative production to measurable experiments.” Left: the customer problem and current baseline. Center: four-step mock flow (goal → event map → QA → experiment brief). Right: gaming versus grocery examples. Footer: MVP, success metrics, dependency and pilot ask. Label 2.1 and 2.2. Avoid turning it into a multi-page PRD in the submission; this file is the supporting detail.
