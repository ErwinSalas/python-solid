class TaskNotifier:
    def __init__(self, notifiers):
        self.notifiers = notifiers  # Lista de Notifier

    def notify(self, task):
        for notifier in self.notifiers:
            if notifier.can_notify(task):
                notifier.notify(task)
