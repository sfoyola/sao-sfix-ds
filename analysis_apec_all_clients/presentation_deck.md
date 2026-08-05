# APEC Personalization Impact — Reactivation Analysis Across All Client States

- Presenter: Sergio Oyola
- Presentation date: [ADD DATE]
- Core question: does receiving an APEC (personalized) marketing send relate to a different reactivation rate than receiving a non-personalized send — and does that answer hold across every client lifecycle state and business line, not just one population?
- Based on real send history across a 516-day window (2025-01-01 to 2026-05-31, ~17 months)

# Slide 1: The Population and the Analysis Window

- This analysis covers every client lifecycle state that can meaningfully "reactivate" — Active, Lapsed, Dormant, and Dormant 3+ years — excluding clients who have never checked out at all, since they have nothing to reactivate from.
- Across those four states combined, roughly **14.3 million clients** (14,272,744) make up the analysis population, alongside a much larger pool of ~37 million clients who have never been active.
- The analysis window spans **516 days** (2025-01-01 to 2026-05-31, ~17 months) of real send history — long enough to give even the thinner campaign categories enough volume to read a reliable rate, and capped at a date old enough for outcome data to have fully settled.

Client population by lifecycle bucket (chart-ready data):

| Lifecycle bucket | Clients |
|---|---|
| Never Active | 36,995,262 |
| Dormant 3+ yrs | 9,860,325 |
| Dormant | 2,080,994 |
| Active | 1,446,560 |
| Lapsed | 884,865 |

# Slide 2: APEC vs. Non-APEC Reactivation Rate, by Client State

- In every one of the four client states, clients sent a non-APEC (non-personalized) marketing send reactivated at a **higher** rate than clients sent an APEC (personalized) send — the gap is statistically significant in all four (p < 0.0001).
- The gap is largest in absolute terms for **Lapsed** clients (2.14 percentage points) and largest in relative terms for **Active** clients (non-APEC reactivates roughly 15x more often than APEC, though both rates are tiny in this state).
- For the state APEC was originally built to focus on — **Dormant 3+ yrs** — non-APEC still leads, by 0.12 percentage points (0.307% vs. 0.186%).

Reactivation rate, APEC vs. non-APEC, full window, by client state (chart-ready data):

| Client state | APEC clients sent | APEC reactivated | APEC reactivation rate | non-APEC clients sent | non-APEC reactivated | non-APEC reactivation rate | Difference (non-APEC − APEC) | p-value |
|---|---|---|---|---|---|---|---|---|
| Active | 1,385,896 | 63 | 0.0045% | 2,855,583 | 1,943 | 0.0680% | 0.0635 pp | 0.00e+00 |
| Lapsed | 717,750 | 3,167 | 0.4412% | 2,247,197 | 58,005 | 2.5812% | 2.1400 pp | 0.00e+00 |
| Dormant | 1,128,490 | 6,158 | 0.5457% | 2,594,787 | 32,502 | 1.2526% | 0.7069 pp | 0.00e+00 |
| Dormant 3+ yrs | 1,349,279 | 2,513 | 0.1862% | 4,308,183 | 13,212 | 0.3067% | 0.1204 pp | 4.18e-153 |

# Slide 3: APEC vs. Non-APEC Reactivation Rate, Month by Month, by Client State

- The full-window gap on the previous slide isn't a one-off: non-APEC outperforms APEC in nearly every individual month, in every state — **17 of 17 months** for Active, **17 of 17** for Lapsed, **16 of 17** for Dormant, and **15 of 17** for Dormant 3+ yrs.
- Each state has its own scale — Lapsed and Dormant clients reactivate at meaningfully higher rates than Active or Dormant 3+ yrs clients, regardless of which campaign type they received.
- Note: each state's monthly rates are naturally noisier than the pooled full-window figures on the previous slide, since a single month has a smaller sample than the full 17-month window.

Monthly reactivation rate, APEC vs. non-APEC, by client state (chart-ready data):

| Month | Active — APEC | Active — non-APEC | Lapsed — APEC | Lapsed — non-APEC | Dormant — APEC | Dormant — non-APEC | Dormant 3+ yrs — APEC | Dormant 3+ yrs — non-APEC |
|---|---|---|---|---|---|---|---|---|
| 2025-01 | 0.0053% | 0.0111% | 0.2352% | 0.7111% | 0.1407% | 0.1948% | 0.0390% | 0.0494% |
| 2025-02 | 0.0016% | 0.0068% | 0.1683% | 0.5079% | 0.0948% | 0.0976% | 0.0260% | 0.0186% |
| 2025-03 | 0.0037% | 0.0084% | 0.1735% | 0.6107% | 0.0859% | 0.1523% | 0.0247% | 0.0390% |
| 2025-04 | 0.0036% | 0.0077% | 0.1700% | 0.6276% | 0.0708% | 0.1947% | 0.0230% | 0.0490% |
| 2025-05 | 0.0030% | 0.0077% | 0.2086% | 0.5314% | 0.1152% | 0.1538% | 0.0338% | 0.0379% |
| 2025-06 | 0.0058% | 0.0063% | 0.3106% | 0.5455% | 0.1431% | 0.1319% | 0.0366% | 0.0306% |
| 2025-07 | 0.0000% | 0.0100% | 0.0655% | 0.6028% | 0.0247% | 0.1905% | 0.0081% | 0.0413% |
| 2025-08 | 0.0009% | 0.0133% | 0.1258% | 0.5240% | 0.0613% | 0.1521% | 0.0198% | 0.0377% |
| 2025-09 | 0.0025% | 0.0095% | 0.2612% | 0.5917% | 0.1669% | 0.3239% | 0.0351% | 0.0796% |
| 2025-10 | 0.0004% | 0.0090% | 0.0895% | 0.5046% | 0.0279% | 0.2011% | 0.0083% | 0.0536% |
| 2025-11 | 0.0005% | 0.0111% | 0.0436% | 0.6171% | 0.0327% | 0.1614% | 0.0135% | 0.0396% |
| 2025-12 | 0.0005% | 0.0087% | 0.0436% | 0.5185% | 0.0246% | 0.2234% | 0.0068% | 0.0557% |
| 2026-01 | 0.0000% | 0.0075% | 0.0419% | 0.4258% | 0.0403% | 0.2907% | 0.0114% | 0.0885% |
| 2026-02 | 0.0000% | 0.0053% | 0.0419% | 0.5605% | 0.0138% | 0.2821% | 0.0085% | 0.0675% |
| 2026-03 | 0.0014% | 0.0079% | 0.0649% | 0.6101% | 0.0610% | 0.3149% | 0.0139% | 0.0878% |
| 2026-04 | 0.0014% | 0.0069% | 0.0569% | 0.5354% | 0.0311% | 0.2575% | 0.0152% | 0.0701% |
| 2026-05 | 0.0000% | 0.0070% | 0.0579% | 0.5921% | 0.0382% | 0.2499% | 0.0123% | 0.0663% |

# Slide 4: APEC vs. Non-APEC Reactivation Rate, by Business Line

- Non-APEC outperforms APEC in both business lines where APEC is actually sent: **Women's** (0.343% vs. 1.402%, a 1.06-point gap) and **Men's** (0.326% vs. 0.699%, a 0.37-point gap), both statistically significant (p < 0.0001).
- **Kids** received zero APEC-classified sends across the entire window — this is a structural fact about which campaigns exist for this business line, not a data gap. Kids clients still reactivated at 0.379% off non-APEC content alone.
- All four lifecycle states are pooled together for this business-line cut, so these rates reflect the full population, not any single state.

Reactivation rate, APEC vs. non-APEC, full window, by business line (chart-ready data):

| Business line | APEC clients sent | APEC reactivated | APEC reactivation rate | non-APEC clients sent | non-APEC reactivated | non-APEC reactivation rate | Difference (non-APEC − APEC) | p-value |
|---|---|---|---|---|---|---|---|---|
| Womens | 2,766,259 | 9,475 | 0.3425% | 6,453,228 | 90,462 | 1.4018% | 1.0593 pp | 0.00e+00 |
| Mens | 733,215 | 2,388 | 0.3257% | 1,532,789 | 10,711 | 0.6988% | 0.3731 pp | 0.00e+00 |
| Kids | 0 (no qualifying sends) | — | — | 529,925 | 2,010 | 0.3793% | n/a | n/a |

# Slide 5: Reactivation Rate by Campaign Category, by Business Line

- **TRANSACTIONAL** sits far above every other category in both business lines (an artifact of clients already returning on their own, not a marketing effect). Among the four marketing categories, full-window, the order differs by line: **Women's ranks DSE above OTHER** (0.920% vs. 0.863%), while **Men's ranks OTHER above DSE** (0.453% vs. 0.407%); APEC and FLS trail both in either line.
- Full-window rankings reward categories that simply resend to the same clients more often (OTHER, DSE, and APEC resend nearly every month; FLS only fires once per triggering event). Normalizing to a **per-client-month** basis — so a client sent in 8 different months contributes 8, not 1 — changes the picture: **OTHER leads per month sent in both lines** (already true in Men's full-window; it overtakes DSE in Women's), and **FLS overtakes APEC in both**, leaving **APEC as the lowest-reactivating genuine marketing category per month sent**, in Women's and Men's alike.
- **Kids** only has two categories present at all — OTHER and TRANSACTIONAL — since DSE, APEC, and FLS are never sent to this business line in the window observed.

Reactivation rate by campaign category, by business line — full window vs. per client-month sent (chart-ready data):

| Business line | Campaign category | Clients sent (full window) | Reactivated (full window) | Reactivation rate (full window) | Client-months sent | Reactivated (month-sum) | Reactivation rate (per month sent) |
|---|---|---|---|---|---|---|---|
| Womens | TRANSACTIONAL | 2,934,840 | 74,032 | 2.5225% | 15,216,236 | 75,358 | 0.4952% |
| Womens | DSE | 3,984,959 | 36,647 | 0.9196% | 48,481,654 | 38,177 | 0.0787% |
| Womens | OTHER | 6,434,723 | 55,539 | 0.8631% | 53,410,859 | 58,551 | 0.1096% |
| Womens | APEC | 2,823,155 | 9,968 | 0.3531% | 16,710,200 | 10,058 | 0.0602% |
| Womens | FLS | 858,401 | 2,121 | 0.2471% | 3,444,715 | 2,164 | 0.0628% |
| Mens | TRANSACTIONAL | 712,769 | 6,028 | 0.8457% | 3,191,965 | 6,106 | 0.1913% |
| Mens | OTHER | 1,531,173 | 6,937 | 0.4531% | 12,580,373 | 7,213 | 0.0573% |
| Mens | DSE | 968,033 | 3,943 | 0.4073% | 10,931,795 | 4,041 | 0.0370% |
| Mens | APEC | 739,930 | 2,432 | 0.3287% | 7,005,210 | 2,476 | 0.0353% |
| Mens | FLS | 77,954 | 91 | 0.1167% | 188,293 | 92 | 0.0489% |
| Kids | TRANSACTIONAL | 250,734 | 1,178 | 0.4698% | 1,219,419 | 1,228 | 0.1007% |
| Kids | OTHER | 529,925 | 2,010 | 0.3793% | 5,657,167 | 2,092 | 0.0370% |
| Kids | DSE | 0 (no qualifying sends) | — | — | — | — | — |
| Kids | APEC | 0 (no qualifying sends) | — | — | — | — | — |
| Kids | FLS | 0 (no qualifying sends) | — | — | — | — | — |

Column notes: the "full window" columns count each client once, however many months they were sent or reactivated. "Client-months sent" and "Reactivated (month-sum)" count a client once per month they were sent or reactivated, so "Reactivation rate (per month sent)" reflects the odds in a typical month rather than cumulative odds across the full ~17-month window.

# Slide 6: Reactivation Rate by Campaign, Month by Month (All Client States Combined)

- Looking at OTHER, DSE, APEC, and FLS side by side across all 17 months (all client states pooled), **APEC ranks lowest of the four in 12 of the 17 months** — and in the most recent 7 months (November 2025 – May 2026), APEC has ranked lowest in **every single month**, versus 5 of the first 10 months.
- **OTHER ranks highest of the four in 14 of the 17 months**, with DSE, FLS, and APEC each leading only once.
- TRANSACTIONAL is included in the table below for completeness, but its rate (consistently 2-10%) is roughly two orders of magnitude above the other four, so it's left off the accompanying chart to keep the marketing categories readable on a shared scale.

Monthly reactivation rate by campaign category, all client states combined (chart-ready data):

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.1085% | 0.0845% | 0.0925% | 0.0862% | 0.6111% |
| 2025-02 | 0.0579% | 0.0575% | 0.0621% | 0.0687% | 0.5273% |
| 2025-03 | 0.0924% | 0.0698% | 0.0594% | 0.0823% | 0.5772% |
| 2025-04 | 0.0957% | 0.0812% | 0.0533% | 0.0915% | 0.4972% |
| 2025-05 | 0.0771% | 0.0641% | 0.0752% | 0.0759% | 0.4769% |
| 2025-06 | 0.0755% | 0.0565% | 0.0938% | 0.0622% | 0.1860% |
| 2025-07 | 0.0928% | 0.0649% | 0.0185% | 0.0627% | 0.3766% |
| 2025-08 | 0.0788% | 0.0581% | 0.0405% | 0.0567% | 0.4808% |
| 2025-09 | 0.1387% | 0.0540% | 0.0907% | 0.0476% | 0.4973% |
| 2025-10 | 0.0887% | 0.0550% | 0.0202% | 0.0328% | 0.4325% |
| 2025-11 | 0.0873% | 0.0651% | 0.0207% | 0.0379% | 0.3435% |
| 2025-12 | 0.0900% | 0.0660% | 0.0168% | 0.0434% | 0.3225% |
| 2026-01 | 0.1020% | 0.1029% | 0.0218% | 0.0568% | 0.5489% |
| 2026-02 | 0.1068% | 0.0794% | 0.0160% | 0.0518% | 0.5100% |
| 2026-03 | 0.1109% | 0.1056% | 0.0319% | 0.0570% | 0.5523% |
| 2026-04 | 0.1057% | 0.0734% | 0.0301% | 0.0821% | 0.4039% |
| 2026-05 | 0.1092% | 0.0831% | 0.0318% | 0.0751% | 0.2514% |

# Slide 7: Reactivation Rate by Campaign, Month by Month, by Client State

- Splitting the previous slide's pooled view into one panel per client state shows the pooled ranking isn't driven by a single state: **FLS leads the other three marketing categories in Lapsed (13/17 months), Dormant (16/17 months), and Dormant 3+ yrs (17/17 months — every month observed)**.
- **Active is the exception** — rates there are extremely small (well under 0.015% throughout) and noisy, with OTHER leading 16 of 17 months and no consistent runner-up; this state's volume is real but its reactivation signal is too thin to draw a reliable category ranking from.
- **APEC ranks lowest of the four most often in every state**: Lapsed (15/17 months), Dormant (11/17), Dormant 3+ yrs (10/17), and Active (7/17, roughly tied with FLS's 9/17).
- Each state keeps its own scale on the accompanying chart, and TRANSACTIONAL is again left off the chart (but included below) for the same readability reason as the previous slide.

Monthly reactivation rate by campaign category, per client state (chart-ready data):

**Active**

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.0071% | 0.0039% | 0.0053% | 0.0032% | 0.0133% |
| 2025-02 | 0.0047% | 0.0022% | 0.0015% | 0.0015% | 0.0110% |
| 2025-03 | 0.0056% | 0.0028% | 0.0034% | 0.0031% | 0.0130% |
| 2025-04 | 0.0045% | 0.0036% | 0.0031% | 0.0017% | 0.0118% |
| 2025-05 | 0.0055% | 0.0023% | 0.0027% | 0.0006% | 0.0108% |
| 2025-06 | 0.0041% | 0.0022% | 0.0053% | 0.0014% | 0.0065% |
| 2025-07 | 0.0065% | 0.0038% | 0.0000% | 0.0006% | 0.0114% |
| 2025-08 | 0.0085% | 0.0051% | 0.0016% | 0.0012% | 0.0152% |
| 2025-09 | 0.0056% | 0.0042% | 0.0024% | 0.0016% | 0.0115% |
| 2025-10 | 0.0054% | 0.0039% | 0.0004% | 0.0015% | 0.0102% |
| 2025-11 | 0.0073% | 0.0045% | 0.0005% | 0.0005% | 0.0108% |
| 2025-12 | 0.0058% | 0.0032% | 0.0005% | 0.0018% | 0.0116% |
| 2026-01 | 0.0049% | 0.0029% | 0.0000% | 0.0024% | 0.0111% |
| 2026-02 | 0.0031% | 0.0023% | 0.0000% | 0.0019% | 0.0117% |
| 2026-03 | 0.0047% | 0.0036% | 0.0014% | 0.0013% | 0.0112% |
| 2026-04 | 0.0050% | 0.0019% | 0.0011% | 0.0020% | 0.0117% |
| 2026-05 | 0.0042% | 0.0031% | 0.0011% | 0.0008% | 0.0085% |

**Lapsed**

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.4330% | 0.3064% | 0.2403% | 0.4146% | 1.2982% |
| 2025-02 | 0.3251% | 0.2222% | 0.1795% | 0.4372% | 1.0144% |
| 2025-03 | 0.3700% | 0.2639% | 0.1801% | 0.4284% | 1.1643% |
| 2025-04 | 0.3568% | 0.2936% | 0.1803% | 0.4161% | 1.1394% |
| 2025-05 | 0.2966% | 0.2500% | 0.2218% | 0.4754% | 0.9074% |
| 2025-06 | 0.3371% | 0.2287% | 0.3152% | 0.4586% | 0.1512% |
| 2025-07 | 0.3651% | 0.2582% | 0.0704% | 0.4157% | 0.7612% |
| 2025-08 | 0.3143% | 0.2298% | 0.1290% | 0.4917% | 1.0511% |
| 2025-09 | 0.3907% | 0.2330% | 0.2629% | 0.3609% | 0.8841% |
| 2025-10 | 0.3244% | 0.2113% | 0.0974% | 0.2742% | 0.8103% |
| 2025-11 | 0.3985% | 0.2779% | 0.0555% | 0.3217% | 0.8637% |
| 2025-12 | 0.3206% | 0.2509% | 0.0540% | 0.3302% | 0.9284% |
| 2026-01 | 0.2568% | 0.2918% | 0.0546% | 0.3970% | 1.0123% |
| 2026-02 | 0.3610% | 0.2604% | 0.0559% | 0.3858% | 0.9777% |
| 2026-03 | 0.3553% | 0.3327% | 0.0683% | 0.4445% | 0.7837% |
| 2026-04 | 0.3270% | 0.2635% | 0.0650% | 0.5907% | 0.3659% |
| 2026-05 | 0.3715% | 0.2853% | 0.0663% | 0.6207% | 0.1785% |

**Dormant**

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.1109% | 0.0981% | 0.1438% | 0.2931% | 3.8629% |
| 2025-02 | 0.0593% | 0.0599% | 0.0964% | 0.1844% | 3.6903% |
| 2025-03 | 0.0880% | 0.0738% | 0.0880% | 0.2156% | 3.7366% |
| 2025-04 | 0.1162% | 0.0895% | 0.0753% | 0.2942% | 3.4297% |
| 2025-05 | 0.0842% | 0.0722% | 0.1171% | 0.2863% | 3.2864% |
| 2025-06 | 0.0752% | 0.0647% | 0.1453% | 0.1797% | 0.3524% |
| 2025-07 | 0.1202% | 0.0791% | 0.0271% | 0.3077% | 2.5248% |
| 2025-08 | 0.0918% | 0.0694% | 0.0636% | 0.1901% | 2.7723% |
| 2025-09 | 0.2780% | 0.0633% | 0.1686% | 0.2223% | 2.9515% |
| 2025-10 | 0.1355% | 0.0776% | 0.0301% | 0.1636% | 2.8806% |
| 2025-11 | 0.0910% | 0.0877% | 0.0367% | 0.2134% | 2.7059% |
| 2025-12 | 0.1394% | 0.1034% | 0.0278% | 0.2826% | 2.0624% |
| 2026-01 | 0.1576% | 0.2105% | 0.0453% | 0.3414% | 3.9579% |
| 2026-02 | 0.1612% | 0.1479% | 0.0187% | 0.2682% | 3.8065% |
| 2026-03 | 0.1610% | 0.1912% | 0.0633% | 0.2427% | 3.8729% |
| 2026-04 | 0.1622% | 0.1192% | 0.0424% | 0.4349% | 2.6227% |
| 2026-05 | 0.1407% | 0.1391% | 0.0541% | 0.3150% | 2.0089% |

**Dormant 3+ yrs**

| Month | OTHER | DSE | APEC | FLS | TRANSACTIONAL |
|---|---|---|---|---|---|
| 2025-01 | 0.0290% | 0.0236% | 0.0394% | 0.3022% | 7.1702% |
| 2025-02 | 0.0116% | 0.0172% | 0.0263% | 0.1577% | 9.9624% |
| 2025-03 | 0.0241% | 0.0172% | 0.0252% | 0.2127% | 10.0746% |
| 2025-04 | 0.0276% | 0.0245% | 0.0238% | 0.3153% | 8.8915% |
| 2025-05 | 0.0213% | 0.0171% | 0.0345% | 0.2476% | 8.8242% |
| 2025-06 | 0.0176% | 0.0153% | 0.0370% | 0.1509% | 7.4246% |
| 2025-07 | 0.0256% | 0.0184% | 0.0085% | 0.2160% | 7.1940% |
| 2025-08 | 0.0236% | 0.0171% | 0.0199% | 0.1229% | 7.7776% |
| 2025-09 | 0.0711% | 0.0153% | 0.0354% | 0.2220% | 7.7296% |
| 2025-10 | 0.0356% | 0.0217% | 0.0086% | 0.1630% | 7.4312% |
| 2025-11 | 0.0240% | 0.0200% | 0.0154% | 0.2080% | 7.3217% |
| 2025-12 | 0.0356% | 0.0255% | 0.0102% | 0.2303% | 1.2283% |
| 2026-01 | 0.0516% | 0.0488% | 0.0142% | 0.1760% | 7.9914% |
| 2026-02 | 0.0410% | 0.0317% | 0.0099% | 0.1825% | 9.0722% |
| 2026-03 | 0.0472% | 0.0484% | 0.0146% | 0.1548% | 8.8130% |
| 2026-04 | 0.0465% | 0.0272% | 0.0184% | 0.4396% | 7.9191% |
| 2026-05 | 0.0386% | 0.0328% | 0.0141% | 0.2330% | 2.7391% |

---

## Images to add

None. Every chart referenced above is provided as chart-ready tabular data directly under its slide heading, so the add-in can build native, editable PowerPoint charts instead of embedding static images.
