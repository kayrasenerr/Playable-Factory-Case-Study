# Task 5.1: qualification, seed list and research execution

## Required finished output

Exactly ten qualified prospects: five eligible independent/mid-size game companies, each with a casual/puzzle mobile app and recent US/European UA evidence; five distinct non-gaming companies with apps in one defined narrow vertical. Include company, app, fit, supporting source link, official website, company LinkedIn and first-contact role. [S01]

This file supplies researched candidates and a rigorous qualification process. It does **not** claim that the five gaming seeds below have proven recent UA. The downstream AI must finish that evidence collection or replace them.

## Narrow non-gaming vertical

Recommended definition: **app-based consumer grocery delivery services operating in European markets**. Include grocery-first services whether they fulfill from their own operations or partner supermarkets. Exclude restaurant-only delivery and general shopping apps without a distinct grocery offer. Count a corporate group once, not five country brands.

Why this vertical: repeatable basket/selection mechanics can demonstrate an actual customer task; first order is a concrete acquisition goal; service areas and repeat behavior create meaningful commercial nuance. It also makes the Task 5.2 grocery analysis useful background without pretending the fictional campaign is one of these companies.

## Research seeds and qualification status

| Gaming seed | App/game to investigate | Verified basis in this kit | Fit hypothesis | First role to investigate | Still required |
|---|---|---|---|---|---|
| Fugo | Words of Wonders | Official game list [S17] | Word mechanic is easy to demonstrate | Head of UA/Growth | Ownership/size, dated UA geo evidence, LinkedIn |
| Lessmore | Arrows – Puzzle Escape | Official site describes logic puzzle [S18] | Short spatial problem can be tried in an ad | UA Lead / Growth Lead | Ownership/size, store ID, dated UA geo evidence, LinkedIn |
| Peaksel | 100 Doors Games: Escape from School | Official game page [S19] | One room puzzle can preview a clear task | Head of Marketing / UA | Ownership/size, current store status, dated UA geo evidence, LinkedIn |
| Infinity Games | Select current puzzle title from official portfolio | Official portfolio retrieved [S29] | Simple calm puzzle could demonstrate core experience | Growth / Performance Marketing Lead | Exact app ID/title, ownership/size, dated UA geo evidence, LinkedIn |
| Metacore | Merge Mansion | Official game/support sources [S30] | Merge-to-renovation loop is visually demonstrable | Head of UA / Creative Strategy | Current ownership/scale eligibility, dated UA geo evidence, LinkedIn |

These are seeds, not a ranked recommendation. Metacore in particular needs a careful current scale/ownership check; replace it if it is too large for the brief's intent. Expand the longlist to 12–15 studios so five evidence-qualified companies remain after filtering. Do not stretch “mid-size” merely to keep a familiar name.

| Non-gaming seed | App to resolve | Basis | Fit hypothesis | First-contact role | Remaining checks |
|---|---|---|---|---|---|
| Picnic | Picnic | Official app/download pages [S20–S22] | Dinner-list/basket completion | Head of Growth / Performance Marketing | Store IDs, company LinkedIn, service area for pilot |
| Ocado Retail | Ocado | Official app help and company site [S23–S24] | Shop planning or range discovery | Performance Marketing Lead | Store IDs, exact buying entity, LinkedIn |
| Everli | Everli | Official app and service pages [S25–S26] | Personalized selection and shopper trust | Head of Growth | Store IDs, current operating markets, LinkedIn |
| Rohlik Group | One verified country app, e.g. Rohlik or Knuspr | Official group country list [S27] | Purposeful grocery collection | Country Growth/Performance Marketing Lead | Exact app/developer, service area, group/country buying scope, LinkedIn |
| Flink | Flink | Official grocery service site [S28] | Assemble a small useful essentials basket | Head of Performance Marketing | App listing, current entity/markets, LinkedIn |

Do not substitute a website service for the required app. A marketing page and an app-store listing should establish that each candidate actually has the named app. Different country brands in Rohlik count as one group-level prospect unless a separate legal/buying organization is explicitly justified; the safest final list uses five distinct groups.

## Gaming hard gates

1. Named casual/puzzle app exists and belongs to the company.
2. Current ownership and scale fit the manual's independent/mid-size intent. Exclude Zynga, Scopely and comparable large publishers, including obvious attempts to count their subsidiaries as independent studios.
3. Recent ad activity is observed in at least one US or European market.
4. Evidence identifies the app or advertiser clearly; similar titles do not qualify.
5. Official company website and correct company LinkedIn are resolved.

Working definition of recent: last 90 days ending on actual research date; explicitly label it as your operational definition because the manual does not specify a window. For this kit's date, use approximately 4 July–2 October 2026 and exact inclusive boundaries in the final query. If evidence is older, label it and replace the prospect rather than quietly extending the window.

## Evidence collection steps

Start from official company portfolio → store listing/app ID → corporate/ownership evidence → ad evidence. Use Sensor Tower ad observations if genuinely available; otherwise inspect Meta Ad Library or Google's Ads Transparency Center where coverage supports the app and market. Record advertiser/app match, visible ad ID, first/last-seen or active date, country/filter, network, URL and screenshot. [S15–S16, S31–S33]

A job opening in UA suggests capability, not active campaigns. A recent game update or high downloads does not prove paid acquisition. An active ad with no country information does not establish US/Europe activity. An empty library result does not prove the company is not advertising; coverage and advertiser naming can be incomplete.

Resolve LinkedIn via an official footer link or search, then verify page name, website domain and business description. Never construct a slug from the company name and assume it exists. Use company pages for the required field; Task 5.1 asks for a role, not a named individual or email.

## Ledger schema

Store prospect_id, company, parent_company, scale_rationale, app_title, store_id, OS, genre, target_market, ad_platform, ad_id, evidence_date_range, observation_date, source_url, screenshot_path, company_website, company_linkedin, contact_role, fit_reason, status and open_questions.

Status vocabulary: seed → identity_verified → eligibility_verified → UA_verified (gaming only) → submission_ready. If a hard gate fails, mark rejected with reason. Deduplicate by parent and store ID, not display name alone.

## Final table presentation

Use two tables of five. In the source field, include a compact dated evidence phrase, such as “US ad observed [date], [source]”; do not use a generic homepage as evidence of recent UA. Keep fit to one company-specific sentence. Put a short vertical rationale above the non-game table. Add the full evidence ledger as a supporting link if needed, but all required fields must remain readable in the main PDF.

## Copy-paste research prompt

“Find 12 candidate casual/puzzle mobile studios, then qualify five against current parent ownership/scale and dated US/Europe advertising in the last 90 days. Return source-backed identities and ad observations. Label missing evidence UNKNOWN. Do not infer UA from downloads, job postings or an updated app. Resolve company LinkedIn pages, not guessed slugs. If fewer than five qualify, continue research and report the exact missing gates rather than inventing rows.”
