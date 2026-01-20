from fastapi import FastAPI

from .tasks import fetch_users_to_csv

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hi! Navigate to /run-task to start Celery"}

@app.get("/run-task")
def run_task():
    task = fetch_users_to_csv.delay()

    return {
        "task_id": task.id,
        "status": "Task run successfully"
    }