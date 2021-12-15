print('CALCULADORA DE VALOR DE TRANPORTE')
print('#################################')

transp = 185.27
uteis_mes = float(input('\nInforme a qntd. de dias úteis no mês (apenas números): '))

transp_dia = transp/uteis_mes

valid = input("Informe: dias ou valor (ou parar)? ")
while valid != 'parar' and valid != 'dias' and valid != 'valor':
    valid = input("Informe corretamente: dias ou valor (ou parar)? ")

while valid != 'parar':
    if valid == 'dias':
        uteis_trab = float(input('\nDias úteis trabalhados: '))
        transp_total = uteis_trab * transp_dia
        transp_total = round(transp_total,2)
        print('Valor total: R$', transp_total)
    elif valid == 'valor':
        valor_total = float(input('\nValor aux. transp.: '))
        uteis_trab = valor_total/transp_dia
        uteis_trab = round(uteis_trab,2)
        uteis_descont = uteis_mes - uteis_trab
        print('Qntd. dias:', uteis_trab, '\nDias descontados:', uteis_descont)

print('\nSaindo.')
