from models.task import Task

class TaskService:
    def __init__(self, notification_service, export_service):
        self.tasks = []
        self.notification_service = notification_service
        self.export_service = export_service

    def create_task(self, description, type, priority):
        task = Task(description, type, priority)
        self.tasks.append(task)

    # def get_tasks(self):
    #     return self.tasks

    # def notify_users(self):
    #     self.notification_service.notify_users(self.tasks)

    # def export_tasks(self, format):
    #     self.export_service.export_tasks(self.tasks)
