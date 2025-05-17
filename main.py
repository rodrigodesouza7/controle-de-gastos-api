# Bibliotecas 

from fastapi import FastAPI
from schemas.gasto import Gasto
from database import carregar_dados, salvar_dados
from fastapi import HTTPException 
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from typing import List 
import unicodedata

# Função auxiliar
def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Instancia do FastAPI

app = FastAPI(
    title="Controle de gastos",
    description="API para registrar e consultar gastos pessoais",
    version="1.0.0"
)

# 🔧 Servir arquivos visuais
app.mount("/static", StaticFiles(directory="static"), name="static")


# Carregar os dados ao iniciar a API
gastos = carregar_dados()

# Rota de teste
@app.get(
    "/",
    tags=["Sistema"],
    summary="Status da API",
    description="Verifica se a API está no ar e responde com uma mensagem de boas-vindas.",
    responses={
        200: {"description": "API respondendo corretamente"}
    }
)
def home():
    return {"mensagem": "API de Controle de Gastos rodando com sucesso!"}

# 🌐 Rota Swagger personalizada com CSS
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="💸 Controle de Gastos — API Docs",
        swagger_css_url="/static/custom.css"
    )

# Rota para listar os gastos
@app.get("/gastos", tags=["Gastos"])
def listar_gastos():
    return gastos


# Rota para obter o total de gastos
@app.get(
    "/gastos/total",
    tags=["Gastos"],
    summary="Obter total de gastos",
    description="Retorna o valor total de todos os gastos registrados e a quantidade de itens.",
    responses={
        200: {"description": "Totais calculados com sucesso"},
        500: {"description": "Erro interno do servidor"}
    }
)
def obter_total_gastos():
    total = sum(g["valor"] for g in gastos)
    return {
        "total": round(total, 2),
        "quantidade_itens": len(gastos)
    }

# Rota para filtrar gastos por categoria
@app.get(
    "/gastos/{categoria}",
    tags=["Gastos"],
    summary="Filtrar gastos por categoria",
    description="Retorna apenas os gastos que pertencem à categoria informada. O filtro ignora acentos e maiúsculas/minúsculas.",
    responses={
        200: {"description": "Gastos filtrados com sucesso"},
        404: {"description": "Nenhum gasto encontrado para a categoria"}
    }
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


# Rota para adicionar novo gasto
@app.post(
    "/gastos",
    status_code=201,
    tags=["Gastos"],
    summary="Adicionar novo gasto",
    description="Adiciona um novo gasto à base de dados, validando os campos recebidos.",
    responses={
        201: {"description": "Gasto adicionado com sucesso"},
        422: {"description": "Erro de validação nos dados enviados"}
    }
)
def adicionar_gasto(gasto: Gasto):
    gastos.append(gasto.model_dump())
    salvar_dados(gastos)
    return {"mensagem": "Gasto adicionado com sucesso!"}



    




    

    
 


