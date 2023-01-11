'''
JOGO DE MATEMÁTICA V1.2 (11/01/2023)
'''

from random import randint, randrange
import time

print ('JOGO DE MATEMÁTICA')
print('#######################')

def saindo():
    print('\nObrigado por jogar!')
    time.sleep(3) #sleep por 3 seg

def instrucoes():
    print('\nINSTRUÇÕES')
    print('#######################')
    print('Acerte o máximo de questões que conseguir.')
    print('Evite digitar letras nas questões.')

def pontua():
    pontuacao += 1
    print('Acertou! :)\nPontuação:', pontuacao)

def nao_pontua():
    pontuacao -= 1
    print('Errou :(\nPontuação:', pontuacao)

sim = ['1', 'Sim', 'sim', 's']
inst = ['2', 'Instrucoes', 'instrucoes', 'Instruções', 'instruções', 'inst']
sair = ['Sair', 'sair']

num_question = 1
pontuacao = 0
iniciar = 0

instrucoes()

while iniciar == 0:
    iniciar = input('\nIniciar? ')
    if iniciar in sim or iniciar in inst:
        while iniciar in sim:    
            print('Iniciando...')
            while iniciar in sim:
                operacao = randint(1, 3)
                x = randint(0, 20)
                y = randint(0, 20)
                if operacao == 1:
                    result = x + y
                    resp = input('\n' + str(x) + ' + ' + str(y) + ' = ')
                    if resp == str(result):
                        pontuacao += 1
                        print('Acertou! :)\nPontuação:', pontuacao)
                    else:
                        pontuacao -= 1
                        print('Errou :(\nPontuação:', pontuacao)
                    iniciar = input('Continuar? ')
                if operacao == 2:
                    result = x - y
                    resp = input('\n' + str(x) + ' - ' + str(y) + ' = ')  
                    if resp == str(result):
                        pontua()
                    else:
                        nao_pontua()
                    iniciar = input('Continuar? ')
                if operacao == 3:
                    x = randint(0, 10)
                    y = randint(0, 10)
                    result = x * y
                    resp = input('\n' + str(x) + ' x ' + str(y) + ' = ')
                    if resp == str(result):
                        pontuacao += 1
                        print('Acertou! :)\nPontuação:', pontuacao)
                    else:
                        pontuacao -= 1
                        print('Errou :(\nPontuação:', pontuacao)
                    iniciar = input('Continuar? ')
                ''' else:
                    result = x / y
                    resp = input('\n' + str(x) + ' / ' + str(y) + ' = ')
                    if resp == str(result):
                        pontuacao += 1
                        print('Acertou! :)\nPontuação:', pontuacao)
                    else:
                        pontuacao -= 1
                        print('Errou :(\nPontuação:', pontuacao)
                    iniciar = input('Continuar? ')'''
                    
    while iniciar in inst:
        print('elif instrucoes')
        instrucoes()
        iniciar = 0
        continue

    if iniciar in sair:
        print('elif saindo')
        saindo()
        break;
        '''Fechando o loop
            elif resp in sair:
                saindo()
                break;  '''
else:
    print('a')
    saindo()
