# -*- coding: utf-8 -*-
#Integrantes: Facundo Aguillón Aravalo
#             Angelo Alvarez Guerrero
#             Camilo Alvarez Escobar
import time
import random
import os
from colorama import init, Fore, Back, Style
init()

def pos(x,y):
 print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
 return None

pillado = 0
tiempo = 0
pasosAgente = 0
pasosEstafador = 0
posXagente = random.randint(0, 19)
posYagente = random.randint(0, 19)
posXEstafa = random.randint(0, 19)
posYEstafa = random.randint(0, 19)
x = random.randint(0, 21)
y = random.randint(0, 21)
Agente = "A"
Estafador = "E"

while(True):
    posXEstafa = random.randint(0, 19)
    posYEstafa = random.randint(0, 19)
    if((posXagente != posXEstafa) and (posYagente != posYEstafa) and ((posYagente - 1  and posYagente - 2 and posYagente + 1 and posYagente + 2) != posYEstafa ) and ((posXagente - 1  and posXagente - 2 and posXagente + 1 and posXagente + 2) != posXEstafa)):
        break
    
while(tiempo < 70):
    movimiento = random.randint(0, 1)
    if(movimiento == 1):
        if(posXEstafa > posXagente):
            posXagente += 1
        if(posXEstafa < posXagente):
            posXagente -= 1
        if(posXagente > 20):
            posXagente = 0
        if(posXagente < 0):
            posXagente = 20
        if(posYagente > 20):
            posYagente = 0
        if(posYagente < 0):
            posYAgente = 20
        pasosAgente += 1
   
    if(posXEstafa == posXagente and posYEstafa == posYagente):
        pillado = 1
        break
    if(movimiento == 0):
        if(posXagente < posXEstafa):
            posXEstafa += 1
        if(posXagente > posXEstafa):
            posXEstafa -= 1
        if(posXEstafa > 20 or posXEstafa < 0 or posYEstafa > 20 or posYEstafa < 0):
            posXEstafa = random.randint(0, 19)
            posYEstafa = random.randint(0, 19)
        pasosEstafador += 1
        tiempo += 1
        pos(x, y) ; print(Agente, Back.RED + Fore.WHITE, end="")
        pos(x, y) ; print(Estafador, Back.BLUE + Fore.WHITE, end="")
if(pillado == 1):
    print("El estafador ha sido capturado")
else:
    print("El estafador logró escapar")
    
print("Tiempo Transcurrido:",tiempo)
print("Pasos Estafador:",pasosEstafador)
print("Pasos Agente:",pasosAgente)

input()

# Codigo no funcional, no muestra tablero, solo movimiento en consola, sin validacion
# Nota 0 pendiente