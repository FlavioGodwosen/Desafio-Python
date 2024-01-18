def adicionar_tarefa(lista, tarefa):
    lista.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada com sucesso!')

def remover_tarefa(lista, indice):
    try:
        tarefa_removida = lista.pop(indice)
        print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
    except IndexError:
        print('Erro: Índice inválido. Certifique-se de que a tarefa existe na lista.')

def listar_tarefas(lista):
    print('Lista de Tarefas:')
    for i, tarefa in enumerate(lista, start=1):
        print(f'{i}. {tarefa}')

# Lista para armazenar as tarefas
tarefas = []

while True:
    # Menu de opções
    print('\nMenu:')
    print('1. Adicionar Tarefa')
    print('2. Remover Tarefa')
    print('3. Listar Tarefas')
    print('4. Sair')

    escolha = input('Escolha uma opção (1/2/3/4): ')

    if escolha == '1':
        nova_tarefa = input('Digite a nova tarefa: ')
        adicionar_tarefa(tarefas, nova_tarefa)
    elif escolha == '2':
        if not tarefas:
            print('Erro: A lista de tarefas está vazia.')
        else:
            listar_tarefas(tarefas)
            indice_remover = int(input('Digite o número da tarefa a ser removida: ')) - 1
            remover_tarefa(tarefas, indice_remover)
    elif escolha == '3':
        if not tarefas:
            print('A lista de tarefas está vazia.')
        else:
            listar_tarefas(tarefas)
    elif escolha == '4':
        print('Saindo do programa. Até logo!')
        break
    else:
        print('Opção inválida. Escolha novamente.')
