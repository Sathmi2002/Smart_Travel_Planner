from tools.itinerary_tool import build_itinerary


def test_itinerary_contains_days():
    result = build_itinerary(["A", "B", "C"], 2)
    assert "Day 1" in result
    assert "Day 2" in result


def test_itinerary_contains_time_sections():
    result = build_itinerary(["A", "B", "C"], 1)
    assert "Morning -" in result
    assert "Afternoon -" in result
    assert "Evening -" in result