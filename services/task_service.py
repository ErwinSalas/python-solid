from models.task import Task

class Task:
    def __init__(self, description, category, priority):
        self.description = description
        self.category = category
        self.priority = priority

class TaskService:
    def __init__(self):
        self.tasks = []

class TaskCreator:
    def __init__(self, task_service):
        self.task_service = task_service  

    def create_task(self, description, priority):
        task = Task(description, "Tarea", priority)
        self.task_service.tasks.append(task)
        print(f"Tarea creada: {task.description} con prioridad {task.priority}")
        
    
class TaskNotifier(TaskService):
    def __init__(self, task_service):
        self.task_service = task_service

class HighPriorityNotifier(TaskNotifier):
    def notify(self):
        for task in self.task_service.tasks:
            if task.priority == "Alta":
                print(f"[EMAIL]Notificando tarea de alta prioridad: {task.description}")

class MediumPriorityNotifier(TaskNotifier):
    def notify(self):
        for task in self.task_service.tasks:
            if task.priority == "Media":
                print(f"[SMS]Notificando tarea de media prioridad: {task.description}")

class LowPriorityNotifier(TaskNotifier):
    def notify(self):
        for task in self.task_service.tasks:
            if task.priority == "Baja":
                print(f"[SMS]Notificando tarea de baja prioridad: {task.description}")

class AllPriorityNotifier(TaskNotifier):
    def notify(self):
        for task in self.task_service.tasks:
            print(f"[EMAIL][SMS]Notificando tarea: {task.description}")

class TaskExporter:
    def __init__(self, task_service):
        self.task_service = task_service

class ExportToPDF(TaskExporter):
    def export(self):
        print("Exportando tareas a PDF...")

class ExportToCSV(TaskExporter):
    def export(self):
        print("Exportando tareas a CSV...")