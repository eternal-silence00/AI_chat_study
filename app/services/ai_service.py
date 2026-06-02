from groq import Groq
from app.services.redis_service import RedisService
from app.services.document_service import DocumentService
import os
from sqlalchemy.ext.asyncio import AsyncSession

class AIService:
    
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.DocService = DocumentService()
        
    async def get_message(self, session: AsyncSession, message: str, session_id, limit: int) -> str:
        redis_client = RedisService()
        history = redis_client.get_history(session_id)
        history.append({'role': "user", "content": message})
        similar = await self.DocService.find_simular(session, message, limit)
        context = "\n".join([doc.content for doc in similar])
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": f"Отвечай только на основе этих документов:\n{context}"},
                *history
            ]
        )
        redis_client.add_message(session_id, "user", message)
        answer = response.choices[0].message.content
        redis_client.add_message(session_id, "assistant", answer)
        return answer
        