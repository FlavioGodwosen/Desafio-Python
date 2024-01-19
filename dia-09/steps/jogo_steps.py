from behave import given, when, then
from jogo_Numero_Primo import Jogo

@given('o programa gera o número {numero:d}')
def step_gerar_numero(context, numero):
    context.jogo = Jogo()
    context.numero_gerado = numero

@when('o jogador responde "{resposta}"')
def step_jogador_responde(context, resposta):
    context.jogo.play_game()
    context.resultado = "correta" if resposta == '1' else "incorreta"

@then('a resposta está correta, e o jogador ganha pontos')
def step_resposta_correta_ganha_pontos(context):
    assert context.resultado == "correta"
    assert context.jogo.pontuacao == 1

