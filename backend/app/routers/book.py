from genericpath import isfile
import os
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlmodel import Session
import app.services as services
from ..models import Book, BookBase, BookCreate, BookView, BookViewReview, User
import secrets
import pypdfium2 as pdfium

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

    stored_filename = secrets.token_urlsafe(16) + ".pdf"
    file_path = f"uploads/{stored_filename}"
    while os.path.isfile(file_path):
        stored_filename = secrets.token_urlsafe(16) + ".pdf"
        file_path = f"uploads/{stored_filename}"

    with open(file_path, "wb") as file_obj:
        file_obj.write(file.file.read())

    # Save the preview
    pdf = pdfium.PdfDocument(file_path)
    preview_path = f"uploads/previews/{stored_filename}"[:-4] + ".jpeg"
    image = pdf[0].render(scale=4).to_pil()
    if not os.path.exists("uploads/previews"):
        os.makedirs("uploads/previews")
    image.save(preview_path)

    book_obj = await services.create_book(BookCreate(
        name = name,
        description = description,
        file_path = file_path,
        preview_path = preview_path,
    ), db)
    return book_obj


@router.get("/api/get-book/{id}")
async def get_book_by_id(id: int, db: Session = Depends(services.get_db)) -> Book | None:
    book = await services.get_book_by_id(id, db)
    return book

@router.get("/api/get-book-full/{id}")
async def get_book_by_id_with_favorite_and_reviews(id: int, db: Session = Depends(services.get_db),
                                       user: User = Depends(services.get_current_user)) -> BookViewReview:
    book = await services.get_book_by_id_with_favorite_and_reviews(id, db, user)
    return book

@router.get("/api/get-books")
async def get_books(offset: int, limit: int, db: Session = Depends(services.get_db), 
                    user: User = Depends(services.get_current_user)) -> list[BookView]:
    return await services.get_books_for_user(offset, limit, db, user)

PATH_BASE = "./uploads/"

@router.get("/api/files/{file_path:path}")
async def read_file(file_path: str):
    print(file_path)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="No SUCH FILE")

    return FileResponse(file_path)