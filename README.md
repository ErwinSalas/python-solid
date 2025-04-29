# 📝 Proyecto: Refactorizando Task Manager (Aplicando SOLID)

## 🎯 Objetivo

Refactorizar un pequeño proyecto Python aplicando los principios **SOLID**. El sistema actual es funcional, pero está lleno de *antipatrones de diseño* y clases con múltiples responsabilidades. Tu misión será mejorar su estructura sin romper su comportamiento.

---

## 📦 Descripción del Proyecto

El proyecto `task_manager` simula un sistema simple de gestión de tareas. Permite crear tareas, notificar usuarios y exportar los datos.

Actualmente, todas estas funcionalidades están centralizadas en una sola clase llamada `TaskService`, lo que provoca varios problemas de diseño.

---

## 🚫 Problemas Identificados (Antipatrones)

### 🔹 SRP – Single Responsibility Principle
La clase `TaskService` hace de todo: crear tareas, notificarlas, y exportarlas.

### 🔹 OCP – Open/Closed Principle
La lógica de exportación está acoplada mediante condicionales. Para agregar un nuevo formato, hay que modificar el código.

### 🔹 DIP – Dependency Inversion Principle
El servicio está acoplado directamente a la lógica interna de notificación y exportación.

### 🔹 (Opcional) LSP / ISP
Puedes extender el proyecto para explorar estos principios creando subclases de tareas o interfaces específicas para distintos canales de notificación.

---

## 🧩 Tu Misión

1. **Analiza** el código actual y detecta qué partes violan los principios SOLID.
2. **Refactoriza** aplicando un principio a la vez, usando ramas o commits separados.
3. **Documenta** tus cambios:
    - Cada commit debe indicar claramente qué principio estás aplicando.
    - Agrega un archivo `SOLID_JUSTIFICACION.md` explicando tus decisiones.


---

## 🛠 Sugerencias de Refactor

- Crea clases específicas para `TaskNotifier`, `TaskExporter`, etc.
- Usa herencia o composición para separar responsabilidades.
- Usa interfaces o clases base para permitir extensibilidad.

---

## 🧪 FORMATO DEL PULL REQUEST

- Adjuntar en la descripcion un texto explicando y justificando los cambios.
---

¡Buena suerte!
