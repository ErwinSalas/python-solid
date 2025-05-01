from models.task import Task

class TaskCreator:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, description, category, priority):
        task = Task(description, category, priority)
        self.repository.add_task(task)
