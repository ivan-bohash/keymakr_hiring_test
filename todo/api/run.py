from fastapi import FastAPI
from todo.api.services.connector import routers


class TodoAPI(FastAPI):
    """
    Main ToDo API class

    """

    def __init__(self, **kwargs):
        super().__init__(
            title="ToDo API",
            description="API for tasks management",
            version="1.0.0",
            **kwargs
        )
        self.add_services()

    def add_services(self) -> None:
        """
        Add API services

        """

        for router in routers:
            self.include_router(router=router)

app = TodoAPI()