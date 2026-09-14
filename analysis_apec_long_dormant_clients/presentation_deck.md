# CTSM Embeddings for Long-Dormant Clients

- Question: for clients dormant 3+ years, is a per-client CTSM-embedding-driven APEC send worth generating — or does a coarser, business-line-average embedding do the job for less?
- Analysis window: 18 months of send history (Jan 2025 – Jun 2026), StitchFix's Blueshift campaign and reactivation data.
- Presenter: Sergio Oyola

# Executive Summary

- **The read:** across every lifecycle state, DSE (non-CTSM-personalized, dynamically assembled shoppable content) reactivates clients better than APEC — and generic OTHER campaigns have overtaken APEC too, state by state: in Dormant since October 2025, in Lapsed since November 2025, and now in Dormant 3+ yrs since April 2026. APEC's early edge over generic content has eroded everywhere, reaching even the most-dormant population last.
- **The cost of proof:** even a realistic +10% lift on APEC's reactivation rate needs 3.65M client-observations (~86 days) to detect in a live test; a more defensible +3–5% lift needs 8 months to 2.5+ years.
- **The call:** substitute a business-line-average embedding for Dormant 3+ yrs clients instead of computing a fresh per-client CTSM embedding for each of them — this population's own purchase history is 3+ years stale, and APEC's personalization isn't showing a reactivation edge over a non-personalized alternative (DSE) for this group anyway.
- This is an observational read of existing send history, not a randomized test — it tells us what's associated with reactivation today, which is the evidence available to make this call without running a lengthy live experiment first.

# Data Behind This Analysis

- **Campaign send history** — `blueshift.campaign_activity_kpis`: every send, its campaign name, and outcome flags.
- **Client lifecycle history** — `curated.checkout_based_client_state_journal`: a full history of each client's lifecycle state, so a client's status can be evaluated as of the exact moment of each send, not just today.
- **Session data with tracking** — `curated.user_session_conversion_metrics`: sessions carrying the UTM parameters that link a visit back to the send that drove it.
- **Purchase/demand confirmation** — `curated.client_reactivation_demand_events`: confirmed Fix requests and direct-buy orders, the actual reactivation signal.

# The Population: Three Lifecycle States

| Lifecycle state | Days since last checkout | Clients today |
|---|---|---|
| Active (excluded) | ≤ 120 | 1,417,668 |
| Lapsed | 121 – 365 | 912,073 |
| Dormant | 366 – 1,095 | 2,038,497 |
| **Dormant 3+ yrs (focus population)** | 1,096+ | **9,974,636** |
| Never Active (excluded) | n/a | 37,241,392 |

- Dormant 3+ yrs is the decision population: for a personalization system built on client purchase history, a client who hasn't interacted with the product in 3+ years is where that history — and the personalization built on it — is most likely to be stale.
- Lapsed and Dormant are carried through this analysis as context, not as a separate ask: they show how reactivation responsiveness changes across the dormancy spectrum, which helps interpret whether a weak Dormant 3+ yrs result is about personalization specifically or about this population being harder to reach in general.
- At ~10M clients, Dormant 3+ yrs is by far the largest of the three states — nearly 5x Dormant and 11x Lapsed.

# How We're Measuring Reactivation

- A client counts as reactivated by a send only if **both** hold: they visited via a session carrying that exact send's UTM parameters (real click-through evidence), **and** that session is linked to a confirmed Fix request or direct-buy order — both within 7 days of the send.
- This is a conservative, click-through-confirmed standard, not "a purchase happened somewhere nearby in time" — in an illustrative single month (April 2026), only ~5.6% of eligible sends produced any UTM-matched session at all.
- Reported rates are a lower bound on true reactivation: reactivations through untracked paths (e.g. closing an email and returning later with no tracked link) aren't counted.

```sql
-- the two joins that define "reactivated"
INNER JOIN curated.user_session_conversion_metrics u
    ON u.client_id = c.client_id
    AND u.utm_source = 'blueshift'
    AND u.utm_content = c.send_utm_content
    AND u.datetime_in_utc >= c.sent_timestamp
    AND u.datetime_in_utc <  c.sent_timestamp + INTERVAL '7' DAY
...
INNER JOIN curated.client_reactivation_demand_events e
    ON e.active_session_id = ms.active_session_id
    WHERE e.demand_type IN ('fix', 'direct_buy')
```

# Campaign Categories in Scope

- **APEC** (Algorithmic Personalized Email Content): shows a client a grid of non-shoppable clothing images matched to their inferred style via a latent style vector — a CTSM-driven, per-client personalization signal.
- **DSE** (Dynamic Shoppable Email): dynamically assembles shoppable Freestyle content at open time — a distinct, well-established program, not built on APEC's CTSM-embedding personalization.
- **OTHER**: every remaining generic marketing/seasonal send with no personalization-, promo-, or program-specific signature.
- Every send is classified by a full, ordered mapping (10 categories total — APEC, TRANSACTIONAL, DSE, PROMO_INCENTIVE, FLS, TRACKING_ARTIFACT, WINBACK, BIRTHDAY, CROSSSELL, OTHER), based on campaign-name pattern matching rather than a verified per-send flag, so that OTHER is a clean residual; only APEC, DSE, and OTHER are profiled here since they're what the embedding decision turns on.

# Reactivation Rate by Client State, Across Categories

| Category | Lapsed | Dormant | Dormant 3+ yrs |
|---|---|---|---|
| APEC | 0.46% (0.44–0.47%) | 0.56% (0.55–0.57%) | 0.19% (0.19–0.20%) |
| DSE | 1.39% (1.37–1.41%) | 0.78% (0.77–0.80%) | 0.27% (0.26–0.28%) |
| OTHER | 0.85% (0.84–0.86%) | 0.30% (0.30–0.31%) | 0.08% (0.08–0.08%) |

- Reactivation rate falls off sharply with dormancy length in every category — Dormant 3+ yrs rates are roughly a third of Dormant rates, across the board.
- DSE has the highest reactivation rate of the three categories in every single lifecycle state.
- APEC beats OTHER in Dormant and Dormant 3+ yrs, but trails OTHER in Lapsed — APEC's personalization doesn't uniformly outperform generic marketing content.

# DSE Outperforms APEC in Every Lifecycle State

- **Lapsed:** DSE 1.39% vs. APEC 0.46% — DSE reactivates at ~3x APEC's rate.
- **Dormant:** DSE 0.78% vs. APEC 0.56% — DSE at ~1.4x APEC.
- **Dormant 3+ yrs (the focus population):** DSE 0.27% vs. APEC 0.19% — DSE at ~1.4x APEC.
- DSE doesn't use APEC's CTSM-embedding-driven personalization — it dynamically assembles shoppable content instead. A non-personalized-by-embedding program consistently out-reactivating the personalized one is the central piece of evidence against per-client APEC embeddings being the thing driving reactivation for this population.

# Reach vs. Response: Where Volume and Reactivation Diverge

| Category | Lapsed sent | Dormant sent | Dormant 3+ yrs sent |
|---|---|---|---|
| APEC | 756,568 | 1,153,241 | 1,362,249 |
| DSE | 1,735,120 | 1,686,563 | 1,866,611 |
| OTHER | 2,167,574 | 2,422,393 | 3,753,853 |

- OTHER receives the most send volume in every state — most strikingly in Dormant 3+ yrs (3.75M clients sent) — despite having the lowest reactivation rate there (0.08%).
- Lapsed, the best-responding state in every category, gets the least send volume of the three states across the board.
- This mismatch — most volume going to the state and category combination that responds weakest — is worth factoring into any resourcing decision, not just the embedding question.

# Lapsed — Monthly Unique Clients Sent, APEC vs. DSE vs. OTHER

| Month | APEC | DSE | OTHER |
|---|---|---|---|
| 2025-01 | 226,803 | 626,542 | 651,852 |
| 2025-02 | 159,927 | 614,205 | 725,752 |
| 2025-03 | 155,444 | 621,375 | 646,667 |
| 2025-04 | 152,006 | 592,911 | 612,942 |
| 2025-05 | 148,775 | 583,181 | 601,577 |
| 2025-06 | 145,283 | 557,172 | 580,226 |
| 2025-07 | 129,342 | 544,937 | 572,295 |
| 2025-08 | 138,035 | 555,736 | 606,663 |
| 2025-09 | 139,952 | 543,787 | 559,116 |
| 2025-10 | 128,275 | 529,096 | 545,472 |
| 2025-11 | 77,470 | 448,381 | 473,263 |
| 2025-12 | 77,831 | 455,205 | 471,134 |
| 2026-01 | 78,743 | 488,691 | 827,039 |
| 2026-02 | 80,537 | 489,648 | 522,585 |
| 2026-03 | 325,049 | 513,986 | 553,600 |
| 2026-04 | 86,126 | 515,031 | 546,175 |
| 2026-05 | 87,506 | 522,679 | 564,777 |
| 2026-06 | 92,590 | 532,626 | 584,353 |

- APEC's Lapsed volume falls sharply from 226,803 (Jan 2025) to a stable 77K–93K band from November 2025 onward — roughly a 65% drop — while DSE and OTHER hold far higher, steadier volume throughout.
- From November 2025 on, DSE and OTHER each send to 5–6x as many Lapsed clients per month as APEC does.
- OTHER's spike to 827,039 in January 2026 is the largest single-month count in this table — a one-off (February 2026 reverts to ~523K), not a sustained shift.

# Dormant — Monthly Unique Clients Sent, APEC vs. DSE vs. OTHER

| Month | APEC | DSE | OTHER |
|---|---|---|---|
| 2025-01 | 654,858 | 968,566 | 1,091,471 |
| 2025-02 | 638,675 | 944,135 | 1,449,635 |
| 2025-03 | 633,085 | 937,219 | 1,011,036 |
| 2025-04 | 617,866 | 924,772 | 989,952 |
| 2025-05 | 604,722 | 915,820 | 891,248 |
| 2025-06 | 601,013 | 904,230 | 957,947 |
| 2025-07 | 568,370 | 898,969 | 967,095 |
| 2025-08 | 575,206 | 887,917 | 972,299 |
| 2025-09 | 567,516 | 870,061 | 905,365 |
| 2025-10 | 552,396 | 851,337 | 904,498 |
| 2025-11 | 136,352 | 617,881 | 673,588 |
| 2025-12 | 140,165 | 603,344 | 636,723 |
| 2026-01 | 143,444 | 608,017 | 859,921 |
| 2026-02 | 139,298 | 584,763 | 602,961 |
| 2026-03 | 486,682 | 576,235 | 598,840 |
| 2026-04 | 134,333 | 566,296 | 598,014 |
| 2026-05 | 133,157 | 560,949 | 601,257 |
| 2026-06 | 131,035 | 558,319 | 606,961 |

- APEC's Dormant volume steps down from ~655K (Jan 2025) to a ~131K–144K band from November 2025 on — a 4–5x drop — while DSE and OTHER stay far higher throughout.
- That volume step-down lines up with the reactivation-rate decline shown on the Dormant rate slide — both arrive in Q4 2025, though this table alone doesn't establish which drove which.
- OTHER's 1,449,635 in February 2025 is an outlier, roughly 1.5x its typical level elsewhere in the window.

# Dormant 3+ yrs — Monthly Unique Clients Sent, APEC vs. DSE vs. OTHER

| Month | APEC | DSE | OTHER |
|---|---|---|---|
| 2025-01 | 888,187 | 1,236,510 | 1,396,676 |
| 2025-02 | 881,350 | 1,239,973 | 3,046,785 |
| 2025-03 | 882,049 | 1,250,951 | 1,388,694 |
| 2025-04 | 878,027 | 1,262,664 | 1,393,307 |
| 2025-05 | 877,447 | 1,279,267 | 1,253,812 |
| 2025-06 | 875,314 | 1,289,977 | 1,429,263 |
| 2025-07 | 856,503 | 1,297,722 | 1,453,355 |
| 2025-08 | 865,496 | 1,303,650 | 1,482,789 |
| 2025-09 | 907,530 | 1,400,618 | 1,538,092 |
| 2025-10 | 960,376 | 1,403,999 | 1,568,960 |
| 2025-11 | 201,404 | 991,359 | 1,185,985 |
| 2025-12 | 206,001 | 987,176 | 1,166,158 |
| 2026-01 | 211,230 | 999,749 | 1,229,085 |
| 2026-02 | 211,817 | 986,665 | 1,076,369 |
| 2026-03 | 960,394 | 990,994 | 1,100,881 |
| 2026-04 | 212,419 | 989,350 | 1,078,354 |
| 2026-05 | 212,527 | 990,715 | 1,079,186 |
| 2026-06 | 211,032 | 989,051 | 1,101,478 |

- APEC's volume steps down from ~880K–960K (through Oct 2025) to a ~201K–212K band from November 2025 on — roughly a 75–80% drop — with a single-month reversion to 960,394 in March 2026.
- DSE holds steady in the 990K–1.4M range throughout, and OTHER grows from ~1.4M toward a peak of 1.57M in October 2025 before settling near 1.1M — both far more stable than APEC's volume over the same period.
- APEC's monthly reach goes from roughly on par with DSE and OTHER in early 2025 to about a fifth of either by 2026 — a much larger swing than either of the other two categories shows.

# Lapsed — Monthly Reactivation Rate, APEC vs. DSE vs. OTHER

| Month | APEC | DSE | OTHER |
|---|---|---|---|
| 2025-01 | 0.240 | 0.306 | 0.165 |
| 2025-02 | 0.179 | 0.222 | 0.144 |
| 2025-03 | 0.180 | 0.264 | 0.182 |
| 2025-04 | 0.180 | 0.294 | 0.217 |
| 2025-05 | 0.222 | 0.250 | 0.155 |
| 2025-06 | 0.315 | 0.228 | 0.173 |
| 2025-07 | 0.070 | 0.258 | 0.144 |
| 2025-08 | 0.129 | 0.230 | 0.160 |
| 2025-09 | 0.263 | 0.233 | 0.170 |
| 2025-10 | 0.097 | 0.211 | 0.217 |
| 2025-11 | 0.056 | 0.278 | 0.122 |
| 2025-12 | 0.054 | 0.251 | 0.154 |
| 2026-01 | 0.055 | 0.292 | 0.174 |
| 2026-02 | 0.056 | 0.261 | 0.226 |
| 2026-03 | 0.068 | 0.333 | 0.191 |
| 2026-04 | 0.065 | 0.263 | 0.184 |
| 2026-05 | 0.066 | 0.285 | 0.225 |
| 2026-06 | 0.066 | 0.231 | 0.200 |

- Through H1 2025, APEC is competitive with DSE and ahead of OTHER (e.g. Jun 2025: APEC 0.315% vs. DSE 0.228% vs. OTHER 0.173%).
- From July 2025 on, APEC collapses to 0.05–0.13% and stays there — while DSE (0.21–0.33%) and OTHER (0.12–0.23%) hold steady.
- From November 2025 through the end of the window, APEC is the **lowest**-performing of the three categories in Lapsed, not just behind DSE but behind OTHER too.

# Dormant — Monthly Reactivation Rate, APEC vs. DSE vs. OTHER

| Month | APEC | DSE | OTHER |
|---|---|---|---|
| 2025-01 | 0.144 | 0.098 | 0.036 |
| 2025-02 | 0.096 | 0.060 | 0.023 |
| 2025-03 | 0.088 | 0.074 | 0.034 |
| 2025-04 | 0.075 | 0.090 | 0.038 |
| 2025-05 | 0.117 | 0.072 | 0.033 |
| 2025-06 | 0.145 | 0.065 | 0.032 |
| 2025-07 | 0.027 | 0.079 | 0.041 |
| 2025-08 | 0.064 | 0.069 | 0.036 |
| 2025-09 | 0.169 | 0.063 | 0.033 |
| 2025-10 | 0.030 | 0.078 | 0.064 |
| 2025-11 | 0.037 | 0.088 | 0.035 |
| 2025-12 | 0.028 | 0.103 | 0.042 |
| 2026-01 | 0.045 | 0.211 | 0.058 |
| 2026-02 | 0.019 | 0.148 | 0.055 |
| 2026-03 | 0.063 | 0.191 | 0.075 |
| 2026-04 | 0.042 | 0.119 | 0.099 |
| 2026-05 | 0.054 | 0.139 | 0.122 |
| 2026-06 | 0.043 | 0.108 | 0.098 |

- APEC leads OTHER through most of 2025 (e.g. Jun 2025: 0.145% vs. 0.032%), but that lead erodes steadily from October 2025 onward.
- DSE pulls sharply ahead of both starting January 2026 (0.11–0.21%), the same jump seen in Lapsed and Dormant 3+ yrs.
- OTHER overtakes APEC from October 2025 on and the gap widens through 2026 — by May–Jun 2026, OTHER (0.10–0.12%) is more than double APEC (0.04–0.05%).

# Dormant 3+ yrs — Monthly Reactivation Rate, APEC vs. DSE vs. OTHER

| Month | APEC | DSE | OTHER |
|---|---|---|---|
| 2025-01 | 0.039 | 0.024 | 0.011 |
| 2025-02 | 0.026 | 0.017 | 0.004 |
| 2025-03 | 0.025 | 0.017 | 0.010 |
| 2025-04 | 0.024 | 0.024 | 0.008 |
| 2025-05 | 0.035 | 0.017 | 0.006 |
| 2025-06 | 0.037 | 0.015 | 0.006 |
| 2025-07 | 0.009 | 0.018 | 0.010 |
| 2025-08 | 0.020 | 0.017 | 0.010 |
| 2025-09 | 0.035 | 0.015 | 0.006 |
| 2025-10 | 0.009 | 0.022 | 0.014 |
| 2025-11 | 0.015 | 0.020 | 0.008 |
| 2025-12 | 0.010 | 0.026 | 0.011 |
| 2026-01 | 0.014 | 0.049 | 0.015 |
| 2026-02 | 0.010 | 0.032 | 0.014 |
| 2026-03 | 0.015 | 0.048 | 0.021 |
| 2026-04 | 0.018 | 0.027 | 0.025 |
| 2026-05 | 0.014 | 0.033 | 0.030 |
| 2026-06 | 0.019 | 0.027 | 0.024 |

- APEC holds a narrow lead over OTHER through most of 2025 (roughly 2–4x), the last of the three states where that lead survives this long.
- DSE separates from both starting January 2026, mirroring the same jump seen in Lapsed and Dormant.
- Only in the final three months (Apr–Jun 2026) does OTHER (0.024–0.030%) overtake APEC (0.014–0.019%) here — the same erosion already visible in Lapsed since November 2025 and in Dormant since October 2025 has now reached even the most-dormant population.

# Sizing a Live Test — and Why It Isn't the Next Step

| Relative MDE | Client-observations per arm | Total | Minimum duration |
|---|---|---|---|
| +3% | 19,607,644 | 39,215,288 | 920 days (~131 weeks) |
| +5% | 7,128,232 | 14,256,464 | 335 days (~48 weeks) |
| +10% | 1,825,481 | 3,650,962 | 86 days (~12 weeks) |
| +15% | 830,623 | 1,661,246 | 39 days (~6 weeks) |

- Sized for a Personalization-vs-No-Personalization test on Dormant 3+ yrs clients, at a 0.09% monthly baseline reactivation rate, 80% power, two-sided 95% test, 50/50 split.
- Population size isn't the constraint (millions of eligible clients) — the constraint is the baseline rate itself: it's low enough that even a "quick" +15% MDE test needs 1.66M total client-observations.
- A realistic, defensible effect size (+3–5%) would take 8 months to 2.5+ years to detect — far longer than the decision in front of us can wait on, especially with no existing evidence APEC is pulling ahead of DSE or OTHER for this population to begin with.

# The Business-Line-Average-Embedding Hypothesis

- APEC's per-client, CTSM-embedding-driven personalization doesn't show a durable reactivation edge for Dormant 3+ yrs clients: it trails DSE (a non-CTSM-personalized program) throughout, and its early lead over generic OTHER content has fully eroded — OTHER has outperformed APEC here since April 2026.
- **Hypothesis:** a client's inferred style, built from purchase history that's 3+ years stale, likely no longer reflects their current taste — so a freshly computed per-client embedding may not be meaningfully more accurate than a coarser signal for this specific population.
- **Proposed alternative:** substitute a business-line-average embedding for Dormant 3+ yrs clients instead of computing and refreshing an individual embedding for each of them — freeing that compute for populations where personalization is demonstrably earning its keep.
- This is a hypothesis the analysis points toward, not something directly tested here — no experiment in this dataset isolates embedding staleness on its own; it's a reasonable inference from APEC's lack of separation from non-personalized alternatives in exactly the population where staleness would matter most.

# Bottom Line

- **No live test justified right now:** the cost to detect a realistic effect (8 months to 2.5+ years) is disproportionate to a population where APEC isn't already showing a lead over available alternatives.
- **No demonstrated payoff from per-client APEC embeddings** in Dormant 3+ yrs: APEC trails DSE across the full window, and its early lead over OTHER has eroded away entirely by the most recent months.
- **The recommendation:** move Dormant 3+ yrs clients to a business-line-average embedding in place of individually computed CTSM embeddings.
- **Scope check:** this call is specific to the Dormant 3+ yrs population — it says nothing about APEC's value for Active, Lapsed, or Dormant clients, where personalization may well be earning its cost.

## Images to add

- None. Every chart in this deck is provided as a markdown table so the add-in can build a native, editable PowerPoint chart directly from the data.
