import os
import pypdfium2 as pdfium
from sqlmodel import Session, select
from app.models import Book
from app.services import get_db
import app.database


if not os.path.exists("uploads/previews"):
    os.makedirs("uploads/previews")
print(os.listdir("./uploads/"))
for file in os.listdir("./uploads/"):
    file_path = f"uploads/{file}"

    if not os.path.isfile(file_path):
        continue

    pdf = pdfium.PdfDocument(file_path)
    preview_path = f"uploads/previews/{file}"[:-4] + ".jpeg"
    image = pdf[0].render(scale=4).to_pil()
    image.save(preview_path)

    with Session(app.database.engine) as db:
        book = db.exec(select(Book).where(Book.file_path == file_path)).first()
        if not book:
            continue

        book.preview_path = preview_path
        db.add(book)
        db.commit()
