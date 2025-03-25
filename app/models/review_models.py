from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewCreateRequest(BaseModel):
    booking_id: int
    user_id: int
    rating: int
    review_text: Optional[str] = None

class ReviewResponse(BaseModel):
    id: int
    booking_id: int
    user_id: int
    rating: int
    review_text: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
