'''Algoritmo para separar páginas de PDFs em arquivos separados.'''

import os
import PyPDF4

# Define uma função para dividir um PDF em arquivos contendo 1 página cada.
def dividir_pdf_1(diretorio, diretorio_saida):
    # Obtém o nome do arquivo original, sem extensão.
    nome_arquivo = os.path.splitext(os.path.basename(diretorio))[0]
    
    # Abre o arquivo PDF e itera sobre as páginas.
    pdf = PyPDF4.PdfFileReader(diretorio)
    for pagina in range(pdf.getNumPages()):
        # Cria um objeto PdfFileWriter para a página atual.
        escreve_pdf = PyPDF4.PdfFileWriter()
        escreve_pdf.addPage(pdf.getPage(pagina))

        # Define o nome do arquivo de saída e escreve o PDF atual para ele.
        nome_arquivo_saida = '{}_{}.pdf'.format(nome_arquivo, pagina)
        nome_completo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)
        with open(nome_completo_saida, 'wb') as saida:
            escreve_pdf.write(saida)
        
        # Imprime uma mensagem indicando que o arquivo de saída foi criado.
        print('Criado: {}'.format(nome_arquivo_saida))

# Define uma função para dividir um PDF em arquivos contendo 2 páginas cada.
def dividir_pdf_2(diretorio, diretorio_saida):
    # Obtém o nome do arquivo original, sem extensão.
    nome_arquivo = os.path.splitext(os.path.basename(diretorio))[0]

    # Abre o arquivo PDF e itera sobre as páginas em intervalos de 2.
    pdf = PyPDF4.PdfFileReader(diretorio)
    for pagina in range(0, pdf.getNumPages(), 2):
        # Cria um objeto PdfFileWriter para as duas páginas atuais, se existirem.
        escreve_pdf = PyPDF4.PdfFileWriter()
        if pagina + 1 < pdf.getNumPages():
            escreve_pdf.addPage(pdf.getPage(pagina))
            escreve_pdf.addPage(pdf.getPage(pagina + 1))
            nome_arquivo_saida = '{}_{}.pdf'.format(nome_arquivo, pagina // 2 + 1)
            nome_completo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)

            # Define o nome do arquivo de saída e escreve o PDF atual para ele.
            with open(nome_completo_saida, 'wb') as saida:
                escreve_pdf.write(saida)
            
            # Imprime uma mensagem indicando que o arquivo de saída foi criado.
            print('Criado: {}'.format(nome_arquivo_saida))

# Obtém o caminho para o arquivo PDF a ser dividido e o nome do arquivo.
pasta = input('Digite o caminho para encontrar o PDF a ser dividido: ')
arquivo = input('Digite o nome do arquivo: ')
diretorio = os.path.join(pasta, arquivo + '.pdf') 

# Obtém o caminho para o diretório onde os arquivos de saída devem ser salvos.
diretorio_saida = input('Digite o caminho para o diretório onde os arquivos de saída devem ser salvos: ')

# Pergunta ao usuário se ele deseja dividir o PDF em arquivos com 1 ou 2 páginas cada.
dividir = int(input('Dividir a cada 1 ou 2 páginas? > '))
while dividir != 1 and dividir != 2:
    dividir = int(input('Opção incorreta. Dividir a cada 1 ou 2 páginas? > '))

# Chama a função apropriada com base na escolha do usuário.
if dividir == 1:
    dividir_pdf_1(diretorio, diretorio_saida)
else:
    dividir_pdf_2(diretorio, diretorio_saida)

input('Tecle Enter para sair.')