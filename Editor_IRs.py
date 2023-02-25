'''
Nome: Editor de IRs
Função: Programa para separar, renomear e criptografar PDFs dos IRs de estagiários da empresa.
Versão 1.1
'''

import os, re, time, PyPDF2, PyPDF4

def menu():
    print('###########################################################')
    print('                      Editor de IRs                        ')
    print('Programa para separar, renomear e criptografar PDFs dos IRs')
    print('###########################################################\n')

# função para obter o nome completo do arquivo pdf
def get_name(filepath):
    try:
        with open(filepath, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            # percorre as páginas do pdf
            for page in pdf.pages:
                # encontra a string que contém o nome completo
                match = re.search(r'(\d{3}\.\d{3}\.\d{3})-(\d{2})\s(.+?)\n.*Natureza do Rendimento', page.extract_text())
                if match:
                    # retorna o nome completo encontrado e o cpf
                    cpf = match.group(1).replace('.', '') + match.group(2)
                    name = match.group(3)
                    return name, cpf
    except (FileNotFoundError, TypeError, PyPDF2.errors.FileNotDecryptedError):
        print(f'O arquivo {diretorio} não foi encontrado.')

def limpa_linha(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)

def verifica_desktop(save_path):
    desktop = os.path.normpath(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
    one_drive_desktop = os.path.normpath(os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Área de Trabalho'))
    
    save_to_desktop = False
    
    # Verifica se a pasta escolhida é a área de trabalho
    if os.path.normpath(save_path) == desktop or os.path.normpath(save_path) == one_drive_desktop:
        save_to_desktop = True
    
    if save_to_desktop:
        # Pergunta ao usuário se deseja salvar diretamente na área de trabalho
        confirm = input("Salvar diretamente na área de trabalho? (s/n) > ")
        if confirm.lower() == 'n':
            # Caso o usuário não queira salvar diretamente na área de trabalho, pede uma nova pasta de destino
            save_path = input("Tudo bem. Digite o caminho: ")
    
    # Aqui iria o código para salvar o arquivo no caminho indicado pelo usuário
    return save_path

# função para criptografar pdf com o CPF localizado
def criptografar_pdf_com_cpf(novo_filepath, cpf):
    with open(novo_filepath, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.append_pages_from_reader(pdf)
        pdf_writer.encrypt(cpf)
        with open(novo_filepath, 'wb') as f:
            pdf_writer.write(f)
            print(f'{novo_filename} bloqueado com a senha {cpf}')
            return 1

# Define uma função para dividir um PDF em arquivos contendo 1 página cada.
def dividir_pdf_1(diretorio, diretorio_saida):
    # Obtém o nome do arquivo original, sem extensão.
    nome_arquivo = os.path.splitext(os.path.basename(diretorio))[0]
    
    # Cria uma variável para contar a quantidade de arquivos divididos
    contagem_dividir_pdf = 0

    try:
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
            contagem_dividir_pdf += 1
    except (FileNotFoundError, TypeError, PyPDF2.errors.FileNotDecryptedError):
        print(f'O arquivo {diretorio} não foi encontrado.')


    # Retorna a contagem de arquivos criados
    return contagem_dividir_pdf

# Define uma função para dividir um PDF em arquivos contendo 2 páginas cada.
def dividir_pdf_2(diretorio, diretorio_saida):
    # Obtém o nome do arquivo original, sem extensão.
    nome_arquivo = os.path.splitext(os.path.basename(diretorio))[0]

    # Cria uma variável para contar a quantidade de arquivos divididos
    contagem_dividir_pdf = 0

    try:
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
                contagem_dividir_pdf += 1
    except (FileNotFoundError, TypeError, PyPDF2.errors.FileNotDecryptedError):
        print(f'O arquivo {diretorio} não foi encontrado.')

    # Retorna a contagem de arquivos criados
    return contagem_dividir_pdf

def verificar_duplicatas(pasta):
    lista_duplicados = []
    file_list = os.listdir(pasta)
    for file_name in file_list:
        if '_' in file_name:
            lista_duplicados.append(file_name)
    return lista_duplicados

if __name__ == '__main__':

    menu()

    # Cria uma variável para contar a quantidade de arquivos criptografados
    cont_criptografados = 0

    while True:
        # Obtém o caminho para o arquivo PDF a ser dividido e o nome do arquivo.
        while True:
            pasta = input('Digite o caminho para encontrar o PDF a ser dividido: ')
            if not os.path.exists(pasta):
                print('Caminho incorreto. Por favor, redigite o caminho')
            elif not os.path.isdir(pasta):
                print('O caminho especificado não é um diretório. Por favor, redigite o caminho')
            else:
                break

        arquivo = input('Digite o nome do arquivo (com a extensão .pdf no final): ')
        diretorio = os.path.join(pasta, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        while extensao_arquivo.lower() != '.pdf' or not os.path.isfile(diretorio):
            if extensao_arquivo.lower() != '.pdf':
                print('O arquivo deve ter a extensão .pdf')
            else:
                print('Arquivo não encontrado.')
            arquivo = input('Digite o nome do arquivo (com a extensão .pdf no final): ')
            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
            diretorio = os.path.join(pasta, arquivo)
        
        while True:
            # Obtém o caminho para o diretório onde os arquivos de saída devem ser salvos.
            diretorio_saida = input('Digite o caminho para o diretório onde os arquivos de saída devem ser salvos: ')
            if not os.path.exists(diretorio_saida):
                print('Caminho incorreto. Por favor, redigite o caminho.')
            elif not os.path.isdir(diretorio_saida):
                print('O caminho especificado não é um diretório. Por favor, redigite o caminho.')
            else:
                desktop = os.path.normpath(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
                one_drive_desktop = os.path.normpath(os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Área de Trabalho'))
                
                save_to_desktop = False
                
                # Verifica se a pasta escolhida é a área de trabalho
                if os.path.normpath(diretorio_saida) == desktop or os.path.normpath(diretorio_saida) == one_drive_desktop:
                    save_to_desktop = True
                
                if save_to_desktop:
                    # Pergunta ao usuário se deseja salvar diretamente na área de trabalho
                    confirm = input('Salvar diretamente na área de trabalho? (s/n) > ')
                    if confirm.lower() == 'n':
                        # Caso o usuário não queira salvar diretamente na área de trabalho, pede uma nova pasta de destino
                        continue
                break

        break
        
    # Pergunta ao usuário se ele deseja dividir o PDF em arquivos com 1 ou 2 páginas cada.
    while True:
        dividir = int(input('Dividir a cada 1 ou 2 páginas? > '))
        if dividir != 1 and dividir != 2:
            print('Opção incorreta. Selecione 1 ou 2.')
        else:
            break

    # Chama a função apropriada com base na escolha do usuário.
    if dividir == 1:
        contagem_dividir_pdf = dividir_pdf_1(diretorio, diretorio_saida)
    else:
        contagem_dividir_pdf = dividir_pdf_2(diretorio, diretorio_saida)

    print(f'\nDivisão finalizada. {contagem_dividir_pdf} arquivos criados.')
    print('Prosseguindo para a renomear e criptografar os arquivos...\n')
    time.sleep(4)

    # percorre os arquivos no diretório
    for filename in os.listdir(diretorio_saida):
        try:
            if filename.endswith('.pdf'):
                filepath = os.path.join(diretorio_saida, filename)
                name, cpf = get_name(filepath)
                if name:
                    # verifica se o arquivo com o mesmo nome já existe
                    novo_filename = name + '.pdf'
                    i = 1
                    while os.path.exists(os.path.join(diretorio_saida, novo_filename)):
                        novo_filename = name + f'_{i}.pdf'
                        i += 1
                    
                    # renomeia o arquivo com o nome completo encontrado
                    novo_filepath = os.path.join(diretorio_saida, novo_filename)
                    os.rename(filepath, novo_filepath)
                    print(f'{filename} renomeado para {novo_filename}')

                    # bloqueia o arquivo com a senha do cpf
                    cont_criptografados += criptografar_pdf_com_cpf(novo_filepath, cpf)
                else:
                    print(f'Nome não encontrado em {filename}')
        except (FileNotFoundError, TypeError, PyPDF2.errors.FileNotDecryptedError):
            print(f'O arquivo {diretorio} não foi encontrado.')

    print(f'\nFinalizado. {cont_criptografados} arquivos renomeados e criptografados.\n')

    print('Verificando duplicados...')
    time.sleep(3)
    duplicados = verificar_duplicatas(diretorio_saida)
    
    if len(duplicados) > 0:
        limpa_linha()
        print('Arquivos duplicados:')
        for nomes in range(len(duplicados)):
            print(duplicados[nomes])
    else:
        print('Não há arquivos duplicados.')
    
    input('\nPrograma finalizado. Tecle Enter para sair.')