from unittest import mock
from modules.entities import Estafador, FIELD_WIDTH, FIELD_HEIGHT
import random

estafador = Estafador()
agente = mock.Mock()


def test_escapardiagonal():
    agente.x = 10
    agente.y = 10

    estafador.x = 8
    estafador.y = 8
    estafador.arrancar(agente)
    assert (estafador.x, estafador.y) == (7, 7)

    estafador.x = 12
    estafador.y = 12
    estafador.arrancar(agente)
    assert (estafador.x, estafador.y) == (13, 13)

    estafador.x = 7
    estafador.y = 15
    estafador.arrancar(agente)
    assert (estafador.x, estafador.y) == (6, 16)

    estafador.x = 13
    estafador.y = 3
    estafador.arrancar(agente)
    assert (estafador.x, estafador.y) == (14, 2)


def test_escaparagenteigualcolumna():
    estafador.x = 4
    estafador.y = 4

    agente.x = 4
    agente.y = 7

    estafador.arrancar(agente)

    assert (estafador.x, estafador.y) == (4, 3)

    agente.x = 4
    agente.y = 1

    estafador.arrancar(agente)

    assert (estafador.x, estafador.y) == (4, 4)


def test_escaparagenteigualfila():
    estafador.x = 8
    estafador.y = 4

    agente.x = 6
    agente.y = 4

    estafador.arrancar(agente)

    assert (estafador.x, estafador.y) == (9, 4)

    agente.x = 15
    agente.y = 4

    estafador.arrancar(agente)

    assert (estafador.x, estafador.y) == (8, 4)


def test_estafadorOOB_izq():
    agente.x = FIELD_WIDTH // 2
    agente.y = FIELD_HEIGHT // 2

    for i in range(1, FIELD_HEIGHT):
        estafador.x = 1
        estafador.y = i

        random.seed(0)
        estafador.arrancar(agente)

        assert (estafador.x, estafador.y) == (13, 14)


def test_estafadorOOB_der():
    agente.x = FIELD_WIDTH // 2
    agente.y = FIELD_HEIGHT // 2

    for i in range(1, FIELD_HEIGHT):
        estafador.x = FIELD_WIDTH
        estafador.y = i

        random.seed(0)
        estafador.arrancar(agente)

        assert (estafador.x, estafador.y) == (13, 14)


def test_estafadorOOB_abajo():
    agente.x = FIELD_WIDTH // 2
    agente.y = FIELD_HEIGHT // 2

    for i in range(1, FIELD_WIDTH+1):
        estafador.x = i
        estafador.y = FIELD_HEIGHT

        random.seed(0)
        estafador.arrancar(agente)

        assert (estafador.x, estafador.y) == (13, 14)


def test_estafadorOOB_arr():
    agente.x = FIELD_WIDTH // 2
    agente.y = FIELD_HEIGHT // 2

    for i in range(1, FIELD_WIDTH+1):
        estafador.x = i
        estafador.y = 1

        random.seed(0)
        estafador.arrancar(agente)

        assert (estafador.x, estafador.y) == (13, 14)
