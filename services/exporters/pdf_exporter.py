from services.interfaces.exporter import Exporter

class PdfExporter(Exporter):
    def export(self, tasks):
        print("Exportando tareas a PDF...")
