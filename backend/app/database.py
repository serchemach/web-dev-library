from sqlmodel import Field, Session, SQLModel, create_engine, select
from backend.app.config import DB_HOST

connection_string = f"mysql+mysqlconnector://root:12345@{DB_HOST}:3306/myapp"
engine = create_engine(connection_string, echo=True)
