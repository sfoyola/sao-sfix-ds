# CTSM Embeddings for Long-Dormant Clients

- Presenter: Sergio Oyola
- Presentation date: [ADD DATE]
- Core question: is it worth continuing to generate CTSM embeddings — the representations that power APEC's personalization — for clients who've been dormant 3+ years?
- Based on a sizing analysis for a potential live test, plus a review of existing send history for this population

# Executive Summary

- The question at hand: is it worth continuing to generate CTSM embeddings specifically for clients who've been dormant 3+ years?
- A live experiment isn't a practical way to answer this directly: even a moderate +5% relative lift in reactivation would need about 48 weeks to confirm, and a more conservative +3% lift would take over two and a half years — timelines out of step with how quickly this resourcing decision needs to be made.
- Existing send history for this population doesn't show APEC's personalized reactivation rate standing out above other marketing content (APEC 0.19% vs. 0.31% pooled across all other qualifying sends), and APEC's own rate for this specific population has trended down over the period observed — roughly 2x lower in the final 7 months than the first 10 — directional evidence, not proof, but consistent with no clear, demonstrated payoff yet from continued investment here.
- Recommendation: don't continue generating fresh CTSM embeddings for long-dormant clients on the current basis; use a substitute in the meantime (e.g. the average CTSM embedding for the client's business line) until there's a practical way to establish real incremental impact.

# Data Behind This Analysis

- **Campaign send history** — every email/push/SMS sent to a client, including whether it was opened, clicked, and whether it led to a purchase (`blueshift.campaign_activity_kpis`); analysis is restricted to sends that actually reached a client (excludes holdout/control-group records with no real delivery).
- **Client lifecycle history** — tracks each client's engagement state (Active / Lapsed / Dormant / Never Active) over time, so a client's status can be checked *as of a specific send* rather than only as of today (`curated.checkout_based_client_state_journal`).
- **Session data with campaign tracking** — links a website/app session back to the specific send that drove it, via matching tracking parameters (`curated.user_session_conversion_metrics`).
- **Purchase/demand confirmation** — confirms whether a tracked session actually led to a real purchase or styling request (`curated.client_reactivation_demand_events`).

# The Population: Clients Dormant 3+ Years

- This population is defined as clients with no checkout in more than 1,095 days (3+ years) — a stricter cut than the standard "Dormant" bucket (any gap over 365 days).
- CTSM embeddings are built from a client's accumulated behavioral history. For clients who haven't interacted with the product in years, that history — and therefore the resulting embedding — is the one most likely to be stale or effectively missing, which is exactly why continued embedding generation is worth scrutinizing for this specific group.
- Within the full client base, this group is sizable: 9,808,734 clients, compared to 2,101,175 in the broader Dormant bucket, 1,463,269 Active, 869,323 Lapsed, and 36,869,411 who have never checked out at all.
- This population definition is used consistently throughout — both for sizing a potential live test and for reviewing existing send history.

Full client base by lifecycle bucket (chart-ready data):

| Lifecycle bucket | Definition (days since last checkout) | Clients |
|---|---|---|
| Active | ≤ 120 days | 1,463,269 |
| Lapsed | 121-365 days | 869,323 |
| Dormant | 366-1,095 days | 2,101,175 |
| Dormant 3+ yrs (this analysis's population) | > 1,095 days | 9,808,734 |
| Never Active | Never checked out | 36,869,411 |

# How We're Measuring Conversion

- A send only counts as producing a **reactivation** if the client visited via a session carrying that specific send's own tracking parameters (real click-through evidence, not just a coincidence), and that session is linked to an actual Fix request or direct-buy order — both within 7 days of the send.
- This click-through-confirmed standard is a meaningful signal but not a perfect one: a tracked click doesn't prove the send caused the visit (the client may have been about to return regardless), and the absence of a tracked click doesn't rule out a real effect that happened through an untracked path. This limitation applies equally to every campaign type, not just one.
- The same metric and 7-day window is applied consistently across every comparison in this analysis, so results are directly comparable to one another.
- Because this standard requires a trackable click-through session, it's inherently conservative — only about 1.9% of eligible sends produce any matched session at all — which is part of why the baseline reactivation rate used for sizing is so low.

# Sizing a Hypothetical Live Experiment

- Eligible population: clients with no checkout in more than 1,095 days (3+ years) — about **9,808,734 clients**, more than enough to support any test design; population size is not the constraint.
- Baseline reactivation rate for this population, restricted to genuine marketing sends (transactional/account-service email is excluded — see the next slide), is just **0.09%** in a given month — genuine marketing-driven reactivation is very rare, which drives up the sample size and time needed to detect a real effect.
- Design assumptions: 50/50 split, single treatment-vs-control comparison, 95% confidence (two-sided), 80% power.
- Even a large +15% relative lift would take about 5.6 weeks to confirm; a more realistic +5% lift would take nearly a year (47.9 weeks), and a +3% lift would take over two and a half years (131.4 weeks).

| Target relative lift | Clients needed per arm | Total clients needed | Minimum duration |
|---|---|---|---|
| +3% | 19,607,644 | 39,215,288 | 920 days (131.4 weeks) |
| +5% | 7,128,232 | 14,256,464 | 335 days (47.9 weeks) |
| +10% | 1,825,481 | 3,650,962 | 86 days (12.3 weeks) |
| +15% | 830,623 | 1,661,246 | 39 days (5.6 weeks) |

# Why Transactional Email Is Excluded From the Marketing Comparison

- Transactional campaigns (password resets, order/Fix status confirmations) convert at **7.45%** — a data artifact, not a campaign effect — but only because the client is already logging in or checking an order, not because of marketing content.
- With transactional email set aside, APEC (0.19%) sits modestly below all genuine non-APEC campaigns combined (0.31%).

Reactivation rate: transactional email vs. genuine marketing (chart-ready data):

| Category | Reactivation rate |
|---|---|
| Transactional email | 7.4502% |
| Non-APEC | 0.31% |
| APEC | 0.1862% |

# What Existing Send History Suggests

- Beyond APEC, this population also received a range of other marketing content, plus a small number of transactional/account-service messages (password resets, order status updates, and similar). Those account-service messages are excluded from this comparison since a client only receives one because they're already returning on their own, not because of any marketing choice.
- Across the remaining marketing content sent to this population, APEC's directly-attributed reactivation rate (0.19%) does not stand out as higher than the rest combined (0.31%) — a modest, not dramatic, difference.
- This is a direct-attribution, observational comparison, not a controlled measurement of any one campaign's true incremental effect: different campaign types can reach different sub-segments of clients, at different frequencies, through different channels, and a tracked click doesn't prove causation either way.
- Combined with the cost of confirming impact through a live test, this send history doesn't provide evidence that continued CTSM embedding generation is paying off for this specific population today.

Reactivation rate, APEC vs. all other marketing content combined (chart-ready data):

| Group | Clients sent | Reactivated | Reactivation rate |
|---|---|---|---|
| APEC (personalized) | 1,349,279 | 2,513 | 0.19% |
| All other marketing content | 4,308,183 | 13,212 | 0.31% |

Monthly reactivation rate, APEC vs. all other marketing content combined (chart-ready data):

| Month | APEC reactivation rate | Other marketing content |
|---|---|---|
| 2025-01 | 0.0390% | 0.0494% |
| 2025-02 | 0.0260% | 0.0186% |
| 2025-03 | 0.0247% | 0.0390% |
| 2025-04 | 0.0230% | 0.0490% |
| 2025-05 | 0.0338% | 0.0379% |
| 2025-06 | 0.0366% | 0.0306% |
| 2025-07 | 0.0081% | 0.0413% |
| 2025-08 | 0.0198% | 0.0377% |
| 2025-09 | 0.0351% | 0.0796% |
| 2025-10 | 0.0083% | 0.0536% |
| 2025-11 | 0.0135% | 0.0396% |
| 2025-12 | 0.0068% | 0.0557% |
| 2026-01 | 0.0114% | 0.0885% |
| 2026-02 | 0.0085% | 0.0675% |
| 2026-03 | 0.0139% | 0.0878% |
| 2026-04 | 0.0152% | 0.0701% |
| 2026-05 | 0.0123% | 0.0663% |

# How Other Campaign Types Compare

- Beyond APEC, sends to this population break down into three other categories by campaign name: general marketing content (OTHER), Dynamic Shoppable Email (DSE), and Freestyle Lifecycle Series (FLS — triggered by specific high-intent events like cart abandonment or a saved item going on sale) — plus transactional/account-service email, tracked separately since a client only receives one because they're already returning on their own, not due to any marketing choice.
- Across the full window, APEC's reactivation rate (0.19%) sits close to OTHER (0.20%), below DSE (0.26%), and further below FLS (0.39%) — but that ordering partly reflects how often each category resends to the same clients. Normalizing to a per-month basis (client-months sent, not just distinct clients ever sent) flips DSE and OTHER: DSE resends to its base far more often, so per month sent, OTHER (0.03%) modestly edges out DSE (0.02%), which lands about even with APEC (0.02%).
- FLS leads on both views — full window and per month — consistent with how it's triggered: only after a client already shows high purchase intent, a different mechanism than APEC's broad-based personalization, so this is descriptive context on the send-history landscape, not a recommendation to favor one campaign type over another.
- DSE and FLS are each a distinct, confirmed campaign program, not a naming-convention guess — but neither uses APEC's CTSM-embedding-driven personalization, so their results don't speak to APEC's personalization specifically.

Reactivation rate by category, full window and per month sent (chart-ready data):

| Category | Clients sent (full window) | Reactivated (full window) | Reactivation rate (full window) | Client-months sent | Reactivated (month-sum) | Reactivation rate (per month sent) |
|---|---|---|---|---|---|---|
| OTHER | 4,295,781 | 8,417 | 0.1959% | 25,458,014 | 8,458 | 0.0332% |
| DSE | 1,846,336 | 4,740 | 0.2567% | 19,901,339 | 4,752 | 0.0239% |
| APEC | 1,355,921 | 2,591 | 0.1911% | 11,088,071 | 2,601 | 0.0235% |
| TRANSACTIONAL | 586,498 | 43,695 | 7.4502% | 717,086 | 43,963 | 6.1308% |
| FLS | 36,294 | 142 | 0.3912% | 64,221 | 144 | 0.2242% |

Column notes: the "full window" columns count each client once, however many months they were sent or reactivated. "Client-months sent" and "Reactivated (month-sum)" count a client once per month they were sent or reactivated, so "Reactivation rate (per month sent)" reflects the odds in a typical month rather than cumulative odds across the full 17-month window.

# Category Performance Over Time

- Among these categories, **FLS** leads every single one of the 17 months observed among genuine marketing categories — consistent with it being triggered only after a client already shows high intent, rather than sent broadly like the others.
- Among OTHER, DSE, and APEC, the ranking shifts over time: **APEC** led both in 5 of the first 6 months (January-June 2025), but hasn't led either since — sitting lowest of the three in 9 of the last 11 months (July 2025-May 2026).
- This shift lines up with the decline in APEC's own rate covered on the next slide.
- These monthly rates look far smaller than the pooled full-window rates on the previous slide by design, not by error: the pooled rate reflects a client's cumulative odds of reactivating *anytime* across the window, while each monthly rate reflects just that one month's odds. FLS stays closer between the two views because those clients typically only appear in the data for a month or two of the 17, unlike OTHER/DSE/APEC, which resend to nearly the same client base almost every month.
- As with the pooled comparison, this month-by-month view is descriptive context on existing send history, not a controlled measurement of incremental impact for any category.

Chart excludes TRANSACTIONAL (7.45%) to keep marketing categories readable. Monthly reactivation rate by category (chart-ready data):

| Month | OTHER | TRANSACTIONAL | DSE | APEC | FLS |
|---|---|---|---|---|---|
| 2025-01 | 0.0290% | 7.1702% | 0.0236% | 0.0394% | 0.3022% |
| 2025-02 | 0.0116% | 9.9624% | 0.0172% | 0.0263% | 0.1577% |
| 2025-03 | 0.0241% | 10.0746% | 0.0172% | 0.0252% | 0.2127% |
| 2025-04 | 0.0276% | 8.8915% | 0.0245% | 0.0238% | 0.3153% |
| 2025-05 | 0.0213% | 8.8242% | 0.0171% | 0.0345% | 0.2476% |
| 2025-06 | 0.0176% | 7.4246% | 0.0153% | 0.0370% | 0.1509% |
| 2025-07 | 0.0256% | 7.1940% | 0.0184% | 0.0085% | 0.2160% |
| 2025-08 | 0.0236% | 7.7776% | 0.0171% | 0.0199% | 0.1229% |
| 2025-09 | 0.0711% | 7.7296% | 0.0153% | 0.0354% | 0.2220% |
| 2025-10 | 0.0356% | 7.4312% | 0.0217% | 0.0086% | 0.1630% |
| 2025-11 | 0.0240% | 7.3217% | 0.0200% | 0.0154% | 0.2080% |
| 2025-12 | 0.0356% | 1.2283% | 0.0255% | 0.0102% | 0.2303% |
| 2026-01 | 0.0516% | 7.9914% | 0.0488% | 0.0142% | 0.1760% |
| 2026-02 | 0.0410% | 9.0722% | 0.0317% | 0.0099% | 0.1825% |
| 2026-03 | 0.0472% | 8.8130% | 0.0484% | 0.0146% | 0.1548% |
| 2026-04 | 0.0465% | 7.9191% | 0.0272% | 0.0184% | 0.4396% |
| 2026-05 | 0.0386% | 2.7391% | 0.0328% | 0.0141% | 0.2330% |

# APEC's Own Trajectory

- Looking at APEC's own reactivation rate for this population over time, independent of any comparison to other campaign types, it declines across the 17-month window observed: pooled at **0.0254%** across the first 10 months (January-October 2025) versus **0.0124%** across the final 7 (November 2025-May 2026) — roughly a **2.0x** difference.
- This isn't simply a smaller-audience effect: APEC's send volume dropped from roughly 856,000-960,000 clients/month down to about 200,000-211,000 partway through the window, but the one month volume unexpectedly returned to its earlier size (March 2026, 959,487 clients) still showed the same lower rate (0.0139%), not a return to the earlier ~0.02-0.04% range.
- The decline was already visible before that volume change, too — October 2025's rate (0.0083%) was already among the lowest observed while volume was still at its earlier, higher level.
- Whatever the specific driver, APEC's reactivation rate for this population has not been stable or improving over the period observed.

APEC monthly send volume and reactivation rate, standalone (chart-ready data):

| Month | Clients sent | Reactivated | Reactivation rate |
|---|---|---|---|
| 2025-01 | 887,518 | 346 | 0.0390% |
| 2025-02 | 880,829 | 229 | 0.0260% |
| 2025-03 | 881,344 | 218 | 0.0247% |
| 2025-04 | 877,113 | 202 | 0.0230% |
| 2025-05 | 876,548 | 296 | 0.0338% |
| 2025-06 | 874,597 | 320 | 0.0366% |
| 2025-07 | 855,777 | 69 | 0.0081% |
| 2025-08 | 864,858 | 171 | 0.0198% |
| 2025-09 | 906,793 | 318 | 0.0351% |
| 2025-10 | 959,734 | 80 | 0.0083% |
| 2025-11 | 200,492 | 27 | 0.0135% |
| 2025-12 | 204,860 | 14 | 0.0068% |
| 2026-01 | 210,125 | 24 | 0.0114% |
| 2026-02 | 210,878 | 18 | 0.0085% |
| 2026-03 | 959,487 | 133 | 0.0139% |
| 2026-04 | 210,740 | 32 | 0.0152% |
| 2026-05 | 211,014 | 26 | 0.0123% |

# Bottom Line: The CTSM-Embedding Recommendation

- A live experiment isn't a practical way to resolve this question: even a moderate +5% lift would take about 48 weeks to confirm, and a more conservative +3% lift would take well over two years — timelines that don't fit a resourcing decision that needs to be made now.
- Existing send history for this specific population doesn't show APEC's personalized rate standing out above other marketing content (0.19% vs. 0.31% pooled), and APEC's own rate for this population has trended down over the period observed — roughly 2x lower in the final 7 months than the first 10 — directional evidence, not proof, but consistent with no clear, demonstrated payoff yet from continued investment here.
- This finding is specific to the long-dormant (3+ year) population, where the behavioral history CTSM embeddings depend on is most likely to be stale — it is not a broader statement about APEC's value for other populations, and not a comparison against any specific other campaign.
- Recommendation: don't continue generating fresh CTSM embeddings for long-dormant clients on the current basis; use a substitute in the meantime (e.g. the average CTSM embedding for the client's business line) until there's a practical way to establish real incremental impact.

---

## Images to add

None. Every chart referenced above is provided as chart-ready tabular data directly under its slide heading, so the add-in can build native, editable PowerPoint charts instead of embedding static images.
