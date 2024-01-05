import json
import os
import string
from typing_extensions import Annotated
import fastapi as fastapi
from fastapi import FastAPI, openapi
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse
from fastapi.routing import APIRoute
import fastapi.security as security
from fastapi.staticfiles import StaticFiles
from httpx import HTTPError

from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import Book, BookBase, BookCreate, Review, ReviewBase, ReviewCreate, User, UserCreate

import services as services

app = fastapi.FastAPI()

@app.get("/api")
async def root() -> str:
    return "server is UP!"


@app.post("/api/user", response_model=User)
async def create_user(
    user: UserCreate,
    db: Session = fastapi.Depends(services.get_db)
) -> User:
    user = await services.create_user(user, db)
    return user


@app.get("/api/user/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db: Session = fastapi.Depends(services.get_db)) -> User | None:
    user = await services.get_user_by_id(user_id, db)
    return user


@app.get("/api/users", response_model=User)
async def get_user_by_name(user_name: str | None = None, db: Session = fastapi.Depends(services.get_db)) -> User | None:
    print(user_name)
    user = await services.get_user_by_name(user_name, db)
    return user


@app.delete("/api/user/{user_id}", response_model=User)
async def delete_user_by_id(user_id: int, db: Session = fastapi.Depends(services.get_db)) -> User | None:
    user = await services.delete_user_by_id(user_id, db)
    return user


@app.delete("/api/users", response_model=User)
async def delete_user_by_name(user_name: str | None = None, db: Session = fastapi.Depends(services.get_db)) -> User | None:
    print(user_name)
    user = await services.delete_user_by_name(user_name, db)
    return user


@app.get("/api/users/me")
async def get_current_user(user: User = fastapi.Depends(services.get_current_user)) -> User | None:
    return user


@app.put("/api/user/{user_id}", response_model=User)
async def update_user_by_id(
    user_id: int,
    user: UserCreate,
    db: Session = fastapi.Depends(services.get_db)
) -> User:
    user = await services.update_user_by_id(user_id, user, db)
    return user


@app.post("/api/review", response_model=Review)
async def create_review(
    review: ReviewCreate,
    db: Session = fastapi.Depends(services.get_db),
    user: User = fastapi.Depends(services.get_current_user)
) -> Review:
    if user.id != review.owner_id:
        raise fastapi.HTTPException(
            status_code=401, detail="Can only add your own reviews")
    review_obj = await services.create_review(review, db)
    return review_obj


@app.post("/api/get-token")
async def generate_token(
    form_data: security.OAuth2PasswordRequestForm = fastapi.Depends(),
    db: Session = fastapi.Depends(services.get_db)
) -> services.Token:
    user = await services.authentificate_user(form_data.username, form_data.password, db)
    if user is None:
        raise fastapi.HTTPException(
            status_code=401, detail="Invalid username or password")

    return await services.create_token(user)


@app.post("/api/upload-book/")
async def upload_book(file: Annotated[fastapi.UploadFile, fastapi.File(description="A file read as UploadFile")], 
                      name: str, description: str, db: Session = fastapi.Depends(services.get_db)) -> Book:
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
async def get_book_by_id(id: int, db: Session = fastapi.Depends(services.get_db)) -> Book | None:
    book = await services.get_book_by_id(id, db)
    return book

@app.get("/api/files/")
async def read_file(file_path: str):
    if not os.path.exists(file_path):
        raise fastapi.HTTPException(status_code=404, detail="No SUCH FILE")

    return FileResponse(file_path)


def use_route_names_as_operation_ids(application: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in application.routes:
        if isinstance(route, APIRoute):
            route: APIRoute = route
            route.operation_id = route.name

use_route_names_as_operation_ids(app)

openapi_schema = get_openapi(
    title="Testing!",
    version="0.1.0",
    routes=app.routes
)

with open('openapi.json', 'w') as f:
    json.dump(openapi_schema, f)


app.mount("/assets", StaticFiles(directory="../frontend/dist/assets"), name="static")

# Simply the root will return our Svelte build
@app.get("/{cool:path}", response_class=FileResponse)
async def main(cool: str):
    return "../frontend/dist/index.html"
