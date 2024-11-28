from task import Task
from task_manager import TaskManager


def main() -> None:
    """Точка входа в приложение."""
    manager = TaskManager()

    while True:
        print("\nМеню:\n1. Добавить задачу\n2. Просмотреть задачи\n3. Удалить задачу\n4. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                title = input("Название: ")
                description = input("Описание: ")
                category = input("Категория: ")
                due_date = input("Срок выполнения (YYYY-MM-DD): ")
                priority = input("Приоритет (Низкий/Средний/Высокий): ")

                task = Task(
                    id=len(manager.tasks) + 1,
                    title=title,
                    description=description,
                    category=category,
                    due_date=due_date,
                    priority=priority
                )
                manager.add_task(task)
                manager.save_tasks()
                print("Задача успешно добавлена.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            if not manager.tasks:
                print("Нет задач для отображения.")
            else:
                for task in manager.tasks:
                    print(f"{task.id}: {task.title} - {task.status}")

        elif choice == "3":
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                manager.delete_task(task_id)
                manager.save_tasks()
                print("Задача успешно удалена.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
