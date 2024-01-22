from analise_FrequenciaLetras import analisar_frequencia

def testar_analise_frequencia():
    # Teste 01
    texto_01 = "hello world"
    resultado_esperado_01 = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    assert analisar_frequencia(texto_01) == resultado_esperado_01

    # Teste 02
    texto_02 = "programming is fun"
    resultado_esperado_02 = {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
    assert analisar_frequencia(texto_02) == resultado_esperado_02

    # Teste 03
    texto_03 = "testing 123321"
    resultado_esperado_03 = {'t': 2, 'e': 1, 's': 1, 'i': 1, 'n': 1, 'g': 1}
    assert analisar_frequencia(texto_03) == resultado_esperado_03

    print("Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    # Executa os testes unitários
    testar_analise_frequencia()
