💸 Controle de Gastos – API com FastAPI

API desenvolvida para registrar, consultar e analisar gastos pessoais.
Ideal para fins de estudo, portfólio profissional e pequenas aplicações reais com foco em controle financeiro automatizado.

Construída com FastAPI, estruturada em módulos e com lógica aplicada de validação, categorização e normalização de dados.

🚀 Funcionalidades

✅ Adicionar novo gasto
✅ Listar todos os gastos
✅ Filtrar por categoria (acentuação insensível)
✅ Obter total dos gastos
✅ Validação de dados com Pydantic
✅ Organização por routers e schemas
✅ Interface Swagger UI customizada (modo escuro)
✅ Normalização automática de categorias (via script)
✅ Código modular, didático e reutilizável
✅ Testes automatizados com pytest
📎 Endpoints Disponíveis

Método	Rota	Descrição
GET	/	Teste de status da API
GET	/gastos	Listar todos os gastos registrados
POST	/gastos	Adicionar novo gasto
GET	/gastos/{categoria}	Filtrar por categoria (ex: "alimentacao")
GET	/gastos/total	Obter o total acumulado dos gastos
GET	/docs	Interface Swagger interativa (modo escuro)
🖼️ Interface Swagger

A API conta com Swagger UI customizado para facilitar a navegação entre os endpoints:

http://127.0.0.1:8000/docs
⚙️ Instalação

# 1. Clone o repositório
git clone https://github.com/rodrigosouza7/controle-de-gastos-api.git
cd controle-de-gastos-api

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Rode a aplicação
uvicorn main:app --reload

🗂️ Estrutura do Projeto

controle-de-gastos-api/
├── main.py                  # Entrada principal da aplicação FastAPI
├── database.py              # Interface de dados simulada
├── gastos.py                # Lógica de domínio (listagem, filtros)
├── gasto.py                 # Modelo de gasto com validação
├── corrigir_categorias.py   # Script para padronização de categorias
├── corrigir_dados.py        # Script de limpeza de dados
├── test_gastos.py           # Testes automatizados com Pytest
├── gastos.json              # Base de dados simulada
├── requirements.txt         # Lista de dependências
├── pyproject.toml           # Metadados do projeto
├── uv.lock                  # Lockfile de dependências
├── README.md                # Este documento

👤 Sobre o Autor
**Rodrigo de Souza Silva**  
Profissional de Tecnologia da Informação com formação em Sistemas de Informação e pós-graduação em Data Science & Machine Learning. Atua no desenvolvimento de projetos práticos com Python, APIs REST, automações e análise de dados, aplicando os conhecimentos adquiridos em formação técnica e cursos especializados.

Apaixonado por dados, boas práticas de código e soluções que unem lógica, organização e utilidade real.

- [LinkedIn](https://www.linkedin.com/in/rodrigodesouzasilva)  
- [GitHub](https://github.com/rodrigodesouza7)

---

## 📄 Licença

Este projeto está licenciado sob os termos da licença [MIT](https://opensource.org/licenses/MIT).  
Você pode usar, modificar e distribuir com os devidos créditos ao autor.
