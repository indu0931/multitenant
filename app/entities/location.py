from app.connectors.database_connector import Base
import sqlalchemy as sa
from datetime import datetime

class Location(Base):
    __tablename__ = "location"

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False) 
    name: str = sa.Column(sa.String(255), nullable=False)  
    address: str = sa.Column(sa.String(500), nullable=True)  
    city: str = sa.Column(sa.String(100), nullable=True) 
    country: str = sa.Column(sa.String(100), nullable=True)  
    latitude: sa.Numeric = sa.Column(sa.Numeric(10, 8), nullable=True)  
    longitude: sa.Numeric = sa.Column(sa.Numeric(11, 8), nullable=True) 
    created_at: datetime = sa.Column(sa.DateTime, nullable=False, default=sa.func.now())  
    updated_at: datetime = sa.Column(sa.DateTime, nullable=True, default=sa.func.now(), onupdate=sa.func.now()) 
