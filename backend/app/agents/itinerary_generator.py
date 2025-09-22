from ..models.pydantic_models import UserProfile, Itinerary
from ..services.gcp_services import generate_itinerary_variants
from typing import TypedDict, List
from langgraph.graph import StateGraph, END

# This is a mock implementation of a more complex itinerary object
# that would be returned by a real Vertex AI call.
mock_itinerary_json = {
    "title": "The Adventurous Spirit",
    "description": "A trip focused on outdoor activities and exploration.",
    "daily_plan": [
      { "day": 1, "activities": ["Arrival & Check-in", "Explore the old town"] },
      { "day": 2, "activities": ["Mountain Hiking", "Picnic by the lake"] },
      { "day": 3, "activities": ["Local Cooking Class", "Evening market visit"] },
    ],
    "budget": "Mid-range",
}


class ItineraryGenerationAgentState(TypedDict):
    """Represents the state of our LangGraph agent."""
    user_profile: UserProfile
    generated_itineraries: List[dict] # The raw generated data

class ItineraryGenerationAgent:
    """
    An 'agent' that orchestrates the generation of itinerary variants using a graph.
    """
    def __init__(self):
        self.workflow = self._build_graph()

    def _build_graph(self):
        """Builds the LangGraph workflow."""
        graph_builder = StateGraph(ItineraryGenerationAgentState)

        graph_builder.add_node("generate", self.generate_variants)
        graph_builder.set_entry_point("generate")
        graph_builder.add_edge("generate", END)

        return graph_builder.compile()

    def generate_variants(self, state: ItineraryGenerationAgentState) -> ItineraryGenerationAgentState:
        """This function is a node in our graph. It calls the core generation service."""
        print("--- Running Itinerary Generation Agent Node ---")
        profile = state['user_profile']

        # In a real app, the service would return structured JSON.
        # Here, we simulate this by returning a list of mock dictionaries.
        # The `generate_itinerary_variants` service returns mock strings, so we ignore them
        # and use our structured mock data instead to simulate a real LLM call.
        generated_data = [mock_itinerary_json.copy() for _ in range(3)]

        # Slightly alter them to show variation
        generated_data[1]['title'] = "The Cultural Connoisseur"
        generated_data[2]['title'] = "The Relaxation Getaway"

        print(f"--- Itinerary Generation Agent Finished: Generated {len(generated_data)} variants ---")
        return {"generated_itineraries": generated_data}


    def run(self, profile: UserProfile) -> List[dict]:
        """Executes the agent's graph."""
        print("--- Kicking off Itinerary Generation Agent ---")
        initial_state = ItineraryGenerationAgentState(user_profile=profile, generated_itineraries=[])
        final_state = self.workflow.invoke(initial_state)
        return final_state['generated_itineraries']
