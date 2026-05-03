from typing import Any, Dict


def initialize_state(
    destination: str, days: int, people: int, budget: int
) -> Dict[str, Any]:
    """
    Create the initial shared state for the travel planning system.

    Args:
        destination: Travel destination.
        days: Number of days.
        people: Number of travelers.
        budget: User's total budget.

    Returns:
        A dictionary representing the global shared state.
    """
    return {
        "destination": destination,
        "days": days,
        "people": people,
        "budget": budget,
        "places": [],
        "itinerary": "",
        "budget_data": {},
        "transport_data": {},
        "agent_outputs": {
            "research": "",
            "itinerary": "",
            "budget": "",
            "transport": "",
        },
        "final_output": "",
    }