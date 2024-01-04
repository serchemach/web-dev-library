from msilib import schema
import sqlalchemy.orm as orm

import database as database, models as models, schemas as schemas

def create_database():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_user(user: schemas.UserCreate, db: orm.Session):
    user_obj = models.User(
        username = user.username,
        email = user.email
    )

    db.add(user_obj)
    db.commit()

    return user_obj

async def get_user_by_id(user_id: int, db: orm.Session):
    return db.query(models.User).filter(models.User.id == user_id).first()

async def get_user_by_name(user_name: str, db: orm.Session):
    return db.query(models.User).filter(models.User.username.contains(user_name)).first()

async def delete_user_by_id(user_id: int, db: orm.Session):
    user =  db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user

async def delete_user_by_name(user_name: str, db: orm.Session):
    user =  db.query(models.User).filter(models.User.username == user_name).first()
    db.delete(user)
    db.commit()
    return user
