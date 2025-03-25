from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CancellationCreateRequest(BaseModel):
    payment_id: int
    reason: str
    cancelled_by: str
    refund_amount: Optional[float] = None
    status: Optional[str] = 'pending'  

class CancellationResponse(BaseModel):
    id: int
    payment_id: int
    reason: str
    cancelled_by: str
    cancellation_date: datetime
    status: str
    refund_amount: Optional[float]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
