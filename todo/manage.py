import uvicorn


def run_app():
    """
    Run ToDo API

    """

    uvicorn.run(
        app="todo.api.run:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    run_app()
