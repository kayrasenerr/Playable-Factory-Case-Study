# Task 1.3–1.4: concept and mockup implementation

## Proposed concept: Picnic “Tonight's dinner, basket sorted”

This is an original concept recommendation, not an existing Picnic campaign. Brand foundation: Picnic's app supports grocery shopping and recipes. [S20–S22]

**Objective:** acquire first orders from new customers in verified delivery areas. Diagnostic outcomes: interaction, list completion, CTA click and successful handoff. Do not count a simulated basket as a real order.

**Target audience:** adults planning household meals who value convenient grocery shopping. This is a proposed audience; avoid unsupported age/income precision. Launch-market assumption: Netherlands, with Dutch final copy reviewed for natural phrasing.

**Key message:** simplify moving from a dinner idea to the groceries needed. Keep the message tied to a real app benefit. Any “one tap” claim, delivery promise or incentive must match the actual flow and offer terms.

**Core interaction:** tap three highlighted ingredients from a small shelf to complete an illustrative meal basket. Prefer forgiving tap targets over precise drag-and-drop. Estimated creative duration of roughly 10–20 seconds is a design target to test, not a benchmark.

## Frame-by-frame wireframe specification

| Frame | What appears | User action | Feedback and next state | Instrumentation |
|---|---|---|---|---|
| A: invitation | Brand mark; headline “Dinner sorted?”; three-item list; simple shelf | Tap a gently highlighted first item | Item moves to basket; first success is immediate | playable_ready, first_interaction, first_success |
| B: progress | List shows 1/3 complete; remaining items clear; persistent product identity | Tap two remaining ingredients | Checkmarks and short motion confirm each selection; wrong tap gets gentle guidance | item_selected, incorrect_tap, step_complete |
| C: payoff | Completed illustrative basket and meal image | No extra action required | “Your dinner essentials, together” transitions to end card | task_complete, end_card_view |
| D: end card | Brand and benefit; clear “Explore Picnic” or approved first-order CTA; terms if applicable | Tap CTA | Explicit navigation only after intentional click | cta_click with position/version |
| E: handoff | Real destination selected for installed/new-user state | Continue real service flow | Serviceability, registration and actual shopping occur outside the simulated ad | landing_view/deep_link_result; first_order downstream |

Frame E can be a small annotation beside the main four frames. It still needs to show what happens after the click. End-card copy can name the intended action without pretending the order has already been placed.

## States the mockup must resolve

- Initial instruction must make sense with sound off.
- After idle time, repeat a hint without auto-redirecting.
- A wrong tap should not trap the user or force repeated failure.
- Make progress visible without demanding that a viewer read a paragraph.
- Use persistent brand cues so entertainment does not obscure the advertiser.
- Put a real button and distinguish it from game objects; avoid fake system UI.
- Keep close controls and network-owned overlays unobstructed.
- Use text labels as well as color; show a static/reduced-motion design option.

## Visual delivery

Create one slide with four portrait frames, then a compact handoff note. Use rectangles, labels and a consistent basket/shelf illustration; the manual asks for a basic mockup, so expensive rendering is unnecessary. Add arrows between states and short annotations under each. Export it into the main PDF so reviewers can understand it without visiting another tool.

If creating a clickable prototype, isolate the simulated task from the real destination. Use only an approved test link. The prototype is optional; a production ad-network package is outside the required scope.

## Proposed experiment

Test a benefit-led invitation versus a challenge-led invitation while holding assets and steps stable. Primary outcome: attributed first-order CPA within comparable acquisition cohorts. Diagnostic measures: first-interaction/load, task completion/interaction, CTA/impressions. Guardrails: first-order margin and repeat-order rate where available. If only the playable is instrumented, call it a creative usability test, not proof of customer acquisition lift.

## Alternative gaming concept

If choosing Words of Wonders for 1.3, show a small authentic letter-selection task, one satisfying word discovery, a glimpse of the next challenge and an install CTA. Verify the actual game interaction first. Keep the same five-stage structure but change the business objective to installs with retention quality. Do not show impossible moves or advertise a mini-game that misrepresents the product.

## Acceptance checklist

The final slide must answer: who is this for, what does the viewer do, what benefit do they learn, what happens on success/failure/idle, what does the CTA do, and how will the concept be judged? Label it 1.4. The objective, audience and message must also be explicitly labeled 1.3 elsewhere in Task 1.
