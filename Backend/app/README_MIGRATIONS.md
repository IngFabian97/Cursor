# Migraciones de Base de Datos - Platziflix

Este documento describe cómo usar Alembic para gestionar las migraciones de base de datos en el proyecto Platziflix.

## Estructura de la Base de Datos

### Tablas Creadas

1. **teachers** - Profesores de los cursos
   - `id` (Primary Key)
   - `name` (String, 255 chars)
   - `email` (String, 255 chars, unique)
   - `created_at` (DateTime)
   - `updated_at` (DateTime)
   - `deleted_at` (DateTime, nullable)

2. **courses** - Cursos de la plataforma
   - `id` (Primary Key)
   - `name` (String, 255 chars)
   - `description` (Text)
   - `thumbnail` (String, 500 chars, nullable)
   - `slug` (String, 255 chars, unique)
   - `created_at` (DateTime)
   - `updated_at` (DateTime)
   - `deleted_at` (DateTime, nullable)
   - `teacher_id` (Foreign Key a teachers.id)

3. **classes** - Clases de los cursos
   - `id` (Primary Key)
   - `name` (String, 255 chars)
   - `description` (Text)
   - `slug` (String, 255 chars)
   - `video_url` (String, 500 chars, nullable)
   - `created_at` (DateTime)
   - `updated_at` (DateTime)
   - `deleted_at` (DateTime, nullable)
   - `course_id` (Foreign Key a courses.id)

## Comandos de Alembic

### Configuración Inicial
```bash
# Inicializar Alembic (ya realizado)
alembic init alembic

# Ver el estado actual de las migraciones
alembic current

# Ver el historial de migraciones
alembic history
```

### Generar Migraciones
```bash
# Generar una nueva migración automáticamente
alembic revision --autogenerate -m "Descripción de la migración"

# Generar una migración manual
alembic revision -m "Descripción de la migración"
```

### Aplicar Migraciones
```bash
# Aplicar todas las migraciones pendientes
alembic upgrade head

# Aplicar hasta una migración específica
alembic upgrade <revision_id>

# Aplicar una migración hacia adelante
alembic upgrade +1
```

### Revertir Migraciones
```bash
# Revertir la última migración
alembic downgrade -1

# Revertir hasta una migración específica
alembic downgrade <revision_id>

# Revertir todas las migraciones
alembic downgrade base
```

### Información
```bash
# Ver el estado actual
alembic current

# Ver el historial
alembic history

# Ver información de una migración específica
alembic show <revision_id>
```

## Configuración

### Variables de Entorno
Asegúrate de tener configurada la variable `DATABASE_URL` en tu archivo `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/platziflix
```

### Archivos de Configuración
- `alembic.ini` - Configuración principal de Alembic
- `alembic/env.py` - Script de entorno de Alembic
- `alembic/versions/` - Directorio con las migraciones

## Modelos SQLAlchemy

Los modelos están definidos en:
- `app/models/teacher.py` - Modelo Teacher
- `app/models/course.py` - Modelo Course
- `app/models/class_model.py` - Modelo Class

## Notas Importantes

1. **Soft Deletes**: Todas las tablas incluyen un campo `deleted_at` para implementar soft deletes
2. **Timestamps**: Los campos `created_at` y `updated_at` se manejan automáticamente
3. **Slugs**: Los campos `slug` permiten URLs amigables
4. **Relaciones**: 
   - Un Teacher puede tener muchos Courses
   - Un Course puede tener muchas Classes
   - Un Course pertenece a un Teacher

## Próximos Pasos

1. Configurar la base de datos PostgreSQL
2. Ejecutar `alembic upgrade head` para aplicar las migraciones
3. Crear datos de prueba
4. Implementar los endpoints de la API 