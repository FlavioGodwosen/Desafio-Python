import random

class Jogo:
    def __init__(self):
        self.pontuacao = 0
        self.jogo_acabou = False

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def gerar_numero_primo(self):
        return random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def gerar_numero_nao_primo(self):
        return random.choice([4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100])

    def play_game(self):
        random_number = self.gerar_numero_primo() if random.choice([True, False]) else self.gerar_numero_nao_primo()
        player_guess = input(f"É o número {random_number} primo? (Digite 1 para Sim, 2 para Não): ")

        if not self.jogo_acabou:
            if (player_guess == '1' and self.is_prime(random_number)) or (player_guess == '2' and not self.is_prime(random_number)):
                print("Resposta correta! +1 ponto\n")
                self.pontuacao += 1
            else:
                print(f"Resposta incorreta. O número {random_number} {'é' if self.is_prime(random_number) else 'não é'} primo.\n")
                self.jogo_acabou = True

    def view_score(self):
        print(f"Sua pontuação atual é: {self.pontuacao}\n")

    def reset_score(self):
        self.pontuacao = 0
        self.jogo_acabou = False
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
1
