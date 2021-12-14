'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
   C = 5 * ((F-32) / 9).
   Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

print("CONVERSOR CELSIUS <> FAHRENHEIT")
print("###############################")

opcao = 1

while opcao != 0:
    print("\nDigite:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius")
    print("Para sair, digite 0")
    opcao = int(input("Opção: "))

    if opcao == 1:
        c = float(input("Digite a temperatura em °C: "))
        f = (c * (9/5)) + 32
        f = round(f,2)
        print("\nA temperatura é de:", f,"°F")
    elif opcao == 2:
        f = float(input("Digite a temperatura em °F: "))
        c = 5 * ((f-32) / 9)
        c = round(c,2)
        print("\nA temperatura é de:", c,"°C")
    elif opcao == 0:
        print("\nSaindo...")
    else:
        print("\nOpção incorreta. Tente novamente.")
