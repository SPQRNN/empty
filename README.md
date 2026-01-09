# README.md

## Getting Started with the Fibonacci API

This is a FastAPI app that exposes a Fibonacci API endpoint. You can run it using Docker or locally.

### Prerequisites

- Docker (for Dockerized deployment)
- Python 3.8+ (for local deployment)
- FastAPI and uvicorn (installed via `pip install -r requirements.txt`)

### Running with Docker

1. Build the Docker image: `docker build -t fibonacci-api .`
2. Run the Docker container: `docker run -p 8000:8000 fibonacci-api`
3. Access the API at: `http://localhost:8000/docs`

### Running Locally

1. Install dependencies: `pip install -r requirements.txt`
2. Run the API: `uvicorn main:app --reload`
3. Access the API at: `http://localhost:8000/docs`

## API Documentation

The API documentation is available at `/docs`. You can use the UI to test the Fibonacci endpoint.

## API Endpoints

- **POST /fibonacci**: Calculate the nth Fibonacci number.
  - Request Body: `{ "n": int }`
  - Response: `int` - The nth Fibonacci number.
