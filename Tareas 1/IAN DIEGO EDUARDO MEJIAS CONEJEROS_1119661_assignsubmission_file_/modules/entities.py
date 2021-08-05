from random import randint

FIELD_WIDTH = 20
FIELD_HEIGHT = 20


class Entidad(object):
    def __init__(self, ent=None):
        self.x = randint(1, FIELD_WIDTH)
        self.y = randint(1, FIELD_HEIGHT)
        self.pasos = 0

        if ent:
            dist = distancia(self, ent)

            while dist < 3:
                self.x = randint(1, FIELD_WIDTH)
                self.y = randint(1, FIELD_HEIGHT)
                dist = distancia(self, ent)


class Estafador(Entidad):
    def arrancar(self, agente):
        if self.x > agente.x and self.y > agente.y:
            self.x = self.x + 1
            self.y = self.y + 1
        if self.x < agente.x and self.y < agente.y:
            self.x = self.x - 1
            self.y = self.y - 1
        if self.x > agente.x and self.y < agente.y:
            self.x = self.x + 1
            self.y = self.y - 1
        if self.x < agente.x and self.y > agente.y:
            self.x = self.x - 1
            self.y = self.y + 1
        if self.x == agente.x and self.y > agente.y:
            self.y = self.y + 1
        if self.x == agente.x and self.y < agente.y:
            self.y = self.y - 1
        if self.y == agente.y and self.x > agente.x:
            self.x = self.x + 1
        if self.y == agente.y and self.x < agente.x:
            self.x = self.x - 1
        if self.x > FIELD_WIDTH or self.y > FIELD_HEIGHT or self.x <= 0 or self.y <= 0:
            self.x = randint(1, FIELD_WIDTH)
            self.y = randint(1, FIELD_HEIGHT)

        self.pasos += 1

    def __repr__(self):
        return '<Estafador: ({self.x},{self.y})'


class Agente(Entidad):
    def perseguir(self, estafador):
        if self.x < estafador.x:
            self.x = self.x + 1
        elif self.x > estafador.x:
            self.x = self.x - 1
        if self.y < estafador.y:
            self.y = self.y + 1
        elif self.y > estafador.y:
            self.y = self.y - 1

        if self.x > FIELD_WIDTH:
            self.x = 1
        elif self.x < 1:
            self.x = FIELD_WIDTH
        if self.y > FIELD_HEIGHT:
            self.y = 1
        elif self.y < 1:
            self.y = FIELD_HEIGHT

        self.pasos += 1

    def __repr__(self):
        return '<Agente: ({self.x},{self.y})'


def distancia(a, b):
    """
    Devuelve la cantidad de pasos entre 2 entidades
    """
    distX = abs(a.x - b.x)
    distY = abs(a.y - b.y)
    if distX > distY:
        dist = distX
    else:
        dist = distY

    return dist
