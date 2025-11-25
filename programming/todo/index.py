import json
import os

class TodoItem:
    def __init__(self, task, done=False) -> None:
        self.task = task
        self.done = done
    
    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {"task": self.task, "done": self.done}
    
    @staticmethod
    def from_dict(data):
        return TodoItem(data["task"], data["done"])
    

    class TodoManager:
        DATA_FILE = "todo_data.json"

        def __init__(self) -> None:
            self.todos = []
            self.load()
        
        def load(self):
            if not os.path.exists(self.DATA_FILE):
                return
            with open(self.DATA_FILE, "r", encoding= "utf-8") as f:
                data = json.load(f)
                self.todos = [TodoItem.from_dict(item) for item in data]