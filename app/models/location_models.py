from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LocationCreateRequest(BaseModel):
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class LocationResponse(BaseModel):
    id: int
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
