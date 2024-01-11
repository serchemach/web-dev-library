import os
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlmodel import Session
import app.services as services
from ..models import Book, BookBase, BookCreate, BookView, User

router = APIRouter(
    tags=["book"],
)

@router.post("/api/upload-book/")
async def upload_book(file: Annotated[UploadFile, File(description="A file read as UploadFile")], 
                      name: str, description: str, db: Session = Depends(services.get_db)) -> Book:
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


@router.get("/api/get-book/{id}")
async def get_book_by_id(id: int, db: Session = Depends(services.get_db)) -> Book | None:
    book = await services.get_book_by_id(id, db)
    return book

@router.get("/api/get-books")
async def get_books(offset: int, limit: int, db: Session = Depends(services.get_db), 
                    user: User = Depends(services.get_current_user)) -> list[BookView]:
    return await services.get_books_for_user(offset, limit, db, user)

@router.get("/api/files/")
async def read_file(file_path: str):
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="No SUCH FILE")

    return FileResponse(file_path)