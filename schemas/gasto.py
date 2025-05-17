# 📚 Bibliotecas
from pydantic import BaseModel, Field, validator
from typing import ClassVar


# ✅ Modelo de dados com validações

class Gasto(BaseModel):
    descricao: str = Field(..., min_length=3, example="Supermercado")
    valor: float = Field(..., gt=0, example=150.75)
    categoria: str = Field(..., min_length=3, example="Alimentação")

    CATEGORIAS_PERMITIDAS: ClassVar[set] = {
        "Alimentação", "Transporte", "Educação", "Lazer", "Saúde", "Moradia", "Outros"
    }

    @validator('descricao', 'categoria')
    def no_whitespace(cls, v):
        if not v.strip():
            raise ValueError("Campo não pode ser vazio ou só espaços")
        return v

    @validator('categoria')
    def categoria_valida(cls, v):
        valor_formatado = v.strip().title()
        if valor_formatado not in cls.CATEGORIAS_PERMITIDAS:
            raise ValueError(f"Categoria inválida. Use uma das: {', '.join(cls.CATEGORIAS_PERMITIDAS)}")
        return valor_formatado

