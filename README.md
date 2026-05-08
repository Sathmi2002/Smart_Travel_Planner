
#AI Smart Travel Planner

Project Overview
AI Smart Travel Planner is a locally hosted Multi-Agent System (MAS) designed to automate travel planning. The system uses multiple intelligent agents to generate tourist recommendations, travel itineraries, budget estimations, transport suggestions, and accommodation recommendations.
The system accepts user inputs such as destination, number of days, budget, and number of travelers. Then, the agents collaboratively generate a complete travel plan.
 
Features
•	Multi-agent orchestration
•	Local LLM execution using Ollama
•	Tool-based reasoning
•	Shared global state management
•	Offline execution using local files
•	Budget estimation and itinerary generation
 
Agents Used
1. Travel Research Agent
•	Finds tourist attractions and places to visit
•	Tool Used: get_places()
2. Itinerary Planner Agent
•	Generates a structured day-by-day itinerary
•	Tool Used: generate_itinerary()
3. Budget Estimator Agent
•	Calculates estimated travel expenses
•	Tool Used: estimate_cost()
4. Transport & Stay Advisor Agent
•	Suggests transport and accommodation options
•	Tool Used: suggest_transport_and_stay()
 
Technologies Used
•	Python
•	LangGraph / CrewAI
•	Ollama
•	Local Small Language Models (Llama3 / Phi3)
•	JSON Files
•	Python Logging
 
Project Structure
AI-Smart-Travel-Planner/
│
├── main.py
├── agents/
│   ├── travel_research_agent.py
│   ├── itinerary_planner_agent.py
│   ├── budget_estimator_agent.py
│   └── transport_stay_agent.py
│
├── tools/
│   ├── place_tool.py
│   ├── itinerary_tool.py
│   ├── budget_tool.py
│   └── transport_stay_tool.py
│
├── data/
│   ├── places.json
│   ├── transport.json
│   └── cost_rules.json
│
├── tests/
│   └── test_agents.py
│
├── logs/
│   └── agent_logs.txt
│
├── requirements.txt
└── README.md
 
System Workflow
User Input
    ↓
Travel Research Agent
    ↓
Itinerary Planner Agent
    ↓
Budget Estimator Agent
    ↓
Transport & Stay Advisor Agent
    ↓
Final Travel Plan
 
Setup Instructions
1. Clone the Repository
git clone <your-github-repository-link>
cd AI-Smart-Travel-Planner
 
2. Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
 
3. Install Dependencies
pip install -r requirements.txt
 
Install Ollama
Download and install Ollama from:
https://ollama.com/
 
Pull Local LLM Model
ollama pull llama3
or
ollama pull phi3
 
Start Ollama
ollama serve
 
Run the Application
Open another terminal and run:
python main.py
 
Example Input
Destination: Ella
Days: 2
Budget: 10000
Travellers: 2
 
Example Output
Travel Plan for Ella

Day 1:
- Nine Arch Bridge
- Little Adam’s Peak
- Ravana Falls

Day 2:
- Ella Rock
- Tea Factory Visit

Estimated Budget:
- Transport: Rs. 3600
- Food: Rs. 4800
- Stay: Rs. 4000
- Activities: Rs. 1600

Transport Recommendation:
Train or bus travel is recommended.

Stay Recommendation:
Budget guest house or homestay.
 
State Management
The system uses a shared global state to pass information between agents.
state = {
    "destination": "",
    "days": 0,
    "places": [],
    "itinerary": "",
    "budget": "",
    "transport": ""
}
Each agent reads and updates the same state to preserve context throughout the workflow.
 
Logging and Observability
The system records:
•	Agent inputs
•	Tool calls
•	Outputs
•	Errors
Logs are stored in the logs/ directory.
 
Running Tests
Run test cases using:
pytest
 
Example Tool Usage
Travel Research Tool
places = get_places("Ella")
Itinerary Tool
itinerary = generate_itinerary(places, days=2)
Budget Tool
budget = estimate_cost(destination="Ella", days=2, people=2)
Transport & Stay Tool
recommendations = suggest_transport_and_stay(destination="Ella", budget=10000)
 
Individual Contributions
Student Name	Agent Developed	Tool Implemented
Student 1	Travel Research Agent	get_places()
Student 2	Itinerary Planner Agent	generate_itinerary()
Student 3	Budget Estimator Agent	estimate_cost()
Student 4	Transport & Stay Advisor Agent	suggest_transport_and_stay()
 
Notes
•	The system runs fully offline.
•	No paid APIs are used.
•	Local JSON files are used for data handling.
•	Ollama is used for local LLM execution.
 
Conclusion
The AI Smart Travel Planner demonstrates the implementation of a locally hosted Multi-Agent System capable of solving a real-world travel planning problem. By combining specialized agents, custom tools, local LLMs, and shared state management, the system produces structured and reliable travel plans efficiently.
