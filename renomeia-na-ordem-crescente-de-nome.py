import os

# Pasta onde estão os arquivos
pasta = input("Informe o caminho para a pasta: ")

# Listar os arquivos na pasta e ordená-los por nome
arquivos = os.listdir(pasta)
arquivos.sort()

# Verificar os arquivos já renomeados e determinar o próximo número disponível
arquivos_renomeados = set()
for arquivo in arquivos:
    nome, extensao = os.path.splitext(arquivo)
    if nome.isdigit() and extensao != '':
        arquivos_renomeados.add(int(nome))

# Renomear os arquivos de acordo com a ordem crescente de nome
for i, arquivo in enumerate(arquivos, start=1):
    nome, extensao = os.path.splitext(arquivo)
    if not nome.isdigit() or extensao == '':
        novo_nome = f"{i:03d}"
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, f"{novo_nome}{extensao}")
        
        # Verificar se o novo nome já está em uso
        while os.path.exists(caminho_novo) or int(novo_nome) in arquivos_renomeados:
            i += 1
            novo_nome = f"{i:03d}"
            caminho_novo = os.path.join(pasta, f"{novo_nome}{extensao}")

        os.rename(caminho_antigo, caminho_novo)
        arquivos_renomeados.add(int(novo_nome))
        print(f"Arquivo {arquivo} renomeado para {novo_nome}{extensao}")

input("")
