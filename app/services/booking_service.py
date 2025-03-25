from sqlalchemy.orm import Session
from app.models.booking import Booking
from app.models.user import User
from app.models.service import Service
from app.schemas.booking import BookingCreateRequest, BookingResponse
from sqlalchemy.exc import IntegrityError

def create_booking(db: Session, booking_create: BookingCreateRequest) -> BookingResponse:
    user = db.query(User).filter(User.id == booking_create.user_id).first()
    if not user:
        raise ValueError("User not found")
    
    service = db.query(Service).filter(Service.id == booking_create.service_id).first()
    if not service:
        raise ValueError("Service not found")

    db_booking = Booking(
        user_id=booking_create.user_id,
        service_id=booking_create.service_id,
        start_date=booking_create.start_date,
        end_date=booking_create.end_date,
        total_amount=booking_create.total_amount,
        payment_status=booking_create.payment_status,
        status=booking_create.status
    )
    
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    
    return BookingResponse.from_orm(db_booking)

def get_booking(db: Session, booking_id: int) -> BookingResponse:
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if db_booking:
        return BookingResponse.from_orm(db_booking)
    return None

def get_bookings(db: Session, skip: int = 0, limit: int = 100) -> list[BookingResponse]:
    db_bookings = db.query(Booking).offset(skip).limit(limit).all()
    return [BookingResponse.from_orm(db_booking) for db_booking in db_bookings]

def update_booking(db: Session, booking_id: int, booking_update: BookingCreateRequest) -> BookingResponse:
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if db_booking:
        db_booking.start_date = booking_update.start_date
        db_booking.end_date = booking_update.end_date
        db_booking.total_amount = booking_update.total_amount
        db_booking.payment_status = booking_update.payment_status
        db_booking.status = booking_update.status
        
        db.commit()
        db.refresh(db_booking)
        return BookingResponse.from_orm(db_booking)
    
    return None

def delete_booking(db: Session, booking_id: int) -> bool:
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
        return True
    return False
