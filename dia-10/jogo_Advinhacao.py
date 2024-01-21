import random

def jogar_jogo():
    numero_secreto = random.randint(1, 100)
    tentativas = 7
    pontuacao = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while tentativas > 0:
        try:
            palpite = int(input(f"Digite seu palpite (tentativas restantes: {tentativas}): "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas -= 1

        if palpite == numero_secreto:
            pontuacao += 1
            print(f"Parabéns! Você acertou o número {numero_secreto} em {7 - tentativas} tentativas. Sua pontuação é {pontuacao}.")
            break
        elif palpite < numero_secreto:
            print("O número correto é maior.")
        else:
            print("O número correto é menor.")

    if tentativas == 0:
        print(f"Fim de jogo! O número correto era {numero_secreto}. Sua pontuação é {pontuacao}.")

def ver_pontuacao():
    # Aqui você pode implementar a lógica para exibir a pontuação do jogador.
    print("Pontuação do jogador.")

def zerar_pontuacao():
    # Aqui você pode implementar a lógica para zerar a pontuação do jogador.
    print("Pontuação zerada.")

while True:
    print("\nMenu Inicial:")
    print("1. Jogar")
    print("2. Ver Pontuação")
    print("3. Zerar Pontuação")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        jogar_jogo()
    elif escolha == "2":
        ver_pontuacao()
    elif escolha == "3":
        zerar_pontuacao()
    elif escolha == "4":
        print("Saindo do jogo. Até a próxima!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
