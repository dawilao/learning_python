#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script para manipulação de arquivos PDF e JPG.
- Converte imagens JPG em um PDF.
- Cria pastas padrão para organização de arquivos.
- Divide um arquivo PDF em várias páginas individuais.

Interface gráfica desenvolvida usando Tkinter.
"""

__author__ = "Dawison Nascimento"
__license__ = "Sem licensa definida"
__version__ = "3.3.0"
__maintainer__ = "Dawison Nascimento"

import tkinter as tk
from tkinter import filedialog, messagebox
import os, errno, requests
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# Função para mostrar a versão do programa
def versão():
    # Exibe uma mensagem com informações sobre a versão do programa
    messagebox.showinfo("Versão", f"Programa criado por {__author__}\nVersão {__version__}\nUltima alteração em 14/08/2024, às 08:39")

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
    diretorio = entry_caminho_pasta.get()

    if os.path.exists(diretorio):
        output_pdf = os.path.join(diretorio, "EXECUÇÃO.pdf")
        convert_to_pdf(diretorio, output_pdf)
    else:
        diretorio = selecionar_diretorio()

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

    if os.path.exists(diretorio):
        criar_pastas(diretorio)
    else:
        diretorio = selecionar_diretorio()

# Função chamada ao clicar no botão para dividir um PDF
def dividir_pdf_interface():
    arquivo = filedialog.askopenfilename(title="Abrir", filetypes=[("PDF files", "*.pdf")])
    if arquivo:
        dividir_pdf_1(arquivo)

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

def janela_principal():
    global entry_caminho_pasta

    # Configuração da interface gráfica principal, com título e tamanho da janela
    janela = tk.Tk()
    janela.title("img_to_pdf")
    janela.geometry("350x300")
 
    # Cria um rótulo (label) para o campo de entrada do caminho (pasta) para localização das fotos
    label_caminho_pasta = tk.Label(janela, text="Caminho:")
    label_caminho_pasta.pack(pady=0)

    # Cria um campo de entrada (Entry) para o usuário digitar o caminho (pasta) para localização das fotos
    entry_caminho_pasta = tk.Entry(janela, width=45)
    entry_caminho_pasta.pack(pady=0)

    # Botão para converter imagens em PDF
    btn_converter = tk.Button(janela, text="Converter Imagens para PDF", command=converter_imagens)
    btn_converter.pack(pady=10)  # Espaçamento vertical (pady) de 10 pixels

    # Botão para criar pastas padrão
    btn_criar_pastas = tk.Button(janela, text="Criar Pastas Padrão", command=criar_pastas_interface)
    btn_criar_pastas.pack(pady=10)

    # Botão para dividir um PDF em páginas individuais
    btn_dividir_pdf = tk.Button(janela, text="Dividir PDF", command=dividir_pdf_interface)
    btn_dividir_pdf.pack(pady=10)

    # Botão para exibir a versão do programa
    btn_versao = tk.Button(janela, text="Versão", command=versão)
    btn_versao.pack(pady=10)

    # Botão para fechar o programa
    btn_sair = tk.Button(janela, text="Sair", command=janela.destroy)
    btn_sair.pack(pady=10)

    # Inicia o loop principal da interface gráfica
    janela.mainloop()

if __name__ == "__main__":
    # URL do arquivo no Github
    url_arquivo = "https://raw.githubusercontent.com/dawilao/learning_python/main/data.txt"

    # Chama a função para obter os dados
    dados_login = obter_dados_login(url_arquivo)
    
    # Biiblioteca de dados de login integrada ao programa
    lista_logins_padroes = {
        "d": "d",
        "dawison": "dawilao",
        "cardoso": "0123", 
        "lucas": "BBMP5988"
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
    janela_login = tk.Tk()
    janela_login.title("Login")
    janela_login.geometry("250x260")

    # Cria um rótulo (label) para o campo de entrada do nome de usuário
    label_usuario = tk.Label(janela_login, text="Usuário:")
    label_usuario.pack(pady=5)

    # Cria um campo de entrada (Entry) para o usuário digitar seu nome de usuário
    entry_usuario = tk.Entry(janela_login)
    entry_usuario.pack(pady=5)

    # Cria um rótulo (label) para o campo de entrada da senha
    label_senha = tk.Label(janela_login, text="Senha:")
    label_senha.pack(pady=5)

    # Cria um campo de entrada (Entry) para o usuário digitar sua senha
    entry_senha = tk.Entry(janela_login, show='*')
    entry_senha.pack(pady=5)

    # Cria um campo de entrada (Entry) para o usuário digitar sua senha. 
    # O parâmetro 'show' é usado para esconder a senha com asteriscos
    botao_login = tk.Button(janela_login, text="Login", command=validacao_login)
    botao_login.pack(pady=20)
    
    # Associa o evento de pressionar 'Enter' ao botão de login
    janela_login.bind('<Return>', lambda enter: botao_login.invoke())

    # Botão para fechar o programa
    botao_sair = tk.Button(janela_login, text="Sair", command=janela_login.destroy)
    botao_sair.pack(pady=5)

    janela_login.mainloop()