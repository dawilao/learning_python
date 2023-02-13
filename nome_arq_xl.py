'''Algoritmo que gera uma planilha com os nomes dos arquivos em determinada pasta.'''

import os
import subprocess
import openpyxl
import time

# Verificar se a biblioteca openpyxl está instalada
try:
    import openpyxl
except ImportError:
    # Instalar a biblioteca openpyxl usando pip
    subprocess.call([sys.executable, "-m", "pip", "install", "openpyxl"])

# Pedir ao usuário para inserir o caminho da pasta
path = input("Insira o caminho da pasta: ")

# Salva o arquivo no caminho informado pelo usuário
save_path = path

# Criar ou abrir o arquivo .xlsx
workbook = openpyxl.Workbook()
sheet = workbook.active

# Adicionar cabeçalho
sheet['A1'] = 'Nome dos Arquivos'

# Contador para começar a escrever na linha 2
row = 2

# Loop para pegar cada arquivo na pasta
for filename in os.listdir(path):
    sheet.cell(row=row, column=1, value=filename)
    row += 1

# Salvar o arquivo
workbook.save(f"{save_path}/nome_dos_arquivos_em_excel.xlsx")

# Exibir mensagem de sucesso
print("Arquivo salvo com sucesso.")

# Fazer o programa esperar um pouco antes de fechar
time.sleep(3)

# Manter o programa aberto
input("Pressione Enter para sair...")