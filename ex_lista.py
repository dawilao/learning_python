#Faça um Programa que leia números inteiros e mostre-os, também na ordem inversa.

x = 0
lista_num = []

while x < 3:    #Recebe 3 números
    num = int(input('Digite um número inteiro: '))
    lista_num.append(num)   #Adiciona numero a lista
    x += 1

print(lista_num)    #Mostra a lista de números

y = x - 1 #Define y
for num in lista_num:   #Mostra os números na ordem reversa, um por um
    print(lista_num[y])
    y -= 1

lista_num.reverse() #Reverte a lista
print(lista_num)