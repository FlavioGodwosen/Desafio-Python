Feature: Jogo de Números Primos

  Scenario: Teste - Resposta correta, jogador ganha pontos para número primo
    Given o programa gera um número primo
    When o jogador responde "Primo"
    Then a resposta está correta, e o jogador ganha pontos

  Scenario: Teste - Resposta correta, jogador ganha pontos para número não primo
    Given o programa gera um número não primo
    When o jogador responde "Não Primo"
    Then a resposta está correta, e o jogador ganha pontos

  Scenario: Teste - Resposta incorreta para número primo, jogo acaba
    Given o programa gera um número primo
    When o jogador responde "Não Primo"
    Then a resposta está incorreta, e o jogador não ganha pontos e o jogo acaba

  Scenario: Teste - Resposta incorreta para número não primo, jogo acaba
    Given o programa gera um número não primo
    When o jogador responde "Primo"
    Then a resposta está incorreta, e o jogador não ganha pontos e o jogo acaba