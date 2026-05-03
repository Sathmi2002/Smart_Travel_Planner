from tools.places_tool import get_places


def test_places():
    result = get_places("Ella")
    assert isinstance(result, list)
    assert len(result) >= 3