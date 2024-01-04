import fastapi as fastapi
from fastapi.openapi.utils import get_openapi

from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import User

import services as services

app = fastapi.FastAPI()

openapi_schema = get_openapi(
    title="Testing!",
    version="0.1.0",
    routes=app.routes
)

@app.get("/api")
async def root():
    return {"message": "server is UP!"}

@app.post("/api/user", response_model=User)
async def create_user(
    user: User,
    db: Session = fastapi.Depends(services.get_db)
):
    user = await services.create_user(user, db)
    return user

@app.get("/api/user/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db: Session = fastapi.Depends(services.get_db)):
    user = await services.get_user_by_id(user_id, db)
    return user

@app.get("/api/users", response_model=User)
async def get_user_by_name(user_name: str | None = None, db: Session = fastapi.Depends(services.get_db)):
    print(user_name)
    user = await services.get_user_by_name(user_name, db)
    return user

@app.delete("/api/user/{user_id}", response_model=User)
async def delete_user_by_id(user_id: int, db: Session = fastapi.Depends(services.get_db)):
    user = await services.delete_user_by_id(user_id, db)
    return user

@app.delete("/api/users", response_model=User)
async def delete_user_by_name(user_name: str | None = None, db: Session = fastapi.Depends(services.get_db)):
    print(user_name)
    user = await services.delete_user_by_name(user_name, db)
    return user

