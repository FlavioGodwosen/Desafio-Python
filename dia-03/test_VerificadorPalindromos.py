import unittest

from verificador_Palindromos import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome_ovo(self):
        self.assertTrue(is_palindrome("ovo"))

    def test_palindrome_arara(self):
        self.assertTrue(is_palindrome("arara"))

    def test_not_palindrome_reconhecer(self):
        self.assertFalse(is_palindrome("reconhecer"))

    def test_not_palindrome_Python(self):
        self.assertFalse(is_palindrome("Python"))

    def test_palindrome_panama(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))

    def test_not_palindrome_ana_lava_tina(self):
        self.assertFalse(is_palindrome("Anita lava a tina"))

    def test_palindrome_car_or_cat(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_not_palindrome_hello_world(self):
        self.assertFalse(is_palindrome("Hello, World!"))

        print("Todos os testes passaram com sucesso!")

if __name__ == '__main__':
    unittest.main()
