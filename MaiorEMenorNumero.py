#Algoritmo que recebe n�meros e identifica o maior e menor entre os n�meros recebidos

ciclo = 0
maior = 0

while ciclo < 5:
    ciclo = ciclo + 1
    num = int(input("Digite um numero: "))

    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    
print("Maior n�mero =", maior)
print("Menor n�mero =", menor)
