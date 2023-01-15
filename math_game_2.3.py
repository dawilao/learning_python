'''
JOGO DE MATEMÁTICA V2.3 (15/01/2023)
'''

from random import randint, randrange
import time
import os

def menu_principal():
    print ('JOGO DE MATEMÁTICA')
    print('#######################')
    print('OBJETIVO: Acerte o máximo de questões que conseguir.')
    print('Para INICIAR, digite jogar.')
    print('Para ver as INSTRUÇÕES, digite instruções.')
    print('Para selecionar a DIFICULDADE, digite dificuldade.')
    print('Para selecionar a quantidade de VIDAS, digite vidas.')
    if cont_jogos > 0:
        print('Maior pontuação:', maior_pontuacao)
        print('Última pontuação:', ultima_pontuacao)
        
def saindo():
    print('\nObrigado por jogar!')
    time.sleep(2.5) #sleep por 3 seg

def instrucoes():
    print('\nINSTRUÇÕES')
    print('#######################')
    print('Acerte o máximo de questões que conseguir antes que suas vidas acabem.')
    print('Você pode selecionar a DIFICULDADE digitando dificuldade, ou a quantidade de VIDAS digitando vidas.')
    print('Para SAIR, digite sair.')
    time.sleep(1)

def nao_iniciar():
    iniciar = True
    print('Voltando...')
    time.sleep(1.3)
    os.system('cls') # Clearing the Screen
    return

def perdeu():
    iniciar == True
    print('Game over. Você não tem mais vidas.\nPontuação final:', pontuacao, '\n')
    time.sleep(2)
    print('Voltando ao menu principal...')
    time.sleep(3.5)
    os.system('cls') # Clearing the Screen
    rodada = 0
    return True

sim = ['1', 'Sim', 'sim', 's', 'S', 'iniciar', 'INICIAR', 'Iniciar', 'Jogar', 'jogar', 'JOGAR', 'ss', 'SS']
inst = ['2', 'Instrucoes', 'instrucoes', 'Instruções', 'instruções', 'inst', 'i', 'I']
sair = ['Sair', 'sair', 'SAIR']
nao = ["não", 'n', 'N', 'nao', 'NÃO']
selec_vidas = ['Vidas', 'vidas', 'v', 'VIDAS']
selec_dificuldade = ['d', 'D', 'Dificuldade', 'DIFICULDADE', 'dificuldade','dif', 'DIF', 'Dif']

pontuacao = 0
ultima_pontuacao = 0
maior_pontuacao1 = maior_pontuacao2 = 0
iniciar = True
vidas = vidas_selecionadas = 1
rodada = 1
cont_jogos = 0
dificuldade = 1
soma_subtracao_facil = 50
soma_subtracao_medio = 500
soma_subtracao_dificil = 10000
multiplicacao_facil = 10
multiplicacao_medio = 20
multiplicacao_dificil = 50
divisao_facil = 100
divisao_medio = 500
divisao_dificil = 1000

while iniciar == True:
    menu_principal()
    iniciar = input('> ')
    while iniciar not in sim or iniciar not in inst or iniciar not in selec_vidas or iniciar not in selec_dificuldade: #AND, não OR
        if iniciar in sair:
            break
        elif iniciar in inst or iniciar in selec_vidas or iniciar in selec_dificuldade:
            while iniciar in inst or iniciar in selec_vidas or iniciar in selec_dificuldade:
                while iniciar in inst:
                    instrucoes()
                    if dificuldade == 1:
                        iniciar = input('\nIniciar jogo? Dificuldade: Fácil' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try 
                    elif dificuldade == 2:
                        iniciar = input('\nIniciar jogo? Dificuldade: Médio' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try 
                    else:
                        iniciar = input('\nIniciar jogo? Dificuldade: Difícil' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try
                while iniciar in selec_vidas:
                    while True:
                        try:
                            vidas_selecionadas = int(input('Selecione a quantidade de vidas (1 ou 3): '))
                            while vidas_selecionadas != 1 and vidas_selecionadas != 3:
                                print('Apenas há a opção de 1 ou 3 vidas.')
                                vidas_selecionadas = int(input('Selecione a quantidade de vidas (1 ou 3): '))
                            break
                        except ValueError:
                            print('Apenas números.')
                    if dificuldade == 1:
                        iniciar = input('\nIniciar jogo? Dificuldade: Fácil' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try 
                    elif dificuldade == 2:
                        iniciar = input('\nIniciar jogo? Dificuldade: Médio' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try 
                    else:
                        iniciar = input('\nIniciar jogo? Dificuldade: Difícil' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try
                while iniciar in selec_dificuldade:
                    print('Dificuldade: FÁCIL, digite 1.\nDificuldade: MÉDIO, digite 2.\nDificuldade: DIFÍCIL, digite 3.')
                    while True:
                        try:
                            dificuldade = int(input('Selecione a dificuldade (1 ou 3): '))
                            while dificuldade < 1 or dificuldade > 3:
                                print('Apenas há a opção de 1 ou 3.')
                                dificuldade = int(input('Selecione a dificuldade (1 ou 3): '))
                            break
                        except ValueError:
                            print('Apenas números.')
                    if dificuldade == 1:
                        iniciar = input('\nIniciar jogo? Dificuldade: Fácil' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try 
                    elif dificuldade == 2:
                        iniciar = input('\nIniciar jogo? Dificuldade: Médio' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try 
                    else:
                        iniciar = input('\nIniciar jogo? Dificuldade: Difícil' + '  Vidas: ' + str(vidas_selecionadas) + '\n> ') # FORA do try
        elif iniciar in nao: # if para voltar ao menu/primeiro while
            iniciar = True
            print('Voltando...')
            time.sleep(1.3)
            os.system('cls') # Clearing the Screen
            break
        elif iniciar in sim:
            while iniciar in sim:
                comecar = randint(1, 5)
                if comecar == 1:
                    print('Que os jogos comecem...')
                elif comecar == 2:
                    print('E lá vamos nós...')
                else:
                    print('Iniciando...')
                time.sleep(1.5)
                vidas = vidas_selecionadas
                rodada = 1
                pontuacao = 0
                while iniciar in sim and vidas > 0:
                    print('\nRodada', rodada, ' Vidas:', vidas, ' Pontuação:', pontuacao)
                    operacao = randint(1, 4)
                    #operacao = 1
                    if dificuldade == 1:
                        x = randint(0, soma_subtracao_facil)
                        y = randint(0, soma_subtracao_facil)
                    elif dificuldade == 2:
                        x = randint(0, soma_subtracao_medio)
                        y = randint(0, soma_subtracao_medio)
                    else:
                        x = randint(0, soma_subtracao_dificil)
                        y = randint(0, soma_subtracao_dificil)
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
                            if pontuacao < 0:
                                pontuacao = 0
                            print('Errou :( Você perdeu uma vida.\nResposta correta:', result)
                            rodada += 1
                            vidas -= 1
                        if vidas == 0:
                            iniciar = True
                            perdeu()
                            ultima_pontuacao = pontuacao
                            break
                        else:
                            iniciar = input('Continuar? ')
                        while iniciar not in sim:
                            if iniciar in nao or iniciar in sair:
                                iniciar = True
                                print('Voltando ao menu principal...')
                                time.sleep(2)
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
                            if pontuacao < 0:
                                pontuacao = 0
                            print('Errou :( Você perdeu uma vida.\nResposta correta:', result)
                            rodada += 1
                            vidas -= 1
                        if vidas == 0:
                            iniciar = True
                            perdeu()
                            ultima_pontuacao = pontuacao
                            break
                        else:
                            iniciar = input('Continuar? ')
                        while iniciar not in sim:
                            if iniciar in nao or iniciar in sair:
                                iniciar = True
                                print('Voltando ao menu principal...')
                                time.sleep(2)
                                os.system('cls') # Clearing the Screen
                                break
                            else:
                                iniciar = input('Tente novamente. Continuar? > ')
                    elif operacao == 3:
                        if dificuldade == 1:
                            x = randint(0, multiplicacao_facil)
                            y = randint(0, multiplicacao_facil)
                        elif dificuldade == 2:
                            x = randint(0, multiplicacao_medio)
                            y = randint(0, multiplicacao_medio)
                        else:
                            x = randint(0, multiplicacao_dificil)
                            y = randint(0, multiplicacao_dificil)
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
                            if pontuacao < 0:
                                pontuacao = 0
                            print('Errou :( Você perdeu uma vida.\nResposta correta:', result)
                            rodada += 1
                            vidas -= 1
                        if vidas == 0:
                            iniciar = True
                            perdeu()
                            ultima_pontuacao = pontuacao
                            break
                        else:
                            iniciar = input('Continuar? ')
                        while iniciar not in sim:
                            if iniciar in nao or iniciar in sair:
                                iniciar = True
                                print('Voltando ao menu principal...')
                                time.sleep(2)
                                os.system('cls') # Clearing the Screen
                                break
                            else:
                                iniciar = input('Tente novamente. Continuar? > ')
                    else:
                        if dificuldade == 1:
                            x = randint(0, divisao_facil)
                            y = randint(1, divisao_facil)
                        elif dificuldade == 2:
                            x = randint(0, divisao_medio)
                            y = randint(1, divisao_medio)
                        else:
                            x = randint(0, divisao_dificil)
                            y = randint(1, divisao_dificil)
                        resto = x % y
                        while resto != 0:
                            if dificuldade == 1:
                                x = randint(0, divisao_facil)
                                y = randint(1, divisao_facil)
                            elif dificuldade == 2:
                                x = randint(0, divisao_medio)
                                y = randint(1, divisao_medio)
                            else:
                                x = randint(0, divisao_dificil)
                                y = randint(1, divisao_dificil)
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
                            if pontuacao < 0:
                                pontuacao = 0
                            print('Errou :(\nResposta correta:', result)
                            rodada += 1
                            vidas -= 1
                        if vidas == 0:
                            iniciar = True
                            perdeu()
                            ultima_pontuacao = pontuacao
                            break
                        else:
                            iniciar = input('Continuar? ')
                        while iniciar not in sim:
                            if iniciar in nao or iniciar in sair:
                                iniciar = True
                                print('Voltando ao menu principal...')
                                time.sleep(2)
                                os.system('cls') # Clearing the Screen
                                break
                            else:
                                iniciar = input('Tente novamente. Continuar? > ')
                if vidas == 0:
                    cont_jogos += 1
                    if cont_jogos > 1:
                        if pontuacao > maior_pontuacao:
                            maior_pontuacao = pontuacao
                    else:
                        maior_pontuacao = pontuacao
                    break
            else:
                break 
        else:
            if vidas == 0:
                break
            else:
                iniciar = input('Tente novamente.\n> ')
    else:
        break
else:
    saindo()