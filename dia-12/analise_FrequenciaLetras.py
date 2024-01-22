def analisar_frequencia(texto):
    # Inicializa um dicionário para armazenar a contagem de cada letra
    contagem_letras = {}

    # Itera sobre cada caractere no texto fornecido pelo usuário
    for caractere in texto:
        # Verifica se o caractere é uma letra usando isalpha()
        if caractere.isalpha():
            # Converte o caractere para minúsculas para tratar maiúsculas e minúsculas da mesma forma
            caractere = caractere.lower()

            # Atualiza a contagem para o caractere atual no dicionário
            contagem_letras[caractere] = contagem_letras.get(caractere, 0) + 1

    return contagem_letras

def main():
    # Solicita ao usuário que insira um texto
    texto = input("Insira um texto: ")

    # Chama a função para analisar a frequência de letras no texto
    contagem_letras = analisar_frequencia(texto)

    # Exibe os resultados
    print("\nFrequência de letras:")
    for letra, contagem in contagem_letras.items():
        print(f"{letra}: {contagem}")

if __name__ == "__main__":
    main()
