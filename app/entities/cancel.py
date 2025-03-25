from app.connectors.database_connector import Base
import sqlalchemy as sa
from datetime import datetime

class Cancellation(Base):
    __tablename__ = "cancellation"

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False)  
    payment_id: int = sa.Column(sa.Integer, sa.ForeignKey('payment.id'), nullable=False)  
    reason: str = sa.Column(sa.String(255), nullable=False)  
    cancelled_by: str = sa.Column(sa.String(255), nullable=False)  
    cancellation_date: datetime = sa.Column(sa.DateTime, nullable=False, default=sa.func.now())  
    status: str = sa.Column(sa.String(50), nullable=False, default='pending')  
    refund_amount: sa.Numeric = sa.Column(sa.Numeric(10, 2), nullable=True)  
    created_at: datetime = sa.Column(sa.DateTime, nullable=False, default=sa.func.now())  
    updated_at: datetime = sa.Column(sa.DateTime, nullable=True, default=sa.func.now(), onupdate=sa.func.now())  


    payment = sa.orm.relationship("Payment", backref="cancellations")
