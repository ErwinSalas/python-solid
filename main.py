import services.task_service as task_service

def main():
    task_service_instance = task_service.TaskService()
    task_creator = task_service.TaskCreator(task_service_instance)
    task_notifier = task_service.HighPriorityNotifier(task_service_instance)
    task_pdf_exporter = task_service.ExportToPDF(task_service_instance)

    task_creator.create_task("Tarea 1", "Alta")
    task_creator.create_task("Tarea 2", "Media")
    task_creator.create_task("Tarea 3", "Baja")

    task_notifier.notify()

    task_pdf_exporter.export()

if __name__ == "__main__":
    main()
