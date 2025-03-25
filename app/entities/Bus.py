from app.connectors.database_connector import Base
import sqlalchemy as sa
from datetime import datetime

class bus(Base):
    __tablename__ = "buses"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False) 
    bus_type: str = sa.Column(sa.String(50), unique=True, nullable=False) 
    description: str = sa.Column(sa.Text, nullable=False) 
    created_at: datetime = sa.Column(sa.DateTime, nullable=False, default=sa.func.now()) 
    is_active: bool = sa.Column(sa.Boolean, nullable=False, default=True) 
