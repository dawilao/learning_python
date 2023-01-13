'''
JOGO DE MATEMÁTICA V1.9 (12/01/2023)
'''

from random import randint, randrange
import time
import os

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

def nao_iniciar():
    iniciar = True
    print('Voltando...')
    time.sleep(1.3)
    os.system('cls') # Clearing the Screen
    return

def perdeu():
    iniciar == True
    print('Game over. Você não tem mais vidas.\nPontuação final:', pontuacao, '\n')
    print('Voltando ao menu principal...')
    time.sleep(4)
    os.system('cls') # Clearing the Screen
    rodada = 0
    return True

sim = ['1', 'Sim', 'sim', 's', 'S', 'iniciar', 'INICIAR', 'Iniciar']
inst = ['2', 'Instrucoes', 'instrucoes', 'Instruções', 'instruções', 'inst']
sair = ['Sair', 'sair', 'SAIR']
nao = ["não", 'n', 'N', 'nao', 'NÃO']
selec_vidas = ['vidas', 'v']

pontuacao = 0
iniciar = True
vidas = vidas_selecionadas = 1
rodada = 1

while iniciar == True:
    menu_principal()
    iniciar = input('> ')
    while iniciar not in sim and inst and selec_vidas: #AND, não OR
        if iniciar in sair:
            break
        while iniciar in inst:
            instrucoes()
            iniciar = input('\nIniciar jogo? ')
        while iniciar in selec_vidas:
            while True:
                try:
                    vidas_selecionadas = int(input('Selecione a quantidade de vidas (1 ou 3): '))
                    break
                except ValueError:
                    print('Apenas números.')
            iniciar = input('\nIniciar jogo? ') # FORA do try 
        if iniciar in nao: # if para voltar ao menu/primeiro while
            iniciar = True
            print('Voltando...')
            time.sleep(1.3)
            os.system('cls') # Clearing the Screen
            break
        elif iniciar in sair:
            break
        elif iniciar in sim:
            continue
        else:
            iniciar = input('Tente novamente.\n> ')
    else:
        while iniciar in sim:
            print('Iniciando...')
            vidas = vidas_selecionadas
            rodada = 1
            pontuação = 0
            while iniciar in sim and vidas > 0:
                print('\nRodada', rodada, ' Vidas:', vidas, ' Pontuação:', pontuacao)
                operacao = randint(1, 4)
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
                        iniciar = True
                        perdeu()
                        print(iniciar)
                        break
                    else:
                        iniciar = input('Continuar? ')
                    while iniciar not in sim:
                        if iniciar in nao or iniciar in sair:
                            iniciar = True
                            print('Voltando ao menu principal...')
                            time.sleep(4)
                            os.system('cls') # Clearing the Screen
                            break
                        else:
                            iniciar = input('Tente novamente. Continuar? > ')
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
                        iniciar = True
                        print('Game over. Você não tem mais vidas.\nPontuação final:', pontuacao, '\n')
                        print('Voltando ao menu principal...')
                        time.sleep(4)
                        os.system('cls') # Clearing the Screen
                        break
                    else:
                        iniciar = input('Continuar? ')
                    while iniciar not in sim:
                        if iniciar in nao or iniciar in sair:
                            iniciar = True
                            print('Voltando ao menu principal...')
                            time.sleep(4)
                            os.system('cls') # Clearing the Screen
                            break
                        else:
                            iniciar = input('Tente novamente. Continuar? > ')
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
                        iniciar = True
                        print('Game over. Você não tem mais vidas.\nPontuação final:', pontuacao, '\n')
                        print('Voltando ao menu principal...')
                        time.sleep(4)
                        os.system('cls') # Clearing the Screen
                        break
                    else:
                        iniciar = input('Continuar? ')
                    while iniciar not in sim:
                        if iniciar in nao or iniciar in sair:
                            iniciar = True
                            print('Voltando ao menu principal...')
                            time.sleep(4)
                            os.system('cls') # Clearing the Screen
                            break
                        else:
                            iniciar = input('Tente novamente. Continuar? > ')
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
                        rodada += 1
                    else:
                        pontuacao -= 1
                        print('Errou :(\nResposta correta:', result)
                        rodada += 1
                        vidas -= 1
                    if vidas == 0:
                        iniciar = True
                        print('Game over. Você não tem mais vidas.\nPontuação final:', pontuacao, '\n')
                        print('Voltando ao menu principal...')
                        time.sleep(4)
                        os.system('cls') # Clearing the Screen
                        break
                    else:
                        iniciar = input('Continuar? ')
                    while iniciar not in sim:
                        if iniciar in nao or iniciar in sair:
                            iniciar = True
                            print('Voltando ao menu principal...')
                            time.sleep(4)
                            os.system('cls') # Clearing the Screen
                            break
                        else:
                            iniciar = input('Tente novamente. Continuar? > ')
            if vidas == 0:
                break
else:
    saindo()