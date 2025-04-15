from fastapi import APIRouter, Depends
from models import Chat
from schemas import MessageCreate
from database import SessionLocal

router = APIRouter(prefix="/chat", tags=["Chat"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/send/{sender_id}")
def send_message(sender_id: int, msg: MessageCreate, db: Session = Depends(get_db)):
    chat = Chat(sender_id=sender_id, receiver_id=msg.receiver_id, message=msg.message)
    db.add(chat)
    db.commit()
    return {"message": "Message sent"}

@router.get("/messages/{user1}/{user2}")
def get_chat(user1: int, user2: int, db: Session = Depends(get_db)):
    messages = db.query(Chat).filter(
        ((Chat.sender_id == user1) & (Chat.receiver_id == user2)) |
        ((Chat.sender_id == user2) & (Chat.receiver_id == user1))
    ).order_by(Chat.timestamp).all()
    return messages
