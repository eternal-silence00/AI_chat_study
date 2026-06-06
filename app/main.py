from fastapi import FastAPI
from app.routers import message, document, storage
from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()

app.include_router(message.router)
app.include_router(document.router)
app.include_router(storage.router)