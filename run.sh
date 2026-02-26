#!/bin/bash

# Function to handle cleanup on exit
cleanup() {
    echo "Shutting down servers..."
    kill $FASTAPI_PID
    kill $STREAMLIT_PID
    exit
}

# Trap SIGINT and SIGTERM to run the cleanup function
trap cleanup SIGINT SIGTERM

echo "Starting FastAPI backend..."
poetry run uvicorn api:app --host 0.0.0.1 --port 8000 &
FASTAPI_PID=$!

echo "Starting Streamlit frontend..."
poetry run streamlit run app.py --server.port 8501 &
STREAMLIT_PID=$!

echo "Both servers are running."
echo "FastAPI backend: http://localhost:8000"
echo "Streamlit frontend: http://localhost:8501"
echo "Press Ctrl+C to stop both servers."

# Wait indefinitely so the script doesn't exit
wait $FASTAPI_PID $STREAMLIT_PID
