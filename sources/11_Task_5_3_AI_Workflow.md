# Task 5.3: repeatable Sensor Tower-assisted prospecting

## Evidence and scope

The brief assumes API access and an assistant that can call it. This kit did not query Sensor Tower. Public Connect material confirms API/data-delivery capabilities; its public MCP page also describes assistant access subject to an API subscription. Specific endpoints, fields, limits and entitlements must come from the actual account documentation/tool schema, not invented code. [S31–S32]

## Proposed workflow

1. **Compile a typed research brief.** Genre/subgenre, OS, target countries, trailing date window, download range, ad-recency requirement and publisher exclusions. Clarify whether minimum downloads apply per market, OS or globally; use explicit units and inclusive boundaries.
2. **Query licensed app data.** Retrieve store/app IDs, app names, genre, publisher/developer IDs, downloads by date/country/OS and available advertising observations. If a requested ad field or market is unavailable, return UNKNOWN and queue manual verification.
3. **Normalize and filter in code.** Apply numerical predicates deterministically; resolve duplicates across OS and store IDs; map current parent ownership. Preserve raw response provenance and query parameters. Do not let the language model silently change thresholds to get ten results.
4. **Resolve organizations.** Match store publisher/developer to official website and company LinkedIn using public sources. Confirm domain, app portfolio and company identity; parent/publisher/developer may be different organizations.
5. **Find relevant professional contacts.** Identify current UA, Growth or Creative Strategy leaders using public professional/official sources. Match company, current role and territory, and attach evidence and confidence. Leave name unknown when unresolved; a role recommendation is still useful. Do not guess personal emails.
6. **Human review and export.** Reject ambiguous ownership, stale employment or unsupported country activity. Export a prospect table plus evidence ledger and rejected-record reasons. Schedule reruns with a run ID; alert on new/changed candidates rather than generating duplicates.

## Data contract

`run_id, queried_at, window_start, window_end, app_id, store, app_name, genre, publisher_id, publisher_name, parent_company, country, downloads_estimate, ad_activity_type, ad_first_seen, ad_last_seen, ad_country, ad_source, website, company_linkedin, contact_name, contact_role, contact_source, confidence, status, rejection_reason`.

Field names above are a proposed internal schema, not Sensor Tower endpoint field names. Numerical estimates are not ground-truth installs. An unavailable ad observation is not zero ad activity.

## Example prompts

**Query planning:** “Find casual/puzzle games on iOS and Android with estimated downloads in [range] in [countries] over [dates], plus observed advertising there within 90 days. Use only available licensed tools. Show exact filters, coverage gaps and publisher exclusions before querying.”

**Entity resolution:** “For each returned publisher, find the official website and company LinkedIn. Verify the app portfolio or store publisher match; keep developer, publisher and parent separate. Cite every match and leave unresolved rows unknown.”

**Contact research:** “Identify the current person responsible for UA/Growth for each verified company, using public professional sources. Return role, territory, source date and confidence; do not infer a person from an old press release or guess an email.”

**QA:** “Audit for stale roles, duplicate parents, wrong app IDs, unsupported geographic ad claims and missing source dates. Do not repair missing evidence with plausible text. Return an exception queue.”

## Reliability implementation

Use schema validation, pagination, bounded retries/backoff, request logging, caching by parameters and idempotent upserts. Preserve raw data separately from AI summaries. Separate tools for numeric retrieval, web evidence and summarization. API keys stay in secret storage; they do not belong in prompts or exported logs. Human review precedes any outreach; this case asks for a workflow, not sending messages.

## Risks and decisions

Coverage and estimated data may miss activity; ownership changes can invalidate eligibility; LinkedIn may be inaccessible; employment can be stale; AI entity matching can confuse similar names. API access does not imply unrestricted access to contacts. Product claims about integrations do not guarantee your subscription has every dataset.

A good failure is a specific exception with a next action. A bad failure is an apparently complete list with invented data. Record confidence per fact, not one reassuring score per company.

## Half-page submission draft structure

Aim for roughly 200–250 words, then verify the actual exported half-page footprint. Use five compact sentences/steps covering filters, data retrieval, organization matching, contacts and QA; add two short example prompts and one risks sentence. Detailed schemas belong in supporting material, not the half-page answer. The page limit is physical, not a word-count exemption.
