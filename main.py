import os
from fastapi import FastAPI

app = FastAPI(title="Hello Cloud Run")


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Hola desde Cloud Run 🎉",
        "port": os.environ.get("PORT")
    }
