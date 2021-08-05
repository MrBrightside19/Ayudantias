# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#INTEGRANTES:
#Cristian Salinas Ríos
#Bastián Flores Díaz
#Benjamín Morales Núñez

import os
from colorama import init, Fore, Back
init(autoreset = True)
import random 
def pos(x,y):
 print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
 return None
def Mapa() :
     pos(3, 2); print("1 * * * * * * * * * * * * * * * * * * * *")   
     pos(4, 2); print("2 * * * * * * * * * * * * * * * * * * * *")
     pos(5, 2); print("3 * * * * * * * * * * * * * * * * * * * *") 
     pos(6, 2); print("4 * * * * * * * * * * * * * * * * * * * *")
     pos(7, 2); print("5 * * * * * * * * * * * * * * * * * * * *") 
     pos(8, 2); print("6 * * * * * * * * * * * * * * * * * * * *")
     pos(9, 2); print("7 * * * * * * * * * * * * * * * * * * * *") 
     pos(10, 2); print("8 * * * * * * * * * * * * * * * * * * * *")
     pos(11, 2); print("9 * * * * * * * * * * * * * * * * * * * *")
     pos(12, 1); print("10 * * * * * * * * * * * * * * * * * * * *")     
     pos(13, 1); print("11 * * * * * * * * * * * * * * * * * * * *")
     pos(14, 1); print("12 * * * * * * * * * * * * * * * * * * * *")
     pos(15, 1); print("13 * * * * * * * * * * * * * * * * * * * *")
     pos(16, 1); print("14 * * * * * * * * * * * * * * * * * * * *")
     pos(17, 1); print("15 * * * * * * * * * * * * * * * * * * * *")
     pos(18, 1); print("16 * * * * * * * * * * * * * * * * * * * *")
     pos(19, 1); print("17 * * * * * * * * * * * * * * * * * * * *")
     pos(20, 1); print("18 * * * * * * * * * * * * * * * * * * * *")
     pos(21, 1); print("19 * * * * * * * * * * * * * * * * * * * *")
     pos(22, 1); print("20 * * * * * * * * * * * * * * * * * * * *")
     # horizontal 
     pos(2, 4); print("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0")
     pos(1, 4); print("                  1                   2")
AgenteX = random.randint(3,22)
AgenteY = random.randint(4,42)
EstafadorX = random.randint(3,22)
EstafadorY = random.randint(4,42)
Sw = 0
while Sw == 0 :
    if AgenteY%2 != 0 :
        AgenteY = random.randint(4,42)
    else:
        Sw = 1
Sw = 0
while Sw == 0 :
    if EstafadorY%2 != 0 :
        EstafadorY = random.randint(4,42)
    else:
        Sw = 1
Sw = 0            
if AgenteX < EstafadorX or EstafadorX < AgenteX :
    while Sw == 0 :
        if abs(AgenteX - EstafadorX) <= 2 : 
            EstafadorX = random.randint(3,22) 
        else : 
            Sw = 1 
Sw = 0 
if AgenteY < EstafadorY or EstafadorY < AgenteY :
    while Sw == 0 : 
        if abs(AgenteY - EstafadorY) <= 2 : 
            EstafadorY = random.randint(4,42)
        else:
            Sw = 1 
    
os.system("cls")
Segundos = 0; PasosA = 0; PasosE = 0; Sw = 0
while Segundos < 70 and Sw == 0 :
    MovAzar = random.randint(1,2)
    if MovAzar == 1:
        #Movimientos del Estafador 
        if AgenteX < EstafadorX:       
            EstafadorX = EstafadorX + 1
        if AgenteX > EstafadorX:
            EstafadorX = EstafadorX - 1
        if AgenteY < EstafadorY:
            EstafadorY = EstafadorY + 2
        if AgenteY > EstafadorY:
            EstafadorY = EstafadorY - 2
        #Movimiento al azar del Estafador si sobrepasa los límites    
        if EstafadorY > 42:
            EstafadorY = random.randint(4,42)
            while EstafadorY%2 != 0 :
                EstafadorY = random.randint(4,42)
            EstafadorX = random.randint(3,22)
        if EstafadorY < 4:
            EstafadorY = random.randint(4,42)
            while EstafadorY%2 != 0 :
                EstafadorY = random.randint(4,42)
            EstafadorX = random.randint(3,22)
        if EstafadorX > 22:
            EstafadorY = random.randint(4,42)
            while EstafadorY%2 != 0 :
                EstafadorY = random.randint(4,42)
            EstafadorX = random.randint(3,22)
        if EstafadorX < 3:
            EstafadorY = random.randint(4,42)
            while EstafadorY%2 != 0 :
                EstafadorY = random.randint(4,42)
            EstafadorX = random.randint(3,22)
        PasosE = PasosE + 1
        
    if MovAzar == 2:
        #Movimientos del Agente
        if EstafadorX < AgenteX:
            AgenteX = AgenteX - 1
        if EstafadorX > AgenteX:
            AgenteX = AgenteX + 1
        if EstafadorY < AgenteY:
            AgenteY = AgenteY - 2
        if EstafadorY > AgenteY:
            AgenteY = AgenteY + 2
        #Movimientos del agente si sobrepasa los límites    
        if AgenteX > 22:
            AgenteX = 3
        if AgenteX < 3:
            AgenteX = 22
        if AgenteY > 42:
            AgenteY = 4
        if AgenteY < 4:
            AgenteY = 42
        PasosA = PasosA + 1 
    Mapa()    
    Segundos = Segundos + 1 
    if AgenteX == EstafadorX and AgenteY == EstafadorY : 
        pos(AgenteX,AgenteY); print(Back.YELLOW + Fore.WHITE + "X", end="")
        Sw = 1
    else:
            pos(AgenteX, AgenteY);  print(Back.GREEN + Fore.WHITE + "A", end="")
            pos(EstafadorX, EstafadorY); print(Back.RED + Fore.WHITE + "E", end="")
  
    pos(24,1); print("Tiempo: ", Segundos)
    pos(26,1); print("Pasos del agente: ", PasosA)    
    pos(28,1); print("Pasos del Estafador:", PasosE)
    if Segundos == 70 :
        pos(30,1); print("El Estafador logró escapar!")
    if Sw == 1 :
        pos(30,1); print("El Estafador ha sido capturado!")
    input()
    os.system("cls")


# Cumple con la ejecucion, validaciones poco eficientes pero funcionales
# NOTA:90-100