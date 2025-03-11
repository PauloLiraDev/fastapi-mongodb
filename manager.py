from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    print(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]
    print("🟢 Conectado ao MongoDB!")
    yield  # Espera a aplicação rodar
    app.mongodb_client.close()
    print("🔴 Conexão encerrada com MongoDB.")