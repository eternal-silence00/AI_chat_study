from fastapi import FastAPI
from app.routers import message
from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()

app.include_router(message.router)