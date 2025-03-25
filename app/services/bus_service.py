from sqlalchemy.orm import Session
from app.connectors.database_connector import Base
import sqlalchemy as sa
from app.models import bus  

def create_bus(db: Session, bus_create: BusCreateRequest):
    db_bus = bus(
        bus_type=bus_create.bus_type,
        description=bus_create.description,
        is_active=bus_create.is_active
    )
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus

def get_bus(db: Session, bus_id: int):
    return db.query(bus).filter(bus.id == bus_id).first()


def get_buses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(bus).offset(skip).limit(limit).all()

def update_bus(db: Session, bus_id: int, bus_update: BusCreateRequest):
    db_bus = db.query(bus).filter(bus.id == bus_id).first()
    if db_bus:
        db_bus.bus_type = bus_update.bus_type
        db_bus.description = bus_update.description
        db_bus.is_active = bus_update.is_active
        db.commit()
        db.refresh(db_bus)
        return db_bus
    return None

def delete_bus(db: Session, bus_id: int):
    db_bus = db.query(bus).filter(bus.id == bus_id).first()
    if db_bus:
        db.delete(db_bus)
        db.commit()
        return db_bus
    return None
