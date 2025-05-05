from services.interfaces.notifier import Notifier

class SMSNotifier(Notifier):
    def can_notify(self, task):
        return task.priority != "alta"

    def notify(self, task):
        print(f"[SMS] Notificando tarea: {task.description}")
