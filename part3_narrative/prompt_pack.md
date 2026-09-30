# Reusable Prompt Pack

## 1. Trigger

The prompt is triggered when a category's `is_flagged` result is `"flagged"`.

## 2. Input List

The prompt requires these placeholder variables:

- `{category}`
- `{previous_revenue}`
- `{current_revenue}`
- `{mom_pct}`
- `{month}`
- `{prev_month}`

## 3. Prompt

Using the supplied values `[category]`, `[previous_revenue]`, `[current_revenue]`, `[mom_pct]`, `[month]`, and `[prev_month]`, write a stakeholder update for the flagged category.

Use the following structure:

### Context
State what is being measured and the comparison period using the supplied category and month placeholders.

### Insight
State exactly what happened using the supplied revenue and MoM placeholders. Label the statement explicitly as `FACT`.

### Implication
Give a specific and actionable next step for the stakeholder. If a cause is proposed that is not proven by the supplied data, label it explicitly as `HYPOTHESIS`.

Do not state any number that is not one of the supplied placeholder values.

## 4. Checklist

Before the output is used, verify:

- Does every number in the draft match a supplied placeholder value exactly?
- Is every claim labeled as `FACT` or `HYPOTHESIS` where required?
- Is the recommendation specific and actionable rather than vague?
- Is the comparison period explicitly stated using the supplied month placeholders?
- If a reseller is referenced, is it represented only by coded alias and never by the raw reseller name?