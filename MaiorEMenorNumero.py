#Algoritmo que recebe números e identifica o maior e menor entre os números recebidos

ciclo = 0
maior = 0

while ciclo < 5:
    ciclo = ciclo + 1
    num = int(input("Digite um numero: "))

    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    
print("Maior número =", maior)
print("Menor número =", menor)
