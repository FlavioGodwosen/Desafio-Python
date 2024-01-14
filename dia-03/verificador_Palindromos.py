def is_palindrome(text):
    # Remove espaços em branco, pontuação e converte para letras minúsculas
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Inverte a string
    reversed_text = cleaned_text[::-1]

    # Verifica se a string original e a invertida são iguais
    return cleaned_text == reversed_text

def main():
    user_input = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

    if is_palindrome(user_input):
        print(f"{user_input} é um palíndromo!")
    else:
        print(f"{user_input} não é um palíndromo.")

if __name__ == "__main__":
    main()
