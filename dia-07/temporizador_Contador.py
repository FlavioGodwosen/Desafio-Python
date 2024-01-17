import time

def contador_progressivo(tempo):
    for segundos in range(tempo + 1):
        print(f"Tempo decorrido: {segundos} segundos")
        time.sleep(1)

def contador_regressivo(tempo):
    for segundos in range(tempo, -1, -1):
        print(f"Tempo restante: {segundos} segundos")
        time.sleep(1)

def main():
    print("Bem-vindo ao Temporizador!")
    escolha = input("Escolha 'P' para contador progressivo ou 'R' para contador regressivo: ").upper()

    if escolha == 'P':
        tempo_total = int(input("Digite o tempo total em segundos: "))
        contador_progressivo(tempo_total)
    elif escolha == 'R':
        tempo_total = int(input("Digite o tempo inicial em segundos: "))
        contador_regressivo(tempo_total)
    else:
        print("Opção inválida. Por favor, escolha 'P' ou 'R'.")

if __name__ == "__main__":
    main()
