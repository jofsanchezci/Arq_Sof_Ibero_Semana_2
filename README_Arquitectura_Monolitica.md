
# Arquitectura Monolítica para un Sistema de Mensajería

Este proyecto implementa un sistema de mensajería utilizando una arquitectura monolítica. Todas las funcionalidades del sistema están contenidas dentro de una sola aplicación.

## Estructura del Proyecto

```
Arq_Sof_Ibero/
├── MessagingApp.py          # Archivo principal que contiene toda la lógica de la aplicación
```

## Descripción del Sistema

El sistema está diseñado de manera monolítica, lo que significa que todas las funciones y responsabilidades, como la gestión de usuarios y el envío de mensajes, están contenidas en una única aplicación.

### Clases Principales:

#### 1. `User`
La clase `User` representa a un usuario en el sistema.

- **Atributos**:
  - `username`: Nombre del usuario.
  - `inbox`: Lista de mensajes recibidos.

- **Métodos**:
  - **send_message(recipient, message)**: Envía un mensaje a otro usuario.
  - **read_inbox()**: Muestra los mensajes recibidos en la bandeja de entrada.

#### 2. `MessagingApp`
La clase `MessagingApp` coordina las acciones del sistema, permitiendo la gestión de usuarios y el envío de mensajes.

- **Métodos**:
  - **register_user(username)**: Registra un nuevo usuario.
  - **send_message(sender, recipient, message)**: Envía un mensaje entre dos usuarios.
  - **show_inbox(username)**: Muestra la bandeja de entrada de un usuario.

## Ejemplo de Uso:

```python
# Ejemplo de uso del sistema de mensajería
app = MessagingApp()
app.register_user("Alice")
app.register_user("Bob")

app.send_message("Alice", "Bob", "Hola, Bob!")
app.show_inbox("Bob")
```

## Ventajas de la Arquitectura Monolítica
1. **Simplicidad**: Todo el sistema está en un solo lugar, lo que facilita el desarrollo y el despliegue para proyectos pequeños o medianos.
2. **Desarrollo rápido**: No requiere gestionar la comunicación entre servicios, lo que acelera el desarrollo inicial.
3. **Fácil de probar**: No hay dependencias externas entre servicios, lo que simplifica las pruebas.

## Desventajas de la Arquitectura Monolítica
1. **Escalabilidad limitada**: A medida que el sistema crece, puede volverse difícil escalar eficientemente.
2. **Difícil de mantener en grandes proyectos**: Los cambios en una parte del sistema pueden afectar otras áreas, lo que aumenta la complejidad a largo plazo.
3. **Despliegue**: Requiere desplegar todo el sistema aunque solo se haga un pequeño cambio en una funcionalidad.

## Despliegue

Para ejecutar este proyecto, simplemente corre el archivo `MessagingApp.py`:

```bash
python MessagingApp.py
```

Este comando ejecutará el sistema de mensajería y te permitirá interactuar con los usuarios y mensajes.

## Requerimientos

Este proyecto no tiene dependencias externas, ya que está basado en una implementación simple utilizando clases en Python.
