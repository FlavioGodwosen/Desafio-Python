def quilometros_para_milhas(quilometros):
    return quilometros * 0.621371

def milhas_para_quilometros(milhas):
    return milhas * 1.60934

def metros_para_pes(metros):
    return metros * 3.28084

def pes_para_metros(pes):
    return pes * 0.3048

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função principal para interação com o usuário
def main():
    print("Escolha a conversão:")
    print("1. Quilômetros para Milhas")
    print("2. Milhas para Quilômetros")
    print("3. Metros para Pés")
    print("4. Pés para Metros")
    print("5. Graus Celsius para Fahrenheit")
    print("6. Graus Fahrenheit para Celsius")

    escolha = int(input("Digite o número da conversão desejada: "))

    if escolha == 1:
        quilometros = float(input("Digite a distância em quilômetros: "))
        resultado = quilometros_para_milhas(quilometros)
        print(f"{quilometros} quilômetros equivalem a {resultado:.2f} milhas.")
    elif escolha == 2:
        milhas = float(input("Digite a distância em milhas: "))
        resultado = milhas_para_quilometros(milhas)
        print(f"{milhas} milhas equivalem a {resultado:.2f} quilômetros.")
    elif escolha == 3:
        metros = float(input("Digite a distância em metros: "))
        resultado = metros_para_pes(metros)
        print(f"{metros} metros equivalem a {resultado:.2f} pés.")
    elif escolha == 4:
        pes = float(input("Digite a distância em pés: "))
        resultado = pes_para_metros(pes)
        print(f"{pes} pés equivalem a {resultado:.2f} metros.")
    elif escolha == 5:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius equivalem a {resultado:.2f} graus Fahrenheit.")
    elif escolha == 6:
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit equivalem a {resultado:.2f} graus Celsius.")
    else:
        print("Escolha inválida. Por favor, digite um número de 1 a 6.")

if __name__ == "__main__":
    main()
