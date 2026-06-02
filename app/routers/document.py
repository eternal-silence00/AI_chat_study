from fastapi import APIRouter, Depends, HTTPException
from app.services.document_service import DocumentService
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemes.document import DocumentCreate, DocumentResponse

router = APIRouter()

@router.post("/document", response_model=DocumentResponse, status_code=201)
async def add_document(
    data: DocumentCreate,
    session: AsyncSession = Depends(get_db)
):
    service = DocumentService()
    document = await service.add_document(session, data.content)
    return document

@router.get("/document/search", response_model=list[DocumentResponse])
async def find_simular(
    query: str,
    limit: int,
    session: AsyncSession = Depends(get_db)
):
    service = DocumentService()
    result = await service.find_simular(session, query, limit)
    if not result:
        raise HTTPException(status_code=404, detail="Nothing was found")
    return result