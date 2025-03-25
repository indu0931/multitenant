from app.connectors.database_connector import Base
import sqlalchemy as sa
from datetime import datetime


class Payment(Base):
    __tablename__ = "payment"

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False)  
    amount: sa.Numeric = sa.Column(sa.Numeric(10, 2), nullable=False)
    bank_id: int = sa.Column(sa.Integer, nullable=False)  
    date: datetime = sa.Column(sa.DateTime, nullable=True)  
    method: str = sa.Column(sa.String(500), nullable=True)  
    access_key: str = sa.Column(sa.String(500), nullable=True)  
    created_at: datetime = sa.Column(sa.DateTime, nullable=False, default=sa.func.now())
    is_active: bool = sa.Column(sa.Boolean, nullable=False, default=True)
