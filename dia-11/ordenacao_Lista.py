def main():
    numeros = []

    # Loop para permitir que o usuário informe números
    while True:
        numero_str = input("Digite um número (ou 'fim' para encerrar a entrada): ")

        # Verifica se o usuário deseja encerrar a entrada
        if numero_str.lower() == 'fim':
            break

        # Tenta converter a entrada para um número
        try:
            numero = int(numero_str)
            numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número válido.")

    # Ordena a lista
    numeros_ordenados = sorted(numeros)

    # lista ordenada
    print("Lista de números ordenada:", numeros_ordenados)

if __name__ == "__main__":
    main()
