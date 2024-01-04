import json
import os
from typing_extensions import Annotated
import fastapi as fastapi
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse
import fastapi.security as security
from httpx import HTTPError

from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import BookBase, BookCreate, Review, ReviewBase, ReviewCreate, User, UserCreate

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
    user: UserCreate,
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


@app.get("/api/users/me")
async def get_current_user(user: User = fastapi.Depends(services.get_current_user)):
    return user


@app.put("/api/user/{user_id}", response_model=User)
async def update_user_by_id(
    user_id: int,
    user: UserCreate,
    db: Session = fastapi.Depends(services.get_db)
):
    user = await services.update_user_by_id(user_id, user, db)
    return user


@app.post("/api/review", response_model=Review)
async def create_review(
    review: ReviewCreate,
    db: Session = fastapi.Depends(services.get_db),
    user: User = fastapi.Depends(services.get_current_user)
):
    if user.id != review.owner_id:
        raise fastapi.HTTPException(
            status_code=401, detail="Can only add your own reviews")
    review_obj = await services.create_review(review, db)
    return review_obj


@app.post("/api/get-token")
async def generate_token(
    form_data: security.OAuth2PasswordRequestForm = fastapi.Depends(),
    db: Session = fastapi.Depends(services.get_db)
):
    user = await services.authentificate_user(form_data.username, form_data.password, db)
    if user is None:
        raise fastapi.HTTPException(
            status_code=401, detail="Invalid username or password")

    return await services.create_token(user)


@app.post("/api/upload-book/")
async def upload_book(file: Annotated[fastapi.UploadFile, fastapi.File(description="A file read as UploadFile")], 
                      name: str, description: str, db: Session = fastapi.Depends(services.get_db)):
    if not file:
        return {
            "message": "No upload file sent"
        }

    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as file_obj:
        file_obj.write(file.file.read())

    book_obj = await services.create_book(BookCreate(
        name = name,
        description = description,
        file_path = file_path,
    ), db)
    return book_obj


@app.get("/api/get-book/{id}")
async def get_book_by_id(id: int, db: Session = fastapi.Depends(services.get_db)):
    book = await services.get_book_by_id(id, db)
    return book

@app.get("/api/files/")
async def read_file(file_path: str):
    if not os.path.exists(file_path):
        raise fastapi.HTTPException(status_code=404, detail="No SUCH FILE")

    return FileResponse(file_path)
