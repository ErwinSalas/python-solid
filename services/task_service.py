from models.task import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def create_task(self, description, type, priority):
        task = Task(description, type, priority)
        self.tasks.append(task)

#Aplicando solid
class NotificationService():
    def notify(self):
        pass
        
                
class EmailNotificationService(NotificationService):
    def notify(self):
        print("Notificando por correo")

class SMSNotificationService(NotificationService):
    def notify(self):
        print(f"Notificando por SMS")


class exportService():
    def export(self):
        pass

class exportPDFService(exportService):
    def export(self):
        print("Exportando PDF")
        pass
    
class exportCSVService(exportService):
    def export(self):
        print("Exportando CSV")
        pass
    