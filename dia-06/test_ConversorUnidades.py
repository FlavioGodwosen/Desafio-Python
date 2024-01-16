import unittest

from conversor_unidades import quilometros_para_milhas, milhas_para_quilometros, metros_para_pes, pes_para_metros, celsius_para_fahrenheit, fahrenheit_para_celsius

class TestConversoes(unittest.TestCase):

    def test_quilometros_para_milhas(self):
        self.assertAlmostEqual(quilometros_para_milhas(10), 6.21371, places=4)

    def test_milhas_para_quilometros(self):
        self.assertAlmostEqual(milhas_para_quilometros(20), 32.1868, places=4)

    def test_metros_para_pes(self):
        self.assertAlmostEqual(metros_para_pes(5), 16.4042, places=4)

    def test_pes_para_metros(self):
        self.assertAlmostEqual(pes_para_metros(100), 30.48, places=4)

    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32.0)
        self.assertEqual(celsius_para_fahrenheit(42), 107.6)
        self.assertEqual(celsius_para_fahrenheit(-3), 26.6)

    def test_fahrenheit_para_celsius(self):
        self.assertAlmostEqual(fahrenheit_para_celsius(0), -17.7778, places=4)
        self.assertAlmostEqual(fahrenheit_para_celsius(100), 37.7778, places=4)
        self.assertAlmostEqual(fahrenheit_para_celsius(-11), -23.8889, places=4)

if __name__ == '__main__':
    unittest.main()
