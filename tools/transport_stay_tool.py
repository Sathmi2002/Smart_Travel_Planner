from typing import Dict


def suggest_transport_and_stay(destination: str, budget: int) -> Dict[str, str]:
    """
    Suggest transport and stay options based on the available budget.

    Args:
        destination: Travel destination.
        budget: Total budget in LKR.

    Returns:
        A dictionary with suggested transport, stay, and travel style.

    Raises:
        ValueError: If budget is invalid.
    """
    if budget <= 0:
        raise ValueError("Budget must be greater than zero.")

    if budget < 15000:
        travel_style = "Budget"
        transport = "Public bus or train"
        stay = "Budget guest house or hostel"
    elif budget < 30000:
        travel_style = "Standard"
        transport = "Train, shared taxi, or intercity bus"
        stay = "Homestay or standard hotel"
    else:
        travel_style = "Comfort"
        transport = "Private cab or rental vehicle"
        stay = "Comfort hotel or boutique stay"

    return {
        "destination": destination,
        "travel_style": travel_style,
        "transport": transport,
        "stay": stay,
    }