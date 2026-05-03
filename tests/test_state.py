from utils.state import initialize_state


def test_initialize_state():
    state = initialize_state("Ella", 2, 2, 15000)
    assert state["destination"] == "Ella"
    assert state["days"] == 2
    assert state["people"] == 2
    assert state["budget"] == 15000
    assert state["places"] == []