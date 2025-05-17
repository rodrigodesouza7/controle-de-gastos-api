 from fastapi.testclient import TestClient
 from main import app

 client = TestClient(app)

 def test_home_status():
     response = client.get("/")
     assert response.status_code == 200
     assert "mensagem" in response.json()

 def test_listar_gastos():
     response = client.get("/gastos/")
     assert response.status_code == 200
     assert isinstance(response.json(), list)

 def test_adicionar_gasto_valido():
     payload = {
         "descricao": "Padaria",
         "valor": 30.5,
         "categoria": "Alimentação"
     }
     response = client.post("/gastos/", json=payload)
     assert response.status_code == 200
     assert "mensagem" in response.json()

 def test_adicionar_gasto_categoria_invalida():
     payload = {
         "descricao": "Teste",
         "valor": 10.0,
         "categoria": "CategoriaErrada"
     }
     response = client.post("/gastos/", json=payload)
     assert response.status_code == 422

 def test_total_gastos():
     response = client.get("/gastos/total")
     assert response.status_code == 200
     body = response.json()
     assert "total" in body
     assert "quantidade_itens" in body

 def test_filtrar_categoria_existente():
     response = client.get("/gastos/Alimentação")
     assert response.status_code == 200
     assert isinstance(response.json(), list)

 def test_filtrar_categoria_inexistente():
     response = client.get("/gastos/NaoExiste")
     assert response.status_code == 200
     assert response.json()["mensagem"].startswith("Nenhum gasto encontrado")



