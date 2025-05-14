from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def notify(self, task):
        pass

class EmailNotification(NotificationChannel):
    def notify(self, task):
        print(f"[EMAIL] Notificando tarea urgente: {task.description}")

class SmsNotification(NotificationChannel):
    def notify(self, task):
        print(f"[SMS] Notificando tarea: {task.description}")

class TaskNotifier:
    def __init__(self, channels):
        self.channels = channels

    def notify_users(self, tasks):
        for task in tasks:
            if task.priority == "alta":
                self.channels['email'].notify(task)
            else:
                self.channels['sms'].notify(task)
