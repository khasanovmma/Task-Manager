import pytest
from ..task import Task
from ..task_manager import TaskManager


@pytest.fixture
def setup_manager() -> TaskManager:
    """Фикстура для создания TaskManager и очистки задач перед тестами."""
    manager = TaskManager(file_path="test_tasks.json")
    manager.tasks = []
    return manager


def test_add_task(setup_manager: TaskManager) -> None:
    """Тест на добавление задачи."""
    manager = setup_manager
    task = Task(
        id=1,
        title="Тестовая задача",
        description="Описание задачи",
        category="Работа",
        due_date="2024-11-30",
        priority="Высокий",
    )
    manager.add_task(task)
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Тестовая задача"


def test_delete_task(setup_manager: TaskManager) -> None:
    """Тест на удаление задачи."""
    manager = setup_manager
    task = Task(
        id=1,
        title="Тестовая задача",
        description="Описание задачи",
        category="Работа",
        due_date="2024-11-30",
        priority="Высокий",
    )
    manager.add_task(task)
    manager.delete_task(1)
    assert len(manager.tasks) == 0
