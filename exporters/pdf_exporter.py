class PDFExporter:
    def __init__(self, repository):
        self.repository = repository

    def export(self):
        print("Exportando tareas a PDF...")
        for task in self.repository.get_tasks():
            print(f"PDF: {task.description} - {task.priority}")
