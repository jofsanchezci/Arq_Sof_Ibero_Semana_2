
# Arquitectura de Microservicios para un Sistema de Mensajería

Este proyecto implementa un sistema de mensajería utilizando una arquitectura de microservicios. Los microservicios están diseñados para ser modulares, lo que permite su escalabilidad y mantenimiento independiente.

## Estructura del Proyecto

```
Arq_Sof_Ibero/
├── MessagingApp.py          # Archivo principal que coordina los servicios
├── services/                # Carpeta donde se almacenan los servicios
│   ├── user_service.py      # Servicio para la gestión de usuarios
│   ├── message_service.py   # Servicio para la gestión de mensajes
│   └── __init__.py          # Archivo vacío para indicar que services es un paquete
```

## Descripción de los Microservicios

### 1. `UserService` (`user_service.py`)
Este servicio maneja toda la lógica relacionada con la gestión de usuarios. 

#### Funciones principales:
- **register_user(username)**: Registra un nuevo usuario en el sistema.
- **get_user(username)**: Devuelve la información de un usuario específico.

### 2. `MessageService` (`message_service.py`)
Este servicio gestiona el envío y la recepción de mensajes entre los usuarios.

#### Funciones principales:
- **send_message(sender, recipient, message)**: Enviar un mensaje desde un usuario a otro.
- **read_inbox(username)**: Leer la bandeja de entrada de un usuario específico.

## Coordinación entre Microservicios

El archivo `MessagingApp.py` actúa como un coordinador que integra los microservicios. Utiliza el `UserService` y el `MessageService` para registrar usuarios, enviar mensajes y mostrar los mensajes recibidos.

### Ejemplo de Uso:

```python
# Ejemplo de uso del sistema de mensajería
app = MessagingApp()
print(app.register_user("Alice"))
print(app.register_user("Bob"))

print(app.send_message("Alice", "Bob", "Hola, Bob!"))
print(app.show_inbox("Bob"))
```

## Ventajas de la Arquitectura de Microservicios
1. **Escalabilidad independiente**: Cada servicio puede escalarse por separado según sea necesario.
2. **Despliegue separado**: Cada microservicio puede ser desarrollado, probado y desplegado de manera independiente.
3. **Modularidad**: Facilita el mantenimiento y las actualizaciones sin afectar a todo el sistema.

## Despliegue

Para ejecutar este proyecto, asegúrate de tener los servicios en su respectiva carpeta. Puedes ejecutar el sistema con:

```bash
python MessagingApp.py
```

Este comando ejecutará el sistema de mensajería y te permitirá interactuar con los usuarios y mensajes.

## Requerimientos

Este proyecto no tiene dependencias externas, ya que está basado en una implementación simple de microservicios utilizando clases en Python.
