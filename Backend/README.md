# 🎓 Platziflix

Plataforma de cursos online simple y directa.

## Descripción

Platziflix es una plataforma minimalista enfocada en la distribución de contenido educativo. Cada curso contiene clases con descripciones básicas.

## Stack Tecnológico

- **Backend**: Python + FastAPI + PostgreSQL
- **Frontend**: TypeScript + CSS Modules + SASS
- **Mobile**: Swift + SwiftUI (iOS) / Kotlin + Jetpack Compose (Android)

## Estructura del Proyecto

```
platziflix/
├── app/
│   ├── __init__.py
│   ├── main.py          # Aplicación FastAPI
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py    # Configuración de la aplicación
│   └── db/
│       ├── __init__.py
│       └── base.py      # Configuración de base de datos
├── pyproject.toml       # Dependencias y configuración
└── README.md
```

## Estado del Proyecto

🚧 **En desarrollo** - Estructura básica creada

## Próximos Pasos

1. ✅ Crear estructura básica del proyecto
2. ⏳ Configurar dependencias
3. ⏳ Crear configuración de la aplicación
4. ⏳ Implementar aplicación FastAPI básica
5. ⏳ Dockerizar la aplicación

## Características

- API REST con FastAPI
- Base de datos PostgreSQL
- Configuración con variables de entorno
- Docker y Docker Compose para desarrollo

## Instalación

### Desarrollo Local

```bash
uv sync
uv run uvicorn app.main:app --reload
```

### Con Docker

```bash
docker compose up --build
```

## Endpoints

- `GET /`: Mensaje de bienvenida
- `GET /health`: Estado del servicio
- `GET /docs`: Documentación automática de la API 