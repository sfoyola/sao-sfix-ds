# Campaign Category Reactivation Analysis — Decomposing "Other" Marketing Content

- Presenter: Sergio Oyola
- Presentation date: [ADD DATE]
- Core question: which campaign categories actually drive client reactivation, and what was really inside the generic "Other" marketing bucket that made it look stronger than it is?
- Based on real send history across a 516-day window (2025-01-01 to 2026-05-31, ~17 months), across three client lifecycle states

# Slide 1: Client Lifecycle States

- Every client is bucketed into one of three states based on how long it's been since their last checkout — the further out a client is, the harder they generally are to bring back, which is why the analysis treats each state separately rather than pooling everyone into one number.
- A client's state is evaluated **as of each specific send**, not as of today — a client who moved between states over the analysis window is correctly bucketed for every send they received, whether that send landed while they were Lapsed or after they'd drifted further into Dormant or Dormant 3+ yrs.
- Clients with no checkout at all ("Never Active") are excluded from every part of this analysis — a client who has never checked out has nothing to reactivate from.
- **Active clients (≤ 120 days since last checkout) are also out of scope.** The reactivation-demand data this analysis relies on (`curated.client_reactivation_demand_events`) only ever logs a demand event for a client returning from Lapsed or Dormant — it has zero rows for clients who were still Active at the time, so this metric structurally cannot measure Active-client conversion.

Client lifecycle states in scope (chart-ready data):

| State | Definition (days since last checkout, as of the send) |
|---|---|
| Lapsed | 121–365 days |
| Dormant | 366–1,095 days |
| Dormant 3+ yrs | > 1,095 days |

# Slide 2: Population and Analysis Window

- This analysis covers three client lifecycle states that can meaningfully "reactivate" — Lapsed, Dormant, and Dormant 3+ years — excluding clients who have never checked out at all (nothing to reactivate from) and excluding Active clients for the structural data-availability reason on the previous slide.
- Across those three states combined, roughly **12.9 million clients** (12,890,073) make up the analysis population, alongside a much larger pool of ~37.2 million clients who have never been active.
- The analysis window spans **516 days** (2025-01-01 to 2026-05-31, ~17 months) of real send history — long enough to give even the thinner campaign categories enough volume to read a reliable monthly rate, and capped at a date old enough for outcome data to have fully settled.

Client population by lifecycle bucket (chart-ready data):

| Lifecycle bucket | Clients |
|---|---|
| Never Active | 37,158,690 |
| Dormant 3+ yrs | 9,929,139 |
| Dormant | 2,057,567 |
| Lapsed | 903,367 |

# Slide 3: Why These Categories

- Campaigns are grouped by what actually appears in the campaign name, not by a verified per-send flag (no such flag exists) — each send is assigned to the *first* category it matches, checked in a specific, deliberate order, since several categories' naming conventions overlap.
- **A single blended "Other" bucket used to hide very different content.** Generic marketing, promotional/incentive sends, plain reactivation messaging, birthday sends, and post-Fix cross-sell were all being counted as one "Other" category with one blended rate — masking very different reactivation behavior underneath.
- **Decomposing it changes the picture.** Isolating the categories below shows that DSE and promotional/incentive content — not generic marketing — are the real high-volume drivers hiding inside the old "Other" bucket. Once those are pulled out, the true "Other" remainder reactivates at 0.3940%, meaningfully behind APEC's personalized content at 0.4710% — generic, unpersonalized marketing underperforms APEC once it's isolated from the higher-performing content it used to be blended with.
- **The category order resolves real naming overlaps found in the data** — for example, a one-time mass reactivation offer test shares FLS's naming convention by coincidence, so it's checked and routed to PROMO_INCENTIVE *before* the FLS check, ahead of being misread as a genuine behavioral FLS trigger; and the general promotional keyword match (which includes "sale") is deliberately checked *after* FLS, so a genuine FLS "saved item now on sale" trigger isn't misclassified as a promotional send.

Reactivation rate by category, full window, three in-scope client states combined (chart-ready data):

| Category | Clients sent | Reactivated | Reactivation rate |
|---|---|---|---|
| TRANSACTIONAL | 2,590,264 | 79,503 | 3.0693% |
| DSE | 3,949,149 | 39,972 | 1.0122% |
| FLS | 279,216 | 2,169 | 0.7768% |
| PROMO_INCENTIVE | 5,167,055 | 32,183 | 0.6228% |
| APEC | 2,618,376 | 12,333 | 0.4710% |
| OTHER (true remainder) | 6,742,912 | 26,566 | 0.3940% |
| BIRTHDAY | 3,267,582 | 4,017 | 0.1229% |
| WINBACK | 2,827,928 | 1,988 | 0.0703% |
| TRACKING_ARTIFACT | 1,132,254 | 0 | 0.0000% |
| CROSSSELL | 19 | 0 | 0.0000% |

How each category is identified, in the order it's checked (chart-ready data):

| Order | Category | What it captures |
|---|---|---|
| 1 | APEC | Algorithmic Personalized Email Content — names containing "apec", plus its confirmed browse-abandon win-back triggers, StylePass onboarding messages, and style-profile reactivation pushes. |
| 2 | TRANSACTIONAL | Account-service email (password resets, order/Fix status confirmations) — a client only receives one because they're already taking an action on their account, not because of a marketing choice. |
| 3 | DSE | Dynamic Shoppable Email, including its TFY and CYL content variants. |
| 4 | PROMO_INCENTIVE (partial) | A one-time mass reactivation offer test (control/test arms) — its name happens to also contain FLS's naming convention, so it's checked and routed here before the FLS check below, ahead of being misread as a behavioral FLS trigger. |
| 5 | FLS | Freestyle Lifecycle Series — behaviorally triggered sends after a high-intent event (cart abandonment, a saved item still on sale), identified by an explicit "freestyle-lifecycle" naming convention. |
| 6 | TRACKING_ARTIFACT | The single `crumbs_has_app` tag — a uniform internal event marker, not a real send with real creative content. |
| 7 | PROMO_INCENTIVE (remainder) | Campaign names referencing an offer, discount, sale, percent-off, markdown, deal, coupon, a "spend X get Y" mechanic, a last-chance framing, a credit, an incentive, or a waived styling fee. |
| 8 | WINBACK | Campaign names explicitly branded as reactivation or win-back messaging, with no financial incentive attached (that combination is already captured by PROMO_INCENTIVE above). |
| 9 | BIRTHDAY | Birthday-triggered sends. |
| 10 | CROSSSELL | Post-Fix cross-sell sends. |
| 11 | OTHER | Everything else — generic seasonal, thematic, and welcome/onboarding marketing content with no personalization-, promotion-, or lifecycle-event-suggestive naming. |

# Slide 4: Reactivation Rate by Campaign, Month by Month (Three In-Scope Client States Combined)

- Pooled across the three in-scope client lifecycle states, **FLS reactivates at by far the highest average monthly rate among genuine marketing categories (0.3619%)** — more than 3.5x DSE's 0.1031%, the next-highest; TRANSACTIONAL sits far above all of them (2.4997% average) as an artifact of clients already returning on their own, not a marketing effect.
- **DSE (0.1031%), PROMO_INCENTIVE (0.0867%), BIRTHDAY (0.0622%), OTHER (0.0597%), and APEC (0.0529%)** form a middle cluster, each within roughly 0.05 points of one another.
- **CROSSSELL and WINBACK are the weakest performers** — CROSSSELL reactivated 0 of the 19 clients it was ever sent across the entire window (it's essentially an Active-only mechanic, see Slide 18), and WINBACK averages 0.0231%, the lowest among categories with meaningful volume.
- TRACKING_ARTIFACT only has recorded volume in 9 of the 17 months (it isn't sent every month), and reactivates at exactly 0.0000% in every one of those months — confirming it carries no reactivation signal at all.

Monthly reactivation rate by campaign category, three in-scope client states combined (chart-ready data):

| Month | APEC | DSE | FLS | TRANSACTIONAL | PROMO_INCENTIVE | WINBACK | BIRTHDAY | CROSSSELL | TRACKING_ARTIFACT | OTHER |
|---|---|---|---|---|---|---|---|---|---|---|
| 2025-01 | 0.1054% | 0.1147% | 0.3651% | 3.3574% | 0.0916% | 0.0037% | 0.1080% | n/a | n/a | 0.0531% |
| 2025-02 | 0.0687% | 0.0784% | 0.3376% | 3.1418% | 0.0889% | 0.0077% | 0.0211% | 0.0000% | n/a | 0.0291% |
| 2025-03 | 0.0647% | 0.0931% | 0.3485% | 3.3090% | 0.0985% | 0.0215% | 0.0756% | 0.0000% | n/a | 0.0555% |
| 2025-04 | 0.0587% | 0.1063% | 0.3731% | 3.0066% | 0.0976% | 0.0044% | 0.0619% | 0.0000% | n/a | 0.0619% |
| 2025-05 | 0.0841% | 0.0865% | 0.3978% | 2.9024% | 0.0516% | 0.0197% | 0.0593% | 0.0000% | n/a | 0.0486% |
| 2025-06 | 0.1043% | 0.0767% | 0.3433% | 0.4151% | 0.1007% | 0.0051% | 0.0517% | n/a | n/a | 0.0480% |
| 2025-07 | 0.0206% | 0.0881% | 0.3613% | 2.3837% | 0.0775% | 0.0073% | 0.0562% | 0.0000% | n/a | 0.0468% |
| 2025-08 | 0.0461% | 0.0789% | 0.3613% | 2.7123% | 0.0574% | 0.1087% | 0.0668% | n/a | n/a | 0.0491% |
| 2025-09 | 0.1035% | 0.0739% | 0.3072% | 2.7398% | 0.1182% | 0.1022% | 0.0668% | 0.0000% | 0.0000% | 0.0455% |
| 2025-10 | 0.0230% | 0.0764% | 0.2294% | 2.6030% | 0.0596% | 0.0049% | 0.0610% | n/a | 0.0000% | 0.0670% |
| 2025-11 | 0.0304% | 0.0988% | 0.2817% | 2.4128% | 0.0994% | 0.0258% | 0.0640% | n/a | 0.0000% | 0.0395% |
| 2025-12 | 0.0245% | 0.1007% | 0.3108% | 1.2790% | 0.0896% | 0.0000% | 0.0560% | 0.0000% | 0.0000% | 0.0498% |
| 2026-01 | 0.0323% | 0.1562% | 0.3629% | 3.2685% | 0.0859% | 0.0282% | 0.0786% | 0.0000% | 0.0000% | 0.0737% |
| 2026-02 | 0.0217% | 0.1214% | 0.3381% | 3.2029% | 0.0949% | 0.0100% | 0.0192% | 0.0000% | 0.0000% | 0.0770% |
| 2026-03 | 0.0380% | 0.1614% | 0.3693% | 3.1795% | 0.1010% | 0.0122% | 0.0771% | 0.0000% | 0.0000% | 0.0784% |
| 2026-04 | 0.0358% | 0.1137% | 0.5442% | 1.8320% | 0.0867% | 0.0306% | 0.0765% | n/a | 0.0000% | 0.0859% |
| 2026-05 | 0.0376% | 0.1279% | 0.5198% | 0.7497% | 0.0751% | 0.0000% | 0.0578% | n/a | 0.0000% | 0.1061% |

Chart excludes TRANSACTIONAL and TRACKING_ARTIFACT to keep the eight genuine campaign categories readable on a shared scale (TRANSACTIONAL's rate is roughly an order of magnitude above the rest; TRACKING_ARTIFACT is a flat zero).

# Slide 5: Reactivation Rate by Campaign, Month by Month (By Client State)

- **Lapsed is where every genuine marketing category reactivates best.** APEC, DSE, FLS, PROMO_INCENTIVE, BIRTHDAY, and OTHER all post their highest average monthly rate in the Lapsed state — e.g. DSE averages 0.2623% in Lapsed versus just 0.0248% in Dormant 3+ yrs.
- **Dormant 3+ yrs is the weakest of the three in-scope states for nearly every category** — e.g. APEC averages just 0.0209% there, well below Lapsed's 0.1351% and Dormant's 0.0731%.
- **CROSSSELL barely exists in this analysis' population at all** — across Lapsed, Dormant, and Dormant 3+ yrs combined, it was sent to only 19 clients total over the full 17-month window (present in just 7, 6, and 3 of the 17 months per state, respectively), with zero reactivations recorded. It's a post-Fix cross-sell send that structurally reaches clients who just checked out — a population this analysis excludes by design (see Slide 1) — so it has almost no presence here.
- **WINBACK has real gaps in its send history for the more dormant states** — it wasn't sent at all in 4 of 17 months to Dormant clients and 5 of 17 months to Dormant 3+ yrs clients, versus full 17-month coverage in Lapsed.

Monthly reactivation rate by campaign category, per client state (chart-ready data):

**Lapsed**

| Month | APEC | DSE | FLS | TRANSACTIONAL | PROMO_INCENTIVE | WINBACK | BIRTHDAY | CROSSSELL | TRACKING_ARTIFACT | OTHER |
|---|---|---|---|---|---|---|---|---|---|---|
| 2025-01 | 0.2403% | 0.3064% | 0.4146% | 1.2982% | 0.2719% | 0.0158% | 0.2808% | n/a | n/a | 0.1652% |
| 2025-02 | 0.1795% | 0.2222% | 0.4372% | 1.0144% | 0.2629% | 0.0258% | 0.0557% | 0.0000% | n/a | 0.1441% |
| 2025-03 | 0.1801% | 0.2639% | 0.4284% | 1.1643% | 0.2715% | 0.0573% | 0.2106% | 0.0000% | n/a | 0.1822% |
| 2025-04 | 0.1803% | 0.2936% | 0.4161% | 1.1394% | 0.2319% | 0.0154% | 0.1536% | 0.0000% | n/a | 0.2170% |
| 2025-05 | 0.2218% | 0.2500% | 0.4754% | 0.9074% | 0.1471% | 0.0197% | 0.1668% | 0.0000% | n/a | 0.1553% |
| 2025-06 | 0.3152% | 0.2285% | 0.4586% | 0.1512% | 0.3433% | 0.0211% | 0.1412% | n/a | n/a | 0.1725% |
| 2025-07 | 0.0704% | 0.2582% | 0.4157% | 0.7612% | 0.2324% | 0.0336% | 0.1285% | 0.0000% | n/a | 0.1443% |
| 2025-08 | 0.1290% | 0.2298% | 0.4917% | 1.0521% | 0.1728% | 0.1087% | 0.1815% | n/a | n/a | 0.1599% |
| 2025-09 | 0.2629% | 0.2328% | 0.3609% | 0.8841% | 0.1470% | 0.4669% | 0.1573% | n/a | 0.0000% | 0.1699% |
| 2025-10 | 0.0974% | 0.2115% | 0.2742% | 0.8103% | 0.1461% | 0.0000% | 0.1345% | n/a | 0.0000% | 0.2172% |
| 2025-11 | 0.0555% | 0.2779% | 0.3217% | 0.8637% | 0.3333% | 0.0258% | 0.2060% | n/a | 0.0000% | 0.1221% |
| 2025-12 | 0.0540% | 0.2509% | 0.3302% | 0.9284% | 0.2253% | 0.0000% | 0.1735% | 0.0000% | 0.0000% | 0.1539% |
| 2026-01 | 0.0546% | 0.2920% | 0.3970% | 1.0123% | 0.1462% | 0.0494% | 0.2329% | n/a | 0.0000% | 0.1739% |
| 2026-02 | 0.0559% | 0.2606% | 0.3858% | 0.9766% | 0.2128% | 0.0184% | 0.0513% | n/a | 0.0000% | 0.2256% |
| 2026-03 | 0.0683% | 0.3327% | 0.4445% | 0.7837% | 0.2437% | 0.0206% | 0.2158% | 0.0000% | 0.0000% | 0.1913% |
| 2026-04 | 0.0650% | 0.2635% | 0.5907% | 0.3653% | 0.2186% | 0.0000% | 0.1977% | n/a | 0.0000% | 0.1842% |
| 2026-05 | 0.0663% | 0.2853% | 0.6207% | 0.1785% | 0.2426% | 0.0000% | 0.1475% | n/a | 0.0000% | 0.2250% |

**Dormant**

| Month | APEC | DSE | FLS | TRANSACTIONAL | PROMO_INCENTIVE | WINBACK | BIRTHDAY | CROSSSELL | TRACKING_ARTIFACT | OTHER |
|---|---|---|---|---|---|---|---|---|---|---|
| 2025-01 | 0.1438% | 0.0981% | 0.2931% | 3.8629% | 0.0754% | 0.0015% | 0.1045% | n/a | n/a | 0.0364% |
| 2025-02 | 0.0964% | 0.0599% | 0.1844% | 3.6903% | 0.0662% | 0.0039% | 0.0193% | n/a | n/a | 0.0228% |
| 2025-03 | 0.0880% | 0.0738% | 0.2156% | 3.7366% | 0.0833% | 0.0148% | 0.0704% | 0.0000% | n/a | 0.0338% |
| 2025-04 | 0.0753% | 0.0895% | 0.2942% | 3.4297% | 0.1214% | 0.0000% | 0.0670% | 0.0000% | n/a | 0.0376% |
| 2025-05 | 0.1171% | 0.0722% | 0.2863% | 3.2864% | 0.0470% | n/a | 0.0584% | 0.0000% | n/a | 0.0333% |
| 2025-06 | 0.1453% | 0.0647% | 0.1797% | 0.3524% | 0.0808% | 0.0026% | 0.0560% | n/a | n/a | 0.0322% |
| 2025-07 | 0.0271% | 0.0791% | 0.3077% | 2.5248% | 0.0797% | 0.0040% | 0.0638% | n/a | n/a | 0.0414% |
| 2025-08 | 0.0636% | 0.0694% | 0.1901% | 2.7723% | 0.0572% | n/a | 0.0705% | n/a | n/a | 0.0356% |
| 2025-09 | 0.1686% | 0.0633% | 0.2223% | 2.9537% | 0.2171% | 0.1203% | 0.0802% | 0.0000% | 0.0000% | 0.0326% |
| 2025-10 | 0.0301% | 0.0776% | 0.1636% | 2.8806% | 0.0734% | 0.0093% | 0.0791% | n/a | 0.0000% | 0.0641% |
| 2025-11 | 0.0367% | 0.0877% | 0.2134% | 2.7059% | 0.0620% | n/a | 0.0562% | n/a | 0.0000% | 0.0349% |
| 2025-12 | 0.0278% | 0.1034% | 0.2826% | 2.0624% | 0.1075% | n/a | 0.0476% | n/a | 0.0000% | 0.0419% |
| 2026-01 | 0.0453% | 0.2105% | 0.3414% | 3.9579% | 0.1273% | 0.0481% | 0.0798% | n/a | 0.0000% | 0.0576% |
| 2026-02 | 0.0187% | 0.1479% | 0.2682% | 3.8129% | 0.1120% | 0.0277% | 0.0209% | 0.0000% | 0.0000% | 0.0554% |
| 2026-03 | 0.0633% | 0.1912% | 0.2427% | 3.8729% | 0.0971% | 0.0253% | 0.0907% | 0.0000% | 0.0000% | 0.0753% |
| 2026-04 | 0.0424% | 0.1192% | 0.4349% | 2.6247% | 0.0816% | 0.0408% | 0.0924% | n/a | 0.0000% | 0.0990% |
| 2026-05 | 0.0541% | 0.1391% | 0.3150% | 2.0089% | 0.0359% | 0.0000% | 0.0701% | n/a | 0.0000% | 0.1216% |

**Dormant 3+ yrs**

| Month | APEC | DSE | FLS | TRANSACTIONAL | PROMO_INCENTIVE | WINBACK | BIRTHDAY | CROSSSELL | TRACKING_ARTIFACT | OTHER |
|---|---|---|---|---|---|---|---|---|---|---|
| 2025-01 | 0.0394% | 0.0236% | 0.3022% | 7.1702% | 0.0154% | 0.0005% | 0.0378% | n/a | n/a | 0.0115% |
| 2025-02 | 0.0263% | 0.0172% | 0.1577% | 9.9624% | 0.0191% | 0.0010% | 0.0069% | n/a | n/a | 0.0041% |
| 2025-03 | 0.0252% | 0.0172% | 0.2127% | 10.0779% | 0.0204% | 0.0000% | 0.0242% | n/a | n/a | 0.0095% |
| 2025-04 | 0.0238% | 0.0245% | 0.3153% | 8.8915% | 0.0272% | 0.0000% | 0.0222% | n/a | n/a | 0.0080% |
| 2025-05 | 0.0345% | 0.0171% | 0.2476% | 8.8342% | 0.0135% | n/a | 0.0190% | n/a | n/a | 0.0059% |
| 2025-06 | 0.0370% | 0.0153% | 0.1509% | 7.4246% | 0.0212% | 0.0006% | 0.0160% | n/a | n/a | 0.0057% |
| 2025-07 | 0.0085% | 0.0184% | 0.2160% | 7.1940% | 0.0145% | 0.0004% | 0.0252% | n/a | n/a | 0.0097% |
| 2025-08 | 0.0199% | 0.0171% | 0.1229% | 7.7776% | 0.0122% | n/a | 0.0237% | n/a | n/a | 0.0104% |
| 2025-09 | 0.0353% | 0.0153% | 0.2220% | 7.7296% | 0.0622% | 0.0244% | 0.0286% | 0.0000% | 0.0000% | 0.0059% |
| 2025-10 | 0.0086% | 0.0217% | 0.1630% | 7.4312% | 0.0207% | 0.0024% | 0.0281% | n/a | 0.0000% | 0.0139% |
| 2025-11 | 0.0154% | 0.0200% | 0.2080% | 7.3217% | 0.0152% | n/a | 0.0264% | n/a | 0.0000% | 0.0078% |
| 2025-12 | 0.0102% | 0.0255% | 0.2303% | 1.2283% | 0.0232% | n/a | 0.0243% | n/a | 0.0000% | 0.0106% |
| 2026-01 | 0.0142% | 0.0488% | 0.1760% | 7.9914% | 0.0328% | 0.0152% | 0.0286% | 0.0000% | 0.0000% | 0.0151% |
| 2026-02 | 0.0099% | 0.0317% | 0.1825% | 9.0787% | 0.0261% | 0.0013% | 0.0067% | n/a | 0.0000% | 0.0142% |
| 2026-03 | 0.0146% | 0.0484% | 0.1548% | 8.8130% | 0.0256% | 0.0063% | 0.0241% | 0.0000% | 0.0000% | 0.0205% |
| 2026-04 | 0.0184% | 0.0272% | 0.4396% | 7.9191% | 0.0198% | 0.0201% | 0.0273% | n/a | 0.0000% | 0.0251% |
| 2026-05 | 0.0141% | 0.0328% | 0.2330% | 2.7379% | 0.0081% | n/a | 0.0205% | n/a | 0.0000% | 0.0299% |

("n/a" indicates the category had no qualifying sends in that state that month, not a rate of zero.) Each state keeps its own scale on the accompanying chart; TRANSACTIONAL and TRACKING_ARTIFACT are again left off the chart for the same readability reason as Slide 4.

# Slide 6: APEC — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (Three In-Scope Client States Combined)

- Algorithmic Personalized Email Content — campaign names containing "apec", plus its confirmed browse-abandon, StylePass, and style-profile triggers.
- Pooled across the three in-scope states, APEC averages **0.0529%** monthly reactivation on roughly 1,201,664 clients sent per month, reactivating an average of 733 clients each month (12,466 total across the window).
- The monthly rate ranges from 0.0206% to 0.1054% — a roughly 5.1x spread between its weakest and strongest month, with no single month or run of months dominating the average.

APEC monthly reactivation rate, unique clients sent, and reactivated clients, three in-scope client states combined (chart-ready data):

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 1,743,593 | 1,837 | 0.1054% |
| 2025-02 | 1,650,923 | 1,135 | 0.0687% |
| 2025-03 | 1,636,503 | 1,059 | 0.0647% |
| 2025-04 | 1,615,859 | 948 | 0.0587% |
| 2025-05 | 1,595,278 | 1,341 | 0.0841% |
| 2025-06 | 1,586,816 | 1,655 | 0.1043% |
| 2025-07 | 1,543,867 | 318 | 0.0206% |
| 2025-08 | 1,551,866 | 716 | 0.0461% |
| 2025-09 | 1,589,147 | 1,645 | 0.1035% |
| 2025-10 | 1,626,872 | 374 | 0.0230% |
| 2025-11 | 408,168 | 124 | 0.0304% |
| 2025-12 | 416,096 | 102 | 0.0245% |
| 2026-01 | 427,045 | 138 | 0.0323% |
| 2026-02 | 423,730 | 92 | 0.0217% |
| 2026-03 | 1,762,021 | 670 | 0.0380% |
| 2026-04 | 425,105 | 152 | 0.0358% |
| 2026-05 | 425,392 | 160 | 0.0376% |

# Slide 7: APEC — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (By Client State)

- **Lapsed** has the highest average monthly reactivation rate for APEC (0.1351%), versus **Dormant 3+ yrs**'s 0.0209% — the lowest of the three in-scope states.
- **Dormant 3+ yrs** receives the most APEC volume on average (652,239 clients/month); Dormant averages 431,008/month, Lapsed averages 137,477/month.

**Lapsed**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 226,803 | 545 | 0.2403% |
| 2025-02 | 159,927 | 287 | 0.1795% |
| 2025-03 | 155,444 | 280 | 0.1801% |
| 2025-04 | 152,006 | 274 | 0.1803% |
| 2025-05 | 148,775 | 330 | 0.2218% |
| 2025-06 | 145,283 | 458 | 0.3152% |
| 2025-07 | 129,342 | 91 | 0.0704% |
| 2025-08 | 138,035 | 178 | 0.1290% |
| 2025-09 | 139,952 | 368 | 0.2629% |
| 2025-10 | 128,275 | 125 | 0.0974% |
| 2025-11 | 77,470 | 43 | 0.0555% |
| 2025-12 | 77,831 | 42 | 0.0540% |
| 2026-01 | 78,743 | 43 | 0.0546% |
| 2026-02 | 80,537 | 45 | 0.0559% |
| 2026-03 | 325,049 | 222 | 0.0683% |
| 2026-04 | 86,126 | 56 | 0.0650% |
| 2026-05 | 87,506 | 58 | 0.0663% |

**Dormant**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 654,858 | 942 | 0.1438% |
| 2025-02 | 638,675 | 616 | 0.0964% |
| 2025-03 | 633,085 | 557 | 0.0880% |
| 2025-04 | 617,866 | 465 | 0.0753% |
| 2025-05 | 604,722 | 708 | 0.1171% |
| 2025-06 | 601,013 | 873 | 0.1453% |
| 2025-07 | 568,370 | 154 | 0.0271% |
| 2025-08 | 575,206 | 366 | 0.0636% |
| 2025-09 | 567,516 | 957 | 0.1686% |
| 2025-10 | 552,396 | 166 | 0.0301% |
| 2025-11 | 136,352 | 50 | 0.0367% |
| 2025-12 | 140,165 | 39 | 0.0278% |
| 2026-01 | 143,444 | 65 | 0.0453% |
| 2026-02 | 139,298 | 26 | 0.0187% |
| 2026-03 | 486,682 | 308 | 0.0633% |
| 2026-04 | 134,333 | 57 | 0.0424% |
| 2026-05 | 133,157 | 72 | 0.0541% |

**Dormant 3+ yrs**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 888,187 | 350 | 0.0394% |
| 2025-02 | 881,350 | 232 | 0.0263% |
| 2025-03 | 882,049 | 222 | 0.0252% |
| 2025-04 | 878,027 | 209 | 0.0238% |
| 2025-05 | 877,447 | 303 | 0.0345% |
| 2025-06 | 875,314 | 324 | 0.0370% |
| 2025-07 | 856,503 | 73 | 0.0085% |
| 2025-08 | 865,496 | 172 | 0.0199% |
| 2025-09 | 907,530 | 320 | 0.0353% |
| 2025-10 | 960,376 | 83 | 0.0086% |
| 2025-11 | 201,404 | 31 | 0.0154% |
| 2025-12 | 206,001 | 21 | 0.0102% |
| 2026-01 | 211,230 | 30 | 0.0142% |
| 2026-02 | 211,817 | 21 | 0.0099% |
| 2026-03 | 960,394 | 140 | 0.0146% |
| 2026-04 | 212,419 | 39 | 0.0184% |
| 2026-05 | 212,527 | 30 | 0.0141% |

# Slide 8: DSE — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (Three In-Scope Client States Combined)

- Dynamic Shoppable Email — dynamically assembled shoppable product content, including its TFY and CYL naming variants.
- DSE is the highest-volume genuine marketing category profiled here, averaging **2,430,798** clients sent per month, and reactivates at an average rate of **0.1031%** — second only to FLS (0.3619%) among genuine marketing categories, but on vastly higher volume — reactivating roughly 2,445 clients in a typical month.
- Its monthly rate ranges from 0.0739% to 0.1614%, a narrower relative spread (2.2x) than most other categories — DSE's performance is comparatively consistent month over month.

DSE monthly reactivation rate, unique clients sent, and reactivated clients, three in-scope client states combined (chart-ready data):

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 2,756,433 | 3,162 | 0.1147% |
| 2025-02 | 2,733,991 | 2,144 | 0.0784% |
| 2025-03 | 2,736,941 | 2,547 | 0.0931% |
| 2025-04 | 2,706,935 | 2,878 | 0.1063% |
| 2025-05 | 2,702,340 | 2,338 | 0.0865% |
| 2025-06 | 2,680,092 | 2,056 | 0.0767% |
| 2025-07 | 2,674,218 | 2,357 | 0.0881% |
| 2025-08 | 2,682,889 | 2,116 | 0.0789% |
| 2025-09 | 2,748,541 | 2,031 | 0.0739% |
| 2025-10 | 2,728,725 | 2,085 | 0.0764% |
| 2025-11 | 2,009,611 | 1,986 | 0.0988% |
| 2025-12 | 2,003,557 | 2,018 | 0.1007% |
| 2026-01 | 2,046,045 | 3,195 | 0.1562% |
| 2026-02 | 2,021,323 | 2,454 | 0.1214% |
| 2026-03 | 2,039,118 | 3,292 | 0.1614% |
| 2026-04 | 2,023,795 | 2,301 | 0.1137% |
| 2026-05 | 2,029,015 | 2,596 | 0.1279% |

# Slide 9: DSE — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (By Client State)

- **Lapsed** has the highest average monthly reactivation rate for DSE (0.2623%), versus **Dormant 3+ yrs**'s 0.0248% — the lowest of the three in-scope states.
- **Dormant 3+ yrs** receives the most DSE volume on average (1,170,667 clients/month); Dormant averages 777,677/month, Lapsed averages 541,327/month.

**Lapsed**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 626,542 | 1,920 | 0.3064% |
| 2025-02 | 614,205 | 1,365 | 0.2222% |
| 2025-03 | 621,375 | 1,640 | 0.2639% |
| 2025-04 | 592,911 | 1,741 | 0.2936% |
| 2025-05 | 583,181 | 1,458 | 0.2500% |
| 2025-06 | 557,172 | 1,273 | 0.2285% |
| 2025-07 | 544,937 | 1,407 | 0.2582% |
| 2025-08 | 555,736 | 1,277 | 0.2298% |
| 2025-09 | 543,787 | 1,266 | 0.2328% |
| 2025-10 | 529,096 | 1,119 | 0.2115% |
| 2025-11 | 448,381 | 1,246 | 0.2779% |
| 2025-12 | 455,205 | 1,142 | 0.2509% |
| 2026-01 | 488,691 | 1,427 | 0.2920% |
| 2026-02 | 489,648 | 1,276 | 0.2606% |
| 2026-03 | 513,986 | 1,710 | 0.3327% |
| 2026-04 | 515,031 | 1,357 | 0.2635% |
| 2026-05 | 522,679 | 1,491 | 0.2853% |

**Dormant**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 968,566 | 950 | 0.0981% |
| 2025-02 | 944,135 | 566 | 0.0599% |
| 2025-03 | 937,219 | 692 | 0.0738% |
| 2025-04 | 924,772 | 828 | 0.0895% |
| 2025-05 | 915,820 | 661 | 0.0722% |
| 2025-06 | 904,230 | 585 | 0.0647% |
| 2025-07 | 898,969 | 711 | 0.0791% |
| 2025-08 | 887,917 | 616 | 0.0694% |
| 2025-09 | 870,061 | 551 | 0.0633% |
| 2025-10 | 851,337 | 661 | 0.0776% |
| 2025-11 | 617,881 | 542 | 0.0877% |
| 2025-12 | 603,344 | 624 | 0.1034% |
| 2026-01 | 608,017 | 1,280 | 0.2105% |
| 2026-02 | 584,763 | 865 | 0.1479% |
| 2026-03 | 576,235 | 1,102 | 0.1912% |
| 2026-04 | 566,296 | 675 | 0.1192% |
| 2026-05 | 560,949 | 780 | 0.1391% |

**Dormant 3+ yrs**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 1,236,510 | 292 | 0.0236% |
| 2025-02 | 1,239,973 | 213 | 0.0172% |
| 2025-03 | 1,250,951 | 215 | 0.0172% |
| 2025-04 | 1,262,664 | 309 | 0.0245% |
| 2025-05 | 1,279,267 | 219 | 0.0171% |
| 2025-06 | 1,289,977 | 198 | 0.0153% |
| 2025-07 | 1,297,722 | 239 | 0.0184% |
| 2025-08 | 1,303,650 | 223 | 0.0171% |
| 2025-09 | 1,400,618 | 214 | 0.0153% |
| 2025-10 | 1,403,999 | 305 | 0.0217% |
| 2025-11 | 991,359 | 198 | 0.0200% |
| 2025-12 | 987,176 | 252 | 0.0255% |
| 2026-01 | 999,749 | 488 | 0.0488% |
| 2026-02 | 986,665 | 313 | 0.0317% |
| 2026-03 | 990,994 | 480 | 0.0484% |
| 2026-04 | 989,350 | 269 | 0.0272% |
| 2026-05 | 990,715 | 325 | 0.0328% |

# Slide 10: FLS — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (Three In-Scope Client States Combined)

- Freestyle Lifecycle Series — sends triggered by a specific high-intent behavioral event (cart abandonment, a saved item now on sale), not sent broadly like the others.
- FLS is the lowest-volume behaviorally-triggered category among the three in-scope states, averaging only **35,355** clients sent per month — far below DSE, PROMO_INCENTIVE, or OTHER — consistent with it firing only after a specific high-intent event rather than being sent broadly.
- Despite the low volume, **FLS reactivates at a far higher average monthly rate (0.3619%) than every other genuine marketing category** — more than 3.5x DSE's 0.1031%, the next-highest — reactivating an average of 130 clients per month (2,211 total across the window).

FLS monthly reactivation rate, unique clients sent, and reactivated clients, three in-scope client states combined (chart-ready data):

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 45,187 | 165 | 0.3651% |
| 2025-02 | 32,584 | 110 | 0.3376% |
| 2025-03 | 37,879 | 132 | 0.3485% |
| 2025-04 | 36,992 | 138 | 0.3731% |
| 2025-05 | 37,710 | 150 | 0.3978% |
| 2025-06 | 30,291 | 104 | 0.3433% |
| 2025-07 | 32,381 | 117 | 0.3613% |
| 2025-08 | 29,062 | 105 | 0.3613% |
| 2025-09 | 31,572 | 97 | 0.3072% |
| 2025-10 | 30,076 | 69 | 0.2294% |
| 2025-11 | 30,169 | 85 | 0.2817% |
| 2025-12 | 33,142 | 103 | 0.3108% |
| 2026-01 | 36,378 | 132 | 0.3629% |
| 2026-02 | 35,192 | 119 | 0.3381% |
| 2026-03 | 40,891 | 151 | 0.3693% |
| 2026-04 | 41,897 | 228 | 0.5442% |
| 2026-05 | 39,630 | 206 | 0.5198% |

# Slide 11: FLS — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (By Client State)

- **Lapsed** has the highest average monthly reactivation rate for FLS (0.4273%), versus **Dormant 3+ yrs**'s 0.2197% — the lowest of the three in-scope states, though still far above most other categories' averages.
- **Lapsed** receives the most FLS volume on average (21,906 clients/month); Dormant averages 9,999/month, Dormant 3+ yrs averages 3,778/month.

**Lapsed**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 25,810 | 107 | 0.4146% |
| 2025-02 | 19,900 | 87 | 0.4372% |
| 2025-03 | 23,340 | 100 | 0.4284% |
| 2025-04 | 22,352 | 93 | 0.4161% |
| 2025-05 | 22,506 | 107 | 0.4754% |
| 2025-06 | 17,880 | 82 | 0.4586% |
| 2025-07 | 18,283 | 76 | 0.4157% |
| 2025-08 | 17,084 | 84 | 0.4917% |
| 2025-09 | 18,841 | 68 | 0.3609% |
| 2025-10 | 17,506 | 48 | 0.2742% |
| 2025-11 | 18,652 | 60 | 0.3217% |
| 2025-12 | 21,201 | 70 | 0.3302% |
| 2026-01 | 23,426 | 93 | 0.3970% |
| 2026-02 | 23,070 | 89 | 0.3858% |
| 2026-03 | 27,221 | 121 | 0.4445% |
| 2026-04 | 28,102 | 166 | 0.5907% |
| 2026-05 | 27,229 | 169 | 0.6207% |

**Dormant**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 15,351 | 45 | 0.2931% |
| 2025-02 | 9,759 | 18 | 0.1844% |
| 2025-03 | 11,133 | 24 | 0.2156% |
| 2025-04 | 11,216 | 33 | 0.2942% |
| 2025-05 | 11,527 | 33 | 0.2863% |
| 2025-06 | 9,461 | 17 | 0.1797% |
| 2025-07 | 10,723 | 33 | 0.3077% |
| 2025-08 | 8,943 | 17 | 0.1901% |
| 2025-09 | 9,446 | 21 | 0.2223% |
| 2025-10 | 9,170 | 15 | 0.1636% |
| 2025-11 | 8,435 | 18 | 0.2134% |
| 2025-12 | 8,847 | 25 | 0.2826% |
| 2026-01 | 9,374 | 32 | 0.3414% |
| 2026-02 | 8,575 | 23 | 0.2682% |
| 2026-03 | 9,476 | 23 | 0.2427% |
| 2026-04 | 9,658 | 42 | 0.4349% |
| 2026-05 | 8,889 | 28 | 0.3150% |

**Dormant 3+ yrs**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 4,302 | 13 | 0.3022% |
| 2025-02 | 3,171 | 5 | 0.1577% |
| 2025-03 | 3,762 | 8 | 0.2127% |
| 2025-04 | 3,806 | 12 | 0.3153% |
| 2025-05 | 4,039 | 10 | 0.2476% |
| 2025-06 | 3,314 | 5 | 0.1509% |
| 2025-07 | 3,703 | 8 | 0.2160% |
| 2025-08 | 3,255 | 4 | 0.1229% |
| 2025-09 | 3,604 | 8 | 0.2220% |
| 2025-10 | 3,681 | 6 | 0.1630% |
| 2025-11 | 3,365 | 7 | 0.2080% |
| 2025-12 | 3,473 | 8 | 0.2303% |
| 2026-01 | 3,977 | 7 | 0.1760% |
| 2026-02 | 3,835 | 7 | 0.1825% |
| 2026-03 | 4,522 | 7 | 0.1548% |
| 2026-04 | 4,550 | 20 | 0.4396% |
| 2026-05 | 3,862 | 9 | 0.2330% |

# Slide 12: PROMO_INCENTIVE — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (Three In-Scope Client States Combined)

- Campaigns using a financial incentive as the mechanism — an offer, discount, sale, percent-off, markdown, deal, coupon, credit, incentive, or waived styling fee.
- PROMO_INCENTIVE averages **2,281,542** clients sent per month — the second-highest volume of any genuine marketing category profiled among the three in-scope states — and an average monthly rate of **0.0867%**, reactivating roughly 1,970 clients in a typical month.
- This is the category that was previously blended into generic "Other" marketing content; isolating it shows it performs closer to DSE (0.1031%) than to the true OTHER remainder (0.0597%).

PROMO_INCENTIVE monthly reactivation rate, unique clients sent, and reactivated clients, three in-scope client states combined (chart-ready data):

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 2,685,457 | 2,461 | 0.0916% |
| 2025-02 | 1,928,392 | 1,715 | 0.0889% |
| 2025-03 | 1,768,100 | 1,742 | 0.0985% |
| 2025-04 | 1,822,154 | 1,778 | 0.0976% |
| 2025-05 | 2,646,197 | 1,366 | 0.0516% |
| 2025-06 | 1,359,053 | 1,369 | 0.1007% |
| 2025-07 | 2,586,046 | 2,003 | 0.0775% |
| 2025-08 | 2,566,232 | 1,472 | 0.0574% |
| 2025-09 | 3,810,925 | 4,506 | 0.1182% |
| 2025-10 | 2,676,274 | 1,596 | 0.0596% |
| 2025-11 | 2,098,265 | 2,086 | 0.0994% |
| 2025-12 | 2,248,598 | 2,014 | 0.0896% |
| 2026-01 | 2,200,824 | 1,891 | 0.0859% |
| 2026-02 | 2,044,903 | 1,940 | 0.0949% |
| 2026-03 | 2,079,376 | 2,100 | 0.1010% |
| 2026-04 | 2,110,710 | 1,831 | 0.0867% |
| 2026-05 | 2,154,707 | 1,619 | 0.0751% |

# Slide 13: PROMO_INCENTIVE — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (By Client State)

- **Lapsed** has the highest average monthly reactivation rate for PROMO_INCENTIVE (0.2264%), versus **Dormant 3+ yrs**'s 0.0222% — the lowest of the three in-scope states.
- **Dormant 3+ yrs** receives the most PROMO_INCENTIVE volume on average (1,146,707 clients/month); Dormant averages 696,103/month, Lapsed averages 472,664/month.

**Lapsed**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 579,226 | 1,575 | 0.2719% |
| 2025-02 | 428,232 | 1,126 | 0.2629% |
| 2025-03 | 405,468 | 1,101 | 0.2715% |
| 2025-04 | 344,987 | 800 | 0.2319% |
| 2025-05 | 532,302 | 783 | 0.1471% |
| 2025-06 | 253,396 | 870 | 0.3433% |
| 2025-07 | 487,901 | 1,134 | 0.2324% |
| 2025-08 | 487,749 | 843 | 0.1728% |
| 2025-09 | 534,563 | 786 | 0.1470% |
| 2025-10 | 482,628 | 705 | 0.1461% |
| 2025-11 | 460,896 | 1,536 | 0.3333% |
| 2025-12 | 463,430 | 1,044 | 0.2253% |
| 2026-01 | 490,355 | 717 | 0.1462% |
| 2026-02 | 479,766 | 1,021 | 0.2128% |
| 2026-03 | 525,659 | 1,281 | 0.2437% |
| 2026-04 | 533,877 | 1,167 | 0.2186% |
| 2026-05 | 544,845 | 1,322 | 0.2426% |

**Dormant**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 926,981 | 699 | 0.0754% |
| 2025-02 | 632,879 | 419 | 0.0662% |
| 2025-03 | 569,195 | 474 | 0.0833% |
| 2025-04 | 604,847 | 734 | 0.1214% |
| 2025-05 | 876,663 | 412 | 0.0470% |
| 2025-06 | 439,472 | 355 | 0.0808% |
| 2025-07 | 856,814 | 683 | 0.0797% |
| 2025-08 | 825,039 | 472 | 0.0572% |
| 2025-09 | 1,066,659 | 2,316 | 0.2171% |
| 2025-10 | 819,079 | 601 | 0.0734% |
| 2025-11 | 630,520 | 391 | 0.0620% |
| 2025-12 | 648,129 | 697 | 0.1075% |
| 2026-01 | 633,788 | 807 | 0.1273% |
| 2026-02 | 584,964 | 655 | 0.1120% |
| 2026-03 | 575,650 | 559 | 0.0971% |
| 2026-04 | 555,070 | 453 | 0.0816% |
| 2026-05 | 587,999 | 211 | 0.0359% |

**Dormant 3+ yrs**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 1,212,007 | 187 | 0.0154% |
| 2025-02 | 889,388 | 170 | 0.0191% |
| 2025-03 | 819,593 | 167 | 0.0204% |
| 2025-04 | 897,536 | 244 | 0.0272% |
| 2025-05 | 1,269,759 | 171 | 0.0135% |
| 2025-06 | 682,490 | 145 | 0.0212% |
| 2025-07 | 1,282,421 | 186 | 0.0145% |
| 2025-08 | 1,286,862 | 157 | 0.0122% |
| 2025-09 | 2,257,611 | 1,404 | 0.0622% |
| 2025-10 | 1,399,912 | 290 | 0.0207% |
| 2025-11 | 1,048,116 | 159 | 0.0152% |
| 2025-12 | 1,175,575 | 273 | 0.0232% |
| 2026-01 | 1,118,533 | 367 | 0.0328% |
| 2026-02 | 1,011,445 | 264 | 0.0261% |
| 2026-03 | 1,014,846 | 260 | 0.0256% |
| 2026-04 | 1,064,916 | 211 | 0.0198% |
| 2026-05 | 1,063,008 | 86 | 0.0081% |

# Slide 14: WINBACK — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (Three In-Scope Client States Combined)

- Reactivation/win-back branded messaging with no financial incentive attached.
- WINBACK averages only **517,264** clients sent per month and reactivates at just **0.0231%** on average — well below every other genuine marketing category except CROSSSELL.
- Its monthly rate touches 0.0000% in 2 of 17 months and peaks at 0.1087% in its single best month — a highly uneven category, unlike the steadier categories above.
- Without a financial incentive attached, plain reactivation/win-back branded messaging underperforms every other identified content type except cross-sell.

WINBACK monthly reactivation rate, unique clients sent, and reactivated clients, three in-scope client states combined (chart-ready data):

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 1,164,388 | 43 | 0.0037% |
| 2025-02 | 232,529 | 18 | 0.0077% |
| 2025-03 | 106,978 | 23 | 0.0215% |
| 2025-04 | 68,311 | 3 | 0.0044% |
| 2025-05 | 5,083 | 1 | 0.0197% |
| 2025-06 | 956,753 | 49 | 0.0051% |
| 2025-07 | 1,555,925 | 114 | 0.0073% |
| 2025-08 | 4,599 | 5 | 0.1087% |
| 2025-09 | 1,243,260 | 1,271 | 0.1022% |
| 2025-10 | 1,360,814 | 66 | 0.0049% |
| 2025-11 | 3,876 | 1 | 0.0258% |
| 2025-12 | 6,621 | 0 | 0.0000% |
| 2026-01 | 904,092 | 255 | 0.0282% |
| 2026-02 | 570,749 | 57 | 0.0100% |
| 2026-03 | 555,495 | 68 | 0.0122% |
| 2026-04 | 49,009 | 15 | 0.0306% |
| 2026-05 | 5,014 | 0 | 0.0000% |

# Slide 15: WINBACK — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (By Client State)

- **Lapsed** has the highest average monthly reactivation rate for WINBACK (0.0517%), versus **Dormant 3+ yrs**'s 0.0060% — the lowest of the three in-scope states.
- **Dormant 3+ yrs** receives the most WINBACK volume on average (404,840 clients/month); Dormant averages 231,652/month, Lapsed averages 56,193/month.
- Coverage is incomplete (fewer than 17 months with any recorded volume) for: Dormant (13/17 months), Dormant 3+ yrs (12/17 months).
- Months with literally zero reactivated clients: Lapsed (4/17 months), Dormant (2/13 months), Dormant 3+ yrs (2/12 months).

**Lapsed**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 215,569 | 34 | 0.0158% |
| 2025-02 | 54,332 | 14 | 0.0258% |
| 2025-03 | 31,412 | 18 | 0.0573% |
| 2025-04 | 19,497 | 3 | 0.0154% |
| 2025-05 | 5,083 | 1 | 0.0197% |
| 2025-06 | 180,316 | 38 | 0.0211% |
| 2025-07 | 265,164 | 89 | 0.0336% |
| 2025-08 | 4,599 | 5 | 0.1087% |
| 2025-09 | 124,448 | 581 | 0.4669% |
| 2025-10 | 4,143 | 0 | 0.0000% |
| 2025-11 | 3,876 | 1 | 0.0258% |
| 2025-12 | 6,621 | 0 | 0.0000% |
| 2026-01 | 20,243 | 10 | 0.0494% |
| 2026-02 | 5,447 | 1 | 0.0184% |
| 2026-03 | 4,846 | 1 | 0.0206% |
| 2026-04 | 4,678 | 0 | 0.0000% |
| 2026-05 | 5,012 | 0 | 0.0000% |

**Dormant**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 398,427 | 6 | 0.0015% |
| 2025-02 | 76,161 | 3 | 0.0039% |
| 2025-03 | 33,846 | 5 | 0.0148% |
| 2025-04 | 20,783 | 0 | 0.0000% |
| 2025-05 | 0 (no qualifying sends) | — | — |
| 2025-06 | 305,105 | 8 | 0.0026% |
| 2025-07 | 544,250 | 22 | 0.0040% |
| 2025-08 | 0 (no qualifying sends) | — | — |
| 2025-09 | 434,608 | 523 | 0.1203% |
| 2025-10 | 482,640 | 45 | 0.0093% |
| 2025-11 | 0 (no qualifying sends) | — | — |
| 2025-12 | 0 (no qualifying sends) | — | — |
| 2026-01 | 332,587 | 160 | 0.0481% |
| 2026-02 | 183,982 | 51 | 0.0277% |
| 2026-03 | 169,710 | 43 | 0.0253% |
| 2026-04 | 29,380 | 12 | 0.0408% |
| 2026-05 | 2 | 0 | 0.0000% |

**Dormant 3+ yrs**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 555,621 | 3 | 0.0005% |
| 2025-02 | 102,974 | 1 | 0.0010% |
| 2025-03 | 43,221 | 0 | 0.0000% |
| 2025-04 | 28,033 | 0 | 0.0000% |
| 2025-05 | 0 (no qualifying sends) | — | — |
| 2025-06 | 477,134 | 3 | 0.0006% |
| 2025-07 | 754,406 | 3 | 0.0004% |
| 2025-08 | 0 (no qualifying sends) | — | — |
| 2025-09 | 685,138 | 167 | 0.0244% |
| 2025-10 | 875,273 | 21 | 0.0024% |
| 2025-11 | 0 (no qualifying sends) | — | — |
| 2025-12 | 0 (no qualifying sends) | — | — |
| 2026-01 | 559,013 | 85 | 0.0152% |
| 2026-02 | 381,378 | 5 | 0.0013% |
| 2026-03 | 380,939 | 24 | 0.0063% |
| 2026-04 | 14,951 | 3 | 0.0201% |
| 2026-05 | 0 (no qualifying sends) | — | — |

# Slide 16: BIRTHDAY — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (Three In-Scope Client States Combined)

- Birthday-triggered sends.
- BIRTHDAY averages **489,258** clients sent per month, reactivating an average of 238 clients monthly at a **0.0622%** average rate — in the same middle cluster as OTHER (0.0597%) and APEC (0.0529%).
- Its monthly rate ranges from 0.0192% to 0.1080%, a wide relative spread (5.6x), but every month shows at least some reactivation, unlike WINBACK or CROSSSELL.

BIRTHDAY monthly reactivation rate, unique clients sent, and reactivated clients, three in-scope client states combined (chart-ready data):

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 360,162 | 389 | 0.1080% |
| 2025-02 | 1,859,392 | 393 | 0.0211% |
| 2025-03 | 364,945 | 276 | 0.0756% |
| 2025-04 | 355,230 | 220 | 0.0619% |
| 2025-05 | 365,831 | 217 | 0.0593% |
| 2025-06 | 363,874 | 188 | 0.0517% |
| 2025-07 | 381,056 | 214 | 0.0562% |
| 2025-08 | 368,507 | 246 | 0.0668% |
| 2025-09 | 369,582 | 247 | 0.0668% |
| 2025-10 | 305,091 | 186 | 0.0610% |
| 2025-11 | 278,079 | 178 | 0.0640% |
| 2025-12 | 285,890 | 160 | 0.0560% |
| 2026-01 | 279,845 | 220 | 0.0786% |
| 2026-02 | 1,502,368 | 289 | 0.0192% |
| 2026-03 | 293,258 | 226 | 0.0771% |
| 2026-04 | 291,676 | 223 | 0.0765% |
| 2026-05 | 292,594 | 169 | 0.0578% |

# Slide 17: BIRTHDAY — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (By Client State)

- **Lapsed** has the highest average monthly reactivation rate for BIRTHDAY (0.1668%), versus **Dormant 3+ yrs**'s 0.0229% — the lowest of the three in-scope states.
- **Dormant 3+ yrs** receives the most BIRTHDAY volume on average (248,198 clients/month); Dormant averages 149,171/month, Lapsed averages 92,587/month.

**Lapsed**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 69,808 | 196 | 0.2808% |
| 2025-02 | 386,092 | 215 | 0.0557% |
| 2025-03 | 70,282 | 148 | 0.2106% |
| 2025-04 | 67,056 | 103 | 0.1536% |
| 2025-05 | 67,754 | 113 | 0.1668% |
| 2025-06 | 65,841 | 93 | 0.1412% |
| 2025-07 | 67,711 | 87 | 0.1285% |
| 2025-08 | 65,571 | 119 | 0.1815% |
| 2025-09 | 63,554 | 100 | 0.1573% |
| 2025-10 | 50,559 | 68 | 0.1345% |
| 2025-11 | 44,666 | 92 | 0.2060% |
| 2025-12 | 47,828 | 83 | 0.1735% |
| 2026-01 | 48,956 | 114 | 0.2329% |
| 2026-02 | 292,675 | 150 | 0.0513% |
| 2026-03 | 54,213 | 117 | 0.2158% |
| 2026-04 | 55,144 | 109 | 0.1977% |
| 2026-05 | 56,271 | 83 | 0.1475% |

**Dormant**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 124,387 | 130 | 0.1045% |
| 2025-02 | 610,575 | 118 | 0.0193% |
| 2025-03 | 122,244 | 86 | 0.0704% |
| 2025-04 | 117,899 | 79 | 0.0670% |
| 2025-05 | 119,932 | 70 | 0.0584% |
| 2025-06 | 117,832 | 66 | 0.0560% |
| 2025-07 | 123,795 | 79 | 0.0638% |
| 2025-08 | 117,722 | 83 | 0.0705% |
| 2025-09 | 114,705 | 92 | 0.0802% |
| 2025-10 | 90,991 | 72 | 0.0791% |
| 2025-11 | 81,902 | 46 | 0.0562% |
| 2025-12 | 81,977 | 39 | 0.0476% |
| 2026-01 | 77,646 | 62 | 0.0798% |
| 2026-02 | 405,747 | 85 | 0.0209% |
| 2026-03 | 77,210 | 70 | 0.0907% |
| 2026-04 | 75,730 | 70 | 0.0924% |
| 2026-05 | 75,615 | 53 | 0.0701% |

**Dormant 3+ yrs**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 166,775 | 63 | 0.0378% |
| 2025-02 | 864,652 | 60 | 0.0069% |
| 2025-03 | 173,303 | 42 | 0.0242% |
| 2025-04 | 171,034 | 38 | 0.0222% |
| 2025-05 | 179,012 | 34 | 0.0190% |
| 2025-06 | 180,958 | 29 | 0.0160% |
| 2025-07 | 190,429 | 48 | 0.0252% |
| 2025-08 | 186,026 | 44 | 0.0237% |
| 2025-09 | 192,120 | 55 | 0.0286% |
| 2025-10 | 163,964 | 46 | 0.0281% |
| 2025-11 | 151,703 | 40 | 0.0264% |
| 2025-12 | 156,417 | 38 | 0.0243% |
| 2026-01 | 153,588 | 44 | 0.0286% |
| 2026-02 | 805,150 | 54 | 0.0067% |
| 2026-03 | 162,155 | 39 | 0.0241% |
| 2026-04 | 160,992 | 44 | 0.0273% |
| 2026-05 | 161,089 | 33 | 0.0205% |

# Slide 18: CROSSSELL — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (Three In-Scope Client States Combined)

- Post-Fix cross-sell sends.
- Once Active clients are excluded, CROSSSELL is nearly absent from this analysis' population — a total of **19 sends** across the three in-scope states over the entire 17-month window, spread across only 10 of those months, with **zero reactivations** recorded in any of them.
- This confirms CROSSSELL is fundamentally an Active-client mechanic — a post-Fix cross-sell send that naturally reaches someone who just checked out — and it has essentially no reactivation role to assess in Lapsed, Dormant, or Dormant 3+ yr populations. It's retained in this deck for completeness, not because it's a meaningful comparison point.

CROSSSELL monthly reactivation rate, unique clients sent, and reactivated clients, three in-scope client states combined (chart-ready data):

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 0 (no qualifying sends) | — | — |
| 2025-02 | 1 | 0 | 0.0000% |
| 2025-03 | 2 | 0 | 0.0000% |
| 2025-04 | 2 | 0 | 0.0000% |
| 2025-05 | 2 | 0 | 0.0000% |
| 2025-06 | 0 (no qualifying sends) | — | — |
| 2025-07 | 1 | 0 | 0.0000% |
| 2025-08 | 0 (no qualifying sends) | — | — |
| 2025-09 | 3 | 0 | 0.0000% |
| 2025-10 | 0 (no qualifying sends) | — | — |
| 2025-11 | 0 (no qualifying sends) | — | — |
| 2025-12 | 2 | 0 | 0.0000% |
| 2026-01 | 1 | 0 | 0.0000% |
| 2026-02 | 1 | 0 | 0.0000% |
| 2026-03 | 4 | 0 | 0.0000% |
| 2026-04 | 0 (no qualifying sends) | — | — |
| 2026-05 | 0 (no qualifying sends) | — | — |

# Slide 19: CROSSSELL — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (By Client State)

- CROSSSELL reactivates at **0.0000% in every one of the three in-scope states** — Lapsed, Dormant, and Dormant 3+ yrs alike — with zero reactivated clients recorded across all three combined.
- Volume is negligible and inconsistent everywhere: Lapsed, Dormant, and Dormant 3+ yrs each average roughly 1 client sent per month, present in only 7, 6, and 3 of the 17 months respectively.
- Every month with any recorded volume in any of the three states shows zero reactivated clients.

**Lapsed**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 0 (no qualifying sends) | — | — |
| 2025-02 | 1 | 0 | 0.0000% |
| 2025-03 | 1 | 0 | 0.0000% |
| 2025-04 | 1 | 0 | 0.0000% |
| 2025-05 | 1 | 0 | 0.0000% |
| 2025-06 | 0 (no qualifying sends) | — | — |
| 2025-07 | 1 | 0 | 0.0000% |
| 2025-08 | 0 (no qualifying sends) | — | — |
| 2025-09 | 0 (no qualifying sends) | — | — |
| 2025-10 | 0 (no qualifying sends) | — | — |
| 2025-11 | 0 (no qualifying sends) | — | — |
| 2025-12 | 2 | 0 | 0.0000% |
| 2026-01 | 0 (no qualifying sends) | — | — |
| 2026-02 | 0 (no qualifying sends) | — | — |
| 2026-03 | 1 | 0 | 0.0000% |
| 2026-04 | 0 (no qualifying sends) | — | — |
| 2026-05 | 0 (no qualifying sends) | — | — |

**Dormant**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 0 (no qualifying sends) | — | — |
| 2025-02 | 0 (no qualifying sends) | — | — |
| 2025-03 | 1 | 0 | 0.0000% |
| 2025-04 | 1 | 0 | 0.0000% |
| 2025-05 | 1 | 0 | 0.0000% |
| 2025-06 | 0 (no qualifying sends) | — | — |
| 2025-07 | 0 (no qualifying sends) | — | — |
| 2025-08 | 0 (no qualifying sends) | — | — |
| 2025-09 | 1 | 0 | 0.0000% |
| 2025-10 | 0 (no qualifying sends) | — | — |
| 2025-11 | 0 (no qualifying sends) | — | — |
| 2025-12 | 0 (no qualifying sends) | — | — |
| 2026-01 | 0 (no qualifying sends) | — | — |
| 2026-02 | 1 | 0 | 0.0000% |
| 2026-03 | 2 | 0 | 0.0000% |
| 2026-04 | 0 (no qualifying sends) | — | — |
| 2026-05 | 0 (no qualifying sends) | — | — |

**Dormant 3+ yrs**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 0 (no qualifying sends) | — | — |
| 2025-02 | 0 (no qualifying sends) | — | — |
| 2025-03 | 0 (no qualifying sends) | — | — |
| 2025-04 | 0 (no qualifying sends) | — | — |
| 2025-05 | 0 (no qualifying sends) | — | — |
| 2025-06 | 0 (no qualifying sends) | — | — |
| 2025-07 | 0 (no qualifying sends) | — | — |
| 2025-08 | 0 (no qualifying sends) | — | — |
| 2025-09 | 2 | 0 | 0.0000% |
| 2025-10 | 0 (no qualifying sends) | — | — |
| 2025-11 | 0 (no qualifying sends) | — | — |
| 2025-12 | 0 (no qualifying sends) | — | — |
| 2026-01 | 1 | 0 | 0.0000% |
| 2026-02 | 0 (no qualifying sends) | — | — |
| 2026-03 | 1 | 0 | 0.0000% |
| 2026-04 | 0 (no qualifying sends) | — | — |
| 2026-05 | 0 (no qualifying sends) | — | — |

# Slide 20: OTHER — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (Three In-Scope Client States Combined)

- The true remainder — generic seasonal, thematic, and welcome/onboarding marketing content with no personalization-, promotion-, or lifecycle-event-suggestive naming.
- OTHER — the true remainder after every identifiable sub-group is removed — averages **2,805,134** clients sent per month, the highest volume of any category profiled among the three in-scope states, at an average rate of **0.0597%**, reactivating roughly 1,599 clients in a typical month.
- Its average monthly rate sits just above APEC's (0.0597% vs. 0.0529%) — the two remain close together in the middle of the pack, well behind FLS, DSE, and PROMO_INCENTIVE.

OTHER monthly reactivation rate, unique clients sent, and reactivated clients, three in-scope client states combined (chart-ready data):

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 3,076,574 | 1,634 | 0.0531% |
| 2025-02 | 5,158,011 | 1,502 | 0.0291% |
| 2025-03 | 2,977,538 | 1,652 | 0.0555% |
| 2025-04 | 2,932,160 | 1,814 | 0.0619% |
| 2025-05 | 2,685,758 | 1,305 | 0.0486% |
| 2025-06 | 2,897,451 | 1,390 | 0.0480% |
| 2025-07 | 2,919,131 | 1,367 | 0.0468% |
| 2025-08 | 2,996,158 | 1,470 | 0.0491% |
| 2025-09 | 2,936,780 | 1,335 | 0.0455% |
| 2025-10 | 2,959,599 | 1,982 | 0.0670% |
| 2025-11 | 2,289,412 | 905 | 0.0395% |
| 2025-12 | 2,241,267 | 1,116 | 0.0498% |
| 2026-01 | 2,873,123 | 2,118 | 0.0737% |
| 2026-02 | 2,163,982 | 1,666 | 0.0770% |
| 2026-03 | 2,212,939 | 1,736 | 0.0784% |
| 2026-04 | 2,175,442 | 1,869 | 0.0859% |
| 2026-05 | 2,191,950 | 2,325 | 0.1061% |

# Slide 21: OTHER — Reactivation Rate, Unique Clients Sent, and Reactivated Clients by Month (By Client State)

- **Lapsed** has the highest average monthly reactivation rate for OTHER (0.1767%), versus **Dormant 3+ yrs**'s 0.0122% — the lowest of the three in-scope states.
- **Dormant 3+ yrs** receives the most OTHER volume on average (1,403,985 clients/month); Dormant averages 865,403/month, Lapsed averages 591,831/month.

**Lapsed**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 651,852 | 1,077 | 0.1652% |
| 2025-02 | 725,752 | 1,046 | 0.1441% |
| 2025-03 | 646,667 | 1,178 | 0.1822% |
| 2025-04 | 612,942 | 1,330 | 0.2170% |
| 2025-05 | 601,577 | 934 | 0.1553% |
| 2025-06 | 580,226 | 1,001 | 0.1725% |
| 2025-07 | 572,295 | 826 | 0.1443% |
| 2025-08 | 606,663 | 970 | 0.1599% |
| 2025-09 | 559,116 | 950 | 0.1699% |
| 2025-10 | 545,472 | 1,185 | 0.2172% |
| 2025-11 | 473,263 | 578 | 0.1221% |
| 2025-12 | 471,134 | 725 | 0.1539% |
| 2026-01 | 827,039 | 1,438 | 0.1739% |
| 2026-02 | 522,585 | 1,179 | 0.2256% |
| 2026-03 | 553,600 | 1,059 | 0.1913% |
| 2026-04 | 546,175 | 1,006 | 0.1842% |
| 2026-05 | 564,777 | 1,271 | 0.2250% |

**Dormant**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 1,091,471 | 397 | 0.0364% |
| 2025-02 | 1,449,635 | 331 | 0.0228% |
| 2025-03 | 1,011,036 | 342 | 0.0338% |
| 2025-04 | 989,952 | 372 | 0.0376% |
| 2025-05 | 891,248 | 297 | 0.0333% |
| 2025-06 | 957,947 | 308 | 0.0322% |
| 2025-07 | 967,095 | 400 | 0.0414% |
| 2025-08 | 972,299 | 346 | 0.0356% |
| 2025-09 | 905,365 | 295 | 0.0326% |
| 2025-10 | 904,498 | 580 | 0.0641% |
| 2025-11 | 673,588 | 235 | 0.0349% |
| 2025-12 | 636,723 | 267 | 0.0419% |
| 2026-01 | 859,921 | 495 | 0.0576% |
| 2026-02 | 602,961 | 334 | 0.0554% |
| 2026-03 | 598,840 | 451 | 0.0753% |
| 2026-04 | 598,014 | 592 | 0.0990% |
| 2026-05 | 601,257 | 731 | 0.1216% |

**Dormant 3+ yrs**

| Month | Unique clients sent | Reactivated clients | Reactivation rate |
|---|---|---|---|
| 2025-01 | 1,396,676 | 160 | 0.0115% |
| 2025-02 | 3,046,785 | 125 | 0.0041% |
| 2025-03 | 1,388,694 | 132 | 0.0095% |
| 2025-04 | 1,393,307 | 112 | 0.0080% |
| 2025-05 | 1,253,812 | 74 | 0.0059% |
| 2025-06 | 1,429,263 | 81 | 0.0057% |
| 2025-07 | 1,453,355 | 141 | 0.0097% |
| 2025-08 | 1,482,789 | 154 | 0.0104% |
| 2025-09 | 1,538,092 | 90 | 0.0059% |
| 2025-10 | 1,568,960 | 218 | 0.0139% |
| 2025-11 | 1,185,985 | 92 | 0.0078% |
| 2025-12 | 1,166,158 | 124 | 0.0106% |
| 2026-01 | 1,229,085 | 185 | 0.0151% |
| 2026-02 | 1,076,369 | 153 | 0.0142% |
| 2026-03 | 1,100,881 | 226 | 0.0205% |
| 2026-04 | 1,078,354 | 271 | 0.0251% |
| 2026-05 | 1,079,186 | 323 | 0.0299% |


---

## Images to add

None. Every chart referenced above is provided as chart-ready tabular data directly under its slide heading, so the add-in can build native, editable PowerPoint charts instead of embedding static images.
