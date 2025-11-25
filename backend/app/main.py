from fastapi import FastAPI
from .config import settings
from .routes import router as readings_router
from .db import get_session, shutdown

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Sistema distribuido IoT con Cassandra (proyecto de Sistemas Distribuidos)"
)

@app.on_event("startup")
def startup_event():
    # Fuerza la conexión al iniciar la app
    get_session()
    print("[APP] Aplicación iniciada")

@app.on_event("shutdown")
def shutdown_event():
    shutdown()
    print("[APP] Aplicación detenida")

@app.get("/")
def root():
    return {"message": "API IoT con Cassandra - Sistema Distribuido"}

# Incluir rutas de lecturas
app.include_router(readings_router, prefix="", tags=["Readings"])
