import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "openai", "inteligencia", "artificial"]
    return random.choice(palavras)

def mostrar_palavra_secreta(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def jogo_da_forca():
    palavra_secreta = escolher_palavra().lower()
    letras_corretas = set()
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(mostrar_palavra_secreta(palavra_secreta, letras_corretas))

    while tentativas < tentativas_maximas:
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite uma única letra.")
            continue

        if tentativa in letras_corretas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if tentativa in palavra_secreta:
            letras_corretas.add(tentativa)
            print("Letra correta!")
        else:
            tentativas += 1
            print(f"Tentativa incorreta. Tentativas restantes: {tentativas_maximas - tentativas}")

        palavra_atual = mostrar_palavra_secreta(palavra_secreta, letras_corretas)
        print(palavra_atual)

        if palavra_atual == palavra_secreta:
            print("Parabéns! Você acertou a palavra!")
            break

    if tentativas == tentativas_maximas:
        print(f"Fim de jogo. A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_da_forca()
