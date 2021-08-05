from colorama import init
import os


class Tablero:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

        init(autoreset=True)

        symbols = {'skull': '\u2620', 'dot': '\u22C5', 'hourglass': '\u23F3'}

        self._tablero = "     "

        for i in range(self.ancho):
            self._tablero += " {:02d} ".format(i+1)

        for i in range(self.alto):
            s = symbols.get('dot')
            self._tablero += f"\n {i+1:02d} |" + f" {s:>2} " * self.ancho

        self._entities = list()

    def addentity(self, e, rep, form=""):
        """
        Agrega una entidad al tablero que se dibujará cada vez que se llame a
        la función `draw`.

        :param e: Entidad que se quiere agregar al tablero.
        :param rep: Representación de la entidad en pantalla
        :param form: Formato de la entidad para mostrarla por pantalla
        """
        self._entities.append((e, rep, form))

    def draw(self):
        os.system('cls')
        print(self._pos(1, 1) + self._tablero)

        for e, r, form in self._entities:
            print(self._pos(4*e.x + 2, 1 + e.y) + form + f"{r:^4}")

        print(self._pos(1, self.alto+1))

    def _pos(self, x, y):
        return '\x1b[%d;%dH' % (y, x)
