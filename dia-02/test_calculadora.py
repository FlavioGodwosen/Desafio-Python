import unittest
from unittest.mock import patch
from calculadora import calculadora

class TestCalculadora(unittest.TestCase):
    def test_adicao(self):
        resultado = calculadora("1", 5, 3)
        self.assertEqual(resultado, 8)

    def test_subtracao(self):
        resultado = calculadora("2", 8, 3)
        self.assertEqual(resultado, 5)

    def test_multiplicacao(self):
        resultado = calculadora("3", 2, 4)
        self.assertEqual(resultado, 8)

    def test_divisao(self):
        resultado = calculadora("4", 10, 2)
        self.assertEqual(resultado, 5)

    def test_divisao_por_zero(self):
        resultado = calculadora("4", 10, 0)
        self.assertEqual(resultado, "Erro: Não é possível realizar divisão por zero.")

    def test_entrada_invalida(self):
        resultado = calculadora("6", 5, 2)
        self.assertIsNone(resultado)

        print("Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    unittest.main()
