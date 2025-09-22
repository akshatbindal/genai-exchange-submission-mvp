from ..models.pydantic_models import UserProfile, Itinerary
from ..services.gcp_services import add_explanations_to_itinerary
from typing import List

class ExplainabilityAgent:
    """
    An 'agent' responsible for adding justifications to an itinerary.
    """
    def run(self, itineraries: List[dict], profile: UserProfile) -> List[dict]:
        """
        Executes the agent's logic.
        1. Takes a list of generated itinerary data (as dicts).
        2. For each one, calls a service to add explanations.
        3. Returns the enriched itineraries.
        """
        print("--- Running Explainability Agent ---")
        enriched_itineraries = []
        for itinerary_data in itineraries:
            # The service function simulates calling an LLM to add explanations
            enriched_itinerary = add_explanations_to_itinerary(itinerary_data, profile)
            enriched_itineraries.append(enriched_itinerary)

        print(f"--- Explainability Agent Finished: Enriched {len(enriched_itineraries)} itineraries ---")
        return enriched_itineraries
