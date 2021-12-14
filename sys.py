'''Algoritmo de introdução a passagem de argumentos do sistema.'''

import sys

argumentos = sys.argv #arg0 caminho; arg1 metodo(soma, subt); arg2 = num1; arg3 = num2

print(argumentos)

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

if argumentos[1] == "soma": #se arg1 for soma, faz a soma do arg2 e arg3
    op = argumentos[1]
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "subtracao":
    op = argumentos[1]
    resp = subtracao(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "multiplicacao":
    op = argumentos[1]
    resp = multiplicacao(float(argumentos[2]), float(argumentos[3]))

print("A resposta para a", op, "é:", resp)

#adicionar informação para metodo incorreto