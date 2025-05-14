from abc import ABC, abstractmethod

class ExportStrategy(ABC):
    @abstractmethod
    def export(self):
        pass

#los if, else, se separaron en diferentes clases
class PdfExport(ExportStrategy):
    def export(self):
        print("Exportando tareas a PDF...")

class CsvExport(ExportStrategy):
    def export(self):
        print("Exportando tareas a CSV...")

class ExportService:
    def __init__(self, task_service, export_strategy):
        self.task_service = task_service
        self.export_strategy = export_strategy

    def export_tasks(self):
        self.export_strategy.export()
