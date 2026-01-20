import pytest
from httpx import AsyncClient, ASGITransport

from todo.api.run import app
from todo.api.database.database import db


# Clear the database before each test to ensure isolation
@pytest.fixture(autouse=True)
def clean_db():
    db.tasks_list.clear()
    db.tasks_dict.clear()
    # id_generator continues to increment, but we clear
    # data structures to keep tests independent.

@pytest.mark.asyncio
async def test_create_task():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        payload = {"title": "Test Task", "description": "Test Description"}
        response = await ac.post("/tasks/", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data
    assert data["completed"] is False

@pytest.mark.asyncio
async def test_get_tasks():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Create a task first to check list retrieval
        await ac.post("/tasks/", json={"title": "Task 1", "description": "Desc 1"})

        response = await ac.get("/tasks/")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Task 1"

@pytest.mark.asyncio
async def test_update_task():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Create a task to be updated
        create_res = await ac.post("/tasks/", json={"title": "Old Title", "description": "Old Desc"})
        task_id = create_res.json()["id"]

        # Perform partial update via PUT
        update_payload = {"title": "New Title", "completed": True}
        response = await ac.put(f"/tasks/{task_id}", json=update_payload)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["completed"] is True
    # Verify that the description remained unchanged
    assert data["description"] == "Old Desc"

@pytest.mark.asyncio
async def test_delete_task():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Create a task to be deleted
        create_res = await ac.post("/tasks/", json={"title": "To Delete", "description": "..."})
        task_id = create_res.json()["id"]

        # Delete the task
        delete_res = await ac.delete(f"/tasks/{task_id}")
        assert delete_res.status_code == 204

        # Confirm the task list is now empty
        get_res = await ac.get("/tasks/")
        assert len(get_res.json()) == 0

@pytest.mark.asyncio
async def test_update_non_existent_task():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Attempt to update a task that doesn't exist
        response = await ac.put("/tasks/999", json={"title": "Ghost", "description": "..."})

    assert response.status_code == 404
    assert response.json()["detail"] == "Task with id 999 not found"