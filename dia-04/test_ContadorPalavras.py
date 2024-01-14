def contar_palavras(texto):
    palavras = texto.split()
    num_palavras = len(palavras)
    return num_palavras

# Testes unitários
testes = [
    ("Isso é um teste.", 4),
    ("   Olá,    mundo!   ", 2),
    ("Palavra Palavra palavra", 3),
    ("Este é um teste de contagem de palavras.", 8),
    ("", 0),
    ("Maria tem 10 anos.", 4),
    ("Olá ,  Mundo", 3),
    ("Em uma tarde ensolarada, 3 crianças brincavam no parque. De repente, encontraram um mapa misterioso, com anotações enigmáticas: 'Vire à esquerda, depois à direita, e avance 100 passos!' Eles, empolgados, seguiram as instruções cuidadosamente, contando cada passo com atenção. No caminho , encontraram diversos obstáculos: pedras, galhos e até um riacho raso. O mapa os levou a uma árvore antiga, com raízes grossas e folhas densas. 'Aqui deve ser!', exclamou João, o mais velho. Mas,   sob a árvore, só encontraram uma caixa vazia e um bilhete: 'A verdadeira aventura está na jornada, não no destino. Parabéns por chegarem até aqui!' Desapontados, mas ainda animados, decidiram continuar explorando. 'Vamos ver o que mais podemos descobrir!', disse Maria, a mais aventureira do grupo. E assim, a busca por tesouros se transformou em uma tarde de descobertas e diversão. No final, o que realmente importava era a amizade e as memórias que criaram juntos.", 151),
    ("Oi", 1),
]

for texto, resultado_esperado in testes:
    resultado = contar_palavras(texto)
    assert resultado == resultado_esperado, f"Falha no teste: {texto}. Resultado obtido: {resultado}, Resultado esperado: {resultado_esperado}"

print("Todos os testes passaram com sucesso!")
