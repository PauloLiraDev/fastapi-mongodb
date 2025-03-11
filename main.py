from fastapi import FastAPI
import uvicorn
from config import settings
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import Pessoa
from manager import lifespan


app = FastAPI(lifespan=lifespan)

@app.post("/itens")
async def cadastrar_pessoa(item: Pessoa):
    try:
        item_dict = item.model_dump()
        resultado = await app.mongodb.user.insert_one(item_dict)
        # Converte o _id para string evitando erro
        item_dict["_id"] = str(resultado.inserted_id)
        # Retorna o item com a conversão para JSON, lidando com o ObjectId
        return jsonable_encoder(item_dict)
    except Exception as err:
        print(err)
        return {'err': err}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )