#Bibiotecas 

import json
from pathlib import Path

# Caminho do arquivo que vai simular o banco de dados

CAMINHO_ARQUIVO = Path("gastos.json") 

# Função para carregar os dados do arquivo JSON com tratamento de erros
def carregar_dados():
    if CAMINHO_ARQUIVO.exists():
        try:
            with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                if not isinstance(dados, list):
                    raise ValueError("Esperado uma lista de gastos.")
                return dados
        except json.JSONDecodeError as e:
            print(f"[ERRO] JSON malformado: {e}")
        except Exception as e:
            print(f"[ERRO] Erro inesperado ao carregar dados: {e}")
    return []


# Função para salvar os dados no arquivo JSON

def salvar_dados(dados):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo: json .dump(dados, arquivo, indent=4, ensure_ascii=False)