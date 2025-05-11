# Bibliotecas 

from fastapi import FastAPI
from models  import Gasto
from database import carregar_dados, salvar_dados

# Instancia do FastAPI

app = FastAPI(
    title="Controle de gastos",
    description="API para registrar e consultar gastos pessoais",
    version="1.0.0"
)

# Carregar os dados ao iniciar a API
gastos = carregar_dados()

# Rota de teste
@app.get("/")
def home():
    return {"mensagem": "API de Controle de Gastos rodando com sucesso!"}

# Rota para listar os gastos

@app.get("/gastos")
def listar_gastos():
    return gastos 

# Rota para adicionar novo gasto
@app.post("/gastos")
def adicionar_gasto(gasto: Gasto):
    gastos.append(gasto.model_dump())
    salvar_dados(gastos)
    return {"mensagem": "Gasto adicionado com sucesso!"}


