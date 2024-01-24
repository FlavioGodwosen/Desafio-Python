import random
import string

def gerar_senha(comprimento, incluir_numeros, incluir_maiusculas, incluir_minusculas, incluir_especiais):
    caracteres = ''
    
    if incluir_numeros:
        caracteres += string.digits
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print("Erro: Nenhum critério selecionado para a geração da senha.")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Gerador de Senhas Aleatórias")

    comprimento = int(input("Digite o comprimento desejado da senha: "))
    incluir_numeros = input("Incluir números? (S/N): ").upper() == 'S'
    incluir_maiusculas = input("Incluir letras maiúsculas? (S/N): ").upper() == 'S'
    incluir_minusculas = input("Incluir letras minúsculas? (S/N): ").upper() == 'S'
    incluir_especiais = input("Incluir caracteres especiais? (S/N): ").upper() == 'S'

    senha = gerar_senha(comprimento, incluir_numeros, incluir_maiusculas, incluir_minusculas, incluir_especiais)

    if senha:
        print("\nSenha gerada: ", senha)

if __name__ == "__main__":
    main()
