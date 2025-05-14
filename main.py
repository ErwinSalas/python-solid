from services.task_service import TaskService
from services.task_notifier import TaskNotifier
from services.task_exporter import ExportService, PdfExport
def main():
    notification_service = TaskNotifier()
    export_service = ExportService(PdfExport())
    task_service = TaskService(notification_service, export_service)

    task_service.create_task("Enviar correo a cliente", "Email", "alta")
    task_service.create_task("Actualizar documento", "Doc", "media")

    task_service.notify_users()
    task_service.export_tasks("pdf")

if __name__ == "__main__":
    main()

