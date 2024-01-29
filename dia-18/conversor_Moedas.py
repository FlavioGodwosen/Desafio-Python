import requests

def obter_taxas_conversao(moeda_base):
    url = f'https://open.er-api.com/v6/latest/{moeda_base}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['rates']
    else:
        raise Exception(f"Erro ao obter taxas de conversão. Código de status: {resposta.status_code}")

def converter_moeda(valor, moeda_origem, moeda_destino):
    taxas = obter_taxas_conversao(moeda_origem)
    
    if moeda_destino in taxas:
        taxa_conversao = taxas[moeda_destino]
        valor_convertido = valor * taxa_conversao
        return valor_convertido
    else:
        raise ValueError("Moeda de destino inválida")

def main():
    try:
        moeda_origem = input("Insira a moeda de origem (Código da moeda, por exemplo, USD): ").upper()
        moeda_destino = input("Insira a moeda de destino (Código da moeda, por exemplo, EUR): ").upper()
        valor = float(input("Insira o valor a ser convertido: "))

        valor_convertido = converter_moeda(valor, moeda_origem, moeda_destino)

        print(f"{valor} {moeda_origem} é equivalente a {valor_convertido:.2f} {moeda_destino}")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
