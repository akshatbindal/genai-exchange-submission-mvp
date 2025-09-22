from ..models.pydantic_models import QuestionnaireAnswers, UserProfile
from ..services.gcp_services import save_user_profile_to_db

class ProfileBuilderAgent:
    """
    An 'agent' responsible for creating and storing a user's taste profile.
    In a real ADK, this might have more formal state management and tooling.
    """
    def run(self, answers: QuestionnaireAnswers) -> UserProfile:
        """
        Executes the agent's logic.
        1. Takes questionnaire answers.
        2. Calls the service to process and save the profile.
        3. Returns the created user profile.
        """
        print("--- Running Profile Builder Agent ---")
        if not isinstance(answers, QuestionnaireAnswers):
            raise TypeError("Input must be a QuestionnaireAnswers model.")

        profile = save_user_profile_to_db(answers)
        print(f"--- Profile Builder Agent Finished: Created profile {profile.user_id} ---")
        return profile
