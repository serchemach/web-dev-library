import os
from sqlmodel import Session
import app.database
from app.models import Book

i = 0
for file in os.listdir("./uploads/"):
    i += 1
    file_path = f"uploads/{file}"
    preview_path = f"uploads/previews/{file}"[:-4] + ".jpeg"

    if not os.path.isfile(file_path):
        continue

    with Session(app.database.engine) as db:
        book = Book(
            name=f"Book{i}",
            description="",
            file_path=file_path,
            preview_path=preview_path,
        )
        db.add(book)
        db.commit()
