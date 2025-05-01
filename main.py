from services.task_repository import TaskRepository
from services.task_creator import TaskCreator
from notifiers.email_notifier import EmailNotifier
from notifiers.sms_notifier import SMSNotifier
from exporters.pdf_exporter import PDFExporter
#opcional se puede usar el CSV exporter si se quisiera y gracias a el refactor el cambio seria minimo
from exporters.csv_exporter import CSVExporter 

def main():
    # las responsabilidades de task_service quedan delegadas a TaskCreator y TaskRepository
    task_repo = TaskRepository()
    # TaskCreator recibe una instancia de TaskRepository a quien delega la
    # tarea de almacenar las tareas creadas
    creator = TaskCreator(task_repo)

    creator.create_task("Enviar correo a cliente", "Email", "alta")
    creator.create_task("Actualizar documento", "Doc", "media")
    creator.create_task("Reunión con equipo", "Meeting", "baja")

    # email_notifier y sms_notifier pasarian a ser clientes de la clase TaskRepository,
    # cuya responsabilidad es almacenar las tareas
    email_notifier = EmailNotifier(task_repo)
    sms_notifier = SMSNotifier(task_repo)
    email_notifier.notify()
    sms_notifier.notify()

    exporter = PDFExporter(task_repo)
    exporter.export()

if __name__ == "__main__":
    main()
