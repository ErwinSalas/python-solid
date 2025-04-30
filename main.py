from services.task_service import TaskService

def main():
    task_service = TaskService()
    task_service = NotifyUsers(prioridad1)
    task_service = ExportarTasks(pdf, prioridad2)
    task_service.create_task("Reunión con equipo", "Meeting", "baja")

    task_service.notify_users()
    task_service.export_tasks("pdf")

if __name__ == "__main__":
    main()
