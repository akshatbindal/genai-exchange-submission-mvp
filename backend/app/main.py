from fastapi import FastAPI, HTTPException
from ..models.pydantic_models import (
    QuestionnaireAnswers,
    ItineraryGenerationResponse,
    Itinerary,
)
from ..agents.profile_builder import ProfileBuilderAgent
from ..agents.itinerary_generator import ItineraryGenerationAgent
from ..agents.explainability import ExplainabilityAgent

# Initialize the FastAPI app
app = FastAPI(
    title="AI Travel Agent API",
    description="API for the AI-Powered Travel Agent MVP.",
    version="0.1.0",
)

# Initialize the agents
profile_builder_agent = ProfileBuilderAgent()
itinerary_generator_agent = ItineraryGenerationAgent()
explainability_agent = ExplainabilityAgent()


@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Travel Agent API"}


@app.post("/api/v1/generate-itinerary", response_model=ItineraryGenerationResponse)
def generate_itinerary_endpoint(answers: QuestionnaireAnswers):
    """
    The main endpoint to generate personalized travel itineraries.
    This endpoint orchestrates the flow between different agents.
    """
    print("--- Received request to generate itinerary ---")
    try:
        # Step 1: Use the Profile Builder Agent to create a user profile
        user_profile = profile_builder_agent.run(answers)
        if not user_profile:
            raise HTTPException(status_code=500, detail="Failed to create user profile.")

        # Step 2: Use the Itinerary Generation Agent to get 3 variants
        generated_itineraries_data = itinerary_generator_agent.run(user_profile)
        if not generated_itineraries_data:
            raise HTTPException(status_code=500, detail="Failed to generate itineraries.")

        # Step 3: Use the Explainability Agent to add justifications
        enriched_itineraries_data = explainability_agent.run(generated_itineraries_data, user_profile)

        # Step 4: Validate the final output with the Pydantic model
        final_itineraries = [Itinerary(**data) for data in enriched_itineraries_data]

        print("--- Successfully generated and enriched itineraries. Sending response. ---")
        return ItineraryGenerationResponse(itineraries=final_itineraries)

    except TypeError as e:
        print(f"Type error during processing: {e}")
        raise HTTPException(status_code=400, detail=f"Invalid data format: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {e}")
