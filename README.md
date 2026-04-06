# Solemne 1 - API de Tiempo con FastAPI y Docker

Una aplicación FastAPI sencilla que expone un endpoint `/time` que devuelve la fecha y hora actual en formato JSON, con automatización CI/CD usando GitHub Actions y dockerización.

## Descripción del Proyecto

Este proyecto implementa:

- **API REST** con FastAPI que consulta la hora actual desde servidores NTP
- **Pruebas Unitarias** con pytest
- **Containerización** con Docker
- **CI/CD Automatizado** con GitHub Actions
- Hora en zona horaria de **Chile (America/Santiago)** utilizando `pytz` para convertir timestamps NTP a datetime con zona horaria

## Requisitos Previos

- Python 3.11+
- `uv` (gestor de dependencias y entorno virtual)
- Docker (para ejecución en contenedor)
- Git

## Instalación Local

### 1. Clonar el repositorio

```bash
git clone <tu-repositorio>
cd Solemne1
```

### 2. Instalar dependencias con uv

```bash
uv pip install -r requirements.txt
```

### 3. Ejecutar la aplicación localmente

```bash
python main.py
```

La aplicación estará disponible en `http://localhost:8000/time`

## Uso de la API

### Endpoint: GET /time

Devuelve la fecha y hora actual en la zona horaria de Chile.

#### Ejemplo de solicitud:

```bash
curl http://localhost:8000/time
```

#### Ejemplo de respuesta:

```json
{
  "Año-Mes-Día": "2026-4-1",
  "Hora:Minutos:Segundo": "14:30:45"
}
```

#### Desde el navegador web:

Simplemente abre en tu navegador:

```
http://localhost:8000/time
```

También puedes acceder a la documentación interactiva de Swagger:

```
http://localhost:8000/docs
```

## Pruebas

### Ejecutar todas las pruebas

```bash
uv pip install pytest
pytest test_main.py -v
```

### Pruebas disponibles:

- `test_get_current_time()`: Verifica el formato correcto de la respuesta
- `test_time_endpoint_returns_json()`: Verifica que el content-type sea JSON
- `test_time_values_are_valid_integers()`: Valida que los valores de tiempo sean válidos

## Ejecución con Docker

### 1. Construir la imagen Docker

```bash
docker build -t solemne1:latest .
```

### 2. Ejecutar el contenedor

```bash
docker run -p 8000:8000 solemne1:latest
```

La aplicación estará disponible en `http://localhost:8000`

### 3. Acceder a la API

```bash
curl http://localhost:8000/time
```

## CI/CD con GitHub Actions

El proyecto incluye un flujo de trabajo automático que se activa con cada `push` a las ramas `main` o `develop`.

### Pasos del flujo CI/CD:

1. **Checkout**: Descarga el código
2. **Setup Python**: Configura Python 3.11
3. **Install Dependencies**: Instala uv y las dependencias
4. **Lint**: Valida el código con `ruff`
5. **Test**: Ejecuta las pruebas con `pytest`
6. **Build & Push Docker**: Construye y publica la imagen en Docker Hub (solo en rama `main`)

### Configuración de Secretos en GitHub

Para que el flujo CI/CD publique en Docker Hub, debes configurar los siguientes secretos en tu repositorio:

1. Ve a **Settings** → **Secrets and variables** → **Actions**
2. Crea los siguientes secretos:
   - `DOCKER_USERNAME`: Tu nombre de usuario en Docker Hub
   - `DOCKER_PASSWORD`: Tu token de acceso en Docker Hub

#### Cómo generar un token de Docker Hub:

1. Inicia sesión en [Docker Hub](https://hub.docker.com)
2. Ve a **Account Settings** → **Security** → **New Access Token**
3. Crea un token con permisos de lectura y escritura
4. Copia el token y úsalo en el secreto `DOCKER_PASSWORD`

## Estructura del Proyecto

```
Solemne1/
├── main.py                  # Aplicación FastAPI
├── test_main.py            # Pruebas unitarias
├── Dockerfile              # Configuración Docker
├── pyproject.toml          # Configuración del proyecto (UV)
├── requirements.txt        # Dependencias de pip
├── .gitignore             # Archivos a ignorar en Git
├── README.md              # Este archivo
└── .github/
    └── workflows/
        └── main.yml       # Flujo CI/CD de GitHub Actions
```

## Dependencias

- **fastapi**: Framework web para crear APIs REST
- **uvicorn**: Servidor ASGI para ejecutar FastAPI
- **ntplib**: Cliente NTP para obtener la hora exacta
- **pytz**: Librería para manejo de zonas horarias
- **pytest**: Framework de pruebas (dev)
- **ruff**: Linter de Python (dev)

## Notas Importantes

- La hora se obtiene desde servidores NTP (`cl.pool.ntp.org`) para garantizar precisión
- La zona horaria utilizada es **America/Santiago** (Chile UTC-3/-4), implementada mediante `pytz.timezone('America/Santiago')` en `datetime.fromtimestamp()`
- El contenedor Docker expone el puerto **8000**
- Las pruebas se ejecutan automáticamente en cada push a través de GitHub Actions

## Autor(es)

Proyecto Solemne 1 - Aplicaciones y Tecnologías Web

## Licencia

Este proyecto está disponible bajo la Licencia MIT.
