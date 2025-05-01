## SRP
Cada clase ahora tiene una única responsabilidad:
    TaskCreator: crea tareas
    TaskNotifier: coordina notificaciones
    TaskExporter: coordina exportaciones
Esto evita que una sola clase tenga múltiples razones para cambiar.

## OCP
La lógica de exportación y notificación se divide en clases extensibles:
    PdfExporter, CsvExporter
    EmailNotifier, SMSNotifier

## DIP
TaskService ahora depende de interfaces en lugar de implementaciones concretas.Para poder así desacoplar componentes y facilita pruebas.

## ISP y LSP
Cumple indirectamente con ISP y permite respetar LSP aunque no se aplicaron exactamente las subclases en este caso.