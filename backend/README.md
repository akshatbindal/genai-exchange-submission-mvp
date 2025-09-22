# AI Travel Agent - Backend

This directory contains the Python backend for the AI Travel Agent MVP. It is built with FastAPI and is designed to be deployed as a containerized service on Google Cloud Run.

## Architecture

The backend consists of several components:
- **`main.py`**: The main FastAPI application that defines the API endpoints and orchestrates the agent workflow.
- **`agents/`**: Contains the core logic for the different AI agents (Profile Builder, Itinerary Generator, etc.).
- **`models/`**: Defines the Pydantic data models for request/response validation.
- **`services/`**: Contains mock implementations of services that would interact with GCP (Firestore, Vertex AI).

## Setup and Running Locally

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    - Copy the `.env.example` file to a new file named `.env`.
    - Fill in the required credentials and configuration for your GCP services.

4.  **Run the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

## Deployment

This service is designed to be deployed using Docker on a platform like Google Cloud Run.

1.  **Build the Docker image:**
    ```bash
    docker build -t ai-travel-agent-backend .
    ```

2.  **Run the Docker container (for local testing):**
    ```bash
    docker run -p 8080:8080 -e GCP_PROJECT_ID="your-project" ai-travel-agent-backend
    ```

3.  **Push to Google Artifact Registry and deploy to Cloud Run.**
    *(Specific gcloud commands would go here)*
