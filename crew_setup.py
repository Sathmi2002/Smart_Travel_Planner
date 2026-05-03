from crewai import Agent, Crew, Process, Task
from crewai.llm import LLM

from agents.prompts import (
    BUDGET_AGENT_BACKSTORY,
    BUDGET_AGENT_GOAL,
    BUDGET_AGENT_ROLE,
    ITINERARY_AGENT_BACKSTORY,
    ITINERARY_AGENT_GOAL,
    ITINERARY_AGENT_ROLE,
    RESEARCH_AGENT_BACKSTORY,
    RESEARCH_AGENT_GOAL,
    RESEARCH_AGENT_ROLE,
    TRANSPORT_AGENT_BACKSTORY,
    TRANSPORT_AGENT_GOAL,
    TRANSPORT_AGENT_ROLE,
)
from tools.budget_tool import estimate_budget
from tools.itinerary_tool import build_itinerary
from tools.places_tool import get_places
from tools.transport_stay_tool import suggest_transport_and_stay
from utils.state import initialize_state


llm = LLM(
    model="ollama/llama3.2:1b",
    base_url="http://localhost:11434",
    temperature=0,
)


def create_crew(user_input: dict):
    destination = user_input["destination"]
    days = user_input["days"]
    people = user_input["people"]
    budget = user_input["budget"]

    state = initialize_state(destination, days, people, budget)

    state["places"] = get_places(destination)
    state["itinerary"] = build_itinerary(state["places"], days)
    state["budget_data"] = estimate_budget(destination, days, people)
    state["transport_data"] = suggest_transport_and_stay(destination, budget)

    research_agent = Agent(
        role=RESEARCH_AGENT_ROLE,
        goal=RESEARCH_AGENT_GOAL,
        backstory=RESEARCH_AGENT_BACKSTORY,
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    itinerary_agent = Agent(
        role=ITINERARY_AGENT_ROLE,
        goal=ITINERARY_AGENT_GOAL,
        backstory=ITINERARY_AGENT_BACKSTORY,
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    budget_agent = Agent(
        role=BUDGET_AGENT_ROLE,
        goal=BUDGET_AGENT_GOAL,
        backstory=BUDGET_AGENT_BACKSTORY,
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    transport_agent = Agent(
        role=TRANSPORT_AGENT_ROLE,
        goal=TRANSPORT_AGENT_GOAL,
        backstory=TRANSPORT_AGENT_BACKSTORY,
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    research_task = Task(
        description=(
            f"Use ONLY this destination and attraction data.\n"
            f"Destination: {state['destination']}\n"
            f"Attractions: {state['places']}\n\n"
            f"Output format:\n"
            f"Overview: <2 short sentences>\n"
            f"Attractions:\n"
            f"- <place 1>\n"
            f"- <place 2>\n"
            f"- <place 3>\n"
            f"- <place 4>\n"
            f"- <place 5>\n\n"
            f"Do not refuse. Do not add warnings. Do not question the data."
        ),
        expected_output="A short overview and attraction list.",
        agent=research_agent,
    )

    itinerary_task = Task(
        description=(
            f"Use ONLY this itinerary data.\n"
            f"Destination: {state['destination']}\n"
            f"Days: {state['days']}\n"
            f"Base itinerary:\n{state['itinerary']}\n\n"
            f"Rewrite it clearly in this format:\n"
            f"Day 1: Morning - ..., Afternoon - ..., Evening - ...\n"
            f"Day 2: Morning - ..., Afternoon - ..., Evening - ...\n\n"
            f"Do not refuse. Do not ask for more information. Do not change destination."
        ),
        expected_output="A clean itinerary.",
        agent=itinerary_agent,
    )

    budget_task = Task(
        description=(
            f"Use ONLY this budget data.\n"
            f"Destination: {state['destination']}\n"
            f"People: {state['people']}\n"
            f"User budget: {state['budget']}\n"
            f"Budget data: {state['budget_data']}\n\n"
            f"Output format:\n"
            f"Budget Summary:\n"
            f"- Transport: ...\n"
            f"- Food: ...\n"
            f"- Stay: ...\n"
            f"- Entry Fees: ...\n"
            f"- Miscellaneous: ...\n"
            f"- Total: ...\n"
            f"- Status: Within budget or Exceeds budget\n\n"
            f"Do not refuse. Do not add unrelated text."
        ),
        expected_output="A clean budget summary.",
        agent=budget_agent,
    )

    transport_task = Task(
        description=(
            f"Use ONLY this recommendation data.\n"
            f"Destination: {state['destination']}\n"
            f"Recommendation data: {state['transport_data']}\n\n"
            f"Output format:\n"
            f"Travel Style: ...\n"
            f"Transport: ...\n"
            f"Accommodation: ...\n\n"
            f"Do not refuse. Do not mention missing or incomplete information."
        ),
        expected_output="A clean transport and stay summary.",
        agent=transport_agent,
    )

    crew = Crew(
        agents=[research_agent, itinerary_agent, budget_agent, transport_agent],
        tasks=[research_task, itinerary_task, budget_task, transport_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew, state