from app.connectors.database_connector import Base
import sqlalchemy as sa
from datetime import datetime

class Booking(Base):
    __tablename__ = "bookings"

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False)  
    user_id: int = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    service_id: int = sa.Column(sa.Integer, sa.ForeignKey('services.id'), nullable=False)  
    start_date: datetime = sa.Column(sa.DateTime, nullable=False)
    end_date: datetime = sa.Column(sa.DateTime, nullable=False)  
    status: str = sa.Column(sa.String(50), nullable=False, default='pending')  
    total_amount: sa.Numeric = sa.Column(sa.Numeric(10, 2), nullable=False)
    payment_status: str = sa.Column(sa.String(50), nullable=False, default='unpaid')  
    created_at: datetime = sa.Column(sa.DateTime, nullable=False, default=sa.func.now())  
    updated_at: datetime = sa.Column(sa.DateTime, nullable=True, default=sa.func.now(), onupdate=sa.func.now()) 

    
    user = sa.orm.relationship("User", backref="bookings")
    service = sa.orm.relationship("Service", backref="bookings")
