# APEC Personalization Impact — Reactivation Analysis Across All Client States

- Presenter: Sergio Oyola
- Presentation date: [ADD DATE]
- Core question: does receiving an APEC (personalized) marketing send relate to a different reactivation rate than receiving a non-personalized send — and does that answer hold across client lifecycle state and business line, not just one population?
- Based on real send history across a 516-day window (2025-01-01 to 2026-05-31, ~17 months)

# Slide 1: The Population and the Analysis Window

- This analysis covers three client lifecycle states — Lapsed, Dormant, and Dormant 3+ years — excluding clients who have never checked out at all, since they have nothing to reactivate from.
- Active clients (checked out within the last 120 days) are also out of scope: the reactivation data this analysis relies on only logs a client returning from Lapsed or Dormant, so it has no way to measure Active-client conversion at all.
- Across the three in-scope states combined, roughly **12.9 million clients** (12,890,073) make up the analysis population, alongside a much larger pool of ~37.2 million clients who have never been active.
- The analysis window spans **516 days** (2025-01-01 to 2026-05-31, ~17 months) of real send history — long enough to give even the thinner campaign categories enough volume to read a reliable rate, and capped at a date old enough for outcome data to have fully settled.

Client population by lifecycle bucket (chart-ready data):

| Lifecycle bucket | Clients |
|---|---|
| Never Active | 37,158,690 |
| Dormant 3+ yrs | 9,929,139 |
| Dormant | 2,057,567 |
| Lapsed | 903,367 |

# Slide 2: APEC vs. Non-APEC Reactivation Rate, by Client State

- In every one of the three client states, clients sent a non-APEC (non-personalized) marketing send reactivated at a **higher** rate than clients sent an APEC (personalized) send — the gap is statistically significant in all three (p < 0.0001).
- The gap is largest in both absolute and relative terms for **Lapsed** clients (2.14 percentage points, non-APEC reactivating roughly 5.9x more often than APEC).
- For the state APEC was originally built to focus on — **Dormant 3+ yrs** — non-APEC still leads, by 0.12 percentage points (0.307% vs. 0.186%).

Reactivation rate, APEC vs. non-APEC, full window, by client state (chart-ready data):

| Client state | APEC clients sent | APEC reactivated | APEC reactivation rate | non-APEC clients sent | non-APEC reactivated | non-APEC reactivation rate | Difference (non-APEC − APEC) | p-value |
|---|---|---|---|---|---|---|---|---|
| Lapsed | 717,750 | 3,167 | 0.4412% | 2,247,197 | 58,000 | 2.5810% | 2.1398 pp | 0.00e+00 |
| Dormant | 1,128,490 | 6,158 | 0.5457% | 2,594,787 | 32,501 | 1.2525% | 0.7069 pp | 0.00e+00 |
| Dormant 3+ yrs | 1,349,279 | 2,512 | 0.1862% | 4,308,183 | 13,211 | 0.3066% | 0.1205 pp | 2.82e-153 |

# Slide 3: APEC vs. Non-APEC Reactivation Rate, Month by Month, by Client State

- The full-window gap on the previous slide isn't a one-off: non-APEC outperforms APEC in nearly every individual month, in every state — **17 of 17 months** for Lapsed, **16 of 17** for Dormant, and **15 of 17** for Dormant 3+ yrs.
- Each state has its own scale — Lapsed and Dormant clients reactivate at meaningfully higher rates than Dormant 3+ yrs clients, regardless of which campaign type they received.
- Note: each state's monthly rates are naturally noisier than the pooled full-window figures on the previous slide, since a single month has a smaller sample than the full 17-month window.

Monthly reactivation rate, APEC vs. non-APEC, by client state (chart-ready data):

| Month | Lapsed — APEC | Lapsed — non-APEC | Dormant — APEC | Dormant — non-APEC | Dormant 3+ yrs — APEC | Dormant 3+ yrs — non-APEC |
|---|---|---|---|---|---|---|
| 2025-01 | 0.2352% | 0.7111% | 0.1407% | 0.1948% | 0.0390% | 0.0494% |
| 2025-02 | 0.1683% | 0.5079% | 0.0948% | 0.0976% | 0.0260% | 0.0186% |
| 2025-03 | 0.1735% | 0.6107% | 0.0859% | 0.1522% | 0.0247% | 0.0390% |
| 2025-04 | 0.1700% | 0.6276% | 0.0708% | 0.1947% | 0.0230% | 0.0490% |
| 2025-05 | 0.2086% | 0.5314% | 0.1152% | 0.1538% | 0.0338% | 0.0379% |
| 2025-06 | 0.3106% | 0.5450% | 0.1431% | 0.1319% | 0.0366% | 0.0306% |
| 2025-07 | 0.0655% | 0.6028% | 0.0247% | 0.1905% | 0.0081% | 0.0413% |
| 2025-08 | 0.1258% | 0.5240% | 0.0613% | 0.1521% | 0.0198% | 0.0377% |
| 2025-09 | 0.2612% | 0.5915% | 0.1669% | 0.3239% | 0.0350% | 0.0796% |
| 2025-10 | 0.0895% | 0.5047% | 0.0279% | 0.2011% | 0.0083% | 0.0536% |
| 2025-11 | 0.0436% | 0.6171% | 0.0327% | 0.1614% | 0.0135% | 0.0396% |
| 2025-12 | 0.0436% | 0.5181% | 0.0246% | 0.2234% | 0.0068% | 0.0557% |
| 2026-01 | 0.0419% | 0.4259% | 0.0403% | 0.2907% | 0.0114% | 0.0885% |
| 2026-02 | 0.0419% | 0.5606% | 0.0138% | 0.2821% | 0.0085% | 0.0675% |
| 2026-03 | 0.0649% | 0.6101% | 0.0610% | 0.3149% | 0.0139% | 0.0877% |
| 2026-04 | 0.0569% | 0.5354% | 0.0311% | 0.2575% | 0.0152% | 0.0701% |
| 2026-05 | 0.0579% | 0.5920% | 0.0382% | 0.2499% | 0.0123% | 0.0663% |

# Slide 4: APEC vs. Non-APEC Reactivation Rate, by Business Line

- Non-APEC outperforms APEC in both business lines where APEC is actually sent: **Women's** (0.465% vs. 1.556%, a 1.09-point gap) and **Men's** (0.427% vs. 0.799%, a 0.37-point gap), both statistically significant (p < 0.0001).
- **Kids** received zero APEC-classified sends across the entire window — this is a structural fact about which campaigns exist for this business line, not a data gap. Kids clients still reactivated at 0.404% off non-APEC content alone.
- All three lifecycle states are pooled together for this business-line cut, so these rates reflect the full in-scope population, not any single state.

Reactivation rate, APEC vs. non-APEC, full window, by business line (chart-ready data):

| Business line | APEC clients sent | APEC reactivated | APEC reactivation rate | non-APEC clients sent | non-APEC reactivated | non-APEC reactivation rate | Difference (non-APEC − APEC) | p-value |
|---|---|---|---|---|---|---|---|---|
| Womens | 2,025,516 | 9,427 | 0.4654% | 5,721,192 | 89,033 | 1.5562% | 1.0908 pp | 0.00e+00 |
| Mens | 555,599 | 2,373 | 0.4271% | 1,325,887 | 10,598 | 0.7993% | 0.3722 pp | 5.79e-223 |
| Kids | 0 (no qualifying sends) | — | — | 458,232 | 1,852 | 0.4042% | n/a | n/a |

# Slide 5: Reactivation Rate by Campaign Category, by Business Line

- **TRANSACTIONAL** sits far above every other category in both business lines (an artifact of clients already returning on their own, not a marketing effect). Among the four marketing categories, full-window, the order differs by line: **Women's ranks DSE above OTHER** (1.130% vs. 0.958%), while **Men's ranks OTHER above DSE** (0.519% vs. 0.514%, essentially tied); APEC and FLS trail both in either line.
- Full-window rankings reward categories that simply resend to the same clients more often (OTHER, DSE, and APEC resend nearly every month; FLS only fires once per triggering event). Normalizing to a **per-client-month** basis — so a client sent in 8 different months contributes 8, not 1 — changes the picture substantially: **FLS leads per month sent in both lines** (0.369% Women's, 0.353% Men's — well above every other category), and **APEC is the lowest-reactivating genuine marketing category per month sent in both lines**, trailing even OTHER and DSE.
- **Kids** only has two categories present at all — OTHER and TRANSACTIONAL — since DSE, APEC, and FLS are never sent to this business line in the window observed.

Reactivation rate by campaign category, by business line — full window vs. per client-month sent (chart-ready data):

| Business line | Campaign category | Clients sent (full window) | Reactivated (full window) | Reactivation rate (full window) | Client-months sent | Reactivated (month-sum) | Reactivation rate (per month sent) |
|---|---|---|---|---|---|---|---|
| Womens | TRANSACTIONAL | 2,022,499 | 72,870 | 3.6030% | 3,370,890 | 74,135 | 2.1993% |
| Womens | DSE | 3,191,888 | 36,082 | 1.1304% | 33,563,663 | 37,572 | 0.1119% |
| Womens | OTHER | 5,701,100 | 54,625 | 0.9581% | 37,684,584 | 57,541 | 0.1527% |
| Womens | APEC | 2,058,709 | 9,916 | 0.4817% | 14,463,731 | 10,005 | 0.0692% |
| Womens | FLS | 263,526 | 2,080 | 0.7893% | 575,518 | 2,121 | 0.3685% |
| Mens | TRANSACTIONAL | 425,141 | 5,913 | 1.3908% | 663,012 | 5,989 | 0.9033% |
| Mens | OTHER | 1,324,227 | 6,877 | 0.5193% | 9,064,252 | 7,150 | 0.0789% |
| Mens | DSE | 757,258 | 3,890 | 0.5137% | 7,759,883 | 3,984 | 0.0513% |
| Mens | APEC | 559,666 | 2,417 | 0.4319% | 5,964,546 | 2,461 | 0.0413% |
| Mens | FLS | 15,690 | 89 | 0.5672% | 25,515 | 90 | 0.3527% |
| Kids | TRANSACTIONAL | 142,612 | 720 | 0.5049% | 268,200 | 761 | 0.2837% |
| Kids | OTHER | 458,232 | 1,852 | 0.4042% | 4,494,478 | 1,918 | 0.0427% |
| Kids | DSE | 0 (no qualifying sends) | — | — | — | — | — |
| Kids | APEC | 0 (no qualifying sends) | — | — | — | — | — |
| Kids | FLS | 0 (no qualifying sends) | — | — | — | — | — |

Column notes: the "full window" columns count each client once, however many months they were sent or reactivated. "Client-months sent" and "Reactivated (month-sum)" count a client once per month they were sent or reactivated, so "Reactivation rate (per month sent)" reflects the odds in a typical month rather than cumulative odds across the full ~17-month window.

# Slide 6: Reactivation Rate by Campaign, Month by Month (All Client States Combined)

- Looking at OTHER, DSE, APEC, and FLS side by side across all 17 months (Lapsed, Dormant, and Dormant 3+ yrs pooled), **FLS ranks highest of the four in every single month (17 of 17)**.
- **APEC ranks lowest of the four in 15 of the 17 months** — including all 7 of the most recent months (November 2025 – May 2026); DSE takes the lowest spot in the other 2 months, and OTHER and FLS are never lowest.
- TRANSACTIONAL is included in the table below for completeness, but its rate (consistently 1-10%) is roughly one to two orders of magnitude above the other four, so it's left off the accompanying chart to keep the marketing categories readable on a shared scale.

Monthly reactivation rate by campaign category, three in-scope client states combined (chart-ready data):

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.1450% | 0.1147% | 0.1054% | 0.3651% | 3.3574% |
| 2025-02 | 0.0695% | 0.0784% | 0.0687% | 0.3376% | 3.1418% |
| 2025-03 | 0.1215% | 0.0931% | 0.0647% | 0.3485% | 3.3090% |
| 2025-04 | 0.1270% | 0.1063% | 0.0587% | 0.3731% | 3.0066% |
| 2025-05 | 0.1041% | 0.0865% | 0.0841% | 0.3978% | 2.9024% |
| 2025-06 | 0.1011% | 0.0767% | 0.1043% | 0.3433% | 0.4151% |
| 2025-07 | 0.1242% | 0.0881% | 0.0206% | 0.3613% | 2.3837% |
| 2025-08 | 0.1055% | 0.0789% | 0.0461% | 0.3613% | 2.7123% |
| 2025-09 | 0.1788% | 0.0739% | 0.1035% | 0.3072% | 2.7398% |
| 2025-10 | 0.1230% | 0.0764% | 0.0230% | 0.2294% | 2.6030% |
| 2025-11 | 0.1294% | 0.0988% | 0.0304% | 0.2817% | 2.4128% |
| 2025-12 | 0.1335% | 0.1007% | 0.0245% | 0.3108% | 1.2790% |
| 2026-01 | 0.1440% | 0.1562% | 0.0323% | 0.3629% | 3.2685% |
| 2026-02 | 0.1607% | 0.1214% | 0.0217% | 0.3381% | 3.2029% |
| 2026-03 | 0.1654% | 0.1614% | 0.0380% | 0.3693% | 3.1795% |
| 2026-04 | 0.1593% | 0.1137% | 0.0358% | 0.5442% | 1.8320% |
| 2026-05 | 0.1643% | 0.1279% | 0.0376% | 0.5198% | 0.7497% |

# Slide 7: Reactivation Rate by Campaign, Month by Month, by Client State

- Splitting the previous slide's pooled view into one panel per client state shows the pooled ranking isn't driven by a single state: **FLS leads the other three marketing categories in Lapsed (13/17 months), Dormant (16/17 months), and Dormant 3+ yrs (17/17 months — every month observed)**.
- **APEC ranks lowest of the four most often in every state**: Lapsed (15/17 months), Dormant (11/17), and Dormant 3+ yrs (10/17).
- Each state keeps its own scale on the accompanying chart, and TRANSACTIONAL is again left off the chart (but included below) for the same readability reason as the previous slide.

Monthly reactivation rate by campaign category, per client state (chart-ready data):

**Lapsed**

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.4330% | 0.3064% | 0.2403% | 0.4146% | 1.2982% |
| 2025-02 | 0.3251% | 0.2222% | 0.1795% | 0.4372% | 1.0144% |
| 2025-03 | 0.3700% | 0.2639% | 0.1801% | 0.4284% | 1.1643% |
| 2025-04 | 0.3568% | 0.2936% | 0.1803% | 0.4161% | 1.1394% |
| 2025-05 | 0.2966% | 0.2500% | 0.2218% | 0.4754% | 0.9074% |
| 2025-06 | 0.3368% | 0.2285% | 0.3152% | 0.4586% | 0.1512% |
| 2025-07 | 0.3651% | 0.2582% | 0.0704% | 0.4157% | 0.7612% |
| 2025-08 | 0.3143% | 0.2298% | 0.1290% | 0.4917% | 1.0521% |
| 2025-09 | 0.3907% | 0.2328% | 0.2629% | 0.3609% | 0.8841% |
| 2025-10 | 0.3244% | 0.2115% | 0.0974% | 0.2742% | 0.8103% |
| 2025-11 | 0.3985% | 0.2779% | 0.0555% | 0.3217% | 0.8637% |
| 2025-12 | 0.3203% | 0.2509% | 0.0540% | 0.3302% | 0.9284% |
| 2026-01 | 0.2568% | 0.2920% | 0.0546% | 0.3970% | 1.0123% |
| 2026-02 | 0.3610% | 0.2606% | 0.0559% | 0.3858% | 0.9766% |
| 2026-03 | 0.3553% | 0.3327% | 0.0683% | 0.4445% | 0.7837% |
| 2026-04 | 0.3270% | 0.2635% | 0.0650% | 0.5907% | 0.3653% |
| 2026-05 | 0.3714% | 0.2853% | 0.0663% | 0.6207% | 0.1785% |

**Dormant**

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.1109% | 0.0981% | 0.1438% | 0.2931% | 3.8629% |
| 2025-02 | 0.0593% | 0.0599% | 0.0964% | 0.1844% | 3.6903% |
| 2025-03 | 0.0879% | 0.0738% | 0.0880% | 0.2156% | 3.7366% |
| 2025-04 | 0.1162% | 0.0895% | 0.0753% | 0.2942% | 3.4297% |
| 2025-05 | 0.0842% | 0.0722% | 0.1171% | 0.2863% | 3.2864% |
| 2025-06 | 0.0752% | 0.0647% | 0.1453% | 0.1797% | 0.3524% |
| 2025-07 | 0.1202% | 0.0791% | 0.0271% | 0.3077% | 2.5248% |
| 2025-08 | 0.0918% | 0.0694% | 0.0636% | 0.1901% | 2.7723% |
| 2025-09 | 0.2780% | 0.0633% | 0.1686% | 0.2223% | 2.9537% |
| 2025-10 | 0.1355% | 0.0776% | 0.0301% | 0.1636% | 2.8806% |
| 2025-11 | 0.0910% | 0.0877% | 0.0367% | 0.2134% | 2.7059% |
| 2025-12 | 0.1394% | 0.1034% | 0.0278% | 0.2826% | 2.0624% |
| 2026-01 | 0.1576% | 0.2105% | 0.0453% | 0.3414% | 3.9579% |
| 2026-02 | 0.1612% | 0.1479% | 0.0187% | 0.2682% | 3.8129% |
| 2026-03 | 0.1610% | 0.1912% | 0.0633% | 0.2427% | 3.8729% |
| 2026-04 | 0.1622% | 0.1192% | 0.0424% | 0.4349% | 2.6247% |
| 2026-05 | 0.1407% | 0.1391% | 0.0541% | 0.3150% | 2.0089% |

**Dormant 3+ yrs**

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.0290% | 0.0236% | 0.0394% | 0.3022% | 7.1702% |
| 2025-02 | 0.0116% | 0.0172% | 0.0263% | 0.1577% | 9.9624% |
| 2025-03 | 0.0241% | 0.0172% | 0.0252% | 0.2127% | 10.0779% |
| 2025-04 | 0.0276% | 0.0245% | 0.0238% | 0.3153% | 8.8915% |
| 2025-05 | 0.0213% | 0.0171% | 0.0345% | 0.2476% | 8.8342% |
| 2025-06 | 0.0176% | 0.0153% | 0.0370% | 0.1509% | 7.4246% |
| 2025-07 | 0.0256% | 0.0184% | 0.0085% | 0.2160% | 7.1940% |
| 2025-08 | 0.0236% | 0.0171% | 0.0199% | 0.1229% | 7.7776% |
| 2025-09 | 0.0711% | 0.0153% | 0.0353% | 0.2220% | 7.7296% |
| 2025-10 | 0.0356% | 0.0217% | 0.0086% | 0.1630% | 7.4312% |
| 2025-11 | 0.0240% | 0.0200% | 0.0154% | 0.2080% | 7.3217% |
| 2025-12 | 0.0356% | 0.0255% | 0.0102% | 0.2303% | 1.2283% |
| 2026-01 | 0.0516% | 0.0488% | 0.0142% | 0.1760% | 7.9914% |
| 2026-02 | 0.0410% | 0.0317% | 0.0099% | 0.1825% | 9.0787% |
| 2026-03 | 0.0471% | 0.0484% | 0.0146% | 0.1548% | 8.8130% |
| 2026-04 | 0.0465% | 0.0272% | 0.0184% | 0.4396% | 7.9191% |
| 2026-05 | 0.0386% | 0.0328% | 0.0141% | 0.2330% | 2.7379% |

---

## Images to add

None. Every chart referenced above is provided as chart-ready tabular data directly under its slide heading, so the add-in can build native, editable PowerPoint charts instead of embedding static images.
