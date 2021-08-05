# -*- coding: utf-8 -*-
#
# Integrantes:
#   Thiare Marina Espinoza Saez
#   Felipe Andres Gonzalez Delgado
#   Verner Andres Marin Fuentes
#   Ian Diego Mejias Conejeros

from random import randint
from modules.interfaz import Tablero
from colorama import Fore, Back
from modules.entities import *

tab = Tablero(FIELD_WIDTH, FIELD_HEIGHT)

frank = Estafador()
carl = Agente(frank)

tab.addentity(frank, "E", Fore.BLACK + Back.RED)
tab.addentity(carl, "A", Fore.BLACK + Back.GREEN)

atrapado = False

turno = 0

tab.draw()

while turno < 70 and not atrapado:

    if randint(0, 10000) % 2 == 0:
        # se mueve el estafador
        frank.arrancar(carl)
    else:
        # se mueve el agente
        carl.perseguir(frank)

    if distancia(frank, carl) == 0:
        atrapado = True

    tab.draw()

    turno += 1
    input()

print()

if atrapado:
    print("El estafador ha sido capturado")
else:
    print("El estafador logró escapar")

print(f'La persecución duró "{turno} segundos"')
print(f'El estafador dió {frank.pasos} pasos')
print(f'El agente dió {carl.pasos} pasos')

input('\nPresione una tecla para finalizar...')


#No presenta estado de los personajes durante ejecucion
# 4 personas utilizan Clases y Objetos
# NOTA 100 Pendiente