# -*- coding: utf-8 -*-
"""
TRABAJO 1. LABORATORIO DE PROGRAMACION. PARALELO 300
Integrantes:
    - Braulio Andrés Navarro Guzmán
    - Pablo Ignacio Rojas Zavala
    - John Gabler Hidalgo Carrasco
    - Danilo Fernando Valenzuela Vergara
"""

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None
 
def crearEspacio():
    import os 
    os.system('cls')
    for i in range (1, 21):
        for j in range(2,41,2):
            pos(i,j); print(".")
    for i in range(1,21):
        pos(i,42); print(f"{i}")
    cont=1
    for j in range(2,41,2):
        pos(21,j); print(f"{cont}")
        cont +=1
 
def posicionarPersonajes():
    global EstafadorX, EstafadorY, AgenteX, AgenteY
    from random import randint
    import colorama
    colorama.init()
    
    AgenteX = randint(1,20)
    AgenteY = randint(1, 20)*2
    pos(AgenteX,AgenteY); print(colorama.Back.BLUE+"A")
    
    EstafadorX = randint(1,20)
    EstafadorY = randint(1,20)*2
    while abs(AgenteX - EstafadorX) < 3 and abs(AgenteY - EstafadorY < 3):
        EstafadorX = randint(1,20)
        EstafadorY = randint(1,20)*2
    pos(EstafadorX,EstafadorY); print(colorama.Back.RED+"E")
    
def moverPersonaje():
    global EstafadorX, EstafadorY, AgenteX, AgenteY, PasosAg, PasosEs
    from random import randint
    import colorama
    colorama.init()
    opcion = randint(0,1)
    if opcion == 0:
        #AGENTE
        PasosAg += 1
        pos(AgenteX, AgenteY); print(colorama.Back.BLACK+".")
        if EstafadorX - AgenteX < 0:
            AgenteX -= 1
            if AgenteX == 0:
                AgenteX = 20
        elif EstafadorX - AgenteX == 0:
            AgenteX = AgenteX
        else:
            AgenteX += 1
            if AgenteX == 21:
                AgenteX = 1
            
        if EstafadorY - AgenteY < 0:
            AgenteY -= 2
            if AgenteY == 0:
                AgenteY = 40
        elif EstafadorY - AgenteY == 0:
            AgenteY = AgenteY
        else:
            AgenteY += 2
            if AgenteY == 42:
                AgenteY = 1
        pos(AgenteX, AgenteY); print(colorama.Back.BLUE+"A")
        
    else:
        #ESTAFADOR
        PasosEs += 1
        pos(EstafadorX, EstafadorY); print(colorama.Back.BLACK+".")
        if EstafadorX - AgenteX < 0:
            EstafadorX -= 1
            if EstafadorX == 0:
                EstafadorX = randint(1,20)
                EstafadorY = randint(1,20)*2
        elif EstafadorX - AgenteX == 0:
            EstafadorX = EstafadorX
        else:
            EstafadorX += 1
            if EstafadorX == 21:
                EstafadorX = randint(1,20)
                EstafadorY = randint(1,20)*2
            
        if EstafadorY - AgenteY < 0:
            EstafadorY -= 2
            if EstafadorY == 0:
                EstafadorX = randint(1,20)
                EstafadorY = randint(1,20)*2
        elif EstafadorY - AgenteY == 0:
            EstafadorY = EstafadorY
        else:
            EstafadorY += 2
            if EstafadorY == 42:
                EstafadorX = randint(1,20)
                EstafadorY = randint(1,20)*2
        pos(EstafadorX, EstafadorY); print(colorama.Back.RED+"E")

def comprobarVictoria():
    global tiempo
    import colorama
    colorama.init()
    if EstafadorX == AgenteX and EstafadorY == AgenteY:
        pos(EstafadorX,EstafadorY); print(colorama.Back.YELLOW+"X")
        pos(25,1); print(colorama.Back.BLACK+'El estafador fue capturado.')
        return True
    if tiempo == 70:
        pos(25,1); print(colorama.Back.BLACK+'El estafador a logrado escapar.')
        return True
        
def simulacion():
    global tiempo, PasosAg, PasosEs
    tiempo = 0; PasosAg = 0; PasosEs = 0
    import colorama
    colorama.init()
    crearEspacio()
    posicionarPersonajes()
    SW_Programa = True
    pos(22,1); print(colorama.Back.BLACK+f'Ha pasado {tiempo} segundos.')
    pos(23,1); print(colorama.Back.BLACK+f'Agente se ha movido {PasosAg}')
    pos(24,1); print(colorama.Back.BLACK+f'Estafador se ha movido {PasosEs}')
    while SW_Programa == True:
        input()
        moverPersonaje()
        tiempo += 1
        pos(22,1); print(colorama.Back.BLACK+f'Ha pasado {tiempo} segundos.')
        pos(23,1); print(colorama.Back.BLACK+f'Agente se ha movido {PasosAg}')
        pos(24,1); print(colorama.Back.BLACK+f'Estafador se ha movido {PasosEs}')

        if comprobarVictoria() == True:
            SW_Programa = False
            input()

#INICIO PROGRAMA
simulacion()

# Codigo funciona correctamente, bien utilizados los modulos, ordenado y legible
# NOTA: 100
# BIBLIOTECAS SE IMPORTAN SOLO UNA VEZ AL PRINCIPIO

