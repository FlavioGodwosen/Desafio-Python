import csv
import os

# Função para criar o arquivo CSV se não existir
def criar_arquivo_csv():
    if not os.path.isfile('biblioteca.csv'):
        with open('biblioteca.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Título', 'Autor', 'Ano'])

# Função para adicionar um novo livro à biblioteca
def adicionar_livro():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o nome do autor: ')
    ano = input('Digite o ano de publicação: ')

    with open('biblioteca.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([titulo, autor, ano])

    print(f'O livro "{titulo}" foi adicionado à biblioteca.')

# Função para visualizar a lista de livros
def visualizar_lista():
    with open('biblioteca.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        for row in reader:
            print(f'Título: {row[0]}, Autor: {row[1]}, Ano: {row[2]}')

# Função principal
def main():
    criar_arquivo_csv()

    while True:
        print('\nMENU:')
        print('1. Adicionar Livro')
        print('2. Visualizar Lista de Livros')
        print('3. Sair')

        escolha = input('Escolha uma opção (1/2/3): ')

        if escolha == '1':
            adicionar_livro()
        elif escolha == '2':
            visualizar_lista()
        elif escolha == '3':
            print('Saindo do programa. Até mais!')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == '__main__':
    main()
