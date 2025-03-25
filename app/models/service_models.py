from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ServiceCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    location_id: int

class ServiceResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    location_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
