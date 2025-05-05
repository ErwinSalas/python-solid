from services.interfaces.notifier import Notifier

class EmailNotifier(Notifier):
    def can_notify(self, task):
        return task.priority == "alta"

    def notify(self, task):
        print(f"[EMAIL] Notificando tarea urgente: {task.description}")
