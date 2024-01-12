from os import link
from pyexpat import model
from fastapi import HTTPException, security
import fastapi
from sqlalchemy import true
from sqlmodel import SQLModel, Session, select
import app.database as database, app.models as models
import passlib.hash as hash
import jwt
JWT_SECRET = "my-secret"

def get_db():
    with Session(database.engine) as session:
        yield session

async def create_user(user: models.UserCreate, db: Session):

    user_obj = models.User(
        username = user.username,
        email = user.email,
        pass_hash = hash.bcrypt.hash(user.password)
    )

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj

async def get_user_by_id(user_id: int, db: Session):
    return db.exec(select(models.User).where(models.User.id == user_id)).first()

async def get_user_by_name(user_name: str, db: Session):
    return db.exec(select(models.User).where(models.User.username == user_name)).first()

async def delete_user_by_id(user_id: int, db: Session):
    user =  db.exec(select(models.User).where(models.User.id == user_id)).first()
    if user is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"User with id={user_id} doesn't exist")
    
    db.delete(user)
    db.commit()
    return user

async def delete_user_by_name(user_name: str, db: Session):
    user = db.exec(select(models.User).where(models.User.username == user_name)).first()
    if user is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"User with username={user_name} doesn't exist")
    
    db.delete(user)
    db.commit()

    return user

async def update_user_by_id(user_id: int, user: models.UserCreate, db: Session):
    user_obj = await get_user_by_id(user_id, db)
    if user_obj is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"User with id={user_id} doesn't exist")
    
    user_obj.username = user.username
    user_obj.email = user.email

    db.commit()
    db.refresh(user_obj)

    return user_obj

async def authentificate_user(username: str, password: str, db: Session):
    user = await get_user_by_name(username, db)

    if user is None or not user.verify_password(password):
        return None

    return user

oauth2schema = security.OAuth2PasswordBearer(tokenUrl="/api/get-token")

async def get_current_user(
    db: Session = fastapi.Depends(get_db),
    token: str = fastapi.Depends(oauth2schema)
):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = await get_user_by_id(payload["id"], db)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid token")

    return user

async def create_review(review: models.ReviewCreate, db: Session):
    user_obj = await get_user_by_id(review.owner_id, db)
    if user_obj is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"User with id={review.owner_id} doesn't exist")
    
    review_obj = models.Review(
        content = review.content,
        owner_id = review.owner_id
    )

    db.add(review_obj)
    db.commit()
    db.refresh(review_obj)

    return review_obj


class Token(SQLModel):
    access_token: str
    token_type: str

async def create_token(user: models.User):
    token = jwt.encode({
        "name": user.username,
        "id": user.id,
        "email": user.email
    }, JWT_SECRET, algorithm="HS256")
    return Token(access_token=token, token_type="Bearer")


async def create_book(book: models.BookCreate, db: Session):
    book_obj = models.Book(
        name = book.name,
        description = book.description,
        file_path = book.file_path,
    )

    db.add(book_obj)
    db.commit()
    db.refresh(book_obj)
    db.close()

    return book_obj

async def get_book_by_id(book_id: int, db: Session):
    return db.exec(select(models.Book).where(models.Book.id == book_id)).first()

async def get_books_for_user(offset: int, limit: int, db: Session, user: models.User):
    favorite_books = user.favorite_books
    books_to_show = db.exec(select(models.Book).offset(offset).limit(limit))

    return map(lambda x: models.BookView(
        name=x.name, 
        description=x.description,
        id=x.id,
        file_path=x.file_path,
        isFavorite=x in favorite_books
        ), books_to_show)

async def add_favorite_book(book_id: int, user: models.User, db: Session):
    link_obj = models.FavoriteBookLink(
        book_id=book_id,
        user_id=user.id
    )

    db.add(link_obj)
    db.commit()
    db.refresh(link_obj)
    return link_obj

async def remove_favorite_book(book_id: int, user: models.User, db: Session):
    link_obj = db.exec(select(models.FavoriteBookLink).where(models.FavoriteBookLink.book_id == book_id and 
                                                             models.FavoriteBookLink.user_id == user.id)).first()

    db.delete(link_obj)
    db.commit()
    
    return link_obj

async def get_favorite_books(user: models.User, db: Session):
    return map(lambda x: models.BookView(
        name=x.name, 
        description=x.description,
        id=x.id,
        file_path=x.file_path,
        isFavorite=True
        ), user.favorite_books)

async def get_book_by_id_with_favorite_and_reviews(book_id: int, db: Session, user: models.User):
    book = db.exec(select(models.Book).where(models.Book.id == book_id)).first()

    return models.BookViewReview(
            name=book.name, 
            description=book.description,
            id=book.id,
            file_path=book.file_path,
            isFavorite=book in user.favorite_books,
            reviews=book.reviews
        )

async def get_reviews_by_book_id(book_id: int, db: Session, user: models.User):
    book = db.exec(select(models.Book).where(models.Book.id == book_id)).first()

    return book.reviews