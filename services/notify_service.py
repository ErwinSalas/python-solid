from models.notifier import notifier
class notify_service:
    def notify(self,task):
        if task.priority == "baja":
            notifier = low_priority_notifier()
        elif task.priority == "media":
            notifier = medium_priority_notifier()
        elif task.priority == "alta":
            notifier = high_priority_notifier()
        notifier.notify(task)

class high_priority_notifier(notifier):
    def notify(self,task):
        print(f"[EMAIL] Notificando tarea urgente: {task.description}")
class medium_priority_notifier(notifier):
    def notify(self,task):
        print(f"[APP] Notificando tarea: {task.description}")
class low_priority_notifier(notifier):
    def notify(self,task):
        print(f"[SMS] Notificando tarea: {task.description}")
