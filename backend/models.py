from sqlmodel import Field, SQLModel, create_engine, select
import database as database

class UserBase(SQLModel):
    __tablename__ = "users"
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    # reviews = orm.relationship("Review", back_populates="owner")

class User(UserBase, table=True):
    id: int | None = Field(primary_key=True, index=True)

class UserCreate(UserBase):
    pass

# class Review(database.Base):
#     __tablename__ = "reviews"
#     id = sql.Column(sql.Integer, primary_key=True, index=True, autoincrement=True)
#     content = sql.Column(sql.String)
#     owner_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
#     owner = orm.relationship("User", back_populates="reviews")