from fastapi import HTTPException, status
from typing import List

from todo.api.database.database import db
from todo.api.schemas.task_schema import TaskCreate, TaskUpdate, Task


async def get_tasks() -> List[Task]:
    return db.tasks_list


async def create_task(task: TaskCreate) -> Task:
    new_id = next(db.id_generator)
    new_task = Task(id=new_id, **task.model_dump())

    # for list
    db.tasks_list.append(new_task)
    # for dict
    db.tasks_dict[new_task.id] = new_task

    return new_task


async def update_task(task_id: int, update_data: TaskUpdate) -> Task:
    if task_id not in db.tasks_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found",
        )

    current_task = db.tasks_dict[task_id]
    updated_task = current_task.model_copy(
        update=update_data.model_dump(exclude_unset=True)
    )

    # for list
    for i, t in enumerate(db.tasks_list):
        if t.id == task_id:
            db.tasks_list[i] = updated_task
            break
    # for dict
    db.tasks_dict[task_id] = updated_task

    return updated_task


async def delete_task(task_id: int) -> None:
    if task_id not in db.tasks_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found",
        )

    # for list
    for i, task in enumerate(db.tasks_list):
        if task.id == task_id:
            db.tasks_list.pop(i)
            break
    # for dict
    del db.tasks_dict[task_id]
