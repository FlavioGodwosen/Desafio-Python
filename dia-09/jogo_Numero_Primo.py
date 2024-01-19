import random

class Jogo:
    def __init__(self):
        self.pontuacao = 0

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(self):
        random_number = random.randint(1, 100)
        player_guess = input(f"É o número {random_number} primo? (Digite 1 para Sim, 2 para Não): ")

        if (player_guess == '1' and self.is_prime(random_number)) or (player_guess == '2' and not self.is_prime(random_number)):
            print("Resposta correta! +1 ponto\n")
            self.pontuacao += 1
        else:
            print(f"Resposta incorreta. O número {random_number} {'é' if self.is_prime(random_number) else 'não é'} primo.\n")

    def view_score(self):
        print(f"Sua pontuação atual é: {self.pontuacao}\n")

    def reset_score(self):
        self.pontuacao = 0
        print("Pontuação zerada.\n")

# Função principal
def main():
    jogo = Jogo()

    while True:
        print("Menu Inicial:")
        print("1. Jogar")
        print("2. Ver Pontuação")
        print("3. Zerar Pontuação")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            jogo.play_game()
        elif choice == '2':
            jogo.view_score()
        elif choice == '3':
            jogo.reset_score()
        elif choice == '4':
            print("Obrigado por jogar! Até logo.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
