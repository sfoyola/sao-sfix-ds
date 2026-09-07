# Autoship Nudge Promo Incentive — Client Allocation Criteria

- The analysis-side eligibility query identifies the client population intended for allocation into the Autoship Nudge Promo Incentive test. The table below lists every filtering criterion the query applies, one row per field.
- Randomization unit: `client_id`. Allocation point: once a client completes First Fix checkout, keep rate is known, and they select a Quick Fix date and click "Schedule a Quick Fix."
- The "Schedule a Quick Fix" click itself is directly observable in `curated.product_tracking_events`, giving a client-level signal for who actually reached the allocation trigger versus who merely qualified for it. Measured against the qualifying population above, the observed click-through (reach) rate is **~38-41%** (2026-07 and 2026-08 reference months); this event has sustained volume back to 2025-07, so earlier reference months are measurable too.

| Table | Field | Logic | Purpose |
|---|---|---|---|
| `curated.merch_sales_and_feedback` | `fix_number` | `= 1` (earliest shipment kept per client when more than one row is tagged `fix_number = 1`) | Identifies the client's first-ever Fix |
| `curated.merch_sales_and_feedback` | `autoship_or_manual` | `= 'manual'` | Confirms the client is not already enrolled in Autoship |
| `curated.merch_sales_and_feedback` | `sold_paid_fix_flag` | `SUM(sold_paid_fix_flag) >= 1` | Buy 1+ keep rate: client kept at least one item from First Fix |
| `curated.checkout_based_client_state_journal` | `client_state_detail` | `= 'Never Active'` as of the journal row covering First Fix checkout | Confirms the client is genuinely new, not a reactivated or previously dormant/lapsed client |
| `curated.client` | `fake_client_flag` | `COALESCE(fake_client_flag, 0) = 0` | Excludes fraudulent accounts |
| `curated.client` | `employee_affiliated_flag` | `COALESCE(employee_affiliated_flag, 0) = 0` | Excludes employee-affiliated accounts |
| `curated.product_tracking_events` | `name`, `action_name`, `screen_view_name` | `name = 'schedule_quick_fix_button' AND action_name = 'schedule_quick_fix' AND screen_view_name = 'post_checkout_promo'`, joined on `event_timestamp >= checkout_date` | Confirms the client actually clicked "Schedule a Quick Fix" (the allocation trigger), not just that they qualified for it |

**Query logic (verbatim, `eligible` CTE):**
```sql
first_fix_deduped AS (
    SELECT client_id, checkout_date, autoship_or_manual, n_items_kept
    FROM (
        SELECT client_id, checkout_date, autoship_or_manual, n_items_kept,
               ROW_NUMBER() OVER (PARTITION BY client_id ORDER BY checkout_date) AS rn
        FROM first_fix
    )
    WHERE rn = 1
),
state_at_fix AS (
    SELECT f.client_id, j.client_state_detail,
           ROW_NUMBER() OVER (PARTITION BY f.client_id ORDER BY j.start_timestamp DESC) AS rn
    FROM first_fix_deduped f
    JOIN curated.checkout_based_client_state_journal j
      ON j.client_id = f.client_id
     AND j.start_timestamp <= CAST(f.checkout_date AS TIMESTAMP)
),
eligible AS (
    SELECT f.client_id, f.checkout_date
    FROM first_fix_deduped f
    JOIN curated.client c ON c.client_id = f.client_id
    JOIN state_at_fix s ON s.client_id = f.client_id AND s.rn = 1
    WHERE f.autoship_or_manual = 'manual'
      AND f.n_items_kept >= 1
      AND COALESCE(c.fake_client_flag, 0) = 0
      AND COALESCE(c.employee_affiliated_flag, 0) = 0
      AND s.client_state_detail = 'Never Active'
)
```

**Reach-rate logic (verbatim, `reached` CTE):**
```sql
reached AS (
    SELECT DISTINCT e.client_id
    FROM eligible e
    JOIN curated.product_tracking_events t
      ON t.client_id = e.client_id
     AND t.name = 'schedule_quick_fix_button'
     AND t.action_name = 'schedule_quick_fix'
     AND t.screen_view_name = 'post_checkout_promo'
     AND t.event_timestamp >= CAST(e.checkout_date AS TIMESTAMP)
)
```
This event has sustained monthly volume back to 2025-07, well before any reference month used in this analysis.
