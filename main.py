# Dependências de terceiros
from fastapi import FastAPI
import uvicorn

# Dependências do projeto
from config import settings
from manager import lifespan
from routers.item_routes import router


app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )