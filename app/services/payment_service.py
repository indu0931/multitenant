from sqlalchemy.orm import Session
from app.models.payment import Payment
from app.schemas.payment import PaymentCreateRequest, PaymentResponse
from sqlalchemy.exc import IntegrityError

def create_payment(db: Session, payment_create: PaymentCreateRequest) -> PaymentResponse:
    db_payment = Payment(
        amount=payment_create.amount,
        bank_id=payment_create.bank_id,
        date=payment_create.date,
        method=payment_create.method,
        access_key=payment_create.access_key,
        is_active=payment_create.is_active
    )

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    return PaymentResponse.from_orm(db_payment)

def get_payment(db: Session, payment_id: int) -> PaymentResponse:
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment:
        return PaymentResponse.from_orm(db_payment)
    return None

def get_payments(db: Session, skip: int = 0, limit: int = 100) -> list[PaymentResponse]:
    db_payments = db.query(Payment).offset(skip).limit(limit).all()
    return [PaymentResponse.from_orm(db_payment) for db_payment in db_payments]

def update_payment(db: Session, payment_id: int, payment_update: PaymentCreateRequest) -> PaymentResponse:
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment:
        db_payment.amount = payment_update.amount
        db_payment.bank_id = payment_update.bank_id
        db_payment.date = payment_update.date
        db_payment.method = payment_update.method
        db_payment.access_key = payment_update.access_key
        db_payment.is_active = payment_update.is_active

        db.commit()
        db.refresh(db_payment)
        return PaymentResponse.from_orm(db_payment)

    return None

def delete_payment(db: Session, payment_id: int) -> bool:
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment:
        db_payment.is_active = False  
        db.commit()
        return True
    return False
