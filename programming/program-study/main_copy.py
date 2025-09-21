from datetime import datetime
from typing import Union, Optional
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


class Todo :
    """
    개별 할 일을 나타내는 클래스
    """
    def __init__(self, task: str) -> None:
        self.task = task
        self.completed: bool = False
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
        logger.debug("set object")
    
    def complete(self):
        if self.completed:
            raise RuntimeError(f"{self.completed_at}에 완료되었습니다.")
        self.completed = True
        self.completed_at = datetime.now()

    def __str__(self): # pyright: ignore[reportIncompatibleMethodOverride]
        status = "V" if self.completed else "X"
        return f"{status} {self.task}"
    
class TodoList:
    def __init__(self) -> None:
        self.storage: list[Todo] = []
    
    def add_todo(self, task: Union[str,Todo,list]) -> None:
        
        self.storage.append(Todo(task))

    def display_todo(self):
        for todo in self.storage :
            if todo.completed_at :
                print(f"완료:{todo.completed_at} | {todo}")
            else :
                print(f"생성:{todo.created_at} | {todo}")

if __name__ == "__main__":
    todolist = TodoList()
    todolist.add_todo("charge")
    
    todolist.display_todo()
