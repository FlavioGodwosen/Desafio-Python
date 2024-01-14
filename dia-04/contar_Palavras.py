def contar_palavras(texto):
    # Use a função split() para dividir o texto em palavras
    palavras = texto.split()

    # Conte o número de palavras
    num_palavras = len(palavras)

    return num_palavras

# Solicita ao usuário inserir o texto
texto_usuario = input("Digite um texto: ")

# Chama a função contar_palavras e imprime o resultado
resultado = contar_palavras(texto_usuario)
print(f"O número de palavras no texto é: {resultado}")
