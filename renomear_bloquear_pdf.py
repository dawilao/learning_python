from dividir_pdf import *
from renomear_ir import *

# Obtém o caminho para o arquivo PDF a ser dividido e o nome do arquivo.
pasta = input('Digite o caminho para encontrar o PDF a ser dividido: ')
arquivo = input('Digite o nome do arquivo: ')
diretorio = os.path.join(pasta, arquivo + '.pdf') 

# Pergunta ao usuário se ele deseja dividir o PDF em arquivos com 1 ou 2 páginas cada.
dividir = int(input('Dividir a cada 1 ou 2 páginas? > '))
while dividir != 1 and dividir != 2:
    dividir = int(input('Opção incorreta. Dividir a cada 1 ou 2 páginas? > '))

# Chama a função apropriada com base na escolha do usuário.
if dividir == 1:
    dividir_pdf_1(diretorio)
else:
    dividir_pdf_2(diretorio)

seguir = input('Deseja seguir para renomear os arquivos?')
if seguir == 's':
    renomear_arquivo_ir(pasta)
else:
    SystemExit
