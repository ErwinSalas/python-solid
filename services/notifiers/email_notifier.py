from services.interfaces.notifier import Notifier

class EmailNotifier(Notifier):
    def notify(self, task):
        print(f"[EMAIL] Notificando tarea urgente: {task.description}")
