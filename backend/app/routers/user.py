from fastapi import APIRouter, Depends, HTTPException, security
from sqlmodel import Session
import app.services as services
from ..models import Book, BookView, FavoriteBookLink, User, UserCreate

router = APIRouter(
    tags=["user"],
)


@router.post("/api/user", response_model=User)
async def create_user(
    user: UserCreate,
    db: Session = Depends(services.get_db)
) -> User:
    user = await services.create_user(user, db)
    return user


@router.get("/api/user/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db: Session = Depends(services.get_db)) -> User | None:
    user = await services.get_user_by_id(user_id, db)
    return user


@router.get("/api/users", response_model=User)
async def get_user_by_name(user_name: str | None = None, db: Session = Depends(services.get_db)) -> User | None:
    print(user_name)
    user = await services.get_user_by_name(user_name, db)
    return user


@router.delete("/api/user/{user_id}", response_model=User)
async def delete_user_by_id(user_id: int, db: Session = Depends(services.get_db)) -> User | None:
    user = await services.delete_user_by_id(user_id, db)
    return user


@router.delete("/api/users", response_model=User)
async def delete_user_by_name(user_name: str | None = None, db: Session = Depends(services.get_db)) -> User | None:
    print(user_name)
    user = await services.delete_user_by_name(user_name, db)
    return user


@router.get("/api/users/me")
async def get_current_user(user: User = Depends(services.get_current_user)) -> User | None:
    return user


@router.put("/api/user/{user_id}", response_model=User)
async def update_user_by_id(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(services.get_db)
) -> User:
    user = await services.update_user_by_id(user_id, user, db)
    return user


@router.post("/api/get-token")
async def generate_token(
    form_data: security.OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(services.get_db)
) -> services.Token:
    user = await services.authentificate_user(form_data.username, form_data.password, db)
    if user is None:
        raise HTTPException(
            status_code=401, detail="Invalid username or password")

    return await services.create_token(user)

@router.get("/api/users/add-favorite")
async def add_favorite_book(book_id: int, user: User = Depends(services.get_current_user),
                            db: Session = Depends(services.get_db)) -> FavoriteBookLink:
    return await services.add_favorite_book(book_id, user, db)

@router.get("/api/users/remove-favorite")
async def remove_favorite_book(book_id: int, user: User = Depends(services.get_current_user),
                            db: Session = Depends(services.get_db)) -> FavoriteBookLink:
    return await services.remove_favorite_book(book_id, user, db)

@router.get("/api/users/get-favorites")
async def get_favorite_books(user: User = Depends(services.get_current_user),
                            db: Session = Depends(services.get_db)) -> list[BookView]:
    return await services.get_favorite_books(user, db)
