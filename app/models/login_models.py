from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AdminCreateRequest(BaseModel):
    role_id: int
    username: str
    password: str
    is_active: Optional[bool] = True  

class AdminResponse(BaseModel):
    id: int
    role_id: int
    username: str
    created_at: datetime
    is_active: bool

    class Config:
        orm_mode = True
