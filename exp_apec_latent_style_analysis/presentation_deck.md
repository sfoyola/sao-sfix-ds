# APEC — Reactivation Impact for Long-Dormant Clients

- Presenter: Sergio Oyola
- Presentation date: July 21, 2026
- Core question: does personalized email content meaningfully improve reactivation among clients who haven't checked out in 3+ years?
- Based on a sizing analysis for a potential live test, plus a look at actual send history for this population

# Executive Summary

- No clear case to run a full randomized test: APEC personalization roughly matches non-APEC marketing content, with no evidence it's helping the long-dormant population.
- Population: about 9.8M clients dormant 3+ years — ample for any test design; population size isn't the constraint.
- The read (17 months): APEC (0.19%) is below non-APEC (0.31%), below DSE (0.32%), and far below the transactional-email artifact (7.35%, which is excluded from the comparison) — and the trend is degrading, not improving, with APEC's rate 2.1x lower in the final 7 months than the first 10.
- The cost of proof: baseline reactivation is only ~0.09%/month, so even a +15% lift would need ~1.66M clients and ~6 weeks, while a more realistic +5% lift would need ~14.3M clients and ~48 weeks — reinforcing that there's no clear case to run a full randomized experiment right now.

# Data Behind This Analysis

- **Campaign send history** — every email/push/SMS sent to a client, including whether it was opened, clicked, and whether it led to a purchase (`blueshift.campaign_activity_kpis`); analysis is restricted to sends that actually reached a client (excludes holdout/control-group records with no real delivery).
- **Client lifecycle history** — tracks each client's engagement state (Active / Lapsed / Dormant / Never Active) over time, so a client's status can be checked *as of a specific send* rather than only as of today (`curated.checkout_based_client_state_journal`).
- **Session data with campaign tracking** — links a website/app session back to the specific send that drove it, via matching tracking parameters (`curated.user_session_conversion_metrics`).
- **Purchase/demand confirmation** — confirms whether a tracked session actually led to a real purchase or styling request (`curated.client_reactivation_demand_events`).

# The Population: Clients Dormant 3+ Years

- This analysis focuses on clients with no checkout in more than 1,095 days (3+ years) — a deliberately stricter cut than StitchFix's standard "Dormant" bucket (any checkout gap over 365 days).
- For a personalization system that relies on a history of client behavior, a client who hasn't interacted with the product in years is the population where that behavioral history — and therefore the personalization itself — is most likely to be stale or unavailable, making this the most informative group to check whether personalization is pulling its weight.
- Within the full client base, Dormant 3+ years is a sizable group: 9,805,722 clients, compared to 2,102,284 in the broader Dormant bucket, 1,464,027 Active, 868,517 Lapsed, and 36,863,824 who have never checked out at all.
- This same population definition anchors every subsequent slide — the power analysis's eligible pool and the personalization-impact comparison's population are both this identical Dormant 3+ years group, evaluated as of each specific send rather than as of today.

Full client base by lifecycle bucket (chart-ready data):

| Lifecycle bucket | Definition (days since last checkout) | Clients |
|---|---|---|
| Active | ≤ 120 days | 1,464,027 |
| Lapsed | 121-365 days | 868,517 |
| Dormant | 366-1,095 days | 2,102,284 |
| Dormant 3+ yrs (this analysis's population) | > 1,095 days | 9,805,722 |
| Never Active | Never checked out | 36,863,824 |

# How We're Measuring Conversion

- A send only counts as producing a **reactivation** if the client visited via a session carrying that specific send's own tracking parameters (real click-through evidence, not just a coincidence) and that session is linked to an actual Fix request or direct-buy order — both within 7 days of the send.
- This click-through-confirmed standard is deliberately stricter than "any purchase within a window of the send": it trades away credit for real reactivations that happen through untracked paths (e.g. closing an email and returning later via the app with no tracked link) in exchange for not crediting a send with an unrelated, coincidental purchase.
- The same metric and 7-day window is used everywhere in this analysis — the power analysis's baseline rate and the personalization-impact comparison are built on this identical definition, so the two are directly comparable and neither one is measuring something different from the other.
- Because this standard requires a trackable click-through session, it's inherently conservative — only about 1.9% of eligible sends produce any UTM-matched session at all — which is why the baseline reactivation rate used for sizing is as low as it is, and why the required sample sizes and durations in the power analysis are as large as they are.

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

# Sizing a Hypothetical Live Experiment

- Eligible population: clients with no checkout in more than 1,095 days (3+ years) — about **9,805,722 clients**, more than enough to support any test design; population size is not the constraint.
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

- Transactional campaigns (password resets, order/Fix status confirmations) convert at **7.35%** — a data artifact, not a campaign effect — but only because the client is already logging in or checking an order, not because of marketing content.
- With transactional email set aside, APEC (0.19%) sits modestly below all genuine non-APEC campaigns (0.31%).

Reactivation rate: transactional email vs. genuine marketing (chart-ready data):

| Category | Reactivation rate |
|---|---|
| Transactional email | 7.3452% |
| Non-APEC | 0.31% |
| APEC | 0.1886% |

# APEC vs. Non-APEC Sends

- To get a reliable read without waiting months for a live test, this analysis looks at **516 days of actual send history (~17 months, January 2025 - May 2026)** for the same 3+-year-dormant population sized above — longer than the minimum duration for the +5%, +10%, or +15% designs above (335, 86, and 39 days respectively), though shorter than the +3% design's 920-day requirement.
- A client counts as **reactivated** by a send only if they clicked through to a tracked session tied to that specific send, and that session led to a real purchase or styling request within 7 days — a strict, click-through-confirmed standard. The TRANSACTIONAL category is excluded from this comparison since clients act on it because they're already returning, not because of marketing.
- APEC (personalized) sends reactivated **0.19%** of the 1,322,312 clients who received them; every other qualifying marketing send combined reactivated **0.31%** of the 4,311,084 clients who received them — roughly **1.6x higher** for non-personalized sends.
- That gap (0.12 percentage points, 95% CI 0.11-0.13 points) is still statistically significant (p < 0.0001), though far smaller than a surface-level comparison would suggest — and it holds up in 15 of the 17 months individually, not just pooled (APEC edges ahead in February and June 2025).

Sends are classified by campaign name — every campaign containing "apec" is labeled `APEC`, everything else is `non-APEC` (transactional email is filtered out of the population before this split):

```sql
-- Transactional/account-service email is excluded from the population before this split
CASE WHEN send_utm_campaign LIKE '%apec%' THEN 'APEC' ELSE 'non-APEC' END AS apec_group
```

Monthly reactivation rate, APEC vs. non-APEC (chart-ready data):

| Month | APEC reactivation rate | Non-APEC reactivation rate |
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

# How Other Campaign Types Compare

- Beyond the APEC-vs-everything split, sends break down into 8 categories by campaign name: APEC, transactional/account-service email (excluded from the Part 1 comparison but shown here for transparency), two other "smart-sounding" campaign families (DSE, TFY), a dormant-specific browse-abandon trigger, two one-time campaigns, and OTHER (everything else).
- Compared against the other genuine marketing categories, APEC's 0.19% reactivation rate is close to OTHER's 0.20% and modestly below DSE's 0.32%.
- TFY (0.04%) and the dormant browse-abandon trigger (0.03%) are the smallest, thinnest-volume marketing categories; two one-time campaigns are even more extreme — Fresh Picks reactivated 0 of 406,283 clients, and New For You reactivated just 3 of 302,180.
- DSE, TFY, and the two one-time campaigns are grouped by naming pattern only, not confirmed personalization — treat them as descriptive context, not proof of what personalization does or doesn't do.

Categories are classified in priority order by campaign name:

```sql
CASE
    WHEN send_utm_campaign LIKE '%apec%' THEN 'APEC'
    WHEN send_utm_campaign LIKE '%transactional%' THEN 'TRANSACTIONAL'
    WHEN send_utm_campaign LIKE '%dse%' THEN 'DSE'
    WHEN send_utm_campaign LIKE '%tfy%' THEN 'TFY'
    WHEN send_utm_campaign LIKE '%dormantbrowseabandon%' THEN 'dormantbrowseabandon'
    WHEN send_utm_campaign LIKE '%newforyou%' THEN 'newforyou'
    WHEN send_utm_campaign LIKE '%freshpicks%' THEN 'freshpicks'
    ELSE 'OTHER'
END AS campaign_category
```

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

- Among the genuine marketing categories, the month-to-month ranking is noisy: **APEC** actually leads all of them in 2 of the 17 months (May and June 2025).
- APEC's rank drops sharply starting **November 2025** — averaging roughly 0.025% in the first ten months of the window vs. roughly 0.011% in the final seven.
- **TFY** shows a low-volume-driven rate spike starting November 2025.
- **Fresh Picks** and **New For You** are each a single one-off data point with poor performance; the **dormant browse-abandon** trigger's monthly volume leads from January to March 2025, then drops to zero and disappears for several months, spikes again in August 2025, and decreases and stabilizes for the remainder of the window.

Chart excludes TRANSACTIONAL (7.35%) to keep marketing categories readable. Monthly reactivation rate by category (chart-ready data; "—" = no sends that category/month):

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

# APEC: Decline Over Time

- Looking at APEC by itself, not compared to other categories, its reactivation rate declines materially over the 17-month window: pooled at **0.0253%** across the first 10 months (January-October 2025) versus **0.0122%** across the final 7 (November 2025-May 2026) — roughly a **2.1x drop**.
- This isn't simply a shrinking-audience artifact: APEC's own send volume dropped sharply starting November 2025 (from roughly 875,000-958,000 clients/month down to about 198,000-203,000), but the one month volume unexpectedly recovered to its earlier size — March 2026, back up to 955,586 clients — still shows the same lower rate (0.0137%) as the surrounding low-volume months, not a reversion to the earlier ~0.02-0.04% range.
- Noisy small samples from reduced reach don't explain the decrease either: the decline was already underway before the November 2025 volume drop — October 2025's rate (0.0083%) was already one of the lowest points in the first ten months.
- Whatever the specific cause, the practical takeaway holds either way: APEC's already-modest reactivation rate is not stable or improving over the window — it's degrading over time.

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

# Bottom Line: Is a Live Experiment Worth Running?

- Compared against genuine marketing categories, APEC (0.19%) is close to OTHER (0.20%) and modestly below DSE (0.32%), though still statistically below the pooled average across all qualifying non-APEC marketing sends (0.31%, p < 0.0001).
- This remains an observational comparison, not a randomized test: differences in who gets targeted, how often, or through which channel could explain part of the remaining gap, so it's an association, not proof that personalization *causes* worse (or better) outcomes.
- Baseline reactivation for genuine marketing sends to this population is just 0.09%/month, so confirming even a large +15% lift with a live randomized test needs ~1.66M clients and about 5.6 weeks, and a more realistic +5% lift needs ~14.3M clients and nearly a year (47.9 weeks).
- Given how costly a live test would be, and that the observational signal doesn't show APEC clearly underperforming — it roughly matches non-personalized marketing content — there isn't a clear case for running a full randomized experiment right now, but there also isn't strong observational evidence that personalization is helping, either.

---

## Images to add

None. Every chart referenced above (the monthly APEC-vs-non-APEC trend and the monthly category breakdown) is provided as chart-ready tabular data directly under its slide heading, so the add-in can build native, editable PowerPoint charts instead of embedding static images.
