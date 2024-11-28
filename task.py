from datetime import datetime


class Task:
    """Класс для представления задачи."""

    def __init__(self, id: int, title: str, description: str, category: str, due_date: str, priority: str, status: str = "Не выполнена"):
        self.id = id
        self.title = self.validate_non_empty(title, "Название")
        self.description = self.validate_non_empty(description, "Описание")
        self.category = self.validate_non_empty(category, "Категория")
        self.due_date = self.validate_date(due_date)
        self.priority = self.validate_priority(priority)
        self.status = status

    @staticmethod
    def validate_non_empty(value: str, field_name: str) -> str:
        """Проверка, что поле не пустое."""
        if not value.strip():
            raise ValueError(f"{field_name} не может быть пустым.")
        return value

    @staticmethod
    def validate_date(date_str: str) -> str:
        """Проверка корректности формата даты."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {date_str}. Ожидаемый формат: YYYY-MM-DD.")

    @staticmethod
    def validate_priority(priority: str) -> str:
        """Проверка корректности приоритета."""
        valid_priorities = ["Низкий", "Средний", "Высокий"]
        if priority not in valid_priorities:
            raise ValueError(f"Приоритет должен быть одним из: {', '.join(valid_priorities)}.")
        return priority

    def to_dict(self) -> dict:
        """Преобразует задачу в словарь."""
        return self.__dict__
