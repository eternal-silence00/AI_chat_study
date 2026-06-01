from fastapi import APIRouter
from app.schemes.message import MessageCreate, MessageResponse
from app.services.ai_service import AIService

router = APIRouter()

@router.post("/message", response_model=MessageResponse)
def create_message(
    data: MessageCreate
):
    chat = AIService()
    response = chat.get_message(data.message, data.session_id)
    return {"message": response}