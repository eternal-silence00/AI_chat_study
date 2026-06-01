from redis import Redis
import os
import json

class RedisService:
    def __init__(self):
        self.redis_client = Redis.from_url(os.getenv("REDIS_URL"), decode_responses = True)
        
    def get_history(self, session_id: str) -> list:
        history = self.redis_client.get(session_id)
        if not history:
            return []
        return json.loads(history)
    
    def add_message(self, session_id: str, role: str, content: str):
        history = self.get_history(session_id)
        history.append({"role":role, "content": content})
        self.redis_client.set(session_id, json.dumps(history), ex=3600)
        return 