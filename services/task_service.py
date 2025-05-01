from models.task import Task
from services.notify_service import notify_service
from services.exporter_service import exporter_service
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
    
    
        
    
