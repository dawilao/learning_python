# Aprendendo a criar um timer.

from time import sleep

t = int(input("Quanto tempo para o timer? > "))

for i in range(0,t):
    print('Faltam %s segundos' % str(t-i), end='\r')
    sleep(1)

print('\nO tempo acabou!')