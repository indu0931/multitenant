from app.connectors.database_connector import Base
import sqlalchemy as sa
from datetime import datetime

class Review(Base):
    __tablename__ = "reviews"

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False)  
    booking_id: int = sa.Column(sa.Integer, sa.ForeignKey('bookings.id'), nullable=False)  
    user_id: int = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)   
    rating: int = sa.Column(sa.Integer, nullable=False) 
    review_text: str = sa.Column(sa.String(1000), nullable=True)  
    created_at: datetime = sa.Column(sa.DateTime, nullable=False, default=sa.func.now())  
    updated_at: datetime = sa.Column(sa.DateTime, nullable=True, default=sa.func.now(), onupdate=sa.func.now())  

    
    booking = sa.orm.relationship("Booking", backref="reviews")
    user = sa.orm.relationship("User", backref="reviews")
