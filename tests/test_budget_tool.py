from tools.budget_tool import estimate_budget


def test_budget_total_positive():
    result = estimate_budget("Ella", 2, 2)
    assert result["total"] > 0


def test_budget_has_all_fields():
    result = estimate_budget("Ella", 2, 2)
    assert "transport" in result
    assert "food" in result
    assert "stay" in result
    assert "entry_fees" in result
    assert "misc" in result