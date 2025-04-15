from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import ItemCreate
from models import Item
from database import SessionLocal

router = APIRouter(prefix="/items", tags=["Items"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload/{user_id}")
def upload_item(user_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    new_item = Item(**item.dict(), uploaded_by=user_id)
    db.add(new_item)
    db.commit()
    return {"message": "Item uploaded"}

@router.get("/")
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
