from typing import Dict


def estimate_budget(destination: str, days: int, people: int) -> Dict[str, int | str]:
    """
    Estimate a travel budget for the trip.

    Args:
        destination: Name of the destination.
        days: Number of days.
        people: Number of travelers.

    Returns:
        A dictionary containing the budget breakdown.

    Raises:
        ValueError: If days or people are invalid.
    """
    if days < 1:
        raise ValueError("Days must be at least 1.")
    if people < 1:
        raise ValueError("People must be at least 1.")

    transport = 1800 * people
    food = 1200 * people * days
    stay = 4000 * max(1, days - 1)
    entry_fees = 800 * people
    misc = 500 * people

    total = transport + food + stay + entry_fees + misc

    return {
        "destination": destination,
        "transport": transport,
        "food": food,
        "stay": stay,
        "entry_fees": entry_fees,
        "misc": misc,
        "total": total,
    }