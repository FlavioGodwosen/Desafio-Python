import random

# Inicializa uma lista vazia para armazenar os números
numeros_mega_sena = []

# Loop para gerar 6 números não repetidos
while len(numeros_mega_sena) < 6:
    # Gera um número aleatório entre 1 e 60
    numero_aleatorio = random.randint(1, 60)
    
    # Verifica se o número já está na lista
    if numero_aleatorio not in numeros_mega_sena:
        # Adiciona o número à lista
        numeros_mega_sena.append(numero_aleatorio)

# Ordena a lista em ordem crescente (opcional)
numeros_mega_sena.sort()

# Exibe a lista de números gerados
print("Números da Mega Sena:", numeros_mega_sena)
