'''Algoritmo que calcula o valor do transporte pela quantidade de dias úteis, além de calcular os dias úteis 
pelo total do transporte.'''

import time

def versao():
    print('Versão 1.0.2')
    print('Criado por Dawison Oliveira')
    time.sleep(2)
    return

x = True
valores = {'bolsa': 600, 'transp': 185.27}

print('CALCULADORA DE VALOR DE TRANPORTE')
print('#################################')

while True:
    while True:
        uteis_mes = input('\nInforme a qntd. de dias úteis no mês (apenas números): ')
        try:
            uteis_mes = float(uteis_mes)
            break
        except:
            if uteis_mes == 'versão' or uteis_mes == 'versao':
                versao()
            else:
                print('Apenas números!')
    if uteis_mes < 17 or uteis_mes > 24:
        print('O mês não pode ter ' + str(round(uteis_mes)) + ' dias úteis. Tente novamente!')
    else:
        break
    
transp_dia = valores['transp']/uteis_mes

while x == True:
    valid = input("Informe: dias ou valor (ou parar)? ")
    while valid != 'parar' and valid != 'dias' and valid != 'valor':
        valid = input("Informe corretamente: dias ou valor (ou parar)? ")

    while valid != 'parar':
        if valid == 'dias':
            while True:
                uteis_trab = input('\nValor aux. transp.: ')
                try:
                    uteis_trab = float(uteis_trab)
                    break
                except:
                    if uteis_trab != 'voltar' and uteis_trab != 'parar':
                        print('Apenas números!')
                    else:
                        break
            if uteis_trab == 'voltar':
                break
            elif uteis_trab == 'parar':
                print('Saindo.\n')
                x = False
                break
            else:
                transp_total = float(uteis_trab) * transp_dia
                transp_total = round(transp_total,2)
                print('Valor total: R$', transp_total)

        elif valid == 'valor':
            while True:
                valor_total = input('\nValor aux. transp.: ')
                try:
                    valor_total = float(valor_total)
                    break
                except:
                    if valor_total != 'voltar' and valor_total != 'parar':
                        print('Apenas números!')
                    else:
                        break
            if valor_total == 'voltar':
                break
            elif valor_total == 'parar':
                print('Saindo.\n')
                x = False
                break
            else:
                uteis_trab = float(valor_total)/transp_dia
                uteis_trab = round(uteis_trab,2)
                uteis_descont = uteis_mes - uteis_trab
                uteis_descont = round(uteis_descont,2)
                print('Qntd. dias:', uteis_trab, '\nDias descontados:', uteis_descont)
  
    if valid == 'parar':
        print('Saindo...\n')
        x = False
        time.sleep(3)
