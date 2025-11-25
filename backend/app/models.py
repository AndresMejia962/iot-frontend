from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ReadingIn(BaseModel):
    sede: str = Field(..., example="Sede Norte")
    sensor_type: str = Field(..., example="temperature")
    sensor_id: str = Field(..., example="sensor-001")
    value: float = Field(..., example=23.7)

class ReadingOut(BaseModel):
    sede: str
    sensor_type: str
    sensor_id: str
    ts: datetime
    value: float

class ReadingQuery(BaseModel):
    sede: str
    sensor_type: str
    from_ts: Optional[datetime] = None
    to_ts: Optional[datetime] = None
