# 💸 Controle de Gastos – API com FastAPI

API para registrar, consultar e analisar gastos pessoais.  
Desenvolvida em **Python com FastAPI**, ideal para estudos, portfólio e uso real com pequenas adaptações.

---

## 🚀 Funcionalidades

✅ Adicionar novo gasto  
✅ Listar todos os gastos  
✅ Filtrar por categoria (acentuação insensível)  
✅ Obter total dos gastos  
✅ Validação com Pydantic  
✅ Organização por `routers` e `schemas`  
✅ Interface Swagger personalizada  
✅ Normalização automática de categorias  
✅ Código com marcações padronizadas e didáticas  

---

## 📎 Endpoints Disponíveis

| Método | Rota                   | Descrição                                 |
|--------|------------------------|-------------------------------------------|
| GET    | `/`                    | Teste de status da API                    |
| GET    | `/gastos`              | Listar todos os gastos                    |
| POST   | `/gastos`              | Adicionar novo gasto                      |
| GET    | `/gastos/{categoria}`  | Filtrar por categoria (ex: "alimentacao") |
| GET    | `/gastos/total`        | Obter o total de gastos registrados       |
| GET    | `/docs`                | Interface Swagger customizada (tema escuro) |

---

## 🖼️ Interface Swagger

![Swagger UI customizado](static/preview-swagger.png)

> Interface visual escura e personalizada, facilitando a navegação entre os endpoints da API.

---

## ⚙️ Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/rodrigosouza7/controle-de-gastos-api.git
cd controle-de-gastos-api

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Rode a aplicação
uvicorn main:app --reload
