# RESTful API for To-Do List Management

A lightweight, high-performance REST API built with FastAPI for managing a task list.
This project demonstrates clean architecture, data validation using Pydantic, and automated testing.

## Note: 
due to task requirements two types for data storage were used (list, dict).

## How to run

1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run _manage.py_
4. Once the server is running, you can explore and test the endpoints directly in your browser:
   ```bash
   http://0.0.0.0:8000/docs#/
   
## Testing
The project uses pytest for automated testing.
1. Navigate to tests directory.
2. To run the tests, execute:
   ```bash
   pytest test_api.py