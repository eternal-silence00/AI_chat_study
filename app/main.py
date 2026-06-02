from fastapi import FastAPI
from app.routers import message, document
from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()

app.include_router(message.router)
app.include_router(document.router)