'''Algoritmo que calcula o valor do transporte pela quantidade de dias úteis, além de calcular os dias úteis pelo total do transporte.'''

print('CALCULADORA DE VALOR DE TRANPORTE')
print('#################################')

x = True
transp = 185.27
uteis_mes = float(input('\nInforme a qntd. de dias úteis no mês (apenas números): '))

transp_dia = transp/uteis_mes

while x == True:
  valid = input("Informe: dias ou valor (ou parar)? ")
  while valid != 'parar' and valid != 'dias' and valid != 'valor':
      valid = input("Informe corretamente: dias ou valor (ou parar)? ")

  while valid != 'parar':
      if valid == 'dias':
          uteis_trab = input('\nDias úteis trabalhados: ')
          if uteis_trab == 'voltar':
            break
          else:
            transp_total = float(uteis_trab) * transp_dia
            transp_total = round(transp_total,2)
            print('Valor total: R$', transp_total)
      elif valid == 'valor':
          valor_total = input('\nValor aux. transp.: ')
          if valor_total == 'voltar':
            break
          else:
            uteis_trab = float(valor_total)/transp_dia
            uteis_trab = round(uteis_trab,2)
            uteis_descont = uteis_mes - uteis_trab
            print('Qntd. dias:', uteis_trab, '\nDias descontados:', uteis_descont)
  
  if valid == 'parar':
    print('\nSaindo.')
    x = False