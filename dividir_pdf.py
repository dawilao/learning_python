import os
from PyPDF2 import PdfReader, PdfWriter

def dividir_pdf_1(diretorio, diretorio_saida):
    nome_arquivo = os.path.splitext(os.path.basename(diretorio))[0]
    pdf = PdfReader(diretorio)
    
    for pagina in range(len(pdf.pages)):
        escreve_pdf = PdfWriter()
        escreve_pdf.add_page(pdf.pages[pagina])

        nome_arquivo_saida = '{}_{}.pdf'.format(nome_arquivo, pagina)
        nome_completo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)
        
        with open(nome_completo_saida, 'wb') as saida:
            escreve_pdf.write(saida)
        
        print('Criado: {}'.format(nome_arquivo_saida))

'''
def dividir_pdf_2(diretorio, diretorio_saida):
    nome_arquivo = os.path.splitext(os.path.basename(diretorio))[0]
    pdf = PdfReader(diretorio)
    
    for pagina in range(0, len(pdf.pages), 2):
        escreve_pdf = PdfWriter()
        if pagina + 1 < len(pdf.pages):
            escreve_pdf.add_page(pdf.pages[pagina])
            escreve_pdf.add_page(pdf.pages[pagina + 1])
            
            nome_arquivo_saida = '{}_{}.pdf'.format(nome_arquivo, pagina // 2 + 1)
            nome_completo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)

            with open(nome_completo_saida, 'wb') as saida:
                escreve_pdf.write(saida)
            
            print('Criado: {}'.format(nome_arquivo_saida))
'''

pasta = input('Digite o caminho para encontrar o PDF a ser dividido: ')
arquivo = input('Digite o nome do arquivo: ')
diretorio = os.path.join(pasta, arquivo + '.pdf') 
diretorio_saida = input('Digite o caminho para o diretório onde os arquivos de saída devem ser salvos: ')

dividir_pdf_1(diretorio, diretorio_saida)

'''
dividir = int(input('Dividir a cada 1 ou 2 páginas? > '))
while dividir != 1 and dividir != 2:
    dividir = int(input('Opção incorreta. Dividir a cada 1 ou 2 páginas? > '))

if dividir == 1:
    dividir_pdf_1(diretorio, diretorio_saida)
else:
    dividir_pdf_2(diretorio, diretorio_saida)
'''
    
input('Tecle Enter para sair.')
