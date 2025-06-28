# Platziflix FastAPI Application
# Main entry point for the API 

from fastapi import FastAPI, Depends
from typing import Annotated

from app.core.config import get_settings, Settings

# Crear instancia FastAPI
app = FastAPI(
    title="Platziflix API",
    description="Plataforma de cursos online",
    version="0.1.0"
)

@app.get("/")
async def read_root():
    return {"message": "¡Bienvenido a Platziflix!"}

@app.get("/health")
async def read_health(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "status": "ok",
        "service_name": settings.PROJECT_NAME,
        "version": settings.VERSION
    } 