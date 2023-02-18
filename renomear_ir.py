'''Algoritmo para renomear IRs.'''

import os
import re
import subprocess

# Verificar se a biblioteca PyPDF2 está instalada
try:
    import PyPDF4
except ImportError:
    # Instalar a biblioteca pandas usando pip
    subprocess.call([sys.executable, "-m", "pip", "install", "pypdf4"])

# função para obter o nome completo do arquivo pdf
def obter_nome_arquivo(filepath):
    with open(filepath, 'rb') as f:
        pdf = PyPDF4.PdfFileReader(f)
        # percorre as páginas do pdf
        for page in pdf.pages:
            # encontra a string que contém o nome completo
            match = re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}\s(.+?)\n.*Natureza do Rendimento', page.extract_text())
            if match:
                # retorna o nome completo encontrado
                return match.group(1)

def renomear_arquivo_ir(pasta):
    # percorre os arquivos no diretório
    for filename in os.listdir(pasta):
        if filename.endswith('.pdf'):
            filepath = os.path.join(pasta, filename)
            name = obter_nome_arquivo(filepath)
            if name:
                # renomeia o arquivo com o nome completo encontrado
                new_filename = name + '.pdf'
                new_filepath = os.path.join(pasta, new_filename)
                os.rename(filepath, new_filepath)
                print(f'{filename} renomeado para {new_filename}')
            else:
                print(f'Nome não encontrado em {filename}')

# caminho para encontrar os arquivos
pasta = input('Digite o caminho para encontrar os arquivos: ')

renomear_arquivo_ir(pasta)
