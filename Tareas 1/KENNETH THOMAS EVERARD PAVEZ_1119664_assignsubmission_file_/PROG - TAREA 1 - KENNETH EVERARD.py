# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:10:05 2021
Grupo compuesto por: Mauro Amaru Pizarro Vega y Kenneth Thomas Everard Pavez
"""
import os
import random
from colorama import init
init()

def pos(x,y):
 print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
 return None

#### Posicion Agente y Estafador #####
XAgente = random.randint(1,20) ; YAgente = random.randint(1,20)
XEstafador = random.randint(1,20); YEstafador = random.randint(1, 20)
while abs(XAgente - XEstafador) < 3 and abs(YAgente - YEstafador) < 3:
      XAgente = random.randint(1,20) ; YAgente = random.randint(1,20)
print("Posición del agente ", (XAgente, YAgente)," y posición del estafador ", (XEstafador, YEstafador))
### Tablero ###
for f in range(1,21): #FILA
    for c in range (1,21): #COLUMNA
        pos(f+1, c)
        print("-")
pos(XEstafador+1, YEstafador); print("E")
pos(XAgente+1, YAgente); print("A")
pos(22,1); print("*** El primer número dentro de los parentesis corresponde a la fila y el segundo a las columnas ***")
input()


os.system("cls")

###### Programa Principal #########
PasosA = 0; PasosE = 0; Segundos = 0; SwMov = 0
while  Segundos !=  70 :
    if XEstafador == XAgente and YEstafador == YAgente:
        break
    SwMov = 0
    SwMov = random.randint(1,2)
    while SwMov == 1:
       PasosA = PasosA + 1
       print("Agente Juega")
       if XAgente > XEstafador and YAgente > YEstafador:
           XAgente = XAgente - 1
           YAgente = YAgente - 1
           break
       if XAgente < XEstafador and YAgente < YEstafador:
           XAgente = XAgente + 1
           YAgente = YAgente + 1
           break
       if XAgente < XEstafador and YAgente > YEstafador:
           XAgente = XAgente + 1
           YAgente = YAgente - 1
           break
       if XAgente > XEstafador and YAgente < YEstafador:
           XAgente = XAgente - 1
           YAgente = YAgente + 1
           break
       if XAgente > XEstafador:
           XAgente = XAgente - 1
           SwMov = 0
           break
       if XAgente < XEstafador:
           XAgente = XAgente + 1
           SwMov = 0
           break
       if YAgente > YEstafador:
           YAgente = YAgente - 1
           SwMov = 0
           break
       if YAgente < YEstafador:
           YAgente = YAgente + 1
           SwMov = 0
           break
       
    while SwMov == 2:
       PasosE = PasosE + 1
       print("Estafador Juega")
       if XAgente == XEstafador and YAgente != YEstafador:
           XEstafador = XEstafador + 1
           if YAgente > YEstafador:
               YEstafador = YEstafador - 1
           else:
               if  YAgente < YEstafador:
                   YEstafador = YEstafador + 1
           break
       if XAgente != XEstafador and YAgente == YEstafador:
           YEstafador = YEstafador + 1
           if XAgente > XEstafador:
               XEstafador = XEstafador - 1
           else:
               if XAgente < XEstafador:
                   XEstafador = XEstafador + 1
           break
       if XEstafador > XAgente and YEstafador > YAgente :
           XEstafador = XEstafador + 1
           YEstafador = YEstafador + 1
           break
       if XEstafador < XAgente and YEstafador < YAgente :
           XEstafador = XEstafador - 1
           YEstafador = YEstafador - 1
           break
       if XEstafador > XAgente :
           XEstafador = XEstafador + 1
           SwMov = 0
           break
       if XEstafador < XAgente:
           XEstafador = XEstafador - 1
           SwMov = 0
           break
       if YEstafador > YAgente:
           YEstafador = YEstafador + 1
           SwMov = 0
           break
       if YEstafador < YAgente:
           YEstafador = YEstafador - 1
           SwMov = 0
           break
    if XAgente > 20:
        XAgente = 1
    if YAgente > 20:
        YAgente = 1
    if XAgente < 1:
        XAgente = 20
    if YAgente < 1:
        YAgente = 20
    if XEstafador < 1 or XEstafador > 20 :
        XEstafador = random.randint(1, 20)
    if YEstafador < 1 or YEstafador > 20:
        YEstafador = random.randint(1, 20)   
        
    for f in range(1,21): #FILA
        for c in range (1,21): #COLUMNA
            pos(f+1, c)
            print("-")
    pos(XEstafador+1, YEstafador); print("E")
    pos(XAgente+1, YAgente); print("A")
    pos(24,1); print("*** El primer número dentro de los parentesis corresponde a la fila y el segundo a las columnas***")
    pos(22,1);print("-Posición del agente", (XAgente, YAgente))
    pos(23,1);print("-Posición del estafador", (XEstafador, YEstafador))
    Segundos = Segundos + 1
    input()
    
    os.system("cls")
    
    
if Segundos == 70:
    print("¡Se ha acabado el tiempo!")
    print("¡El Estafador gana!")
    print("El agente ha reccorido ", PasosA, " pasos y el estafador ha recorrido ", PasosE ," pasos.")
if XEstafador == XAgente and YEstafador == YAgente:
    print("¡El agente ha conseguido atrapar al estafador!")
    print("El agente ha reccorido ", PasosA, " pasos y el estafador ha recorrido ", PasosE ," pasos.")
input()

# Codigo bien implementado, no muestra estado del juego durante la ejecucion
# NOTA: 95-100