# CTSM Embeddings for Long-Dormant Clients: An Investment Question

- Presenter: Sergio Oyola
- Presentation date: [ADD DATE]
- Core question: is it worth continuing to generate CTSM embeddings — the representations that power APEC's personalization — for clients who've been dormant 3+ years?
- Based on a sizing analysis for a potential live test, plus a review of existing send history for this population

# Executive Summary

- The question at hand: is it worth continuing to generate CTSM embeddings specifically for clients who've been dormant 3+ years?
- A live experiment isn't a practical way to answer this directly: even a moderate +5% relative lift in reactivation would need about 48 weeks to confirm, and a more conservative +3% lift would take over two and a half years — timelines out of step with how quickly this resourcing decision needs to be made.
- Existing send history for this population doesn't show APEC's personalized reactivation rate standing out above other marketing content, and APEC's own rate for this specific population has trended down over the period observed — directional evidence, not proof, but consistent with no clear, demonstrated payoff yet from continued investment here.
- Recommendation: don't continue generating fresh CTSM embeddings for long-dormant clients on the current basis; use a substitute in the meantime (e.g. the average CTSM embedding for the client's business line) until there's a practical way to establish real incremental impact.

# Data Behind This Analysis

- **Campaign send history** — every email/push/SMS sent to a client, including whether it was opened, clicked, and whether it led to a purchase (`blueshift.campaign_activity_kpis`); analysis is restricted to sends that actually reached a client (excludes holdout/control-group records with no real delivery).
- **Client lifecycle history** — tracks each client's engagement state (Active / Lapsed / Dormant / Never Active) over time, so a client's status can be checked *as of a specific send* rather than only as of today (`curated.checkout_based_client_state_journal`).
- **Session data with campaign tracking** — links a website/app session back to the specific send that drove it, via matching tracking parameters (`curated.user_session_conversion_metrics`).
- **Purchase/demand confirmation** — confirms whether a tracked session actually led to a real purchase or styling request (`curated.client_reactivation_demand_events`).

# The Population: Clients Dormant 3+ Years

- This population is defined as clients with no checkout in more than 1,095 days (3+ years) — a stricter cut than the standard "Dormant" bucket (any gap over 365 days).
- CTSM embeddings are built from a client's accumulated behavioral history. For clients who haven't interacted with the product in years, that history — and therefore the resulting embedding — is the one most likely to be stale or effectively missing, which is exactly why continued embedding generation is worth scrutinizing for this specific group.
- Within the full client base, this group is sizable: 9,805,722 clients, compared to 2,102,284 in the broader Dormant bucket, 1,464,027 Active, 868,517 Lapsed, and 36,863,824 who have never checked out at all.
- This population definition is used consistently throughout — both for sizing a potential live test and for reviewing existing send history.

Full client base by lifecycle bucket (chart-ready data):

| Lifecycle bucket | Definition (days since last checkout) | Clients |
|---|---|---|
| Active | ≤ 120 days | 1,464,027 |
| Lapsed | 121-365 days | 868,517 |
| Dormant | 366-1,095 days | 2,102,284 |
| Dormant 3+ yrs (this analysis's population) | > 1,095 days | 9,805,722 |
| Never Active | Never checked out | 36,863,824 |

# How We're Measuring Conversion

- A send only counts as producing a **reactivation** if the client visited via a session carrying that specific send's own tracking parameters (real click-through evidence, not just a coincidence), and that session is linked to an actual Fix request or direct-buy order — both within 7 days of the send.
- This click-through-confirmed standard is a meaningful signal but not a perfect one: a tracked click doesn't prove the send caused the visit (the client may have been about to return regardless), and the absence of a tracked click doesn't rule out a real effect that happened through an untracked path. This limitation applies equally to every campaign type, not just one.
- The same metric and 7-day window is applied consistently across every comparison in this analysis, so results are directly comparable to one another.
- Because this standard requires a trackable click-through session, it's inherently conservative — only about 1.9% of eligible sends produce any matched session at all — which is part of why the baseline reactivation rate used for sizing is so low.

The core matching logic, applied consistently throughout:

```sql
-- session/UTM match: within the attribution window, using the send's own UTM content
AND u.utm_source = 'blueshift'
AND u.utm_content = d.send_utm_content
AND u.datetime_in_utc >= d.sent_timestamp
AND u.datetime_in_utc <  d.sent_timestamp + INTERVAL '7' DAY
...
-- demand confirmation: the matched session must link to a real Fix or direct-buy order
INNER JOIN curated.client_reactivation_demand_events e
    ON e.active_session_id = ms.active_session_id
WHERE e.demand_type IN ('fix', 'direct_buy')
```

# Why a Live Test Isn't a Practical Path Here

- Sizing a hypothetical live test (personalization vs. no personalization) for this population starts from a baseline reactivation rate of just 0.09%/month — reactivation via any tracked marketing send is inherently rare here, which drives up the sample size and time needed to detect a real effect.
- Even a moderate +5% relative lift would need about 335 days (~48 weeks) to confirm with standard confidence and power; a more conservative +3% lift would need about 920 days — well over two years.
- Only a large +15% lift could be confirmed in a meaningfully shorter window (~39 days) — a bigger effect than what's typically assumed for an incremental personalization signal.
- Given these timelines, a live experiment isn't a practical way to resolve whether continued CTSM embedding investment for this population is worth it right now — the decision needs another basis.

Sample size and duration by target relative lift (chart-ready data):

| Target relative lift | Clients needed per arm | Total clients needed | Minimum duration |
|---|---|---|---|
| +3% | 19,607,644 | 39,215,288 | 920 days (131.4 weeks) |
| +5% | 7,128,232 | 14,256,464 | 335 days (47.9 weeks) |
| +10% | 1,825,481 | 3,650,962 | 86 days (12.3 weeks) |
| +15% | 830,623 | 1,661,246 | 39 days (5.6 weeks) |

# What Existing Send History Suggests

- Beyond APEC, this population also received a range of other marketing content, plus a small number of transactional/account-service messages (password resets, order status updates, and similar). Those account-service messages are excluded from this comparison since a client only receives one because they're already returning on their own, not because of any marketing choice.
- Across the remaining marketing content sent to this population, APEC's directly-attributed reactivation rate (0.19%) does not stand out as higher than the rest combined (0.31%) — a modest, not dramatic, difference.
- This is a direct-attribution, observational comparison, not a controlled measurement of any one campaign's true incremental effect: different campaign types can reach different sub-segments of clients, at different frequencies, through different channels, and a tracked click doesn't prove causation either way.
- Combined with the cost of confirming impact through a live test, this send history doesn't provide evidence that continued CTSM embedding generation is paying off for this specific population today.

Reactivation rate, APEC vs. all other marketing content combined (chart-ready data):

| Group | Clients sent | Reactivated | Reactivation rate |
|---|---|---|---|
| APEC (personalized) | 1,322,312 | 2,494 | 0.19% |
| All other marketing content | 4,311,084 | 13,227 | 0.31% |

Monthly reactivation rate, APEC vs. all other marketing content combined (chart-ready data):

| Month | APEC reactivation rate | Other marketing content |
|---|---|---|
| 2025-01 | 0.0393% | 0.0494% |
| 2025-02 | 0.0258% | 0.0186% |
| 2025-03 | 0.0245% | 0.0391% |
| 2025-04 | 0.0231% | 0.0490% |
| 2025-05 | 0.0338% | 0.0379% |
| 2025-06 | 0.0366% | 0.0306% |
| 2025-07 | 0.0081% | 0.0413% |
| 2025-08 | 0.0197% | 0.0377% |
| 2025-09 | 0.0350% | 0.0796% |
| 2025-10 | 0.0083% | 0.0536% |
| 2025-11 | 0.0132% | 0.0396% |
| 2025-12 | 0.0065% | 0.0557% |
| 2026-01 | 0.0114% | 0.0886% |
| 2026-02 | 0.0074% | 0.0677% |
| 2026-03 | 0.0137% | 0.0879% |
| 2026-04 | 0.0148% | 0.0702% |
| 2026-05 | 0.0123% | 0.0663% |

# APEC's Own Trajectory in This Population

- Looking at APEC's own reactivation rate for this population over time, independent of any comparison to other campaign types, it declines across the 17-month window observed: pooled at 0.0253% across the first 10 months versus 0.0122% across the final 7 — roughly a 2.1x difference.
- This isn't simply a smaller-audience effect: APEC's send volume dropped from roughly 875,000-958,000 clients/month down to about 198,000-203,000 partway through the window, but the one month volume unexpectedly returned to its earlier size still showed the same lower rate (0.0137%), not a return to the earlier ~0.02-0.04% range.
- The decline was already visible before that volume change, too — one month's rate was already among the lowest observed while volume was still at its earlier, higher level.
- Whatever the specific driver, APEC's reactivation rate for this population has not been stable or improving over the period observed.

APEC monthly send volume and reactivation rate, standalone (chart-ready data):

| Month | Clients sent | Reactivated | Reactivation rate |
|---|---|---|---|
| 2025-01 | 875,027 | 344 | 0.0393% |
| 2025-02 | 878,809 | 227 | 0.0258% |
| 2025-03 | 880,369 | 216 | 0.0245% |
| 2025-04 | 876,291 | 202 | 0.0231% |
| 2025-05 | 876,254 | 296 | 0.0338% |
| 2025-06 | 874,596 | 320 | 0.0366% |
| 2025-07 | 855,775 | 69 | 0.0081% |
| 2025-08 | 864,421 | 170 | 0.0197% |
| 2025-09 | 905,792 | 317 | 0.0350% |
| 2025-10 | 958,731 | 80 | 0.0083% |
| 2025-11 | 197,553 | 26 | 0.0132% |
| 2025-12 | 198,700 | 13 | 0.0065% |
| 2026-01 | 202,341 | 23 | 0.0114% |
| 2026-02 | 203,329 | 15 | 0.0074% |
| 2026-03 | 955,586 | 131 | 0.0137% |
| 2026-04 | 203,136 | 30 | 0.0148% |
| 2026-05 | 203,837 | 25 | 0.0123% |

# How Other Campaign Types Compare

- Beyond APEC, sends to this population break down into several other categories by campaign name: general marketing content (OTHER), two other campaign families (DSE, TFY), a dormant-specific browse-abandon trigger, and two one-time campaigns — plus transactional/account-service email, tracked separately since a client only receives one because they're already returning on their own, not due to any marketing choice.
- Across the categories with meaningful volume, APEC's reactivation rate (0.19%) sits close to OTHER (0.20%) and modestly below DSE (0.32%); TFY (0.04%) and the dormant browse-abandon trigger (0.03%) are much smaller in both volume and reactivation.
- The two one-time campaigns show close to no measurable reactivation: Fresh Picks reactivated 0 of 406,283 clients sent, and New For You reactivated 3 of 302,180.
- These categories are grouped by naming pattern only, not confirmed personalization, and this remains a direct-attribution, observational comparison — useful descriptive context, not a controlled measurement of any one campaign's true effect, and not a basis for recommending one campaign type over another.

Reactivation rate by category, full window (chart-ready data):

| Category | Clients sent | Reactivated | Reactivation rate |
|---|---|---|---|
| OTHER | 4,297,628 | 8,588 | 0.1998% |
| DSE | 1,400,189 | 4,434 | 0.3167% |
| APEC | 1,322,312 | 2,494 | 0.1886% |
| TFY | 643,965 | 263 | 0.0408% |
| TRANSACTIONAL | 595,900 | 43,770 | 7.3452% |
| Fresh Picks (one-time) | 406,283 | 0 | 0.0000% |
| New For You (one-time) | 302,180 | 3 | 0.0010% |
| Dormant browse-abandon | 59,236 | 18 | 0.0304% |

# Category Performance Over Time

- Among these categories, the month-to-month ranking is noisy rather than one-sided: APEC leads all of them in 2 of the 17 months observed (May and June 2025).
- TFY shows a rate spike starting around November 2025, coinciding with a sharp drop in its own send volume that same month — likely a smaller, different remaining segment rather than a stable signal about the category's typical performance.
- Fresh Picks and New For You are each a single one-off send, contributing one data point rather than a trend; the dormant browse-abandon trigger's thin monthly volume (well under 9,500 clients in any month) leads briefly in January-March 2025, drops out for several months, spikes once in August 2025, then levels off for the remainder of the window.
- As with the pooled comparison, this month-by-month view is descriptive context on existing send history, not a controlled measurement of incremental impact for any category.

Monthly reactivation rate by category (chart-ready data; "—" = no sends that category/month):

| Month | OTHER | TRANSACTIONAL | DSE | APEC | TFY | Dormant browse-abandon | New For You | Fresh Picks |
|---|---|---|---|---|---|---|---|---|
| 2025-01 | 0.0306% | 7.0237% | 0.0288% | 0.0393% | 0.0043% | 0.0428% | — | — |
| 2025-02 | 0.0120% | 9.6980% | 0.0215% | 0.0258% | 0.0024% | 0.0633% | — | — |
| 2025-03 | 0.0254% | 9.7490% | 0.0214% | 0.0245% | 0.0024% | 0.0604% | — | — |
| 2025-04 | 0.0288% | 8.4885% | 0.0330% | 0.0231% | 0.0017% | 0.0000% | — | — |
| 2025-05 | 0.0227% | 8.4744% | 0.0226% | 0.0338% | 0.0018% | 0.0000% | — | — |
| 2025-06 | 0.0186% | 7.1600% | 0.0202% | 0.0366% | 0.0016% | — | — | — |
| 2025-07 | 0.0266% | 6.9610% | 0.0258% | 0.0081% | 0.0002% | — | — | 0.0000% |
| 2025-08 | 0.0241% | 7.5549% | 0.0237% | 0.0197% | 0.0017% | 0.0743% | — | — |
| 2025-09 | 0.0720% | 7.5112% | 0.0183% | 0.0350% | 0.0033% | 0.0295% | — | — |
| 2025-10 | 0.0358% | 7.2358% | 0.0294% | 0.0083% | 0.0034% | 0.0000% | — | — |
| 2025-11 | 0.0253% | 7.0757% | 0.0173% | 0.0132% | 0.0593% | 0.0300% | — | — |
| 2025-12 | 0.0376% | 1.2235% | 0.0230% | 0.0065% | 0.0407% | 0.0142% | — | — |
| 2026-01 | 0.0379% | 7.7691% | 0.0654% | 0.0114% | 0.0665% | 0.0117% | 0.0010% | — |
| 2026-02 | 0.0438% | 8.7973% | 0.0268% | 0.0074% | 0.0689% | 0.0359% | — | — |
| 2026-03 | 0.0510% | 8.5368% | 0.0427% | 0.0137% | 0.0659% | 0.0212% | — | — |
| 2026-04 | 0.0502% | 7.5639% | 0.0252% | 0.0148% | 0.0122% | 0.0120% | — | — |
| 2026-05 | 0.0422% | 2.6944% | 0.0278% | 0.0123% | 0.0506% | 0.0127% | — | — |

# Bottom Line: The CTSM-Embedding Recommendation

- A live experiment isn't a practical way to resolve this question: even a moderate +5% lift would take about 48 weeks to confirm, and a more conservative +3% lift would take well over two years — timelines that don't fit a resourcing decision that needs to be made now.
- Existing send history for this specific population doesn't show APEC's personalized rate standing out above other marketing content, and APEC's own rate for this population has trended down over the period observed — directional evidence, not proof, but consistent with no clear, demonstrated payoff yet from continued investment here.
- This finding is specific to the long-dormant (3+ year) population, where the behavioral history CTSM embeddings depend on is most likely to be stale — it is not a broader statement about APEC's value for other populations, and not a comparison against any specific other campaign.
- Recommendation: don't continue generating fresh CTSM embeddings for long-dormant clients on the current basis; use a substitute in the meantime (e.g. the average CTSM embedding for the client's business line) until there's a practical way to establish real incremental impact.

---

## Images to add

None. Every chart referenced above is provided as chart-ready tabular data directly under its slide heading, so the add-in can build native, editable PowerPoint charts instead of embedding static images.
