def mom_growth(previous, current):
    return round((current - previous) / previous * 100, 2)
    
def is_flagged(mom_pct, threshold=8.0):
    if abs(mom_pct) > threshold:
        return "flagged"
    elif abs(mom_pct) < threshold:
        return "not_flagged"
    else:
        return "escalate_exact_boundary"

def validate_feed(csv_path):
    import csv

    errors = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for line_num, row in enumerate(reader, start=2):
            month = row["month"]
            category = row["category"]
            revenue = row["revenue"]

            if category == "":
                errors.append(
                    f"line {line_num}: missing category (month={month})"
                )

            if revenue == "":
                errors.append(
                    f"line {line_num}: missing revenue (category={category})"
                )
            else:
                try:
                    revenue_value = float(revenue)
                except ValueError:
                    errors.append(
                        f"line {line_num}: revenue not numeric: {revenue!r}"
                    )
                else:
                    if revenue_value < 0:
                        errors.append(
                            f"line {line_num}: negative revenue ({revenue_value}) for category={category}"
                        )

    if errors:
        return False, errors

    return True, []