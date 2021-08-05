# Victoria Paz Contreras Toro
# Martín Nicolas Vega Pino
# Felipe Navarrete Valdivia

import os
os.system ("cls")
import random

ColAgente = random.randint(1,20)
FilAgente = random.randint(1,20)
ColEstafador = random.randint(1,20)
FilEstafador = random.randint(1,20)

while (abs(FilAgente - FilEstafador) <= 2 and abs(ColAgente - ColEstafador) <= 2) :
    FilAgente = random.randint(1,20)
    FilEstafador = random.randint(1,20)
    ColAgente = random.randint(1,20)
    ColEstafador = random.randint(1,20)


def MostrarPlano(ColAgente,ColEstafador,FilAgente,FilEstafador) :
    os.system ("cls")
    print("                               1  1  1  1  1  1  1  1  1  1  2")
    print(" 0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9  0")
    fila = 1 
    while fila < 21 :
        prota = ""
        columna = 1
        while columna < 21 :
            if fila == FilAgente and columna == ColAgente :
                prota = prota + " A "
            elif fila == FilEstafador and columna == ColEstafador :
                prota = prota + " E "
            else:
                prota = prota + " . "
            columna = columna + 1
        if fila < 10 :
            print("",fila,prota)
        else:			
            print(fila, prota)
        fila = fila + 1

tiempo = 0
PasosAgente = 0
PasosEstafador = 0
azar = random.randint(1,2)

while (tiempo < 70) and (ColAgente != ColEstafador or FilAgente != FilEstafador) :
    print(MostrarPlano(ColAgente,ColEstafador,FilAgente,FilEstafador))
    azar = random.randint(1,2)
    if azar == 1 :  
        if ColAgente < ColEstafador :
            ColAgente += 1
        if ColAgente > ColEstafador :
            ColAgente -= 1
        if FilAgente < FilEstafador :
            FilAgente += 1
        if FilAgente > FilEstafador :
            FilAgente -= 1
        PasosAgente += 1

    elif azar == 2 : 
        if ColEstafador > ColAgente:
            ColEstafador += 1
        if ColEstafador < ColAgente :
            ColEstafador -= 1
        if FilEstafador > FilAgente :
            FilEstafador += 1
        if FilEstafador < FilAgente :
            FilEstafador -= 1
        while ColEstafador < 1 or ColEstafador > 20 or FilEstafador < 1 or FilEstafador > 20 :
            ColEstafador = random.randint(1,21)
            FilEstafador = random.randint(1,21)
        PasosEstafador += 1
        
    tiempo += 1
    print(tiempo,"segundos.")
    input("Presione Enter...")

if ColAgente == ColEstafador and FilEstafador == FilAgente :
    print("El Estafador ha sido capturado")
else:
    tiempo == 70 
    print("Se acabó el tiempo, el estafador ha escapado huichipirichi XD")

print("Tiempo que duró la persecución: ",tiempo,"segundos.")
print("Pasos del Agente: ",PasosAgente)
print("Pasos del Estafador: ",PasosEstafador)

input()

# Vuelve a colocar ambos personajes si uno se valida, debe ser solo uno 
#Codigo printea un None (modulo sin return), sin colores

#Codigo completamente funcional, 
#Nota 95-100