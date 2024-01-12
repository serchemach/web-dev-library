from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
import app.services as services
from ..models import Review, ReviewCreate, User

router = APIRouter(
    tags=["review"],
)

@router.post("/api/review", response_model=Review)
async def create_review(
    review: ReviewCreate,
    db: Session = Depends(services.get_db),
    user: User = Depends(services.get_current_user)
) -> Review:
    if user.id != review.owner_id:
        raise HTTPException(
            status_code=401, detail="Can only add your own reviews")
    review_obj = await services.create_review(review, db)
    return review_obj

@router.get("/api/get-reviews-book-id")
async def get_reviews_by_book_id(book_id: int, db: Session = Depends(services.get_db), 
                    user: User = Depends(services.get_current_user)) -> list[Review]:
    return await services.get_reviews_by_book_id(book_id, db, user)

