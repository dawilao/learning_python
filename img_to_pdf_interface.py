import tkinter as tk
from tkinter import filedialog, messagebox
import os, errno
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# Função para mostrar a versão do programa
def versão():
    # Exibe uma mensagem com informações sobre a versão do programa
    messagebox.showinfo("Versão", "Programa criado por: Dawison Nascimento\nVersão 3.0\nUltima alteração em 13/08/2024, às 13:48")

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
def dividir_pdf_1(diretorio, diretorio_saida):
    nome_arquivo = os.path.splitext(os.path.basename(diretorio))[0]
    pdf = PdfReader(diretorio)
    
    # Para cada página do PDF, cria um novo arquivo PDF com a página única
    for pagina in range(len(pdf.pages)):
        escreve_pdf = PdfWriter()
        escreve_pdf.add_page(pdf.pages[pagina])

        nome_arquivo_saida = '{}_{}.pdf'.format(nome_arquivo, pagina)
        nome_completo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)
        
        with open(nome_completo_saida, 'wb') as saida:
            escreve_pdf.write(saida)
        
        print('Criado: {}'.format(nome_arquivo_saida))
    messagebox.showinfo("Sucesso", "Divisão de PDF concluída.")

# Função para abrir o seletor de diretório
def selecionar_diretorio():
    return filedialog.askdirectory(title="Selecione o Diretório")

# Função chamada ao clicar no botão para converter imagens em PDF
def converter_imagens():
    diretorio = selecionar_diretorio()
    if diretorio:
        output_pdf = os.path.join(diretorio, "EXECUÇÃO.pdf")
        convert_to_pdf(diretorio, output_pdf)

# Função chamada ao clicar no botão para criar pastas padrão
def criar_pastas_interface():
    diretorio = selecionar_diretorio()
    if diretorio:
        criar_pastas(diretorio)

# Função chamada ao clicar no botão para dividir um PDF
def dividir_pdf_interface():
    pasta = selecionar_diretorio()
    if pasta:
        arquivo = filedialog.askopenfilename(title="Selecione o PDF", filetypes=[("PDF files", "*.pdf")])
        if arquivo:
            dividir_pdf_1(arquivo, pasta)

# Configuração da interface gráfica principal, com título e tamanho da janela
janela = tk.Tk()
janela.title("img_to_pdf")
janela.geometry("200x200")

# Botão para converter imagens em PDF
btn_converter = tk.Button(janela, text="Converter Imagens para PDF", command=converter_imagens)
btn_converter.pack(pady=10)

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
