# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 20:02:20 2021

@author: Kevin
"""


##INTREGANTES DEL GRUPO: KEVIN'S VILLATORO GUERRERO, PARALELO 192-B##
##LAS VARIABLES "FAGENTE/CAGENTE/FESTF/CESTF" CORRESPONDEN A LAS VARIABLES DE POSICIÓN DE CADA PERSONAJE, SIENDO F POR FILA Y C POR COLUMNA##
##LA VARIABLE TURNO ES LA CUAL DETERMINA AL AZAR ESCOGIENDO ENTRE DOS NUMEROS (1 Y 2) CUAL VA A SER EL PERSONAJE QUE SE DESPLAZARÁ##
##ENTRE LA LÍNEA N68 Y N139 SE DESARROLLA EL ALGORITMO CREADO PARA EL DESPLAZAMIENTO DE UNO U OTRO DE LOS PERSONAJES, BAJO LAS CONDICIONES ENUNCIADAS EN EL PROBLEMA##


import random
import os

Tiempo = 0
PasosA = 0
PasosE = 0
Sw = 0



FAgente = random.randint(1, 20)
CAgente = random.randint(1, 20)

FEstf = random.randint(1, 20)
CEstf = random.randint(1, 20)

while abs(FEstf - FAgente) <= 2 and abs(CEstf - CAgente) <= 2:
    FEstf = random.randint(1, 20)
    CEstf = random.randint(1, 20)
    
print("=======================================================")
print("=======================================================")
print("         Presione cualquier tecla para iniciar")
print("=======================================================")
print("=======================================================")
input()
os.system("cls")
print("")
print("=======================================================")
print("El Estafador comienza en Fila = ", FEstf, "|Columna = ", CEstf)
print("El Agente comienza en Fila =   ", FAgente, "|Columna = ", CAgente)
print("=======================================================")
print("")

PasosYAg = CAgente
PasosXAg = FAgente
PasosYEf = CEstf
PasosXEf = FEstf



while Sw == 0:

    print("1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18   19  20")

    for i in range(1, 21):
        for j in range(1, 21):
            print("+   ", end="")
        print(i, " ")

    print("")

    Turno = random.randint(1, 2)
    Tiempo = Tiempo + 1
    
    if Turno == 1:
        if CAgente > CEstf:
            FEstf = random.randint(1, 20)
            CEstf = random.randint(1, CEstf)

        if CAgente < CEstf:
            FEstf = random.randint(1, 20)
            CEstf = random.randint(CEstf, 20)

        if CAgente == CEstf:
            FEstf = random.randint(1, 20)

        if FAgente > FEstf:
            FEstf = random.randint(1, FEstf)
            CEstf = random.randint(1, 20)

        if FAgente < FEstf:
            FEstf = random.randint(FEstf, 20)
            CEstf = random.randint(1, 20)

        if FAgente == FEstf:
            CEstf = random.randint(1, 20)

        if (FEstf < 1 or FEstf > 20) or (CEstf < 1 or CEstf > 20):
            FEstf = random.randint(1, 20)
            CEstf = random.randint(1, 20)

        PasosE = PasosE + (abs(PasosYEf - CEstf) + (PasosXEf - FEstf))
        PasosYEf = CEstf
        PasosXEf = FEstf
        print("=======================================================")
        print("=======================================================")
        print("Se mueve el Estafador. |Fila: ", FEstf, "|Fila:", CEstf)
        print("Posición Agente.       |Fila ", FAgente, "|Columna:", CAgente)
        print("=======================================================")
        print("=======================================================")

    else:
        if CAgente > CEstf:
            FAgente = random.randint(1, 20)
            CAgente = random.randint(1, CAgente)

        if CAgente < CEstf:
            FAgente = random.randint(1, 20)
            CAgente = random.randint(CAgente, 20)

        if CAgente == CEstf:
            FAgente = random.randint(1, 20)

        if FAgente > FEstf:
            FAgente = random.randint(1, FAgente)
            CAgente = random.randint(1, 20)

        if FAgente < FEstf:
            FAgente = random.randint(FAgente, 20)
            CAgente = random.randint(1, 20)

        if FAgente == FEstf:
            CAgente = random.randint(1, 20)

        if FAgente < 1:
            FAgente = 20
        if FAgente > 20:
            FAgente = 1
        if CAgente < 1:
            CAgente = 20
        if CAgente > 20:
            CAgente = 1

        PasosA = PasosA + (abs(PasosYAg - CAgente) + (PasosXAg - FAgente))
        PasosYAg = CAgente
        PasosXAg = FAgente
        print("=======================================================")
        print("=======================================================")
        print("Se mueve el Agente. |Fila: ", FAgente, "|Columna:", CAgente)
        print("Posicion Estafador. |Fila: ", FEstf, "|Columna:", CEstf)
        print("=======================================================")
        print("=======================================================")
    # Fin If

    input()

    if FAgente == FEstf and CAgente == CEstf:
        Sw = 1
    if Tiempo >= 70:
        Sw = 2
    os.system("cls")
# Fin while
if Sw == 1:
    print("=======================================================")
    print("=======================================================")
    print("El agente Encontró al estafador en: ", Tiempo, "segundos.")
    print("El agente caminó:                  ", PasosA,"pasos.")
    print("El estafador caminó:               ", PasosE,"pasos.")
    print("=======================================================")
    print("=======================================================")
else:
    print("=======================================================")
    print("=======================================================")
    print("El estafador escapó del agente.")
    print("El agente caminó:    ", PasosA, "pasos.")
    print("El estafador caminó: ", PasosE,"pasos.")
    print("=======================================================")
    print("=======================================================")
    
input("FIN DEL JUEGO")
input()

# Problema de ejecucion, exceso de pasos, personajes no se muestran en tablero
# Nota: 55-80