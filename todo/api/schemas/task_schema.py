from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    id: int = Field(..., description="Task id")


class TaskProperties(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Task title")
    description: str | None = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)


class Task(TaskProperties, TaskBase):
    pass


class TaskCreate(TaskProperties):
    pass


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=1000)
    completed: bool | None = Field(default=None)