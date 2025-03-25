from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentCreateRequest(BaseModel):
    amount: float
    bank_id: int
    date: Optional[datetime] = None
    method: Optional[str] = None
    access_key: Optional[str] = None
    is_active: Optional[bool] = True 

class PaymentResponse(BaseModel):
    id: int
    amount: float
    bank_id: int
    date: Optional[datetime]
    method: Optional[str]
    access_key: Optional[str]
    created_at: datetime
    is_active: bool

    class Config:
        orm_mode = True
