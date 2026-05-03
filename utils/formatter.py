from typing import Any, Dict


def format_final_plan(state: Dict[str, Any]) -> str:
    """
    Build the final travel plan from validated shared state.

    Args:
        state: Global shared state dictionary.

    Returns:
        A formatted final plan string.
    """
    budget_total = state["budget_data"]["total"]
    affordability = (
        "Within budget"
        if budget_total <= state["budget"]
        else "Exceeds budget"
    )

    lines = [
        "=== AI SMART TRAVEL PLAN ===",
        f"Destination: {state['destination'].title()}",
        f"Trip Duration: {state['days']} day(s)",
        f"Travelers: {state['people']}",
        f"User Budget: LKR {state['budget']}",
        "",
        "Top Attractions:",
    ]

    for place in state["places"]:
        lines.append(f"- {place}")

    lines.extend(
        [
            "",
            "Itinerary:",
            state["itinerary"],
            "",
            "Budget Breakdown:",
            f"- Transport: LKR {state['budget_data']['transport']}",
            f"- Food: LKR {state['budget_data']['food']}",
            f"- Stay: LKR {state['budget_data']['stay']}",
            f"- Entry Fees: LKR {state['budget_data']['entry_fees']}",
            f"- Miscellaneous: LKR {state['budget_data']['misc']}",
            f"- Total Estimated Cost: LKR {budget_total}",
            f"- Budget Status: {affordability}",
            "",
            "Transport & Stay Recommendation:",
            f"- Travel Style: {state['transport_data']['travel_style']}",
            f"- Transport: {state['transport_data']['transport']}",
            f"- Accommodation: {state['transport_data']['stay']}",
        ]
    )

    return "\n".join(lines)