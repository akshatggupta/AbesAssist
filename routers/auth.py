from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserLogin
from utils.security import hash_password, verify_password
from database import SessionLocal

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered.")
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role,
        application_id=user.application_id
    )
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user.id, "role": user.role}
