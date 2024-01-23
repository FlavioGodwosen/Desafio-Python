import pytest

from validador_Email import validar_email

def test_email_valido():
    assert validar_email("usuario@email.com") is True

def test_email_invalido_01():
    assert validar_email("email.com") is False

def test_email_invalido_02():
    assert validar_email("usuario@.com") is False

def test_email_invalido_03():
    assert validar_email("usuario@dominio") is False

def test_email_invalido_04():
    assert validar_email("@dominio.com") is False

def test_email_invalido_05():
    assert validar_email("meu email@dominio.com") is False

def test_email_invalido_06():
    assert validar_email("meu@dominio.c") is False
