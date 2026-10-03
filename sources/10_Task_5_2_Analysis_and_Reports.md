# Task 5.2: research-grade analysis and client report implementation

## Source handling and limitations

S02 is a two-page horizontal split of eight rows, not sixteen records. Page 1 gives identity/spend/impressions; page 2 continues each row with engagement and conversion fields. Both pages were rendered and visually checked before transcription. See `data/campaign_raw.csv`; run `python data/recalculate.py` from this folder to rebuild outputs. The source PDFs remain in `sources/`.

No campaign dates, creative IDs, networks, audience definitions, attribution windows, unique-user definitions, retention, revenue, order value, margin or benchmark targets are supplied. The data supports descriptive comparison, not a causal claim that geography/OS or a particular creative caused performance differences. Do not invent a reporting week or label the results statistically significant.

All spends are explicitly USD. Do not convert the Türkiye rows into TRY. Puzzle conversions are installs; grocery conversions are first orders. There is no grocery install count, so no grocery CPI or install-to-first-order rate can be calculated.

## Metric dictionary

| Metric | Formula | Use and caveat |
|---|---|---|
| CPI / first-order CPA | spend / conversions | Primary efficiency metric; conversion differs by client |
| CPM | 1,000 × spend / impressions | Separates media price from response efficiency |
| Load rate | playable_loads / impressions | Delivery/technical diagnostic, not unique-user reach |
| First interaction rate | first_interaction / playable_loads | Opening clarity/interest diagnostic |
| End-card reach among interactors | end_card_reached / first_interaction | Progression diagnostic; not necessarily gameplay completion |
| End-card click ratio | cta_clicks / end_card_reached | Useful only as a stage ratio; clicks may occur before end-card if design permits |
| CTR | cta_clicks / impressions | Explicit impression denominator |
| Conversion per click | conversions / cta_clicks | Descriptive aggregate ratio; not proof all conversions are click-attributed |
| IPM / orders per thousand | 1,000 × conversions / impressions | Outcome yield from exposure |
| CPC | spend / cta_clicks | Secondary diagnostic; omit from main report if it adds clutter |

Multiply ratios by 100 when displaying percentages. Aggregate using sums of numerators and denominators, not mean row percentages or mean row CPAs. `avg_time_sec` has no supplied base: do not average it across rows or claim a weighted mean without stating and verifying the population. Show the row-level times only if they help diagnose a specific issue. Longer time could mean interest or friction.

Counts decline monotonically in each supplied row, but this does not prove a deduplicated sequential funnel. Treat “drop-off” as a provisional stage diagnostic until event definitions and cohort matching are confirmed. Ask whether repeat sessions/clicks, view-through conversions and asynchronous attribution are included.

## Report A: Puzzle Game X

### Recommended headline

“7,160 installs at $2.79 CPI; Germany Android is the main efficiency concern.”

### Audited evidence

- Total spend $20,000; 1,085,000 impressions; 7,160 installs; $2.79 CPI; 6.60 installs per 1,000 impressions.
- Germany Android CPI $5.10 versus Germany iOS $2.40. Their CPMs are very similar ($19.26 vs $19.33), while install yield differs sharply (3.78 vs 8.07 per 1,000 impressions).
- Germany Android load rate 87.41%, interaction/load 51.69%, end-card/interactor 47.54%; Germany iOS 94.00%, 68.79%, 59.79% respectively. Weakness appears before the click as well as afterward.
- US Android CPI $2.55 is lower than US iOS $2.75 despite lower install yield. Its cheaper CPM ($16.05 vs $20.00) helps explain that result. “iOS is better everywhere” would be false.

### Interpretation, clearly bounded

The near-equal German CPMs make impression cost alone an inadequate explanation for that OS gap. The provided stage ratios suggest investigating delivery and early interaction on Android, alongside targeting and measurement differences. They do not prove an Android software bug or a German translation issue.

### Exactly three proposed recommendations

1. **Diagnose Germany Android before broad expansion.** Break results down by device, network, creative version and day; test load behavior and first-action clarity. Owner: UA lead with creative QA. Success: improved install yield/CPI under comparable traffic, without worse retention.
2. **Run a bounded incremental-spend test in Germany iOS and/or US Android.** These cells have the lowest observed CPI; choose based on available audience and quality. Do not assume historical average CPI holds at additional spend. Set stop rules against an agreed CPI and retained-player threshold.
3. **Instrument early progression and validate player quality.** Add first-success latency, tutorial completion, retry/error and exit-step events. Link creative-level results to retained-player or value cohorts only where permitted and reliable.

### Missing metrics to request

Inside playable: time to first interaction; time to first successful action; step reach/exit; wrong inputs/retries; actual task completion; CTA position/timing; load duration/error rate. Each needs a denominator and a defined unique-session policy. Outside playable: D1/D7 retention, meaningful in-game progression, revenue/value and attribution settings. Keep the two categories separate because the manual specifically asks for in-playable metrics.

### One-page layout

Headline; three KPI cards (spend, installs, CPI); four-row geo×OS table with CPI and IPM; two concise diagnosis bullets; small missing-metrics box; final three recommendations. A footer should say “Period not supplied; descriptive comparison; attributed installs.” Keep full technical ratios in the appendix/research sheet. Explain in one line that CPI/IPM were chosen for acquisition efficiency; CPM/funnel ratios diagnose it; CPC and mean playtime were left out of the main view to reduce duplication and ambiguous interpretation.

## Report B: Grocery App Y

### Recommended headline

“1,810 first orders at $7.96 CPA; the US carries most spend at much higher acquisition cost.”

### Audited evidence

- Total spend $14,400; 760,000 impressions; 1,810 first orders; first-order CPA $7.96.
- US: $12,500 spend, 1,000 orders, $12.50 CPA. Türkiye: $1,900 spend, 810 orders, $2.35 CPA.
- US accounts for 86.81% of spend and 55.25% of orders. Türkiye accounts for 13.19% of spend and 44.75% of orders.
- US CPM $22.32 versus Türkiye $9.50; orders per 1,000 impressions 1.79 versus 4.05. Both media cost and observed response efficiency contribute to the gap.
- Türkiye iOS has the lowest first-order CPA ($1.73); US Android the highest ($14.72).
- Türkiye Android click-to-order ratio (6.04%) is below US Android (6.43%), despite its much lower CPA. Do not claim every Türkiye funnel stage is stronger.

### Interpretation, clearly bounded

Türkiye is a promising measured acquisition pocket, but profitability and scale are unknown. Basket values, subsidies, market maturity, delivery economics and audience mix could differ. A recommendation to move all US spend would ignore marginal CPA, operational capacity and the client's strategic market priorities.

### Exactly three proposed recommendations

1. **Validate economics and service capacity before a controlled Türkiye iOS expansion.** Check net contribution after discounts/delivery and repeat orders. Test additional spend in steps against a first-order CPA and quality ceiling agreed with the client.
2. **Investigate the US Android journey.** Review early interaction and end-card progression, then the real landing/app/order handoff. Test a clearer benefit-led opening and a shorter path separately where feasible. Low observed conversion does not identify which mechanism is broken.
3. **Connect creative intent to first-order and repeat-order measurement.** Add basket-task completion, selected category, offer visibility and CTA events; inspect downstream serviceability, checkout and payment exits in the actual app. Label app events as downstream, not events inside the playable.

### Missing metrics to request

Inside playable: basket task step progression; correct/incorrect selections; list completion; benefit/offer exposure; CTA view and click by location; time-to-complete; load errors; exit stage. Avoid treating simulated item choice as a real purchase preference without validation.

Outside playable: service-area eligibility, landing/deep-link success, app install if needed, signup, checkout start, first completed order, cancellations/refunds, discount cost, contribution margin and second order within a defined interval. A fictional “first order” may need definition: placed, paid or fulfilled? Confirm before modeling business value.

### One-page layout

Headline; spend/orders/CPA cards; US versus Türkiye comparison; four geo×OS CPA rows or bars; one bounded implication; missing playable metrics; final three recommendations. Explain that first-order CPA and volume are prioritized because the goal is orders, not installs. CTR and interaction are diagnostic. Omit ROAS/profitability because revenue and cost inputs are absent; never fill them with benchmarks as if observed.

## Optional opportunity sizing — do not put unqualified forecasts in reports

An analyst may calculate a constant-efficiency scenario, such as hypothetical incremental spend divided by observed CPA. Label it a mechanical scenario, not a forecast, and show why it is fragile. Prefer a controlled budget test to reporting a made-up number of “extra orders.” The brief can be answered well without any counterfactual forecast.

## Final arithmetic QA

Check original row values, campaign totals and ratio denominators. Show money to two decimals, rates to one or two decimals, counts as integers. Do not compare grocery CPA directly to gaming CPI as if they are the same business outcome. Do not infer significance from large impression counts when experimental design and event independence are unknown.
