from sqlalchemy.orm import Session
from app.models.location import Location
from app.schemas.location import LocationCreateRequest, LocationResponse
from sqlalchemy.exc import IntegrityError

def create_location(db: Session, location_create: LocationCreateRequest) -> LocationResponse:
    db_location = Location(
        name=location_create.name,
        address=location_create.address,
        city=location_create.city,
        country=location_create.country,
        latitude=location_create.latitude,
        longitude=location_create.longitude
    )
    
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    
    return LocationResponse.from_orm(db_location)

def get_location(db: Session, location_id: int) -> LocationResponse:
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location:
        return LocationResponse.from_orm(db_location)
    return None

def get_locations(db: Session, skip: int = 0, limit: int = 100) -> list[LocationResponse]:
    db_locations = db.query(Location).offset(skip).limit(limit).all()
    return [LocationResponse.from_orm(db_location) for db_location in db_locations]

def update_location(db: Session, location_id: int, location_update: LocationCreateRequest) -> LocationResponse:
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location:
        db_location.name = location_update.name
        db_location.address = location_update.address
        db_location.city = location_update.city
        db_location.country = location_update.country
        db_location.latitude = location_update.latitude
        db_location.longitude = location_update.longitude
        
        db.commit()
        db.refresh(db_location)
        return LocationResponse.from_orm(db_location)
    
    return None

def delete_location(db: Session, location_id: int) -> bool:
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location:
        db.delete(db_location)
        db.commit()
        return True
    return False
