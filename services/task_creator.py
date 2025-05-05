from models.task import Task

class TaskCreator:
    def create_task(self, description, type, priority):
        return Task(description, type, priority)
