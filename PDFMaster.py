#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script para manipulação de arquivos PDF e JPG.
- Converte imagens JPG em um PDF.
- Cria pastas padrão para organização de arquivos.
- Divide um arquivo PDF em várias páginas individuais.
- Divide um arquivo PDF em outros, limitando o tamanho a 5Mb
- Abre o WhatsApp de contato infomado

Interface gráfica desenvolvida usando o customtkinter.
<https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22>
"""

__author__ = "Dawison Nascimento"
__license__ = "Sem licensa definida"
__version__ = "4.0.0"
__maintainer__ = "Dawison Nascimento"

import tkinter as tk
from tkinter import filedialog, messagebox
import os, errno, requests, webbrowser, customtkinter, shutil
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# Função para mostrar a versão do programa
def versão():
    instrucoes = (
        "Bem-vindo ao PDFMaster.\n\n"
        "O PDFMaster foi desenvolvido para facilitar a criação e manipulação de arquivos PDF. Ele oferece ferramentas para gerar PDFs a partir de imagens, criar pastas padrão e dividir PDFs, otimizando esses processos.\n"
        "\nFunções do programa:"
        "\n    1. Imagem para PDF: Converte imagens JPG de uma pasta especificada em um arquivo PDF."
        "\n    2. Criar Pastas Padrão: Cria as pastas 'DOCUMENTOS' e 'LEVANTAMENTO' no diretório escolhido."
        "\n    3. Dividir PDF: Separa as páginas de um PDF selecionado em arquivos individuais."
        "\n    4. Dividir PDF por Tamanho: Divide um PDF selecionado em arquivos menores, com no máximo 5 MB cada."
        "\n    5. Contato por WhatsApp: Abre o aplicativo WhatsApp na conversa com o número fornecido."
        )

    # Exibe uma mensagem com informações sobre a versão do programa
    messagebox.showinfo("Sobre o Programa", 
                        f"{instrucoes}\n\nPrograma criado por {__author__}\nVersão {__version__}\nUltima alteração em 27/08/2024, às 11:30")

def toggle_ajuda():
    if btn_versao.winfo_ismapped():
        btn_versao.grid_forget()
        btn_contato_programador.grid_forget()
    else:
        # Adiciona os botões "Versão" e "Contate o programador" acima do botão "Sair"
        btn_versao.grid(row=0, column=0, pady=(5,0))
        btn_contato_programador.grid(row=1, column=0, pady=(10, 5))
        # Atualiza o layout e ajusta o tamanho da janela ao conteúdo

'''def toggle_contato_wpp():
    if entry_contato.winfo_ismapped():
        entry_contato.pack_forget()
        btn_gerador_contato_wpp.pack_forget()
    else:
        # Adiciona os botões "Versão" e "Contate o programador" acima do botão "Sair"
        entry_contato.pack(pady=5, before=btn_ajuda_e_suporte)
        btn_gerador_contato_wpp.pack(pady=5, before=btn_ajuda_e_suporte)'''

# Função para converter arquivos JPG em PDF
def convert_to_pdf(image_folder, output_pdf):
    # Obtém a lista de arquivos JPG/JPEG no diretório especificado
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg')])

    arquivo = os.path.join(image_folder, "EXECUÇÃO.pdf")
    
    # Verifica se há arquivos de imagem válidos no diretório
    if not image_files:
        messagebox.showerror("Erro", "Não há arquivos válidos para inclusão no PDF.")
        return

    # Verifica se no diretório já existe arquivo PDF de nome "EXECUÇÃO"
    if os.path.exists(arquivo):
        messagebox.showinfo("Aviso", "Arquivo já existente.")
        return

    # Cria um novo documento PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)
    
    for image_file in image_files:
        # Abre cada imagem e redimensiona para caber na página PDF
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

        # Adiciona a imagem ao PDF centralizada na página
        c.drawImage(image_path, (page_width - scaled_width) / 2, (page_height - scaled_height) / 2, width=scaled_width, height=scaled_height)
        c.showPage()  # Adiciona uma nova página para a próxima imagem

    # Salva o documento PDF
    c.save()
    messagebox.showinfo("Sucesso", f"PDF criado com sucesso em: {output_pdf}")

# Função para criar pastas padrão
def criar_pastas(diretorio):
    # Define os nomes das pastas a serem criadas
    pastas = ["DOCUMENTOS", "LEVANTAMENTO"]
    pastas_criadas = []

    # Tenta criar cada pasta no diretório especificado
    for pasta in pastas:
        try:
            os.makedirs(os.path.join(diretorio, pasta))
            pastas_criadas.append(pasta)
        except OSError as e:
            # Verifica se a pasta já existe ou se ocorreu outro erro
            if e.errno == errno.EEXIST:
                messagebox.showwarning("Aviso", f"A pasta {pasta} já existe.")
            else:
                messagebox.showerror("Erro", f"Erro ao criar a pasta {pasta}: {e}")

    # Informa ao usuário quais pastas foram criadas
    if pastas_criadas:
        messagebox.showinfo("Pastas Criadas", f"Pastas criadas: {' e '.join(pastas_criadas)}")
    else:
        messagebox.showinfo("Nenhuma Pasta Criada", "Nenhuma pasta foi criada.")

# Função para dividir um arquivo PDF em páginas individuais
def dividir_pdf_1(diretorio):
    nome_arquivo = os.path.splitext(os.path.basename(diretorio))[0]
    pasta_saida = os.path.dirname(diretorio)  # Obtém o diretório do arquivo original
    pdf = PdfReader(diretorio)
    
    # Para cada página do PDF, cria um novo arquivo PDF com a página única
    for pagina in range(len(pdf.pages)):
        escreve_pdf = PdfWriter()
        escreve_pdf.add_page(pdf.pages[pagina])

        nome_arquivo_saida = '{}_{}.pdf'.format(nome_arquivo, pagina)
        nome_completo_saida = os.path.join(pasta_saida, nome_arquivo_saida)
        
        with open(nome_completo_saida, 'wb') as saida:
            escreve_pdf.write(saida)
        
        print('Criado: {}'.format(nome_arquivo_saida))
    
    messagebox.showinfo("Sucesso", "Divisão de PDF concluída.")

########## DIVIDIR PDF POR TAMANHO ##########

# Função chamada ao clicar no botão para dividir por tamanho
def dividir_pdf_por_tamanho_interface():
    caminho_inicial = entry_caminho_pasta_dividir_por_tamanho.get()  # Obtém o caminho indicado pelo usuário

    if caminho_inicial.lower() == "jesus":
        messagebox.askquestion("Amém", "Será que você vai para o céu?")

    arquivo = filedialog.askopenfilename(title="Selecione o arquivo", initialdir=caminho_inicial, filetypes=[("PDF files", "*.pdf")])
        
    # Obtém o diretório de saída
    pasta_saida = os.path.dirname(arquivo)

    if arquivo:
        # Exibindo o arquivo selecionado
        messagebox.showinfo(title='Arquivo selecionado', message=f"Arquivo selecionado: {arquivo}\n\nPressione OK e aguarde...")

        dividir_por_tamanho(arquivo, pasta_saida)

# Função para dividir um arquivo PDF em partes com menos que o tamanho (em MB) especificado
def dividir_por_tamanho(caminho, caminho_saida, tamanho_mb_maximo=4.2):

    mensagem_final = []

    # Determinar o caminho da pasta temporária na pasta Documentos
    temp_folder = os.path.join(os.path.expanduser('~'), 'Documents', 'temp_folder')
    
    # Verifica se a pasta definida na temp_folder existe. Se existir, apaga a mesma antes de seguir com a função
    if os.path.exists(temp_folder):
        # Excluir a pasta temporária
        shutil.rmtree(temp_folder)

    os.makedirs(temp_folder, exist_ok=True)

    # Copiar o arquivo selecionado para a pasta temporária
    caminho_temp = os.path.join(temp_folder, os.path.basename(caminho))
    shutil.copy(caminho, caminho_temp)

    # Atualizar o caminho para o arquivo temporário copiado
    leitor_pdf = PdfReader(caminho_temp)
    total_pages = len(leitor_pdf.pages)

    num_contagem = 1
    current_writer = PdfWriter()
    temp_caminho = os.path.join(temp_folder, "temp.pdf")

    def save_current_part():
        nonlocal num_contagem, current_writer, temp_caminho

        nome_arquivo = os.path.basename(caminho)

        if len(current_writer.pages) > 0:
            with open(temp_caminho, "wb") as temp_file:
                current_writer.write(temp_file)
            nome_arquivo_base = os.path.splitext(os.path.basename(caminho))[0]
            current_size_mb = os.path.getsize(temp_caminho) / (1024 * 1024)
            output_file_name = f"PT{num_contagem:02} {nome_arquivo_base}.pdf"
            output_caminho = os.path.join(temp_folder, output_file_name)
            os.rename(temp_caminho, output_caminho)
            print(f"{output_file_name} criado com {len(current_writer.pages)} páginas, tamanho: {current_size_mb:.2f} MB")
            mensagem_final.append(f"{output_file_name} criado com {len(current_writer.pages)} páginas, tamanho: {current_size_mb:.2f} MB\n")
            num_contagem += 1
            current_writer = PdfWriter()

    for i in range(total_pages):
        current_writer.add_page(leitor_pdf.pages[i])

        # Salva a parte atual temporariamente e verifica o tamanho do arquivo
        if len(current_writer.pages) >= 1:
            current_writer.write(temp_caminho)
            current_size_mb = os.path.getsize(temp_caminho) / (1024 * 1024)
            if current_size_mb >= tamanho_mb_maximo:
                save_current_part()

    # Salva a última parte, se houver páginas restantes
    if len(current_writer.pages) > 0:
        save_current_part()

    # Mover os arquivos gerados de volta para a pasta original
    for file_name in os.listdir(temp_folder):
        if file_name.startswith("PT"):
            shutil.move(os.path.join(temp_folder, file_name), caminho_saida)

    # Excluir a pasta temporária
    shutil.rmtree(temp_folder)

    messagebox.showinfo("Sucesso", f"Divisão de PDF concluída.\n\n{'\n'.join(mensagem_final)}")

# Função para abrir o seletor de diretório
def selecionar_diretorio():
    """Abre um diálogo para selecionar um diretório e atualiza o campo de entrada com o caminho selecionado."""
    diretorio = filedialog.askdirectory()
    if diretorio:  # Verifica se um diretório foi selecionado
        entry_caminho_pasta.delete(0, tk.END)  # Limpa o campo de entrada
        entry_caminho_pasta.insert(0, diretorio)  # Insere o novo caminho no campo de entrada
        return diretorio
    return None

# Função chamada ao clicar no botão para converter imagens em PDF
def converter_imagens():
    caminho = entry_caminho_pasta.get()

    if caminho.lower() == "jesus":
        messagebox.askquestion("Amém", "Será que você vai para o céu?")

    if os.path.exists(caminho):
        output_pdf = os.path.join(caminho, "EXECUÇÃO.pdf")
        convert_to_pdf(caminho, output_pdf)
    else:
        caminho = selecionar_diretorio()

# Função para obter dados de login na URL especificada (GitHub)
def obter_dados_login(url):
    try:
        # Faz a requisição para obter o conteúdo do arquivo
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve algum erro na requisição
        
        # Processa o conteúdo do arquivo
        dados = resposta.text.splitlines()
        usuarios = {}
        
        for linha in dados:
            if linha.strip():  # Ignora linhas vazias
                usuario, senha = linha.split(':')  # Supondo que o formato seja "usuario:senha"
                usuarios[usuario.strip()] = senha.strip()
        
        return usuarios
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o arquivo: {e}")
        return None

# Função chamada ao clicar no botão para criar pastas padrão
def criar_pastas_interface():
    diretorio = entry_caminho_pasta.get()

    if diretorio.lower() == "jesus":
        messagebox.askquestion("Amém", "Será que você vai para o céu?")

    if os.path.exists(diretorio):
        criar_pastas(diretorio)
    else:
        diretorio = selecionar_diretorio()

# Função chamada ao clicar no botão para dividir um PDF
def dividir_pdf_1_interface():
    caminho_inicial = entry_caminho_dividir_pdf_1.get()  # Obtém o caminho indicado pelo usuário

    if caminho_inicial.lower() == "jesus":
        messagebox.askquestion("Amém", "Será que você vai para o céu?")

    arquivo = filedialog.askopenfilename(title="Selecione o arquivo", initialdir=caminho_inicial, filetypes=[("PDF files", "*.pdf")])
    
    if arquivo:
        dividir_pdf_1(arquivo)

def formata_contato_wpp():
    contato = entry_gerador_contato_por_wpp.get()

    # Cria uma tabela de tradução para remover os caracteres desejados
    tabela_remocao = str.maketrans('', '', '().-, \n')

    contato_formatado = contato.translate(tabela_remocao)

    if str(len(contato_formatado)) == "11":
        webbrowser.open(f"https://wa.me/55{contato_formatado}")
    else:
        messagebox.showerror("Erro", "Contato incorreto. Verifique o contato informado.")

# Função de validação dos dados de login
def validacao_login():
    usuario = entry_usuario.get().lower()  # Recebe o usuário do entrybox
    senha = entry_senha.get()  # Recebe a senha do entrybox

    # Verifica o usuário e verifica a senha definida para o usuário na biiblioteca de dados de login
    if lista_logins_padroes.get(usuario) == senha:  
        messagebox.showinfo("Login sucedido", f"Bem vindo, {usuario.capitalize()}!")
        janela_login.destroy()  # Fecha a tela de login
        janela_principal()  # Abre tela principal
    else:
        messagebox.showerror("Login incorreto", "Usuário ou senha inválidos!")

def config_btn(btn):
    btn.configure(fg_color="#035397",
                  text_color=("white"),
                  corner_radius=52)
    
def switch_altera_modo_dark_light():
    modo = switch_dark_light_mode.get()

    if modo == "on":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

def print_dimensão():
    lista = [tab_janela, frame_contatos_sair, frame_switch, frame_contatos_sair_centralizado, frame_contatos_sair_esquerda, 
             switch_dark_light_mode, label_switch]

    for item in lista:
        largura = item.winfo_width()
        altura = item.winfo_height()
        print(f"{item}, largura = {largura} || Altura = {altura}")

########## JANELA PRINCIPAL ##########

def janela_principal():
    global entry_caminho_pasta, btn_versao, btn_contato_programador, btn_sair, entry_gerador_contato_por_wpp, btn_gerador_contato_wpp
    global btn_ajuda_e_suporte, switch_dark_light_mode, frame_contatos_sair_centralizado, frame_contatos_sair_esquerda, entry_caminho_pasta_dividir_por_tamanho
    global entry_caminho_dividir_pdf_1, btn_abrir_pasta_dividir_pdf_por_tamanho, tab_janela, frame_contatos_sair, frame_switch, label_switch

    # Configuração da interface gráfica principal, com título e tamanho da janela
    janela = customtkinter.CTk()
    janela.title("PDFMaster")
    janela.geometry("540x320")
 
    tab_janela = customtkinter.CTkTabview(master=janela, border_width=2, height=35, width=520)
    tab_janela.pack(pady=(0,5))  # Ajusta o padding e expande para preencher o espaço

########## ABA IMAGEM PARA PDF ##########

    # Adicionar uma aba
    aba_imagem_pdf = tab_janela.add("Imagem para PDF")

    # Frame para separação dos botões
    frame_aba_imagem_pdf = customtkinter.CTkFrame(master=aba_imagem_pdf, border_width=0, width=350)
    frame_aba_imagem_pdf.pack(padx=0, fill="x")

    # Cria um rótulo (label) para o campo de entrada do caminho (pasta) para localização das fotos
    label_caminho_pasta = customtkinter.CTkLabel(master=frame_aba_imagem_pdf, text="Caminho:", pady=5, anchor="w", width=350) # Alinha o texto à esquerda
    label_caminho_pasta.pack(pady=(5,0), padx=0)  # Ajusta o padding superior e faz o label preencher a largura disponível

    # Cria um campo de entrada (Entry) para o usuário digitar o caminho (pasta) para localização das fotos
    entry_caminho_pasta = customtkinter.CTkEntry(master=frame_aba_imagem_pdf, 
                                                 placeholder_text="Insira o caminho",
                                                 width=350,
                                                 border_width=1)
    entry_caminho_pasta.pack(pady=0)

    # Botão para converter imagens em PDF
    btn_converter = customtkinter.CTkButton(master=frame_aba_imagem_pdf,
                                            text="Converter Imagens para PDF",
                                            command=converter_imagens)
    btn_converter.pack(pady=15)  # Espaçamento vertical (pady)
    config_btn(btn_converter)

    # Botão para criar pastas padrão
    btn_criar_pastas = customtkinter.CTkButton(master=frame_aba_imagem_pdf,
                                               text="Criar Pastas Padrão",
                                               command=criar_pastas_interface)
    btn_criar_pastas.pack(pady=(0,10))
    config_btn(btn_criar_pastas)

########## ABA DIVIDIR PDF ##########

    # Adicionar uma aba
    aba_dividir_pdf = tab_janela.add("Dividir PDF")

    # Frame para separação dos botões
    frame_aba_dividir_pdf_1 = customtkinter.CTkFrame(master=aba_dividir_pdf, border_width=0)
    frame_aba_dividir_pdf_1.pack(padx=0, fill="x")  # Preencher horizontalmente (fill="x") ativa o width acima

    # Cria um rótulo (label) para o campo de entrada do caminho (pasta) para localização das fotos
    label_caminho_pasta_aba_dividir_pdf_1 = customtkinter.CTkLabel(master=frame_aba_dividir_pdf_1, text="Caminho:", pady=5, anchor="w", width=350) # Alinha o texto à esquerda
    label_caminho_pasta_aba_dividir_pdf_1.pack(pady=(5,0), padx=0)  # Ajusta o padding superior e faz o label preencher a largura disponível

    entry_caminho_dividir_pdf_1 = customtkinter.CTkEntry(master=frame_aba_dividir_pdf_1,
                                                         placeholder_text="Insira o caminho",
                                                         width=350,
                                                         border_width=1)
    entry_caminho_dividir_pdf_1.pack(pady=(0,5))

    # Botão para dividir um PDF em páginas individuais
    btn_dividir_pdf = customtkinter.CTkButton(master=frame_aba_dividir_pdf_1, 
                                              text="Dividir PDF", 
                                              command=dividir_pdf_1_interface)
    btn_dividir_pdf.pack(pady=10)
    config_btn(btn_dividir_pdf)

########## ABA DIVIDIR POR TAMANHO ##########

    # Adicionar uma aba
    aba_dividir_pdf_por_tamanho = tab_janela.add("Dividir PDF por Tamanho")

    # Frame para separação dos botões
    frame_aba_dividir_pdf_por_tamanho = customtkinter.CTkFrame(master=aba_dividir_pdf_por_tamanho, border_width=0)
    frame_aba_dividir_pdf_por_tamanho.pack(padx=0, fill="x")  # Preencher horizontalmente (fill="x") ativa o width acima

    # Cria um rótulo (label) para o campo de entrada do caminho (pasta) para localização das fotos
    label_caminho_pasta_aba_dividir_pdf_por_tamanho = customtkinter.CTkLabel(master=frame_aba_dividir_pdf_por_tamanho,
                                                                   text="Caminho:",
                                                                   pady=5,
                                                                   anchor="w",
                                                                   width=350) # Alinha o texto à esquerda
    label_caminho_pasta_aba_dividir_pdf_por_tamanho.pack(pady=(5,0), padx=0)  # Ajusta o padding superior e faz o label preencher a largura disponível

    # Cria um campo de entrada (Entry) para o usuário digitar o caminho (pasta) para localização do PDF
    entry_caminho_pasta_dividir_por_tamanho = customtkinter.CTkEntry(master=frame_aba_dividir_pdf_por_tamanho, 
                                                 placeholder_text="Insira o caminho",
                                                 width=350,
                                                 border_width=1)
    entry_caminho_pasta_dividir_por_tamanho.pack(pady=(0,5))

    # Botão para abrir o caminho especificado
    btn_abrir_pasta_dividir_pdf_por_tamanho = customtkinter.CTkButton(master=frame_aba_dividir_pdf_por_tamanho, 
                                              text="Converter PDF por Tamanho: até 5 MB", 
                                              command=dividir_pdf_por_tamanho_interface)
    btn_abrir_pasta_dividir_pdf_por_tamanho.pack(pady=10)  # Espaçamento vertical (pady)
    config_btn(btn_abrir_pasta_dividir_pdf_por_tamanho)

########## ABA CONTATO WHATSAPP ##########

    # Adicionar uma aba
    aba_contato_por_wpp = tab_janela.add("Contato por Whatsapp")

    # Frame para separação dos botões
    frame_aba_contato_por_wpp = customtkinter.CTkFrame(master=aba_contato_por_wpp, border_width=0)
    frame_aba_contato_por_wpp.pack(padx=0, fill="x")  # Preencher horizontalmente (fill="x") ativa o width acima

    # Cria um rótulo (label) para o campo de entrada do caminho (pasta) para localização das fotos
    label_caminho_pasta_aba_dividir_pdf_por_tamanho = customtkinter.CTkLabel(master=frame_aba_contato_por_wpp,
                                                                   text="Contato:",
                                                                   pady=5,
                                                                   width=140,
                                                                   anchor="w") # Alinha o texto à esquerda
    label_caminho_pasta_aba_dividir_pdf_por_tamanho.pack(pady=(5,0), padx=0)  # Ajusta o padding superior e faz o label preencher a largura disponível

    # Botão para abrir funcionalidade de contatar por WhatsApp
    ''' btn_contato_wpp = customtkinter.CTkButton(master=frame_contatos_sair, text="Contato por WhatsApp", command=toggle_contato_wpp)
    btn_contato_wpp.pack(pady=15)
    config_btn(btn_contato_wpp)'''
    # Cria os entry e o botão, mas não os exibe inicialmente
    entry_gerador_contato_por_wpp = customtkinter.CTkEntry(master=frame_aba_contato_por_wpp,
                                           placeholder_text="(DDD) 90000-0000",
                                           border_width=1)
    entry_gerador_contato_por_wpp.pack(pady=(0,5))
    
    btn_gerador_contato_wpp = customtkinter.CTkButton(master=frame_aba_contato_por_wpp, text="Gerar", command=formata_contato_wpp)
    btn_gerador_contato_wpp.pack(pady=10)
    config_btn(btn_gerador_contato_wpp)

########## FRAME INFERIOR - AJUDA E SUPORTE | SAIR ##########

    # Adiciona um frame fixado na parte de baixo da janela
    frame_contatos_sair = customtkinter.CTkFrame(master=janela)
    frame_contatos_sair.pack(side='bottom', fill='x', padx=0)

    # Configura o layout do frame para usar grid com 3 colunas, sem expandir além do tamanho mínimo necessário (weight=0)
    frame_contatos_sair.grid_columnconfigure(0, weight=0, minsize=10)  # Coluna da esquerda
    frame_contatos_sair.grid_columnconfigure(1, weight=0, minsize=170)  # Coluna do centro
    frame_contatos_sair.grid_columnconfigure(2, weight=0, minsize=180)  # Coluna da direita
    frame_contatos_sair.grid_columnconfigure(3, weight=0, minsize=170)  # Coluna da direita
    frame_contatos_sair.grid_columnconfigure(4, weight=0, minsize=10)  # Coluna da direita

########## COLUNA À ESQUERDA - SWITCH ##########

    # Cria um frame adicional para o switch e o label
    frame_switch = customtkinter.CTkFrame(master=frame_contatos_sair,
                                          fg_color="transparent",
                                          border_width=0)
    frame_switch.grid(row=0, column=1, sticky="nsew")  # O frame se expandirá para preencher completamente a célula do grid
    frame_switch.grid_columnconfigure(0, weight=1)  # Permitir que os botões se expandam

    # Cria um label para o texto acima do switch
    label_switch = customtkinter.CTkLabel(
        master=frame_switch, 
        text=" Alterar tema"
    )
    label_switch.grid(row=0, column=0, pady=(10, 2))

    # Variável para armazenar o estado do switch
    switch_dark_light_mode_var = customtkinter.StringVar(value="on")

    # Cria um switch para alterar o modo escuro e claro
    switch_dark_light_mode = customtkinter.CTkSwitch(
        master=frame_switch,
        command=switch_altera_modo_dark_light, 
        text="",
        variable=switch_dark_light_mode_var,
        onvalue="on",
        offvalue="off"
    )

    def centraliza_switch():
        '''
        CÁLCULO PARA AUTOMATIZAR A CENTRALIZAÇÃO DO SWITCH
        espaco_entre_texto = (tamanho do frame - tamanho do texto) / 2
        espaco_entre_switch = (tamanho do frame - tamanho do switch) / 2
        espaco_centralizar_switch = (espaco_entre_texto - espaco_entre_switch) + ((tamanho do texto / 2) + 11)
        '''
        
        global espaco_centralizar_switch
        tamanho_do_frame = frame_switch.winfo_width()
        tamanho_do_texto = label_switch.winfo_width()
        tamanho_do_switch = 100
        espaco_entre_texto = (tamanho_do_frame - tamanho_do_texto) / 2
        espaco_entre_switch = (tamanho_do_frame - tamanho_do_switch) / 2
        espaco_centralizar_switch = (espaco_entre_texto - espaco_entre_switch) + ((tamanho_do_texto / 2) + 11)
        print(tamanho_do_frame, tamanho_do_texto, tamanho_do_switch)
        print(espaco_entre_texto, espaco_entre_switch, espaco_centralizar_switch)

        # Grid do switch
        switch_dark_light_mode.grid(row=1, column=0, padx=(espaco_centralizar_switch, 0), pady=(0, 10))
        
    # Adia a medição em 100 milissegundos, para que a interface seja criada e as medições dos pixels sejam corretas
    janela.after(100, centraliza_switch)  

########## ESPAÇO CENTRAL - BOTÕES ##########

    # Cria um frame adicional para os botões de "Ajuda e Suporte" e "Sair"
    frame_contatos_sair_centralizado = customtkinter.CTkFrame(master=frame_contatos_sair,
                                                              fg_color="transparent",
                                                              border_width=0,
                                                              height=76)
    frame_contatos_sair_centralizado.grid(row=0, column=2, sticky="nsew")  # O frame se expandirá para preencher completamente a célula do grid
    frame_contatos_sair_centralizado.grid_columnconfigure(0, weight=1)  # Permitir que os botões se expandam

    # Cria o botão de suporte
    btn_ajuda_e_suporte = customtkinter.CTkButton(master=frame_contatos_sair_centralizado,
                                        text="Ajuda e Suporte",
                                        fg_color="#035397",
                                        text_color="white",
                                        corner_radius=52,
                                        command=toggle_ajuda,
                                        width=160)
    btn_ajuda_e_suporte.grid(row=0, column=0, pady=(5,0))

########## ESPAÇO À ESQUERDA - BOTÕES SOBRE E CONTATO PROGRAMADOR ##########

    # Cria um frame adicional para os botões "Sobre o Programa" e "Contate o Programador"
    frame_contatos_sair_esquerda = customtkinter.CTkFrame(master=frame_contatos_sair,
                                                          fg_color="transparent",
                                                          border_width=0,
                                                          height=76,
                                                          width=170)
    frame_contatos_sair_esquerda.grid(row=0, column=3, sticky="nsew")  # O frame se expandirá para preencher completamente a célula do grid
    frame_contatos_sair_esquerda.grid_columnconfigure(0, weight=1)  # Permitir que os botões se expandam

    # Cria os botões, mas não os exibe inicialmente
    btn_versao = customtkinter.CTkButton(master=frame_contatos_sair_esquerda, 
                                         text="Sobre o programa",
                                         width=160,
                                         fg_color="#035397",
                                         text_color="white",
                                         corner_radius=52,
                                         command=versão,
                                         )

    btn_contato_programador = customtkinter.CTkButton(master=frame_contatos_sair_esquerda,
                                      text="Contate o programador",  # Texto com 159px de largura
                                      width=160,
                                      fg_color="#035397",
                                      text_color="white",
                                      corner_radius=52,
                                      command=lambda: webbrowser.open("https://wa.me/5571988500008"))

    # Botão para fechar o programa
    btn_sair = customtkinter.CTkButton(
        master=frame_contatos_sair_centralizado,
        text="Sair",
        fg_color="#B31312",
        hover_color="Dark red",
        text_color=("white"),
        corner_radius=52,
        command=janela.destroy,
        width=160)
    btn_sair.grid(row=1, column=0, pady=(10, 5))  # Ajusta o padding conforme necessário

    # Retorna a dimensão (largura e altura) do especificado na função print_dimensions
    janela.after(2000, print_dimensão)  # Adia a medição em 100 milissegundos

    # Inicia o loop principal da interface gráfica
    janela.mainloop()

if __name__ == "__main__":
    # URL do arquivo no Github
    url_arquivo = "https://raw.githubusercontent.com/dawilao/learning_python/main/data.txt"

    # Chama a função para obter os dados
    dados_login = obter_dados_login(url_arquivo)
    
    # Biiblioteca de dados de login integrada ao programa
    lista_logins_padroes = {
        "dawison": "624426",
        "cardoso": "0123", 
        "lucas": "BBMP5988",
        # "": "",
    }

    # Atualiza a biblioteca lista_logins_padroes com os dados obtidos do txt no Github
    if dados_login:
        lista_logins_padroes.update(dados_login)
        ''' print("Biblioteca de logins atualizada:")
        for usuario, senha in lista_logins_padroes.items():
            print(f"Usuário: {usuario}, Senha: {senha}")
    else:
        print("Não foi possível obter os dados de login do arquivo.")  '''

    # Configuração da interface gráfica principal, com título e tamanho da janela
    janela_login = customtkinter.CTk()
    janela_login.title("Login")
    janela_login.geometry("250x270")

    # Definir modo escuro (dark), modo claro (light), ou definido pelo sistems (system)
    customtkinter.set_appearance_mode("system")

    # Cria um rótulo (label) para o campo de entrada do nome de usuário
    label_usuario = customtkinter.CTkLabel(master=janela_login, text="Usuário:", anchor="w")
    label_usuario.pack(pady=(15,0), padx=57, fill="x")

    # Cria um campo de entrada (Entry) para o usuário digitar seu nome de usuário
    entry_usuario = customtkinter.CTkEntry(master=janela_login,
                                           placeholder_text="Insira o usuário",
                                           border_width=1)
    entry_usuario.pack(pady=(0,15))

    # Cria um rótulo (label) para o campo de entrada da senha
    label_senha = customtkinter.CTkLabel(master=janela_login, text="Senha:", anchor="w")
    label_senha.pack(pady=0, padx=57, fill="x")

    # Cria um campo de entrada (Entry) para o usuário digitar sua senha
    entry_senha = customtkinter.CTkEntry(master=janela_login, 
                                         show='*',
                                         placeholder_text="Insira a senha",
                                         border_width=1)
    entry_senha.pack(pady=(0,20))

    # Cria um campo de entrada (Entry) para o usuário digitar sua senha. 
    # O parâmetro 'show' é usado para esconder a senha com asteriscos
    botao_login = customtkinter.CTkButton(master=janela_login,
                                          text="Login",
                                          command=validacao_login)
    config_btn(botao_login)
    botao_login.pack(pady=(0,15))
    
    janela_login.bind('<Return>', lambda enter: botao_login.invoke())

    # Botão para fechar o programa
    botao_sair = customtkinter.CTkButton(master=janela_login,
                                         text="Sair",
                                         fg_color="#B31312",
                                         hover_color="Dark red",
                                         text_color=("black", "white"),
                                         corner_radius=32,
                                         command=janela_login.destroy)
    
    botao_sair.pack(pady=(0,15))

    janela_login.mainloop()