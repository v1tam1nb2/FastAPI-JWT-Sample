from typing import Union
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
