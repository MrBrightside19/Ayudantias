# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:15:24 2021

@author: esteb
"""

import random
import os
from colorama import init
import colorama

"""
NOMBRES DE LOS INREGRANTES DEL GRUPO : - SEBASTIAN ALEJANDRO BARRA MONTECINOS
                                       - ESTEBAN IGNACIO GALLARDO VALDENEGRO
"""
os.system('cls')
init()
def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None

sw = 0 ; N = 0 ; X = 1 ; Y = 1 ; cont = 0 ; sw2 = 0
while sw == 0:
    pos(X,Y); print(N)
    N = N + 1
    Y = Y + 2
    cont = cont + 1
    if sw2 == 1:
        N = N - 1
        sw2 = 0
    if N == 10:
        N = 1
        sw2 = 1
    if cont == 20:
        sw = 1
        
sw = 0 ; N = 0 ; X = 1 ; Y = 1 ; cont = 0 ; sw2 = 0
while sw == 0:
    pos(X,Y); print(N)
    N = N + 1
    X = X + 1
    cont = cont + 1
    if sw2 == 1:
        N = N - 1
        sw2 = 0
    if N == 10:
        N = 1
        sw2 = 1
    if cont == 21:
        sw = 1
        
sw = 0 ; N = "-" ; X = 2 ; Y = 3 ; cont = 0 ; sw2 = 0
while sw == 0:
    pos(X,Y); print(N)
    cont = cont + 1
    Y = Y + 2
    if Y == 43:
        Y = 3
        X = X + 1
    if X == 22:
        sw = 1 
    
pos(21,1); print(20)
pos(1,41); print(20)

AGENTEXX = random.randint(2,20)
AGENTEYY = random.randint(2,40)
ESTAFADORXX = random.randint(2,20)
ESTAFADORYY = random.randint(2,40)
while abs(AGENTEXX - ESTAFADORXX) <= 2 and abs(AGENTEYY - ESTAFADORYY) <= 2:
    AGENTEXX = random.randint(2,20)
    AGENTEYY = random.randint(2,40)

if AGENTEYY % 2 == 0:
    AGENTEYY = AGENTEYY + 1
if ESTAFADORYY % 2 == 0:
    ESTAFADORYY = ESTAFADORYY + 1

pos(AGENTEXX,AGENTEYY); print("A", end="")
pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")

sw=0
seg = 0 ; contestafador = 0 ; contagente = 0
while sw==0:
    if AGENTEXX==ESTAFADORXX and AGENTEYY==ESTAFADORYY:
        sw=1
    else :
        X = random.randint(1,2)
        seg = seg + 1
        pos(23, 1); print("segundos :", seg)
        if seg == 70 :
            sw=2
    
    input()
    while X == 1 and sw == 0: #AGENTE YY HORIZONTAL - XX VERTICAL
        contagente = contagente + 1
        if AGENTEYY > ESTAFADORYY and AGENTEXX > ESTAFADORXX: # DIAGONAL <\
            AGENTEYY = AGENTEYY - 2 ; AGENTEXX = AGENTEXX - 1
            X = 0
            pos(AGENTEXX,AGENTEYY); print("A", end="")
            pos(AGENTEXX + 1,AGENTEYY + 2); print("-", end="")
        elif AGENTEYY < ESTAFADORYY and AGENTEXX < ESTAFADORXX: # DIAGONAL \>
            AGENTEYY = AGENTEYY + 2 ; AGENTEXX = AGENTEXX + 1
            X = 0
            pos(AGENTEXX - 1,AGENTEYY - 2); print("-", end="")
            pos(AGENTEXX,AGENTEYY); print("A", end="")
        elif AGENTEXX > ESTAFADORXX and AGENTEYY < ESTAFADORYY: # DIAGONAL />
            AGENTEXX = AGENTEXX - 1 ; AGENTEYY = AGENTEYY + 2
            X = 0
            pos(AGENTEXX,AGENTEYY); print("A", end="")
            pos(AGENTEXX  + 1,AGENTEYY - 2); print("-", end="")
        elif AGENTEXX < ESTAFADORXX and AGENTEYY > ESTAFADORYY: # DIAGONAL </
            AGENTEXX = AGENTEXX + 1 ; AGENTEYY = AGENTEYY - 2
            X = 0
            pos(AGENTEXX,AGENTEYY); print("A", end="")
            pos(AGENTEXX  - 1,AGENTEYY + 2); print("-", end="")
        elif AGENTEYY > ESTAFADORYY: #
            AGENTEYY = AGENTEYY - 2
            X = 0
            pos(AGENTEXX,AGENTEYY); print("A", end="")
            pos(AGENTEXX,AGENTEYY + 2); print("-", end="")
        elif AGENTEYY < ESTAFADORYY: #
            AGENTEYY = AGENTEYY + 2
            X = 0
            pos(AGENTEXX,AGENTEYY - 2); print("-", end="")
            pos(AGENTEXX,AGENTEYY); print("A", end="")
        elif AGENTEXX > ESTAFADORXX: #
            AGENTEXX = AGENTEXX - 1
            X = 0
            pos(AGENTEXX,AGENTEYY); print("A", end="")
            pos(AGENTEXX  + 1,AGENTEYY); print("-", end="")
        elif AGENTEXX < ESTAFADORXX:
            AGENTEXX = AGENTEXX + 1
            X = 0
            pos(AGENTEXX,AGENTEYY); print("A", end="")
            pos(AGENTEXX  - 1,AGENTEYY); print("-", end="")
    
    while X == 2 and sw == 0:
        contestafador = contestafador + 1
        ESTAFADORX1 = ESTAFADORXX ; ESTAFADORY1 = ESTAFADORYY
        if AGENTEYY > ESTAFADORYY and AGENTEXX > ESTAFADORXX:### DIAGONAL <\
            ESTAFADORYY = ESTAFADORYY - 2 ; ESTAFADORXX = ESTAFADORXX - 1
            X = 0
            if ESTAFADORXX < 2 or ESTAFADORXX > 21 or ESTAFADORYY < 3 or ESTAFADORYY > 41:
                pos(ESTAFADORX1,ESTAFADORY1); print("-", end="")
                ESTAFADORXX = random.randint(2,20)
                ESTAFADORYY = random.randint(2,41)
                if ESTAFADORYY % 2 == 0:
                    ESTAFADORYY = ESTAFADORYY + 1
            pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")
            pos(ESTAFADORXX + 1,ESTAFADORYY + 2); print("-", end="")
        elif AGENTEYY < ESTAFADORYY and AGENTEXX < ESTAFADORXX:### DIAGONAL \>
            ESTAFADORYY = ESTAFADORYY + 2 ; ESTAFADORXX = ESTAFADORXX + 1
            X = 0
            if ESTAFADORXX < 2 or ESTAFADORXX > 21 or ESTAFADORYY < 3 or ESTAFADORYY > 41:
                pos(ESTAFADORX1,ESTAFADORY1); print("-", end="")
                ESTAFADORXX = random.randint(2,20)
                ESTAFADORYY = random.randint(2,41)
                if ESTAFADORYY % 2 == 0:
                    ESTAFADORYY = ESTAFADORYY + 1
            pos(ESTAFADORXX - 1,ESTAFADORYY - 2); print("-", end="")
            pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")
        elif AGENTEXX > ESTAFADORXX and AGENTEYY < ESTAFADORYY:### DIAGONAL />
            ESTAFADORXX = ESTAFADORXX - 1 ; ESTAFADORYY = ESTAFADORYY + 2
            X = 0
            if ESTAFADORXX < 2 or ESTAFADORXX > 21 or ESTAFADORYY < 3 or ESTAFADORYY > 41:
                pos(ESTAFADORX1,ESTAFADORY1); print("-", end="")
                ESTAFADORXX = random.randint(2,20)
                ESTAFADORYY = random.randint(2,41)
                if ESTAFADORYY % 2 == 0:
                    ESTAFADORYY = ESTAFADORYY + 1
            pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")
            pos(ESTAFADORXX  + 1,ESTAFADORYY - 2); print("-", end="")
        elif AGENTEXX < ESTAFADORXX and AGENTEYY > ESTAFADORYY:### DIAGONAL </
            ESTAFADORXX = ESTAFADORXX + 1 ; ESTAFADORYY = ESTAFADORYY - 2
            X = 0
            if ESTAFADORXX < 2 or ESTAFADORXX > 21 or ESTAFADORYY < 3 or ESTAFADORYY > 41:
                pos(ESTAFADORX1,ESTAFADORY1); print("-", end="")
                ESTAFADORXX = random.randint(2,20)
                ESTAFADORYY = random.randint(2,41)
                if ESTAFADORYY % 2 == 0:
                    ESTAFADORYY = ESTAFADORYY + 1
            pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")
            pos(ESTAFADORXX  - 1,ESTAFADORYY + 2); print("-", end="") 
        elif AGENTEYY > ESTAFADORYY: ###
            ESTAFADORYY = ESTAFADORYY - 2
            X = 0
            if ESTAFADORYY < 2 or ESTAFADORYY > 41:
                pos(ESTAFADORX1,ESTAFADORY1); print("-", end="")
                ESTAFADORYY = random.randint(2,41)
                ESTAFADORXX = random.randint(2,20)
                if ESTAFADORYY % 2 == 0:
                    ESTAFADORYY = ESTAFADORYY + 1
            pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")
            pos(ESTAFADORXX,ESTAFADORYY + 2); print("-", end="")
            
        elif AGENTEYY < ESTAFADORYY: ###
            ESTAFADORYY = ESTAFADORYY + 2
            X = 0
            if ESTAFADORYY < 2 or ESTAFADORYY > 41:
                pos(ESTAFADORX1,ESTAFADORY1); print("-", end="")
                ESTAFADORYY = random.randint(2,41)
                ESTAFADORXX = random.randint(2,20)
                if ESTAFADORYY % 2 == 0:
                    ESTAFADORYY = ESTAFADORYY + 1
            pos(ESTAFADORXX,ESTAFADORYY - 2); print("-", end="")
            pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")
        elif AGENTEXX > ESTAFADORXX: ###
            ESTAFADORXX = ESTAFADORXX - 1
            X = 0
            if ESTAFADORXX < 2 or ESTAFADORXX > 21:
                pos(ESTAFADORX1,ESTAFADORY1); print("-", end="")
                ESTAFADORXX = random.randint(2,20)
                ESTAFADORYY = random.randint(2,41)
                if ESTAFADORYY % 2 == 0:
                    ESTAFADORYY = ESTAFADORYY + 1
            pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")
            pos(ESTAFADORXX  + 1,ESTAFADORYY); print("-", end="")
           
        elif AGENTEXX < ESTAFADORXX: ### 
            ESTAFADORXX = ESTAFADORXX + 1
            X = 0
            if ESTAFADORXX < 2 or ESTAFADORXX > 21:
                pos(ESTAFADORX1,ESTAFADORY1); print("-", end="")
                ESTAFADORXX = random.randint(2,20)
                ESTAFADORYY = random.randint(2,41)
                if ESTAFADORYY % 2 == 0:
                    ESTAFADORYY = ESTAFADORYY + 1
            pos(ESTAFADORXX,ESTAFADORYY); print("E", end="")
            pos(ESTAFADORXX  - 1,ESTAFADORYY); print("-", end="")
          
if sw==1:
    pos(25, 1); print("El agente atrapo al estafador")
elif sw==2:
    pos(25, 1); print("el estafador ha escapado")
pos(27, 1); print("El agente dio", contagente , " pasos")
pos(28, 1); print("El estafador dio", contestafador , " pasos")
input()
input()


#codigo poco legible,contador de pasos entre personajes llega hasta 69
# Ejecucion correcta Nota: 90-95