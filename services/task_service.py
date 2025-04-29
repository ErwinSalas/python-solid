from models.task import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def create_task(self, description, type, priority):
        task = Task(description, type, priority)
        self.tasks.append(task)

    def notify_users(self):
        for task in self.tasks:
            if task.priority == "alta":
                print(f"[EMAIL] Notificando tarea urgente: {task.description}")
            else:
                print(f"[SMS] Notificando tarea: {task.description}")

    def export_tasks(self, format):
        if format == "pdf":
            print("Exportando tareas a PDF...")
        elif format == "csv":
            print("Exportando tareas a CSV...")
        else:
            print("Formato de exportación no soportado")
