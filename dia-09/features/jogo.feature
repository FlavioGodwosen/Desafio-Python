Feature: Jogo de Números Primos

  Scenario: Teste 01 - Resposta correta, jogador ganha pontos
    Given o programa gera o número 7
    When o jogador responde "1"
    Then a resposta está correta, e o jogador ganha pontos

  Scenario: Teste 02 - Resposta correta, jogador ganha pontos
    Given o programa gera o número 10
    When o jogador responde "2"
    Then a resposta está correta, e o jogador ganha pontos

  Scenario: Teste 03 - Resposta incorreta, jogo acaba
    Given o programa gera o número 15
    When o jogador responde "1"
    Then a resposta está incorreta, e o jogador não ganha pontos e o jogo acaba

  Scenario: Teste 04 - Resposta incorreta, jogo acaba
    Given o programa gera o número 3
    When o jogador responde "2"
    Then a resposta está incorreta, e o jogador não ganha pontos e o jogo acaba

  Scenario: Teste 05 - Verificar pontuação correta
    Given o jogador tem uma pontuação de 1
    When o jogador escolhe a opção de ver sua pontuação
    Then a pontuação é exibida corretamente

  Scenario: Teste 06 - Zerar pontuação e ganhar pontos novamente
    Given o jogador tem uma pontuação de 1
    When o jogador escolhe a opção de zerar sua pontuação
    And o jogador joga novamente e acerta
    Then a pontuação vai para 1

  Scenario: Teste 07 - Sair do jogo
    Given o jogador está no menu principal
    When o jogador escolhe a opção de sair
    Then o jogo é encerrado
