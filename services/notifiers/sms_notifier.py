from services.interfaces.notifier import Notifier

class SMSNotifier(Notifier):
    def notify(self, task):
        print(f"[SMS] Notificando tarea: {task.description}")
