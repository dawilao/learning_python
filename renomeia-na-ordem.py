import os
from datetime import datetime

# Pasta onde estão os arquivos
pasta = input("Informe o caminho para a pasta: ")

# Listar os arquivos na pasta e ordená-los por data de modificação
arquivos = os.listdir(pasta)
arquivos.sort(key=lambda x: os.path.getmtime(os.path.join(pasta, x)))

# Renomear os arquivos de acordo com sua posição na classificação por data
for i, arquivo in enumerate(arquivos, start=1):
    novo_nome = f"{i:03d}"
    nome, extensao = os.path.splitext(arquivo)
    caminho_antigo = os.path.join(pasta, arquivo)
    caminho_novo = os.path.join(pasta, f"{novo_nome}{extensao}")
    os.rename(caminho_antigo, caminho_novo)
    print(f"Arquivo {arquivo} renomeado para {novo_nome}{extensao}")

input("")
