import pydantic as pydantic


class _UserBase(pydantic.BaseModel):
    name: str


class UserCreate(_UserBase):
    class Config:
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True
