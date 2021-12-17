'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
   C = 5 * ((F-32) / 9).
   Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

print("-- CONVERSOR DE TEMPERATURAS --")
print("###############################")

opcao = 1

while opcao != 0:
    print("\nDigite:\n1. Celsius para Fahrenheit\n2. Celsius para Kelvin\n3. Fahrenheit para Celsius\n4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celsius\n6. Kelvin para Fahrenheit")
    print("Para sair, digite 0")
    opcao = int(input("Opção: "))

    if opcao == 1:
        c = float(input("\nDigite a temperatura em °C: "))
        f = (c * (9/5)) + 32
        f = round(f,2)
        print("A temperatura é de:", f,"°F")
    elif opcao == 2:
        c = float(input("\nDigite a temperatura em °C: "))
        k = c + 273.15
        print("A temperatura é de:", k,"K")        
    elif opcao == 3:
        f = float(input("\nDigite a temperatura em °F: "))
        c = 5 * ((f-32) / 9)
        c = round(c,2)
        print("A temperatura é de:", c,"°C")
    elif opcao == 4:
        f = float(input("\nDigite a temperatura em °F: "))
        k = (5 * ((f-32) / 9)) + 273.15
        k = round(k,2)
        print("A temperatura é de:", k,"K")
    elif opcao == 5:
        k = float(input("\nDigite a temperatura em K: "))
        c = k - 273.15
        c = round(c,2)
        print("A temperatura é de:", c,"°C")
    elif opcao == 6:
        k = float(input("\nDigite a temperatura em K: "))
        f = ((k - 273.15) * (9/5)) + 32
        f = round(f,2)
        print("A temperatura é de:", f,"°C")
    elif opcao == 0:
        print("\nSaindo...")
    else:
        print("\nOpção incorreta. Tente novamente.")
