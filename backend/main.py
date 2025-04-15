from fastapi import FastAPI
from database import Base, engine
from routers import auth, items, requests, chat
import streamlit as st

app = FastAPI(title="College Help Project")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(items.router)
app.include_router(requests.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Welcome to College Help API"}
