from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from .db import get_session
from .models import ReadingIn, ReadingOut

router = APIRouter()

@router.post("/readings", response_model=dict)
def create_reading(reading: ReadingIn):
    session = get_session()

    query = """
        INSERT INTO readings (sede, sensor_type, sensor_id, ts, value)
        VALUES (%s, %s, %s, %s, %s)
    """
    ts = datetime.utcnow()

    try:
        session.execute(
            query,
            (reading.sede, reading.sensor_type, reading.sensor_id, ts, reading.value)
        )
        return {"ok": True, "message": "Lectura registrada", "ts": ts}
    except Exception as e:
        print("[CASSANDRA] Error al insertar lectura:", e)
        raise HTTPException(status_code=500, detail="Error al insertar lectura")


@router.get("/readings", response_model=List[ReadingOut])
def list_readings(
    sede: str = Query(...),
    sensor_type: str = Query(...),
    from_ts: Optional[datetime] = Query(None),
    to_ts: Optional[datetime] = Query(None)
):
    session = get_session()

    query = """
        SELECT sede, sensor_type, sensor_id, ts, value
        FROM readings
        WHERE sede = %s AND sensor_type = %s
    """
    params: list = [sede, sensor_type]

    # Importante: Cassandra exige que las condiciones respeten el PRIMARY KEY.
    # Como ts es clustering key, se puede usar >= y <=
    if from_ts:
        query += " AND ts >= %s"
        params.append(from_ts)
    if to_ts:
        query += " AND ts <= %s"
        params.append(to_ts)

    query += " ALLOW FILTERING"  # para evitar problemas en pruebas; luego se puede refinar

    try:
        result = session.execute(query, params)
        readings = [
            ReadingOut(
                sede=row.sede,
                sensor_type=row.sensor_type,
                sensor_id=row.sensor_id,
                ts=row.ts,
                value=row.value
            )
            for row in result
        ]
        return readings
    except Exception as e:
        print("[CASSANDRA] Error al consultar lecturas:", e)
        raise HTTPException(status_code=500, detail="Error al consultar lecturas")
