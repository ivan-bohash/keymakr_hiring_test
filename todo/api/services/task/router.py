from fastapi import APIRouter, status

from todo.api.services.task.task_view import (
    get_tasks,
    create_task,
    update_task,
    delete_task
)


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

# api routes
router.add_api_route(
    path="/",
    endpoint=get_tasks,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
)
router.add_api_route(
    path="/",
    endpoint=create_task,
    methods=["POST"],
    status_code=status.HTTP_201_CREATED,
)
router.add_api_route(
    path="/{task_id}",
    endpoint=update_task,
    methods=["PUT"],
    status_code=status.HTTP_200_OK,
)
router.add_api_route(
    path="/{task_id}",
    endpoint=delete_task,
    methods=["DELETE"],
    status_code=status.HTTP_204_NO_CONTENT,
)