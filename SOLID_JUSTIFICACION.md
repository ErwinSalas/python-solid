###  Cambios aplicados
SRP: se separaron responsabilidades en clases individuales (`TaskCreator`, `TaskNotifier`, `TaskExporter`)
OCP: eliminación de condicionales mediante clases extensibles (`PdfExporter`, `EmailNotifier`, etc.)
DIP: el servicio principal depende de interfaces (`Creator`, `Notifier`, `Exporter`)
ISP: se crearon métodos específicos como `can_notify()` y `can_export()` para responsabilidades concretas
Se reorganizó el proyecto en carpetas por rol (services, interfaces, notifiers, exporters).
Documentación detallada en `SOLID_JUSTIFICACION.md`.
El sistema mantiene su funcionalidad original, con código más limpio, mantenible y extensible.
