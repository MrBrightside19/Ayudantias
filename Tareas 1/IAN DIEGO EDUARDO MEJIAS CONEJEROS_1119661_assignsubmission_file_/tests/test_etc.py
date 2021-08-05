from unittest import mock
from modules.entities import distancia


def test_distancia():
    a = mock.Mock(x=1, y=3)
    b = mock.Mock(x=1, y=5)

    assert distancia(a, b) == 2

    a = mock.Mock(x=1, y=3)
    b = mock.Mock(x=2, y=4)

    assert distancia(a, b) == 1

    a = mock.Mock(x=3, y=1)
    b = mock.Mock(x=4, y=4)

    assert distancia(a, b) == 3
