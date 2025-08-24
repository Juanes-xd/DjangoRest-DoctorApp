# DjangoRest DoctorApp

Pequeña API REST para gestionar médicos, pacientes y reservas (appointments).

Características principales
- Endpoints para pacientes, médicos y reservas.
- Documentación automática con drf-spectacular (OpenAPI) y UIs Swagger / ReDoc.
- Django 5 + Django REST Framework.

Requisitos
- Python 3.11+ (o la versión compatible que uses en tu entorno)
- Virtualenv (recomendado)

Instalación (PowerShell)
```powershell
# Desde la raíz del proyecto
# 1) Crear y activar entorno virtual (si aún no lo tienes)
python -m venv venv
; .\venv\Scripts\Activate.ps1

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Migrar la base de datos
python manage.py migrate

# 4) (Opcional) Crear superusuario para acceder al admin
python manage.py createsuperuser

# 5) Ejecutar servidor de desarrollo
python manage.py runserver
```

Rutas de documentación (disponibles cuando el servidor esté corriendo)
- Esquema OpenAPI (JSON/YAML): /api/schema/
- Swagger UI: /api/schema/swagger-ui/
- ReDoc: /api/schema/redoc/

Ejemplos de endpoints (prefijo `/api/`)
- Pacientes:
  - `GET /api/patients/`
  - `GET /api/patients/<id>/`
  - `GET /api/insurances/`
  - `GET /api/medicalrecords/`

- Médicos:
  - `GET /api/doctors/`  (también disponible por el router del ViewSet)
  - `GET /api/departments/`
  - `GET /api/doctoravailabilities/`
  - `GET /api/medicalnotes/`

- Reservas (bookings):
  - `GET /api/appointments/`
  - `GET /api/medicalnotes/` (booking-related notes)

Autenticación
- La app incluye `rest_framework` con `SessionAuthentication` activado. Puedes iniciar sesión en `/api-auth/login/` (si estás usando la UI de DRF) o usar el admin para crear usuarios.

Ejecutar tests
```powershell
python manage.py test
```

Resolución de errores comunes
- ModuleNotFoundError: No module named 'drf_spectacular'
  - Asegúrate de activar el entorno virtual donde instalaste las dependencias.
  - Reinstala con `pip install drf-spectacular` (o `pip install -r requirements.txt`).

Notas de configuración
- `doctorapp/settings.py` ya contiene la configuración mínima para drf-spectacular:
  - `REST_FRAMEWORK['DEFAULT_SCHEMA_CLASS'] = 'drf_spectacular.openapi.AutoSchema'`
- Las rutas de documentación están definidas en `docs/urls.py` como:
  - `api/schema/`, `api/schema/swagger-ui/`, `api/schema/redoc/`.

Contribuir
- Si quieres añadir endpoints o mejorar la documentación, crea una rama nueva y abre un PR.

Contacto
- Este README fue generado automáticamente para el proyecto local. Si necesitas ejemplos de requests (curl/Postman) o ayuda para desplegar, pídeme y los preparo.
