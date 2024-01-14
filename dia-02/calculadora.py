def calculadora(escolha, num1, num2):
    resultado = None

    if escolha == '1':
        resultado = num1 + num2

    elif escolha == '2':
        resultado = num1 - num2

    elif escolha == '3':
        resultado = num1 * num2

    elif escolha == '4':
        if num2 == 0:
            resultado = "Erro: Não é possível realizar divisão por zero."
        else:
            resultado = num1 / num2

    return resultado


if __name__ == "__main__":
    while True:
        print("\nOperações disponíveis:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha a operação (1, 2, 3, 4, ou 5): ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break

        if escolha not in {'1', '2', '3', '4'}:
            print("Escolha inválida. Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir números válidos.")
            continue

        resultado = calculadora(escolha, num1, num2)
        print(resultado)
