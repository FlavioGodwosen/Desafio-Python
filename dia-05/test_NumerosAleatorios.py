import unittest

def gerar_numeros_mega_sena():
    numeros_mega_sena = []
    while len(numeros_mega_sena) < 6:
        numero_aleatorio = random.randint(1, 60)
        if numero_aleatorio not in numeros_mega_sena:
            numeros_mega_sena.append(numero_aleatorio)
    numeros_mega_sena.sort()
    return numeros_mega_sena

class TestGeracaoNumerosMegaSena(unittest.TestCase):

    def test_gerar_numeros_mega_sena_tamanho(self):
        for _ in range(10):  # Executar 10 vezes para verificar a consistência
            numeros = gerar_numeros_mega_sena()
            self.assertEqual(len(numeros), 6, "A lista deve conter 6 números")

    def test_gerar_numeros_mega_sena_faixa(self):
        for _ in range(10):
            numeros = gerar_numeros_mega_sena()
            for numero in numeros:
                self.assertTrue(1 <= numero <= 60, f"Número {numero} fora da faixa esperada")

    def test_gerar_numeros_mega_sena_repeticao(self):
        for _ in range(10):
            numeros = gerar_numeros_mega_sena()
            self.assertEqual(len(set(numeros)), len(numeros), "Números repetidos na lista")

    def test_gerar_numeros_mega_sena_ordem(self):
        for _ in range(10):
            numeros = gerar_numeros_mega_sena()
            self.assertEqual(numeros, sorted(numeros), "A lista não está em ordem crescente")

if __name__ == '__main__':
    unittest.main()