'''
JOGO DE MATEMÁTICA V1.9 (12/01/2023)
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

sim = ['1', 'Sim', 'sim', 's', 'S']
inst = ['2', 'Instrucoes', 'instrucoes', 'Instruções', 'instruções', 'inst']
sair = ['Sair', 'sair', 'SAIR']

num_question = 1
pontuacao = 0
iniciar = 0
rodada = 1
vidas = 3

instrucoes()

while iniciar == 0:
    iniciar = input('\nIniciar? ')
    if iniciar in sim or iniciar in inst:
        while iniciar in sim:
            print('Iniciando...')
            while iniciar in sim and vidas > 0:
                print('\nRodada', rodada, ' Vidas:', vidas, ' Pontuação:', pontuacao)
                operacao = randint(1, 4)
                operacao = 3
                x = randint(0, 50)
                y = randint(0, 50)
                if operacao == 1:
                    result = x + y
                    while True:
                        try:
                            resp = int(input('' + str(x) + ' + ' + str(y) + ' = '))
                            break
                        except ValueError:
                            print('Apenas números.')
                    if str(resp) == str(result):
                        pontuacao += 1
                        print('Acertou! :)')
                        rodada += 1
                    else:
                        pontuacao -= 1
                        print('Errou :( Você perdeu uma vida.\nResposta correta:', result)
                        rodada += 1
                        vidas -= 1
                    if vidas == 0:
                        print('Você não tem mais vidas.')
                        break
                    else:
                        iniciar = input('Continuar? ')
                elif operacao == 2:
                    if y > x:
                        result = y - x
                        while True:
                            try:
                                resp = int(input('' + str(y) + ' - ' + str(x) + ' = '))
                                break
                            except ValueError:
                                print('Apenas números.')
                    else:
                        result = x - y
                        while True:
                            try:
                                resp = int(input('' + str(x) + ' - ' + str(y) + ' = '))
                                break
                            except ValueError:
                                print('Apenas números.')
                    if str(resp) == str(result):
                        pontuacao += 1
                        print('Acertou! :)')
                        rodada += 1
                    else:
                        pontuacao -= 1
                        print('Errou :( Você perdeu uma vida.\nResposta correta:', result)
                        rodada += 1
                        vidas -= 1
                    if vidas == 0:
                        print('Você não tem mais vidas.')
                        break
                    else:
                        iniciar = input('Continuar? ')
                elif operacao == 3:
                    x = randint(0, 10)
                    y = randint(0, 10)
                    result = x * y
                    while True:
                        try:
                            resp = int(input('' + str(x) + ' x ' + str(y) + ' = '))
                            break
                        except ValueError:
                            print('Apenas números.')
                    if str(resp) == str(result):
                        pontuacao += 1
                        print('Acertou! :)')
                        rodada += 1
                    else:
                        pontuacao -= 1
                        print('Errou :( Você perdeu uma vida.\nResposta correta:', result)
                        rodada += 1
                        vidas -= 1
                    if vidas == 0:
                        print('Você não tem mais vidas.')
                        break
                    else:
                        iniciar = input('Continuar? ')
                else:
                    x = randint(0, 100)
                    y = randint(1, 100)
                    resto = x % y
                    while resto != 0:
                        x = randint(0, 100)
                        y = randint(1, 100)
                        resto = x % y
                    result = x // y
                    while True:
                        try:
                            resp = int(input('' + str(x) + ' / ' + str(y) + ' = '))
                            break
                        except ValueError:
                            print('Apenas números.')
                    if str(resp) == str(result):
                        pontuacao += 1
                        print('Acertou! :)')
                    else:
                        pontuacao -= 1
                        print('Errou :(\nResposta correta:', result)
                        rodada += 1
                        vidas -= 1
                    if vidas == 0:
                        print('Você não tem mais vidas.')
                        break
                    else:
                        iniciar = input('Continuar? ')
            if vidas == 0:
                print('Game over\nPontuação final:', pontuacao)
                iniciar = 'n'
                break
    while iniciar in inst:
        instrucoes()
        iniciar = 0
        continue
    if iniciar in sair:
        print('Pontuação final:', pontuacao)
        saindo()
        break
        '''Fechando o loop
            elif resp in sair:
                saindo()
                break;  '''
else:
    saindo()
