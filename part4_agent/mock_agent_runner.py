import csv
import json
import sys
from pathlib import Path

# Allow imports from the project root.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from part2_engine.growth_engine import (
    validate_feed,
    mom_growth,
    is_flagged,
)


def fill_message(category, mom_pct):
    return (
        f"Context: Monthly revenue monitoring for {category}. "
        f"Insight: FACT — {category} changed by {mom_pct}% MoM. "
        f"Implication: HYPOTHESIS — review category performance to understand "
        f"the reason for this change."
    )

def load_revenue(csv_path, target_month):
    revenue = {}

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["month"] == target_month:
                revenue[row["category"]] = float(row["revenue"])

    return revenue

def run(month, previous_month_csv, current_month_csv):
    valid, errors = validate_feed(current_month_csv)

    if not valid:
        return {
            "run_month": month,
            "validation_status": "invalid",
            "validation_errors": errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "hard_stop",
        }

    previous_month = {
        "May": "April",
        "June": "May",
    }[month]

    previous_revenue = load_revenue(previous_month_csv, previous_month)
    current_revenue = load_revenue(current_month_csv, month)

    flagged = []
    escalated_categories = []

    for category, current_value in current_revenue.items():
        if category not in previous_revenue:
            continue

        previous_value = previous_revenue[category]

        mom_pct = mom_growth(previous_value, current_value)
        status = is_flagged(mom_pct)

        if status == "flagged":
            flagged.append(
                {
                    "category": category,
                    "mom_pct": mom_pct,
                    "previous_revenue": previous_value,
                    "current_revenue": current_value,
                }
            )

        elif status == "escalate_exact_boundary":
            escalated_categories.append(category)

    flagged.sort(key=lambda item: abs(item["mom_pct"]), reverse=True)

    top_three = flagged[:3]
    suppressed = flagged[3:]

    flagged_categories = []

    for item in top_three:
        flagged_categories.append(
            {
                "category": item["category"],
                "mom_pct": item["mom_pct"],
                "previous_revenue": item["previous_revenue"],
                "current_revenue": item["current_revenue"],
                "drafted": True,
                "message": fill_message(
                    item["category"],
                    item["mom_pct"],
                ),
            }
        )

    suppressed_categories = [
        item["category"]
        for item in suppressed
    ]

    return {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": flagged_categories,
        "suppressed_categories": suppressed_categories,
        "escalated_categories": escalated_categories,
        "action_taken": "drafted_and_held_for_approval",
    }


if __name__ == "__main__":
    may_result = run(
        "May",
        "part1_sql/output/monthly_category_revenue.csv",
        "part1_sql/output/monthly_category_revenue.csv",
    )

    print(json.dumps(may_result, indent=2))