# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code into the container at /code
COPY ./app /code/app

# Command to run the application
# Uvicorn is a lightning-fast ASGI server.
# We bind to 0.0.0.0 to allow traffic from outside the container.
# The port is set to 8080, which is the default for Cloud Run.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
