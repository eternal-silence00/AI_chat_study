from pydantic import BaseModel, ConfigDict

class MessageCreate(BaseModel):
    session_id: str
    message: str
    
class MessageResponse(BaseModel):
    message: str
    
    model_config = ConfigDict(from_attributes=True)
    