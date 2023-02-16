'''Algoritmo para renomear IRs.'''

import os
import re
import subprocess

# Verificar se a biblioteca PyPDF2 está instalada
try:
    import PyPDF2
except ImportError:
    # Instalar a biblioteca pandas usando pip
    subprocess.call([sys.executable, "-m", "pip", "install", "pypdf2"])

# função para obter o nome completo do arquivo pdf
def get_name(filepath):
    with open(filepath, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        # percorre as páginas do pdf
        for page in pdf.pages:
            # encontra a string que contém o nome completo
            match = re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}\s(.+?)\n.*Natureza do Rendimento', page.extract_text())
            if match:
                # retorna o nome completo encontrado
                return match.group(1)

# caminho para encontrar os arquivos
path = input('Digite o caminho para encontrar os arquivos: ')

# percorre os arquivos no diretório
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        filepath = os.path.join(path, filename)
        name = get_name(filepath)
        if name:
            # renomeia o arquivo com o nome completo encontrado
            new_filename = name + '.pdf'
            new_filepath = os.path.join(path, new_filename)
            os.rename(filepath, new_filepath)
            print(f'{filename} renomeado para {new_filename}')
        else:
            print(f'Nome não encontrado em {filename}')
