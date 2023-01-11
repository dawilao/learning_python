from random import randint, randrange
import time

print ('JOGO DE MATEMÁTICA 1.0')
print('#######################')

def saindo():
    print('\nObrigado por jogar!')
    time.sleep(3) #sleep por 3 seg

sim = ['1', 'Sim', 'sim', 's']
inst = ['2', 'Instrucoes', 'instrucoes', 'Instruções', 'instruções']
sair = ['Sair', 'sair']

num_question = 1
pontuacao = 0

print('\nINSTRUÇÕES')
print('#######################')
print('Acerte o máximo de questões que conseguir.')
print('Evite digitar letras nas questões.')

iniciar = input('\nIniciar? ')
print('Iniciando...')

while iniciar in sim:
    operacao = randint(1,2)
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
    else:
        result = x - y
        resp = input('\n' + str(x) + ' - ' + str(y) + ' = ')  
        if resp == str(result):
            pontuacao += 1
            print('Acertou! :)\nPontuação:', pontuacao)
        else:
            pontuacao -= 1
            print('Errou :(\nPontuação:', pontuacao)
        iniciar = input('Continuar? ')
else:
    saindo()

'''Fechando o loop
elif resp in sair:
            saindo()
            break;
'''