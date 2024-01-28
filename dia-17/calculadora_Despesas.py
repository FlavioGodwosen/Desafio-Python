import csv
from datetime import datetime

def registrar_despesa(despesas):
    descricao = input("Digite a descrição da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    categoria = input("Digite a categoria da despesa: ")
    data = input("Digite a data da despesa (formato DD/MM/AAAA): ")
    data_formatada = datetime.strptime(data, "%d/%m/%Y").date()

    despesa = {"descricao": descricao, "valor": valor, "categoria": categoria, "data": data_formatada}
    despesas.append(despesa)
    print("Despesa registrada com sucesso!\n")

def resumo_por_categoria(despesas):
    resumo = {}
    for despesa in despesas:
        categoria = despesa["categoria"]
        if categoria not in resumo:
            resumo[categoria] = 0
        resumo[categoria] += despesa["valor"]

    print("\nResumo por Categoria:")
    for categoria, total in resumo.items():
        print(f"{categoria}: R${total:.2f}")
    print()

def total_por_data(despesas):
    data_escolhida = input("Digite a data para visualizar o total de despesas (formato DD/MM/AAAA): ")
    data_formatada = datetime.strptime(data_escolhida, "%d/%m/%Y").date()

    total = 0
    for despesa in despesas:
        if despesa["data"] == data_formatada:
            total += despesa["valor"]

    print(f"\nTotal de despesas em {data_escolhida}: R${total:.2f}\n")

def salvar_despesas_csv(despesas):
    with open("despesas.csv", "w", newline="") as csvfile:
        fieldnames = ["descricao", "valor", "categoria", "data"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(despesas)
    print("Despesas salvas em despesas.csv\n")

def main():
    despesas = []

    while True:
        print("----- Menu -----")
        print("1. Registrar nova despesa")
        print("2. Resumo por categoria")
        print("3. Total de despesas por data")
        print("4. Salvar despesas em CSV")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            registrar_despesa(despesas)
        elif opcao == "2":
            resumo_por_categoria(despesas)
        elif opcao == "3":
            total_por_data(despesas)
        elif opcao == "4":
            salvar_despesas_csv(despesas)
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
