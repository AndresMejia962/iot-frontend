# Imagen base
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Cloud Run usa esta variable PORT
ENV PORT=8080

# Comando de arranque
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
