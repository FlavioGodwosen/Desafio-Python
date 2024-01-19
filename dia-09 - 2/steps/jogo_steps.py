from behave import given, when, then
from jogo_Numero_Primo import Jogo

@given('o programa gera um número primo')
def step_gerar_numero_primo(context):
    context.jogo = Jogo()
    context.jogo.numero_gerado = context.jogo.gerar_numero_primo()

@given('o programa gera um número não primo')
def step_gerar_numero_nao_primo(context):
    context.jogo = Jogo()
    context.jogo.numero_gerado = context.jogo.gerar_numero_nao_primo()

@when('o jogador responde "{resposta}"')
def step_jogador_responde(context, resposta):
    context.resultado = context.jogo.responder(resposta)

@then('a resposta está correta, e o jogador ganha pontos')
def step_resposta_correta_ganha_pontos(context):
    assert context.resultado == "correta"
    assert context.jogo.pontuacao == 1

@then('a resposta está incorreta, e o jogador não ganha pontos e o jogo acaba')
def step_resposta_incorreta_jogo_acaba(context):
    assert context.resultado == "incorreta"
    assert context.jogo.pontuacao == 0
    assert context.jogo.jogo_acabou


