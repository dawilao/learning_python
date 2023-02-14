''' Programa para rastrear pacotes nos Correios
    Versão: 1.5
'''

from PyRastreamentoCorreios import rastrear
import pandas as pd
import re
import os

directory = 'C:\\Users\\dawis\\Documents'
filename = 'ultimos_rastreamentos.txt'
file_path = directory + "\\" + filename
if not os.path.exists(directory):
    os.makedirs(directory)

def valida_cod_rastreio(cod_rastreio):
    '''Nesta validação, verificamos se o código de rastreamento começa com duas letras maiúsculas ([A-Z]{2}), 
    seguido de nove dígitos ([0-9]{9}) e termina com mais duas letras maiúsculas ([A-Z]{2}).'''
    valid_cod = re.compile("^[A-Za-z]{2}[0-9]{9}[A-Za-z]{2}$")
    if valid_cod.match(cod_rastreio):
        return True
    else:
        return False

def edita_arq():
    # Abre o arquivo para escrita
    with open(os.path.join(directory, filename), "a") as f:
        # Escreve as informações
        f.write(f"Código de rastreio: {cod_rastreio}\n")
        f.write(f"Nome: {nome_pct}\n")
        f.write(f"Último status: {df.iloc[0]['status']}\n")
        f.write(f"Data e hora: {df.iloc[0]['data']}\n\n")

def verif_ultimo_rastreio():
    if os.path.isfile(file_path) == True:
        with open(os.path.join(directory, filename), "r") as f:
            lines = f.readlines()
            if lines[0] != []:
                codigo_arq = lines[0].split(": ")[1].strip()
                nome_arq = lines[1].split(": ")[1].strip()
                rerastrear = input(f"Deseja rastrear novamente o código {codigo_arq} para {nome_arq}? > ")
                if rerastrear.upper() == "S":
                    return codigo_arq, nome_arq
    else:
        return 0, 0

while True:
    cod_rastreio, nome_arq = verif_ultimo_rastreio()
    if cod_rastreio != 0:
        # Código veio do arquivo
        rastrear(cod_rastreio)
        nome_pct = nome_arq
        break
    else:
        # Código veio do usuário
        cod_rastreio = input("Digite o código de rastreamento: ")
        if valida_cod_rastreio(cod_rastreio) == True:
            rastrear(cod_rastreio)
            nome_pct = input('Dê um nome ao código de rastreio: ')
            break
        else:
            print("Código de rastreamento inválido. Por favor, tente novamente.")

statusList = rastrear(cod_rastreio)

if len(statusList['status_list']) == 0:
    print('Objeto não encontrado na base de dados dos Correios.')
else:
    df = pd.DataFrame.from_dict(statusList['status_list'])

    df['status'] = df['status'].str.replace("Status: ", "")  #Substitui a palavra "Status: " da célula
    df['data'] = df['data'].str.replace("Data  : ", "")
    df['data'] = df['data'].str.replace("| Hora:", "", regex=True)
    df['local'] = df['local'].str.replace("Local: ", "")
    df.fillna("", inplace=True)  #preencher todas as células com NaN com uma string vazia

    data = df.iloc[0]['data']  #armazena o conteúdo da primeira linha da coluna "data"

    print('\nSeguem os ultimos últimos status do pacote:')
    
    for i in range(len(df)):
        print(f"{df.iloc[i]['data']}: {df.iloc[i]['status']} | {df.iloc[i]['local']}")

    #print(df.head(2).to_string(index=False))  #Printa as duas primeiras linhas da tabela

    #print(df.to_string()) #Imprime toda a tabela
    #df.to_excel("status_table.xlsx", index=False)  #Gera um arquivo xlsx ta tabela
    #print(statusList['status_list'][0]['status'])

    # Código teste: 'NA869896819BR'

edita_arq()

input('\nTecle ENTER para sair')