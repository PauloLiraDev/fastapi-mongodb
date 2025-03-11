from config import settings
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
# Configuração da URL do MongoDB
MONGO_URI = settings.DB_URL
print(settings.DB_URL)
async def main():
    try:
        # Conectar ao MongoDB
        client = AsyncIOMotorClient(MONGO_URI)
        db = client["meu_banco"]
        collection = db["minha_colecao"]

        print("🟢 Conectado ao MongoDB!")

        # Inserir um documento de exemplo
        resultado = await collection.insert_one({"nome": "Paulo", "idade": 29})
        print(f"✅ Documento inserido com ID: {resultado.inserted_id}")

        # Consultar os documentos
        documento = await collection.find_one({"nome": "Paulo"})
        print("📄 Documento encontrado:", documento)

        # Fechar a conexão
        client.close()
        print("🔴 Conexão encerrada.")

    except Exception as e:
        print(f"❌ Erro ao conectar ao MongoDB: {e}")

# Executar a função assíncrona
asyncio.run(main())
