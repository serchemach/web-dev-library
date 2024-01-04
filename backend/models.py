import sqlalchemy as sql
import sqlalchemy.orm as orm
import database as database

class User(database.Base):
    __tablename__  = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True, autoincrement=True)
    username = sql.Column(sql.String, index=True, unique=True)
    email = sql.Column(sql.String, index=True, unique=True)
    reviews = orm.relationship("Review", back_populates="owner")


class Review(database.Base):
    __tablename__ = "reviews"
    id = sql.Column(sql.Integer, primary_key=True, index=True, autoincrement=True)
    content = sql.Column(sql.String)
    owner_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    owner = orm.relationship("User", back_populates="reviews")