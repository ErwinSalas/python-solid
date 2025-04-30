from models.task import Task
class exporter:
    def export(self, tasks):
        pass
class pdf_exporter(exporter):
    def export(self, tasks):
        print("Exportando tareas a PDF..."+str(tasks))
class csv_exporter:
    def export(self, tasks):
        print("Exportando tareas a CSV..."+str(tasks))
class exporter_service:
    def export(self, tasks, format):
        if format == "pdf":
            exporter = pdf_exporter()
        elif format == "csv":
            exporter = csv_exporter()
        exporter.export(tasks)
class notify_service:
    def notify(self,task):
        if task.priority == "baja":
            notifier = low_priority_notifier()
        elif task.priority == "media":
            notifier = medium_priority_notifier()
        elif task.priority == "alta":
            notifier = high_priority_notifier()
        notifier.notify(task)
class notifier:
    def notify(self,task):
        pass
class high_priority_notifier(notifier):
    def notify(self,task):
        print(f"[EMAIL] Notificando tarea urgente: {task.description}")
class medium_priority_notifier(notifier):
    def notify(self,task):
        print(f"[APP] Notificando tarea: {task.description}")
class low_priority_notifier(notifier):
    def notify(self,task):
        print(f"[SMS] Notificando tarea: {task.description}")

class TaskService:
    def __init__(self):
        self.tasks = []
    def create_task(self, description, type, priority):
        task = Task(description, type, priority)
        self.tasks.append(task)
    def notify_users(self):
        notifier = notify_service()
        for task in self.tasks:
            notifier.notify(task)
    def export_tasks(self, format):
        exporter = exporter_service()
        exporter.export(self.tasks, format)
    
    
        
    
