
import unittest
from unittest.mock import patch
from temporizador_Contador import contador_progressivo, contador_regressivo

class TestTemporizador(unittest.TestCase):

    def test_contador_progressivo(self):
        with patch('builtins.print') as mock_print:
            contador_progressivo(12)
        expected_output = [f"Tempo decorrido: {i} segundos" for i in range(13)]
        mock_print.assert_has_calls([unittest.mock.call(output) for output in expected_output])

    def test_contador_regressivo(self):
        with patch('builtins.print') as mock_print:
            contador_regressivo(12)
        expected_output = [f"Tempo restante: {i} segundos" for i in range(12, -1, -1)]
        mock_print.assert_has_calls([unittest.mock.call(output) for output in expected_output])

if __name__ == "__main__":
    unittest.main()

