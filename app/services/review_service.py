from sqlalchemy.orm import Session
from app.models.review import Review
from app.schemas.review import ReviewCreateRequest, ReviewResponse
from sqlalchemy.exc import IntegrityError

def create_review(db: Session, review_create: ReviewCreateRequest) -> ReviewResponse:
    db_review = Review(
        booking_id=review_create.booking_id,
        user_id=review_create.user_id,
        rating=review_create.rating,
        review_text=review_create.review_text
    )

    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    return ReviewResponse.from_orm(db_review)

def get_review(db: Session, review_id: int) -> ReviewResponse:
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if db_review:
        return ReviewResponse.from_orm(db_review)
    return None

def get_reviews_for_booking(db: Session, booking_id: int, skip: int = 0, limit: int = 100) -> list[ReviewResponse]:
    db_reviews = db.query(Review).filter(Review.booking_id == booking_id).offset(skip).limit(limit).all()
    return [ReviewResponse.from_orm(db_review) for db_review in db_reviews]

def update_review(db: Session, review_id: int, review_update: ReviewCreateRequest) -> ReviewResponse:
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if db_review:
        db_review.rating = review_update.rating
        db_review.review_text = review_update.review_text

        db.commit()
        db.refresh(db_review)
        return ReviewResponse.from_orm(db_review)

    return None

def delete_review(db: Session, review_id: int) -> bool:
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if db_review:
        db.delete(db_review)
        db.commit()
        return True
    return False
