from sqlmodel import Session, select
import database as database, models as models


def get_db():
    with Session(database.engine) as session:
        yield session

async def create_user(user: models.UserCreate, db: Session):
    user_obj = models.User(
        username = user.username,
        email = user.email
    )

    db.add(user_obj)
    db.commit()

    return user_obj

async def get_user_by_id(user_id: int, db: Session):
    return db.exec(select(models.User).where(models.User.id == user_id)).first()

async def get_user_by_name(user_name: str, db: Session):
    return db.exec(select(models.User).where(models.User.username == user_name)).first()

async def delete_user_by_id(user_id: int, db: Session):
    user =  db.exec(select(models.User).where(models.User.id == user_id)).first()
    db.delete(user)
    db.commit()
    return user

async def delete_user_by_name(user_name: str, db: Session):
    user = db.exec(select(models.User).where(models.User.username == user_name)).first()
    db.delete(user)
    db.commit()
    return user
