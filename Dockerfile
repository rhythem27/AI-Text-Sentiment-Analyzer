# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies and Poetry
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
# Add Poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

# Copy poetry.lock and pyproject.toml first to cache dependencies
COPY pyproject.toml poetry.lock ./

# Install project dependencies, avoiding creating a virtual environment inside the Docker container
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

# Expose ports for both services (they will be managed by docker-compose)
EXPOSE 8000 8501
