from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str
    application_id: str

class UserLogin(BaseModel):
    email: str
    password: str

class ItemCreate(BaseModel):
    title: str
    description: str
    category: str
    image_url: Optional[str]

class RequestCreate(BaseModel):
    item_id: int

class MessageCreate(BaseModel):
    receiver_id: int
    message: str
