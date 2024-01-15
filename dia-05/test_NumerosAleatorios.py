import unittest
from numeros_Aleatorios import random

class TestMegaSenaGenerator(unittest.TestCase):
    def test_gera_seis_numeros(self):
        numeros_mega_sena = gera_numeros_mega_sena()
        self.assertEqual(len(numeros_mega_sena), 6)

    def test_sem_numeros_repetidos(self):
        numeros_mega_sena = gera_numeros_mega_sena()
        self.assertEqual(len(set(numeros_mega_sena)), 6)

    def test_numeros_dentro_do_intervalo(self):
        numeros_mega_sena = gera_numeros_mega_sena()
        for numero in numeros_mega_sena:
            self.assertGreaterEqual(numero, 1)
            self.assertLessEqual(numero, 60)

    def test_lista_ordenada(self):
        numeros_mega_sena = gera_numeros_mega_sena()
        numeros_mega_sena_ordenados = sorted(numeros_mega_sena)
        self.assertEqual(numeros_mega_sena, numeros_mega_sena_ordenados)

def gera_numeros_mega_sena():
    numeros_mega_sena = []
    while len(numeros_mega_sena) < 6:
        numero_aleatorio = random.randint(1, 60)
        if numero_aleatorio not in numeros_mega_sena:
            numeros_mega_sena.append(numero_aleatorio)
    return numeros_mega_sena

if __name__ == '__main__':
    unittest.main()
