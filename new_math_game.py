'''
JOGO DE MATEMÁTICA V1.9 (12/01/2023)
'''

from random import randint, randrange
import time

def menu_principal():
    print ('JOGO DE MATEMÁTICA')
    print('#######################')
    print('OBJETIVO: Acerte o máximo de questões que conseguir.')
    print('Para INICIAR, digite iniciar.')
    print('Para ver as INSTRUÇÕES, digite instruções.')

def saindo():
    print('\nObrigado por jogar!')
    time.sleep(3) #sleep por 3 seg

def instrucoes():
    print('\nINSTRUÇÕES')
    print('#######################')
    print('Acerte o máximo de questões que conseguir.')

sim = ['1', 'Sim', 'sim', 's', 'S', 'iniciar', 'INICIAR', 'Iniciar']
inst = ['2', 'Instrucoes', 'instrucoes', 'Instruções', 'instruções', 'inst']
sair = ['Sair', 'sair', 'SAIR', "não", 'n', 'N', 'nao', 'NÃO']
selec_vidas = ['vidas', 'v']

num_question = 1
pontuacao = 0
iniciar = True
rodada = 1
vidas = 3

menu_principal()
while iniciar == True:
    iniciar = input('> ')
    if iniciar in sim:        
        print("rodar jogo")
    else:
        break
else:
    saindo()