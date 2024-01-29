agenda = []

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    # Verifica se o contato já existe na agenda
    for contato in agenda:
        if contato["nome"] == nome:
            print("Este contato já existe na agenda.")
            return

    novo_contato = {"nome": nome, "telefone": telefone, "email": email}
    agenda.append(novo_contato)
    print("Contato adicionado com sucesso!")

def listar_contatos():
    if not agenda:
        print("A agenda está vazia.")
    else:
        for contato in agenda:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")

def buscar_contato():
    nome_busca = input("Digite o nome do contato a ser buscado: ")
    encontrado = False

    for contato in agenda:
        if contato["nome"] == nome_busca:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
            encontrado = True
            break

    if not encontrado:
        print("Contato não encontrado.")

def excluir_contato():
    nome_exclusao = input("Digite o nome do contato a ser excluído: ")

    for i, contato in enumerate(agenda):
        if contato["nome"] == nome_exclusao:
            del agenda[i]
            print("Contato excluído com sucesso!")
            return

    print("Contato não encontrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Excluir Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            excluir_contato()
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
