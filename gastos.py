# 📚 Bibliotecas
from fastapi import APIRouter
from schemas.gasto import Gasto
from database import carregar_dados, salvar_dados
import unicodedata

# 🔗 Criação do router com prefixo e tag
router = APIRouter(
    prefix="/gastos",
    tags=["Gastos"],
    responses={404: {"description": "Não encontrado"}}
)

gastos = carregar_dados()

# 🔧 Função auxiliar para normalizar acentos
def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# 📄 Listar todos os gastos
@router.get(
    "/",
    summary="Listar todos os gastos",
    description="Retorna uma lista com todos os gastos cadastrados.",
    response_model=list[dict]
)
def listar_gastos():
    return gastos

# 📊 Obter total de gastos
@router.get(
    "/total",
    summary="Obter total de gastos",
    description="Retorna a soma total dos gastos e a quantidade de itens.",
    response_model=dict
)
def obter_total_gastos():
    total = sum(g["valor"] for g in gastos)
    return {
        "total": round(total, 2),
        "quantidade_itens": len(gastos)
    }

# 🔍 Filtrar por categoria
@router.get(
    "/{categoria}",
    summary="Filtrar gastos por categoria",
    description="Retorna os gastos que pertencem à categoria informada, ignorando acentuação.",
    response_model=list[dict]
)
def filtrar_gastos(categoria: str):
    categoria_normalizada = remover_acentos(categoria.lower())
    gastos_filtrados = [
        g for g in gastos
        if remover_acentos(g["categoria"].lower()) == categoria_normalizada
    ]
    if not gastos_filtrados:
        return {"mensagem": f"Nenhum gasto encontrado para a categoria '{categoria}'"}
    return gastos_filtrados

# ➕ Adicionar novo gasto
@router.post(
    "/",
    summary="Adicionar novo gasto",
    description="Adiciona um novo gasto no sistema e salva no arquivo local.",
    response_model=dict
)
def adicionar_gasto(gasto: Gasto):
    gastos.append(gasto.model_dump())
    salvar_dados(gastos)
    return {"mensagem": "Gasto adicionado com sucesso!"}
