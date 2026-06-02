from fastapi import APIRouter, Depends
from app.schemes.message import MessageCreate, MessageResponse
from app.services.ai_service import AIService
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

router = APIRouter()

@router.post("/message", response_model=MessageResponse)
async def create_message(
    data: MessageCreate,
    session: AsyncSession = Depends(get_db),
    limit: int = 3
):
    chat = AIService()
    response = await chat.get_message(session, data.message, data.session_id, limit)
    return {"message": response}