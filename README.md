# 💸 Controle de Gastos API

API desenvolvida em Python com FastAPI para registrar, consultar e organizar gastos pessoais.

---

## 📋 Funcionalidades

* ✅ Registrar novos gastos
* ✅ Listar todos os gastos registrados
* ✅ Persistência local em `gastos.json`
* ✅ Documentação interativa com Swagger UI
* ✅ Validações com Pydantic
* ✅ Modularização com `routers/` e `schemas/`
* ✅ Filtro por categoria ignorando acentuação
* ✅ Cálculo do total de gastos

---

## 🚀 Tecnologias Utilizadas

* [Python 3.11+](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Pydantic v2](https://docs.pydantic.dev/latest/)
* [Replit](https://replit.com/) (ambiente de execução em nuvem)

---

## 📂 Estrutura de Arquivos

```
📁 controle-de-gastos-api
├── main.py             # Ponto de entrada da API
├── database.py         # Persistência em JSON
├── gastos.json         # Simulação do "banco de dados"
├── routers/            # Rotas separadas com APIRouter
│   └── gastos.py
├── schemas/            # Modelos de dados com validações
│   └── gasto.py
├── requirements.txt    # Dependências
└── README.md
```

---

## 🧪 Teste Rápido (Swagger UI)

Acesse via navegador:

```
🔗 https://controle-de-gastos-api.rodrigosouza71.repl.co/docs
```

---

## 📌 Exemplo de Requisição (POST /gastos)

```json
{
  "descricao": "Supermercado",
  "valor": 120.00,
  "categoria": "Alimentação"
}
```

---

## 📦 Instalação local (opcional)

```bash
git clone https://github.com/rodrigodesouza7/controle-de-gastos-api.git
cd controle-de-gastos-api
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## ✅ Boas Práticas Aplicadas

* Separação de responsabilidades (`main.py`, `database.py`, `routers/`, `schemas/`)
* Código limpo e documentado
* Tipagem estática com `str`, `float`, `Field`
* Validações com Pydantic (v2)
* Documentação automática (Swagger + OpenAPI)
* Persistência de dados com JSON para estudos (sem banco real)

---

## 📌 Autor

**Rodrigo Souza**
Formado em Sistemas de Informação
Bootcamp Desenvolvedor Python - XP Educação
🔗 [LinkedIn](https://www.linkedin.com/in/rodrigodesouzasilva)
📧 [rodrigosouzasilva@outlook.com](mailto:rodrigosouzasilva@outlook.com)

