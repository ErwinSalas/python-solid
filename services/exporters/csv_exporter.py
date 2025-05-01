from services.interfaces.exporter import Exporter

class CsvExporter(Exporter):
    def export(self, tasks):
        print("Exportando tareas a CSV...")
