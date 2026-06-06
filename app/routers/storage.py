from fastapi import UploadFile, APIRouter, File
from app.services.storage_service import StorageService

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    storage = StorageService()
    result = storage.upload_file(file.file, file.filename)
    return result
    