# database/schemas.py

from typing import Optional
from pydantic import BaseModel

from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        from_attributes = True

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_complete: Optional[bool] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_complete: Optional[bool] = None

    class Config:
        from_attributes = True
        
class Task(TaskBase):
    id: int
    is_complete: bool = False

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
