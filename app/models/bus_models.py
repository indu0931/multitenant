from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BusCreateRequest(BaseModel):
    bus_type: str
    description: str
    is_active: bool = True

class BusResponse(BaseModel):
    id: int
    bus_type: str
    description: str
    created_at: datetime
    is_active: bool

    class Config:
        orm_mode = True  
