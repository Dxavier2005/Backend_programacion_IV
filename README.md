#  backend de Gestión de Eventos

Este proyecto es una API RESTful desarrollada con **Django** y **Django REST Framework (DRF)** para la gestión integral de eventos y conferencias.

## Instalación y Ejecución

Sigue estos pasos en tu terminal para poner en marcha el backend:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Dxavier2005/Backend_programacion_IV.git](https://github.com/Dxavier2005/Backend_programacion_IV.git)
   cd Backend_programacion_IV

## Sincronizar dependencias:
uv sync
## Aplicar migraciones:

uv run python manage.py migrate

## Ejecutar el servidor:


uv run python manage.py runserver

## Autenticación y Seguridad
La API utiliza JWT (JSON Web Token). Para consumir los endpoints protegidos:

Login: Realiza una petición POST a /api/token/ enviando tu username y password.

Autorización: En el cliente (Postman), usa la pestaña Authorization, selecciona Bearer Token y pega el token obtenido.

Roles: Los usuarios con permisos de administrador tienen acceso a las operaciones de creación, edición y eliminación (POST, PUT, DELETE).