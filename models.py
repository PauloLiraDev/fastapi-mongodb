from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    idade: int
    profissao: str
    salario: int