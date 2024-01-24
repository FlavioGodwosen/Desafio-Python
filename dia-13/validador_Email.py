import re

def validar_email(email):
    # Define a expressão regular para validar o e-mail
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Verifica se o e-mail corresponde ao padrão
    if re.match(padrao_email, email):
        return True
    else:
        return False

# Solicita ao usuário que insira um e-mail
endereco_email = input("Digite um endereço de e-mail: ")

# Remove espaços em branco do início e do final da string
endereco_email = endereco_email.strip()

# Verifica se o e-mail é válido
if validar_email(endereco_email):
    print(f'O e-mail "{endereco_email}" é válido.')
else:
    print(f'O e-mail "{endereco_email}" não é válido.')
