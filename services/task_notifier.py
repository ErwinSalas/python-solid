class TaskNotifier:
    def __init__(self, urgent_notifier, regular_notifier):
        self.urgent_notifier = urgent_notifier
        self.regular_notifier = regular_notifier

    def notify(self, task):
        if task.priority == "alta":
            self.urgent_notifier.notify(task)
        else:
            self.regular_notifier.notify(task)
