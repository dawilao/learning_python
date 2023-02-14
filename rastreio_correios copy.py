''' Programa para rastrear pacotes nos Correios
    Versão: 1.5
'''

from PyRastreamentoCorreios import rastrear
from termcolor import colored  #print(colored('Error Test!!!', 'red'))
import pandas as pd
import re
import os

directory = os.path.join(os.path.expanduser("~"), "Documents")
# directory = 'C:\\Users\\dawis\\Documents'
filename = 'ultimos_rastreamentos.txt'
file_path = os.path.join(directory, filename)
print(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)

def menu_inicial():
    print('#########################################')
    print('          RASTREAMENTO CORREIOS          ')
    print('#########################################\n')


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
    with open(os.path.join(directory, filename), "w") as f:
        '''ara reescrever as informações no arquivo, em vez de adicionar novas informações abaixo da última linha, 
        você precisa abrir o arquivo no modo de escrita ('w') em vez de modo de anexação ('a') na função edita_arq().
        Isso irá substituir todo o conteúdo do arquivo existente pelo novo conteúdo que você está escrevendo'''
        # Escreve as informações
        f.write(f"Código de rastreio: {cod_rastreio}\n")
        f.write(f"Nome: {nome_pct}\n")
        f.write(f"Último status: {df.iloc[0]['status']}\n")
        f.write(f"Data e hora: {df.iloc[0]['data']}")

def verif_ultimo_rastreio():
    if os.path.isfile(file_path) == True:
        with open(os.path.join(directory, filename), "r") as f:
            lines = f.readlines()
            if lines[0] != []:
                codigo_arq = lines[0].split(": ")[1].strip()
                nome_arq = lines[1].split(": ")[1].strip()
                rerastrear = input("Foi localizado seu último código rastreado!\n"
                f"Deseja rastrear novamente o pacote {nome_arq} ({codigo_arq})? > ")
                while not rerastrear.upper() == ["S", "N"]:
                    if rerastrear.upper() == "S":
                        return codigo_arq, nome_arq
                    elif rerastrear.upper() == "N":
                        return "NOVO", "NOVO"
                    else:
                        print(colored('Resposta incorreta.', 'red'))
                        rerastrear = input(f"Deseja rastrear novamente o pacote {nome_arq} ({codigo_arq})? > ")
    else:
        return "NOVO", "NOVO"

menu_inicial()
cod_rastreio, nome_arq = verif_ultimo_rastreio()

if cod_rastreio != "NOVO":
    # Código veio do arquivo
    rastrear(cod_rastreio)
    nome_pct = nome_arq
    statusList = rastrear(cod_rastreio)
    while len(statusList['status_list']) == 0:
        print('Objeto não encontrado na base de dados dos Correios.')
        cod_rastreio = input("Digite o código de rastreamento correto: ")
        statusList = rastrear(cod_rastreio)
        nome_pct = input('Dê um nome ao código de rastreio: ')
else:
    # Código veio do usuário
    while valida_cod_rastreio(cod_rastreio) == False:
        cod_rastreio = input("Digite o código de rastreamento: ")
        statusList = rastrear(cod_rastreio)
        while len(statusList['status_list']) == 0:
            print('Objeto não encontrado na base de dados dos Correios.')
            cod_rastreio = input("Digite o código de rastreamento: ")
            statusList = rastrear(cod_rastreio)
        else:    
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

    print(f'\nSeguem os ultimos últimos status do pacote do código {cod_rastreio}:')
    
    for i in range(len(df)):
        print(f"{df.iloc[i]['data']}: {df.iloc[i]['status']} | {df.iloc[i]['local']}")

    #print(df.head(2).to_string(index=False))  #Printa as duas primeiras linhas da tabela

    #print(df.to_string()) #Imprime toda a tabela
    #df.to_excel("status_table.xlsx", index=False)  #Gera um arquivo xlsx ta tabela
    #print(statusList['status_list'][0]['status'])

    # Código teste: 'NA869896819BR', 'NL383239602BR'

edita_arq()

input('\nTecle ENTER para sair')