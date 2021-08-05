# -*- coding: utf-8 -*-
"""
Created on Fri Jun 4 13:10:39 2021

@author:Sebastian Jerez

Integrantes: Sebastian Jerez
             Maria Jose Alballay
"""

import os
from colorama import init, Fore, Back, Style
from random import randint
import winsound
init(autoreset=True)

init()
os.system('cls')

eay = 2
eax = 2

# def beep1():
#     winsound.Beep(200,250)
# def beep2():
#     winsound.Beep(400,250)

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None
def GeneracionMapa():
    pos(1,31) ; print("1")
    pos(1,61) ; print("2")
    pos(2,4) ; print("1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9  0")
    
    j = 3
    for i in range(1,21):
        if i < 10:
            pos(j,2) ; print(i)
        else:
            pos(j,1) ; print(i)
        j = j + 1
    
    for j in range(3,23):
        cont = 4
        while cont < 64:
            pos(j,cont) ; print(".")
            cont = cont + 3
def GeneracionRandomEstafador():
    global xe,ye,pxe,pye
    xe = randint(3,22)
    ye1 = randint(0,19)
    ye = 4
    for i in range(0,ye1):
        if ye1 == 0:
            ye = 4
        else:
            ye = ye + 3
    pos(xe,ye) ; print(Back.RED + "E")
    pxe = xe
    pye = ye

def GeneracionRandomAgente():
    global xa,ya,pxa,pya
    aay = 2
    aax = 2
    pos(aax,aay) ; print(".")
    xa = randint(3,22)
    ya1 = randint(0,19)
    ya = 4
    for j in range(0,ya1):
        if ya1 == 0:
            ya = 4
        else:
            ya = ya + 3
    while  abs(xa - pxe) <= 2  and  abs(ya - pye) <= 6:
        xa = randint(3,22)
        ya1 = randint(0,19)
        ya = 4
        for j in range(0,ya1):
            if ya1 == 0:
                ya = 4
            else:
                ya = ya + 3
    pos(xa,ya) ; print(Back.BLUE + "A")
    pxa = xa
    pya = ya
def MovimientoEstafador():
    global eax,eay,xe,ye
    if ye != ya and xe != xa:
        if xe >= 22 or xe <= 3 or ye >= 61 or ye <= 4:
            pos(pxe,pye) ; print(".")
            pos(eax,eay) ; print(".")
            GeneracionRandomEstafador()
            eax = xe
            eay = ye
        else:
            if ye < ya and xe < xa:
                pos(pxe,pye) ; print(".")
                pos(eax,eay) ; print(".")
                xe = xe - 1
                ye = ye - 3
                pos(xe,ye) ; print(Back.RED + "E")
                eax = xe
                eay = ye
            if ye < ya and xe > xa:
                pos(pxe,pye) ; print(".")
                pos(eax,eay) ; print(".")
                xe = xe + 1
                ye = ye - 3
                pos(xe,ye) ; print(Back.RED + "E")
                eax = xe
                eay = ye
            if ye > ya and xe < xa:
                pos(pxe,pye) ; print(".")
                pos(eax,eay) ; print(".")
                xe = xe - 1
                ye = ye + 3
                pos(xe,ye) ; print(Back.RED + "E")
                eax = xe
                eay = ye
            if ye > ya and xe > xa:
                pos(pxe,pye) ; print(".")
                pos(eax,eay) ; print(".")
                xe = xe + 1
                ye = ye + 3
                pos(xe,ye) ; print(Back.RED + "E")
                eax = xe
                eay = ye

    else:
        if ya == ye:
            if xa < xe:
                if xe >= 22:
                    pos(pxe,pye) ; print(".")
                    pos(eax,eay) ; print(".")
                    GeneracionRandomEstafador()
                    eax = xe
                    eay = ye
                else:
                    xe = xe + 1
                    pos(pxe,pye) ; print(".")
                    pos(eax,eay) ; print(".")
                    pos(xe,ye) ; print(Back.RED + "E")
                    eax = xe
                    eay = ye
            else:
                if xe <= 3:
                    pos(pxe,pye) ; print(".")
                    pos(eax,eay) ; print(".")
                    GeneracionRandomEstafador()
                    eax = xe
                    eay = ye
                else:
                    xe = xe - 1
                    pos(pxe,pye) ; print(".")
                    pos(eax,eay) ; print(".")
                    pos(xe,ye) ; print(Back.RED + "E")
                    eax = xe
                    eay = ye
                #######
        else:
            if ya < ye:
                if ye >= 61:
                    pos(eax,eay) ; print(".")
                    pos(pxe,pye) ; print(".")
                    GeneracionRandomEstafador()
                    eax = xe
                    eay = ye
                else:
                    ye = ye + 3
                    pos(pxe,pye) ; print(".")
                    pos(eax,eay) ; print(".")
                    pos(xe,ye) ; print(Back.RED + "E")
                    eax = xe
                    eay = ye
            else:
                if ye <= 4:
                    pos(eax,eay) ; print(".")
                    pos(pxe,pye) ; print(".")
                    GeneracionRandomEstafador()
                    eax = xe
                    eay = ye
                else:
                    ye = ye - 3
                    pos(pxe,pye) ; print(".")
                    pos(eax,eay) ; print(".")
                    pos(xe,ye) ; print(Back.RED + "E")
                    eax = xe
                    eay = ye
def MovimientoAgente():
    global ya,xa,aay,aax
    if ye != ya and xe != xa:
        if ye > ya and xe > xa:
            pos(pxa,pya) ; print(".")
            pos(aax,aay) ; print(".")
            xa = xa + 1
            ya = ya + 3
            pos(xa,ya) ; print(Back.BLUE + "A")
            aax = xa
            aay = ya
        if ye < ya and xe > xa:
            pos(pxa,pya) ; print(".")
            pos(aax,aay) ; print(".")
            xa = xa + 1
            ya = ya - 3
            pos(xa,ya) ; print(Back.BLUE + "A")
            aax = xa
            aay = ya
        if ye < ya and xe < xa:
            pos(pxa,pya) ; print(".")
            pos(aax,aay) ; print(".")
            xa = xa - 1
            ya = ya - 3
            pos(xa,ya) ; print(Back.BLUE + "A")
            aax = xa
            aay = ya
        if ye > ya and xe < xa:
            pos(pxa,pya) ; print(".")
            pos(aax,aay) ; print(".")
            xa = xa - 1
            ya = ya + 3
            pos(xa,ya) ; print(Back.BLUE + "A")
            aax = xa
            aay = ya
    else:
        if ye == ya:
            if xe < xa:
                if xa >= 22:
                    pos(aax,aay) ; print(".")
                    pos(pxa,pya) ; print(".")
                    xa = 4
                    pos(xa,ya) ; print(Back.BLUE + "A")
                    aax = xa
                    aay = ya
                else:
                    xa = xa - 1
                    pos(pxa,pya) ; print(".")
                    pos(aax,aay) ; print(".")
                    pos(xa,ya) ; print(Back.BLUE + "A")
                    aax = xa
                    aay = ya
            else:
                if xa <= 4:
                    pos(aax,aay) ; print(".")
                    pos(pxa,pya) ; print(".")
                    xa = 23
                    pos(xa,ya) ; print(Back.BLUE + "A")
                    aax = xa
                    aay = ya
                else:
                    xa = xa + 1
                    pos(pxa,pya) ; print(".")
                    pos(aax,aay) ; print(".")
                    pos(xa,ya) ; print(Back.BLUE + "A")
                    aax = xa
                    aay = ya
                #######  
        else:
            if ye < ya:
                if ya >= 61:
                    pos(aax,aay) ; print(".")
                    pos(pxa,pya) ; print(".")
                    ya = 4
                    pos(xa,ya) ; print(Back.BLUE + "A")
                    aax = xa
                    aay = ya
                else:
                    ya = ya - 3
                    pos(pxa,pya) ; print(".")
                    pos(aax,aay) ; print(".")
                    pos(xa,ya) ; print(Back.BLUE + "A")
                    aax = xa
                    aay = ya
            else:
                if ya <= 4:
                    pos(aax,aay) ; print(".")
                    pos(pxa,pya) ; print(".")
                    ya = 61
                    pos(xa,ya) ; print(Back.BLUE + "A")
                    aax = xa
                    aay = ya
                else:
                    ya = ya + 3
                    pos(pxa,pya) ; print(".")
                    pos(aax,aay) ; print(".")
                    pos(xa,ya) ; print(Back.BLUE + "A")
                    aax = xa
                    aay = ya
                    
#PROGRAMA PRINCIPAL

GeneracionMapa()
GeneracionRandomEstafador()
GeneracionRandomAgente()
contagente = 0
contestafa = 0
cont = 0
pos(24,3) ; print("Pasos del Agente: ",contagente)
pos(25,3) ; print("Pasos del Estafador: ",contestafa)
pos(26,3) ; print("Segundos Transcurridos: ",cont)
aax = 2
aay = 2
sw1 = 0
while cont <= 69 and sw1 == 0:
    turno = randint(1,2)
    if turno == 1:
        MovimientoEstafador()
        # beep1()
        contestafa = contestafa + 1
        pos(25,3) ; print("Pasos del Estafador: ",contestafa)
    else:
        MovimientoAgente()
        # beep2()
        contagente = contagente + 1
        pos(24,3) ; print("Pasos del Agente: ",contagente)
    if xa == xe and ya == ye:
        sw1 = 1
        pos(xa,ya) ; print(Back.YELLOW + "X")
        
    cont = cont + 1
    pos(26,3) ; print("Segundos Transcurridos: ",cont)
    a = input()

os.system ("cls") 
if sw1 == 0:
    print('         .                                                      . ')
    print('        .n                   .                 .                  n. ')
    print('  .   .dP                  dP                   9b                 9b. ')
    print(' 4    qXb         .       dX                     Xb       .        dXp     t ')
    print('dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb ')
    print('9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP ')
    print(' 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP ')
    print("  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP' ")
    print("    `9XXXXXXXXXXXP' `9XX'   GANA    `98v8P' ESTAFADOR `XXP' `9XXXXXXXXXXXP' ")
    print('        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~ ')
    print("                        )b.  .dbo.dP'`v'`9b.odb.  .dX( ")
    print('                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb. ')
    print("                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb ")
    print('                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb ')
    print("                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP ")
    print("                     `'      9XXXXXX(   )XXXXXXP      `' ")
    print("                              XXXX X.`v'.X XXXX ")
    print("                              XP^X'`b   d'`X^XX ")
    print("      ")
    print("Gano el estafador Debido a que el agente no lo alcanzo en 70 segundos")
    # for i in range(1,4):
        # winsound.Beep(150,500)
        # winsound.Beep(150,500)
        # winsound.Beep(100,1000)
else:
    print('         .::::::::::.        -(_)====u         .::::::::::. ')
    print("       .::::''''''::::.                      .::::''''''::::. ")
    print("    .:::'          `::::....          ....::::'          `:::. ")
    print("    .::'             `:::::::|        |:::::::'             `::. ")
    print("   .::|               |::::::|_ ___ __|::::::|               |::. ")
    print("   `--'     GANA      |::::::|_()__()_|::::::|     AGENTE    `--' ")
    print("    :::               |::-o::|        |::o-::|               ::: ")
    print("    `::.             .|::::::|        |::::::|.             .::' ")
    print("     `:::.          .::\-----'        `-----/::.          .:::' ")
    print("       `::::......::::'                      `::::......::::' ")
    print("         `::::::::::'                          `::::::::::' ")
    print("      ")
    print("Gano el agente Debido a que atrapo al estafador antes de 70 segundos")
    # for i in range(1,4):
        # winsound.Beep(260,1000)
        # winsound.Beep(200,1000)   

input()


# Codigo completo y funcional, biblioteca de sonidos implementadas y con fallos
# se comenta codigo para revisar ejecucion
# Nota: 100