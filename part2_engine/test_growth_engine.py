from growth_engine import mom_growth, is_flagged, validate_feed

def test_ethnic_wear_may_growth():
    result = mom_growth(104520.77, 185107.61)
    assert result == 77.1
    assert is_flagged(result) == "flagged"

def test_beauty_personal_care_june_growth():
    result = mom_growth(35542.11, 37559.07)
    assert result == 5.67
    assert is_flagged(result) == "not_flagged"

def test_exact_boundary_growth():
    result = mom_growth(100000, 108000)
    assert result == 8.0
    assert is_flagged(result) == "escalate_exact_boundary"

def test_corrupted_feed_validation():
    ok, errors = validate_feed("part2_engine/fixtures/corrupted_feed.csv")

    assert ok is False

    assert errors == [
        "line 3: negative revenue (-4200.0) for category=Western Wear",
        "line 4: missing category (month=July)",
        "line 6: missing revenue (category=Home & Kitchen)",
    ]