# 📚 Bibliotecas
from database import carregar_dados, salvar_dados
from gastos import normalizar_categoria  # ou do lugar onde está a função

# Funcão para corrigir categorias existentes

def corrigir_categorias_existentes():
    dados = carregar_dados()
    for gasto in dados:
        gasto["categoria"] = normalizar_categoria(gasto["categoria"])
    salvar_dados(dados)
    print("[OK] Categorias corrigidas e salvas.")

corrigir_categorias_existentes()
