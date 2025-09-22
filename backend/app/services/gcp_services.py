from ..models.pydantic_models import UserProfile, QuestionnaireAnswers
import uuid

# This is a mock implementation of Firestore and other GCP services.
# In a real application, this would use the Google Cloud client libraries.

class MockFirestoreDB:
    def __init__(self):
        self._data = {}

    def save_user_profile(self, profile: UserProfile):
        print(f"Saving user profile for {profile.user_id} to mock Firestore...")
        self._data[profile.user_id] = profile
        return profile

    def get_user_profile(self, user_id: str) -> UserProfile:
        print(f"Fetching user profile for {user_id} from mock Firestore...")
        return self._data.get(user_id)

class MockNeo4jDB:
    def create_user_node(self, user_id: str):
        print(f"Creating user node '{user_id}' in mock Neo4j...")
        # In a real app, this would create a (User {id: user_id}) node.
        pass

class MockVertexAI:
    def generate_text(self, prompt: str) -> str:
        print(f"Generating text with mock Vertex AI for prompt: {prompt[:100]}...")
        if "summary" in prompt:
            return "This user is an adventurous traveller who loves history and mid-range budgets."
        if "itinerary" in prompt:
            # This would be a complex JSON output in a real scenario
            return "Generated itinerary content..."
        return "Default mock response."

# Instantiate mock services
mock_firestore_db = MockFirestoreDB()
mock_neo4j_db = MockNeo4jDB()
mock_vertex_ai = MockVertexAI()


# --- Service functions that agents will call ---

def save_user_profile_to_db(answers: QuestionnaireAnswers) -> UserProfile:
    """
    Creates a user profile, generates a summary, and saves it.
    """
    user_id = str(uuid.uuid4())

    # 1. Generate a summary using the 'LLM' (mock_vertex_ai)
    summary_prompt = f"Summarize the travel preferences for a user with these answers: {answers.dict()}"
    summary = mock_vertex_ai.generate_text(summary_prompt)

    profile = UserProfile(user_id=user_id, answers=answers, taste_profile_summary=summary)

    # 2. Save to Firestore
    mock_firestore_db.save_user_profile(profile)

    # 3. Create a node in Neo4j
    mock_neo4j_db.create_user_node(user_id)

    return profile

def get_user_profile_from_db(user_id: str) -> UserProfile:
    """
    Retrieves a user profile from Firestore.
    """
    return mock_firestore_db.get_user_profile(user_id)

def generate_itinerary_variants(profile: UserProfile, num_variants: int = 3) -> list:
    """
    Uses the 'LLM' to generate itinerary variants based on a user profile.
    """
    variants = []
    for i in range(num_variants):
        prompt = f"Generate itinerary variant {i+1} for a user with this profile: {profile.taste_profile_summary}"
        # In a real app, this would return structured JSON. Here we just return text.
        variants.append(mock_vertex_ai.generate_text(prompt))
    return variants

def add_explanations_to_itinerary(itinerary_data: dict, profile: UserProfile) -> dict:
    """
    Uses the 'LLM' to add one-sentence explanations to an itinerary.
    """
    print("Adding explanations to itinerary...")
    # This is a mock transformation.
    for day_plan in itinerary_data.get("daily_plan", []):
        prompt = f"Create a one-sentence explanation for the activity '{day_plan['activities'][0]}' based on the user's preference for {profile.answers.interests}"
        day_plan["explanation"] = mock_vertex_ai.generate_text(prompt)
    return itinerary_data
