from app.connectors.database_connector import Base
import sqlalchemy as sa
from datetime import datetime

class Service(Base):
    __tablename__ = "services"

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False)
    name: str = sa.Column(sa.String(255), nullable=False)  
    description: str = sa.Column(sa.String(1000), nullable=True)  
    price: sa.Numeric = sa.Column(sa.Numeric(10, 2), nullable=False)  
    location_id: int = sa.Column(sa.Integer, sa.ForeignKey('location.id'), nullable=False) 
    created_at: datetime = sa.Column(sa.DateTime, nullable=False, default=sa.func.now())  
    updated_at: datetime = sa.Column(sa.DateTime, nullable=True, default=sa.func.now(), onupdate=sa.func.now())   

    
    location = sa.orm.relationship("Location", backref="services")
