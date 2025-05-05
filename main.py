from services.task_creator import TaskCreator
from services.task_service import TaskService
from services.task_exporter import TaskExporter
from services.task_notifier import TaskNotifier

from services.exporters.pdf_exporter import PdfExporter
from services.exporters.csv_exporter import CsvExporter
from services.notifiers.email_notifier import EmailNotifier
from services.notifiers.sms_notifier import SMSNotifier

def main():
    creator = TaskCreator()
    notifier = TaskNotifier([EmailNotifier(), SMSNotifier()])
    exporter = TaskExporter([PdfExporter(), CsvExporter()])


    service = TaskService(creator, notifier, exporter)

    service.create_task("Enviar correo a cliente", "Email", "alta")
    service.create_task("Actualizar documento", "Doc", "media")
    service.create_task("Reunión con equipo", "Meeting", "baja")

    service.notify_users()
    service.export_tasks("pdf")

if __name__ == "__main__":
    main()
