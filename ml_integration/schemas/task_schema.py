from pydantic import BaseModel


class TaskRequest(BaseModel):
    task_description: str

class TaskResponse(BaseModel):
    task_description: str
    priority: str
