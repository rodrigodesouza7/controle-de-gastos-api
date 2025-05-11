#Bibiotecas 

import json
from pathlib import Path

# Caminho do arquivo que vai simular o banco de dados

CAMINHO_ARQUIVO = Path("gastos.json") 

# Função para carregar os dados do arquivo JSON

def carregar_dados():
    if CAMINHO_ARQUIVO.exists(): 
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo: 
             return json.load(arquivo) 
    return [] 

# Função para salvar os dados no arquivo JSON

def salvar_dados(dados):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo: json .dump(dados, arquivo, indent=4, ensure_ascii=False)