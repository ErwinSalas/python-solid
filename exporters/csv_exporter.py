class CSVExporter:
    def __init__(self, repository):
        self.repository = repository

    def export(self):
        print("Exportando tareas a CSV...")
        for task in self.repository.get_tasks():
            print(f"CSV: {task.description},{task.priority}")
