#Integrantes
#Maximiliano Ariel Gálvez Arraño
#Khrisna Ignacia González Méndez
#Dante Alejandro Catalán Uribe
#       CATCH ME IF YOU CAN ;)
from random import randint
from colorama import init, Fore, Back
import os
import cursor

os.system("cls")
init(autoreset = True)
cursor.hide()

def pos(x,y):
 print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
 return None

def coor( agente_fila, agente_columna, estafador_fila, estafador_columna, segundos, contA, contE ):
    for fil in range (2,22):
        for col in range (2,22):
            pos(fil,col*3)
            print(Fore.WHITE + "○")
            pos(20,20)
            
    for fil in range (2,22):
        pos(fil,1)
        print(Fore.LIGHTGREEN_EX + str(fil - 1))
      
    for col in range (2,22):
        pos(1,col*3)
        print(Fore.LIGHTGREEN_EX + str(col - 1))
   
    pos((estafador_fila + 1),(estafador_columna + 1)*3)
    print(Back.RED + Fore.WHITE + "E")

    pos((agente_fila + 1),(agente_columna + 1)*3)
    print(Back.BLUE + Fore.WHITE + "A")

    pos(2,66)
    print("Tiempo                : ", segundos,"segundos")
    
    pos(3,66)
    print("Pasos del Estafador   : ", contE)
    
    pos(4,66)
    print("Pasos del Agente      : ", contA)
    
    pos (23, 24);                     print("▄▀")
    
    pos (25, 2);print("░█▀▀█ ▀▀█▀▀ ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ▒█▀▀▀   ▒█▀▀▀█ ▀█▀   ▒█▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀▀█ ")
    pos (26, 2);print("▒█▄▄█ ░▒█░░ ▒█▄▄▀ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ▒█▒█▒█ ▒█▀▀▀   ░▀▀▀▄▄ ▒█░   ▒█▄▄█ ▒█░▒█ ▒█▀▀▀ ▒█░▒█ ▒█▀▀▀ ░▀▀▀▄▄ ")
    pos (27, 2);print("▒█▒░█ ░▒█░░ ▒█░▒█ ▒█░▒█ ▒█░░░ ▒█░▒█ ▒█░░▒█ ▒█▄▄▄   ▒█▄▄▄█ ▄█▄   ▒█░░░ ░▀▄▄▀ ▒█▄▄▄ ▒█▄▄▀ ▒█▄▄▄ ▒█▄▄▄█")
    
    pos (10,66);print("─────────██────────────────██────")
    pos (11,66);print("───────▄▀█▄▄▄───────────▄▀█▄▄▄▄── ")
    pos (12,66);print("─────▄▀──█▄▄─────────▄▀──█▄▄──── ")
    pos (13,66);print("──────▄▄▄▀──▀▄────────▄▄▄▀───▀▄── ")
    pos (14,66);print("──────▀───────▀▀──────▀────────▀▀ ")
  
    if agente_fila == estafador_fila and agente_columna == estafador_columna:
        pos((estafador_fila + 1),(estafador_columna + 1)*3)
        print(Back.YELLOW + Fore.WHITE + "X")

        pos(16,66);print(" El estafador ha sido capturado")
        pos(18,71);       print(" (⌐■_■) ╦╤─ (╥ n ╥)")
        pos (50, 50);print('uwu')


    if segundos == 70 :
        pos((estafador_fila + 1),(estafador_columna + 1)*3)
        print("○")

        pos(16,69);print(" El estafador logró escapar")
        pos(18, 78);          print(" (•̀ᴗ•́) ")
        pos (100, 100);print('uwu')
        
#########################     PROGRAMA PRINCIPAL     #########################
segundos = 0; contA = 0; contE = 0
estafador_fil = randint(1,20) 
estafador_col = randint(1,20) 
agente_fil = randint(1,20) 
agente_col = randint(1,20) 

while ((agente_fil == estafador_fil) and (agente_col == estafador_col) )   and   (abs(estafador_fil - agente_fil) < 3) or (abs(estafador_col - agente_col) < 3):
    agente_fil = randint(1,20)
    agente_col = randint(1,20)
    
while segundos <= 70:
    
    coor( agente_fil, agente_col, estafador_fil, estafador_col, segundos, contA, contE )
    
    if agente_fil == estafador_fil and agente_col == estafador_col:
        segundos = 71

    input()
    boton = randint(0,1)
    if boton == 1 :
        if  agente_col > estafador_col:
            agente_col = agente_col - 1
        elif agente_col < estafador_col:
            agente_col = agente_col + 1
            
        if  agente_fil > estafador_fil:
            agente_fil = agente_fil - 1
        elif agente_fil < estafador_fil:
            agente_fil = agente_fil + 1
            
        contA += 1
    else:
        if  estafador_col > agente_col:
            estafador_col = estafador_col + 1
        elif estafador_col < agente_col:
            estafador_col = estafador_col - 1
            
        if  estafador_fil > agente_fil:
            estafador_fil = estafador_fil + 1    
        elif estafador_fil < agente_fil:
            estafador_fil = estafador_fil - 1
            
        contE += 1
        if (estafador_fil == 0) or (estafador_fil == 21) :
            estafador_fil = randint(1,20)
            estafador_col = randint(1,20)
        elif (estafador_col == 0) or (estafador_col == 21): 
            estafador_fil = randint(1,20)
            estafador_col = randint(1,20)
    
    segundos = segundos + 1
    pos(1,30)
input()

# Codigo perfecto, buen diseño y buena ejecucion. Felicidades
# NOTA: 100