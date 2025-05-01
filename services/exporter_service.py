from models.exporter import exporter
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