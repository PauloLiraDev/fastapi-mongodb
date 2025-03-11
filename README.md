# FastAPI com MongoDB

Este é um projeto de API simples utilizando **FastAPI** e **MongoDB** com o **Motor**, que é o driver assíncrono do MongoDB para Python. A API permite realizar operações básicas de CRUD, como cadastrar e listar pessoas em um banco de dados MongoDB.

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido para construir APIs.
- **MongoDB**: Banco de dados NoSQL.
- **Motor**: Driver assíncrono do MongoDB para Python.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.

## Instalação

Certifique-se de que tenha o Python 3.7+ instalado.

### 1. Clone o repositório

Clone o repositório para sua máquina local.


```bash
git clone https://github.com/PauloLiraDev/fastapi-mongodb
```


### 2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate  # No Windows
```


### 3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 4. Renomeie o arquivo .env_template para .env e defina as variáveis para se conectar ao MongoDB.

Veja o arquivo [aqui](.env_template).

```
DEBUG_MODE=True
DB_NAME=seu_banco
DB_URL=mongodb+srv://<seu_usuario>:<sua_senha>@<nome_do_cluster>.nbtnt.mongodb.net/?retryWrites=true&w=majority&appName=<nome_do_cluster>
```

### 5. Execute o arquivo    ```main.py``` ou inicialize o servidor localmente com o comando:
```
uvicorn main:app --reload
```

