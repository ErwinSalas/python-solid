from models.task import Task

class TaskService:
    def __init__(self):
        self.tasks = []

class CreateTask(Prioridad, ):
    def create_task(self, description, type, priority):
        task = Task(description, type, priority)
        self.tasks.append(task)

#es mejor tener una implementación algo así
class Prioridad:
    #de acuerdo al tipo de prioridad manda a la que corresponda
    pass

class PrioridadAlta(Prioridad):
    def enviar_prioridad(self, prioridad):
        #retorna que es de prioridad alta
        pass

#Esta clase tiene una función no muy bien implementada, deberia ser general 
class NotifyUsers(Prioridad):
    #esto no sirve pero lo dejo como referencia
    def notify_users(self):
        for task in self.tasks:
            if task.priority == "alta":
                print(f"[EMAIL] Notificando tarea urgente: {task.description}")
            else:
                print(f"[SMS] Notificando tarea: {task.description}")
            pass

class FormaDeEnvio(Prioridad):
    #retorna el tipo de envio segun la prioridad
    pass

class SMS(FormaDeEnvio):
    pass

class Email(Prioridad):
    pass

class Formato:
    def tipo_formato(self, formato):
        #ver que formato es
        pass

class PDF(Formato):
    def pdf(self, pdf):
        #retorna que es pdf
        pass

class CSV(Formato):
    def csv(self, csv):
        #retorna que es csv
        pass

#Pasa lo mismo aquí, se necesita descomponer en clases más pequeñas
class ExportTasks(Formato, Prioridad):
    #esto no sirve pero lo dejo como referencia
    def export_tasks(self, format):
        if format == "pdf":
            print("Exportando tareas a PDF...")
        elif format == "csv":
            print("Exportando tareas a CSV...")
        else:
            print("Formato de exportación no soportado")