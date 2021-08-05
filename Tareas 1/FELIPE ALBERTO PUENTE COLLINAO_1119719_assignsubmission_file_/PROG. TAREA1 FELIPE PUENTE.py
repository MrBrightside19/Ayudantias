"""
INTEGRANTES:FELIPE ALBERTO PUENTE COLLINAO
            DANIEL ESTEBAN GARRIDO GONZALEZ
            NATALIA PAULINA ALVIAL DIAZ
            
COMENTARIOS DEL PROGRAMA:
Vemos que las coordenadas no sean iguales y que esten a una distancia mayor de 2
si prota == 1 entonces se mueve el estafador
si prota == 2 entonces se mueve el agente
procuramos que no salgan de los bordes
si el agente atrapa al estafador entonces el programa termina gracias a un switch
si pasan de 70 pasos y no es atrapado el estafador entonces el programa termina

"""
import os
import colorama
colorama.init(autoreset = True)

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None

import random
segundos = 0
switch = 0
pasosA = 0
pasosE = 0

filaA = random.randint(1,20)
columnaA = random.randint(1,20)
filaE = random.randint(1,20)
columnaE = random.randint(1,20)

while abs(filaA - filaE) <= 2 and abs(columnaA - columnaE) <= 2:
    filaE = random.randint(1,20)
    columnaE = random.randint(1,20)
    
while segundos < 70 and switch == 0:
    segundos = segundos + 1
    prota = random.randint(1,2)
    if prota == 1:
        pasosE = pasosE + 1
        if columnaA < columnaE:
            columnaE = columnaE + 1
            if columnaE > 20:
                columnaE = random.randint(1,20)
                filaE = random.randint(1,20)
        elif columnaA > columnaE:
            columnaE = columnaE - 1
            if columnaE < 1:
                columnaE = random.randint(1,20)
                filaE = random.randint(1,20)
        elif columnaA == columnaE:
            columnaE = columnaE
            
        if filaA < filaE:
            filaE = filaE + 1
            if filaE > 20:
                columnaE = random.randint(1,20)
                filaE = random.randint(1,20)
        elif filaA > filaE:
            filaE = filaE - 1
            if filaE < 1:
                columnaE = random.randint(1,20)
                filaE = random.randint(1,20)
        elif filaA == filaE:
            filaE = filaE
            
    if prota == 2:
        pasosA = pasosA + 1
        if columnaA < columnaE:
            columnaA = columnaA + 1
            if columnaA > 20:
                columnaA = 1
        elif columnaA > columnaE:
            columnaA = columnaA - 1
            if columnaA < 1:
                columnaA = 20
        elif columnaA == columnaE:
            columnaA = columnaA
        
        if filaA < filaE:
            filaA = filaA + 1
            if filaA > 20:
                filaA = 1
        elif filaA > filaE:
            filaA = filaA - 1
            if filaA < 1:
                filaA = 20
        elif filaA == filaE:
            filaA == filaA
    
    if filaA == filaE and columnaA == columnaE:
        switch = 1
        pos(filaE,columnaE); print("X")
        
    pos(filaA,columnaA); print(colorama.Fore.BLUE + "A")
    pos(filaE,columnaE); print(colorama.Fore.RED + "E")
    input()
    os.system("cls")

pos(21,21);
if switch == 1:
    print("El estafador ha sido capturado")
if segundos >= 70 :
    print("El estafador logro escapar")
print("La persecucion fue de ",segundos, " segundos")
print("El estafador dio un total de ",pasosE," pasos")
print("El agente dio un total de ",pasosA," pasos")

input("FIN DEL PROGRAMA")

    
# No implementa estado durante el desarrollo, tablero nose visualiza
#Nota: 80-90


'''
POSIBLE COPIA
Josthin Ahumada Barrera
Kathalinna Cáceres Torres
Nicolás Vásquez Donoso
'''