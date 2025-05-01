class EmailNotifier:
    def __init__(self, repository):
        self.repository = repository

    def notify(self):
        for task in self.repository.get_tasks():
            if task.priority.lower() == "alta":
                print(f"[EMAIL] Notificando tarea urgente: {task.description}")
