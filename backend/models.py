import sqlalchemy as sql
import database as database

class User(database.Base):
    __tablename__  = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    name = sql.Column(sql.String, index=True, unique=True)
