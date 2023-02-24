import os
import re, time

pasta = 'C:\\Users\\dawis\\Documents\\IR'

print('Verificando duplicados...')
time.sleep(3)

def clear_line(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)

# Cria um dicionário para armazenar o nome do arquivo e sua quantidade de ocorrências
arquivos_duplicados = {}
for arquivo in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, arquivo)):
        verifica = re.search(r'^(.+)_\d+\..+', arquivo)
        if verifica:
            filename = verifica.group(1)
            if filename not in arquivos_duplicados:
                arquivos_duplicados[filename] = [arquivo]
            else:
                arquivos_duplicados[filename].append(arquivo)
        else:
            if arquivo not in arquivos_duplicados:
                arquivos_duplicados[arquivo] = [arquivo]
            else:
                arquivos_duplicados[arquivo].append(arquivo)

# Mostra apenas os arquivos duplicados
duplicados = [filename for filename, paths in arquivos_duplicados.items() if len(paths) > 1]
if duplicados:
    print('ARQUIVOS DUPLICADOS:')
    for filename in duplicados:
        print(filename)
else:
    print('Nenhum arquivo duplicado encontrado.')

