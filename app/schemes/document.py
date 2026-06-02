from pydantic import BaseModel, ConfigDict

class DocumentCreate(BaseModel):
    content: str
    
class DocumentResponse(BaseModel):
    content: str
    
    model_config = ConfigDict(from_attributes=True)