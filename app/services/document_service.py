from app.repositories.DocumentRepo import DocumentRepo
from app.services.embedding_service import EmbeddingService
from sqlalchemy.ext.asyncio import AsyncSession

class DocumentService:
        
    async def add_document(
        self,
        session: AsyncSession,
        content: str
    ):
        DocRepo = DocumentRepo(session)
        embedding = EmbeddingService().get_embedding(content)
        result = await DocRepo.add_document(content, embedding)
        return result 
    
    async def find_simular(
        self,
        session: AsyncSession,
        query: str,
        limit: int
    ):
        DocRepo = DocumentRepo(session)
        embedding = EmbeddingService().get_embedding(query)
        result = await DocRepo.find_simular(embedding, limit)
        return result