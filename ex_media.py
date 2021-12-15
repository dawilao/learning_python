'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
Descrição simplificada: Algoritmo que lê duas notas e calcula a média entre elas, retornando diferentes mensagens dependendo da média final.
'''

def media (n1, n2): #função que calcula média
    m = (nota1 + nota2)/2
    return m

def verifica_media(m):
    if m > 7 and m < 10:
        print('\nMédia final:', mfinal, 'pontos.\nAprovado! :)\n')
    elif m == 10:
        print('\nMédia final:', mfinal, 'pontos.\nAprovado com Distinção! :D')
    else:
        print('\nMédia final:', mfinal, 'pontos.\nReprovado. :(')

print('MEDIA DE DUAS NOTAS')
print('###################\n')

nota1 = float(input('Informe a 1ª nota: '))
while nota1 > 10 or nota1 < 0:
    if nota1 > 10:
        print('A nota não pode ser maior que 10 pontos.')
        nota1 = float(input('Informe novamente a 1ª nota: '))
    elif nota1 < 0:
        print('A nota não pode ser negativa.')
        nota1 = float(input('Informe novamente a 1ª nota: '))

nota2 = float(input('\nInforme a 2ª nota: '))
while nota2 > 10 or nota2 < 0:
    if nota2 > 10:
        print('A nota não pode ser maior que 10 pontos.')
        nota2 = float(input('Informe novamente a 2ª nota: '))
    elif nota2 < 0:
        print('A nota não pode ser negativa.')
        nota2 = float(input('Informe novamente a 2ª nota: '))

mfinal = media(nota1, nota2)
verifica_media(mfinal)
