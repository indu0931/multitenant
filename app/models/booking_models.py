from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BookingCreateRequest(BaseModel):
    user_id: int
    service_id: int
    start_date: datetime
    end_date: datetime
    total_amount: float
    payment_status: Optional[str] = 'unpaid'  
    status: Optional[str] = 'pending'  

class BookingResponse(BaseModel):
    id: int
    user_id: int
    service_id: int
    start_date: datetime
    end_date: datetime
    status: str
    total_amount: float
    payment_status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
