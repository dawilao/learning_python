#Faça um Programa que leia 4 notas, mostre as notas e a média na tela (utilizando lista).

x = 1
notas = []
while x <= 4:
    nota = float(input('Insira a nota ' + str(x) + ': '))
    notas.append(nota)
    x += 1

print('Notas:', notas)

media = sum(notas)/len(notas)

#media = statistics.mean(list)  Outra maneira de calcular média de lista. Necessário import statistics

print('A média é:', media)