import unittest

def contar_palavras(texto):
    palavras = texto.split()
    num_palavras = len(palavras)
    return num_palavras

class TestContagemPalavras(unittest.TestCase):

    def test_teste_01(self):
        self.assertEqual(contar_palavras("Isso é um teste."), 4)

    def test_teste_02(self):
        self.assertEqual(contar_palavras("   Olá,    mundo!   "), 2)

    def test_teste_03(self):
        self.assertEqual(contar_palavras("Palavra Palavra palavra"), 3)

    def test_teste_04(self):
        self.assertEqual(contar_palavras("Este é um teste de contagem de palavras."), 8)

    def test_teste_05(self):
        self.assertEqual(contar_palavras(""), 0)

    def test_teste_06(self):
        self.assertEqual(contar_palavras("Maria tem 10 anos."), 4)

    def test_teste_07(self):
        self.assertEqual(contar_palavras("Olá ,  Mundo"), 3)

    def test_teste_08(self):
        texto = ("Em uma tarde ensolarada, 3 crianças brincavam no parque. De repente, encontraram um mapa "
                 "misterioso, com anotações enigmáticas: 'Vire à esquerda, depois à direita, e avance 100 "
                 "passos!' Eles, empolgados, seguiram as instruções cuidadosamente, contando cada passo com "
                 "atenção. No caminho , encontraram diversos obstáculos: pedras, galhos e até um riacho raso. "
                 "O mapa os levou a uma árvore antiga, com raízes grossas e folhas densas. 'Aqui deve ser!', "
                 "exclamou João, o mais velho. Mas, sob a árvore, só encontraram uma caixa vazia e um bilhete: "
                 "'A verdadeira aventura está na jornada, não no destino. Parabéns por chegarem até aqui!' "
                 "Desapontados, mas ainda animados, decidiram continuar explorando. 'Vamos ver o que mais podemos "
                 "descobrir!', disse Maria, a mais aventureira do grupo. E assim, a busca por tesouros se transformou "
                 "em uma tarde de descobertas e diversão. No final, o que realmente importava era a amizade e as "
                 "memórias que criaram juntos.")
        self.assertEqual(contar_palavras(texto), 151)

    def test_teste_09(self):
        self.assertEqual(contar_palavras("Oi"), 1)

if __name__ == '__main__':
    unittest.main()

