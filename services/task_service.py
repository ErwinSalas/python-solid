class TaskService:
    def __init__(self, creator, notifier, exporter):
        self.creator = creator
        self.notifier = notifier
        self.exporter = exporter
        self.tasks = []

    def create_task(self, description, type, priority):
        task = self.creator.create_task(description, type, priority)
        self.tasks.append(task)

    def notify_users(self):
        for task in self.tasks:
            self.notifier.notify(task)

    def export_tasks(self, format):
        self.exporter.export(self.tasks, format)
