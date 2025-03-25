from sqlalchemy.orm import Session
from app.models.cancellation import Cancellation
from app.schemas.cancellation import CancellationCreateRequest, CancellationResponse
from app.models.payment import Payment  
from sqlalchemy.exc import IntegrityError

def create_cancellation(db: Session, cancellation_create: CancellationCreateRequest) -> CancellationResponse:
    payment = db.query(Payment).filter(Payment.id == cancellation_create.payment_id).first()
    if not payment:
        raise ValueError("Payment not found")

    db_cancellation = Cancellation(
        payment_id=cancellation_create.payment_id,
        reason=cancellation_create.reason,
        cancelled_by=cancellation_create.cancelled_by,
        refund_amount=cancellation_create.refund_amount,
        status=cancellation_create.status
    )

    db.add(db_cancellation)
    db.commit()
    db.refresh(db_cancellation)

    return CancellationResponse.from_orm(db_cancellation)

def get_cancellation(db: Session, cancellation_id: int) -> CancellationResponse:
    db_cancellation = db.query(Cancellation).filter(Cancellation.id == cancellation_id).first()
    if db_cancellation:
        return CancellationResponse.from_orm(db_cancellation)
    return None

def get_cancellations(db: Session, skip: int = 0, limit: int = 100) -> list[CancellationResponse]:
    db_cancellations = db.query(Cancellation).offset(skip).limit(limit).all()
    return [CancellationResponse.from_orm(db_cancellation) for db_cancellation in db_cancellations]

def update_cancellation(db: Session, cancellation_id: int, cancellation_update: CancellationCreateRequest) -> CancellationResponse:
    db_cancellation = db.query(Cancellation).filter(Cancellation.id == cancellation_id).first()
    if db_cancellation:
        db_cancellation.reason = cancellation_update.reason
        db_cancellation.cancelled_by = cancellation_update.cancelled_by
        db_cancellation.status = cancellation_update.status
        db_cancellation.refund_amount = cancellation_update.refund_amount

        db.commit()
        db.refresh(db_cancellation)
        return CancellationResponse.from_orm(db_cancellation)

    return None

def delete_cancellation(db: Session, cancellation_id: int) -> bool:
    db_cancellation = db.query(Cancellation).filter(Cancellation.id == cancellation_id).first()
    if db_cancellation:
        db.delete(db_cancellation)
        db.commit()
        return True
    return False
