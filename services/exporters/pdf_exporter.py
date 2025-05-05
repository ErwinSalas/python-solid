from services.interfaces.exporter import Exporter

class PdfExporter(Exporter):
    def can_export(self, format):
        return format == "pdf"

    def export(self, tasks):
        print("Exportando tareas a PDF...")
