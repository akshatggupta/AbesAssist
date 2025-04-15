from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)  # "senior" or "junior"
    application_id = Column(String)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    category = Column(String)
    image_url = Column(String)
    uploaded_by = Column(Integer, ForeignKey("users.id"))

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    requested_by = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer)
    receiver_id = Column(Integer)
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
