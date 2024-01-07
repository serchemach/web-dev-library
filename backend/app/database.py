from sqlmodel import Field, Session, SQLModel, create_engine, select

connection_string = "mysql+mysqlconnector://root:12345@127.0.0.1:3306/myapp"
engine = create_engine(connection_string, echo=True)
