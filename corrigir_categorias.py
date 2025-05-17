# 📚 Bibliotecas
from database import carregar_dados, salvar_dados
import unicodedata

# 🧠 Função auxiliar para normalizar categorias
def normalizar_categoria(categoria: str) -> str:
    categoria = unicodedata.normalize("NFKD", categoria)
    categoria = "".join(c for c in categoria if not unicodedata.combining(c))
    return categoria.strip().lower()

# 🔧 Função principal para corrigir as categorias no JSON
def corrigir():
    dados = carregar_dados()
    for gasto in dados:
        gasto["categoria"] = normalizar_categoria(gasto.get("categoria", ""))
    salvar_dados(dados)
    print("[OK] Categorias normalizadas no JSON.")

# 🚀 Execução direta
if __name__ == "__main__":
    corrigir()
