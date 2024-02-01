import sqlite3  # Módulo usado para este exemplo. Substitua pelo módulo do seu banco de dados.

def criar_consulta_select():
    # Coleta de informações para a consulta SELECT
    print("Criar Consulta SELECT:")
    tabelas = input("Digite o nome da tabela (ou tabelas, separadas por vírgula): ").split(',')
    colunas = input("Digite as colunas desejadas (ou '*' para todas): ").split(',')
    condicao = input("Digite a condição da cláusula WHERE (ou deixe em branco): ")

    # Construção da consulta SQL SELECT
    consulta = f"SELECT {', '.join(colunas)} FROM {', '.join(tabelas)}"
    if condicao:
        consulta += f" WHERE {condicao}"

    print("\nConsulta SQL SELECT resultante:")
    print(consulta)

def criar_comando_update():
    # Coleta de informações para o comando UPDATE
    print("\nCriar Comando UPDATE:")
    tabela = input("Digite o nome da tabela: ")
    colunas = input("Digite as colunas a serem atualizadas e seus novos valores (no formato coluna1 = valor1, coluna2 = valor2): ")
    condicao = input("Digite a condição da cláusula WHERE (ou deixe em branco para atualizar todos os registros): ")

    # Construção do comando SQL UPDATE
    comando = f"UPDATE {tabela} SET {colunas}"
    if condicao:
        comando += f" WHERE {condicao}"

    print("\nComando SQL UPDATE resultante:")
    print(comando)

def criar_comando_insert():
    # Coleta de informações para o comando INSERT
    print("\nCriar Comando INSERT:")
    tabela = input("Digite o nome da tabela: ")
    colunas = input("Digite as colunas nas quais deseja inserir valores (separadas por vírgula): ").split(',')
    valores = input("Digite os valores correspondentes (separados por vírgula): ").split(',')

    # Construção do comando SQL INSERT
    comando = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['?' for _ in valores])})"
    
    print("\nComando SQL INSERT resultante:")
    print(comando)

    # Exemplo de execução (pode variar dependendo do banco de dados usado)
    # conn = sqlite3.connect("exemplo.db")
    # cursor = conn.cursor()
    # cursor.execute(comando, valores)
    # conn.commit()

def main():
    while True:
        print("\n--- Menu Interativo ---")
        print("1. Criar Consulta SELECT")
        print("2. Criar Comando UPDATE")
        print("3. Criar Comando INSERT")
        print("4. Sair")

        escolha = input("Escolha a opção (1-4): ")
        
        if escolha == '1':
            criar_consulta_select()
        elif escolha == '2':
            criar_comando_update()
        elif escolha == '3':
            criar_comando_insert()
        elif escolha == '4':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()