#Algoritmo que gera números aleatórios de 1 a 6, como um dado.

from random import randint, randrange
import time

sim = ['1', 'Sim', 'sim', 's']

print('\nBem-vindo ao dado virtual!')
quest = input('Jogar o dado?\n') #pergunta inicial

if quest in sim:
    #imprimindo o nº aleatório
    print('Jogando... ', randrange(1, 6), '\n')
    jog_dnv = input(str('Jogar o dado novamente? '))
    while jog_dnv in sim:
        print('Jogando... ', randrange(1, 7), '\n')
        jog_dnv = input(str('Jogar o dado novamente? '))
    else:
        print('Adeus!\n')
else:
    print('Adeus!\n')
