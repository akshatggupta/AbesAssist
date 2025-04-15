from fastapi import APIRouter, Depends
from schemas import RequestCreate
from models import Request
from database import SessionLocal

router = APIRouter(prefix="/requests", tags=["Requests"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/make")
def make_request(req: RequestCreate, user_id: int, db: Session = Depends(get_db)):
    new_req = Request(item_id=req.item_id, requested_by=user_id)
    db.add(new_req)
    db.commit()
    return {"message": "Request sent"}
