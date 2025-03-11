from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
import logging
from models import Pessoa

# Configuração de logging para capturar os erros
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/cadastrar", response_description="Cadastrar nova pessoa", status_code=status.HTTP_201_CREATED)
async def cadastrar_pessoa(request: Request, item: Pessoa):
    try:
        item_dict = item.model_dump()
        
        # Tentativa de inserção no banco de dados
        resultado = await request.app.mongodb.user.insert_one(item_dict)
        
        # Converte o _id para string evitando erro ao retornar
        item_dict["_id"] = str(resultado.inserted_id)
        
        # Retorna o item inserido com a conversão para JSON
        return jsonable_encoder(item_dict)
    
    except Exception as err:
        # Log do erro
        logger.error(f"Erro ao cadastrar pessoa: {err}")
        
        # Lançando uma HTTPException com status 500 (Erro interno do servidor)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao cadastrar pessoa. Tente novamente mais tarde."
        )


@router.get("/listar", response_description="Listar todas as pessoas")
async def listar_pessoas(request: Request, item: Pessoa):
    try:
        item_dict = item.model_dump()
        item_dict['_id'] = {"$toString": "$_id"}
        pipeline = [
            {
                "$project": item_dict
            }
        ]
        # Executa a agregação na coleção 'user'
        registros = await request.app.mongodb.user.aggregate(pipeline).to_list(length=100)
        
        return jsonable_encoder(registros)
    
    except Exception as err:
        # Log do erro
        logger.error(f"Erro ao listar pessoas: {err}")
        
        # Lançando uma HTTPException com status 500 (Erro interno do servidor)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao listar pessoas. Tente novamente mais tarde."
        )
