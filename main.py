from services.task_service import TaskService,EmailNotificationService,SMSNotificationService, exportPDFService, exportCSVService

def main():
    task_service = TaskService()
    emailNotification_Service = EmailNotificationService()
    smsNotification_Service = SMSNotificationService()
    export_pdf_service = exportPDFService()
    export_csv_service = exportCSVService()
    task_service.create_task("Enviar correo a cliente", "Email", "alta")
    task_service.create_task("Actualizar documento", "Doc", "media")
    task_service.create_task("Reunión con equipo", "Meeting", "baja")

    emailNotification_Service.notify()
    smsNotification_Service.notify()
    export_pdf_service.export()
    export_csv_service.export()


main()