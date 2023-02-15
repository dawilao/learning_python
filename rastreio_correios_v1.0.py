''' Programa para rastrear pacotes nos Correios
    Versão: 1.0
'''

from PyRastreamentoCorreios import rastrear
import pandas as pd
import re

while True:
    cod_rastreio = input('Digite o código de rastreamento: ') 
    valid_pattern = re.compile("^[A-Za-z]{2}[0-9]{9}[A-Za-z]{2}$")
    '''Nesta validação, verificamos se o código de rastreamento começa com duas letras maiúsculas ([A-Z]{2}), 
    seguido de nove dígitos ([0-9]{9}) e termina com mais duas letras maiúsculas ([A-Z]{2}).'''
    if valid_pattern.match(cod_rastreio):
        break
    else:
        print("Código de rastreamento inválido. Por favor, tente novamente.")

statusList = rastrear(cod_rastreio)
# print(statusList)

if len(statusList['status_list']) == 0:
    print('Objeto não encontrado na base de dados dos Correios.')
else:
    df = pd.DataFrame.from_dict(statusList['status_list'])

    df['status'] = df['status'].str.replace("Status: ", "")  #Substitui a palavra "Status: " da célula
    df['data'] = df['data'].str.replace("Data  : ", "")
    df['data'] = df['data'].str.replace("| Hora:", "", regex=True)
    df['local'] = df['local'].str.replace("Local: ", "")
    df.fillna("", inplace=True)  #preencher todas as células com NaN com uma string vazia

    print('\nSeguem os ultimos últimos status do pacote:')
    
    for i in range(len(df)):
        print(f"{df.iloc[i]['data']}: {df.iloc[i]['status']} | {df.iloc[i]['local']}")

    #print(df.head(2).to_string(index=False))  #Printa as duas primeiras linhas da tabela

    #print(df.to_string()) #Imprime toda a tabela
    #df.to_excel("status_table.xlsx", index=False)  #Gera um arquivo xlsx ta tabela
    #print(statusList['status_list'][0]['status'])

    # Código teste: 'NA869896819BR'

input('\nTecle ENTER para sair')