from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service import ServiceCreateRequest, ServiceResponse
from sqlalchemy.exc import IntegrityError

def create_service(db: Session, service_create: ServiceCreateRequest) -> ServiceResponse:
    db_service = Service(
        name=service_create.name,
        description=service_create.description,
        price=service_create.price,
        location_id=service_create.location_id
    )

    db.add(db_service)
    db.commit()
    db.refresh(db_service)

    return ServiceResponse.from_orm(db_service)

def get_service(db: Session, service_id: int) -> ServiceResponse:
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if db_service:
        return ServiceResponse.from_orm(db_service)
    return None

def get_services(db: Session, skip: int = 0, limit: int = 100) -> list[ServiceResponse]:
    db_services = db.query(Service).offset(skip).limit(limit).all()
    return [ServiceResponse.from_orm(db_service) for db_service in db_services]

def update_service(db: Session, service_id: int, service_update: ServiceCreateRequest) -> ServiceResponse:
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if db_service:
        db_service.name = service_update.name
        db_service.description = service_update.description
        db_service.price = service_update.price
        db_service.location_id = service_update.location_id

        db.commit()
        db.refresh(db_service)
        return ServiceResponse.from_orm(db_service)

    return None

def delete_service(db: Session, service_id: int) -> bool:
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if db_service:
        db.delete(db_service)
        db.commit()
        return True
    return False
