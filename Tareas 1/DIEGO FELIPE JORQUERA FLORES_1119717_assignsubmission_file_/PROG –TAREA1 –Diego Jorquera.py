#Miembros:
#Diego Felipe Jorquera Flores
#Franco Antonio Cadiz San Martin
#Josiel Abraham Videla Arriagada
#Felipe Danilo Menay Neira

import os
os.system( 'cls' )
import random
from win32 import win32gui
import win32con
import win32ui
from colorama import init, Fore, Back
from colorama.ansi import clear_screen
init(autoreset=True)

def clear():
    os.system( 'cls' )

def pos(x,y):
    print("\033[" +str(x) + ";" +str(y) + "H", sep="", end="")
    return None

def msn(Mensaje="",Titulo="",Tipo=0):
    return win32ui.MessageBox(Mensaje,Titulo,Tipo)

x= 1 ;y = 1 ;Contador = 0;PasoEstafador = 0;PasoAgente = 0;flag = 1;first = 0
pos(1,22);print ("1")
pos(1,42);print ("2")

Contador = 4
while Contador < 44:
    auxContador = Contador
    auxy = y
    if Contador % 2 == 0:
        if y < 10:
            pos(2,auxContador);print(auxy)
            y += 1
        else:
            y = 0
            auxy = y
            pos(2,auxContador);print(auxy)
            y += 1
    else:
        pos(2,auxContador);print(" ")
    Contador += 1

Contador2=3
while Contador2 < 23:
    auxContador2 = Contador2
    auxx = x
    if x < 10:
        pos(auxContador2,1);print (auxx,end= "  ")
        for i in range(20):print(".", end = " ")
    else:
        pos(auxContador2,1);print (auxx,end= " ")
        for i in range(20):print(".", end = " ")
    x+=1
    Contador2 += 1
R = 1
while R <= 2:
    Time = 0
    while Time < 71 and flag == 1:
        Eleccion = random.randint(0,1)
        if first == 0:
            pos(24,21);print(" ");pos(26,18);print(" ");pos(25,21);print(" ")
            AgenteX = random.randrange(3,22)
            AgenteY = random.randrange(4,42,2)
            EstafadorX = random.randrange(3,22)
            EstafadorY = random.randrange(4,42,2)
            CercaX = abs(AgenteX-EstafadorX)
            CercaY = abs(AgenteY-EstafadorY)
            while AgenteX == EstafadorX and AgenteY == EstafadorY or CercaX <= 3 and CercaY <= 8:
                AgenteX = random.randrange(3,22)
                AgenteY = random.randrange(4,42,2)
                EstafadorX = random.randrange(3,22)
                EstafadorY = random.randrange(4,42,2)
                CercaX = abs(AgenteX-EstafadorX)
                CercaY = abs(AgenteY-EstafadorY)
        first = 1
        pos(24,1);print ("Tiempo = ",Time,"segundos")
        pos(25,1);print ("Pasos Estafador = ",PasoEstafador)
        pos(26,1);print ("Pasos Agente = ",PasoAgente)


        if Eleccion == 0:
            PasoEstafador +=1
            if AgenteY < EstafadorY:
                EstafadorY += 2
            if AgenteY > EstafadorY:
                EstafadorY -=2
            if AgenteX > EstafadorX:
                EstafadorX -=1
            if AgenteX < EstafadorX:
                EstafadorX +=1
            if AgenteY == EstafadorY:
                EstafadorY = AgenteY
            if EstafadorY > 42 or EstafadorY < 3:
                EstafadorY = random.randrange(4,42,2)
                EstafadorX = random.randrange(3,22)
            if AgenteX == EstafadorX:
                EstafadorX = AgenteX
            if EstafadorX > 22 or EstafadorX < 3:
                EstafadorX = random.randrange(3,22)
                EstafadorY = random.randrange(4,42,2)
        pos(EstafadorX,EstafadorY);print (Fore.GREEN+Back.BLACK+"E")


        if Eleccion == 1:
            PasoAgente +=1
            if AgenteY < EstafadorY:
                AgenteY +=2
            if AgenteY > EstafadorY:
                AgenteY -= 2
            if AgenteY <= 4:
                AgenteY = 42
            if AgenteY > 42:
                AgenteY = 4
            if EstafadorX > AgenteX:
                AgenteX += 1
            if EstafadorX < AgenteX:
                AgenteX -= 1
            if AgenteX == EstafadorX:
                AgenteX = EstafadorX
            if AgenteY == EstafadorY:
                AgenteY = EstafadorY
        pos(AgenteX,AgenteY);print (Fore.BLUE+Back.BLACK+"A")


        Time += 1
        pos(27,1);input()
        if EstafadorY > 42 or EstafadorX > 22 or AgenteY > 42 or AgenteX > 42:
            pos(AgenteX,AgenteY);print ("");pos(EstafadorX,EstafadorY);print ("")
        else:
            pos(AgenteX,AgenteY);print (".");pos(EstafadorX,EstafadorY);print (".")
        if EstafadorY == AgenteY and AgenteX == EstafadorX:
            pos(AgenteX,AgenteY);print ("X")
            flag = 0
    if flag == 0:
        pos(27,1);print("Han atrapado al estafador.") 
        Rtn = msn("El estafador a sido atrapado, ¿Te gustaria reintentarlo?","Fin del juego",4+64)
        if Rtn == 6:
            input()
            PasoAgente=0
            PasoEstafador=0
            flag=1
            first=0
            pos(AgenteX,AgenteY);print (".")
            pos(27,1);print("                          ")
        else:
            R=3
    if Time == 71:
        pos(27,1);print("El estafador escapo.") 
        Rtn=msn("El estafador ha escapado, ¿Te gustaria reintentarlo?","Fin del juego",4+64)
        if Rtn == 6:
            input()
            PasoEstafador = 0
            PasoAgente = 0
            first = 0
            pos(27,1);print("                    ")
        else:
            R = 3


# Ejecucion correcta y funcional, exceso de contadores y variables poco representativas
# NOTA: 100