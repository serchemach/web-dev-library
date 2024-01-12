from sqlalchemy import table
from sqlmodel import Field, SQLModel, Relationship
import passlib.hash as hash

class FavoriteBookLink(SQLModel, table=True):
    __tablename__ = "user_book_link"
    user_id: int | None = Field(
        default=None, foreign_key="users.id", primary_key=True
    )
    book_id: int | None = Field(
        default=None, foreign_key="books.id", primary_key=True
    )

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)

class User(UserBase, table=True):
    __tablename__ = "users"
    id: int | None = Field(primary_key=True, index=True)
    pass_hash: str

    reviews: list['Review'] = Relationship(back_populates="owner")
    favorite_books: list['Book'] = Relationship(back_populates="favorited_users", link_model=FavoriteBookLink)

    def verify_password(self, password: str) -> bool:
        return hash.bcrypt.verify(password, self.pass_hash)

class UserCreate(UserBase):
    password: str
    pass

class ReviewBase(SQLModel):
    content: str
    owner_id: int = Field(default=None, foreign_key="users.id")
    book_id: int = Field(default=None, foreign_key="books.id")

class Review(ReviewBase, table=True):
    __tablename__ = "reviews"
    id: int | None = Field(primary_key=True, index=True)
    owner: User = Relationship(back_populates='reviews')
    book: 'Book' = Relationship(back_populates='reviews')

class ReviewCreate(ReviewBase):
    pass

class BookBase(SQLModel):
    name: str = Field(index=True)
    description: str

class BookCreate(BookBase):
    file_path: str
    pass

class Book(BookCreate, table=True):
    __tablename__ = "books"
    id: int | None = Field(primary_key=True, index=True)
    favorited_users: list['User'] = Relationship(back_populates="favorite_books", link_model=FavoriteBookLink)
    reviews: list[Review] = Relationship(back_populates="book")

class BookView(BookCreate):
    id: int
    isFavorite: bool

class BookViewReview(BookView):
    reviews: list[Review]
