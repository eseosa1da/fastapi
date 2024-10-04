from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(UserBase):
    password: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: User

    class Config:
        from_attributes = True

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True