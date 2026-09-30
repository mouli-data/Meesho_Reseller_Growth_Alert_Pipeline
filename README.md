# Meesho Reseller Growth & Alert Intelligence Pipeline

## Project Overview

This project implements the required four-part data analytics and alert workflow:

SQL → verified business numbers → Python guardrails + growth flags → stakeholder-ready narrative → agent orchestration → human final approval.

## Dataset

The dataset is generated using the supplied script:

data/generate_dataset.py

The generated dataset contains:

- data/resellers.csv
- data/orders.csv
- data/meesho_reseller.db

To regenerate the dataset, run:

py data/generate_dataset.py

## Part 1 — SQL Business Query Engine

Part 1 calculates the required business metrics from the SQLite database.

SQL files:

- part1_sql/qureies.sql
- part1_sql/q2_region_revenue.sql
- part1_sql/q3_top_resellers.sql
- part1_sql/q4_never_ordered.sql
- part1_sql/q4_count_demo.sql
- part1_sql/q5_june_delivered_aov.sql

The Part 1 output files are stored in:

part1_sql/output/

The monthly category revenue output is used by Part 2 and Part 4.

## Part 2 — Python Guardrail & Growth-Detection Engine

Part 2 provides:

- validate_feed()
- mom_growth()
- is_flagged()

Run the Part 2 tests with:

py -m pytest part2_engine/test_growth_engine.py -v

The tests verify:

- April to May Ethnic Wear growth
- May to June Beauty & Personal Care growth
- Exact 8% boundary escalation
- Corrupted-feed validation

## Part 3 — Reliable AI Narrative & Prompt-Pack Report

Part 3 contains:

- part3_narrative/prompt_pack.md
- part3_narrative/narrative_report.md
- part3_narrative/masking.py

The prompt pack defines the required trigger, input placeholders, Context → Insight → Implication structure, and checklist.

The narrative report contains the required narratives, chart-choice justification, and masked reseller references.

## Part 4 — Agentic Workflow Specification & Mock Agent Runner

Part 4 contains:

- part4_agent/agent_spec.md
- part4_agent/mock_agent_runner.py

The agent follows the required ordered workflow:

1. Load the monthly revenue feed.
2. Run validate_feed().
3. If the feed is invalid, perform a Hard Stop and report the validation errors.
4. If the feed is valid, compute mom_growth() for every category against the previous month.
5. Run is_flagged() on every category.
6. Sort flagged categories by absolute MoM percentage in descending order.
7. Draft messages for at most the top 3 flagged categories by magnitude.
8. Log remaining flagged categories as suppressed, review manually.
9. Separately log escalate_exact_boundary categories.
10. Emit one structured JSON object per run.

Every drafted message is held for human approval.

No real email or SMTP integration is used.

## How the Parts Connect

Part 1 → Part 2 → Part 3 / Part 4

- Part 1 produces the verified business numbers.
- Part 2 validates the feed and calculates growth and flags.
- Part 3 provides the narrative and prompt-pack logic.
- Part 4 orchestrates the validated calculations and narrative drafting.

The workflow follows the required pattern:

compute-real-numbers-then-hand-off

The agent workflow follows:

Intake → Summary → Report Draft → Validate

## API Keys

No API keys are required.

No paid API, network service, email service, or SMTP integration is used.

## Run Order

1. Generate the dataset when required:

py data/generate_dataset.py

2. Run the Part 1 SQL queries against:

data/meesho_reseller.db

3. Run the Part 2 tests:

py -m pytest part2_engine/test_growth_engine.py -v

4. Review the Part 3 prompt pack and narrative report.

5. Run the Part 4 mock agent runner:

part4_agent/mock_agent_runner.py

## Human Approval

The workflow does not automatically send messages.

Drafted messages remain held for human approval.