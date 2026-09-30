# Agent Specification

## 1. Goal

Keep category managers informed of any category moving beyond the 8% threshold, with human approval required before any message goes out.

## 2. Tools

- `validate_feed()` from Part 2
- `mom_growth()` from Part 2
- `is_flagged()` from Part 2
- Part 3 template-fill logic for drafting the stakeholder message

## 3. Memory / State

The agent maintains the previous month's revenue per category. This is required to calculate the next month's month-over-month growth.

## 4. Planner

The agent follows the required ordered workflow:

1. Load the monthly revenue feed.
2. Run `validate_feed()`.
3. If the feed is invalid, perform a Hard Stop, report the validation errors, and stop.
4. If the feed is valid, compute `mom_growth()` for every category against the previous month.
5. Run `is_flagged()` on every category.
6. Sort flagged categories by absolute MoM percentage in descending order.
6b. Draft a message using Part 3's template for at most the top 3 flagged categories by magnitude.
7. Log any remaining flagged categories beyond the cap as `suppressed, review manually` — not dropped.
7b. Separately log any `escalate_exact_boundary` category into `escalated_categories` — never merged into flagged or suppressed.
8. Emit one structured JSON object per run.

## 5. Feedback Loop

Every drafted message is held for human approval before it can be considered sent.

No real email or SMTP integration is used.

## Guardrails

### Input Guardrail

`validate_feed()` must pass before any MoM calculation, flagging, sorting, or drafting occurs.

### Action Guardrail

No message is ever automatically sent. Messages are only drafted and held for human approval.

### Output Guardrail

Every number in the output must be traceable to the validated input data and calculated Part 2 results.

### Hard Stop

If `validate_feed()` returns invalid, the agent reports the validation errors and stops. No flagged categories, suppressed categories, or drafted messages are produced.