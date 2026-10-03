# Task 3: direct evaluation protocol and non-gaming adaptation

## Exact artifacts to evaluate

These URLs were extracted from the manual's PDF link annotations, matched by vertical order to the three named playables. [S01, S12–S14]

| Playable | Exact URL |
|---|---|
| Squad Busters | https://home.playablefactory.com/preview?exportId=6a0300e942f7ff76c6a68d02 |
| Clean It! | https://home.playablefactory.com/preview?exportId=6a0300f742f7ff76c6a68d1c |
| All in Hole | https://home.playablefactory.com/preview?exportId=6a03010b42f7ff76c6a68d36 |

**Research limitation:** the text web reader could not access the interactive exports. No direct gameplay observations were made for this kit. The ideas below are inspection prompts, not findings. Use an interactive browser or a human recording to finish 3.1. Do not review a different playable with the same game title or substitute the full mobile game for this export.

## Observation workflow

1. Record exact URL, date, viewport, device/browser and whether the page loaded normally.
2. First run: behave like a new viewer without advance instructions. Record opening frame, first meaningful action, first feedback, progress, payoff and CTA.
3. Second run: try idle, incorrect input, boundary cases and replay. Note whether the creative helps or traps the user.
4. Capture at least opening, gameplay and end-card evidence. Include a short recording if timing matters.
5. Separate observed symptom, plausible cause and proposed remedy. A single device test cannot establish cross-device failure.
6. Select exactly three critical improvements per playable. Choose the most consequential issues, not three arbitrary aesthetic preferences.

If the link is unavailable, record the failure, request a recording/alternate export and continue other tasks. An unobserved placeholder is preferable to a fabricated evaluation, but it must remain flagged as incomplete before submission.

## Mechanics description template

“The player [input] to [immediate action], aiming to [goal]. Progress is communicated by [feedback]. The playable ends when [observed condition] and offers [observed CTA].” Fill only what the artifact shows. The original game's full systems are irrelevant unless the ad communicates them.

## Inspection prompts by title — not observed defects

| Title | Questions to investigate | Candidate remedy only if evidence supports it |
|---|---|---|
| Squad Busters | Is the first objective readable? Can the player distinguish controllable elements from combat effects? Does a choice produce understandable feedback? | Simplify first-action cue; sequence information; clarify outcome of a decision |
| Clean It! | Are interaction targets obvious? Does progress remain satisfying and visible? Is there a clear payoff rather than repetitive action without closure? | Make remaining task visible; shorten low-value repetition; align payoff and CTA |
| All in Hole | Does movement/collection behave as the viewer expects? Is progress/eligibility clear? Does the CTA arrive at a meaningful payoff? | Improve control feedback; explain collection constraints; revise pacing or end-card timing |

Do not assert a specific control scheme until it is observed. These title-informed questions may prove irrelevant; discard them freely.

## Improvement record

For each issue write: evidence timestamp/screenshot → user friction → proposed change → why it should help → metric/test → implementation cost/dependency. Example structure: “At 00:04 the instruction obscures the target on the tested viewport [evidence]. Move it into a reserved instruction zone; test first-success rate and accidental taps.” This is an illustrative format, not a real observation.

Prioritize by severity, frequency during observation, relevance to conversion, and confidence. Avoid claiming a redesign will improve CPI by a made-up percentage. For visual polish issues, explain the user consequence or drop them in favor of a more important problem.

## 3.2 proposed adaptation: collection mechanic for Picnic

Conditional on confirming that All in Hole's supplied playable is based on steering/collecting objects, retain collection, spatial feedback and a visible completion goal. Replace destructive/indiscriminate collection with purposeful grocery selection. If the supplied export uses a different mechanic, adapt the actual observed mechanic instead.

Proposed five-step flow:

1. Show a three-item dinner list and a clearly branded basket.
2. Guide the basket toward the first required ingredient with one simple cue.
3. Collect the other listed ingredients, confirming each match; irrelevant items trigger gentle feedback rather than punitive failure.
4. Show the completed meal basket and the convenience benefit.
5. Present an end card with “Explore Picnic” / approved first-order CTA and an explicit handoff to the real app journey.

**Kept:** collection loop, immediate feedback, progress and payoff. **Changed:** object semantics, visual tone, success condition, complexity and business CTA. The viewer should understand the grocery service, not merely enjoy a reskinned game. No fake delivery-time or price promise. [S20–S22 for brand basis; adaptation is original proposal]

## Submission shape

Three pages/slides for 3.1: one title, one mechanic summary, three numbered evidence-backed changes each. One for 3.2: brand, 3–5-step flow, CTA and explicit kept/changed comparison. Screenshots should be annotated lightly and refer to the exact export. No manual cap applies, but avoid a sprawling game-design critique.
