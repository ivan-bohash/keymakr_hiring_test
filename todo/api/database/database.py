import itertools
from typing import List, Dict

from todo.api.schemas.task_schema import Task


class Database:
    """
    Class for data storage operations.

    Used list and dict just for different examples.

    """

    def __init__(self) -> None:
        self.tasks_list: List[Task] = []
        self.tasks_dict: Dict[int, Task] = {}

        # generate id number
        self.id_generator = itertools.count(start=1)


db = Database()
