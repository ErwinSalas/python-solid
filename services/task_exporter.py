class TaskExporter:
    def __init__(self, exporters):
        self.exporters = exporters  # Dict: formato -> Exporter

    def export(self, tasks, format):
        exporter = self.exporters.get(format)
        if exporter:
            exporter.export(tasks)
        else:
            print("Formato de exportación no soportado")
