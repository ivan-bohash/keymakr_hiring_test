# FastAPI + Celery + Redis Integration

This project demonstrates automation of data retrieval from an API
and saving it to a CSV file using the Celery task queue.

## How to run

1. Make sure you have installed **Docker** and **Docker Compose**.
2. Open terminal and run:
   ```bash
   docker compose up -d --build
3. Open browser and navigate to:
   ```bash
   http://localhost:8000/run-task
4. Or choose _GET /run-task_ in Swagger UI:
   ```bash
   http://localhost:8000/docs
