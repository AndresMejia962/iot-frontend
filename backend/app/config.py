import os
from dotenv import load_dotenv

# Carga variables desde .env si existe
load_dotenv()

class Settings:
    APP_NAME: str = "IoT Cassandra Distributed System"
    APP_PORT: int = int(os.getenv("PORT", 8000))

    CASSANDRA_CONTACT_POINTS: list[str] = os.getenv(
        "CASSANDRA_CONTACT_POINTS",
        "127.0.0.1:9042"
    ).split(",")
    CASSANDRA_DATACENTER: str = os.getenv(
        "CASSANDRA_DATACENTER",
        "datacenter1"
    )
    CASSANDRA_KEYSPACE: str = os.getenv(
        "CASSANDRA_KEYSPACE",
        "iot"
    )

settings = Settings()
