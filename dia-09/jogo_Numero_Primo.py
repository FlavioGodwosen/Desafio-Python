import random

# Função para verificar se um número é primo
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Função para jogar
def play_game():
    random_number = random.randint(1, 100)
    player_guess = int(input(f"É o número {random_number} primo? (Digite 1 para Sim, 2 para Não): "))

    if (player_guess == 1 and is_prime(random_number)) or (player_guess == 2 and not is_prime(random_number)):
        print("Resposta correta! +1 ponto\n")
        return 1
    else:
        print(f"Resposta incorreta. O número {random_number} {'é' if is_prime(random_number) else 'não é'} primo.\n")
        return 0

# Função para ver pontuação
def view_score(score):
    print(f"Sua pontuação atual é: {score}\n")

# Função principal
def main():
    score = 0

    while True:
        print("Menu Inicial:")
        print("1. Jogar")
        print("2. Ver Pontuação")
        print("3. Zerar Pontuação")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            score += play_game()
        elif choice == '2':
            view_score(score)
        elif choice == '3':
            score = 0
            print("Pontuação zerada.\n")
        elif choice == '4':
            print("Obrigado por jogar! Até logo.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
