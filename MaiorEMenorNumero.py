#Algoritmo que recebe números e identifica o maior e menor entre os números recebidos

cont = 0

while cont < 3:
    num = int(input("Digite um número: "))
    
    if cont == 0:
        menor = num
        maior = num
        
    if num > maior:
        maior = num
    elif menor > num:
        menor = num
    cont = cont + 1

print("Maior número =", maior)
print("Menor número =", menor)
