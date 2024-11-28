import json
from typing import List
from task import Task


class TaskManager:
    """Класс для управления задачами."""

    def __init__(self, file_path: str = "tasks.json") -> None:
        self.file_path = file_path
        self.tasks: List[Task] = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        """Загружает задачи из файла."""
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [Task(**task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self) -> None:
        """Сохраняет задачи в файл."""
        with open(self.file_path, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def add_task(self, task: Task) -> None:
        """Добавляет новую задачу."""
        self.tasks.append(task)

    def delete_task(self, task_id: int) -> None:
        """Удаляет задачу по ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def find_tasks(self, keyword: str) -> List[Task]:
        """Ищет задачи по ключевому слову."""
        return [task for task in self.tasks if keyword.lower() in task.title.lower()]
