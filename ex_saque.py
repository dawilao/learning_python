'''Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

print('BEM VINDO.\nValor mínimo do saque: R$ 10,00\nValor máximo do saque: R$ 600,00')

saque = int(input('\nDigite o valor do saque: '))

while saque < 10 or saque > 600:
    if saque < 10:
        saque = int(input('Valor mínimo: R$ 10,00. Digite novamente o valor do saque: '))
    elif saque > 600:
        saque = int(input('Valor máximo: R$ 600,00. Digite novamente o valor do saque: '))
        
print('\nNotas:')

s_100 = saque//100  #// para divisão inteira
if s_100 > 0:
    saque = saque - (s_100 * 100)   #Subtrai o valor das notas de 100 pelo valor do saque
    print(f'{s_100} notas de 100')  #Imprime o valor, caso exista; f'{} printa o valor da var 
    
s_50 = saque//50
if s_50 > 0:
    saque = saque - (s_50 * 50)
    print(f'{s_50} notas de 50')

s_20 = saque//20
if s_20 > 0:
    saque = saque - (s_20 * 20)
    print(f'{s_20} notas de 20')

s_10 = saque//10
if s_10 > 0:
    saque = saque - (s_10 * 10)
    print(f'{s_10} notas de 10')
    
s_5 = saque//5
if s_5 > 0:
    saque = saque - (s_5 * 5)
    print(f'{s_5} notas de 5')

s_1 = saque//1
if s_1 > 0:
    saque = saque - (s_1 * 1)
    print(f'{s_1} notas de 1')
