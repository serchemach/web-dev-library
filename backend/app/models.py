from sqlmodel import Field, SQLModel, Relationship
import passlib.hash as hash

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)

class User(UserBase, table=True):
    __tablename__ = "users"
    id: int | None = Field(primary_key=True, index=True)
    reviews: list['Review'] = Relationship(back_populates="owner")
    pass_hash: str
    def verify_password(self, password: str) -> bool:
        return hash.bcrypt.verify(password, self.pass_hash)

class UserCreate(UserBase):
    password: str
    pass

class ReviewBase(SQLModel):
    content: str
    owner_id: int = Field(default=None, foreign_key="users.id")

class Review(ReviewBase, table=True):
    __tablename__ = "reviews"
    id: int | None = Field(primary_key=True, index=True)
    owner: User = Relationship(back_populates='reviews')

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

