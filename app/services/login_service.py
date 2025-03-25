from sqlalchemy.orm import Session
from app.models.admin import Admin
from app.schemas.admin import AdminCreateRequest, AdminResponse
from sqlalchemy.exc import IntegrityError

def create_admin(db: Session, admin_create: AdminCreateRequest) -> AdminResponse:
    db_admin = db.query(Admin).filter(Admin.username == admin_create.username).first()
    if db_admin:
        raise ValueError("Username already taken")

    db_admin = Admin(
        role_id=admin_create.role_id,
        username=admin_create.username,
        password=admin_create.password,  
        is_active=admin_create.is_active
    )

    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)

    return AdminResponse.from_orm(db_admin)

def get_admin(db: Session, admin_id: int) -> AdminResponse:
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin:
        return AdminResponse.from_orm(db_admin)
    return None

def get_admins(db: Session, skip: int = 0, limit: int = 100) -> list[AdminResponse]:
    db_admins = db.query(Admin).offset(skip).limit(limit).all()
    return [AdminResponse.from_orm(db_admin) for db_admin in db_admins]

def update_admin(db: Session, admin_id: int, admin_update: AdminCreateRequest) -> AdminResponse:
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin:
        db_admin.role_id = admin_update.role_id
        db_admin.username = admin_update.username
        db_admin.password = admin_update.password  
        db_admin.is_active = admin_update.is_active

        db.commit()
        db.refresh(db_admin)
        return AdminResponse.from_orm(db_admin)

    return None

def delete_admin(db: Session, admin_id: int) -> bool:
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin:
        db_admin.is_active = False  
        db.commit()
        return True
    return False
