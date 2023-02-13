# Aprendendo a criar um timer.

from time import sleep
import os

t = int(input("Quanto tempo para o timer? > "))

for i in range(0,t):
    delta_tempo = t-i
    print('Faltam %s segundos' % str(delta_tempo), end='\r') # end='\r' reescreve a linha ao final
    sleep(1)

print('O tempo acabou!')