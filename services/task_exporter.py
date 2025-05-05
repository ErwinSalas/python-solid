class TaskExporter:
    def __init__(self, exporters):
        self.exporters = exporters  # Lista de Exporter

    def export(self, tasks, format):
        for exporter in self.exporters:
            if exporter.can_export(format):
                exporter.export(tasks)
                return
        print("Formato de exportación no soportado")
