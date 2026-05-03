from tools.transport_stay_tool import suggest_transport_and_stay


def test_transport_and_stay_fields():
    result = suggest_transport_and_stay("Ella", 20000)
    assert "transport" in result
    assert "stay" in result
    assert "travel_style" in result


def test_transport_budget_category():
    result = suggest_transport_and_stay("Ella", 10000)
    assert result["travel_style"] == "Budget"


def test_transport_invalid_budget():
    try:
        suggest_transport_and_stay("Ella", 0)
        assert False
    except ValueError:
        assert True