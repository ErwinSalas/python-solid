from services.interfaces.exporter import Exporter

class CsvExporter(Exporter):
    def can_export(self, format):
        return format == "csv"

    def export(self, tasks):
        print("Exportando tareas a CSV...")
