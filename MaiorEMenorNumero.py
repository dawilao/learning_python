#Algoritmo que recebe números e identifica o maior e menor entre os números recebidos

cont = 0
c = int(input("Qntd. de números a serem verificados: "))

while cont < c:
    num = int(input("Digite o "+ str(cont+1) + "° número: "))
    
    if cont == 0:
        menor = num
        maior = num
        
    if num > maior:
        maior = num
    elif menor > num:
        menor = num
        
    cont = cont + 1

print("\nMaior número =", maior)
print("Menor número =", menor)
