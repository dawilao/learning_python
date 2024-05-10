import subprocess

def transform_case(text):
    # Verifica se o texto está em minúsculas
    if text.islower():
        # Se estiver em minúsculas, transforma em maiúsculas
        return text.upper()
    # Verifica se o texto está em maiúsculas
    elif text.isupper():
        # Se estiver em maiúsculas, transforma em minúsculas
        return text.lower()
    else:
        # Se o texto contiver uma mistura de maiúsculas e minúsculas, inverte o caso de cada caractere
        return text.swapcase()

def copy_to_clipboard(text):
    try:
        subprocess.run('echo ' + text.strip() + '| clip', check=True, shell=True)
        print("Texto copiado para a área de transferência com sucesso!")
    except subprocess.CalledProcessError:
        print("Erro ao copiar texto para a área de transferência.")

# Exemplo de uso
text = input("Informe o texto a ser alterado: ")
text_novo = transform_case(text)
copy_to_clipboard(text_novo)
