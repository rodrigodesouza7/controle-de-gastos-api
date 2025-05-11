# Bibilotecas

from pydantic import BaseModel, Field 

# Modelo de dados para um gasto
class Gasto(BaseModel):
    descricao: str = Field (... , example="Supermercado")
    valor: float = Field (... , gt=0, example=150.75)
    categoria: str = Field (... , example="Alimentacão")