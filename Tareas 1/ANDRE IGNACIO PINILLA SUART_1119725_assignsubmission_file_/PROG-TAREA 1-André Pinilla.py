# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:05:13 2021

@author: André Ignacio Pinilla Suart
"""

import random


PasosE = 0
PasosA = 0
Tiempo = 0

FilE = random.randint(1, 20)
ColE = random.randint(1, 20)

FilA = random.randint(1, 20)
ColA = random.randint(1, 20)


while abs(FilA - FilE) <= 2 and abs(ColA - ColE) <= 2:
    FilA = random.randint(1, 20)
    ColA = random.randint(1, 20)

    if FilA < 20 and ColA < 20:
        FilA = random.randint(1, 20) + 1
        ColA = random.randint(1, 20) + 1
        PasosA = PasosA + 1
        if ColA > ColE:
            ColA = random.randint(1, 20) - 1
            FilA = random.randint(1, 20) - 1
            PasosA = PasosA + 1
        elif ColA < ColE:
            ColA = random.randint(1, 20) + 1
            FilA = random.randint(1, 20) + 1
            PasosA = PasosA + 1
        else:
            ColA = random.randint(1, 20) + 1

            if ColE > ColA:
                ColE = random.randint(1, 20) + 1
                FilE = random.randint(1, 20) + 1
                PasosE = PasosE + 1
            elif ColE < ColA:
                ColE = random.randint(1, 20) - 1
                FilE = random.randint(1, 20) - 1
                PasosE = PasosE + 1
            else:
                ColE = random.randint(1, 20) + 1
                if FilE == 20 and ColE < 20 or FilE < 20 and ColE == 20:
                    FilE = random.randint(1, 20)
                    ColE = random.randint(1, 20)
                    PasosE = PasosE + 1
                    if Tiempo == 70:
                        print("Se acabo el juego"), Tiempo, PasosE, PasosA
                    elif FilA == FilE and ColA == ColE:
                        print("El Estafador fue atrapado"), Tiempo, PasosE, PasosA
                    else:
                        print("El Estafador escapo"), Tiempo, PasosE, PasosA

for Fil in range(1, 21):
    for Col in range(1, 21):
        if FilE == Fil and ColE == Col:
            print("E", end=" ")
        elif FilA == Fil and ColA == Col:
            print("A", end=" ")
        else:
            print(".", end=" ")

    print()

    Tiempo = PasosE + PasosA


input()


#No entra a la iteracion while, movimientos generados completamente al azar, no cumple con
# la instruccion, implementa interfaz de tablero. PENDIENTE