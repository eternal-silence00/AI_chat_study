from groq import Groq
from app.services.redis_service import RedisService
import os

class AIService:
    
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
    def get_message(self, message: str, session_id) -> str:
        redis_client = RedisService()
        history = redis_client.get_history(session_id)
        history.append({'role': "user", "content": message})
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=history
        )
        redis_client.add_message(session_id, "user", message)
        answer = response.choices[0].message.content
        redis_client.add_message(session_id, "assistant", answer)
        return answer
        