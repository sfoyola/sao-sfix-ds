# Autoship Nudge Promo Incentive — Client Allocation Criteria

- The analysis-side eligibility query identifies the client population intended for allocation into the Autoship Nudge Promo Incentive test. The table below lists every filtering criterion the query applies, one row per field.
- Randomization unit: `client_id`. Allocation point: once a client completes First Fix checkout, keep rate is known, and they select a Quick Fix date and click "Schedule a Quick Fix."

| Table | Field | Logic | Purpose |
|---|---|---|---|
| `curated.merch_sales_and_feedback` | `fix_number` | `= 1` (earliest shipment kept per client when more than one row is tagged `fix_number = 1`) | Identifies the client's first-ever Fix |
| `curated.merch_sales_and_feedback` | `autoship_or_manual` | `= 'manual'` | Confirms the client is not already enrolled in Autoship |
| `curated.merch_sales_and_feedback` | `sold_paid_fix_flag` | `SUM(sold_paid_fix_flag) >= 1` | Buy 1+ keep rate: client kept at least one item from First Fix |
| `curated.checkout_based_client_state_journal` | `client_state_detail` | `= 'Never Active'` as of the journal row covering First Fix checkout | Confirms the client is genuinely new, not a reactivated or previously dormant/lapsed client |
| `curated.client` | `fake_client_flag` | `COALESCE(fake_client_flag, 0) = 0` | Excludes fraudulent accounts |
| `curated.client` | `employee_affiliated_flag` | `COALESCE(employee_affiliated_flag, 0) = 0` | Excludes employee-affiliated accounts |

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
