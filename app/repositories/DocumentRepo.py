from app.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from app.models.document import Document

class DocumentRepo:
    
    def __init__(self, session: AsyncSession = Depends(get_db)):
        
        self.session = session
    
    async def add_document(self, content: str, embedding: list):
        document = Document(content=content, embedding=embedding)
        self.session.add(document)
        await self.session.flush()
        await self.session.refresh(document)
        return document
    
    async def find_simular(self, embedding: list, limit: int):
        embedding=str([float(x) for x in embedding])
        result = await self.session.execute(select(Document).
                                            order_by(text("embedding <-> CAST(:embedding AS vector)").bindparams(embedding=embedding))
                                            .limit(limit)
                                            )
        return result.scalars().all()