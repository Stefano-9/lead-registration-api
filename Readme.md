# Lead Registration API

Este proyecto es una API RESTful construida con FastAPI que permite registrar leads, los cuales son personas cursando materias en diversas carreras. La API permite registrar estos leads junto con la información de las materias que está cursando y proporciona endpoints para consultar los registros.

## Características

- Registrar un lead con sus datos personales y las materias que está cursando.
- Obtener todos los leads registrados de manera paginada.
- Obtener un lead específico por su ID.
- Dockerización del backend con FastAPI y PostgreSQL.

## Tecnologías Utilizadas

- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- Docker
- Docker Compose

## Configuración del Proyecto

Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/lead-registration-api.git
cd lead-registration-api

Crea un archivo .env en la raíz del proyecto con el siguiente contenido:
POSTGRES_USER=postgres
POSTGRES_PASSWORD=41957458
POSTGRES_DB=postgres

Construir y ejecutar la aplicación con Docker Compose:
docker-compose up --build

Una vez que los contenedores estén en funcionamiento, puedes acceder a la documentación interactiva de la API en:
http://localhost:8000/docs

Uso de la API
Registrar un Lead
Endpoint: POST /leads/
{
  "full_name": "John Doe",
  "email": "johndoe@example.com",
  "address": "123 Main St, Springfield",
  "phone_number": "555-1234",
  "courses": [
    {
      "name": "Python Programming",
      "duration": 30,
      "year": 2023
    },
    {
      "name": "Data Science",
      "duration": 45,
      "year": 2023
    }
  ]
}

Response:
200 OK: Registro exitoso del lead.
400 Bad Request: Si el email ya está registrado.

Obtener Leads Paginados
Endpoint: GET /leads/

Query Parameters:

skip: Número de registros a saltar (por defecto 0).
limit: Número máximo de registros a devolver (por defecto 10).

[
  {
    "id": 1,
    "full_name": "John Doe",
    "email": "johndoe@example.com",
    "address": "123 Main St, Springfield",
    "phone_number": "555-1234",
    "courses": [
      {
        "id": 1,
        "name": "Python Programming",
        "duration": 30,
        "year": 2023
      },
      {
        "id": 2,
        "name": "Data Science",
        "duration": 45,
        "year": 2023
      }
    ]
  }
]
Obtener un Lead por ID
Endpoint: GET /leads/{lead_id}

Path Parameters:

lead_id: ID del lead a consultar.
{
  "id": 1,
  "full_name": "John Doe",
  "email": "johndoe@example.com",
  "address": "123 Main St, Springfield",
  "phone_number": "555-1234",
  "courses": [
    {
      "id": 1,
      "name": "Python Programming",
      "duration": 30,
      "year": 2023
    },
    {
      "id": 2,
      "name": "Data Science",
      "duration": 45,
      "year": 2023
    }
  ]
}
Documentación Técnica
La estructura del proyecto sigue una organización común para aplicaciones FastAPI. A continuación, se describe brevemente cada componente:

app/main.py: Contiene la configuración principal de la aplicación FastAPI y define los endpoints de la API.
app/models.py: Define los modelos de datos utilizando SQLAlchemy.
app/schemas.py: Define los esquemas de Pydantic utilizados para validar las entradas y salidas de la API.
app/crud.py: Contiene las operaciones CRUD para interactuar con la base de datos.
app/database.py: Configura la conexión a la base de datos y la sesión de SQLAlchemy.
Dockerfile: Define la imagen de Docker para la API.
docker-compose.yml: Configura y orquesta los contenedores de Docker para la base de datos y la API.

Ejecución de Migraciones
Si en el futuro necesitas realizar cambios en el esquema de la base de datos, puedes utilizar Alembic para manejar las migraciones. Asegúrate de que Alembic esté configurado correctamente en tu proyecto.