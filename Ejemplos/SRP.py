"""
    El principio de responsabilidad única (SRP) establece que una clase debe tener
    una única razón para cambiar, lo que significa que debe tener una única
    responsabilidad o función. Esto ayuda a mantener el código limpio, modular y
    fácil de mantener.
"""

# Parte 1: Diseño inicial con incumplimiento de SRP

"""
    En este diseño, la clase ServicioDeTareas tiene múltiples responsabilidades:
    1. Crear tareas.
    2. Notificar al usuario.
    3. Exportar tareas a diferentes formatos.
    Esto hace que la clase sea difícil de mantener y entender, ya que cada
    responsabilidad puede cambiar por separado.
"""
class ServicioDeTareas:
    def __init__(self):
        self.tareas = []
    
    def crear_tarea(self, descripcion, tipo, prioridad):
        tarea = {
            "descripcion": descripcion,
            "tipo": tipo,
            "prioridad": prioridad
        }
        self.tareas.append(tarea)
    
    def notificar_usuario(self, mensaje, tipo_notificacion):
        if tipo_notificacion == "email":
            print(f"Notificando por correo: {mensaje}")
        elif tipo_notificacion == "sms":
            print(f"Notificando por SMS: {mensaje}")
        else:
            print("Tipo de notificación no soportado")

    def exportar_tareas(self, formato):
        if formato == "PDF":
            print("Exportando tareas a PDF")
        elif formato == "CSV":
            print("Exportando tareas a CSV")
        else:
            print("Formato no soportado")
    


# Parte 2: Diseño corregido que respeta SRP
"""
    En este diseño, hemos separado las responsabilidades en diferentes clases:
    TaskService para crear tareas, NotificationService para notificaciones
    y ExportService para exportar tareas. Cada clase tiene una única
    responsabilidad, lo que facilita el mantenimiento y la comprensión del código,
    ademas de permitir la reutilización de las clases en diferentes contextos.
    Esto respeta el principio de responsabilidad única (SRP) y hace que el
    sistema sea más robusto y fácil de extender.
"""


class TaskService:
    def __init__(self):
        self.tasks = []
    
    def create_task(self, description, type, priority):
        task = {
            "description": description,
            "type": type,
            "priority": priority
        }
        self.tasks.append(task)


#Interfaz para notificaciones
class NotificationService:
    def notify(self, mensaje):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Clase para notificaciones por correo
class EmailNotificationService(NotificationService):
    def notify(self, mensaje):
        print(f"Notificando por correo: {mensaje}")

# Clase para notificaciones por SMS
class SMSNotificationService(NotificationService):
    def notify(self, mensaje):
        print(f"Notificando por SMS: {mensaje}")


# Interfaz para exportación de tareas
class ExportService:
    def export(self, tareas):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Clase para exportar tareas a PDF
class PDFExportService(ExportService):
    def export(self, tareas):
        print("Exportando tareas a PDF")

# Clase para exportar tareas a CSV
class CSVExportService(ExportService):
    def export(self, tareas):
        print("Exportando tareas a CSV")

