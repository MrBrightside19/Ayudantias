# -*- coding: utf-8 -*-
"""
Buenos días profesor, espero esté bien, quería comentarle que por motivos personales decidí
realizar el trabajo solo, espero su comprensión, saludos cordiales, muchas gracias por su atención

@author: Vicente Páez
"""
##IMPORTACIONES##
from colorama import init, Fore, Back
init(autoreset = True)
import os
import random
import colorama
colorama.init()

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None

## Primera ubicación de "A" (agente) y "E" (estafador), donde "Y" representa la columna Vertical y "X" la fila Horizontal#
SW = 0
XE = int(random.randrange(20) + 1)
YE = int(random.randrange(20) + 1)
SW = 0
while SW == 0:
    SW = 1
    XA = int(random.randrange(20) + 1)
    if XA == XE + 2 or XA == XE + 1 or XA == XE:
        SW = 0
    elif XA == XE - 2 or XA == XE - 1 or XA == XE:
        SW = 0
SW1 = 0
while SW1 == 0:
     SW1 = 1
     YA = int(random.randrange(20) + 1)
     if YA == YE + 2 or YA == YE + 1 or YA == YE:
         SW1 = 0
     elif YA == YE - 2 or YA == YE - 1 or YA == YE:
         SW1 = 0
pos(1,1); print("el Estafador está en ", XE, ",",YE," y el Agente está en", XA, ",",YA)
## juego ##

Seg = 0; Atrapado = False; PasosEst = 0; PasosAge = 0
while Seg < 70 and Atrapado == False:
    ## TABLERO ###
    # horizontal superior
    pos(2,2); print("_") 
    pos(2,3); print("_")
    pos(2,4); print("_")
    pos(2,5); print("_")
    pos(2,6); print("_")
    pos(2,7); print("_")
    pos(2,8); print("_")
    pos(2,9); print("_")
    pos(2,10); print("_")
    pos(2,11); print("_")
    pos(2,12); print("_")
    pos(2,13); print("_")
    pos(2,14); print("_")
    pos(2,15); print("_")
    pos(2,16); print("_")
    pos(2,17); print("_")
    pos(2,18); print("_")
    pos(2,19); print("_")
    pos(2,20); print("_")
    pos(2,21); print("_")
    pos(2,22); print("_")
    pos(2,23); print("_")
    pos(2,24); print("_")
    
    # vertical izquierda
    pos(3,2); print("|")
    pos(4,2); print("|")
    pos(5,2); print("|")
    pos(6,2); print("|")
    pos(7,2); print("|")
    pos(8,2); print("|")
    pos(9,2); print("|")
    pos(10,2); print("|")
    pos(11,2); print("|")
    pos(12,2); print("|")
    pos(13,2); print("|")
    pos(14,2); print("|")
    pos(15,2); print("|")
    pos(16,2); print("|")
    pos(17,2); print("|")
    pos(18,2); print("|")
    pos(19,2); print("|")
    pos(20,2); print("|")
    pos(21,2); print("|")
    pos(22,2); print("|")
    
    # vertical derecha
    pos(3,24); print("|")
    pos(4,24); print("|")
    pos(5,24); print("|")
    pos(6,24); print("|")
    pos(7,24); print("|")
    pos(8,24); print("|")
    pos(9,24); print("|")
    pos(10,24); print("|")
    pos(11,24); print("|")
    pos(12,24); print("|")
    pos(13,24); print("|")
    pos(14,24); print("|")
    pos(15,24); print("|")
    pos(16,24); print("|")
    pos(17,24); print("|")
    pos(18,24); print("|")
    pos(19,24); print("|")
    pos(20,24); print("|")
    pos(21,24); print("|")
    pos(22,24); print("|")
    
    # horizontal inferior
    pos(23,2); print("_")
    pos(23,3); print("_")
    pos(23,4); print("_")
    pos(23,5); print("_")
    pos(23,6); print("_")
    pos(23,7); print("_")
    pos(23,8); print("_")
    pos(23,9); print("_")
    pos(23,10); print("_")
    pos(23,11); print("_")
    pos(23,12); print("_")
    pos(23,13); print("_")
    pos(23,14); print("_")
    pos(23,15); print("_")
    pos(23,16); print("_")
    pos(23,17); print("_")
    pos(23,18); print("_")
    pos(23,19); print("_")
    pos(23,20); print("_")
    pos(23,21); print("_")
    pos(23,22); print("_")
    pos(23,23); print("_")
    pos(23,24); print("_")
    
    Var = int(random.randrange(2))
    # si es el turno del agente
    if Var == 0 :
        if XE > XA:
            XA = XA + 1
        elif XE < XA:
            XA = XA - 1
        if YE > YA:
            YA = YA + 1
        elif YE < YA:
            YA = YA - 1
        PasosAge = PasosAge + 1
    # si es el turno del estafador
    if Var == 1:
         if XE != XA:
              if XE > XA:
                  XE = XE + 1
              elif XE < XA:
                  XE = XE - 1
         if YE != YA:
             if YE > YA:
                 YE = YE + 1
             elif YE < YA:
                 YE = YE - 1
         
         PasosEst = PasosEst + 1
    #Si el estafador sale del tablero
    if XE > 20 or XE <= 0 or YE > 20 or YE <= 0:
        XE = int(random.randrange(20) + 1)
        YE = int(random.randrange(20) + 1)
    #Si el agente sale del tablero#
    if XA > 20:
        XA = 1
    elif XA <= 0:
        XA = 20
    if YA > 20:
        YA = 1
    elif YA <= 0:
        YA = 20

    print("el Estafador está en ", YE, ",",XE," y el Agente está en", YA, ",",XA)
    pos(YA + 2, XA + 2); print(Back.GREEN + Fore.WHITE + "A", end="")
    pos(YE + 2, XE + 2); print(Back.RED + Fore.WHITE + "E", end="")
    Seg = Seg + 1
    pos(25,1); print("Tiempo transcurrido: ", Seg, " Segundos")
    #si el estafador es atrapado
    if XA == XE and YA == YE:
        Atrapado = True
        pos(YA + 2, XA + 2); print(Back.BLUE + Fore.WHITE + "X", end="")
    input()
    os.system("cls")
## FIN DEL JUEGO ##
print("    FIN DEL JUEGO")
if Atrapado == True:
    print("El estafador ha sido capturado")
    print("Tiempo: ", Seg,  "Segundos")
    print("Pasos del Agente: ", PasosAge, " pasos")
    print("Pasos del Estafador: ", PasosEst, " pasos")
else:
    print("El estafador logró escapar")
    print("Tiempo: ", Seg,  "Segundos")
    print("Pasos del Agente: ", PasosAge, " pasos")
    print("Pasos del Estafador: ", PasosEst, " pasos")
input()


#Variables poco representativas, ejecucion funcional, Buen codigo
# NOTA: 100