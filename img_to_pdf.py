import os
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

def versão():
    print("\nPrograma criado por: Dawison Nascimento")
    print("Versão 2.0.2")
    print("Ultima alteração em 09/08/2024, às 17:48")

def convert_to_pdf(image_folder, output_pdf):
    # Obtém a lista de arquivos na pasta de imagens
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg')])
    print("Arquivos encontrados:", image_files)

    if not image_files:
        print("Não há arquivos válidos para inclusão no PDF.")
        return

    # Cria um novo documento PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)

    for image_file in image_files:
        # Abre a imagem
        image_path = os.path.join(image_folder, image_file)
        print("Convertendo:", image_path)
        img = Image.open(image_path)

        # Calcula as dimensões da imagem para caber na página com margens
        img_width, img_height = img.size
        page_width, page_height = A4
        if img_width > img_height:
            scaled_width = page_width
            scaled_height = (page_width / img_width) * img_height
        else:
            scaled_height = page_height
            scaled_width = (page_height / img_height) * img_width

        # Adiciona a imagem à página PDF com margens
        c.drawImage(image_path, (page_width - scaled_width) / 2, (page_height - scaled_height) / 2, width=scaled_width, height=scaled_height)

        # Adiciona uma nova página para a próxima imagem
        c.showPage()

    # Salva o PDF
    c.save()
    print("PDF criado com sucesso em:", output_pdf, "\n")

#Função para criar pastas
def criar_pastas(diretorio):
    # Verifica se o diretório existe, se não, cria
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Nomes das pastas a serem criadas
    pastas = ["DOCUMENTOS", "LEVANTAMENTO"]

    pastas_criadas = []
    for pasta in pastas:
        try:
            os.makedirs(os.path.join(diretorio, pasta))
            pastas_criadas.append(pasta)
        except OSError as e:
            print(f"Erro ao criar a pasta {pasta}: {e}")

    # Informa as pastas criadas
    if pastas_criadas:
        print("Pastas criadas:", ' e '.join(pastas_criadas), "\n")
    else:
        print("Nenhuma pasta foi criada.")

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

if __name__ == "__main__":
    iniciar = True

    # Iniciando a variável de contagem para print de mensagem específica
    contagem_print = 0

    # Definindo os comandos válidos
    comandos_validos = ["1", "sim", "s", "0", "n", "nao", "não", "comando", "comandos", "c", "3", "dividir", "v", "versao", "versão"]

    print("____________________________________________________________________________________________________")

    # Definir se o usuário deseja que as pastas sejam criadas
    escolha_criar_pastas = input("Responda digitando 1 para SIM ou 0 para NÃO.\nDeseja criar as pastas padrões (Documentos e Levantamento)? ")

    while escolha_criar_pastas.lower() not in ["0", "1", "s", "sim", "n", "nao", "não"]:
        print("Entrada inválida. Por favor, responda digitando 1 para SIM ou 0 para NÃO.\n")
        escolha_criar_pastas = input("Deseja criar as pastas padrões (Documentos e Levantamento)? ")

    if escolha_criar_pastas.lower() in ["1", "sim", "s"]:
        print("Você escolheu criar as pastas.\n")
        escolha_criar_pastas = True
    else:
        print("Você escolheu não criar as pastas.\n")
        escolha_criar_pastas = False
        
    while iniciar:
            print("____________________________________________________________________________________________________")

            # Verifica contagem_print para mostrar a mensagem específica
            if contagem_print > 4:
                input("\nLimpando a tela... Pressione Enter.")
                os.system('cls')
                print("____________________________________________________________________________________________________")
                contagem_print = 0
            elif contagem_print == 0:
                print("Para saber os comandos válidos, digite ""c"" ou ""comandos"".")
                contagem_print += 1
            else:
                contagem_print += 1
                pass

            # Pasta de entrada contendo as imagens
            input_folder = input("Insira um comando válido ou a pasta onde encontram-se as imagens: ")

            # Verifica se o diretório é acessível
            if os.path.isdir(input_folder):
                # Nome do PDF de saída
                output_pdf = os.path.join(input_folder, "EXECUÇÃO.pdf")

                # Converte as imagens para PDF
                convert_to_pdf(input_folder, output_pdf)

                # Usando a função para criar duas pastas, caso o usuário tenha optado por isso
                if escolha_criar_pastas:
                    criar_pastas(input_folder)
            else:
                # Verifica se a entrada é um comando válido
                if input_folder.lower() in comandos_validos:
                    if input_folder.lower() in ["1", "sim", "s"]:
                        print("Você escolheu criar as pastas.\n")
                        escolha_criar_pastas = True
                    
                    # Inicia a função para dividir PDF
                    elif input_folder.lower() in ["3", "dividir"]:
                        funcao_dividir_pdf = True

                        while funcao_dividir_pdf:
                            escolha_criar_pastas = False

                            pasta = input('\nDigite o caminho para encontrar o PDF a ser dividido: ')
                            arquivo = input('Digite o nome do arquivo: ')
                            diretorio = os.path.join(pasta, arquivo + '.pdf')

                            # Verifica se o arquivo existe. Se existir, roda a função
                            if os.path.isfile(diretorio):
                                diretorio_saida = pasta
                                dividir_pdf_1(diretorio, diretorio_saida)

                                # Finaliza a função após executar
                                funcao_dividir_pdf = False   
                                contagem_print += 1
                                input("\nDivisão finalizada. Pressione Enter para voltar.")

                            # Se não existir, solicita nova entrada
                            else:
                                print("Arquivo não encontrado. Tente novamente.")

                    elif input_folder.lower() in ["comando", "comandos", "c"]:
                        print("\nComandos válidos:")
                        print("Para criar as pastas, digite ""1"", ""sim"" ou ""s"".")
                        print("Para não criar as pastas, digite ""0"", ""nao"" ou ""n"".")
                        print("Para dividir PDF, digite ""3"" ou ""dividir"".")
                        print("Para saber a versão do programa, digite ""v"", ""versao"" ou ""versão""")
                        contagem_print -= 1

                    elif input_folder.lower() in ["v", "versao", "versão"]:
                        versão()

                    else:
                        print("Você escolheu não criar as pastas.\n")
                        escolha_criar_pastas = False
                
                else:
                    print("Comando ou diretório inválido. Tente novamente.\n")
                    
    input("\nPressione ENTER para finalizar.")