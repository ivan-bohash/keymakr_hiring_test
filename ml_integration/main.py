from fastapi import FastAPI, HTTPException

from src.predictor import PriorityPredictor
from schemas.task_schema import TaskRequest, TaskResponse

app = FastAPI(title="Task Classifier API")

predictor = PriorityPredictor(model_path="models/model.pkl")


@app.post("/predict", response_model=TaskResponse)
async def get_prediction(request: TaskRequest):
    prediction = predictor.predict(request.task_description)
    
    if prediction == "Model not initialized":
        raise HTTPException(status_code=503, detail="Model is currently unavailable")
        
    return {
        "task_description": request.task_description,
        "priority": prediction
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )