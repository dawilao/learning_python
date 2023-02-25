import os
import time

pasta = 'C:\\Users\\dawis\\Documents\\IR'

print('Verificando duplicados...')
time.sleep(3)

def clear_line(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)

def verificar_duplicatas(pasta):
	file_list = os.listdir(pasta)

	for file_name in file_list:
		if "_" in file_name:
        		print(file_name)    	
    
# exemplo de uso
path = "C:\\Users\\dawis\\Documents\\IR"
find_duplicates(path)

