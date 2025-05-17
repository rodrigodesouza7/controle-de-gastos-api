✅ README.md

# 💸 Controle de Gastos API

API desenvolvida em **Python com FastAPI** para registrar, consultar e organizar gastos pessoais.  
Ideal para estudos, portfólio profissional e projetos reais com persistência leve via JSON.

---

## 📋 Funcionalidades

✅ Registrar novos gastos  
✅ Listar todos os gastos registrados  
✅ Filtro por categoria (ignora acentuação)  
✅ Cálculo do total de gastos  
✅ Validações com Pydantic v2  
✅ Modularização com `routers/` e `schemas/`  
✅ Documentação interativa via Swagger UI (personalizada)  
✅ Persistência local em `gastos.json`  
✅ Testes automatizados com `pytest`  
✅ Interface Swagger com tema escuro via `custom.css`

---

## 🚀 Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic v2](https://docs.pydantic.dev/latest/)
- [pytest](https://docs.pytest.org/)
- [Replit](https://replit.com/) (ambiente de execução em nuvem)

---

## 📂 Estrutura de Arquivos

controle-de-gastos-api/
├── main.py # Ponto de entrada da API
├── database.py # Funções de persistência em JSON
├── gastos.json # Simulação do "banco de dados"
├── static/ # Arquivos visuais (tema Swagger)
│ ├── custom.css
│ └── preview-swagger.png
├── schemas/ # Modelos de dados (Pydantic)
│ └── gasto.py
├── routers/ # Rotas separadas com APIRouter (opcional)
│ └── gastos.py
├── test_gastos.py # Testes com pytest
├── requirements.txt # Dependências
└── README.md


---

## 🧪 Interface (Swagger UI)

Acesse no navegador:

🔗 https://controle-de-gastos-api.rodrigosouza71.repl.co/docs


---

## 📌 Exemplo de Requisição (POST /gastos)

```json
{
  "descricao": "Supermercado",
  "valor": 120.00,
  "categoria": "Alimentação"
}
🧪 Executar Testes Locais

pytest test_gastos.py

##📦 Instalação local (opcional)
git clone https://github.com/rodrigodesouza7/controle-de-gastos-api.git
cd controle-de-gastos-api
pip install -r requirements.txt
uvicorn main:app --reload

#✅ Boas Práticas Aplicadas

Separação de responsabilidades (main.py, database.py, routers/, schemas/)
Código limpo e comentado
Tipagem estática com str, float, List
Pydantic v2 com validações automáticas
Swagger customizado (tema escuro)
Testes automatizados com pytest
Estrutura pronta para deploy ou extensão futura

# 👤 Autor

Rodrigo Souza
Formado em Sistemas de Informação
Bootcamp Desenvolvedor Python — XP Educação
📧 rodrigosouzasilva@outlook.com
🔗 LinkedIn - www.linkedin.com/in/rodrigodesouzasilva

