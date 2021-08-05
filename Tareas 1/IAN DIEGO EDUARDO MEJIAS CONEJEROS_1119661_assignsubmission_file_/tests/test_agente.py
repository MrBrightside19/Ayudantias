
from unittest import mock
from modules.entities import Agente


agente = Agente()
estafador = mock.Mock()


def test_perseguirdiagonal():
    estafador.x = 10
    estafador.y = 10

    agente.x = 3
    agente.y = 6
    agente.perseguir(estafador)
    assert (agente.x, agente.y) == (4, 7)

    agente.x = 12
    agente.y = 12
    agente.perseguir(estafador)
    assert (agente.x, agente.y) == (11, 11)

    agente.x = 7
    agente.y = 15
    agente.perseguir(estafador)
    assert (agente.x, agente.y) == (8, 14)

    agente.x = 13
    agente.y = 3
    agente.perseguir(estafador)
    assert (agente.x, agente.y) == (12, 4)


def test_perseguirestafadormismafila():
    """
    El agente se mueve en la misma fila que el estafador.
    """
    estafador.x = 8
    estafador.y = 4

    agente.x = 6
    agente.y = 4

    agente.perseguir(estafador)

    assert (agente.x, agente.y) == (7, 4)

    estafador.x = 4
    estafador.y = 4
    agente.perseguir(estafador)

    assert (agente.x, agente.y) == (6, 4)


def test_perseguirestafadormismacolumna():
    """
    El agente se mueve en la misma columna que el estafador.
    """
    estafador.x = 16
    estafador.y = 5

    agente.x = 16
    agente.y = 8

    agente.perseguir(estafador)

    assert (agente.x, agente.y) == (16, 7)

    estafador.x = 16
    estafador.y = 11
    agente.perseguir(estafador)

    assert (agente.x, agente.y) == (16, 8)
