#Integrante: Sebastian Alejandro Liquitay Cerda
#Primero se proframa la representacion de la situacion para que sea vea en la pantalla
#Luego se les da la posicion al agente y al estafador
#Y se programa el juego en si con los posibles movimientos de cada sujeto
#Se finaliza con unas preguntas para conocer el resultado del juego y mostrarlo en la pantalla
import os
os.system('cls')
import random
from colorama import init, Fore , Back
init(autoreset = True)
import win32ui
def MsgBox(Mensaje="", Titulo="", Tipo=0):
    return win32ui.MessageBox(Mensaje,Titulo,Tipo)
#Cuadricula
def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None
for i in range(1,21):
    pos(i+2,1);print(i)
for j in range(1,10):
   pos(2,j+2);print(j)
pos(1,12);print(1)
pos(2,12);print(0)
for v in range(1,10):
    pos(2,v+12);print(v)
pos(1,22);print(2)
pos(2,22);print(0)
x = 3
while x <= 22:
    for k in range(1,21):
        pos(k+2,x);print(".")
    x = x + 1
# Programa del juego
fag = random.randint(3,22)
cag = random.randint(3,22)
fes = random.randint(3,22)
ces = random.randint(3,22)
while fag == fes and cag == ces or abs(fag - fes) < 2 or abs(cag - ces) < 2:
    fes = random.randint(3,22)
    ces = random.randint(3,22)
pos(fag,cag);print(Fore.GREEN + Back.BLACK + "A")
pos(fes,ces);print(Fore.RED + Back.BLACK + "E")
pos(23,1);print('Tiempo         :',0,'Segundos')
pos(24,1);print('Pasos Estafador:',0)
pos(25,1);print('Pasos Agente   :',0)
input()
seg = 0
sw = 'F'
pasesta = 0
pasag = 0
fagprev = 0
cagprev = 0
fesprev = 0
cesprev = 0
while seg < 70 and sw == 'F':
    num = random.randint(0,1)
    if num == 0:
        fesprev = fes
        cesprev = ces
        pos(fesprev,cesprev);print(".")
        if fes - fag < 0 and ces - cag < 0: # agente abajo y derecha
            fes = fes - 1 ; ces = ces - 1
            if fes < 3 or ces < 3:
                fes = random.randint(3,22)
                ces = random.randint(3,22)
        elif fes - fag < 0 and ces - cag > 0: # agente abajo e izquierda
            fes = fes -1 ; ces = ces + 1
            if fes < 3 or ces > 22:
                fes = random.randint(3,22)
                ces = random.randint(3, 22)
        elif fes - fag > 0 and ces - cag < 0: # agente arriba y derecha
            fes = fes + 1 ; ces = ces - 1
            if fes > 22 or ces < 3:
                fes = random.randint(3, 22)
                ces = random.randint(3, 22)
        elif fes - fag > 0 and ces - cag > 0: # agente arriba e izquierda
            fes = fes + 1 ; ces = ces + 1
            if fes > 22 or ces > 22:
                fes = random.randint(3, 22)
                ces = random.randint(3,22)
        elif fes == fag and ces - cag < 0: # derecha
            ces = ces - 1
            if ces < 3:
                fes = random.randint(3, 22)
                ces = random.randint(3, 22)
        elif fes == fag and ces - cag > 0 : # izquierda
            ces = ces + 1
            if ces > 22:
                fes = random.randint(3, 22)
                ces = random.randint(3, 22)
        elif fes - fag < 0 and ces == cag: # abajo
            fes = fes - 1
            if fes < 3:
                fes = random.randint(3,22)
                ces = random.randint(3, 22)
        elif fes - fag > 0 and ces == cag: # arriba
            fes = fes + 1
            if fes > 22:
                fes = random.randint(3, 22)
                ces = random.randint(3, 22)
        pasesta = pasesta + 1
    elif num == 1:
        fagprev = fag
        cagprev = cag
        pos(fagprev,cagprev);print(".")
        if cag - ces < 0 and fag - fes > 0: # estafador derecha y arriba
            cag = cag + 1 ; fag = fag - 1
            if cag > 22:
                cag = 3
            elif fag < 3:
                fag = 22
        elif cag - ces < 0 and fag - fes < 0: # estafador derecha y abajo
            cag = cag + 1 ; fag = fag + 1
            if cag > 22:
                cag = 3
            elif fag > 22:
                fag = 3
        elif cag - ces > 0 and fag - fes > 0: # estafador izquierda y arriba
            cag = cag - 1 ; fag = fag - 1
            if  cag < 3:
                cag = 22
            elif fag > 22:
                fag = 3
        elif cag - ces > 0 and fag - fes < 0: # estafador izquierda y abajo
            cag = cag - 1 ; fag = fag + 1
            if cag < 3:
                cag = 22
            elif fag > 22:
                fag = 3
        elif cag == ces and  fag - fes > 0: # arriba
            fag = fag - 1
            if fag < 3:
                fag = 22
        elif cag == ces and fag - fes < 0: # abajo
            fag = fag + 1
            if fag > 22:
                fag = 3
        elif cag - ces < 0 and fag == fes: # derecha
            cag = cag + 1
            if cag > 22:
                cag = 3
        elif cag - ces > 0 and fag == fes: # izquierda
            cag = cag - 1
            if cag < 3 :
                cag = 22
        pasag = pasag + 1
    seg = seg + 1
    pos(fes,ces);print(Fore.RED + Back.BLACK + "E")
    pos(fag,cag);print(Fore.GREEN + Back.BLACK + "A")
    pos(23,1);print('Tiempo         :',seg,'Segundos')
    pos(24,1);print('Pasos Estafador:',pasesta)
    pos(25,1);print('Pasos Agente   :',pasag)
    if fag == fes and cag == ces:
        sw = 'T'
        pos(fes,ces);print(Fore.BLUE + Back.BLACK + 'X')
    input()
if sw == 'T':
    MsgBox("Estafador atrapado, Ganaste :)", "Resultado", 0 + 64)
elif seg == 70 and sw == 'F':
    MsgBox("El estafador se escapo, Perdiste :(", "Resultado", 0 + 64)
input()


#codigo poco eficiente, completo y funcional
# NOTA: 100