"""
integrantes: 
Javiera Farias (paralelo 301)
Jonas Gonzalez (paralelo 300)
Franz Quiroz   (paralelo 301)
"""

import os
os.system('cls')
from random import *
import colorama
from colorama import init
init(autoreset=True)
def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", end="")
    return None

a_columna    = randint(1,20)
a_fila       = randint(1,20)
e_columna    = randint(1,20)
e_fila       = randint(1,20)

while (a_columna == e_columna and a_fila == e_fila):
    a_columna    = randint(1,20)
    a_fila       = randint(1,20)
    e_columna    = randint(1,20)
    e_fila       = randint(1,20) 

sw2 = 0
while sw2 == 0 :
    if (a_fila < e_fila + 2 and a_fila > e_fila - 2 ) and (a_columna < e_columna + 2 and a_columna > e_columna - 2):
        e_fila = randint(1,20)
        e_columna = randint(1,20)
        a_fila = randint(1,20)
        a_columna = randint(1,20)
    else :
        sw2 = 1

for x in range (20):
    for y in range (20):
        print("+", end="")
    print("\n", end="")

pos(1,21); print(colorama.Fore.YELLOW +" 1")
pos(2,21); print(colorama.Fore.YELLOW +" 2")
pos(3,21); print(colorama.Fore.YELLOW +" 3")
pos(4,21); print(colorama.Fore.YELLOW +" 4")
pos(5,21); print(colorama.Fore.YELLOW +" 5")
pos(6,21); print(colorama.Fore.YELLOW +" 6")
pos(7,21); print(colorama.Fore.YELLOW +" 7")
pos(8,21); print(colorama.Fore.YELLOW +" 8")
pos(9,21); print(colorama.Fore.YELLOW +" 9")
pos(10,21); print(colorama.Fore.YELLOW +" 10")
pos(11,21); print(colorama.Fore.YELLOW +" 11")
pos(12,21); print(colorama.Fore.YELLOW +" 12")
pos(13,21); print(colorama.Fore.YELLOW +" 13")
pos(14,21); print(colorama.Fore.YELLOW +" 14")
pos(15,21); print(colorama.Fore.YELLOW +" 15")
pos(16,21); print(colorama.Fore.YELLOW +" 16")
pos(17,21); print(colorama.Fore.YELLOW +" 17")
pos(18,21); print(colorama.Fore.YELLOW +" 18")
pos(19,21); print(colorama.Fore.YELLOW +" 19")
pos(20,21); print(colorama.Fore.YELLOW +" 20")

pos(21,1); print(colorama.Fore.YELLOW +"1 ")
pos(21,2); print(colorama.Fore.YELLOW +"2 ")
pos(21,3); print(colorama.Fore.YELLOW +"3 ")
pos(21,4); print(colorama.Fore.YELLOW +"4 ")
pos(21,5); print(colorama.Fore.YELLOW +"5 ")
pos(21,6); print(colorama.Fore.YELLOW +"6 ")
pos(21,7); print(colorama.Fore.YELLOW +"7 ")
pos(21,8); print(colorama.Fore.YELLOW +"8 ")
pos(21,9); print(colorama.Fore.YELLOW +"9 ")
pos(21,10); print(colorama.Fore.YELLOW +"1 ")
pos(22,10); print(colorama.Fore.YELLOW +"0 ")
pos(21,11); print(colorama.Fore.YELLOW +"1 ")
pos(21,12); print(colorama.Fore.YELLOW +"2 ")
pos(21,13); print(colorama.Fore.YELLOW +"3 ")
pos(21,14); print(colorama.Fore.YELLOW +"4 ")
pos(21,15); print(colorama.Fore.YELLOW +"5 ")
pos(21,16); print(colorama.Fore.YELLOW +"6 ")
pos(21,17); print(colorama.Fore.YELLOW +"7 ")
pos(21,18); print(colorama.Fore.YELLOW +"8 ")
pos(21,19); print(colorama.Fore.YELLOW +"9 ")
pos(21,20); print(colorama.Fore.YELLOW +"2 ")
pos(22,20); print(colorama.Fore.YELLOW +"0 ")

input()
tiempo = 0 ; a_pasos = 0 ; e_pasos = 0 ; sw = 0
while tiempo < 70 and sw == 0:
    turno = randint(1,2)
    os.system('cls')

    for x in range (20):
        for y in range (20):
            print("+", end="")
        print("\n", end="")

    pos(1,21); print(colorama.Fore.YELLOW +" 1")
    pos(2,21); print(colorama.Fore.YELLOW +" 2")
    pos(3,21); print(colorama.Fore.YELLOW +" 3")
    pos(4,21); print(colorama.Fore.YELLOW +" 4")
    pos(5,21); print(colorama.Fore.YELLOW +" 5")
    pos(6,21); print(colorama.Fore.YELLOW +" 6")
    pos(7,21); print(colorama.Fore.YELLOW +" 7")
    pos(8,21); print(colorama.Fore.YELLOW +" 8")
    pos(9,21); print(colorama.Fore.YELLOW +" 9")
    pos(10,21); print(colorama.Fore.YELLOW +" 10")
    pos(11,21); print(colorama.Fore.YELLOW +" 11")
    pos(12,21); print(colorama.Fore.YELLOW +" 12")
    pos(13,21); print(colorama.Fore.YELLOW +" 13")
    pos(14,21); print(colorama.Fore.YELLOW +" 14")
    pos(15,21); print(colorama.Fore.YELLOW +" 15")
    pos(16,21); print(colorama.Fore.YELLOW +" 16")
    pos(17,21); print(colorama.Fore.YELLOW +" 17")
    pos(18,21); print(colorama.Fore.YELLOW +" 18")
    pos(19,21); print(colorama.Fore.YELLOW +" 19")
    pos(20,21); print(colorama.Fore.YELLOW +" 20")

    pos(21,1); print(colorama.Fore.YELLOW +"1 ")
    pos(21,2); print(colorama.Fore.YELLOW +"2 ")
    pos(21,3); print(colorama.Fore.YELLOW +"3 ")
    pos(21,4); print(colorama.Fore.YELLOW +"4 ")
    pos(21,5); print(colorama.Fore.YELLOW +"5 ")
    pos(21,6); print(colorama.Fore.YELLOW +"6 ")
    pos(21,7); print(colorama.Fore.YELLOW +"7 ")
    pos(21,8); print(colorama.Fore.YELLOW +"8 ")
    pos(21,9); print(colorama.Fore.YELLOW +"9 ")
    pos(21,10); print(colorama.Fore.YELLOW +"1 ")
    pos(22,10); print(colorama.Fore.YELLOW +"0 ")
    pos(21,11); print(colorama.Fore.YELLOW +"1 ")
    pos(21,12); print(colorama.Fore.YELLOW +"2 ")
    pos(21,13); print(colorama.Fore.YELLOW +"3 ")
    pos(21,14); print(colorama.Fore.YELLOW +"4 ")
    pos(21,15); print(colorama.Fore.YELLOW +"5 ")
    pos(21,16); print(colorama.Fore.YELLOW +"6 ")
    pos(21,17); print(colorama.Fore.YELLOW +"7 ")
    pos(21,18); print(colorama.Fore.YELLOW +"8 ")
    pos(21,19); print(colorama.Fore.YELLOW +"9 ")
    pos(21,20); print(colorama.Fore.YELLOW +"2 ")
    pos(22,20); print(colorama.Fore.YELLOW +"0 ")

    #agente
    if turno == 1 :
        if a_fila > e_fila and a_columna > e_columna :
            a_fila = a_fila - 1
            a_columna = a_columna - 1 
        elif a_fila > e_fila and a_columna < e_columna :
            a_fila = a_fila - 1
            a_columna = a_columna + 1 
        elif a_fila < e_fila and a_columna > e_columna :
            a_fila = a_fila + 1
            a_columna = a_columna - 1 
        elif a_fila < e_fila and a_columna < e_columna :
            a_fila = a_fila + 1
            a_columna = a_columna + 1 
        elif a_fila == e_fila and a_columna > e_columna :
            a_columna = a_columna - 1 
        elif a_fila == e_fila and a_columna < e_columna :
            a_columna = a_columna + 1 
        elif a_fila > e_fila and a_columna == e_columna :
            a_fila = a_fila - 1
        elif a_fila < e_fila and a_columna == e_columna :
            a_fila = a_fila + 1

        a_pasos = a_pasos +1

    if a_columna > 20 :
        a_columna = 1

    if a_columna < 1 :
        a_columna = 20

    if a_fila > 20 : 
        a_fila = 1

    if a_fila < 1 : 
        a_fila = 20
    

    #estafador 
    if turno == 2 : 
        if e_fila > a_fila and e_columna > a_columna :
            e_fila = e_fila + 1 
            e_columna = e_columna + 1 
        elif e_fila > a_fila and e_columna < a_columna : 
            e_fila = e_fila + 1 
            e_columna = e_columna - 1 
        elif e_fila < a_fila and e_columna > a_columna : 
            e_fila = e_fila - 1 
            e_columna = e_columna + 1 
        elif e_fila < a_fila and e_columna < a_columna :
            e_fila = e_fila - 1 
            e_columna = e_columna - 1 
        elif e_fila == a_fila and e_columna > a_columna :
            e_columna = e_columna + 1 
        elif e_fila == a_fila and e_columna < a_columna :
            e_columna = e_columna - 1 
        elif e_fila > a_fila and e_columna == a_columna :
            e_fila = e_fila + 1
        elif e_fila < a_fila and e_columna == a_columna : 
            e_fila = e_fila - 1 

        if e_fila > 20 or e_fila < 1 or e_columna > 20 or e_columna < 1 :
            e_columna   = randint(1,20)
            e_fila      = randint(1,20)
        e_pasos = e_pasos + 1

    pos(a_fila ,a_columna); print(colorama.Back.RED + colorama.Fore.WHITE + "A")
    pos(e_fila ,e_columna); print(colorama.Back.GREEN + colorama.Fore.WHITE +"E")
    
    tiempo = tiempo + 1 
    pos(24,1);print(colorama.Fore.YELLOW + "Tiempo: ",tiempo)
    pos(25,1);print(colorama.Fore.GREEN + "Pasos Del Estafador: ",e_pasos)
    pos(26,1);print(colorama.Fore.RED + "Pasos Del Agente: ",a_pasos)
    input()
    
    if a_columna == e_columna and a_fila == e_fila :
        sw = 1

if a_columna == e_columna and a_fila == e_fila :
    pos(27,1);print(colorama.Back.BLUE + colorama.Fore.WHITE + "Estafador ha sido capturado.")

elif tiempo >= 70 :
    pos(27,1);print(colorama.Back.BLUE + colorama.Fore.WHITE + "El estafador ha escapado.")



input()

#Vuelve a ubicar a ambos personajes cuando estan cerca, no a uno, 
# NOTA : 80 - 90

