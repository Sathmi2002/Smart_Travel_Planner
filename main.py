from crew_setup import create_crew
from utils.formatter import format_final_plan
from utils.logger import setup_logger
from utils.output_cleaner import clean_agent_output
from utils.text_postprocess import remove_duplicate_lines


def main() -> None:
    logger = setup_logger()

    print("=== AI Smart Travel Planner ===")

    destination = input("Enter destination: ").strip()
    days = int(input("Enter number of days: ").strip())
    people = int(input("Enter number of people: ").strip())
    budget = int(input("Enter budget (LKR): ").strip())

    user_input = {
        "destination": destination,
        "days": days,
        "people": people,
        "budget": budget,
    }

    logger.info("User input: %s", user_input)

    # 🔹 Create crew and shared state
    crew, state = create_crew(user_input)

    # 🔹 Run agents
    result = crew.kickoff()

    # --------------------------------------------------
    # 🔹 FALLBACKS (trusted tool/state-based outputs)
    # --------------------------------------------------

    research_fallback = (
        f"Overview: {state['destination'].title()} is a popular travel destination in Sri Lanka.\n"
        + "Attractions:\n- "
        + "\n- ".join(state["places"])
    )

    itinerary_fallback = state["itinerary"]

    budget_total = state["budget_data"]["total"]
    budget_status = (
        "Within budget"
        if budget_total <= state["budget"]
        else "Exceeds budget"
    )

    budget_fallback = (
        "Budget Summary:\n"
        f"- Transport: LKR {state['budget_data']['transport']}\n"
        f"- Food: LKR {state['budget_data']['food']}\n"
        f"- Stay: LKR {state['budget_data']['stay']}\n"
        f"- Entry Fees: LKR {state['budget_data']['entry_fees']}\n"
        f"- Miscellaneous: LKR {state['budget_data']['misc']}\n"
        f"- Total: LKR {state['budget_data']['total']}\n"
        f"- Status: {budget_status}"
    )

    transport_fallback = (
        f"Travel Style: {state['transport_data']['travel_style']}\n"
        f"Transport: {state['transport_data']['transport']}\n"
        f"Accommodation: {state['transport_data']['stay']}"
    )

    # --------------------------------------------------
    # 🔹 CLEAN RAW AGENT OUTPUT
    # --------------------------------------------------

    cleaned_output = clean_agent_output(str(result), transport_fallback)
    cleaned_output = remove_duplicate_lines(cleaned_output)

    state["agent_outputs"]["transport"] = cleaned_output

    # --------------------------------------------------
    # 🔹 FINAL USER OUTPUT (SAFE + CLEAN)
    # --------------------------------------------------

    state["final_output"] = format_final_plan(state)

    # --------------------------------------------------
    # 🔹 LOGGING (for debugging, not shown to user)
    # --------------------------------------------------

    logger.info("Shared state after execution: %s", state)
    logger.info("Raw crew result: %s", result)
    logger.info("Cleaned output: %s", cleaned_output)
    logger.info("Formatted final output: %s", state["final_output"])

    # --------------------------------------------------
    # 🔹 FINAL DISPLAY (CLEAN FOR DEMO)
    # --------------------------------------------------

    print("\n=== FINAL PLAN ===")
    print(state["final_output"])


if __name__ == "__main__":
    main()