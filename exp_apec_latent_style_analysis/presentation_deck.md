# APEC — Reactivation Impact for Long-Dormant Clients

- Presenter: Sergio Oyola
- Presentation date: July 21, 2026
- Core question: does personalized email content meaningfully improve reactivation among clients who haven't checked out in 3+ years?
- Based on a sizing analysis for a potential live test, plus a look at actual send history for this population

# Executive Summary

- No clear case to run a full randomized test: APEC personalization roughly matches non-APEC marketing content overall, with no evidence it's helping the long-dormant population more than other campaign types.
- Population: about 9.8M clients dormant 3+ years — ample for any test design; population size isn't the constraint.
- The read (17 months): APEC (0.19%) sits below the pooled non-APEC average (0.31%), just under OTHER (0.20%), further below DSE (0.26%), and well below FLS (0.39%, a behaviorally-triggered category) — and far below the transactional-email artifact (7.45%, excluded from the comparison) — and the trend is degrading, not improving, with APEC's own rate roughly 2x lower in the final 7 months than the first 10.
- The cost of proof: baseline reactivation is only ~0.09%/month, so even a +15% lift would need ~1.66M clients and ~6 weeks, while a more realistic +5% lift would need ~14.3M clients and ~48 weeks — reinforcing that there's no clear case to run a full randomized experiment right now.

# Data Behind This Analysis

- **Campaign send history** — every email/push/SMS sent to a client, including whether it was opened, clicked, and whether it led to a purchase (`blueshift.campaign_activity_kpis`); analysis is restricted to sends that actually reached a client (excludes holdout/control-group records with no real delivery).
- **Client lifecycle history** — tracks each client's engagement state (Active / Lapsed / Dormant / Never Active) over time, so a client's status can be checked *as of a specific send* rather than only as of today (`curated.checkout_based_client_state_journal`).
- **Session data with campaign tracking** — links a website/app session back to the specific send that drove it, via matching tracking parameters (`curated.user_session_conversion_metrics`).
- **Purchase/demand confirmation** — confirms whether a tracked session actually led to a real purchase or styling request (`curated.client_reactivation_demand_events`).

# The Population: Clients Dormant 3+ Years

- This analysis focuses on clients with no checkout in more than 1,095 days (3+ years) — a deliberately stricter cut than StitchFix's standard "Dormant" bucket (any checkout gap over 365 days).
- For a personalization system that relies on a history of client behavior, a client who hasn't interacted with the product in years is the population where that behavioral history — and therefore the personalization itself — is most likely to be stale or unavailable, making this the most informative group to check whether personalization is pulling its weight.
- Within the full client base, Dormant 3+ years is a sizable group: 9,808,734 clients, compared to 2,101,175 in the broader Dormant bucket, 1,463,269 Active, 869,323 Lapsed, and 36,869,411 who have never checked out at all.
- This same population definition anchors every subsequent slide — the power analysis's eligible pool and the personalization-impact comparison's population are both this identical Dormant 3+ years group, evaluated as of each specific send rather than as of today.

Full client base by lifecycle bucket (chart-ready data):

| Lifecycle bucket | Definition (days since last checkout) | Clients |
|---|---|---|
| Active | ≤ 120 days | 1,463,269 |
| Lapsed | 121-365 days | 869,323 |
| Dormant | 366-1,095 days | 2,101,175 |
| Dormant 3+ yrs (this analysis's population) | > 1,095 days | 9,808,734 |
| Never Active | Never checked out | 36,869,411 |

# How We're Measuring Conversion

- A send only counts as producing a **reactivation** if the client visited via a session carrying that specific send's own tracking parameters (real click-through evidence, not just a coincidence) and that session is linked to an actual Fix request or direct-buy order — both within 7 days of the send.
- This click-through-confirmed standard is deliberately stricter than "any purchase within a window of the send": it trades away credit for real reactivations that happen through untracked paths (e.g. closing an email and returning later via the app with no tracked link) in exchange for not crediting a send with an unrelated, coincidental purchase.
- The same metric and 7-day window is used everywhere in this analysis — the power analysis's baseline rate and the personalization-impact comparison are built on this identical definition, so the two are directly comparable and neither one is measuring something different from the other.
- Because this standard requires a trackable click-through session, it's inherently conservative — only about 1.9% of eligible sends produce any UTM-matched session at all — which is why the baseline reactivation rate used for sizing is as low as it is, and why the required sample sizes and durations in the power analysis are as large as they are.

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

# APEC vs. Non-APEC Sends

- To get a reliable read without waiting months for a live test, this analysis looks at **516 days of actual send history (~17 months, January 2025 - May 2026)** for the same 3+-year-dormant population sized above — longer than the minimum duration for the +5%, +10%, or +15% designs above (335, 86, and 39 days respectively), though shorter than the +3% design's 920-day requirement.
- A client counts as **reactivated** by a send only if they clicked through to a tracked session tied to that specific send, and that session led to a real purchase or styling request within 7 days — a strict, click-through-confirmed standard. The TRANSACTIONAL category is excluded from this comparison since clients act on it because they're already returning, not because of marketing.
- APEC (personalized) sends reactivated **0.19%** of the 1,349,279 clients who received them; every other qualifying marketing send combined reactivated **0.31%** of the 4,308,183 clients who received them — roughly **1.6x higher** for non-personalized sends.
- That gap (0.12 percentage points, 95% CI 0.11-0.13 points) is still statistically significant (p < 0.0001), though far smaller than a surface-level comparison would suggest — and it holds up in 15 of the 17 months individually, not just pooled (APEC edges ahead in February and June 2025).

Sends are classified by campaign name — every campaign matching APEC's naming (including its confirmed browse-abandon and style-profile triggers) is labeled `APEC`; everything else is `non-APEC` (transactional email is filtered out of the population before this split).

Monthly reactivation rate, APEC vs. non-APEC (chart-ready data):

| Month | APEC reactivation rate | Non-APEC reactivation rate |
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

- Beyond the APEC-vs-everything split, sends break down into four other categories by campaign name: general marketing content (OTHER), Dynamic Shoppable Email (DSE), Freestyle Lifecycle Series (FLS — triggered by specific high-intent events like cart abandonment or a saved item going on sale), and transactional/account-service email (excluded from the Part 1 comparison but shown here for transparency).
- Across the full window, APEC's reactivation rate (0.19%) sits close to OTHER's (0.20%), below DSE's (0.26%), and well below FLS's (0.39%) — but that ordering partly reflects how often each category resends to the same clients. Normalizing to a per-month basis (client-months sent, not just distinct clients ever sent) flips DSE and OTHER: DSE resends to its base far more often, so per month sent, OTHER (0.03%) modestly edges out DSE (0.02%), which lands about even with APEC (0.02%).
- FLS leads on both views — full window and per month — consistent with how it's triggered: only after a client already shows high purchase intent, a fundamentally different targeting mechanism than APEC's broad-based personalization, so this isn't a like-for-like read on campaign quality.
- DSE and FLS are each a distinct, confirmed campaign program, not a naming-convention guess — DSE dynamically assembles shoppable product content, and FLS is behaviorally triggered — but neither uses APEC's CTSM-embedding-driven personalization, so their results are descriptive context, not proof of what personalization does or doesn't do.

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
- This shift lines up with the decline in APEC's own rate covered on a later slide — it isn't just that APEC looks worse next to FLS, its standing relative to OTHER and DSE has also fallen since mid-2025.
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

# APEC: Decline Over Time

- Looking at APEC by itself, not compared to other categories, its reactivation rate declines materially over the 17-month window: pooled at **0.0254%** across the first 10 months (January-October 2025) versus **0.0124%** across the final 7 (November 2025-May 2026) — roughly a **2.0x drop**.
- This isn't simply a shrinking-audience artifact: APEC's own send volume dropped sharply starting November 2025 (from roughly 856,000-960,000 clients/month down to about 200,000-211,000), but the one month volume unexpectedly recovered to its earlier size — March 2026, back up to 959,487 clients — still shows a similarly low rate (0.0139%), not a reversion to the earlier ~0.02-0.04% range.
- Noisy small samples from reduced reach don't explain the decrease either: the decline was already underway before the November 2025 volume drop — October 2025's rate (0.0083%) was already one of the lowest points in the first ten months.
- Whatever the specific cause, the practical takeaway holds either way: APEC's already-modest reactivation rate is not stable or improving over the window — it's degrading over time.

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

# Bottom Line: Is a Live Experiment Worth Running?

- Compared against genuine marketing categories, APEC (0.19%) sits just below OTHER (0.20%), further below DSE (0.26%), and well below FLS (0.39%, a behaviorally-triggered category) — and is still statistically below the pooled average across all qualifying non-APEC marketing sends (0.31%, p < 0.0001).
- This remains an observational comparison, not a randomized test: differences in who gets targeted, how often, or through which channel could explain part of the remaining gap, so it's an association, not proof that personalization *causes* worse (or better) outcomes.
- Baseline reactivation for genuine marketing sends to this population is just 0.09%/month, so confirming even a large +15% lift with a live randomized test needs ~1.66M clients and about 5.6 weeks, and a more realistic +5% lift needs ~14.3M clients and nearly a year (47.9 weeks).
- Given how costly a live test would be, and that the observational signal doesn't show APEC clearly underperforming across the board — it's close to OTHER, though below DSE and further below FLS — there isn't a clear case for running a full randomized experiment right now, but there also isn't strong observational evidence that personalization is helping, either.

---

## Images to add

None. Every chart referenced above (the monthly APEC-vs-non-APEC trend and the monthly category breakdown) is provided as chart-ready tabular data directly under its slide heading, so the add-in can build native, editable PowerPoint charts instead of embedding static images.
