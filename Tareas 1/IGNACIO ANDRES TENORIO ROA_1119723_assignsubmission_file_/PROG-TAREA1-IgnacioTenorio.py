# -*- coding: utf-8 -*-
"""
Tarea Numero 1
Paralelo 301

integrantes : Ignacio Andres Tenorio Roa 
              Sebastian Ignacio Santander Machuca
              Tomas Ignacio Cisternas Jorquera


"""
import os
os.system("cls")

import random

from colorama import init, Fore, Back, Style
init(autoreset = True)

def pos(y,x):
    print("\033[" +str(y) + ";" + str(x) + "H", sep="", end="")
    

import win32ui
def MsgBox(Mensaje="", Titulo="", Tipo=0):
 return win32ui.MessageBox(Mensaje,Titulo,Tipo)

# variables 
numx = 0 ; numx2 = "" ; numy = 1
Yestafador = 1 ; Yagente = 1
Xestafador = 1 ; Xagente = 1
SW = 0 ; SW2 = 0 ; SW3= 5
Tiempo = 0
Cagente = 0 ; Cestafador = 0

# creacion del tablero 

for  a in range(0,21):
    if a > 9:
        numx2 = "1"
        if a == 20:
            numx2 = "2"
    else:
        numx2 = " "
    print(numx2,end="  ")    
    
print()
        
for  a in range(0,21):
    print(numx, end="  ")
    numx = int(numx) + 1
    if a == 19:
        numx = "0"
    if int(numx) > 9:
        numx = "0"
        
print()

for a in range(0,20):
     print(numy)
     numy= numy+1
     
     
# ubicacion estafador y agente, luego sus movimientos
while SW == 0 :
    pos(Yagente+2,Xagente*3+1); print(Back.BLACK + Fore.BLACK +"A")
    pos(Yestafador+2,Xestafador*3+1); print(Back.BLACK + Fore.BLACK +"E")
    pos(25, 1)    ;print(Back.BLACK + Fore.BLACK + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    pos(27, 1)    ;print(Back.BLACK + Fore.BLACK + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    
    
    
    
    
    
    
    while SW2 == 0 : 
       Xestafador = random.randint(1, 20) ;  Yestafador = random.randint(1,20)
       Xagente = random.randint(1, 20)  ; Yagente = random.randint(1,20) 
       while  abs(Xagente - Xestafador) <= 2  and  abs(Yagente - Yestafador) <= 2  : 
           Xagente  = random.randint(1, 20)  ; Yagente  = random.randint(1, 20) 
           if abs(Xagente - Xestafador) >= 2  and  abs(Yagente - Yestafador) >= 2  :
               SW2 = 1
            
    if SW2 == 1 and Tiempo > 0:
        SW3 = random.randrange(1,3)
        
    if SW3 == 1:
        if Xestafador == Xagente and Yestafador > Yagente:
            Yestafador = Yestafador + 1
        if Xestafador == Xagente and Yestafador < Yagente:
            Yestafador = Yestafador - 1
        if Yestafador == Yagente and Xestafador > Xagente:
            Xestafador = Xestafador + 1
        if Yestafador == Yagente and Xestafador < Xagente:
             Xestafador = Xestafador - 1
        if Xestafador > Xagente and Yestafador > Yagente:
            Xestafador = Xestafador + 1 ; Yestafador = Yestafador + 1
        if Xestafador < Xagente and Yestafador < Yagente:
            Xestafador = Xestafador - 1 ; Yestafador = Yestafador - 1
        if Xestafador > Xagente and Yestafador < Yagente:
            Xestafador = Xestafador + 1 ; Yestafador = Yestafador - 1
        if Xestafador < Xagente and Yestafador > Yagente:
            Xestafador = Xestafador - 1 ; Yestafador = Yestafador + 1
        if Xestafador >= 21 or Yestafador >= 21 or Xestafador <= 0 or Yestafador <= 0 :
             Xestafador = random.randint(1, 20) ;  Yestafador = random.randint(1,20)
        Cestafador = Cestafador + 1
    
    if SW3 == 2:
        if Xestafador == Xagente and Yestafador > Yagente:
            Yagente = Yagente + 1
        if Xestafador == Xagente and Yestafador < Yagente:
            Yagente = Yagente - 1 
        if Yestafador == Yagente and Xestafador > Xagente:
            Xagente = Xagente + 1   
        if Yestafador == Yagente and Xestafador < Xagente:
            Xagente = Xagente - 1
        if Xestafador > Xagente and Yestafador > Yagente:
            Xagente = Xagente + 1 ; Yagente = Yagente + 1
        if Xestafador < Xagente and Yestafador < Yagente:
            Xagente = Xagente - 1 ; Yagente = Yagente - 1
        if Xestafador > Xagente and Yestafador < Yagente:
            Xagente = Xagente + 1 ; Yagente = Yagente - 1
        if Xestafador < Xagente and Yestafador > Yagente:
            Xagente = Xagente - 1 ; Yagente = Yagente + 1
        if Xagente >= 21 :
            Xagente = 1
        if Xagente <= 0 :
            Xagente = 20 
        if Yagente >= 21:
            Yagente = 1 
        if Yagente <= 0:
            Yagente = 20
        Cagente = Cagente + 1
        
        
            
        
      
    pos(Yagente+2,Xagente*3+1); print(Back.RED + Fore.WHITE +"A")
    pos(Yestafador+2,Xestafador*3+1); print(Back.BLUE + Fore.WHITE +"E")
    
    pos(25, 1)    ;print("la ubicacion del agente es : ", Xagente,",", Yagente,"")
    pos(26, 1)    ;print("la ubicacion del estafador es : ", Xestafador,",",Yestafador,"")
    pos(27, 1)    ;print("el tiempo transcurrido es :", Tiempo)
    pos(28, 1)    ;print("la cantidad de pasos del estafador son: ", Cestafador)
    pos(29, 1)    ;print("la cantidad de pasos del agente son: ", Cagente)
    
    Tiempo = Tiempo + 1
    
    if Tiempo >= 70:
        SW = 1
    if Xagente == Xestafador and Yagente == Yestafador:
        SW = 2
    
    pos(1, 1)    ;input()

# resultado final
    
if SW == 1:
    MsgBox("el estafador logro escapar", "programa finalizado", 1 + 64) 
    
if SW == 2 :
    MsgBox("el agente atrapo al estafador", "programa finalizado", 1 + 64) 
   
    
input()

# Codigo funcional, implementa coordenadas pero no tablero como tal, cumple
# con los requisitos. NOTA: 100
    