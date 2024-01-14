import unittest

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."

class TestParImpar(unittest.TestCase):

    def test_numero_impar_positivo(self):
        self.assertEqual(verificar_par_impar(5), "O número 5 é ímpar.")

    def test_numero_par_positivo(self):
        self.assertEqual(verificar_par_impar(898), "O número 898 é par.")

    def test_numero_impar_negativo(self):
        self.assertEqual(verificar_par_impar(-5), "O número -5 é ímpar.")

    def test_numero_par_negativo(self):
        self.assertEqual(verificar_par_impar(-4), "O número -4 é par.")

    def test_numero_zero(self):
        self.assertEqual(verificar_par_impar(0), "O número 0 é par.")

        print("Todos os testes passaram com sucesso!")

if __name__ == '__main__':
    unittest.main()

